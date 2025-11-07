# Session Cleanup Hook

Automatically clean up resources and save state when Claude Code session ends.

## What This Hook Does

- Saves session end timestamp to `.claude/session_history.txt`
- Records git status at session end
- Cleans up old temporary files (>1 day old)
- Removes `.tmp` files from project
- Fast cleanup (<30 seconds)

## Event Type

**Stop** - Triggers once when session ends normally (NON-BLOCKING)

## Installation

### Automatic
```bash
# User-level (all projects)
cp -r examples/session-cleanup ~/.claude/hooks/

# Project-level (this project only)
cp -r examples/session-cleanup .claude/hooks/
```

### Manual
Add `hook.json` content to `Stop` array in settings.json

## How It Works

1. **Session Log**: Appends session end time to `.claude/session_history.txt`
2. **Git Status**: Records working tree status if in git repo
3. **Temp Cleanup**: Removes old `/tmp/claude-*` files (>1 day)
4. **Local Cleanup**: Deletes `*.tmp` files in project

## Example Output

```
Session cleanup complete
```

**Session History** (`.claude/session_history.txt`):
```
Session ended: Wed Nov  6 14:30:25 PST 2025
Git status at end:
 M generated-skills/hook-factory/templates.json
 M documentation/delivery/hook-factory-phase-2/plan.md
---
Session ended: Wed Nov  6 16:15:42 PST 2025
Git status at end:
---
```

## Customization

### Add Backup on Exit

Edit `hook.json` to backup modified files:
```bash
# Backup modified files
if git rev-parse --git-dir &> /dev/null; then\n    BACKUP_DIR=\".claude/backups/$(date +%Y%m%d_%H%M%S)\"\n    mkdir -p \"$BACKUP_DIR\"\n    git diff --name-only | while read file; do\n        if [ -f \"$file\" ]; then\n            cp \"$file\" \"$BACKUP_DIR/\" 2>/dev/null || exit 0\n        fi\n    done\nfi
```

### Generate Session Summary

Add summary generation:
```bash
# Generate session summary
if git rev-parse --git-dir &> /dev/null; then\n    echo \"# Session Summary - $(date)\" > .claude/session_summary.md\n    echo \"## Files Modified\" >> .claude/session_summary.md\n    git diff --name-only >> .claude/session_summary.md\nfi
```

### View Session History

```bash
cat .claude/session_history.txt           # All sessions
tail -20 .claude/session_history.txt      # Last 20 entries
grep "Session ended" .claude/session_history.txt | tail -10  # Last 10 sessions
```

## Use Cases

- **Session Tracking**: Know when you worked on project
- **Git History**: See what was modified each session
- **Cleanup**: Keep project and /tmp clean
- **Backup**: Optional backup of modified files

## Safety Notes

- **Non-Blocking**: Won't prevent Claude from closing
- **Safe Operations**: Uses silent failure (`|| exit 0`)
- **Fast**: Should complete in <30 seconds
- **Local Only**: Only cleans local files, not remote

## Testing

1. **Test Session Logging**:
   ```bash
   # Close Claude Code session
   # Check log:
   cat .claude/session_history.txt
   ```

2. **Test Temp Cleanup**:
   ```bash
   touch /tmp/claude-test-old
   touch -t 202501010000 /tmp/claude-test-old  # Make it old
   # Close session
   ls /tmp/claude-test-old  # Should be gone
   ```

3. **Test Local Cleanup**:
   ```bash
   touch test.tmp
   # Close session
   ls test.tmp  # Should be gone
   ```

## Troubleshooting

**Session not logged:**
- Check hook is in `Stop` section (not PostToolUse)
- Verify `.claude/` directory exists and is writable
- Check session actually ended normally (not crashed)

**Temp files not cleaned:**
- Check permissions on /tmp directory
- Verify files are >1 day old (mtime +1)
- Check filename matches pattern `claude-*`

**Too slow:**
- Reduce timeout from 30s to 15s
- Remove temp cleanup if not needed
- Skip git status recording

**Cleanup too aggressive:**
- Change `mtime +1` to `mtime +7` (keep files 7 days)
- Remove `*.tmp` cleanup if needed
- Add specific exclusions
