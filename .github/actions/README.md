# Composite Actions

Reusable composite actions for GitHub workflows in this repository. These actions follow the DRY (Don't Repeat Yourself) principle and provide consistent behavior across multiple workflows.

---

## 📦 Available Actions

### 1. Fork Safety Check

**Path**: `.github/actions/fork-safety/`

**Purpose**: Detects if a pull request originates from a forked repository and sets appropriate permissions to prevent unauthorized write operations.

**Why It's Important**:
- Prevents security risks from fork contributions
- Automatically restricts write operations (comments, labels, branch deletion) for fork PRs
- Allows read-only operations (validation, testing) to continue normally

**Outputs**:
- `is-fork`: Boolean indicating if PR is from a fork
- `should-skip-writes`: Boolean indicating if write operations should be skipped

**Usage Example**:
```yaml
- name: Check fork status
  id: fork-check
  uses: ./.github/actions/fork-safety

- name: Post comment
  if: steps.fork-check.outputs.should-skip-writes != 'true'
  run: |
    gh pr comment ${{ github.event.pull_request.number }} \
      --body "Review completed!"
```

**How It Works**:
Compares `github.event.pull_request.head.repo.full_name` with `github.repository` to determine if the PR source is a fork.

---

### 2. Quality Gates

**Path**: `.github/actions/quality-gates/`

**Purpose**: Runs comprehensive code quality checks (linting, type-checking, testing, YAML validation) with graceful fallback when tools or scripts are missing.

**Why It's Important**:
- Ensures consistent code quality across all PRs
- Gracefully handles missing tools or configuration
- Skills Factory specific: validates YAML files in `generated-skills/`
- Prevents broken code from being merged

**Inputs**:
- `skip-lint`: Skip linting check (default: `false`)
- `skip-typecheck`: Skip type checking (default: `false`)
- `skip-tests`: Skip tests (default: `false`)

**Outputs**:
- `lint-passed`: Whether lint check passed
- `typecheck-passed`: Whether type check passed
- `tests-passed`: Whether tests passed
- `all-passed`: Whether all quality gates passed

**What It Checks**:

1. **Linting** (`npm run lint`):
   - Skips if no `package.json` exists
   - Skips if no `lint` script defined
   - Fails PR if linting errors found

2. **Type Checking** (TypeScript):
   - Tries `npm run type-check`, `npm run typecheck`, or `npx tsc --noEmit`
   - Skips if no `tsconfig.json` exists
   - Fails PR if type errors found

3. **Testing** (`npm test`):
   - Skips if no `package.json` exists
   - Skips if no real test script (detects placeholder like `echo "No tests"`)
   - Fails PR if tests fail

4. **YAML Validation** (Skills Factory Specific):
   - Validates YAML files in `generated-skills/` directory
   - Uses `yamllint` with relaxed configuration
   - Skips if `yamllint` not installed
   - Validates up to 10 files for performance

**Usage Example**:
```yaml
- name: Run quality checks
  id: quality
  uses: ./.github/actions/quality-gates
  with:
    skip-lint: 'false'
    skip-typecheck: 'false'
    skip-tests: 'false'

- name: Verify all passed
  if: steps.quality.outputs.all-passed != 'true'
  run: |
    echo "Quality gates failed"
    exit 1
```

**Advanced Usage** (Skip specific checks):
```yaml
# Skip type-check for documentation PRs
- name: Quality gates for docs
  uses: ./.github/actions/quality-gates
  with:
    skip-typecheck: 'true'
    skip-tests: 'true'
```

**Exit Behavior**:
- Uses `continue-on-error: true` for each step
- Always produces outputs (passed/failed)
- Final summary step fails if any check failed
- Graceful fallback: missing tools/scripts = passed ✅

---

### 3. Branch Cleanup

**Path**: `.github/actions/branch-cleanup/`

**Purpose**: Automatically deletes merged branches and posts confirmation comment to maintain a clean repository.

**Why It's Important**:
- Prevents branch clutter in repository
- Automates manual cleanup task
- Protects important branches from accidental deletion
- Only deletes branches that are actually merged (not just closed)

**Inputs**:
- `github-token`: GitHub token for API operations (required)
- `skip-cleanup`: Skip cleanup (for forks or manual control, default: `false`)

**Outputs**:
- `cleaned`: Whether branch was deleted
- `branch-name`: Name of the deleted branch

**What It Does**:

1. **Verification**:
   - Checks if event is a merged PR (not just closed)
   - Verifies branch name is available
   - Skips if `skip-cleanup` is `true`

2. **Protection**:
   - Never deletes protected branches: `main`, `dev`, `release/*`
   - Validates branch pattern before deletion

3. **Deletion**:
   - Uses GitHub API to delete branch reference
   - Posts confirmation comment on PR
   - Handles errors gracefully (already deleted, protected)

4. **Confirmation**:
   - Posts comment: "🧹 **Branch Cleanup**: Automatically deleted merged branch `feature/xyz`"
   - Non-critical: If comment fails, cleanup still succeeds

**Usage Example**:
```yaml
# Trigger on PR close
on:
  pull_request:
    types: [closed]

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - name: Delete merged branch
        uses: ./.github/actions/branch-cleanup
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

**With Fork Safety**:
```yaml
- name: Check fork status
  id: fork-check
  uses: ./.github/actions/fork-safety

- name: Clean up branch
  uses: ./.github/actions/branch-cleanup
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    skip-cleanup: ${{ steps.fork-check.outputs.should-skip-writes }}
```

**Protected Branches**:
The action automatically skips deletion for:
- `main` (production branch)
- `dev` (development branch)
- `release/*` (release branches)

**Edge Cases Handled**:
- ✅ PR closed but not merged → No deletion
- ✅ Branch already deleted → Silent success
- ✅ Protected branch pattern → Skip with warning
- ✅ Fork PR → Skip if `skip-cleanup=true`
- ✅ API failure → Graceful failure without blocking workflow

---

## 🔧 Development Guidelines

### Creating a New Composite Action

1. **Create Directory**:
   ```bash
   mkdir -p .github/actions/your-action-name
   ```

2. **Create action.yml**:
   ```yaml
   name: Your Action Name
   description: Brief description of what it does

   inputs:
     input-name:
       description: Input description
       required: true
       default: 'default-value'

   outputs:
     output-name:
       description: Output description
       value: ${{ steps.step-id.outputs.output-name }}

   runs:
     using: composite
     steps:
       - name: Step name
         id: step-id
         shell: bash
         run: |
           echo "Your bash commands here"
   ```

3. **Key Principles**:
   - ✅ Use `shell: bash` for all steps
   - ✅ Always set outputs using `>> $GITHUB_OUTPUT`
   - ✅ Use `continue-on-error: true` for graceful degradation
   - ✅ Check for prerequisites before running commands
   - ✅ Provide clear echo messages for logging
   - ✅ Handle edge cases explicitly

4. **Testing**:
   - Test in a real PR workflow
   - Test with missing tools/configuration
   - Test fork vs. non-fork scenarios
   - Test error conditions

### Best Practices

**Graceful Degradation**:
```yaml
- name: Optional check
  continue-on-error: true
  run: |
    if ! command -v tool &> /dev/null; then
      echo "⏭️  Tool not installed - skipping"
      exit 0
    fi
    # Run actual check
```

**Clear Logging**:
```yaml
run: |
  echo "🔍 Running validation..."
  if [ condition ]; then
    echo "✅ Validation passed"
  else
    echo "❌ Validation failed"
    exit 1
  fi
```

**Input Validation**:
```yaml
- name: Validate inputs
  run: |
    if [ -z "${{ inputs.required-input }}" ]; then
      echo "❌ Error: required-input is missing"
      exit 1
    fi
```

**Safe API Calls**:
```yaml
- name: API call
  env:
    GH_TOKEN: ${{ inputs.github-token }}
  run: |
    if gh api /endpoint 2>/dev/null; then
      echo "✅ API call succeeded"
    else
      echo "⚠️  API call failed (non-critical)"
    fi
```

---

## 📚 Related Documentation

- **Workflow Adaptation Plan**: `WORKFLOW_ADAPTATION_PLAN.md`
- **Branch Protection**: `.github/BRANCH_PROTECTION_CONFIG.md`
- **Implementation Timeline**: `.github/WORKFLOW_IMPLEMENTATION_TRACKER.md`
- **GitHub Workflows**: `.github/workflows/`

---

## 🔄 Version History

**v1.0.0** (November 13, 2025):
- Initial release with three composite actions
- Fork safety detection
- Quality gates with graceful fallback
- Branch cleanup automation

---

**Maintained by**: Claude Code Skills Factory Team
**Last Updated**: November 13, 2025
