# Status Synchronization System

Complete guide for bidirectional synchronization between GitHub issues and project boards.

---

## Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Status Labels](#status-labels)
- [Workflow Architecture](#workflow-architecture)
- [Team Workflow](#team-workflow)
- [Sync Loop Prevention](#sync-loop-prevention)
- [Troubleshooting](#troubleshooting)
- [Advanced Usage](#advanced-usage)

---

## Overview

The status sync system keeps your team aligned by automatically synchronizing status changes between:
- **GitHub Issues** (labels, state, comments)
- **GitHub Project Board** (@claude-skills-factory #7)

### Key Features
- ✅ **Bidirectional sync** - Changes in either direction are reflected
- ✅ **Team visibility** - Automated comments notify team of status changes
- ✅ **State management** - Issues automatically close when moved to "Done"
- ✅ **Loop prevention** - Smart concurrency controls prevent infinite sync loops
- ✅ **Audit trail** - All changes are tracked with comments

---

## How It Works

### Three-Layer Status Tracking

#### 1. **Labels** (Primary tracking mechanism)
Visible everywhere, searchable, filterable:
- `status: triage` - Yellow (#fbca04)
- `status: backlog` - Purple (#d4c5f9)
- `status: ready` - Green (#0e8a16)
- `status: in-progress` - Blue (#1d76db)
- `status: in-review` - Pink (#d876e3)
- `status: done` - Dark green (#2ea44f)

#### 2. **Issue State** (Secondary tracking)
GitHub's built-in open/closed:
- **Open**: Any status except "Done"
- **Closed**: "Done" status

#### 3. **Comments** (Audit trail)
Automated comments post on major transitions:
```markdown
## 📊 Status Update
**Status changed to**: **In Progress**
This issue was moved on the @claude-skills-factory project board by @username.
```

---

## Status Labels

### Label Mapping

| Project Board Column | Issue Label | Issue State | Color |
|---------------------|-------------|-------------|-------|
| To triage | `status: triage` | Open | Yellow |
| Backlog | `status: backlog` | Open | Purple |
| Ready | `status: ready` | Open | Green |
| In Progress | `status: in-progress` | Open | Blue |
| In Review | `status: in-review` | Open | Pink |
| Done | `status: done` | Closed | Dark Green |

### Label Lifecycle

**Creation**:
- Labels are created automatically on first use
- All 6 status labels created during initial setup

**Replacement**:
- When status changes, old status label is removed
- New status label is added
- Only one status label exists per issue at a time

**Visibility**:
- Labels appear in issue lists, filters, and searches
- Use filters like `label:"status: in-progress"` to find active work

---

## Workflow Architecture

### Two Workflows Handle Sync

#### 1. **project-to-issue-sync.yml** (Board → Issue)

**Trigger**: `projects_v2_item` event (when items move on board)

**Actions**:
1. Query project item to get issue number
2. Determine new status from project column
3. Remove old status label
4. Add new status label
5. Close/reopen issue if needed
6. Post status change comment

**Permissions**: `issues: write`, `id-token: write`

**Tool Allowlist**: `gh issue:*`, `gh api:*`

---

#### 2. **issue-to-project-sync.yml** (Issue → Board)

**Trigger**: `issues` event (labeled with `status:*`, closed, reopened)

**Actions**:
1. Check if issue is in project (add if missing)
2. Determine target status from labels or state
3. Query project to get status field ID
4. Update project item status column
5. Post confirmation comment (on label changes only)

**Permissions**: `issues: read`, `id-token: write`

**Tool Allowlist**: `gh issue:*`, `gh api:*`, `gh project:*`

---

## Team Workflow

### Scenario 1: Developer Starts Work

**Option A - Update Project Board** (Recommended):
1. Developer moves issue to "In Progress" on project board
2. `project-to-issue-sync` workflow triggers
3. Issue gets `status: in-progress` label
4. Comment posted: "Status changed to In Progress"

**Option B - Update Issue Label**:
1. Developer adds `status: in-progress` label to issue
2. `issue-to-project-sync` workflow triggers
3. Issue moves to "In Progress" column on board
4. Comment posted: "Project board updated"

**Result**: Issue and board are in sync regardless of which the developer updates.

---

### Scenario 2: Code Review Phase

**Developer creates PR**:
1. Developer moves issue to "In Review" on board
2. Issue gets `status: in-review` label
3. Team members see issue is under review

**PR merged**:
1. Developer moves issue to "Done" on board
2. Issue gets `status: done` label
3. **Issue automatically closes**
4. Comment posted: "Status changed to Done"

---

### Scenario 3: Issue Needs More Work

**Reopen from Done**:
1. Team member reopens closed issue
2. `issue-to-project-sync` detects reopening
3. Issue moved to "To triage" on board (default for reopened)
4. Team triages to determine next status

**Or**:
1. Team member adds `status: in-progress` label
2. Issue moves to "In Progress" on board
3. Issue automatically reopened (if was closed)

---

## Sync Loop Prevention

### Problem: Infinite Loops
Without protection, workflows could trigger each other infinitely:
1. Board update → Issue update → Board update → Issue update → ...

### Solutions Implemented

#### 1. **Directional Workflow Design**
- `project-to-issue-sync`: Only READS from board, WRITES to issues
- `issue-to-project-sync`: Only READS from issues, WRITES to board
- Neither workflow modifies its own trigger source

#### 2. **Concurrency Controls**
```yaml
concurrency:
  group: project-sync-${{ github.event.projects_v2_item.node_id }}
  cancel-in-progress: false
```
- Prevents multiple sync workflows running on same issue simultaneously
- Each issue/project item has its own concurrency group

#### 3. **Conditional Triggers**
```yaml
if: |
  (github.event.action == 'labeled' && startsWith(github.event.label.name, 'status:')) ||
  github.event.action == 'closed' ||
  github.event.action == 'reopened'
```
- Only triggers on specific, relevant events
- Ignores unrelated issue updates

#### 4. **Smart State Checks**
- Check current state before making changes
- Skip if already in target state
- Prevents redundant operations

---

## Troubleshooting

### Issue: Workflow Not Triggering

**Symptom**: Move issue on board, but label doesn't update

**Diagnosis**:
```bash
# Check recent workflow runs
gh run list --workflow=project-to-issue-sync.yml --limit 5

# Check workflow status
gh run view <run-id> --log
```

**Common Causes**:
1. **PROJECTS_TOKEN missing** - Workflow needs project permissions
2. **Status field name mismatch** - Project board must have "Status" field
3. **Column name mismatch** - Column names must exactly match mapping

**Fix**:
- Verify PROJECTS_TOKEN exists: Settings → Secrets → PROJECTS_TOKEN
- Check project board has "Status" field with correct column names
- Review workflow logs for specific error

---

### Issue: Sync Loop Detected

**Symptom**: Multiple rapid updates, duplicate comments

**Diagnosis**:
```bash
# Check for rapid successive runs
gh run list --workflow=project-to-issue-sync.yml --limit 10
gh run list --workflow=issue-to-project-sync.yml --limit 10
```

**Common Causes**:
1. **Concurrency not working** - Multiple workflows running simultaneously
2. **Custom workflow** - Another workflow modifying issues/board

**Fix**:
- Verify concurrency groups in workflow YAML
- Check for other custom workflows that modify status
- Review recent workflow runs for timing

---

### Issue: Status Out of Sync

**Symptom**: Issue label shows "In Progress" but board shows "Ready"

**Diagnosis**:
```bash
# Check issue labels
gh issue view 123 --json labels

# Check project item status (requires GraphQL query)
```

**Manual Sync**:
```bash
# Option 1: Update issue label (triggers board sync)
gh issue edit 123 --remove-label "status: ready"
gh issue edit 123 --add-label "status: in-progress"

# Option 2: Move on project board (triggers issue sync)
# Use GitHub UI to move issue to correct column
```

---

### Issue: Permissions Error

**Symptom**: "403 Forbidden" or "Resource not accessible"

**Common Causes**:
1. **PROJECTS_TOKEN missing/invalid** - Token expired or lacks permissions
2. **Wrong token scopes** - Token needs `repo` and `project` scopes

**Fix**:
1. Generate new Personal Access Token:
   - Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Scopes: `repo`, `project`
2. Update repository secret:
   - Repository → Settings → Secrets → Actions → PROJECTS_TOKEN
3. Re-trigger workflow

---

## Advanced Usage

### Custom Status Workflows

**Add Custom Status Labels**:
```bash
gh label create "status: blocked" --color "d73a4a" --description "Blocked by external dependency"
```

**Update Workflow Mapping**:
Edit `.github/workflows/project-to-issue-sync.yml`:
```yaml
case "$STATUS" in
  # ... existing mappings ...
  "Blocked")
    NEW_LABEL="status: blocked"
    ;;
esac
```

---

### Integration with Other Workflows

**Example: Auto-assign on status change**

Edit `.github/workflows/project-to-issue-sync.yml`, add after Step 4:

```bash
# Auto-assign when moved to "In Progress"
if [ "$STATUS" = "In Progress" ]; then
  # Get who moved it
  ASSIGNEE="${{ github.event.sender.login }}"
  gh issue edit $ISSUE_NUMBER --add-assignee "$ASSIGNEE"
fi
```

---

### Bulk Status Updates

**Update Multiple Issues**:
```bash
# Move all "triage" issues to "backlog"
for issue in $(gh issue list --label "status: triage" --json number --jq '.[].number'); do
  gh issue edit $issue --remove-label "status: triage"
  gh issue edit $issue --add-label "status: backlog"
  echo "Updated issue #$issue"
done
```

The `issue-to-project-sync` workflow will automatically update the project board for each issue.

---

### Status Reports

**Generate Status Report**:
```bash
echo "## Team Status Report - $(date)"
echo ""
echo "### In Progress"
gh issue list --label "status: in-progress" --json number,title,assignees
echo ""
echo "### In Review"
gh issue list --label "status: in-review" --json number,title,assignees
echo ""
echo "### Ready"
gh issue list --label "status: ready" --json number,title --limit 5
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Project Board                      │
│                  @claude-skills-factory (#7)                 │
│                                                              │
│  To triage → Backlog → Ready → In Progress → In Review → Done│
│      ↓          ↓        ↓          ↓            ↓         ↓ │
└──────┼──────────┼────────┼──────────┼────────────┼─────────┼─┘
       │          │        │          │            │         │
       │    project-to-issue-sync.yml (Board → Issue)       │
       │          │        │          │            │         │
       ↓          ↓        ↓          ↓            ↓         ↓
┌──────────────────────────────────────────────────────────────┐
│                      GitHub Issues                           │
│                                                              │
│  status:      status:    status:   status:      status:    status:│
│  triage       backlog    ready     in-progress  in-review  done   │
│  (open)       (open)     (open)    (open)       (open)     (closed)│
│      ↑          ↑         ↑          ↑            ↑          ↑    │
└──────┼──────────┼─────────┼──────────┼────────────┼──────────┼────┘
       │          │         │          │            │          │
       │     issue-to-project-sync.yml (Issue → Board)        │
       │          │         │          │            │          │
       └──────────┴─────────┴──────────┴────────────┴──────────┘

         Concurrency Controls Prevent Sync Loops
```

---

## Configuration Reference

### Required Secrets

| Secret | Required Scopes | Used By | Purpose |
|--------|----------------|---------|---------|
| `CLAUDE_CODE_OAUTH_TOKEN` | - | Both workflows | Claude Code action authentication |
| `PROJECTS_TOKEN` | `repo`, `project` | Both workflows | Project board access |

### Required Labels

All status labels are automatically created. Manual creation:

```bash
gh label create "status: triage" --color "fbca04" --description "To Triage column"
gh label create "status: backlog" --color "d4c5f9" --description "Backlog column"
gh label create "status: ready" --color "0e8a16" --description "Ready column"
gh label create "status: in-progress" --color "1d76db" --description "In Progress column"
gh label create "status: in-review" --color "d876e3" --description "In Review column"
gh label create "status: done" --color "2ea44f" --description "Done column"
```

---

## Related Documentation

- [Issue Auto-Triage](ISSUE_AUTO_TRIAGE.md) - Automatic issue classification
- [Plan-to-Issues](PLAN_TO_ISSUES.md) - Plan automation
- [Project Integration Setup](PROJECT_INTEGRATION_SETUP.md) - Token configuration
- [Security Model](SECURITY.md) - Security and access control

---

## Support

**Issues with sync**:
1. Check workflow runs: `gh run list --workflow=project-to-issue-sync.yml`
2. Review logs: `gh run view <run-id> --log`
3. Verify tokens: Settings → Secrets → Actions
4. Check project board structure: Must have "Status" field with exact column names

**Feature requests**:
- Open issue with `enhancement` label
- Describe desired sync behavior
- Include use case and team workflow context

---

**Last Updated**: 2025-10-24
**Version**: 1.0.0
**Status**: Production Ready
