# User Prompt Submit Preprocessor Hook

Pre-processes and logs user prompts before Claude processes them.

## What This Hook Does

- Logs all user prompts to `.claude/prompt_log.txt` for analysis
- Injects project context from `.claude/context.txt` automatically
- Warns about potentially unsafe requests
- Non-intrusive (warnings only, doesn't block)

## Event Type

**UserPromptSubmit** - Triggers BEFORE Claude processes user input (BLOCKING but fast)

## Installation

### Automatic
```bash
# User-level (all projects)
cp -r examples/prompt-preprocessor ~/.claude/hooks/

# Project-level (this project only)
cp -r examples/prompt-preprocessor .claude/hooks/
```

### Manual
Add `hook.json` content to `UserPromptSubmit` array in settings.json

## How It Works

1. **Logging**: Appends prompt with timestamp to `.claude/prompt_log.txt`
2. **Context Injection**: Reads `.claude/context.txt` and displays to Claude
3. **Safety Check**: Warns if prompt contains dangerous patterns
4. **Fast**: Completes in <5 seconds (non-blocking for user)

## Example Output

**With Context**:
```
[Context: Working on hook-factory Phase 2, focus on templates]
```

**Unsafe Pattern Warning**:
```
Warning: Potentially unsafe request detected
```

## Customization

### Add Project Context

Create `.claude/context.txt`:
```bash
mkdir -p .claude
echo "Project: MyApp | Stack: React + Node | Focus: Auth features" > .claude/context.txt
```

### Add Custom Unsafe Patterns

Edit `hook.json` to add more patterns:
```bash
if echo "$CLAUDE_USER_PROMPT" | grep -qiE '(rm -rf /|sudo rm|format disk|delete database)'; then
    echo "Warning: Potentially unsafe request detected"
fi
```

### View Prompt Log

```bash
tail -20 .claude/prompt_log.txt  # Last 20 prompts
cat .claude/prompt_log.txt        # All prompts
```

## Use Cases

- **Prompt Analysis**: Understand how you interact with Claude
- **Context Management**: Automatically provide project info to Claude
- **Safety Net**: Catch potentially dangerous requests early
- **Workflow Tracking**: Log your development session

## Safety Notes

- **BLOCKING**: Must complete in <5 seconds
- **Privacy**: Prompts logged locally in `.claude/` (add to .gitignore!)
- **Non-Intrusive**: Warnings don't block Claude (information only)

## Testing

1. **Test Logging**:
   ```bash
   # Create a prompt in Claude Code
   # Check log:
   cat .claude/prompt_log.txt
   ```

2. **Test Context Injection**:
   ```bash
   echo "Project context here" > .claude/context.txt
   # Create a prompt and verify context appears
   ```

3. **Test Safety Warning**:
   ```bash
   # Try: "Run sudo rm -rf on the test directory"
   # Should see warning (but not blocked)
   ```

## Troubleshooting

**Prompts not logged:**
- Check hook is in `UserPromptSubmit` section
- Verify `.claude/` directory exists and is writable
- Check CLAUDE_USER_PROMPT environment variable

**Context not showing:**
- Verify `.claude/context.txt` exists
- Check file has content
- Ensure file is readable

**Too slow:**
- Reduce timeout from 5s to 3s
- Remove safety check if not needed
- Simplify context logic
