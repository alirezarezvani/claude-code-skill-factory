---
description: Convert TodoWrite task list to GitHub plan issue (triggers automation)
argument-hint: "<plan-title>"
---

## Purpose
Efficiently convert current TodoWrite tasks into a GitHub plan issue. Existing workflows handle task creation automatically.

## Usage

```bash
/sync-todos-to-github "Sprint 5 - User Authentication"
/sync-todos-to-github "Feature: Payment Integration" --dry-run
```

## Process

### Step 1: Prepare Todo List
**From TodoWrite**: Copy your current task list and format as markdown checklist:
```markdown
- [ ] Task 1: Implement authentication
- [ ] Task 2: Add password reset
- [ ] Task 3: Create login UI
- [ ] Task 4: Add JWT tokens
- [ ] Task 5: Write auth tests
```

**Requirements**:
- Minimum: 5 tasks
- Maximum: 10 tasks
- Format: `- [ ] Task description`

### Step 2: Set Plan Details
```bash
PLAN_TITLE="$1"  # From command argument
REPO="alirezarezvani/claude-code-skill-factory"

# Validate title provided
if [ -z "$PLAN_TITLE" ]; then
  echo "❌ Error: Plan title required"
  echo "Usage: /sync-todos-to-github \"Plan Title\""
  exit 1
fi

# Check if dry-run mode
DRY_RUN=false
if [[ "$2" == "--dry-run" ]]; then
  DRY_RUN=true
fi
```

### Step 3: Get Todo List (Interactive)
```bash
echo "📋 Paste your todo list (markdown checklist format):"
echo "Example:"
echo "- [ ] Task 1"
echo "- [ ] Task 2"
echo ""
echo "Enter checklist (Ctrl+D when done):"

# Read multiline input
TODO_LIST=$(cat)

# Validate format and count
TASK_COUNT=$(echo "$TODO_LIST" | grep -c "^- \[ \]" || echo "0")

if [ "$TASK_COUNT" -lt 5 ]; then
  echo "❌ Error: Minimum 5 tasks required (found: $TASK_COUNT)"
  echo "💡 Tip: Combine small tasks or add more scope"
  exit 1
fi

if [ "$TASK_COUNT" -gt 10 ]; then
  echo "❌ Error: Maximum 10 tasks allowed (found: $TASK_COUNT)"
  echo "💡 Tip: Split into $(( ($TASK_COUNT + 9) / 10 )) separate plans"
  echo ""
  echo "Example:"
  echo "  Plan 1: Tasks 1-10"
  echo "  Plan 2: Tasks 11-$TASK_COUNT"
  exit 1
fi

echo "✅ Validated: $TASK_COUNT tasks"
```

### Step 4: Create Goal Description
```bash
echo ""
echo "📝 Enter goal/context (single line, Ctrl+D when done):"
GOAL=$(cat)

if [ -z "$GOAL" ]; then
  GOAL="Complete the tasks listed below."
fi
```

### Step 5: Preview (Always Show Before Creating)
```bash
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 PLAN PREVIEW"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Title: Plan: $PLAN_TITLE"
echo "Tasks: $TASK_COUNT"
echo ""
echo "Goal:"
echo "$GOAL"
echo ""
echo "Tasks:"
echo "$TODO_LIST"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ "$DRY_RUN" = true ]; then
  echo ""
  echo "🔍 DRY RUN MODE - No issue created"
  echo "Command would create plan issue with $TASK_COUNT tasks"
  exit 0
fi

echo ""
read -p "Create this plan issue? (y/N): " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
  echo "❌ Cancelled"
  exit 0
fi
```

### Step 6: Create Plan Issue (Efficient REST API)
```bash
echo ""
echo "🚀 Creating plan issue..."

# Build issue body
ISSUE_BODY="## Goal
$GOAL

## Tasks
$TODO_LIST

## Acceptance Criteria
- [ ] All tasks completed
- [ ] Tests passing
- [ ] Documentation updated

---
**Created**: $(date -u +"%Y-%m-%d %H:%M UTC")
**Source**: TodoWrite sync
**Tasks**: $TASK_COUNT"

# Create issue using REST API (1 rate limit point vs 5 for GraphQL)
ISSUE_NUMBER=$(gh api "repos/$REPO/issues" \
  --method POST \
  --field title="Plan: $PLAN_TITLE" \
  --field body="$ISSUE_BODY" \
  --raw-field 'labels=["plan"]' \
  --jq '.number' 2>&1)

# Check for errors
if ! [[ "$ISSUE_NUMBER" =~ ^[0-9]+$ ]]; then
  echo "❌ Error creating issue:"
  echo "$ISSUE_NUMBER"
  exit 1
fi
```

