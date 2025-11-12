# GitHub Workflow Adaptation Plan

**Project**: Claude Code Skills Factory
**Blueprint Source**: `/Users/rezarezvani/projects/claudecode-github-bluprint`
**Date**: November 12, 2025
**Status**: Planning Phase

---

## 🎯 Objective

Adapt the GitHub workflow blueprint to create an automated, Claude Code-integrated branching and PR workflow for the Skills Factory repository that:

1. ✅ Enforces clear branch naming conventions
2. ✅ Prevents direct pushes to `main`
3. ✅ Routes all PRs through `dev` branch
4. ✅ Auto-creates branches from issues
5. ✅ Integrates Claude Code reviews (@claude)
6. ✅ Auto-merges and cleans up after approval
7. ✅ Auto-switches back to `dev` before next task

---

## 📊 Current State vs. Desired State

### Current Workflow Problems

| Issue | Impact | Example |
|-------|--------|---------|
| **No branch naming convention** | Inconsistent branches | `fix/psychology-advisor-link` (unclear) |
| **Direct pushes to main** | Bypasses review process | Recent commits went straight to main |
| **No automated branch creation** | Manual git commands needed | Developer creates branches manually |
| **No PR automation** | Manual PR creation and cleanup | No auto-merge, no auto-delete |
| **No Claude Code review integration** | Missing automated reviews | Reviews done manually |
| **Manual branch management** | Forgot to switch back to dev | Stayed on feature branch |

### Desired Workflow (Blueprint-Based)

```
1. Create GitHub Issue
   ↓
2. Label with 'claude-code' + 'status:ready'
   ↓
3. **AUTO**: Branch created (feature/issue-123-clear-name)
   ↓
4. Developer works on branch
   ↓
5. /commit-smart (quality checks + secrets scan)
   ↓
6. /create-pr (auto-links issue, adds labels)
   ↓
7. **AUTO**: PR validation (branch name, title, quality gates)
   ↓
8. Tag @claude for review
   ↓
9. **AUTO**: Claude Code review posted
   ↓
10. After approval → **AUTO**: Merge to dev
   ↓
11. **AUTO**: Delete source branch
   ↓
12. **AUTO**: Switch to dev branch
   ↓
13. Ready for next task
```

---

## 🏗️ Blueprint Patterns to Adopt

### Pattern 1: Branch Naming Convention

**From Blueprint**: `{type}/issue-{number}-{slug}`

**Types**:
- `feature/` - New features (default)
- `fix/` - Bug fixes
- `hotfix/` - Critical production fixes
- `refactor/` - Code refactoring
- `test/` - Test additions
- `docs/` - Documentation changes

**Example**:
```
Issue #42: "Add AWS Solution Architect Skill"
Branch: feature/issue-42-add-aws-solution-architect-skill
```

**Enforcement**:
- ✅ `pr-into-dev.yml` validates branch names
- ❌ PRs with invalid names are rejected
- 📝 Helpful error message shows correct format

---

### Pattern 2: Branching Strategy

**Blueprint Strategy**: `feature → dev → main`

**Rules**:
1. **Base Branch**: All feature branches created from `dev`
2. **PR Target**: All feature PRs target `dev` (not `main`)
3. **Release Flow**: Only `dev` can merge to `main`
4. **Hotfix Exception**: `hotfix/*` can merge to `main` directly (emergency only)

**Current Branches**:
- `main` - Production releases only
- `dev` - Active development (new base branch)
- `feature/*` - Individual features (auto-created from issues)
- `hotfix/*` - Emergency fixes (manual creation)

**Migration**:
```bash
# Create dev branch from current main
git checkout main
git pull origin main
git checkout -b dev
git push -u origin dev

# Set dev as default branch in GitHub Settings
# Protect both main and dev branches
```

---

### Pattern 3: Auto-Branch Creation

**Workflow**: `create-branch-on-issue.yml`

**Trigger**:
```yaml
on:
  issues:
    types: [labeled]
```

