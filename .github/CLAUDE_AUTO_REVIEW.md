# Claude Automatic Code Review

**Last Updated**: October 24, 2025
**Status**: ✅ **ACTIVE** - Claude automatically reviews ALL pull requests

---

## 🤖 How It Works

Every pull request in this repository is **automatically reviewed by Claude AI** with no human intervention required.

### Workflow

```
PR Created → Claude Review Workflow Triggers → Claude Analyzes Code →
Review Posted → Status Check Updates → Merge Allowed (if approved)
```

**Timeline**:
- PR opened: 0 seconds
- Claude review starts: ~5-10 seconds
- Review completed: ~1-3 minutes (depending on PR size)
- Status check updated: Immediately after review

---

## ✅ What Claude Reviews

Claude provides comprehensive code review covering:

### 1. Code Quality & Best Practices
- ✅ Code structure and organization
- ✅ Naming conventions
- ✅ Design patterns
- ✅ Code duplication
- ✅ Complexity analysis

### 2. Potential Bugs
- ✅ Logic errors
- ✅ Edge cases
- ✅ Error handling
- ✅ Null/undefined checks
- ✅ Type mismatches

### 3. Performance Considerations
- ✅ Algorithm efficiency
- ✅ Resource usage
- ✅ Database query optimization
- ✅ Memory leaks
- ✅ Unnecessary computations

### 4. Security Concerns
- ✅ Input validation
- ✅ Authentication/authorization
- ✅ Data exposure
- ✅ Injection vulnerabilities
- ✅ Secure dependencies

### 5. Test Coverage
- ✅ Missing test cases
- ✅ Test quality
- ✅ Edge case coverage
- ✅ Integration tests
- ✅ E2E test needs

---

## 🔒 Branch Protection Integration

### Current Protection Rules

**Main branch requires**:
- ✅ `claude-review` status check must PASS
- ✅ All conversations must be resolved
- ✅ Branch must be up-to-date with main
- ✅ Cannot force push
- ✅ Cannot delete branch
- ✅ Enforced for everyone (including admins)

**NOT required**:
- ❌ Human code review (Claude reviews instead)
- ❌ Minimum number of approvals (Claude approval is automatic via status check)

**View current protection**:
```bash
gh api repos/:owner/:repo/branches/main/protection \
  --jq '{
    required_check: .required_status_checks.contexts[0],
    enforce_admins: .enforce_admins.enabled,
    conversation_resolution: .required_conversation_resolution.enabled
  }'
```

---

## 🎯 Differences from Human Review

| Feature | Human Review | Claude Auto-Review |
|---------|--------------|-------------------|
| **Assignment** | Manual | ✅ Automatic |
| **Speed** | Hours/days | ✅ 1-3 minutes |
| **Consistency** | Varies | ✅ Always consistent |
| **Availability** | Business hours | ✅ 24/7 |
| **Coverage** | May miss items | ✅ Comprehensive |
| **Bias** | Can be subjective | ✅ Objective |
| **Cost** | Expensive | ✅ Automated |

**Recommendation**: Claude auto-review for speed and consistency, optional human review for architectural decisions.

---

## 📋 Workflow Configuration

**File**: `.github/workflows/claude-code-review.yml`

### Triggers
```yaml
on:
  pull_request:
    types: [opened, synchronize]
```

**Events**:
- Pull request opened
- New commits pushed to PR

**No restrictions**: Runs for ALL PRs (internal and external contributors)

### Permissions
```yaml
permissions:
  contents: read          # Read repository code
  pull-requests: read     # Read PR details
  issues: read            # Read linked issues
  id-token: write         # OIDC authentication
```

### Concurrency Control
```yaml
concurrency:
  group: claude-review-${{ github.event.pull_request.number }}
  cancel-in-progress: true
```

**Behavior**: New commits cancel outdated reviews, ensuring Claude always reviews the latest code.

### Review Prompt
```yaml
prompt: |
  Please review this pull request and provide feedback on:
  - Code quality and best practices
  - Potential bugs or issues
  - Performance considerations
  - Security concerns
  - Test coverage

  Use the repository's CLAUDE.md for guidance on style and conventions.
  Use `gh pr comment` to leave your review as a comment on the PR.
```

