# Branch Protection Configuration

**Repository**: claude-code-skills-factory
**Date**: November 12, 2025
**Status**: Ready to Apply

---

## 🎯 Overview

This document provides **step-by-step instructions** for configuring branch protection rules in GitHub Settings. These rules enforce the new branching workflow and prevent direct pushes to protected branches.

---

## 📋 Prerequisites

Before applying branch protection:

1. ✅ `dev` branch exists on remote (will be pushed during implementation)
2. ✅ Current working branch is clean
3. ✅ You have **admin access** to the repository

---

## 🔧 GitHub Settings Configuration

### Step 1: Access Branch Protection Settings

1. Go to repository on GitHub: `https://github.com/alirezarezvani/claude-code-skill-factory`
2. Click **Settings** tab
3. In left sidebar, click **Branches** under "Code and automation"
4. Scroll to **Branch protection rules** section

---

### Step 2: Protect `main` Branch

Click **Add rule** or edit existing `main` rule.

**Branch name pattern**: `main`

#### Required Settings

**Protect matching branches**:

- ✅ **Require a pull request before merging**
  - ✅ Require approvals: **1**
  - ✅ Dismiss stale pull request approvals when new commits are pushed
  - ✅ Require review from Code Owners (if CODEOWNERS file exists)
  - ✅ Require approval of the most recent reviewable push
  - ❌ Require conversation resolution before merging (optional, can enable later)

- ✅ **Require status checks to pass before merging**
  - ✅ Require branches to be up to date before merging
  - **Status checks that are required** (select these after workflows run once):
    - `validate-source` (from dev-to-main.yml - will be created)
    - `build-prod` (from dev-to-main.yml - will be created)
    - `Commit & Branch Guard / guard` (existing - from ci-commit-branch-guard.yml)
  - Note: These checks will appear after the first PR runs the workflows

- ✅ **Require conversation resolution before merging** (recommended)

- ❌ **Require signed commits** (optional - enable if your team uses GPG signing)

- ✅ **Require linear history** (enforces squash or rebase merges, no merge commits)

- ❌ **Require merge queue** (not needed for small teams)

- ✅ **Require deployments to succeed before merging** (optional - skip for now)

- ❌ **Lock branch** (not needed)

- ❌ **Do not allow bypassing the above settings** (recommended to DISABLE so admins can emergency merge)

**Rules applied to everyone including administrators**:

- ✅ **Restrict who can push to matching branches**
  - **Role**: Restrict pushes to **Maintain role** or higher
  - **People, teams, or apps**: Leave empty (default: only admins/maintainers)
  - Effect: **Only admins** can push directly to main (emergency use only)

- ✅ **Allow force pushes**: **DISABLE** (❌)
  - **Everyone**: No one can force push
  - **Specify who can force push**: Not applicable
  - Effect: Prevents history rewriting on main

- ✅ **Allow deletions**: **DISABLE** (❌)
  - Effect: Prevents accidental deletion of main branch

#### Summary for `main` Branch

```yaml
Branch: main
Purpose: Production releases only

Protections:
  ✅ Require PR with 1 approval
  ✅ Require status checks (validate-source, build-prod)
  ✅ Require up-to-date branches
  ✅ Linear history (squash/rebase only)
  ✅ Restrict direct pushes (admins only)
  ❌ No force pushes
  ❌ No deletions

Allowed Sources:
  - dev (via PR)
  - release/* (hotfix via PR)
  - dependabot/* (automated via PR)
```

**Click "Create" or "Save changes"**

---

### Step 3: Protect `dev` Branch

Click **Add rule**.

**Branch name pattern**: `dev`

#### Required Settings

**Protect matching branches**:

- ✅ **Require a pull request before merging**
  - ✅ Require approvals: **1** (can reduce to 0 for solo developer, but keep 1 for discipline)
  - ✅ Dismiss stale pull request approvals when new commits are pushed
  - ❌ Require review from Code Owners (optional)
  - ✅ Require approval of the most recent reviewable push
  - ❌ Require conversation resolution before merging (optional)

