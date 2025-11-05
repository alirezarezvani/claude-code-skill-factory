# Auto-Sync Plan to GitHub Hook

**Automatically sync approved plans to GitHub issues with file references**

## Overview

This hook triggers when you approve a plan in Claude Code (ExitPlanMode) and automatically:
1. ✅ Extracts TodoWrite tasks from the approved plan
2. ✅ Parses file and folder references from the plan content
3. ✅ Creates a GitHub plan issue with enhanced task list
4. ✅ Triggers automation to create individual TASK issues
5. ✅ Includes file references in each task

**No manual steps required** - just approve your plan and the rest happens automatically.

---

## Features

### Automatic Sync
- Triggers on plan approval (ExitPlanMode event)
- No user confirmation needed
- Fast execution (<2 seconds)
- Zero Actions minutes consumed

### File Reference Extraction
Automatically detects and includes:
- **Files**: `src/auth/login.ts`, `tests/auth.test.ts`
- **Folders**: `src/auth/`, `components/`
- **Patterns**: `*.tsx`, `src/**/*.ts`

### Validation
- Task count: 5-10 (same as manual sync)
- Skips plans outside range (warns in log)
- Graceful error handling
- Detailed logging to `/tmp/auto-sync-plan-*.log`

### GitHub Integration
- Creates plan issue with `plan` label
- Triggers existing automation workflows:
  - `plan-validator.yml` (validates task count)
  - `plan-to-tasks.yml` (creates TASK issues)
  - `smart-sync.yml` (adds to project board)

---

## Installation

### Option 1: Project-Level (Recommended)

Install to `.claude/settings.json` (project-specific):

```bash
# Navigate to project root
cd /path/to/your/project

# Create .claude directory if needed
mkdir -p .claude

# Install hook
/install-hook generated-hooks/auto-sync-plan-to-github project
```

### Option 2: User-Level (Global)

Install to `~/.claude/settings.json` (all projects):

```bash
/install-hook generated-hooks/auto-sync-plan-to-github user
```

### Manual Installation

Copy hook files to your settings:

```bash
# Project-level
cp -r generated-hooks/auto-sync-plan-to-github .claude/hooks/

# User-level
cp -r generated-hooks/auto-sync-plan-to-github ~/.claude/hooks/
```

Then add to `settings.json`:

```json
{
  "hooks": [
    {
      "name": "auto-sync-plan-to-github",
      "path": ".claude/hooks/auto-sync-plan-to-github/hook.json",
      "enabled": true
    }
  ]
}
```

**Restart Claude Code** to activate the hook.

---

## How It Works

### 1. Plan Creation & Approval

```
User: "Create a plan to implement authentication"

Claude: [Creates detailed plan with tasks and file references]

Plan content:
- [ ] Implement JWT authentication in src/auth/jwt.ts
- [ ] Create login UI in src/components/Login.tsx
- [ ] Add tests in tests/auth/login.test.ts
- [ ] Update documentation in docs/auth.md
- [ ] Configure middleware in src/middleware/auth.ts

User: [Approves plan]
```

### 2. Automatic Sync Triggered

```
ExitPlanMode event → Hook triggers → sync-plan.sh executes
```

### 3. Extraction & Enhancement

**Hook extracts**:
- TodoWrite tasks (5 tasks)
- Files: `src/auth/jwt.ts`, `src/components/Login.tsx`, etc.
- Folders: `src/auth/`, `tests/auth/`, `docs/`

**Creates enhanced issue**:
```markdown
## Goal
Implement authentication system with JWT tokens

## Tasks
- [ ] Implement JWT authentication in src/auth/jwt.ts
- [ ] Create login UI in src/components/Login.tsx
- [ ] Add tests in tests/auth/login.test.ts
- [ ] Update documentation in docs/auth.md
- [ ] Configure middleware in src/middleware/auth.ts

## File References

**Files**:
- `src/auth/jwt.ts`
- `src/components/Login.tsx`
- `tests/auth/login.test.ts`
- `docs/auth.md`
- `src/middleware/auth.ts`

**Folders**:
- `src/auth/`
- `src/components/`
- `tests/auth/`
- `docs/`

## Acceptance Criteria
- [ ] All tasks completed
- [ ] Tests passing
- [ ] Documentation updated
- [ ] File changes reviewed
```