### Step 7: Confirmation & Next Steps
```bash
echo ""
echo "✅ SUCCESS!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 Plan Issue Created: #$ISSUE_NUMBER"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔗 URL: https://github.com/$REPO/issues/$ISSUE_NUMBER"
echo ""
echo "🤖 Automation Pipeline (starts automatically):"
echo "   1. plan-validator.yml validates task count & rate limits (~30s)"
echo "   2. plan-to-tasks.yml creates $TASK_COUNT task issues (~2min)"
echo "   3. smart-sync.yml adds all to project board (~30s)"
echo "   4. Total time: ~3 minutes"
echo ""
echo "📊 What happens next:"
echo "   • $TASK_COUNT TASK issues will be created automatically"
echo "   • Each task gets labels: task, plan-item, skip-triage"
echo "   • All added to project board column: To triage"
echo "   • Parent plan gets comment with task links"
echo ""
echo "💡 Optional task breakdown:"
echo "   • To create subtasks: Add 'needs-subtasks' label to any task"
echo "   • Add checklist to task body (max 5 subtasks)"
echo "   • task-to-subtasks.yml creates subtask issues automatically"
echo ""
echo "🎯 Monitor progress:"
echo "   gh issue view $ISSUE_NUMBER"
echo "   gh run list --workflow 'Plan to Tasks'"
echo ""
```

## Efficiency Notes

**API Calls (This Command)**:
- 1 REST API call (`gh api`) = 1 rate limit point
- Total: 1 point per sync (very efficient)

**GitHub Actions Consumption**:
- This command: 0 minutes (runs locally)
- Triggered workflows: ~2-3 minutes total
  - plan-validator: ~30s
  - plan-to-tasks: ~2min (depends on task count)
  - smart-sync: ~30s (per task)

**Rate Limit Budget**:
- REST API: 5000/hour
- This command: 1 point
- Automation: ~5-10 points per plan
- Can sync 500+ plans/hour safely

## Developer Best Practices

### When to Use
✅ **Good use cases**:
- End of day: sync session work to GitHub
- Sprint planning: convert plan to trackable tasks
- Checkpoint: preserve TodoWrite state to issues

❌ **Avoid**:
- Every small task (use regular issues)
- <5 tasks (not worth automation overhead)
- >10 tasks (split into multiple plans)

### Optimization Tips
1. **Batch work**: Sync once per day, not per task
2. **Combine tasks**: Merge small todos to reach 5 minimum
3. **Split large plans**: Keep under 10 tasks to avoid rate limits
4. **Use dry-run**: Preview before creating (`--dry-run`)

### Error Handling
```bash
# Check authentication
gh auth status || {
  echo "❌ Not authenticated. Run: gh auth login"
  exit 1
}

# Check rate limits before creating
RATE_LIMIT=$(gh api rate_limit --jq '.resources.core.remaining')
if [ "$RATE_LIMIT" -lt 10 ]; then
  echo "⚠️  Warning: Low rate limits ($RATE_LIMIT remaining)"
  echo "Consider waiting before syncing"
fi
```

## Examples

### Example 1: Sprint Planning
```bash
/sync-todos-to-github "Sprint 12 - Payment System"

# Paste checklist:
- [ ] Design payment flow diagram
- [ ] Implement Stripe integration
- [ ] Add payment webhook handlers
- [ ] Create invoice generation
- [ ] Add payment history UI
- [ ] Write integration tests
- [ ] Update documentation

# Result: Plan #123 with 7 task issues created
```

### Example 2: Feature Development
```bash
/sync-todos-to-github "Feature: Real-time Notifications" --dry-run

# Preview without creating
# Verify task count and format
# Then run without --dry-run when ready
```

## Troubleshooting

**"Minimum 5 tasks required"**
→ Add more tasks or combine small ones

**"Maximum 10 tasks allowed"**
→ Split into 2-3 smaller plans

**"Error creating issue"**
→ Check `gh auth status` and network connection

**"Rate limit too low"**
→ Wait for reset or reduce automation usage

## Related Commands

- `/review` - Validate code before creating plan
- `/project-status` - Check current plans and tasks
- `/check-docs` - Verify documentation before planning

---

**Efficiency**: 1 API call | 0 Actions minutes | ~3min automation
**Best for**: 5-10 task plans | Sprint planning | Daily checkpoints
