# Security Model - Claude Code GitHub Workflows

**Last Updated**: October 24, 2025
**Version**: 1.0

This document describes the security model for Claude Code integration in this repository, including access controls, permissions, and operational guidelines.

---

## Overview

This repository uses two GitHub Actions workflows to integrate Claude Code:

1. **`claude.yml`** - On-demand Claude assistance via @claude mentions
2. **claude-code-review.yml`** - Automatic code reviews on pull requests

Both workflows implement strict security controls to prevent unauthorized access and API abuse.

---

## Access Control Model

### Authorization Levels

| Role | Can Trigger @claude? | Gets Auto-Reviews? | Rationale |
|------|---------------------|-------------------|-----------|
| **OWNER** | ✅ Yes | ✅ Yes | Full repository access |
| **MEMBER** | ✅ Yes | ✅ Yes | Organization member |
| **COLLABORATOR** | ✅ Yes | ✅ Yes | Explicit write access granted |
| **CONTRIBUTOR** | ❌ No | ❌ No | Read-only, no write permissions |
| **FIRST_TIME_CONTRIBUTOR** | ❌ No | ❌ No | First PR, untrusted |
| **NONE** (External) | ❌ No | ❌ No | Public user, no relationship |

### How External Contributors Get Help

External contributors **cannot directly trigger @claude**, but they can:

1. **Request help in PR description** - Team members can mention @claude on their behalf
2. **Ask in comments** - Team members review and invoke Claude if appropriate
3. **Wait for auto-review** - Not applicable (security by design)

**Why this restriction?** Prevents:
- API quota abuse from spam PRs
- Malicious attempts to exploit Claude's capabilities
- Unauthorized access to repository operations

---

## Workflow Security Details

### 1. `claude.yml` - On-Demand Assistance

**File**: `.github/workflows/claude.yml`

#### Triggers
- Issue comments containing `@claude`
- PR review comments containing `@claude`
- PR reviews containing `@claude`
- New issues with `@claude` in title/body

#### Access Control (Line 20-26)
```yaml
if: |
  (
    (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude') &&
     contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)) ||
    (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude') &&
     contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)) ||
    (github.event_name == 'pull_request_review' && contains(github.event.review.body, '@claude') &&
     contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.review.author_association)) ||
    (github.event_name == 'issues' && (contains(github.event.issue.body, '@claude') || contains(github.event.issue.title, '@claude')) &&
     contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.issue.author_association))
  )
```

**Validation**: Each event type checks:
1. ✅ @claude mentioned in content
2. ✅ Author is OWNER, MEMBER, or COLLABORATOR

#### Permissions (Line 28-31)
```yaml
permissions:
  contents: read          # Read repository files
  pull-requests: read     # Read PR context
  issues: read            # Read issue context
  actions: read           # Read CI results
```

**Note**: No write permissions granted. Claude can read context but cannot directly modify repository without explicit tool allowlist.

#### Tool Allowlist (Line 55)
```yaml
claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh pr:*),Bash(gh search:*),Bash(npm install:*),Bash(npm run:*)"'
```

**Allowed Operations**:
- `gh issue:*` - View, comment, manage issues
- `gh pr:*` - View, comment, manage PRs
- `gh search:*` - Search repository content
- `npm install:*` - Install dependencies (for testing)
- `npm run:*` - Run package scripts (for testing/building)

**Why restricted?** Principle of least privilege - only grant tools Claude actually needs.

#### Concurrency Control (Line 14-16)
```yaml
concurrency:
  group: claude-${{ github.event.issue.number || github.event.pull_request.number }}
  cancel-in-progress: false
```

**Behavior**:
- Multiple @claude mentions on same issue/PR will queue (not run simultaneously)
- Previous runs complete before new ones start
- Prevents duplicate work and API waste

---

### 2. `claude-code-review.yml` - Automatic PR Reviews

**File**: `.github/workflows/claude-code-review.yml`

#### Triggers
- Pull request opened
- Pull request synchronized (new commits pushed)

#### Access Control (Line 22-23)
```yaml
if: |
  contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.pull_request.author_association)
