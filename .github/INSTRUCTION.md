# GitHub Workflows - Setup & Usage Instructions

**Version**: 1.0.0
**Last Updated**: 2025-10-24

Complete guide for setting up, using, and troubleshooting the GitHub automation system.

---

## Table of Contents

- [Initial Setup](#initial-setup)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [Workflow Details](#workflow-details)
- [Troubleshooting](#troubleshooting)
- [Advanced Configuration](#advanced-configuration)
- [Maintenance](#maintenance)

---

## Initial Setup

### Prerequisites

1. **GitHub Repository**
   - Issues enabled
   - Projects enabled
   - Actions enabled

2. **Required Tokens** (see Configuration section)
   - CLAUDE_CODE_OAUTH_TOKEN
   - PROJECTS_TOKEN

3. **Team Access**
   - At least COLLABORATOR permission for team members

---

### Step 1: Create Required Secrets

#### 1.1 CLAUDE_CODE_OAUTH_TOKEN

**Purpose**: Authenticates Claude Code GitHub Action

**How to Add**:
1. Navigate to: Repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `CLAUDE_CODE_OAUTH_TOKEN`
4. Value: [Your Claude Code OAuth token]
5. Click "Add secret"

---

#### 1.2 PROJECTS_TOKEN (Personal Access Token)

**Purpose**: Project board access (default GITHUB_TOKEN lacks permissions)

**Required Scopes**:
- `repo` (Full control of private repositories)
- `project` (Full control of projects)

**How to Create**:

1. **Navigate to Token Settings**:
   - Go to: https://github.com/settings/tokens/new
   - Or: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)

2. **Configure Token**:
   - Note: "GitHub Workflows Project Access"
   - Expiration: 90 days (recommended) or No expiration
   - Select scopes:
     - ✅ `repo` - Full control of private repositories
     - ✅ `project` - Full control of projects

3. **Generate and Copy**:
   - Click "Generate token"
   - Copy token immediately (shown only once)

4. **Add to Repository**:
   - Repository → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `PROJECTS_TOKEN`
   - Value: [Paste your token]
   - Click "Add secret"

**Security Note**: This token has powerful permissions. Keep it secure and regenerate quarterly.

---

### Step 2: Create Project Board

**Purpose**: Track issues across workflow stages

**Setup**:

1. **Create New Project**:
   - Navigate to: https://github.com/users/YOUR_USERNAME/projects
   - Click "New project"
   - Select "Board" template
   - Name: "@claude-skills-factory" (or your project name)

2. **Configure Columns** (in this exact order):
   - To triage
   - Backlog
   - Ready
   - In Progress
   - In Review
   - Done

3. **Note Project Number**:
   - Project URL: `https://github.com/users/USERNAME/projects/7`
   - Project Number: `7`
   - Update workflows if using different number

---

### Step 3: Create Labels

**Purpose**: Enable automatic classification and status tracking

**Run These Commands**:

```bash
# Status labels (6)
gh label create "status: triage" --color "fbca04" --description "To Triage column"
gh label create "status: backlog" --color "d4c5f9" --description "Backlog column"
gh label create "status: ready" --color "0e8a16" --description "Ready column"
gh label create "status: in-progress" --color "1d76db" --description "In Progress column"
gh label create "status: in-review" --color "d876e3" --description "In Review column"
gh label create "status: done" --color "2ea44f" --description "Done column"

# Type labels (8)
gh label create "bug" --color "d73a4a" --description "Something isn't working"
gh label create "feature" --color "a2eeef" --description "New feature request"
gh label create "documentation" --color "0075ca" --description "Documentation improvements"
gh label create "question" --color "d876e3" --description "Questions or help needed"
gh label create "enhancement" --color "84b6eb" --description "Enhancement to existing feature"
gh label create "skill-request" --color "fbca04" --description "Request for new skill"
gh label create "agent-request" --color "c5def5" --description "Request for new agent"
gh label create "template-improvement" --color "7057ff" --description "Template improvements"

# Priority labels (4)
gh label create "P0" --color "b60205" --description "Critical priority"
gh label create "P1" --color "d93f0b" --description "High priority"
gh label create "P2" --color "fbca04" --description "Medium priority"
gh label create "P3" --color "0e8a16" --description "Low priority"

# Plan labels (3)
gh label create "plan" --color "0366d6" --description "Issue is a plan to convert to subtasks"
gh label create "subtask" --color "bfdadc" --description "Task created from a plan"
gh label create "plan-item" --color "d4c5f9" --description "Item belonging to a plan"
```

**Total**: 21 labels created

---

### Step 4: Apply Branch Protection

**Purpose**: Enforce PR workflow and quality checks

**Option A - Via GitHub UI**:

1. Navigate to: Repository → Settings → Branches
2. Click "Add branch protection rule"
3. Branch name pattern: `main`
4. Configure:
   - ✅ Require a pull request before merging
   - ✅ Require approvals: 1
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - Status checks: Select `claude-review`
   - ✅ Require conversation resolution before merging
   - ✅ Do not allow bypassing the above settings
5. Click "Create" or "Save changes"

**Option B - Via GitHub API**:

```bash
# Create configuration file
cat > .github/branch-protection-config.json <<EOF
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["claude-review"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": null,
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_conversation_resolution": true
}
EOF

# Apply protection (replace OWNER and REPO)
gh api repos/OWNER/REPO/branches/main/protection \
  --method PUT \
  --input .github/branch-protection-config.json
```

---

### Step 5: Verify Setup

**Quick Verification**:

```bash
# 1. Check secrets exist
gh secret list
# Expected: CLAUDE_CODE_OAUTH_TOKEN, PROJECTS_TOKEN

# 2. Check labels created
gh label list | wc -l
# Expected: 21+ labels

# 3. Check workflows exist
gh workflow list
# Expected: 6 workflows listed

# 4. Check branch protection
gh api repos/OWNER/REPO/branches/main/protection
# Expected: JSON with protection rules
```

**Setup Complete!** Your automation system is ready to use.

---

## Configuration

### Workflow Files Location

All workflows are in `.github/workflows/`:
- `claude.yml` - On-demand assistance
- `claude-code-review.yml` - Automatic PR reviews
- `issue-triage.yml` - Issue classification
- `plan-to-issues.yml` - Plan conversion
- `issue-to-project-sync.yml` - Issue → Board sync
- `project-to-issue-sync.yml` - Board → Issue sync

### Customizing Project Number

If using a different project number, update these workflows:

**Files to Update**:
- `issue-triage.yml` (line with `gh project item-add`)
- `plan-to-issues.yml` (line with `gh project item-add`)
- `issue-to-project-sync.yml` (GraphQL queries)

**Find and Replace**:
```bash
# Current
project item-add 7

# Replace with your number
project item-add YOUR_NUMBER
```

### Customizing Status Columns

If your project board has different column names:

**Update Mappings**:

In `issue-to-project-sync.yml`:
```yaml
# Map labels to your column names
- `status: triage` → "YOUR_COLUMN_NAME"
```

In `project-to-issue-sync.yml`:
```yaml
# Map column names to labels
- "YOUR_COLUMN_NAME" → `status: custom`
```

---

## Usage Guide

### Using Automatic Code Review

**How It Works**:
1. Create pull request (any branch → main)
2. Claude review workflow triggers automatically (within 30 seconds)
3. Claude analyzes all code changes
4. Review posted as PR comment (2-3 minutes)
5. Status check updates (pass/fail)

**What Claude Reviews**:
- Code quality and best practices
- Potential bugs or issues
- Security concerns
- Performance considerations
- Test coverage

**Manual Trigger**:
```bash
# Re-run review if needed
gh run rerun RUN_ID
```

---

### Using On-Demand Claude Assistance

**How to Use**:

In any issue or PR comment, mention `@claude`:

```
@claude please review this code

@claude help me write a test for this function

@claude what's the performance impact of this change?

@claude suggest improvements to this implementation

@claude explain how this algorithm works
```

**Response Time**: 1-2 minutes

**Who Can Use**: Team members only (OWNER, MEMBER, COLLABORATOR)

**Note**: External contributors cannot use @claude mentions (security)

---

### Using Issue Auto-Triage

**How It Works**:
1. Create new issue (any description)
2. Triage workflow triggers automatically (within 30 seconds)
3. Claude analyzes title and description
4. Labels applied (type + priority)
5. Issue added to project board
6. Triage summary comment posted

**What's Analyzed**:
- Issue type (bug, feature, documentation, etc.)
- Priority level (P0-P3)
- Completeness (has enough detail?)
- Potential duplicates

**Example**:

Create issue:
```
Title: Login button doesn't work on mobile
Body: When I click the login button on iOS Safari, nothing happens.
```

Claude adds:
- Labels: `bug`, `P1`
- Comment: Triage summary with analysis
- Adds to project board in "To triage" column

---

### Using Plan-to-Issues Automation

**How to Create a Plan**:

1. **Create Issue with Plan Label**:
```bash
gh issue create \
  --title "Plan: User Authentication Feature" \
  --label "plan" \
  --body "## Goal
Implement complete user authentication system

## Tasks
- [ ] Design login UI components
- [ ] Implement JWT authentication backend
- [ ] Add password reset flow
- [ ] Write integration tests
- [ ] Update documentation"
```

2. **Automation Executes** (within 1-2 minutes):
   - Parses all tasks from markdown
   - Creates child issue for each task
   - Links all to parent issue
   - Adds all to project board
   - Posts summary on parent issue

3. **Result**: 5 trackable subtask issues created

**Supported Task Formats**:

✅ **Markdown Checkboxes** (recommended):
```markdown
- [ ] Task 1
- [ ] Task 2
```

✅ **Numbered Lists**:
```markdown
1. Task 1
2. Task 2
```

✅ **Bulleted Lists**:
```markdown
- Task 1
* Task 2
```

**Best Practices**:
- Use descriptive task names
- One task per line
- Keep tasks actionable
- Use checkboxes for best results

---

### Using Status Sync

**Two Ways to Update Status**:

#### Option A: Update Issue Label

```bash
# Add status label to issue
gh issue edit 123 --add-label "status: in-progress"

# Automation:
# - Moves issue to "In Progress" on project board
# - Posts confirmation comment
```

#### Option B: Move on Project Board

1. Go to project board
2. Drag issue to "In Progress" column
3. Automation:
   - Adds `status: in-progress` label
   - Removes old status label
   - Posts status update comment

**Status Flow**:
```
To triage → Backlog → Ready → In Progress → In Review → Done
```

**Special Behavior**:
- Moving to "Done" → Automatically closes issue
- Reopening issue → Moves back to "To triage"

**Team Workflow**:
```
Developer starts work:
- Option A: Add "status: in-progress" label
- Option B: Move to "In Progress" on board
→ Both ways work, automation keeps them in sync

Code review:
- Move to "In Review"
→ Label updates, team sees status

Task complete:
- Move to "Done"
→ Issue closes, label added
```

---

## Workflow Details

### claude.yml - On-Demand Assistance

**Trigger**: @claude mentions in comments
**Runs on**: ubuntu-latest
**Timeout**: 10 minutes
**Permissions**: contents:read, pull-requests:read, issues:read, id-token:write

**Security**:
- Only OWNER/MEMBER/COLLABORATOR can trigger
- Tool allowlist: `gh issue:*`, `gh pr:*`, `npm:*`
- Concurrency: One at a time per issue/PR

**Monitoring**:
```bash
gh run list --workflow=claude.yml --limit 10
```

---

### claude-code-review.yml - Automatic PR Review

**Trigger**: Pull request (opened, synchronize, reopened)
**Runs on**: ubuntu-latest
**Timeout**: 10 minutes
**Permissions**: contents:read, pull-requests:write, id-token:write

**Review Focus**:
- Code quality, best practices
- Bugs, security issues
- Performance considerations
- Test coverage

**Concurrency**: Cancel previous runs on PR update

**Monitoring**:
```bash
gh run list --workflow=claude-code-review.yml --limit 10
gh pr checks PULL_NUMBER
```

---

### issue-triage.yml - Issue Classification

**Trigger**: Issues (opened)
**Runs on**: ubuntu-latest
**Timeout**: 5 minutes
**Permissions**: contents:read, issues:write, id-token:write

**Actions**:
1. Classify issue type
2. Assign priority
3. Check completeness
4. Detect duplicates
5. Add labels
6. Add to project board
7. Post triage summary

**Monitoring**:
```bash
gh run list --workflow=issue-triage.yml --limit 10
```

---

### plan-to-issues.yml - Plan Conversion

**Trigger**: Issues (labeled with `plan`)
**Runs on**: ubuntu-latest
**Timeout**: 10 minutes
**Permissions**: contents:read, issues:write, id-token:write

**Process**:
1. Parse tasks from issue body
2. Create child issue per task
3. Link to parent
4. Add to project board
5. Post summary

**Concurrency**: One per plan issue

**Monitoring**:
```bash
gh run list --workflow=plan-to-issues.yml --limit 10
```

---

### issue-to-project-sync.yml - Issue → Board

**Trigger**: Issues (labeled, closed, reopened)
**Runs on**: ubuntu-latest
**Timeout**: 5 minutes
**Permissions**: contents:read, issues:read, id-token:write

**Logic**:
```
Status label added → Determine target column → Update project item
Issue closed → Move to "Done"
Issue reopened → Move to "To triage"
```

**Concurrency**: One per issue

**Monitoring**:
```bash
gh run list --workflow=issue-to-project-sync.yml --limit 10
```

---

### project-to-issue-sync.yml - Board → Issue

**Trigger**: projects_v2_item (edited)
**Runs on**: ubuntu-latest
**Timeout**: 5 minutes
**Permissions**: contents:read, issues:write, id-token:write

**Logic**:
```
Item moved on board → Get issue number → Remove old status label →
Add new status label → Close/reopen if needed → Post comment
```

**Concurrency**: One per project item

**Monitoring**:
```bash
gh run list --workflow=project-to-issue-sync.yml --limit 10
```

---

## Troubleshooting

### Common Issues

#### Issue: Workflow Not Triggering

**Symptoms**: Created issue/PR but workflow didn't run

**Diagnosis**:
```bash
# Check if workflow exists and is active
gh workflow list

# Check recent runs
gh run list --limit 10

# Check for syntax errors
yamllint .github/workflows/WORKFLOW.yml
```

**Solutions**:
1. Verify workflow file is on `main` branch (not just local)
2. Check `if` conditions aren't filtering it out
3. Wait 5-10 minutes for GitHub to index new workflows
4. Verify GitHub Actions is enabled: Settings → Actions → General

---

#### Issue: "Secret not found" Error

**Symptoms**: Workflow fails with "CLAUDE_CODE_OAUTH_TOKEN not found"

**Diagnosis**:
```bash
# List secrets
gh secret list

# Check workflow references
grep -r "CLAUDE_CODE_OAUTH_TOKEN" .github/workflows/
```

**Solutions**:
1. Add secret: Repository → Settings → Secrets → Actions
2. Verify exact name match (case-sensitive)
3. Re-save secret if exists (might be expired)
4. Check you're in correct repository

---

#### Issue: Project Board Sync Failing

**Symptoms**: "Could not resolve to a ProjectV2" or "403 Forbidden"

**Diagnosis**:
```bash
# Check if PROJECTS_TOKEN exists
gh secret list | grep PROJECTS_TOKEN

# Check project number
# Visit: https://github.com/users/USERNAME/projects
# Verify number in URL
```

**Solutions**:
1. Verify PROJECTS_TOKEN has `repo` + `project` scopes
2. Update project number in workflows if different
3. Regenerate token if expired
4. Ensure project is accessible to token owner

**Common Mistakes**:
- Token scopes: Must be both `repo` AND `project`
- Project number: Must match URL (e.g., `/projects/7` = number 7)
- Token expiration: Check if token expired

---

#### Issue: Infinite Sync Loops

**Symptoms**: Dozens of rapid workflow runs, duplicate comments

**Diagnosis**:
```bash
# Check for rapid successive runs
gh run list --workflow=issue-to-project-sync.yml --limit 20
gh run list --workflow=project-to-issue-sync.yml --limit 20
```

**Solutions**:
1. Verify concurrency controls exist in workflow YAML
2. Check workflows aren't modifying their own triggers:
   - `issue-to-project-sync` should ONLY modify project board
   - `project-to-issue-sync` should ONLY modify issues
3. Review recent workflow changes for loop-causing logic

**Prevention**: Built-in concurrency controls prevent this

---

#### Issue: Claude Review Takes Too Long

**Symptoms**: PR review takes >5 minutes or times out

**Diagnosis**:
```bash
# Check workflow run logs
gh run view RUN_ID --log

# Look for:
# - Large PR size
# - Network timeouts
# - API rate limits
```

**Solutions**:
1. Split large PRs into smaller ones (<500 lines recommended)
2. Check GitHub API rate limits: `gh api rate_limit`
3. Re-run if transient error: `gh run rerun RUN_ID`

---

#### Issue: Labels Not Syncing

**Symptoms**: Move issue on board but label doesn't update

**Diagnosis**:
```bash
# Check workflow triggered
gh run list --workflow=project-to-issue-sync.yml --limit 5

# Verify label names match exactly
gh label list | grep "status:"
```

**Solutions**:
1. Verify status label names match exactly (case-sensitive)
2. Check project column names match mapping:
   - "In Progress" → `status: in-progress` (hyphen, not space)
3. Manually trigger by removing/re-adding status label
4. Check workflow logs for GraphQL errors

---

#### Issue: Wrong Priority Assigned

**Symptoms**: Issue classified as P2 but should be P0

**Solutions**:
1. **Manual Override**: Change label manually
   ```bash
   gh issue edit ISSUE_NUM --remove-label "P2"
   gh issue edit ISSUE_NUM --add-label "P0"
   ```
2. **Improve Issue Description**: Add more context for better classification
3. **Request Re-triage**: Add comment `@claude please re-evaluate priority`

---

### Monitoring Commands

**View All Recent Runs**:
```bash
gh run list --limit 20
```

**View Specific Workflow**:
```bash
gh run list --workflow=issue-triage.yml --limit 10
```

**View Failed Runs**:
```bash
gh run list --status failure --limit 10
```

**View Logs**:
```bash
gh run view RUN_ID --log
```

**Monitor in Real-Time**:
```bash
watch -n 5 'gh run list --limit 5'
```

---

## Advanced Configuration

### Custom Issue Types

Add domain-specific issue types:

```bash
# Create custom labels
gh label create "ui-bug" --color "fc8181" --description "UI/UX bug"
gh label create "api-bug" --color "f56565" --description "API/Backend bug"
gh label create "infrastructure" --color "4299e1" --description "Infrastructure task"
```

Then update `issue-triage.yml` classification logic to include new types.

---

### Custom Status Columns

If using different column names:

1. **Create Custom Labels**:
```bash
gh label create "status: blocked" --color "d73a4a" --description "Blocked column"
gh label create "status: testing" --color "1d76db" --description "Testing column"
```

2. **Update Sync Workflows**:
- Add mappings in `issue-to-project-sync.yml`
- Add mappings in `project-to-issue-sync.yml`

---

### Team-Specific Auto-Assignment

Add auto-assignment based on labels:

**In `issue-triage.yml`**, add after labeling:
```yaml
# Auto-assign based on type
- name: Auto-assign
  run: |
    if gh issue view ${{ github.event.issue.number }} --json labels --jq '.labels[].name' | grep -q "ui-bug"; then
      gh issue edit ${{ github.event.issue.number }} --add-assignee @ui-team-lead
    fi
```

---

### Notification Integration

Add Slack/Discord notifications:

**In workflow files**, add step:
```yaml
- name: Notify Team
  if: contains(github.event.issue.labels.*.name, 'P0')
  run: |
    curl -X POST ${{ secrets.SLACK_WEBHOOK_URL }} \
      -H 'Content-Type: application/json' \
      -d '{"text":"🚨 P0 Issue Created: ${{ github.event.issue.html_url }}"}'
```

---

## Maintenance

### Weekly Tasks

```bash
# Review failed workflow runs
gh run list --status failure --limit 20

# Check for stale issues
gh issue list --label "status: in-progress" --json number,title,updatedAt

# Verify secrets haven't expired
gh secret list
```

---

### Monthly Tasks

```bash
# Update Claude Code action version
# Check: https://github.com/anthropics/claude-code-action/releases

# Review and clean up labels
gh label list

# Analyze workflow performance
gh api /repos/OWNER/REPO/actions/runs \
  --jq '.workflow_runs[] | {name: .name, duration: .run_duration_ms}'
```

---

### Quarterly Tasks

```bash
# Regenerate PROJECTS_TOKEN (security best practice)
# 1. Create new token with same scopes
# 2. Update repository secret
# 3. Delete old token

# Review branch protection rules
gh api repos/OWNER/REPO/branches/main/protection

# Audit team access
gh api repos/OWNER/REPO/collaborators
```

---

### Backup

**Backup Configuration**:
```bash
# Backup workflows
tar -czf workflows-backup-$(date +%Y%m%d).tar.gz .github/workflows/

# Backup labels
gh label list --json name,description,color > labels-$(date +%Y%m%d).json

# Backup branch protection
gh api repos/OWNER/REPO/branches/main/protection > protection-$(date +%Y%m%d).json
```

---

## Getting Help

### Debug Checklist

When workflows fail:

1. ✅ Check workflow run logs: `gh run view RUN_ID --log`
2. ✅ Verify secrets exist: `gh secret list`
3. ✅ Check GitHub Actions enabled
4. ✅ Verify workflow file on main branch
5. ✅ Check for YAML syntax errors
6. ✅ Review GitHub API rate limits

---

### Support Resources

- **WORKFLOWS.md**: System overview and quick reference
- **Master Prompt**: `documentation/implementation/github-workflow-master-prompt.md`
- **Claude Code Docs**: https://docs.claude.com/claude-code
- **GitHub Actions Docs**: https://docs.github.com/actions
- **Create Issue**: Use `question` label for help

---

**Last Updated**: 2025-10-24
**Version**: 1.0.0
**Status**: Production Ready

All workflows are tested and production-ready. Follow this guide for setup and troubleshooting.
