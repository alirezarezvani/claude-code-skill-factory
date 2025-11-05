#!/bin/bash

# Auto-sync approved plan to GitHub issues
# Triggered when ExitPlanMode is called

set -e

PLAN_CONTENT="${1:-}"
PLAN_TITLE="${2:-Approved Plan}"
REPO="alirezarezvani/claude-code-skill-factory"
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="/tmp/auto-sync-plan-$(date +%Y%m%d-%H%M%S).log"

# Logging
log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
log "🤖 Auto-Sync: Plan Approved → GitHub"
log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if gh CLI is authenticated
if ! gh auth status &>/dev/null; then
  log "❌ GitHub CLI not authenticated. Run: gh auth login"
  exit 1
fi

# Extract TodoWrite tasks from plan content
# Look for markdown checklists in the plan
extract_todos() {
  local content="$1"

  # Extract lines that look like checklist items
  echo "$content" | grep -E '^\s*-\s*\[\s*\]\s*' | sed 's/^\s*//' || true
}

# Extract file references from plan content
# Looks for patterns like: src/file.ts, folder/, *.tsx
extract_file_references() {
  local content="$1"

  # Find file patterns (improved regex)
  echo "$content" | grep -oE '`[^`]+\.(ts|tsx|js|jsx|py|md|json|yml|yaml|sh|css|html)`|[a-zA-Z0-9_/-]+/[a-zA-Z0-9_.-]+\.(ts|tsx|js|jsx|py|md|json|yml|yaml|sh|css|html)' | \
    sed 's/`//g' | sort -u || true
}

# Extract folder references from plan content
extract_folder_references() {
  local content="$1"

  # Find folder patterns
  echo "$content" | grep -oE '`[a-zA-Z0-9_/-]+/`|[a-zA-Z0-9_/-]+/' | \
    sed 's/`//g' | sort -u || true
}

# Build enhanced task list with file references
build_enhanced_tasks() {
  local todos="$1"
  local files="$2"
  local folders="$3"

  echo "$todos"

  if [ -n "$files" ] || [ -n "$folders" ]; then
    echo ""
    echo "## File References"
    echo ""

    if [ -n "$files" ]; then
      echo "**Files**:"
      while IFS= read -r file; do
        [ -n "$file" ] && echo "- \`$file\`"
      done <<< "$files"
      echo ""
    fi

    if [ -n "$folders" ]; then
      echo "**Folders**:"
      while IFS= read -r folder; do
        [ -n "$folder" ] && echo "- \`$folder\`"
      done <<< "$folders"
    fi
  fi
}

# Main sync logic
main() {
  log "Plan Title: $PLAN_TITLE"

  # Extract todos
  TODO_LIST=$(extract_todos "$PLAN_CONTENT")
  TASK_COUNT=$(echo "$TODO_LIST" | grep -c "^- \[ \]" || echo "0")

  log "Tasks found: $TASK_COUNT"

  # Validate task count
  if [ "$TASK_COUNT" -lt 5 ]; then
    log "⚠️  Warning: Only $TASK_COUNT tasks (minimum 5 required)"
    log "Skipping auto-sync. Use /sync-todos-to-github manually if needed."
    exit 0
  fi

  if [ "$TASK_COUNT" -gt 10 ]; then
    log "⚠️  Warning: $TASK_COUNT tasks (maximum 10 allowed)"
    log "Skipping auto-sync. Split into multiple plans manually."
    exit 0
  fi

  # Extract file and folder references
  FILES=$(extract_file_references "$PLAN_CONTENT")
  FOLDERS=$(extract_folder_references "$PLAN_CONTENT")

  log "Files referenced: $(echo "$FILES" | wc -l | tr -d ' ')"
  log "Folders referenced: $(echo "$FOLDERS" | wc -l | tr -d ' ')"

  # Build enhanced task list
  ENHANCED_TASKS=$(build_enhanced_tasks "$TODO_LIST" "$FILES" "$FOLDERS")

  # Extract goal from plan (first paragraph or use default)
  GOAL=$(echo "$PLAN_CONTENT" | head -n 5 | grep -v "^#" | grep -v "^-" | grep -v "^\s*$" | head -n 1)
  [ -z "$GOAL" ] && GOAL="Complete the approved plan tasks with file references."

  # Build issue body
  ISSUE_BODY="## Goal
$GOAL

## Tasks
$ENHANCED_TASKS

## Acceptance Criteria
- [ ] All tasks completed
- [ ] Tests passing
- [ ] Documentation updated
- [ ] File changes reviewed

---
**Created**: $(date -u +"%Y-%m-%d %H:%M UTC")
**Source**: Auto-sync from approved plan
**Tasks**: $TASK_COUNT
**Auto-synced**: Yes"

  log "Creating GitHub plan issue..."

  # Create issue using gh CLI
  ISSUE_URL=$(gh issue create \
    --repo "$REPO" \
    --title "Plan: $PLAN_TITLE" \
    --label "plan" \
    --body "$ISSUE_BODY" 2>&1)

  ISSUE_NUMBER=$(echo "$ISSUE_URL" | grep -oE '[0-9]+$')

  if [ -z "$ISSUE_NUMBER" ]; then
    log "❌ Error creating issue:"
    log "$ISSUE_URL"
    exit 1
  fi

  log "✅ SUCCESS!"
  log ""
  log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  log "📋 Plan Issue Created: #$ISSUE_NUMBER"
  log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  log "🔗 URL: $ISSUE_URL"
  log ""
  log "🤖 Automation will create $TASK_COUNT TASK issues (~3 min)"
  log "📊 Each task will include file references"
  log "💾 Log saved: $LOG_FILE"
  log ""
}

main