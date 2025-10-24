# Automatic Reviewer Assignment

**Last Updated**: October 24, 2025
**Reviewer**: @alirezarezvani
**Status**: ✅ **ACTIVE**

This document describes how automatic reviewer assignment works in this repository.

---

## 🎯 How It Works

Every pull request in this repository is **automatically assigned** to @alirezarezvani for review through two complementary mechanisms:

### 1. CODEOWNERS File (Primary Method)
**File**: `.github/CODEOWNERS`

GitHub's built-in code ownership system automatically requests review from specified users when a PR touches files they own.

**Configuration**:
```
# All files owned by @alirezarezvani
* @alirezarezvani
```

**Effect**:
- ✅ Automatic review request when PR is opened
- ✅ Shows "Review required from code owners" in PR checks
- ✅ Enforced by branch protection (if enabled)
- ✅ Works for all PRs (internal and external contributors)

**Branch Protection Integration**:
- Required review from code owner: ✅ **ENABLED**
- PRs cannot be merged without code owner approval

### 2. Auto-Assign Workflow (Backup Method)
**File**: `.github/workflows/auto-assign-reviewer.yml`

GitHub Actions workflow that explicitly assigns reviewer when PR is opened.

**Triggers**:
- Pull request opened
- Pull request reopened
- Pull request marked "ready for review"

