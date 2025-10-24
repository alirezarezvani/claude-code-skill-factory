# Branch Protection Rules

**Last Updated**: October 24, 2025
**Branch**: `main`
**Status**: 🔒 **PROTECTED**

This document describes the branch protection rules configured for the `main` branch.

---

## 🛡️ Active Protection Rules

| Rule | Status | Enforcement |
|------|--------|-------------|
| **Require Pull Requests** | ✅ Active | No direct pushes to main allowed |
| **Required Approvals** | ✅ Active | 1 approval minimum before merge |
| **Required Status Checks** | ✅ Active | `claude-review` workflow must pass |
| **Strict Status Checks** | ✅ Active | Branch must be up-to-date before merge |
| **Dismiss Stale Reviews** | ✅ Active | Re-review required after new commits |
| **Conversation Resolution** | ✅ Active | All PR comments must be resolved |
| **Enforce for Admins** | ✅ Active | Rules apply to everyone (no bypass) |
| **Block Force Pushes** | ✅ Active | History cannot be rewritten |
| **Block Deletions** | ✅ Active | Branch cannot be deleted |

---

## 🚫 What You CANNOT Do

These actions are **blocked** on the `main` branch:

### ❌ Direct Push to Main
```bash
git checkout main
git commit -m "some change"
git push origin main  # ❌ BLOCKED
```

**Error you'll see**:
```
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote: - Changes must be made through a pull request.
remote: - Required status check "claude-review" is expected.
```

### ❌ Force Push
```bash
git push --force origin main  # ❌ BLOCKED
```

### ❌ Delete Branch
```bash
git push origin --delete main  # ❌ BLOCKED
```

### ❌ Merge Without Approval
```bash
gh pr merge <NUMBER>  # ❌ BLOCKED if no approval
```

### ❌ Merge Without Status Checks
```bash
gh pr merge <NUMBER>  # ❌ BLOCKED if claude-review hasn't passed
```

---

## ✅ What You MUST Do

To merge changes into `main`, follow this workflow:

### Step 1: Create a Feature Branch
```bash
git checkout -b feature/my-feature
# Make your changes
git add .
git commit -m "feat: Add my feature"
git push -u origin feature/my-feature
```

### Step 2: Create a Pull Request
```bash
gh pr create \
  --base main \
  --title "feat: Add my feature" \
  --body "Description of changes"
```

### Step 3: Wait for Automatic Review
- ✅ Claude will automatically review your PR (if you're OWNER/MEMBER/COLLABORATOR)
- ✅ The `claude-review` status check will appear
- ⏳ Wait for it to complete

### Step 4: Get Human Approval
- 🔍 Request review from at least 1 team member
- ⏳ Wait for approval
- 💬 Resolve all PR comments (required)

### Step 5: Ensure Branch is Up-to-Date
```bash
# If main has changed, update your branch
git checkout feature/my-feature
git fetch origin
git merge origin/main
git push
```

### Step 6: Merge
```bash
# Only after ALL requirements met:
gh pr merge <NUMBER> --squash
# or --merge, --rebase
```

---

## 📊 Merge Requirements Checklist

Before you can merge a PR into `main`, verify:

- [ ] Pull request created (no direct pushes)
- [ ] At least 1 approval from team member
- [ ] `claude-review` status check passed ✅
- [ ] Branch is up-to-date with main
- [ ] All PR comments resolved
- [ ] No stale reviews (re-approved after latest commit)

**ALL must be green ✅ before GitHub allows merge.**

---

## 🎯 Who These Rules Apply To

### Everyone (Including Repository Owner)

These rules apply to:
- ✅ Repository owner (you)
- ✅ Organization members
- ✅ Collaborators
- ✅ External contributors

**No one can bypass** these rules (`enforce_admins: true`).

This ensures consistent code quality and review process for everyone.

---

## 🔍 Status Check: `claude-review`

**What it does**:
- Automatically runs when you open/update a PR
- Performs comprehensive code review:
  - Code quality and best practices
  - Potential bugs or issues
  - Performance considerations
  - Security concerns
  - Test coverage

**Workflow file**: `.github/workflows/claude-code-review.yml`

**Who gets it**:
- OWNER, MEMBER, COLLABORATOR PRs → ✅ Automatic review
- External contributor PRs → ❌ No automatic review (security)

**Manual trigger**: Team members can mention `@claude` in PR comments

---

## 🛠️ Configuration File

The branch protection rules are defined in:

**File**: `.github/branch-protection-config.json`

```json
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["claude-review"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": false,
    "required_approving_review_count": 1,
    "require_last_push_approval": false
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": true,
  "required_linear_history": false,
  "lock_branch": false
}
```

---

## 🔧 Modifying Protection Rules

### Via GitHub UI

1. Go to: https://github.com/alirezarezvani/claude-code-skill-factory/settings/branches
2. Click "Edit" next to the `main` branch rule
3. Modify settings
4. Click "Save changes"

### Via GitHub API (Command Line)

```bash
# Update configuration file
nano .github/branch-protection-config.json

# Apply changes
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  repos/:owner/:repo/branches/main/protection \
  --input .github/branch-protection-config.json
```

### Via GitHub CLI (Interactive)

```bash
# View current settings
gh api repos/:owner/:repo/branches/main/protection | jq .

# Disable protection (NOT RECOMMENDED)
gh api --method DELETE repos/:owner/:repo/branches/main/protection
```

---

## ⚠️ Troubleshooting

### "Protected branch update failed"

**Cause**: Trying to push directly to main
**Solution**: Create a PR instead (see workflow above)

### "Required status check 'claude-review' is expected"

**Cause**: PR doesn't have the claude-review check
**Solution**:
1. Make sure you're a team member (OWNER/MEMBER/COLLABORATOR)
2. Wait for the workflow to run automatically
3. If external contributor, ask team member to trigger `@claude`

### "Requires approving reviews"

**Cause**: No one has approved your PR yet
**Solution**: Request review from a team member

### "Branch is not up-to-date"

**Cause**: Main branch has changed since your branch was created
**Solution**:
```bash
git checkout your-branch
git fetch origin
git merge origin/main
git push
```

---

## 📚 Related Documentation

- **Security Model**: [.github/SECURITY.md](.github/SECURITY.md)
- **Workflow Documentation**: [.github/WORKFLOWS.md](.github/WORKFLOWS.md)
- **Claude Code Review**: [.github/workflows/claude-code-review.yml](.github/workflows/claude-code-review.yml)

---

## 📊 Testing Branch Protection

You can test that protection is working:

```bash
# This will fail (as expected)
git checkout main
echo "test" > test.txt
git add test.txt
git commit -m "test"
git push origin main

# Expected error:
# remote: error: GH006: Protected branch update failed
# remote: - Changes must be made through a pull request
```

If you see this error, **protection is working correctly!** ✅

---

## 🎯 Benefits

**Code Quality**:
- ✅ All changes reviewed by Claude AI
- ✅ All changes reviewed by humans
- ✅ Consistent quality standards

**Security**:
- ✅ Prevents accidental direct pushes
- ✅ Prevents force-push history rewrites
- ✅ Ensures review before sensitive changes

**Collaboration**:
- ✅ Encourages discussion in PRs
- ✅ Knowledge sharing through reviews
- ✅ Clear audit trail of all changes

**Stability**:
- ✅ Main branch always stable
- ✅ All changes tested via CI/CD
- ✅ No breaking changes without review

---

**Configured by**: Claude Code
**Date**: 2025-10-24
**Status**: 🔒 Fully Protected