**Logic**:
1. Issue labeled with both `claude-code` + `status:ready`
2. Extract issue number and title
3. Detect branch type from labels (`type:fix`, `type:feature`, etc.)
4. Create slug from title (sanitize, kebab-case, max 50 chars)
5. Build branch name: `{type}/issue-{number}-{slug}`
6. Create branch from `dev` (or custom base via `base:` label)
7. Post comment with checkout instructions
8. Update project board status to "In Progress"

**Example Comment**:
```markdown
## 🌿 Branch Created

Your feature branch is ready!

```bash
git fetch origin
git checkout feature/issue-42-add-aws-solution-architect-skill
```

**Next steps**:
1. Make your changes
2. Run `/commit-smart` to commit with quality checks
3. Run `/create-pr` to create pull request
```

**Benefits**:
- ✅ Consistent naming (no human error)
- ✅ Auto-linked to issue
- ✅ Clear instructions for developers
- ✅ Project board auto-updated

---

### Pattern 4: PR Validation (dev branch)

**Workflow**: `pr-into-dev.yml`

**Validations**:
1. **Branch Name** - Must match `^(feature|fix|hotfix|test)/`
2. **PR Title** - Must follow conventional commits format
3. **Issue Linking** - At least one issue must be referenced
4. **Quality Gates** - Lint, tests, type-check must pass
5. **Fork Safety** - Read-only for fork PRs

**Conventional Commit Types**:
```
feat: New feature
fix: Bug fix
docs: Documentation changes
style: Code style (formatting, etc.)
refactor: Code refactoring
perf: Performance improvements
test: Adding/updating tests
build: Build system changes
ci: CI/CD changes
chore: Other changes
```

**Example PR Titles**:
```
✅ feat(skills): add AWS Solution Architect skill
✅ fix(prompts): correct validation rule in prompt factory
✅ docs: update README with new slash commands
❌ Add new skill (missing type)
❌ Fixed bug (no conventional format)
```

**Auto-Comment on Failure**:
```markdown
## ❌ Invalid PR Title

Your PR title doesn't follow the conventional commit format.

**Required format:** `<type>(<scope>): <subject>`

**Example:** `feat(skills): add AWS Solution Architect skill`
```

---

### Pattern 5: Release Gates (main branch)

**Workflow**: `dev-to-main.yml`

**Allowed Sources**:
- ✅ `dev` - Production releases (standard flow)
- ✅ `release/*` - Emergency hotfix releases
- ❌ `feature/*`, `fix/*`, `test/*` - Must merge to dev first

**Production Gates**:
1. **Production Build** - Must build successfully with `NODE_ENV=production`
2. **Build Artifacts** - Verify dist/, build/, out/, .next/ exists
3. **Smoke Tests** - Run quick sanity tests
4. **Security Scan** - Basic secret scanning (informational)

**Error Message for Invalid Source**:
```
❌ Invalid source branch: feature/issue-42-add-aws-skill

Only dev and release/* branches may be merged to 'main'.

All other branches must merge to dev first:
  feature/issue-42-add-aws-skill → dev → main
```

---

### Pattern 6: Claude Code Review Integration

**Workflow**: `claude-code-review.yml` (to be adapted)

**Trigger**:
```yaml
on:
  pull_request_review_comment:
    types: [created]
  issue_comment:
    types: [created]
```

**Logic**:
1. Detect @claude mention in PR comment
2. Fetch PR diff and context
3. Use Claude Code Action (v1 GA) to analyze
4. Post comprehensive review as comment
5. Update PR labels based on findings

**Review Output**:
```markdown
## 🤖 Claude Code Review

**Overall Assessment**: Looks good with minor suggestions

### 🟢 Strengths
- Clean code structure
- Good test coverage
- Proper error handling

### 🟡 Suggestions
- Consider adding JSDoc comments to public methods
- Extract magic numbers to constants
- Add input validation for edge cases

### ❌ Issues
None found

**Recommendation**: Approve with minor improvements
```

---

