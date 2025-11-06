# Pre-Push Validation Hook

Validates code quality and commit messages before allowing git push.

## What This Hook Does

- Blocks direct pushes to protected branches (main/master/production)
- Validates commit messages (no WIP/TODO/FIXME)
- Runs test suite before allowing push
- Prevents pushing broken code
- Can take 60-120 seconds (runs tests)

## Event Type

**PrePush** - Triggers BEFORE `git push` executes (BLOCKING)

## Installation

### Automatic
```bash
# User-level (all projects)
cp -r examples/pre-push-check ~/.claude/hooks/

# Project-level (this project only)
cp -r examples/pre-push-check .claude/hooks/
```

### Manual
Add `hook.json` content to `PrePush` array in settings.json

## How It Works

1. **Branch Protection**: Blocks pushes to main/master/production
2. **Commit Message Validation**: Rejects WIP/TODO/FIXME in messages
3. **Test Execution**: Runs npm test or pytest if available
4. **Exit Codes**:
   - `0` = All checks passed, allow push
   - `1` = Validation failed, block push

## Example Output

**Success**:
```
Running pre-push validation...
No test framework detected - skipping tests
All pre-push checks passed!
```

**Blocked (Protected Branch)**:
```
Running pre-push validation...
Error: Direct push to protected branch 'main' is not allowed
Please create a feature branch and submit a pull request
```

**Blocked (Bad Commit Message)**:
```
Running pre-push validation...
Error: Commit messages contain WIP/TODO/FIXME
Please clean up commit messages before pushing
```

**Blocked (Test Failure)**:
```
Running pre-push validation...
Running npm tests...
Tests failed - push blocked
```

## Customization

### Add More Protected Branches

Edit `PROTECTED_BRANCHES` array in `hook.json`:
```bash
PROTECTED_BRANCHES=("main" "master" "production" "staging" "release")
```

### Skip Tests (Faster Validation)

Remove test section from `hook.json`:
```bash
# Remove this block to skip test execution:
if [ -f package.json ] && command -v npm &> /dev/null; then
    ...
fi
```

### Add Linting Check

Add after commit message check:
```bash
# Run linter
if [ -f .eslintrc.js ] || [ -f .eslintrc.json ]; then\n    echo \"Running ESLint...\"\n    npx eslint . || { echo \"Linting failed - push blocked\"; exit 1; }\nfi
```

### Change Timeout

Default is 120 seconds (for slow tests). Adjust in `hook.json`:
```json
"timeout": 120  // Change to 60 for fast tests, 180 for slow
```

## Use Cases

- **Quality Gate**: Prevent broken code from being pushed
- **Branch Protection**: Enforce PR workflow
- **Commit Hygiene**: Keep commit history clean
- **Team Collaboration**: Ensure code quality standards

## Safety Notes

- **BLOCKING**: Can prevent `git push` from succeeding
- **Timeout**: Can take 60-120 seconds (runs tests)
- **Bypass**: Use `git push --no-verify` to bypass (emergency only)
- **Local Only**: Runs on your machine, not on server

## Testing

1. **Test Branch Protection**:
   ```bash
   git checkout main
   git push  # Should block
   ```

2. **Test Commit Message Validation**:
   ```bash
   git commit -m "WIP: temporary commit"
   git push  # Should block with WIP error
   ```

3. **Test With Passing Tests**:
   ```bash
   git checkout -b feature/test
   # Make changes, commit
   git push  # Should run tests and allow push
   ```

4. **Test With Failing Tests**:
   ```bash
   # Break a test
   git commit -am "breaking change"
   git push  # Should block with test failure
   ```

## Troubleshooting

**Push not blocked:**
- Check hook is in `PrePush` section (not PostToolUse)
- Verify git push command (not direct remote push)
- Check you're not using `--no-verify` flag

**Tests not running:**
- Verify test framework installed (npm, pytest)
- Check package.json or pytest.ini exists
- Ensure tests work manually first

**Too slow:**
- Reduce timeout from 120s to 60s
- Remove test execution (validation only)
- Run only critical tests (not full suite)

**Too strict:**
- Remove branch protection check
- Allow WIP commits (remove message validation)
- Skip test execution

**Bypass Hook (Emergency)**:
```bash
git push --no-verify  # WARNING: Use only in emergencies
```
