# Workflow Testing Guide

**Branch**: `fix/workflow-bugs-phase1-3`
**Status**: Ready for testing
**Priority**: Critical - Must test before merging to main

---

## ⚠️ Important: How GitHub Actions Works

**Critical Understanding**:
- GitHub Actions workflows run from the **DEFAULT BRANCH** (main), not feature branches
- To test workflow changes, you must either:
  1. Merge to main (❌ NOT RECOMMENDED - defeats the purpose)
  2. Test using workflow_dispatch on the feature branch (⚠️ Limited)
  3. Change default branch temporarily (❌ DANGEROUS)
  4. **RECOMMENDED**: Manual testing + code review

---

## 🎯 What We're Testing

### Fix: WORKFLOW_KILLSWITCH Integration
**File**: `plan-validator.yml` (✅ FIXED)
**Bug**: Workflow doesn't check kill switch file
**Fix**: Added checkout + kill switch check as first steps

### Test Scenarios

#### Scenario 1: Kill Switch ENABLED (Workflows Run)
1. Ensure `.github/WORKFLOW_KILLSWITCH` has `STATUS: ENABLED`
2. Create test plan issue with 5-7 tasks
3. Add `plan` label
4. Workflow should:
   - ✅ Checkout repository
   - ✅ Check kill switch (STATUS: ENABLED)
   - ✅ Continue with validation
   - ✅ Validate task count (5-10)
   - ✅ Check rate limits
   - ✅ Add `plan-validated` label

#### Scenario 2: Kill Switch DISABLED (Workflows Stop)
1. Change `.github/WORKFLOW_KILLSWITCH` to `STATUS: DISABLED`
2. Create test plan issue with 5-7 tasks
3. Add `plan` label
4. Workflow should:
   - ✅ Checkout repository
   - ✅ Check kill switch (STATUS: DISABLED)
   - ✅ Post comment explaining workflows disabled
   - ✅ Exit gracefully (exit 0)
   - ❌ Should NOT validate plan
   - ❌ Should NOT add `plan-validated` label

---

## 🔬 Manual Testing Steps (RECOMMENDED)

Since workflows run from main branch, we'll do **code review + manual verification**:

### Step 1: Code Review
Review the changes in `plan-validator.yml`:
```yaml
steps:
  - name: Checkout repository
    uses: actions/checkout@v4
    with:
      fetch-depth: 1

  - name: Check Workflow Kill Switch
    id: killswitch
    run: |
      if [ -f ".github/WORKFLOW_KILLSWITCH" ]; then
        STATUS=$(grep "STATUS:" .github/WORKFLOW_KILLSWITCH | awk '{print $2}')
        if [ "$STATUS" = "DISABLED" ]; then
          echo "🛑 Workflow execution stopped by kill switch"
          gh issue comment ${{ github.event.issue.number }} --body "..."
          exit 0
        fi
      fi
      echo "✅ Kill switch check passed - STATUS: ENABLED"
```

**Verify**:
- ✅ Checkout step exists
- ✅ Kill switch check runs before validation
- ✅ Reads WORKFLOW_KILLSWITCH file correctly
- ✅ Exits gracefully if DISABLED
- ✅ Posts helpful comment to user
- ✅ Continues if ENABLED

### Step 2: Merge to Main (With Safeguards)

**Before Merging**:
1. ✅ Code review passed
2. ✅ All team members notified
3. ✅ Kill switch set to DISABLED (safety)
4. ✅ Ready to manually test after merge

**After Merging**:
1. Keep kill switch DISABLED
2. Create test plan issue (5 tasks)
3. Add `plan` label
4. Verify workflow exits gracefully
5. Change kill switch to ENABLED
6. Remove and re-add `plan` label
7. Verify workflow runs successfully

---

## 🧪 Full Testing Protocol

### Phase 1: Merge Single Fix
- [x] Fix plan-validator.yml
- [ ] Code review
- [ ] Merge to main
- [ ] Test with kill switch DISABLED
- [ ] Test with kill switch ENABLED
- [ ] Verify it works

### Phase 2: Fix Remaining Workflows
- [ ] plan-to-tasks.yml
- [ ] task-to-subtasks.yml
- [ ] smart-sync.yml
- [ ] hierarchy-dashboard.yml
- [ ] plan-auto-close.yml
- [ ] workflow-health.yml

### Phase 3: Integration Testing
- [ ] Create full test plan (5-7 tasks)
- [ ] Verify plan validation
- [ ] Verify task creation
- [ ] Verify subtask creation
- [ ] Verify project board sync
- [ ] Verify all workflows respect kill switch

---

## ✅ Success Criteria

**Kill Switch ENABLED**:
- ✅ Workflows run normally
- ✅ Plan validated
- ✅ Tasks created
- ✅ Project board updated

**Kill Switch DISABLED**:
- ✅ Workflows stop immediately
- ✅ Helpful comment posted
- ✅ No issues created
- ✅ No API calls made
- ✅ Graceful exit

---

## 🚨 Rollback Plan

If testing fails:
1. Set kill switch to DISABLED immediately
2. Identify the issue
3. Fix on feature branch
4. Repeat testing process

---

## 📋 Checklist Before Merging

- [ ] Code review completed
- [ ] Kill switch integration verified
- [ ] Testing plan documented
- [ ] Team notified
- [ ] Kill switch set to DISABLED (safety)
- [ ] Rollback plan ready
- [ ] Emergency procedures reviewed

---

**Last Updated**: 2025-10-24
**Branch**: fix/workflow-bugs-phase1-3
**Status**: Ready for code review and merge