### Pattern 7: Smart Commit Command

**Slash Command**: `/commit-smart`

**Steps**:
1. **Check Status** - Show staged/unstaged/untracked files
2. **Stage Selection** - Interactive or bulk staging
3. **Secret Detection** - Scan for API keys, tokens, passwords
4. **Quality Checks** - Run lint, type-check, tests
5. **Commit Message** - Guide conventional commit format
6. **Auto-Sign** - Add co-author (Claude)

**Secret Patterns Detected**:
```regex
api[_-]?key
api[_-]?secret
password\s*=\s*["'][^"']+
token\s*=\s*["'][^"']+
aws[_-]?access
AKIA[0-9A-Z]{16}      # AWS Access Key
sk-[a-zA-Z0-9]{32}    # Anthropic API key
```

**Benefits**:
- ✅ Prevents committing secrets
- ✅ Ensures code quality
- ✅ Enforces commit message standards
- ✅ Reduces manual steps

---

### Pattern 8: Create PR Command

**Slash Command**: `/create-pr`

**Steps**:
1. **Detect Branch** - Get current branch name
2. **Validate Name** - Check naming convention
3. **Push Check** - Ensure branch is pushed to remote
4. **Target Selection** - Auto-detect `dev` or allow custom
5. **Quality Gates** - Run quick lint/test checks
6. **Extract Issue** - Parse issue number from branch name
7. **Build PR Body** - Template with checkboxes
8. **Create PR** - Use `gh pr create` with proper labels
9. **Link Issue** - Add "Closes #123" to body

**PR Template Generated**:
```markdown
## Summary
[Briefly describe changes]

## Related Issues
Closes #42

## Changes Made
- [ ] Added AWS Solution Architect skill
- [ ] Created documentation
- [ ] Added tests
- [ ] Updated README

## Testing
- [ ] Lint passed
- [ ] Tests passed
- [ ] Type check passed
- [ ] Manual testing complete

## Screenshots (if applicable)
[Add screenshots]

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

---

## 📋 Implementation Roadmap

### Phase 1: Repository Setup (Week 1)

**Prerequisites**:
```bash
# 1. Create dev branch from main
git checkout main
git pull origin main
git checkout -b dev
git push -u origin dev

# 2. Set dev as default branch in GitHub
# Settings → Branches → Default branch → dev → Update

# 3. Enable required GitHub features
# Settings → Features → Issues ✅
# Settings → Features → Projects ✅
```

**Branch Protection Rules**:

**For `main` branch**:
```yaml
# Settings → Branches → Add rule
Branch name pattern: main

Require pull request before merging: ✅
  Require approvals: 1
  Dismiss stale reviews: ✅
  Require review from Code Owners: ✅

Require status checks to pass: ✅
  Require branches to be up to date: ✅
  Status checks:
    - validate-source
    - build-prod

Require conversation resolution: ✅
Require linear history: ✅
Do not allow bypassing settings: ✅
Restrict who can push: admins only
Allow force pushes: ❌
Allow deletions: ❌
```

**For `dev` branch**:
```yaml
Branch name pattern: dev

Require pull request before merging: ✅
  Require approvals: 1 (can be relaxed for solo developer)

Require status checks to pass: ✅
  Status checks:
    - validate-branch
    - validate-pr-title
    - quality-gates

Require conversation resolution: ✅
Allow force pushes: ❌ (only admins)
Allow deletions: ❌
```

**Deliverables**:
- [x] `dev` branch created and set as default
- [ ] Branch protection rules configured
- [ ] GitHub features enabled

---

### Phase 2: Core Workflows (Week 1-2)

**File Structure**:
```
.github/
├── workflows/
│   ├── create-branch-on-issue.yml     # Auto-create branches
│   ├── pr-into-dev.yml                # Validate PRs to dev
│   ├── dev-to-main.yml                # Validate releases
│   ├── claude-code-review.yml         # Claude reviews
│   └── pr-cleanup.yml                 # Auto-merge & cleanup
└── actions/                           # Composite actions (DRY)
    ├── fork-safety/                   # Fork PR detection
    ├── quality-gates/                 # Lint, test, type-check
    └── branch-cleanup/                # Delete merged branches