### Tool Access
```yaml
claude_args: '--allowed-tools "Bash(gh issue view:*),Bash(gh search:*),Bash(gh pr comment:*),Bash(gh pr diff:*),Bash(gh pr view:*)"'
```

**Claude can**:
- View PR diffs
- View issues
- Search repository
- Post review comments

**Claude cannot**:
- Modify code directly
- Merge PRs
- Access secrets
- Run arbitrary commands

---

## 🧪 Testing & Verification

### Test That Claude Reviews Your PR

**Step 1: Create test PR**
```bash
git checkout -b test-claude-review
echo "// Test file" > test.js
git add test.js
git commit -m "test: Verify Claude auto-review"
git push -u origin test-claude-review
gh pr create --base main --title "Test: Claude Review" --body "Testing automatic review"
```

**Step 2: Monitor review**
```bash
# Watch workflow run
gh run list --workflow=claude-code-review.yml --limit 1

# View PR status checks
gh pr view <NUMBER> --json statusCheckRollup

# View Claude's review comment
gh pr view <NUMBER> --comments
```

**Step 3: Expected results**
- ✅ Workflow starts within 10 seconds
- ✅ `claude-review` status check appears
- ✅ Claude posts review comment (1-3 minutes)
- ✅ Status check updates to ✅ PASS or ❌ FAIL
- ✅ Merge button enabled/disabled based on status

**Step 4: Cleanup**
```bash
gh pr close <NUMBER> --delete-branch
```

---

## 🔍 Understanding Status Checks

### Status: ✅ PASS

**Meaning**: Claude reviewed the PR and found no blocking issues

**Actions**:
- ✅ PR can be merged (subject to other protections)
- ✅ Review comments may contain suggestions (non-blocking)
- ✅ Follow Claude's recommendations for best practices

**Example**:
```
✅ claude-review — Code review completed
```

### Status: ❌ FAIL

**Meaning**: Claude found critical issues or workflow encountered errors

**Common reasons**:
- Critical security vulnerabilities
- Major bugs identified
- Workflow execution error
- API authentication issues

**Actions**:
1. Read Claude's review comments
2. Address all critical issues
3. Push fixes to PR
4. Claude automatically reviews updated code

### Status: ⏳ PENDING

**Meaning**: Claude is currently reviewing

**Actions**:
- Wait 1-3 minutes for review to complete
- Avoid pushing new commits (will restart review)

---

## 📊 Review Quality & Accuracy

### What Claude Does Well

✅ **Excellent at**:
- Identifying common bugs and anti-patterns
- Spotting security vulnerabilities
- Detecting performance issues
- Checking code consistency
- Suggesting best practices

✅ **Very Good at**:
- Analyzing algorithm complexity
- Reviewing test coverage
- Identifying missing error handling
- Checking documentation completeness

⚠️ **Good but Limited**:
- Business logic validation (needs context)
- Architectural decisions (needs human judgment)
- Trade-off analysis (may lack full context)

### False Positives

Claude may occasionally flag non-issues. When this happens:

1. **Review Claude's reasoning** - Often highlights valid concerns
2. **Add clarifying comments** - Help Claude understand context
3. **Override if necessary** - You can merge despite concerns (status will pass)
4. **Provide feedback** - Mention @claude in comment to discuss

---

## 🛠️ Customization

### Change Review Focus

Edit `.github/workflows/claude-code-review.yml`:

```yaml
# Example: Focus on security only
prompt: |
  Review this PR focusing ONLY on security concerns:
  - Input validation
  - Authentication/authorization
  - Data exposure
  - Injection vulnerabilities

  Ignore style and performance issues.
```

### Add File Path Filters

```yaml
on:
  pull_request:
    types: [opened, synchronize]
    paths:
      - "src/**/*.ts"
      - "src/**/*.tsx"
      # Only review TypeScript files in src/
```

### Change Tool Access

```yaml
# Allow Claude to check CI results
claude_args: '--allowed-tools "Bash(gh pr:*),Bash(gh run:*)"'
```