- ✅ **Require status checks to pass before merging**
  - ✅ Require branches to be up to date before merging
  - **Status checks that are required** (will appear after first PR):
    - `validate-branch` (from pr-into-dev.yml - will be created)
    - `validate-pr-title` (from pr-into-dev.yml - will be created)
    - `quality-gates` (from pr-into-dev.yml - will be created)
    - `Commit & Branch Guard / guard` (existing)
  - Note: More lenient than main - focuses on validation, not production readiness

- ✅ **Require conversation resolution before merging** (recommended)

- ❌ **Require signed commits** (optional)

- ✅ **Require linear history** (keep history clean)

- ❌ **Require merge queue** (not needed)

- ❌ **Require deployments to succeed before merging** (not needed for dev)

- ❌ **Lock branch** (not needed)

- ❌ **Do not allow bypassing the above settings** (allow admins to bypass for flexibility)

**Rules applied to everyone including administrators**:

- ❌ **Restrict who can push to matching branches**: **DISABLE**
  - **Allow** direct pushes from anyone (for flexibility during development)
  - However, PR requirements still apply for merges
  - Effect: Admins can push directly in emergencies, but merges require PR

- ✅ **Allow force pushes**: **DISABLE** (❌)
  - **Everyone**: No one can force push
  - Effect: Prevents history rewriting

- ✅ **Allow deletions**: **DISABLE** (❌)
  - Effect: Prevents accidental deletion of dev branch

#### Summary for `dev` Branch

```yaml
Branch: dev
Purpose: Active development, integration branch

Protections:
  ✅ Require PR with 1 approval (can reduce to 0 for solo)
  ✅ Require status checks (validate-branch, validate-pr-title, quality-gates)
  ✅ Require up-to-date branches
  ✅ Linear history (squash/rebase only)
  ⚠️ Allow direct pushes (admins only, for flexibility)
  ❌ No force pushes
  ❌ No deletions

Allowed Sources:
  - feature/* (via PR)
  - fix/* (via PR)
  - hotfix/* (via PR)
  - refactor/* (via PR)
  - test/* (via PR)
  - docs/* (via PR)
```

**Click "Create"**

---

### Step 4: Set `dev` as Default Branch

**Important**: This makes `dev` the base for new PRs and clones.

1. In **Settings** → **Branches**
2. Find **Default branch** section (top of page)
3. Click switch icon next to current default (`main`)
4. Select **`dev`** from dropdown
5. Click **"I understand, update the default branch"**
6. Confirm the change

**Effect**:
- New PRs will default to targeting `dev`
- `git clone` will default to `dev` branch
- GitHub UI will show `dev` branch by default

---

### Step 5: Optional Branch Protections

If your team grows or you need stricter controls, add these rules:

#### Protect All `feature/*` Branches (Optional)

**Branch name pattern**: `feature/*`

**Minimal protections**:
- ✅ Require status checks: `Commit & Branch Guard / guard`
- ✅ No deletions until merged
- ❌ No PR requirements (can commit directly to feature branch)

**Purpose**: Prevents accidental deletion of in-progress feature branches

#### Protect All `release/*` Branches (Recommended for Production)

**Branch name pattern**: `release/*`

**Strong protections**:
- ✅ Require PR with 1 approval before merging to main
- ✅ Require all status checks
- ✅ Restrict direct pushes (admins only)
- ❌ No force pushes
- ❌ No deletions

**Purpose**: Release branches are critical hotfix paths to production

---

## 📊 Verification Checklist

After applying all rules, verify:

**main branch**:
- [ ] Requires PR with 1 approval
- [ ] Requires status checks
- [ ] Only admins can push directly
- [ ] No force pushes allowed
- [ ] No deletions allowed
- [ ] Can only receive PRs from `dev` or `release/*`

**dev branch**:
- [ ] Requires PR with 1 approval
- [ ] Requires status checks
- [ ] Direct pushes allowed (admins only)
- [ ] No force pushes allowed
- [ ] No deletions allowed
- [ ] Set as default branch ✅

**Repository settings**:
- [ ] Default branch is `dev`
- [ ] GitHub Actions enabled
- [ ] Pull requests enabled
- [ ] Issues enabled

---