```

**1. Create Branch on Issue** (`create-branch-on-issue.yml`)

**Features**:
- Trigger: Issue labeled with `claude-code` + `status:ready`
- Branch naming: `{type}/issue-{number}-{slug}`
- Type detection from labels (`type:feature`, `type:fix`, etc.)
- Base branch: `dev` (or custom via `base:` label)
- Post checkout instructions as comment

**Adaptation Notes**:
- Use blueprint's workflow almost as-is
- Adjust default base branch from `dev` → `main` fallback to just `dev`
- Update project board integration (if using GitHub Projects)

---

**2. PR Validation (Dev)** (`pr-into-dev.yml`)

**Validations**:
1. Branch name format (enforce convention)
2. PR title (conventional commits)
3. Issue linking (at least one issue)
4. Quality gates (lint, tests, type-check)
5. Fork safety (read-only for forks)

**Quality Gates** (composite action):
```yaml
# .github/actions/quality-gates/action.yml
name: Quality Gates
description: Run lint, tests, and type checks

runs:
  using: composite
  steps:
    - name: Run linter
      run: npm run lint
      shell: bash

    - name: Run type check
      run: npm run type-check || npx tsc --noEmit
      shell: bash

    - name: Run tests
      run: npm test
      shell: bash
      env:
        CI: true