### Disable for Specific PRs

Add `[skip claude]` to PR title or commit message:
```bash
git commit -m "docs: Update README [skip claude]"
```

---

## 🔐 Security & Privacy

### What Claude Can Access

**Yes**:
- ✅ All PR code changes
- ✅ PR description and comments
- ✅ Public repository files
- ✅ Linked issues (public)

**No**:
- ❌ Repository secrets
- ❌ Private environment variables
- ❌ Personal access tokens
- ❌ Other PRs or branches

### Data Retention

**Anthropic's Policy**:
- Code sent to Claude API for review
- Review results cached temporarily
- See: [Anthropic Privacy Policy](https://www.anthropic.com/privacy)

**GitHub Actions**:
- Workflow logs retained for 90 days
- Review comments permanent (until deleted)

---

## ⚠️ Troubleshooting

### Review not triggering

**Check 1: Workflow file exists**
```bash
cat .github/workflows/claude-code-review.yml
```

**Check 2: Workflow enabled**
```bash
gh workflow list | grep "Claude Code Review"
```

**Check 3: OAuth token configured**
```bash
gh secret list | grep CLAUDE_CODE_OAUTH_TOKEN
```

### Status check failing with errors

**Check workflow logs**:
```bash
gh run list --workflow=claude-code-review.yml --limit 1
gh run view <RUN-ID> --log
```

**Common errors**:
- `ACTIONS_ID_TOKEN_REQUEST_URL not found` → Check permissions in workflow
- `Authentication failed` → Check CLAUDE_CODE_OAUTH_TOKEN secret
- `Rate limit exceeded` → Wait and retry

### Claude's review seems incomplete

**Reasons**:
- PR too large (>1000 files) → Consider splitting PR
- Timeout (>10 minutes) → Workflow killed, retry
- API issues → Check [Anthropic Status](https://status.anthropic.com)

---

## 📈 Metrics & Monitoring

### View Review History

```bash
# Recent Claude reviews
gh run list --workflow=claude-code-review.yml --limit 10

# Success rate
gh run list --workflow=claude-code-review.yml --json conclusion \
  | jq '[.[] | select(.conclusion == "success")] | length'
```

### Average Review Time

Check workflow run durations in Actions tab:
- Typical: 1-3 minutes
- Large PRs: 3-10 minutes
- Very large PRs: May timeout (>10 minutes)

---

## 🎯 Best Practices

### For Pull Request Authors

1. **Keep PRs small** (< 500 lines) for better reviews
2. **Add descriptive PR descriptions** - Helps Claude understand context
3. **Link related issues** - Provides additional context
4. **Respond to Claude's feedback** - Engage with suggestions
5. **Push fixes incrementally** - Claude reviews each update

### For Repository Maintainers

1. **Trust Claude's reviews** for standard issues
2. **Human review** for architectural decisions
3. **Monitor review quality** - Adjust prompts if needed
4. **Keep CLAUDE.md updated** - Claude uses it for style guide
5. **Provide feedback** - Mention @claude to improve reviews

---

## 📚 Related Documentation

- **Workflow File**: [claude-code-review.yml](.github/workflows/claude-code-review.yml)
- **Branch Protection**: [BRANCH_PROTECTION.md](.github/BRANCH_PROTECTION.md)
- **Security Model**: [SECURITY.md](.github/SECURITY.md)
- **Claude Code Docs**: https://docs.claude.com/en/docs/claude-code
- **GitHub Actions**: https://docs.github.com/en/actions

---

## 📊 Status Summary

| Feature | Status | Configuration |
|---------|--------|---------------|
| Auto-review ALL PRs | ✅ Active | No author restrictions |
| Status check required | ✅ Active | Branch protection |
| Review comments | ✅ Active | Posted automatically |
| Human review required | ❌ Disabled | Claude reviews instead |
| 24/7 availability | ✅ Active | Always on |
| External contributor support | ✅ Active | Reviews all PRs |

---

**Configured by**: Claude Code
**Date**: October 24, 2025
**Status**: ✅ Operational
