# GitHub Workflows - Claude Code Integration

This directory contains GitHub Actions workflows for Claude Code integration.

## Quick Reference

### 🤖 Available Workflows

#### 1. Claude Code (`claude.yml`)
**Purpose**: On-demand Claude assistance via @claude mentions

**How to use**:
```
# In any issue or PR comment:
@claude please review this code

@claude help me write a test for this function

@claude what's the performance impact of this change?
```

**Who can use**: OWNER, MEMBER, COLLABORATOR only

**Tool access**: GitHub CLI (issues/PRs), npm commands

---

#### 2. Claude Code Review (`claude-code-review.yml`)
**Purpose**: Automatic code reviews on pull requests

**How it works**: Automatically reviews PRs from team members (OWNER/MEMBER/COLLABORATOR)

**Review focus**:
- Code quality and best practices
- Potential bugs or issues
- Performance considerations
- Security concerns
- Test coverage

**Who gets reviews**: OWNER, MEMBER, COLLABORATOR only

---

## Security Model

### ✅ Team Members (OWNER/MEMBER/COLLABORATOR)
- Can mention @claude in comments
- Get automatic PR reviews
- Full access to Claude capabilities

### ❌ External Contributors
- Cannot directly trigger @claude
- No automatic reviews (security by design)
- Team members can invoke @claude on their behalf

**Why?** Prevents API abuse and unauthorized access. See [SECURITY.md](SECURITY.md) for details.

---

## Configuration

### Secrets Required
- `CLAUDE_CODE_OAUTH_TOKEN` - OAuth token for Claude Code API

### Customization Options

**Add more allowed tools** (claude.yml line 55):
```yaml
claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh pr:*),Bash(your-command:*)"'
```

**Change who gets auto-reviews** (claude-code-review.yml line 22-23):
```yaml
# Example: Only review PRs with specific label
if: contains(github.event.pull_request.labels.*.name, 'ready-for-review')
```

**Add file path filters** (claude-code-review.yml line 7-11):
```yaml
paths:
  - "src/**/*.ts"
  - "src/**/*.tsx"
```

---

## Troubleshooting

### Workflow not triggering?

**Check**:
1. Are you a OWNER/MEMBER/COLLABORATOR? (Settings → Collaborators)
2. Did you mention @claude exactly? (case-sensitive)
3. Check Actions tab for failed runs

### Auto-review not running?

**Check**:
1. Is PR author a team member? (External contributors don't get auto-reviews)
2. Check if concurrency group is queued (rapid updates cancel old runs)
3. Look for workflow runs in Actions tab

### Permission errors?

**Check**:
1. Is `CLAUDE_CODE_OAUTH_TOKEN` secret configured?
2. Review workflow permissions (should be read-only)
3. Check tool allowlist includes needed commands

---

## Documentation

- **[SECURITY.md](SECURITY.md)** - Comprehensive security model and threat mitigation
- **[PR #8](https://github.com/alirezarezvani/claude-code-skill-factory/pull/8)** - Security hardening implementation
- **[Issue #1](https://github.com/alirezarezvani/claude-code-skill-factory/issues/1)** - Original security review

---

## Examples

### Request Code Review
```
@claude please review this PR and check for security issues
```

### Get Implementation Help
```
@claude how would you implement authentication for this API?
```

### Debug Issues
```
@claude this test is failing, can you help identify the issue?
```

### Documentation
```
@claude please update the README with these new features
```

---

**Last Updated**: October 24, 2025
**Questions?** Open an issue with the `question` label
