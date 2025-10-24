#!/usr/bin/env bash

###########################################
# EMERGENCY CLEANUP SCRIPT
# Closes spam issues created by workflows
###########################################

set -e

echo "🚨 EMERGENCY: Cleaning up spam issues"
echo ""

# Configuration
CUTOFF_DATE="2025-10-24T14:00:00Z"  # Issues created after this time
BATCH_SIZE=50  # Process in batches to avoid rate limits
DRY_RUN=${1:-"false"}  # Pass "false" as first argument to actually close issues

if [ "$DRY_RUN" = "true" ]; then
  echo "⚠️  DRY RUN MODE - No issues will be closed"
  echo ""
fi

# Get all issues created after cutoff date
echo "📊 Finding spam issues created after $CUTOFF_DATE..."
SPAM_ISSUES=$(gh issue list \
  --limit 500 \
  --json number,createdAt,title,labels \
  --jq ".[] | select(.createdAt > \"$CUTOFF_DATE\") | select(.labels | any(.name == \"plan-item\")) | .number")

if [ -z "$SPAM_ISSUES" ]; then
  echo "✅ No spam issues found!"
  exit 0
fi

# Count issues
ISSUE_COUNT=$(echo "$SPAM_ISSUES" | wc -l | tr -d ' ')
echo "Found $ISSUE_COUNT spam issues to close"
echo ""

if [ "$DRY_RUN" = "true" ]; then
  echo "Would close the following issues:"
  echo "$SPAM_ISSUES" | head -20
  if [ "$ISSUE_COUNT" -gt 20 ]; then
    echo "... and $((ISSUE_COUNT - 20)) more"
  fi
  exit 0
fi

# Confirm before proceeding
read -p "⚠️  Close $ISSUE_COUNT issues? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
  echo "❌ Cancelled"
  exit 1
fi

# Close issues in batches
echo ""
echo "🗑️  Closing issues in batches of $BATCH_SIZE..."
count=0
total=0

for issue_num in $SPAM_ISSUES; do
  count=$((count + 1))
  total=$((total + 1))

  echo -n "  Closing #$issue_num... "
  gh issue close $issue_num --reason "not planned" --comment "🤖 Automatically closed: Created by misconfigured workflow" 2>/dev/null && echo "✅" || echo "❌"

  # Rate limit protection: pause after each batch
  if [ $((count % BATCH_SIZE)) -eq 0 ]; then
    echo ""
    echo "  ⏸️  Paused after $total issues (rate limit protection)..."
    sleep 5
    echo "  ▶️  Resuming..."
    count=0
  fi
done

echo ""
echo "✅ Cleanup complete! Closed $total issues"
echo ""
echo "📋 Next steps:"
echo "  1. Disable problematic workflows"
echo "  2. Fix workflow bugs"
echo "  3. Test on feature branch before merging to main"
