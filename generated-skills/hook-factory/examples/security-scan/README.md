# Security Scan Hook

Comprehensive security scanning before git push to detect secrets and vulnerabilities.

## What This Hook Does

- Scans staged changes for hardcoded secrets (passwords, API keys, tokens)
- Detects AWS keys, Stripe keys, GitHub tokens, private keys
- Runs semgrep security rules (if installed)
- Runs bandit for Python security (if installed)
- Blocks push if security issues found
- Can take 30-120 seconds

## Event Type

**PrePush** - Triggers BEFORE `git push` executes (BLOCKING)

## Installation

### Automatic
```bash
# User-level (all projects)
cp -r examples/security-scan ~/.claude/hooks/

# Project-level (this project only)
cp -r examples/security-scan .claude/hooks/
```

### Manual
Add `hook.json` content to `PrePush` array in settings.json

## Prerequisites

**Optional Tools** (scan runs without them, but limited):

1. **semgrep** (recommended):
   ```bash
   pip install semgrep
   # or
   brew install semgrep
   ```

2. **bandit** (for Python projects):
   ```bash
   pip install bandit
   ```

## How It Works

1. **Secrets Scan** (always runs):
   - Checks `git diff --cached` for secret patterns
   - Detects: password, api_key, secret, token assignments
   - Detects: AWS keys (AKIA...), Stripe keys (sk_live/sk_test), GitHub tokens (ghp_/ghs_)
   - Detects: Private keys (-----BEGIN PRIVATE KEY-----)

2. **Semgrep Scan** (if installed):
   - Runs `semgrep --config=auto --error`
   - Checks for common vulnerabilities
   - Language-agnostic security rules

3. **Bandit Scan** (if installed, Python only):
   - Runs `bandit -r . -ll`
   - Python-specific security issues
   - Low and high severity only

4. **Exit Codes**:
   - `0` = No security issues, allow push
   - `1` = Security issues found, block push

## Example Output

**Success**:
```
Running security scan...
Checking for secrets...
semgrep not installed - skipping (install with: pip install semgrep)
bandit not installed - skipping Python scan (install with: pip install bandit)
Security scan passed!
```

**Blocked (Secrets Detected)**:
```
Running security scan...
Checking for secrets...
Warning: Potential secrets found in staged changes
Error: AWS/Stripe/GitHub tokens detected in staged changes
Security scan failed - potential secrets detected
Please remove secrets before pushing
```

**Blocked (Semgrep Issues)**:
```
Running security scan...
Checking for secrets...
Running semgrep security scan...
Semgrep found security issues
Security scan found 1 issue(s) - push blocked
```

## Customization

### Add Custom Secret Patterns

Edit secrets check in `hook.json`:
```bash
# Add more patterns
if git diff --cached | grep -iE '(password|api_key|secret|token|bearer|jwt)\\s*='; then
    echo \"Warning: Potential secrets found\"
    SECRETS_FOUND=true
fi
```

### Skip Specific Scanners

Remove unwanted scanners from `hook.json`:
```bash
# Remove semgrep block to skip
# Remove bandit block to skip Python scanning
```

### Change Severity Levels

For bandit, change `-ll` (low+high) to:
- `-l` (only low severity)
- `-m` (only medium)
- `-h` (only high)
- No flag (all severities)

### Change Timeout

Default is 120 seconds. Adjust in `hook.json`:
```json
"timeout": 120  // Change to 60 for faster, 180 for thorough
```

## Use Cases

- **Prevent Secret Leaks**: Catch secrets before they hit remote
- **Security Gate**: Block vulnerable code from being pushed
- **Compliance**: Meet security requirements
- **Team Protection**: Prevent accidental security issues

## Safety Notes

- **BLOCKING**: Can prevent `git push` from succeeding
- **Slow**: Can take 30-120 seconds (runs multiple scans)
- **Bypass**: Use `git push --no-verify` (emergency only)
- **False Positives**: May flag non-sensitive strings

## Testing

1. **Test Secrets Detection**:
   ```bash
   echo 'password = "secret123"' > test.txt
   git add test.txt
   git commit -m "test"
   git push  # Should block
   ```

2. **Test AWS Key Detection**:
   ```bash
   echo 'AWS_KEY = "AKIAIOSFODNN7EXAMPLE"' > config.py
   git add config.py
   git commit -m "test"
   git push  # Should block
   ```

3. **Test Private Key Detection**:
   ```bash
   echo '-----BEGIN RSA PRIVATE KEY-----' > key.pem
   git add key.pem
   git commit -m "test"
   git push  # Should block
   ```

4. **Test With Semgrep** (if installed):
   ```bash
   # Add vulnerable code (SQL injection, etc.)
   git push  # Should catch vulnerability
   ```

## Troubleshooting

**Too many false positives:**
- Adjust regex patterns to be more specific
- Whitelist specific files/patterns
- Use `--no-verify` for known-safe pushes

**Semgrep/Bandit not running:**
- Check installation: `which semgrep`, `which bandit`
- Install if missing
- Check PATH environment variable

**Too slow:**
- Reduce timeout from 120s to 60s
- Skip semgrep/bandit (secrets scan only)
- Run on staged changes only (current behavior)

**Missing real secrets:**
- Add more patterns to secrets check
- Lower semgrep/bandit sensitivity
- Add project-specific patterns

**Need to bypass (emergency):**
```bash
git push --no-verify  # WARNING: Use only when certain it's safe
```

## Common Secret Patterns Detected

- `password = "value"`
- `api_key = "value"`
- `secret = "value"`
- `token = "value"`
- `AKIA...` (AWS Access Key ID)
- `sk_live_...` (Stripe Live Secret Key)
- `sk_test_...` (Stripe Test Secret Key)
- `ghp_...` (GitHub Personal Access Token)
- `ghs_...` (GitHub Secret Scanning Token)
- `-----BEGIN PRIVATE KEY-----` (RSA/SSH keys)

## Best Practices

1. **Use .gitignore**: Add `.env`, `secrets/`, `credentials/` to .gitignore
2. **Use Environment Variables**: Store secrets in env vars, not code
3. **Use Secret Management**: Tools like AWS Secrets Manager, HashiCorp Vault
4. **Review Staged Changes**: Always `git diff --cached` before push
5. **Team Training**: Educate team on secret management
