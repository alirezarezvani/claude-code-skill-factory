# Desktop Notification Hook

Send native desktop notifications when agents complete tasks (macOS/Linux).

## What This Hook Does

- Displays desktop notification when agent finishes
- Plays sound alert (optional)
- Works on macOS (osascript) and Linux (notify-send)
- Non-intrusive, fast (<5 seconds)

## Event Type

**SubagentStop** - Triggers when agent completes its task (NON-BLOCKING)

## Installation

### Automatic
```bash
# User-level (all projects)
cp -r examples/desktop-notify ~/.claude/hooks/

# Project-level (this project only)
cp -r examples/desktop-notify .claude/hooks/
```

### Manual
Add `hook.json` content to `SubagentStop` array in settings.json

## Platform Requirements

**macOS**: Built-in support (osascript)
```bash
# Test notification:
osascript -e 'display notification "Test" with title "Test"'
```

**Linux**: Requires `notify-send` (usually pre-installed)
```bash
# Check if installed:
which notify-send

# Install if needed (Ubuntu/Debian):
sudo apt-get install libnotify-bin

# Install if needed (Fedora):
sudo dnf install libnotify

# Test notification:
notify-send "Test" "Test message"
```

## How It Works

1. **Platform Detection**: Checks `$OSTYPE` for macOS or Linux
2. **macOS**: Uses `osascript` with system sound ("Glass")
3. **Linux**: Uses `notify-send` command
4. **Fast**: Completes in <5 seconds

## Example Output

**macOS**: Native notification with "Glass" sound
**Linux**: System notification popup
**Console**: `Desktop notifications not supported on this platform` (if neither)

## Customization

### Change Sound (macOS)

Edit `hook.json` to use different sound:
```bash
# Available sounds: Basso, Blow, Bottle, Frog, Funk, Glass, Hero, Morse, Ping, Pop, Purr, Sosumi, Submarine, Tink
osascript -e 'display notification \"Agent completed\" with title \"Claude Code\" sound name \"Hero\"'
```

### Change Notification Text

Edit message in `hook.json`:
```bash
osascript -e 'display notification \"Your custom message here\" with title \"Custom Title\"'
```

### Add Critical Alert (Linux)

For urgent notifications:
```bash
notify-send -u critical \"Claude Code\" \"Agent completed with errors\"
```

### Use for Test Results

Change matcher and logic for test-specific notifications:
```json
{
  "matcher": {
    "tool_names": ["Bash"]
  },
  "hooks": [
    {
      "type": "command",
      "command": "if [ $? -eq 0 ]; then\n    osascript -e 'display notification \"Tests passed\" with title \"Test Results\" sound name \"Glass\"'\nelse\n    osascript -e 'display notification \"Tests failed\" with title \"Test Results\" sound name \"Basso\"'\nfi"
    }
  ]
}
```

## Use Cases

- **Long-Running Tasks**: Get notified when agent finishes
- **Background Work**: Know when Claude completes while you work elsewhere
- **Test Results**: Immediate feedback on test pass/fail
- **Build Status**: Notification when builds complete

## Safety Notes

- **Non-Blocking**: Won't slow down Claude
- **Fast**: <5 seconds execution
- **Silent Fallback**: No error if notifications unavailable
- **Platform-Specific**: macOS/Linux only (not Windows)

## Testing

1. **Test macOS Notification**:
   ```bash
   osascript -e 'display notification "Test notification" with title "Test" sound name "Glass"'
   ```

2. **Test Linux Notification**:
   ```bash
   notify-send "Test" "Test notification"
   ```

3. **Test With Agent**:
   ```bash
   # Run an agent task in Claude Code
   # Should see desktop notification when agent completes
   ```

## Troubleshooting

**No notification on macOS:**
- Check System Preferences > Notifications > Terminal/Claude Code
- Enable "Allow Notifications"
- Test with manual osascript command

**No notification on Linux:**
- Check notify-send is installed: `which notify-send`
- Install libnotify-bin if missing
- Check notification daemon is running

**Notification appears but no sound (macOS):**
- Check System Preferences > Sound > Sound Effects
- Verify volume is not muted
- Test with: `afplay /System/Library/Sounds/Glass.aiff`

**Too many notifications:**
- Change matcher to be more specific
- Only notify on specific agents
- Add rate limiting (once per minute)

**Want Windows support:**
- Windows not supported (excluded from Phase 2)
- Consider using WSL with Linux notifications
