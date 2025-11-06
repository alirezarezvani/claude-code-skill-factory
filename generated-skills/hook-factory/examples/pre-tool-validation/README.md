# Pre-Tool Use Validation Hook

Validates file permissions and protects sensitive files before Write/Edit operations.

## What This Hook Does

- Checks write permissions before modifying files
- Prevents modifications to protected files (.env, credentials, AWS/SSH configs)
- Blocks operations that would fail due to permission errors
- Fast validation (<10 seconds)

## Event Type

**PreToolUse** - Triggers BEFORE Write/Edit tools execute (BLOCKING)

## Installation

### Automatic (Recommended)
```bash
# Copy to user-level (all projects)
cp -r examples/pre-tool-validation ~/.claude/hooks/

# OR copy to project-level (this project only)
cp -r examples/pre-tool-validation .claude/hooks/
```

### Manual
1. Copy `hook.json` content
2. Add to `~/.claude/settings.json` or `.claude/settings.json`
3. Merge into `PreToolUse` array (not PostToolUse!)

## How It Works

1. **Permission Check**: Verifies write permission on target file
2. **Protected Files**: Checks against protected patterns:
   - `/.env` files (environment variables)
   - `/secrets` directories
   - `/credentials` files
   - `/.aws/` AWS configurations
   - `/.ssh/` SSH keys
3. **Exit Codes**:
   - `0` = Validation passed, allow tool to execute
   - `1` = Validation failed, block tool execution

## Example Output

**Success**:
```
Validation passed
```

**Blocked (No Permission)**:
```
Error: No write permission for /path/to/file.txt
```

**Blocked (Protected File)**:
```
Error: Cannot modify protected file: /home/user/.env
```

## Customization

### Add More Protected Patterns

Edit the `PROTECTED_PATTERNS` array in `hook.json`:

```bash
PROTECTED_PATTERNS=(
    "/.env$"           # Environment files
    "/secrets"         # Secrets directories
    "/credentials"     # Credential files
    "/.aws/"           # AWS config
    "/.ssh/"           # SSH keys
    "/production.yml"  # Custom: Production configs
    "/api_keys.json"   # Custom: API keys
)
```

### Change Timeout

Default is 10 seconds (fast validation). Adjust in `hook.json`:

```json
"timeout": 10  // Change to 5 for faster, 20 for more thorough checks
```

## Testing

1. **Test Normal Operation**:
   ```bash
   echo "test" > test_file.txt
   # Should allow write (no protection)
   ```

2. **Test Protected File**:
   ```bash
   touch .env
   echo "SECRET=123" > .env
   # Should block (protected pattern)
   ```

3. **Test Read-Only File**:
   ```bash
   touch readonly.txt
   chmod 444 readonly.txt
   # Should block (no write permission)
   ```

## Safety Notes

- **BLOCKING**: This hook can prevent Write/Edit operations
- **Fast**: Must complete in <10 seconds
- **Use Cases**: Prevent accidental modifications to critical files
- **Limitations**: Only checks permissions, not file content

## Troubleshooting

**Hook doesn't block writes:**
- Verify hook is in `PreToolUse` section (not PostToolUse)
- Check CLAUDE_TOOL_FILE_PATH is set
- Test protected pattern regex with your file path

**Too restrictive:**
- Remove patterns from PROTECTED_PATTERNS array
- Adjust regex patterns to be more specific

**Timeout errors:**
- Reduce timeout from 10s to 5s
- Simplify validation logic