**Behavior**:
- Assigns @alirezarezvani as reviewer
- Adds confirmation comment
- Skips if PR author is @alirezarezvani (can't self-review)

**Why both methods?**
- CODEOWNERS is the primary, built-in GitHub method
- Auto-assign workflow is a backup for edge cases
- Belt-and-suspenders approach ensures assignment never fails

---

## ✅ What Happens When a PR is Created

### Step 1: PR Opened
```bash
gh pr create --base main --title "feat: New feature" --body "Description"
```

### Step 2: Automatic Assignment (Both Methods)

**CODEOWNERS (immediate)**:
- ✅ Review request sent to @alirezarezvani
- ✅ Shows in PR "Reviewers" section
- ✅ Email notification sent (if enabled)

**Auto-assign workflow (within seconds)**:
- ✅ Workflow triggers on PR open
- ✅ Explicitly assigns @alirezarezvani
- ✅ Adds comment: "👀 @alirezarezvani has been automatically assigned as reviewer"

### Step 3: Review Required
- PR shows "Review required from @alirezarezvani"
- Branch protection enforces review before merge
- PR cannot be merged until approved

---

## 🚫 Exception: Self-Review Not Allowed

If **you** (@alirezarezvani) create a PR:

- ❌ Auto-assign workflow skips (you can't review your own PR)
- ⚠️ CODEOWNERS still requests review (GitHub limitation)
- ℹ️ You'll need to request review from another team member

**Recommendation**:
- Add collaborators for mutual code review
- Or use an alternate GitHub account for PR author

---

## 📊 Workflow Details

### Auto-Assign Workflow Configuration

**Permissions**:
```yaml
permissions:
  pull-requests: write  # Required to assign reviewers
```

**Concurrency Control**:
```yaml
concurrency:
  group: auto-assign-${{ github.event.pull_request.number }}
  cancel-in-progress: true
```
Prevents duplicate assignments if PR is updated rapidly.

**Conditional Execution**:
```yaml
if: github.event.pull_request.user.login != 'alirezarezvani'
```
Skips assignment if you're the PR author.

**Actions Used**:
- `actions/github-script@v7` - Uses GitHub API to assign reviewer

---

## 🔧 Customization

### Change Reviewer

**Option 1: Update CODEOWNERS** (recommended)
```bash
# Edit .github/CODEOWNERS
* @new-reviewer

# Commit and push
git add .github/CODEOWNERS
git commit -m "chore: Update code owner"
git push
```

**Option 2: Update Auto-Assign Workflow**
```bash
# Edit .github/workflows/auto-assign-reviewer.yml
# Change line with reviewers: ['alirezarezvani']
reviewers: ['new-reviewer']

# Also update the conditional check
if: github.event.pull_request.user.login != 'new-reviewer'

# Commit and push
git add .github/workflows/auto-assign-reviewer.yml
git commit -m "chore: Update auto-assign reviewer"
git push
```

**Option 3: Update Branch Protection**
```bash
# Edit .github/branch-protection-config.json
# Change require_code_owner_reviews to false if not using CODEOWNERS
"require_code_owner_reviews": false

# Apply changes
gh api \
  --method PUT \
  repos/:owner/:repo/branches/main/protection \
  --input .github/branch-protection-config.json
```

### Add Multiple Reviewers

**CODEOWNERS (all required)**:
```
* @alirezarezvani @other-reviewer
```
Both must review.

**Auto-Assign Workflow (all assigned)**:
```yaml
reviewers: ['alirezarezvani', 'other-reviewer']
```
Both assigned, any can approve (unless CODEOWNERS requires both).

---

## 🧪 Testing

### Test Automatic Assignment

1. **Create test branch**:
```bash
git checkout -b test-auto-assign
echo "test" > test.txt
git add test.txt
git commit -m "test: Auto-assign"
git push -u origin test-auto-assign
```

2. **Create PR**:
```bash
gh pr create --base main --title "Test: Auto-assign" --body "Testing reviewer assignment"
```

3. **Verify assignment**:
- Check PR on GitHub
- Should see @alirezarezvani in "Reviewers" section
- Should see workflow comment
- Should see "Review required from @alirezarezvani"

4. **Cleanup**:
```bash
gh pr close <NUMBER>
git checkout main
git branch -D test-auto-assign
git push origin --delete test-auto-assign
```

---

## 📋 Integration with Branch Protection

CODEOWNERS integrates with branch protection rules:

**Current Configuration**:
- ✅ Require review from code owners: **ENABLED**
- ✅ Required approving review count: 1
- ✅ Dismiss stale reviews: Enabled

**Effect**:
- PRs **must** be approved by @alirezarezvani (code owner)
- Other approvals don't count toward required reviews
- Re-approval required if code changes after initial approval

**View settings**:
```bash
gh api repos/:owner/:repo/branches/main/protection \
  --jq '.required_pull_request_reviews'
```

---

## ⚠️ Troubleshooting

### Reviewer not automatically assigned

**Check 1: CODEOWNERS syntax**
```bash
# Verify file exists and has correct syntax
cat .github/CODEOWNERS
# Should show: * @alirezarezvani
```

**Check 2: Workflow running**
```bash
# View workflow runs
gh run list --workflow=auto-assign-reviewer.yml

# View specific run details
gh run view <RUN-ID>
```

**Check 3: Permissions**
- Workflow needs `pull-requests: write` permission
- Check `.github/workflows/auto-assign-reviewer.yml`

### "Review required from code owners" but no reviewer

**Cause**: CODEOWNERS file may have syntax error

**Fix**:
```bash
# Check CODEOWNERS format
# Lines starting with * must have space before @username
* @alirezarezvani   # ✅ Correct
*@alirezarezvani    # ❌ Wrong
```

### Cannot approve own PR

**Cause**: GitHub doesn't allow self-review

**Solution**:
- Ask another team member to review
- Or add a collaborator account for mutual reviews
- Or temporarily disable code owner requirement (not recommended)

---

## 📊 Workflow Logs

### View Assignment Activity

**Recent assignments**:
```bash
gh run list --workflow=auto-assign-reviewer.yml --limit 10
```

**Detailed logs**:
```bash
gh run view <RUN-ID> --log
```

**Expected output**:
```
PR #10 opened by @external-contributor
Requesting review from @alirezarezvani...
✅ Successfully assigned @alirezarezvani as reviewer
```

---

## 🔒 Security Considerations

**Who can be assigned**:
- Only repository collaborators can be assigned as reviewers
- CODEOWNERS users must have write access to repository
- External users in CODEOWNERS will be ignored

**Permissions required**:
- Auto-assign workflow: `pull-requests: write`
- CODEOWNERS: No special permissions (GitHub built-in)

**Bypass protection**:
- Code owner reviews cannot be bypassed (enforce_admins: true)
- Even repository owner must get code owner approval

---

## 📚 References

**CODEOWNERS**:
- [GitHub CODEOWNERS Documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [CODEOWNERS Syntax](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners#codeowners-syntax)

**Branch Protection**:
- [Require review from code owners](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging)

**GitHub Actions**:
- [actions/github-script](https://github.com/actions/github-script)
- [Pull Requests API](https://docs.github.com/en/rest/pulls/review-requests)

---

## 📊 Status Summary

| Feature | Status | Method |
|---------|--------|--------|
| Automatic assignment | ✅ Active | CODEOWNERS + Workflow |
| Code owner review required | ✅ Active | Branch protection |
| Assignment to @alirezarezvani | ✅ Active | Both methods |
| Notification comment | ✅ Active | Auto-assign workflow |
| Self-review prevention | ✅ Active | Workflow conditional |
| External contributor support | ✅ Active | CODEOWNERS |

---

**Configured by**: Claude Code
**Date**: 2025-10-24
**Reviewer**: @alirezarezvani