## 🧪 Testing Branch Protection

### Test 1: Try to Push Directly to `main`

```bash
git checkout main
git commit --allow-empty -m "test: direct push to main"
git push origin main
```

**Expected Result**: ❌ Push rejected with error message
```
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote: error: Changes must be made through a pull request.
```

### Test 2: Try to Push Directly to `dev`

```bash
git checkout dev
git commit --allow-empty -m "test: direct push to dev"
git push origin dev
```

**Expected Result**:
- If admin: ✅ Push succeeds (but not recommended)
- If non-admin: ❌ Push rejected

**Correct workflow**: Should create PR even for dev

### Test 3: Create PR from Invalid Branch

```bash
git checkout -b invalid-branch-name
git commit --allow-empty -m "test: invalid branch"
git push -u origin invalid-branch-name
gh pr create --base dev --title "test: invalid branch"
```

**Expected Result**: ❌ PR checks fail
- `validate-branch` job fails
- Comment posted explaining naming convention

### Test 4: Create PR with Valid Branch

```bash
git checkout dev
git pull origin dev
git checkout -b feature/test-branch-protection
git commit --allow-empty -m "test: valid feature branch"
git push -u origin feature/test-branch-protection
gh pr create --base dev --title "feat: test branch protection"
```

**Expected Result**: ✅ PR checks pass
- `validate-branch` passes
- `validate-pr-title` passes (conventional commit format)
- Ready for review

---

## 🚨 Emergency Procedures

### Bypass for Critical Hotfix

If you need to bypass protection for emergency (admin only):

**Option 1**: Temporarily disable protection
1. Go to Settings → Branches
2. Edit `main` protection rule
3. Temporarily disable "Do not allow bypassing"
4. Perform emergency push
5. **IMMEDIATELY** re-enable protection

**Option 2**: Use emergency PR with bypass label
1. Create PR from `hotfix/*` branch
2. Add `[EMERGENCY]` to PR title
3. Claude Code review will be skipped
4. Merge with reduced checks

**Option 3**: Admin override (last resort)
1. Admins can force-merge PRs that don't meet requirements
2. Document reason in PR comments
3. Create follow-up issue to fix properly

### Rollback Branch Protection

If protection causes issues:

1. Go to Settings → Branches
2. Find rule causing issues
3. Click **Delete** (trash icon)
4. Confirm deletion
5. Document reason and fix underlying issue
6. Reapply protection after fix

---

## 🔄 Migration from Current State

### Current Branches That Don't Match Convention

These branches will need to be renamed or closed:

```
❌ origin/claude/issue-1010-20251101-2155  → close or rename to feature/issue-1010-*
❌ origin/docs/update-changelog            → rename to docs/update-changelog
❌ origin/feat-add-git-governance-workflows → rename to feat/add-git-governance-workflows
❌ origin/feat-add-hooks-support-12068     → rename to feat/add-hooks-support-12068
✅ origin/feat/add-git-governance-workflows → valid (feat/)
✅ origin/fix/psychology-advisor-link      → valid (fix/)
✅ origin/fix/yaml-lint-errors             → valid (fix/)
```

**Cleanup Commands**:
```bash
# Delete old format branches (after merging or closing PRs)
git push origin --delete claude/issue-1010-20251101-2155
git push origin --delete feat-add-git-governance-workflows
git push origin --delete feat-add-hooks-support-12068

# Or rename if still needed
git branch -m old-name feature/new-name
git push origin :old-name feature/new-name
```

---

## 📚 Reference

**Related Files**:
- `.github/workflows/pr-into-dev.yml` - Validates PRs to dev
- `.github/workflows/dev-to-main.yml` - Validates PRs to main
- `.github/workflows/ci-commit-branch-guard.yml` - Validates branch names
- `WORKFLOW_ADAPTATION_PLAN.md` - Complete workflow documentation

**GitHub Documentation**:
- [Managing branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)
- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Changing the default branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/changing-the-default-branch)

---

**Ready to Apply**: Follow Steps 1-5 above in GitHub Settings
**Questions**: Refer to WORKFLOW_ADAPTATION_PLAN.md or ask in repository discussions
