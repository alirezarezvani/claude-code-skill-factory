# 🚨 EMERGENCY PROCEDURES

## Quick Actions

### 1. IMMEDIATE: Disable All Workflows

```bash
# Edit .github/WORKFLOW_KILLSWITCH
# Change STATUS from ENABLED to DISABLED
echo "STATUS: DISABLED" > .github/WORKFLOW_KILLSWITCH
git add .github/WORKFLOW_KILLSWITCH
git commit -m "emergency: Disable all workflows"
git push origin main --no-verify  # EMERGENCY BYPASS
```

### 2. Clean Up Spam Issues

```bash
# Dry run first (see what would be deleted)
chmod +x .github/EMERGENCY_CLEANUP.sh
.github/EMERGENCY_CLEANUP.sh true

# Actually close issues
.github/EMERGENCY_CLEANUP.sh false
```

### 3. Push Without Code Review (EMERGENCY ONLY)

**Method 1: Force Push to Main** (Use with extreme caution)
```bash
git push origin main --no-verify --force
```

**Method 2: Bypass Protection with Label**
```bash
# Add [EMERGENCY] to PR title
gh pr create --title "[EMERGENCY] Fix critical workflow bug" --body "..."
```

**Method 3: Disable Branch Protection Temporarily**
1. Go to: Settings → Branches → main → Edit
2. Uncheck "Require status checks"
3. Save changes
4. Push your fix
5. **RE-ENABLE protection immediately after**

### 4. Manual Merge Without Review

```bash
# Create PR
gh pr create --title "[SKIP REVIEW] Emergency fix" --body "..."

# Get PR number
PR_NUM=$(gh pr list --limit 1 --json number --jq '.[0].number')

# Merge immediately (bypassing checks)
gh pr merge $PR_NUM --admin --squash
```

---

## Prevention Systems

### Kill Switch

**File**: `.github/WORKFLOW_KILLSWITCH`

All workflows check this file before running. If STATUS is DISABLED, they exit immediately.

**Usage**:
```bash
# Disable all workflows
echo "STATUS: DISABLED" > .github/WORKFLOW_KILLSWITCH
git commit -am "emergency: Kill switch activated"
git push

# Re-enable workflows
echo "STATUS: ENABLED" > .github/WORKFLOW_KILLSWITCH
git commit -am "chore: Re-enable workflows"
git push
```

### Rate Limit Guardian

All workflows have circuit breaker checks:
- Checks rate limits before execution
- Requires minimum 50-100 remaining
- Exits gracefully if limits low

**Manual Check**:
```bash
gh api rate_limit --jq '.resources.core.remaining, .resources.graphql.remaining'
```

### Manual Review Bypass

**Method 1: PR Title Markers**
- `[EMERGENCY]` - Critical fix, bypass all checks
- `[SKIP REVIEW]` - Minor fix, skip code review
- `[HOTFIX]` - Production issue, fast-track

**Method 2: Special Labels**
- `emergency` - Bypass all checks
- `skip-review` - Skip code review only
- `hotfix` - Fast-track but keep essential checks

---

## Root Cause Analysis

### Why 279 Issues Were Created

**Problem**: Workflows had bugs and were on main branch

**Triggers**:
1. Commits pushed to main triggered workflows
2. Workflows processed old/existing issues
3. Label bugs caused wrong issue types
4. No kill switch to stop runaway execution

**Fixes Implemented**:
1. ✅ Kill switch file (immediate stop capability)
2. ✅ Cleanup script (bulk issue closure)
3. ✅ Manual bypass procedures
4. ✅ Rate limit guardians in all workflows

---

## Escalation Contacts

**GitHub Rate Limits**:
- Personal: 5,000/hour
- OAuth: 5,000/hour
- Actions: 1,000/hour per repo

**If Monthly Limit Hit**:
1. Contact GitHub Support
2. Request limit increase (explain emergency)
3. Use alternative account temporarily
4. Wait for monthly reset

---

## Testing Protocol (MANDATORY)

**Never merge workflows directly to main again!**

1. **Feature Branch**: All workflow changes go to feature branch first
2. **Test on Feature Branch**:
   - Create test issues
   - Trigger workflows
   - Monitor behavior
3. **Code Review**: Get review even for "safe" changes
4. **Gradual Rollout**:
   - Merge one workflow at a time
   - Monitor for 24 hours
   - Then merge next workflow

---

## Recovery Checklist

- [ ] Kill switch activated (workflows disabled)
- [ ] Spam issues cleaned up
- [ ] Rate limit status checked
- [ ] Workflow bugs identified and fixed
- [ ] Fixes tested on feature branch
- [ ] Code review completed
- [ ] Kill switch deactivated (workflows enabled)
- [ ] Monitoring active for 48 hours

---

## Lessons Learned

1. **NEVER push workflow changes directly to main**
2. **ALWAYS test workflows on feature branch first**
3. **ALWAYS have a kill switch**
4. **ALWAYS have cleanup scripts ready**
5. **ALWAYS have emergency bypass procedures documented**

---

**Last Updated**: 2025-10-24
**Status**: Active