### 4. GitHub Automation

Plan issue created → Workflows trigger:
1. `plan-validator.yml` validates (30s)
2. `plan-to-tasks.yml` creates 5 TASK issues (2min)
3. `smart-sync.yml` adds all to project board (30s)

**Total time**: ~3 minutes for complete setup

---

## Configuration

### Settings in `hook.json`

```json
{
  "settings": {
    "enabled": true,                    // Enable/disable hook
    "autoSync": true,                   // Auto-sync on approval
    "includeFileReferences": true,      // Extract file refs
    "minTasks": 5,                      // Minimum task count
    "maxTasks": 10,                     // Maximum task count
    "repository": "owner/repo"          // GitHub repository
  }
}
```

### Customization

Edit `sync-plan.sh` to customize:

**Repository**:
```bash
REPO="your-org/your-repo"
```

**File extraction patterns**:
```bash
# Add more file extensions
grep -oE '\.(ts|tsx|js|jsx|py|go|rs|java)'
```

**Task validation**:
```bash
# Change min/max tasks
if [ "$TASK_COUNT" -lt 3 ]; then
```

---

## Examples

### Example 1: Authentication Feature

**Plan approved**:
```
Goal: Implement OAuth authentication

Tasks:
- [ ] Add OAuth provider config in src/config/oauth.ts
- [ ] Create auth routes in src/routes/auth.ts
- [ ] Build login page in src/pages/Login.tsx
- [ ] Add auth middleware in src/middleware/auth.ts
- [ ] Write integration tests in tests/auth/oauth.test.ts
```

**Auto-created GitHub issue #1010**:
- Title: "Plan: Implement OAuth authentication"
- Label: `plan`
- Tasks: 5 (with file references)
- Files: 5 extracted
- Folders: 4 extracted

**Automation creates**:
- Task #1011: Add OAuth provider config
- Task #1012: Create auth routes
- Task #1013: Build login page
- Task #1014: Add auth middleware
- Task #1015: Write integration tests

### Example 2: UI Refactoring

**Plan approved**:
```
Goal: Refactor dashboard components

Tasks:
- [ ] Split Dashboard.tsx into smaller components
- [ ] Extract charts to components/charts/
- [ ] Move styles to styles/dashboard/
- [ ] Update tests in tests/components/
- [ ] Document in docs/components.md
- [ ] Add Storybook stories
```

**Auto-created GitHub issue #1020**:
- 6 tasks → 6 TASK issues
- File references: Dashboard.tsx, *.css, *.md
- Folder references: components/charts/, styles/dashboard/, tests/components/

---

## Workflow Integration

### Daily Development

```
1. Morning: Plan your day's work
   "Create a plan for today's sprint tasks"

2. Claude creates plan with file references

3. You approve → Auto-syncs to GitHub

4. GitHub creates TASK issues automatically

5. Team sees your plan on project board

6. Start working on tasks
```

### Sprint Planning

```
1. Plan sprint features
   "Create a plan for Sprint 15 - User Dashboard"

2. Approve plan → Auto-syncs

3. 7-10 TASK issues created automatically

4. Team can pick tasks from project board

5. All tasks tracked with file references
```

---

## Monitoring & Debugging

### Check Logs

```bash
# View latest sync log
cat /tmp/auto-sync-plan-*.log | tail -n 50

# List all logs
ls -lt /tmp/auto-sync-plan-*.log
```

### Verify Sync

```bash
# Check if issue was created
gh issue list --label plan --limit 5

# View latest plan issue
gh issue view <number>

# Check workflow runs
gh run list --workflow "Plan to Tasks" --limit 5
```

### Common Issues

**Hook not triggering**:
```bash
# 1. Check hook is loaded
grep "auto-sync-plan-to-github" .claude/settings.json

# 2. Restart Claude Code
# 3. Approve a plan (5-10 tasks)
# 4. Check log: /tmp/auto-sync-plan-*.log
```

