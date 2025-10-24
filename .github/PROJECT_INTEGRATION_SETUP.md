# GitHub Project Integration Setup

This guide explains how to set up automatic issue-to-project assignment for the **@claude-skills-factory** project board.

---

## Overview

The issue auto-triage workflow automatically adds triaged issues to your GitHub Project board. This requires a **Personal Access Token (PAT)** with project permissions because GitHub Actions' default `GITHUB_TOKEN` doesn't have access to Projects v2.

**Project**: [@claude-skills-factory](https://github.com/users/alirezarezvani/projects/7) (Project #7)

---

## Quick Setup (5 minutes)

### Step 1: Create Personal Access Token

1. **Go to GitHub Settings**:
   - Navigate to: https://github.com/settings/tokens/new
   - Or: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token

2. **Configure the token**:
   - **Note**: `claude-skills-factory-projects` (descriptive name)
   - **Expiration**: Choose expiration (recommend 90 days or No expiration for automation)
   - **Select scopes**:
     - ✅ `repo` (Full control of private repositories)
       - This includes: `repo:status`, `repo_deployment`, `public_repo`, `repo:invite`
     - ✅ `project` (Full access to projects - includes read and write)

3. **Generate token**:
   - Click "Generate token" at the bottom
   - **IMPORTANT**: Copy the token immediately (you won't see it again!)
   - Token format: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

### Step 2: Add Token as Repository Secret

1. **Go to Repository Settings**:
   - Navigate to: https://github.com/alirezarezvani/claude-code-skill-factory/settings/secrets/actions
   - Or: Repository → Settings → Secrets and variables → Actions

2. **Create new secret**:
   - Click "New repository secret"
   - **Name**: `PROJECTS_TOKEN` (must be exactly this name)
   - **Secret**: Paste your token (the `ghp_xxx...` value)
   - Click "Add secret"

3. **Verify secret created**:
   - You should see `PROJECTS_TOKEN` in the secrets list
   - The value will be hidden (shows as `***`)

---

### Step 3: Verify Workflow Configuration

The workflow is already configured to use the `PROJECTS_TOKEN`. Verify this in [.github/workflows/issue-triage.yml](workflows/issue-triage.yml):

```yaml
- name: Run Claude Triage
  uses: anthropics/claude-code-action@v1
  env:
    GH_TOKEN: ${{ secrets.PROJECTS_TOKEN }}  # ✅ Uses your PAT
  with:
    claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
```

**No changes needed** - the workflow is ready to use the token!

---

## Testing the Integration

### Test with a New Issue

1. **Create a test issue**:
   ```bash
   gh issue create \
     --title "Test: Verify project board integration" \
     --body "This issue tests automatic assignment to project #7.

   Expected:
   - Issue triaged within 60 seconds
   - Labels applied automatically
   - Added to @claude-skills-factory project board"
   ```

2. **Wait 60-90 seconds** for auto-triage to complete

3. **Verify project assignment**:
   - Check issue has triage comment
   - Check issue has labels applied
   - **Check project board**: https://github.com/users/alirezarezvani/projects/7
   - Issue should appear in the project board

4. **Check workflow logs** (if issues):
   ```bash
   gh run list --workflow=issue-triage.yml --limit 1
   gh run view <run-id> --log | grep "project"
   ```

---

## Troubleshooting

### Issue Not Added to Project

**Symptom**: Issue gets triaged (comment + labels) but doesn't appear in project board

**Possible causes**:

#### 1. Token Not Set or Incorrect Name

**Check**:
```bash
# This should show PROJECTS_TOKEN
gh secret list -R alirezarezvani/claude-code-skill-factory
```

**Fix**: Ensure secret name is exactly `PROJECTS_TOKEN` (case-sensitive)

---

#### 2. Token Missing Permissions

**Error in logs**: `GraphQL: Could not resolve to a ProjectV2 with the number 7`

**Fix**:
1. Delete old token: https://github.com/settings/tokens
2. Create new token with ALL these scopes:
   - ✅ `repo`
   - ✅ `project`
3. Update `PROJECTS_TOKEN` secret with new token

---

#### 3. Wrong Project Number

**Error in logs**: `Could not resolve to a ProjectV2 with the number 7`

**Verify project number**:
```bash
# Run locally (not in Actions)
gh auth refresh -s project
gh project list --owner alirezarezvani
```

**Fix workflow** if project number is different:
- Edit [.github/workflows/issue-triage.yml](workflows/issue-triage.yml:147)
- Change `gh project item-add 7` to `gh project item-add <CORRECT_NUMBER>`

---

#### 4. Token Expired

**Symptom**: Worked before, now doesn't

**Fix**:
1. Check token expiration: https://github.com/settings/tokens
2. Generate new token (same scopes)
3. Update `PROJECTS_TOKEN` secret

---

#### 5. Project Permissions Changed

**Symptom**: Error about insufficient permissions

**Fix**: Ensure your user account has write access to the project:
- Project settings → Manage access → Verify you're listed as owner/admin

---

## Security Best Practices

### Token Security

✅ **DO**:
- Use descriptive token names (`claude-skills-factory-projects`)
- Set reasonable expiration (90 days recommended)
- Use minimum required scopes (`repo`, `project`)
- Store only in GitHub Secrets (never commit to code)
- Rotate tokens periodically

❌ **DON'T**:
- Share tokens in plain text
- Use tokens with `admin:org` or excessive permissions
- Store tokens in environment variables or config files
- Use the same token across multiple projects

---

### Secret Management

**Access control**:
- Only repository admins can view/edit secrets
- GitHub masks secret values in logs
- Secrets are encrypted at rest

**Rotation schedule**:
- Review tokens quarterly
- Regenerate if compromised
- Update expiration before token expires

---

## Alternative: GitHub Native Auto-Add (No Token Required)

If you prefer not to use a PAT, you can configure GitHub Projects to auto-add issues:

### Setup

1. **Go to project**: https://github.com/users/alirezarezvani/projects/7

2. **Open project settings** (⚙️ icon)

3. **Workflows → Auto-add items**:
   - Click "Add workflow"
   - Select: "Item added to project"
   - Trigger: "When issue is opened"
   - Repository: `alirezarezvani/claude-code-skill-factory`
   - Save workflow

4. **Remove workflow project command**:
   - Edit [.github/workflows/issue-triage.yml](workflows/issue-triage.yml:144-149)
   - Remove or comment out step 6 (project assignment)

### Comparison

| Approach | Pros | Cons |
|----------|------|------|
| **PAT in workflow** | Full automation, logged in workflow, programmatic control | Requires token management, expiration handling |
| **GitHub native auto-add** | No token needed, GitHub-managed, zero maintenance | Less control, all issues added (no filtering) |

---

## Monitoring & Maintenance

### Check Workflow Health

```bash
# View recent triage runs
gh run list --workflow=issue-triage.yml --limit 10

# Check success rate
gh run list --workflow=issue-triage.yml --json conclusion --jq '[.[] | select(.conclusion != null)] | group_by(.conclusion) | map({conclusion: .[0].conclusion, count: length})'

# View specific run logs
gh run view <run-id> --log | grep -i "project\|error"
```

### Monitor Project Integration

**Monthly checklist**:
- [ ] Verify token hasn't expired
- [ ] Check recent issues are being added to project
- [ ] Review workflow failure rate (<5% acceptable)
- [ ] Audit project board for missing issues

---

## FAQ

### Q: Can I use a GitHub App instead of PAT?

**A**: Yes, but requires more setup:
1. Create GitHub App with `repository_projects:write` permission
2. Install app on repository
3. Use app installation token in workflow
4. More secure but complex setup

**Recommendation**: PAT is simpler for single-repository automation

---

### Q: Does this work with organization projects?

**A**: Yes! Change the command:
```bash
# User project (current):
gh project item-add 7 --owner alirezarezvani --url <issue-url>

# Organization project:
gh project item-add <NUMBER> --owner <ORG_NAME> --url <issue-url>
```

Also update token to have `read:org` scope.

---

### Q: Can I add issues to multiple projects?

**A**: Yes! Add multiple commands in the workflow:
```bash
# Add to user project
gh project item-add 7 --owner alirezarezvani --url <issue-url>

# Add to team project
gh project item-add 12 --owner myorg --url <issue-url>
```

---

### Q: What if I want to filter which issues get added?

**A**: Modify the Claude prompt to only add issues based on criteria:
```yaml
# Example: Only add P0/P1 bugs to project
6. **Add to project board** (ONLY for P0/P1 bugs):
   if priority is P0 or P1 AND type is bug:
     gh project item-add 7 --owner alirezarezvani --url <issue-url>
```

---

## Current Status

✅ **Workflow configured** - Ready to use PROJECTS_TOKEN
⚠️ **Token setup required** - Need to complete Step 1 & 2 above
📋 **Project**: https://github.com/users/alirezarezvani/projects/7

---

## Need Help?

**Token creation issues**: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

**Projects API**: https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects

**GitHub CLI projects**: https://cli.github.com/manual/gh_project

---

**Last Updated**: 2025-10-24
**Workflow Version**: 1.1.0
**Status**: Ready for token configuration