```

**Adaptation Notes**:
- Skills Factory may not have lint/test scripts
- Make quality gates optional with graceful fallback
- Focus on YAML validation for skills

---

**3. Release Gates (Main)** (`dev-to-main.yml`)

**Validations**:
1. Source must be `dev` or `release/*`
2. Production build must succeed
3. All tests must pass
4. No failing quality checks

**Adaptation Notes**:
- May not need production builds for this repo
- Focus on ensuring all skills are valid
- Validate YAML frontmatter in skills

---

**4. Claude Code Review** (`claude-code-review.yml`)

**Trigger**: @claude mentioned in PR comment

**Actions**:
1. Fetch PR diff
2. Run Claude Code Action for review
3. Post review as comment
4. Add labels based on review (needs-work, ready-to-merge)

**Blueprint Reference**:
```yaml
# Use Claude Code Action v1 GA
- name: Run Claude Code Review
  uses: anthropics/claude-code-action@v1
  with:
    anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
    github-token: ${{ github.token }}
    mode: auto  # Auto-detect PR review
```

**Adaptation Notes**:
- Requires `ANTHROPIC_API_KEY` secret
- Optional for this repo (can be added later)
- Focus on code quality and YAML validation

---

**5. PR Auto-Merge & Cleanup** (`pr-cleanup.yml`)

**Trigger**: PR approved and all checks pass

**Actions**:
1. Auto-merge PR to dev
2. Delete source branch
3. Post cleanup confirmation comment

**Blueprint Pattern**:
```yaml
name: Auto-Merge and Cleanup

on:
  pull_request_review:
    types: [submitted]

jobs:
  auto-merge:
    if: github.event.review.state == 'approved'
    runs-on: ubuntu-latest
    steps:
      - name: Auto-merge PR
        uses: pascalgn/automerge-action@v0.16.3
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          MERGE_METHOD: squash
          MERGE_DELETE_BRANCH: true
```

**Adaptation Notes**:
- Use squash merge to keep history clean
- Delete branch immediately after merge
- Post comment confirming cleanup

---

### Phase 3: Slash Commands (Week 2)

**File Structure**:
```
.claude/commands/github/
├── commit-smart.md           # Smart commits with quality checks
├── create-pr.md              # PR creation with auto-linking
├── switch-to-dev.md          # Switch back to dev branch
└── start-task.md             # Start new task (create issue + branch)
```

**1. /commit-smart** - Smart Commit Command

**Features**:
- Git status check
- Interactive staging
- Secret detection (API keys, tokens, etc.)
- Quality checks (lint, test, type-check)
- Conventional commit guidance
- Auto co-author (Claude)

**Usage**:
```
User: /commit-smart
Claude: [Runs all checks, guides commit message, creates commit]
```

**Adaptation Notes**:
- Copy blueprint command almost as-is
- Adjust quality checks for this repo
- Add YAML validation for skills

---

**2. /create-pr** - Create PR Command

**Features**:
- Branch detection and validation
- Auto-push if not pushed
- Target branch selection (auto-detect `dev`)
- Quality gates before PR
- Extract issue number from branch
- Build PR body from template
- Create PR with `gh pr create`
- Auto-link issues

**Usage**:
```
User: /create-pr
Claude: [Validates, runs checks, creates PR targeting dev]
```

**Adaptation Notes**:
- Always target `dev` (not `main`)
- Custom PR template for skills
- Add skill validation checklist

---

**3. /switch-to-dev** - Switch Branch Command (NEW)

**Purpose**: Ensure developer is back on `dev` before starting next task

**Features**:
- Check current branch
- Warn if uncommitted changes
- Stash if requested
- Switch to `dev`
- Pull latest changes
- Confirm ready for next task

**Usage**:
```
User: /switch-to-dev
Claude: [Checks status, switches to dev, pulls latest]

✅ Switched to dev branch and pulled latest changes
Ready to start next task!
```

---

**4. /start-task** - Start Task Command (NEW)

**Purpose**: Streamline starting a new task

**Features**:
1. Ensure on `dev` branch
2. Pull latest changes
3. Ask for task description
4. Create GitHub issue (or use existing)
5. Label issue (`claude-code`, `status:ready`, `type:feature`)
6. Wait for auto-branch creation
7. Checkout new branch
8. Post ready message

**Usage**:
```
User: /start-task

Claude: What task would you like to work on?
User: Add new skill for X

Claude:
1. Created issue #123: "Add new skill for X"
2. Labeled with claude-code, status:ready, type:feature
3. Branch created: feature/issue-123-add-new-skill-for-x
4. Checked out branch

✅ Ready to work! Start coding on feature/issue-123-add-new-skill-for-x
```

---

### Phase 4: Documentation & Training (Week 2-3)

**Create Documentation**:

1. **GITHUB_WORKFLOW.md** - Complete workflow guide
   - Branching strategy
   - How to start a task
   - How to create PR
   - How to merge to main
   - Emergency procedures

2. **Update README.md** - Add workflow section
   ```markdown
   ## GitHub Workflow

   This repository uses an automated GitHub workflow with Claude Code integration.

   **Quick Start**:
   1. Run `/start-task` to begin new work
   2. Make your changes
   3. Run `/commit-smart` to commit
   4. Run `/create-pr` to create PR
   5. Tag @claude for review
   6. After approval → auto-merged to dev
   7. Run `/switch-to-dev` before next task

   See [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md) for complete guide.
   ```

3. **Update CLAUDE.md** - Add workflow context
   ```markdown
   ## Branching Workflow

   **IMPORTANT**: Never push directly to `main` or `dev`.

   **Standard Flow**:
   feature/issue-123-name → dev → main

   **Slash Commands**:
   - `/start-task` - Start new task (creates issue + branch)
   - `/commit-smart` - Smart commit with quality checks
   - `/create-pr` - Create PR targeting dev
   - `/switch-to-dev` - Return to dev after task
   ```

---

## 🚀 Quick Win: Start with Minimal Implementation

### Immediate Actions (This Week)

Instead of implementing everything at once, start with core essentials:

**1. Create `dev` branch and protect it** ✅ (Done)
```bash
git checkout main
git pull origin main
git checkout -b dev
git push -u origin dev
```

**2. Add branch protection rules** (GitHub UI)
- Protect `main`: Require PR, 1 approval, no direct push
- Protect `dev`: Require PR, status checks

**3. Create ONE workflow**: `pr-into-dev.yml`
- Validate branch names
- Validate PR titles
- Basic quality gates (optional)

**4. Create TWO commands**:
- `/create-pr` - Create PR targeting dev
- `/switch-to-dev` - Switch back to dev

**5. Update CLAUDE.md with workflow rules**

---

## ✅ Success Criteria

### Week 1 Goals
- [x] `dev` branch created
- [ ] Branch protection configured (main + dev)
- [ ] `pr-into-dev.yml` workflow working
- [ ] `/create-pr` command working
- [ ] CLAUDE.md updated with workflow rules

### Week 2 Goals
- [ ] `/commit-smart` command working
- [ ] `/start-task` command working
- [ ] `create-branch-on-issue.yml` working
- [ ] Auto-merge & cleanup working

### Week 3 Goals
- [ ] Claude Code review integration
- [ ] `dev-to-main.yml` workflow
- [ ] Documentation complete
- [ ] Team trained on new workflow

---

## 🎓 Team Training

### For Developers

**Starting a New Task**:
```bash
# Option 1: Use slash command
/start-task

# Option 2: Manual
1. Create issue on GitHub
2. Label: claude-code, status:ready, type:feature
3. Wait for auto-branch creation
4. git fetch && git checkout feature/issue-123-name
```

**Working on Task**:
```bash
# Make changes
# ...

# Commit (with quality checks)
/commit-smart

# Create PR
/create-pr
```

**After Merge**:
```bash
# Return to dev
/switch-to-dev

# Start next task
/start-task
```

### For Reviewers

**Review Process**:
1. Receive PR notification
2. Review code on GitHub
3. Tag @claude for automated review (optional)
4. Approve or request changes
5. After approval → Auto-merged to dev
6. Branch auto-deleted

---

## 🔧 Customization Options

### Branch Naming Variations

If you prefer different naming:
```
Current: feature/issue-123-add-aws-skill

Options:
1. feat/123-add-aws-skill         (shorter, no "issue")
2. feature/add-aws-skill-123      (issue at end)
3. 123-feature-add-aws-skill      (issue first)
```

**To customize**: Edit regex in `create-branch-on-issue.yml` and `pr-into-dev.yml`

### Branching Strategy Variations

**Current Plan**: `feature → dev → main`

**Alternative**: `feature → dev → staging → main` (if needed)
- Add `staging` branch
- Update workflows to allow `dev → staging` and `staging → main`

### Quality Gates Customization

**Make optional** if repo doesn't have tests:
```yaml
- name: Run tests
  run: npm test
  continue-on-error: true  # Don't fail if no tests
```

---

## 📚 Reference Links

**Blueprint Repository**:
- Local: `/Users/rezarezvani/projects/claudecode-github-bluprint`
- GitHub: `https://github.com/alirezarezvani/claude-code-github-workflow`

**Key Blueprint Files**:
- `implementation.md` - Complete PRD and implementation plan
- `.github/workflows/create-branch-on-issue.yml` - Auto-branch creation
- `.github/workflows/pr-into-dev.yml` - PR validation
- `.github/workflows/dev-to-main.yml` - Release gates
- `.claude/commands/github/commit-smart.md` - Smart commit
- `.claude/commands/github/create-pr.md` - PR creation

**Official Documentation**:
- [GitHub Actions](https://docs.github.com/en/actions)
- [Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Claude Code Action](https://github.com/anthropics/claude-code-action)

---

## 🎯 Next Steps

1. **Review this plan** with team
2. **Decide on timeline** (1 week, 2 weeks, or 3 weeks)
3. **Start with Phase 1** (Repository Setup)
4. **Implement Phase 2** (Core Workflows) incrementally
5. **Add Phase 3** (Slash Commands) for developer experience
6. **Complete Phase 4** (Documentation) for sustainability

**Recommended**: Start with "Quick Win" approach (minimal implementation this week, expand next week)

---

**Created**: November 12, 2025
**Author**: Claude Code
**Status**: Planning - Ready for Review and Implementation
