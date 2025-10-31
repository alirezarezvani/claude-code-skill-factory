# /install-hook - Install Generated Hook to Settings

**Install a generated hook to Claude Code settings (user-level or project-level).**

---

## Usage

```
/install-hook generated-hooks/my-hook
/install-hook generated-hooks/my-hook user
/install-hook generated-hooks/my-hook project
```

---

## What This Command Does

Installs hook.json configuration to:
- **User-level** (`~/.claude/settings.json`) - Applies to all projects
- **Project-level** (`.claude/settings.json`) - Current project only

**Installation process**:
1. ✅ Validates hook.json structure
2. ✅ Checks for safety violations
3. ✅ Backs up existing settings.json
4. ✅ Merges with existing hooks (preserves other settings)
5. ✅ Saves and displays confirmation

---

## Examples

### Install User-Level Hook (All Projects)

```
/install-hook generated-hooks/auto-format-python user
```

**Performs**:
1. Reads `generated-hooks/auto-format-python/hook.json`
2. Validates JSON structure and safety
3. Creates backup: `~/.claude/settings.json.backup`
4. Opens `~/.claude/settings.json`
5. Adds hook to appropriate event type section
6. Saves changes

**Output**:
```
Installing hook: auto-format-python
Location: User-level (~/.claude/settings.json)

✅ Hook validation PASSED
   - JSON structure: Valid
   - Safety checks: All passed
   - Event type: PostToolUse

Creating backup...
✅ Backup created: ~/.claude/settings.json.backup

Installing to PostToolUse hooks...
✅ Hook installed successfully!

Event type: PostToolUse
Matcher: tool_names=["Write", "Edit"], paths=["**/*.py"]
Command: Auto-format Python with Black

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next steps:
1. Restart Claude Code (required)
2. Test by editing a .py file
3. Verify hook runs automatically

To test:
claude --continue
> Edit any Python file
> Check if Black formatting runs
```

---

### Install Project-Level Hook (Current Project Only)

```
/install-hook generated-hooks/test-runner project
```

**Installs to**: `.claude/settings.json` (current project)

**Output**:
```
Installing hook: test-runner
Location: Project-level (.claude/settings.json)

✅ Hook validation PASSED
✅ Backup created: .claude/settings.json.backup
✅ Hook installed successfully!

Event type: SubagentStop
Matcher: (empty - runs for all agents)
Command: Run pytest after agent completes

This hook will only run in this project.

Next steps:
1. Restart Claude Code
2. Run any Task agent
3. Hook will automatically run tests when agent completes
```

---

### Auto-Detect Installation Level

```
/install-hook generated-hooks/git-auto-add
```

**Auto-detection logic**:
- If `.claude/settings.json` exists → Install to project
- Otherwise → Ask user: "Install to user or project level?"

---

## Safety Validation

**Before installation, the hook is validated for**:

1. **JSON Structure**:
   - ✅ Valid JSON syntax
   - ✅ Required fields present (matcher, hooks)
   - ✅ Correct data types

2. **Safety Patterns**:
   - ✅ Tool detection for external commands
   - ✅ Silent failure mode (`|| exit 0`)
   - ✅ No destructive operations (rm -rf, git push --force, etc.)
   - ✅ File path safety (no path traversal, proper quoting)

3. **Event Type Validation**:
   - ✅ Appropriate timeout for event type
   - ✅ Matcher matches event requirements
   - ✅ Command complexity appropriate

**If validation fails**:
```
❌ Hook validation FAILED

Issues found:
1. Missing tool detection for "black"
2. Path traversal detected (..)
3. No silent failure mode

Fix these issues before installation:
/validate-output hook generated-hooks/auto-format-python

Then regenerate the hook or fix manually.
```

---

## Settings Merge Behavior

**Existing hooks are preserved**:

**Before installation**:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": {"tool_names": ["Write"]},
        "hooks": [{"type": "command", "command": "existing hook"}]
      }
    ]
  }
}
```

**After installing new hook**:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": {"tool_names": ["Write"]},
        "hooks": [{"type": "command", "command": "existing hook"}]
      },
      {
        "matcher": {"tool_names": ["Write", "Edit"], "paths": ["**/*.py"]},
        "hooks": [{"type": "command", "command": "new hook"}]
      }
    ]
  }
}
```

**Key points**:
- ✅ Existing hooks preserved
- ✅ Other settings untouched
- ✅ Proper event type grouping
- ✅ Backup created before changes

---

## Backup and Recovery

**Automatic backups**:
- Created before every installation
- Named: `settings.json.backup`
- Location: Same directory as settings.json

**Restore from backup**:
```bash
# User-level
cp ~/.claude/settings.json.backup ~/.claude/settings.json

# Project-level
cp .claude/settings.json.backup .claude/settings.json
```

**After restore**: Restart Claude Code

---

## Uninstalling Hooks

**Manual uninstallation**:

1. Open settings file:
   ```bash
   # User-level
   vim ~/.claude/settings.json

   # Project-level
   vim .claude/settings.json
   ```

2. Find and remove the hook entry under its event type

3. Save and restart Claude Code

**Future**: Automated `/uninstall-hook` command planned

---

## Related Commands

**Before installing**:
- `/build hook` - Generate hook configuration
- `/validate-output hook` - Validate before installation

**After installing**:
- `/factory-status` - See all installed hooks
- `/test-factory` - Test hook functionality

**Managing hooks**:
- Run `/hooks` in Claude Code to view and manage all hooks
- Use Claude Code's settings menu to edit hook configuration

---

## Common Workflows

### Build → Validate → Install → Test

```bash
# 1. Build hook
/build hook

[Answer questions, hook generated]

# 2. Validate (CRITICAL for security)
/validate-output hook generated-hooks/my-hook

# 3. Install
/install-hook generated-hooks/my-hook user

# 4. Restart Claude Code
claude --continue

# 5. Test
[Trigger the hook event - e.g., edit a file for PostToolUse]
```

---

### Quick Install (If Already Validated)

```bash
# Already validated during generation
/install-hook generated-hooks/auto-format-python project
[Restart Claude Code]
```

---

## Tips

**Choosing user vs project level**:
- **User-level**: For hooks you want in ALL projects (formatters, notifications)
- **Project-level**: For project-specific hooks (tests, deployment, custom workflows)

**Testing hooks**:
- Start small: Install to project level first
- Test thoroughly before installing user-level
- Use `/hooks` command in Claude Code to view active hooks

**Managing multiple hooks**:
- Install one at a time
- Test each hook individually
- Check `/factory-status` to see all installed hooks

**Troubleshooting**:
- If hook doesn't run: Check event type matches your action
- If errors occur: Check hook validation with `/validate-output hook`
- If conflicts: Review settings.json manually
- Always check backup if something goes wrong

---

## Platform Notes

**macOS**:
- Hooks can use `osascript`, `afplay` for notifications/sounds
- Settings location: `~/.claude/settings.json`

**Linux**:
- Hooks can use `notify-send`, `paplay` for notifications/sounds
- Settings location: `~/.claude/settings.json`

**Windows**:
- Settings location: `%USERPROFILE%\.claude\settings.json`
- Use cross-platform tools (git, language-specific formatters)

---

**Safe hook installation with automatic validation!** 🔧✅