```

**Validation**: Only runs if PR author is OWNER, MEMBER, or COLLABORATOR

**Why?** Prevents:
- API abuse from external contributors opening spam PRs
- Review runs on exploratory/test PRs from untrusted sources

#### Permissions (Line 26-29)
```yaml
permissions:
  contents: read          # Read repository files
  pull-requests: read     # Read PR details
  issues: read            # Read linked issues
```

**Note**: Read-only. Reviews posted via `gh pr comment` command (allowed in tool list).

#### Tool Allowlist (Line 56)
```yaml
claude_args: '--allowed-tools "Bash(gh issue view:*),Bash(gh search:*),Bash(gh issue list:*),Bash(gh pr comment:*),Bash(gh pr diff:*),Bash(gh pr view:*),Bash(gh pr list:*)"'
```

**Allowed Operations**:
- `gh issue view/list:*` - View related issues
- `gh pr view/list/diff:*` - Analyze PR changes
- `gh pr comment:*` - Post review comments
- `gh search:*` - Search for context

**Why restricted?** Code reviews only need read access + ability to comment. No modification capabilities needed.

#### Concurrency Control (Line 14-16)
```yaml
concurrency:
  group: claude-review-${{ github.event.pull_request.number }}
  cancel-in-progress: true
```

**Behavior**:
- New commits to PR cancel outdated review runs
- Saves API quota on rapidly-updated PRs
- Ensures reviews always analyze latest code

---

## Security Validation

### GitHub Context Fields Used

All GitHub context fields are validated against GitHub's webhook payload documentation:

| Workflow | Event Type | Field | Valid? |
|----------|-----------|-------|--------|
| claude.yml | issue_comment | `github.event.comment.author_association` | ✅ |
| claude.yml | pull_request_review_comment | `github.event.comment.author_association` | ✅ |
| claude.yml | pull_request_review | `github.event.review.author_association` | ✅ |
| claude.yml | issues | `github.event.issue.author_association` | ✅ |
| claude-code-review.yml | pull_request | `github.event.pull_request.author_association` | ✅ |

**References**:
- [GitHub Webhook Events](https://docs.github.com/en/webhooks/webhook-events-and-payloads)
- [GitHub Actions Contexts](https://docs.github.com/en/actions/learn-github-actions/contexts#github-context)

---

## Threat Model & Mitigations

### Threat 1: API Quota Abuse
**Attack**: External contributor opens many PRs or spam issues with @claude mentions
**Mitigation**:
- ✅ Author association checks prevent external contributors from triggering workflows
- ✅ Concurrency controls prevent duplicate runs

### Threat 2: Unauthorized Repository Modifications
**Attack**: Malicious actor attempts to use Claude to modify repository
**Mitigation**:
- ✅ Read-only permissions (no `contents: write`)
- ✅ Explicit tool allowlist (no unrestricted bash access)
- ✅ GitHub's branch protection rules still apply

### Threat 3: Secrets Exposure
**Attack**: Attempt to extract `CLAUDE_CODE_OAUTH_TOKEN` or other secrets
**Mitigation**:
- ✅ GitHub Actions secrets are masked in logs automatically
- ✅ No unrestricted bash commands allowed
- ✅ Tool allowlist prevents arbitrary command execution

### Threat 4: Privilege Escalation
**Attack**: CONTRIBUTOR tries to gain COLLABORATOR privileges via Claude
**Mitigation**:
- ✅ Author association determined by GitHub (cannot be spoofed)
- ✅ Workflow conditions check association before any execution
- ✅ No ability to modify workflow files via Claude

### Threat 5: Resource Exhaustion
**Attack**: Rapid-fire @claude mentions to overwhelm system
**Mitigation**:
- ✅ Concurrency groups queue runs (no parallel execution per issue/PR)
- ✅ GitHub Actions has built-in rate limiting
- ✅ Can disable workflows if abuse detected

---

## Operational Guidelines

### For Repository Administrators

**Granting Access**:
1. Add trusted users as COLLABORATOR via Settings → Collaborators
2. They immediately gain Claude access (no workflow changes needed)
3. Their PRs automatically get reviews

**Revoking Access**:
1. Remove COLLABORATOR status via Settings → Collaborators
2. They immediately lose Claude access
3. Their PRs no longer get auto-reviewed

**Monitoring Usage**:
- View workflow runs: Actions tab → Claude Code / Claude Code Review
- Check API usage: Workflow run logs show Claude operations
- Set up notifications: Settings → Notifications → Actions

### For Contributors

**Team Members (OWNER/MEMBER/COLLABORATOR)**:
- ✅ Mention @claude in any comment on issues/PRs
- ✅ Create issues with @claude in title/description
- ✅ Automatic code reviews on your PRs
- ✅ Full Claude capabilities within tool allowlist

**External Contributors**:
- ❌ Cannot directly trigger @claude
- ✅ Can request help in PR description
- ✅ Team members can invoke @claude on your behalf
- ℹ️ This is security by design, not a bug

### For Claude Itself

When Claude runs, it:
1. ✅ Has read access to entire repository
2. ✅ Can view CI results and checks
3. ✅ Can post comments on issues/PRs
4. ✅ Can run allowed bash commands (gh, npm)
5. ❌ Cannot directly commit/push code
6. ❌ Cannot modify secrets or settings
7. ❌ Cannot run arbitrary system commands

---

## Compliance & Audit

### Security Checklist

- [x] Access control implemented (author_association checks)
- [x] Permissions minimized (read-only + explicit writes)
- [x] Tool allowlist configured (no unrestricted bash)
- [x] Concurrency controls prevent abuse
- [x] No unnecessary permissions (id-token removed)
- [x] GitHub context fields validated
- [x] Threat model documented
- [x] Operational guidelines provided

### Audit Log

All Claude runs are logged in GitHub Actions:
- **Location**: Actions tab → Claude Code / Claude Code Review
- **Retention**: 90 days (GitHub default)
- **Information**: Trigger, requester, commands executed, output
- **Access**: Repository administrators

---

## Testing & Validation

### Pre-Deployment Testing

Before deploying workflow changes, validate:

1. **YAML Syntax**:
   ```bash
   yamllint .github/workflows/claude*.yml
   ```

2. **GitHub Context Fields**:
   - Verify fields exist in GitHub webhook payload documentation
   - Test with actual PRs/issues from different user types

3. **Logic Flow**:
   - OWNER creates issue with @claude → ✅ Should trigger
   - CONTRIBUTOR comments with @claude → ❌ Should NOT trigger
   - COLLABORATOR opens PR → ✅ Should get auto-review
   - External user opens PR → ❌ Should NOT get auto-review

### Post-Deployment Validation

After workflow updates are merged:

1. **Test with team member account**:
   - Create test issue, mention @claude
   - Verify workflow triggers and completes

2. **Test with external account** (or simulate):
   - Fork repo, open PR as external contributor
   - Verify auto-review does NOT trigger
   - Have team member mention @claude
   - Verify manual trigger works

3. **Monitor for failures**:
   - Check Actions tab for failed runs
   - Review logs for permission errors
   - Adjust if needed

---

## Incident Response

### If Unauthorized Access Detected

1. **Immediate**: Disable workflows via Settings → Actions → Disable
2. **Revoke**: Rotate `CLAUDE_CODE_OAUTH_TOKEN` secret
3. **Investigate**: Review Actions logs for unauthorized runs
4. **Fix**: Update workflows with stricter controls
5. **Re-enable**: Test and re-enable workflows

### If API Quota Exceeded

1. **Identify**: Check Actions logs for excessive runs
2. **Disable**: Temporarily disable auto-review workflow
3. **Restrict**: Keep only @claude mentions workflow
4. **Monitor**: Re-enable gradually with monitoring
5. **Optimize**: Consider adding rate limiting or label-based triggers

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-24 | Initial security model documentation |

---

## References

- [GitHub Actions Security Hardening](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Claude Code Action Documentation](https://github.com/anthropics/claude-code-action)
- [GitHub Webhook Events](https://docs.github.com/en/webhooks/webhook-events-and-payloads)
- [Issue #1 - Original Security Review](https://github.com/alirezarezvani/claude-code-skill-factory/issues/1)
- [PR #8 - Security Hardening Implementation](https://github.com/alirezarezvani/claude-code-skill-factory/pull/8)

---

**Maintained by**: Repository Security Team
**Questions?** Open an issue with the `security` label
