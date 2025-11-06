#!/bin/bash
#
# install-hook.sh - Install Claude Code hooks to settings.json
#
# Usage:
#   ./install-hook.sh /path/to/hook-folder user
#   ./install-hook.sh /path/to/hook-folder project
#
# Requirements:
#   - jq (JSON processor)
#   - macOS or Linux
#
# Features:
#   - Automatic backup with timestamp
#   - JSON validation before/after
#   - Atomic write (temp file → rename)
#   - Rollback on failure
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check dependencies
if ! command -v jq &> /dev/null; then
    echo -e "${RED}❌ Error: jq is not installed${NC}"
    echo ""
    echo "Install jq:"
    echo "  macOS:  brew install jq"
    echo "  Ubuntu: sudo apt-get install jq"
    echo "  Fedora: sudo dnf install jq"
    exit 1
fi

# Parse arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <hook-folder> <user|project>"
    echo ""
    echo "Examples:"
    echo "  $0 ./generated-hooks/my-hook user     # Install to ~/.claude/settings.json"
    echo "  $0 ./generated-hooks/my-hook project  # Install to .claude/settings.json"
    exit 1
fi

HOOK_PATH="$1"
LEVEL="$2"

# Validate level
if [ "$LEVEL" != "user" ] && [ "$LEVEL" != "project" ]; then
    echo -e "${RED}❌ Error: Level must be 'user' or 'project'${NC}"
    exit 1
fi

# Determine settings.json path
if [ "$LEVEL" = "user" ]; then
    SETTINGS_PATH="$HOME/.claude/settings.json"
else
    SETTINGS_PATH=".claude/settings.json"
fi

# Validate hook path
if [ ! -d "$HOOK_PATH" ]; then
    echo -e "${RED}❌ Error: Hook folder not found: $HOOK_PATH${NC}"
    exit 1
fi

HOOK_JSON="$HOOK_PATH/hook.json"
if [ ! -f "$HOOK_JSON" ]; then
    echo -e "${RED}❌ Error: hook.json not found in $HOOK_PATH${NC}"
    exit 1
fi

# Validate hook.json syntax
if ! jq empty "$HOOK_JSON" 2>/dev/null; then
    echo -e "${RED}❌ Error: Invalid JSON in $HOOK_JSON${NC}"
    exit 1
fi

# Extract hook name
HOOK_NAME=$(basename "$HOOK_PATH")

echo -e "${BLUE}📦 Installing hook: $HOOK_NAME${NC}"
echo -e "${BLUE}📍 Location: $SETTINGS_PATH${NC}"

# Determine event type from hook.json (top-level key)
EVENT_TYPE=$(jq -r 'keys[0]' "$HOOK_JSON")
echo -e "${GREEN}🎯 Event type: $EVENT_TYPE${NC}"

# Create .claude directory if needed
SETTINGS_DIR=$(dirname "$SETTINGS_PATH")
mkdir -p "$SETTINGS_DIR"

# Backup existing settings.json
if [ -f "$SETTINGS_PATH" ]; then
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    BACKUP_PATH="${SETTINGS_PATH}.backup.${TIMESTAMP}"

    cp "$SETTINGS_PATH" "$BACKUP_PATH"
    echo -e "${GREEN}✅ Backup created: $BACKUP_PATH${NC}"

    # Keep only last 5 backups
    BACKUP_COUNT=$(find "$SETTINGS_DIR" -name "settings.json.backup.*" | wc -l | tr -d ' ')
    if [ "$BACKUP_COUNT" -gt 5 ]; then
        echo -e "${YELLOW}🗑️  Cleaning up old backups...${NC}"
        find "$SETTINGS_DIR" -name "settings.json.backup.*" -type f | sort | head -n -5 | xargs rm -f
    fi
else
    # Create minimal settings structure
    echo '{"hooks":{}}' > "$SETTINGS_PATH"
    echo -e "${GREEN}✅ Created new settings.json${NC}"
    BACKUP_PATH=""
fi

# Validate settings.json syntax
if ! jq empty "$SETTINGS_PATH" 2>/dev/null; then
    echo -e "${RED}❌ Error: Invalid JSON in $SETTINGS_PATH${NC}"
    exit 1
fi

# Create temporary file for atomic write
TMP_SETTINGS=$(mktemp)
trap "rm -f $TMP_SETTINGS" EXIT

# Merge hook into settings.json
# 1. Ensure hooks key exists
# 2. Ensure event type key exists
# 3. Extract hook entry from hook.json
# 4. Append to event type array

jq --slurpfile hook_data "$HOOK_JSON" \
   --arg event_type "$EVENT_TYPE" \
   '
   # Ensure hooks key exists
   if .hooks == null then .hooks = {} else . end |

   # Ensure event type array exists
   if .hooks[$event_type] == null then .hooks[$event_type] = [] else . end |

   # Append hook from hook_data
   .hooks[$event_type] += $hook_data[0][$event_type]
   ' "$SETTINGS_PATH" > "$TMP_SETTINGS"

# Validate merged JSON
if ! jq empty "$TMP_SETTINGS" 2>/dev/null; then
    echo -e "${RED}❌ Error: Merge failed - invalid JSON generated${NC}"

    # Rollback if backup exists
    if [ -n "$BACKUP_PATH" ] && [ -f "$BACKUP_PATH" ]; then
        echo -e "${YELLOW}🔄 Rolling back from backup...${NC}"
        cp "$BACKUP_PATH" "$SETTINGS_PATH"
    fi

    exit 1
fi

# Atomic write (rename is atomic operation)
mv "$TMP_SETTINGS" "$SETTINGS_PATH"

echo -e "${GREEN}✅ Hook installed successfully!${NC}"
echo -e "${GREEN}📝 Hook name: $HOOK_NAME${NC}"
echo -e "${GREEN}🎯 Event type: $EVENT_TYPE${NC}"
echo -e "${GREEN}📍 Location: $LEVEL ($SETTINGS_PATH)${NC}"
echo ""
echo "ℹ️  Restart Claude Code to activate the hook"