**GitHub authentication**:
```bash
# Verify gh CLI auth
gh auth status

# Re-authenticate if needed
gh auth login
```

**Task count outside range**:
```
Plan has 3 tasks → Skipped (min 5)
Plan has 12 tasks → Skipped (max 10)
Check log for warning message
```

---

## Efficiency Metrics

### Per Plan Sync

**Hook Execution**:
- Time: <2 seconds
- API calls: 1 (gh issue create)
- Rate limit: 5 points (GraphQL)
- Actions minutes: 0 (runs locally)

**Triggered Automation**:
- Workflows: 3 (validator, to-tasks, sync)
- Actions minutes: ~2-3 minutes
- TASK issues: 5-10 (automatic)
- Rate limit: ~10-15 points

### Monthly Capacity (Free Tier)

**Limits**:
- Actions: 2,000 minutes/month
- API: 5,000 calls/hour

**Capacity**:
- Plans per month: ~400 (within Actions limit)
- Plans per hour: ~150 (within rate limits)
- Daily average: ~13 plans/day (3% budget)

---

## Comparison: Manual vs Auto-Sync

### Manual Workflow (Before)

```
1. Approve plan
2. Open terminal
3. Run /sync-todos-to-github "Plan Title"
4. Paste todos (copy from plan)
5. Enter goal (copy from plan)
6. Confirm creation
7. Wait for issue creation

Time: ~2-3 minutes
User actions: 6 steps
```

### Auto-Sync Workflow (After)

```
1. Approve plan
   [Done - issue created automatically]

Time: 0 seconds (automatic)
User actions: 0 steps
```

**Time saved**: 2-3 minutes per plan
**User effort**: Eliminated 6 manual steps

---

## Uninstallation

### Remove Hook

```bash
# Project-level
rm -rf .claude/hooks/auto-sync-plan-to-github

# User-level
rm -rf ~/.claude/hooks/auto-sync-plan-to-github
```

### Update settings.json

Remove hook entry:

```json
{
  "hooks": [
    // Remove this:
    // {
    //   "name": "auto-sync-plan-to-github",
    //   "path": "...",
    //   "enabled": true
    // }
  ]
}
```

**Restart Claude Code**.

---

## Troubleshooting

### Hook Not Working

**Symptom**: Plan approved but no GitHub issue created

**Solutions**:
1. Check logs: `cat /tmp/auto-sync-plan-*.log`
2. Verify hook enabled in settings.json
3. Restart Claude Code
4. Check task count (5-10 required)
5. Verify gh CLI authenticated: `gh auth status`

### File References Not Extracted

**Symptom**: Issue created but no file references

**Solution**: Files must be mentioned in plan with proper format:
- ✅ `src/auth/login.ts`
- ✅ `components/Login.tsx`
- ❌ "the login file" (too vague)
- ❌ "auth module" (not a file path)

### Rate Limit Issues

**Symptom**: Issue creation fails with 429 error

**Solution**:
```bash
# Check rate limits
gh api rate_limit

# Wait for reset or reduce sync frequency
```

---

## Related Tools

- **Manual sync**: `/sync-todos-to-github` (when auto-sync disabled)
- **View issues**: `gh issue list --label plan`
- **Monitor workflows**: `gh run list --workflow "Plan to Tasks"`
- **Project board**: Check GitHub project board for task status

---

## Credits

**Created**: 2025-10-31
**Version**: 1.0.0
**Author**: Claude Code Skills Factory
**License**: MIT

---

## Changelog

### v1.0.0 (2025-10-31)
- ✅ Initial release
- ✅ ExitPlanMode auto-sync
- ✅ File reference extraction
- ✅ Folder reference extraction
- ✅ Enhanced task formatting
- ✅ Detailed logging
- ✅ Task count validation (5-10)
- ✅ GitHub automation integration

---

**Questions?** Check the logs at `/tmp/auto-sync-plan-*.log` for detailed execution info.