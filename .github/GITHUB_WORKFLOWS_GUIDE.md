# GitHub Workflows - Complete Guide

**Version**: 2.0.0
**Last Updated**: October 28, 2025
**Status**: ✅ Production Ready

Complete documentation for GitHub automation system powered by Claude AI - covering setup, usage, workflows, emergency procedures, and troubleshooting.

---

## Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Available Workflows](#available-workflows)
4. [Initial Setup](#initial-setup)
5. [Usage Guide](#usage-guide)
6. [Emergency Procedures](#emergency-procedures)
7. [Troubleshooting](#troubleshooting)
8. [Security Model](#security-model)
9. [Maintenance](#maintenance)
10. [Advanced Configuration](#advanced-configuration)

---

## Overview

This repository includes a comprehensive GitHub automation system that provides:

### 🤖 AI-Powered Automation
- **Automatic Code Reviews** - Claude reviews every PR automatically
- **Automatic Issue Closure** - PRs auto-close linked issues when merged
- **Intelligent Issue Triage** - Auto-classification, labeling, and prioritization
- **Plan-to-Tasks Conversion** - Transform plans into trackable subtasks
- **Bidirectional Status Sync** - Keep issues and project boards aligned
- **Hierarchy Visualization** - Automatic plan/task/subtask tree generation

### 🔒 Enterprise Security
- 4-layer security model (GitHub permissions, tool restrictions, token scoping, branch protection)
- Access control based on team membership
- Strict tool allowlists for safe automation
- Complete audit trail
- Kill switch for emergency shutdown

### 📊 Project Management
- Automatic issue-to-project board assignment
- Status synchronization (issues ↔ project board)
- Plan auto-close when all tasks complete
- Real-time team visibility
- Comprehensive labeling system

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Repository                         │
│  Issues → PRs → Project Board                               │
└─────────┬───────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│              GitHub Actions Workflows                        │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Claude     │  │ PR→Issue     │  │ Issue Auto-  │    │
│  │ Code Review  │  │ Auto-Close   │  │   Triage     │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ Plan-to-     │  │ Plan Auto-   │  │  Hierarchy   │    │
│  │   Tasks      │  │    Close     │  │  Dashboard   │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐                       │
│  │ Issue→Board  │  │ Board→Issue  │                       │
│  │    Sync      │  │    Sync      │                       │
│  └──────────────┘  └──────────────┘                       │
└─────────┬───────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│              Claude Code AI Engine                           │
│  Code Analysis • Issue Classification • Plan Parsing •      │
│  Status Synchronization • GraphQL Operations                │
└─────────────────────────────────────────────────────────────┘
```

---

## Available Workflows

| Workflow | Trigger | Purpose | Status |
|----------|---------|---------|--------|
| **claude-code-review.yml** | PR opened/updated | Automatic code reviews | ✅ Active |
| **pr-issue-auto-close.yml** | PR merged | Auto-close linked issues | ✅ Active |
| **issue-triage.yml** | Issue created | Auto-classification | ✅ Active |
| **plan-validator.yml** | `plan` label | Validate plan format | ✅ Active |
| **plan-to-tasks.yml** | Plan validated | Create task issues | ✅ Active |
| **plan-auto-close.yml** | Task closed | Close plan when done | ✅ Active |
| **task-to-subtasks.yml** | `needs-subtasks` label | Create subtasks | ✅ Active |
| **smart-sync.yml** | Issue/board changes | Bidirectional sync | ✅ Active |
| **hierarchy-dashboard.yml** | Schedule + events | Visual tree (HIERARCHY.md) | ✅ Active |
| **workflow-health.yml** | Every 6 hours | Monitor system health | ✅ Active |

### Key Workflows Explained

**1. Automatic Code Review**
- **What**: Claude reviews every PR
- **When**: PR opened/updated
- **Output**: Review comment + status check

**2. PR→Issue Auto-Close** (NEW!)
- **What**: Closes linked issues when PR merges
- **Detects**: `Fixes #123`, `Closes #456`, `Resolves #789`
- **Actions**: Close issues, add comments, update board

**3. Plan Hierarchy**
```
PLAN (#100)
  ├─ TASK #101 (auto-created)
  ├─ TASK #102 (auto-created)
  │   ├─ SUBTASK #103 (auto-created if needs-subtasks)
  │   └─ SUBTASK #104
  └─ TASK #105
```

**4. Smart Sync**
- Updates issue when board changes
- Updates board when issue changes
- Prevents ping-pong loops with 10-second debounce

---

## Initial Setup

### Prerequisites

1. **GitHub Repository**
   - Issues enabled
   - Projects enabled
   - Actions enabled

2. **Required Tokens**
   - `CLAUDE_CODE_OAUTH_TOKEN`
   - `PROJECTS_TOKEN`

3. **Team Access**
   - At least COLLABORATOR permission for team members

**Total Setup Time**: ~15-20 minutes

---

### Step 1: Create Required Secrets

#### CLAUDE_CODE_OAUTH_TOKEN

**Purpose**: Authenticates Claude Code GitHub Action

**How to Add**:
1. Navigate to: Repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `CLAUDE_CODE_OAUTH_TOKEN`
4. Value: [Your Claude Code OAuth token]
5. Click "Add secret"

---

#### PROJECTS_TOKEN (Personal Access Token)

**Purpose**: Project board access (default GITHUB_TOKEN lacks permissions)

**Required Scopes**:
- ✅ `repo` (Full control of private repositories)
- ✅ `project` (Full control of projects)

**How to Create**:

1. Navigate to: https://github.com/settings/tokens/new
2. Configure Token:
   - Note: "GitHub Workflows Project Access"
   - Expiration: 90 days (recommended)
   - Select scopes: `repo` + `project`
3. Generate and Copy token
4. Add to Repository Secrets:
   - Name: `PROJECTS_TOKEN`
   - Value: [Your token]

**Security Note**: Regenerate quarterly for security

---

### Step 2: Create Project Board

1. **Create New Project**:
   - Navigate to: https://github.com/users/YOUR_USERNAME/projects
   - Click "New project"
   - Select "Board" template
   - Name: "@claude-skills-factory"

2. **Configure Columns** (exact order):
   1. To triage
   2. Backlog
   3. Ready
   4. In Progress
   5. In Review
   6. Done

3. **Note Project Number**:
   - From URL: `https://github.com/users/USERNAME/projects/7`
   - Project Number: `7`

---

### Step 3: Create Labels

**Status Labels** (6):
```bash
gh label create "status: triage" --color "fbca04" --description "To Triage column"
gh label create "status: backlog" --color "d4c5f9" --description "Backlog column"
gh label create "status: ready" --color "0e8a16" --description "Ready column"
gh label create "status: in-progress" --color "1d76db" --description "In Progress column"
gh label create "status: in-review" --color "d876e3" --description "In Review column"
gh label create "status: done" --color "2ea44f" --description "Done column"
```

**Type Labels** (8):
```bash
gh label create "bug" --color "d73a4a" --description "Something isn't working"
gh label create "feature" --color "a2eeef" --description "New feature request"
gh label create "documentation" --color "0075ca" --description "Documentation improvements"
gh label create "question" --color "d876e3" --description "Questions or help needed"
gh label create "enhancement" --color "84b6eb" --description "Enhancement to existing feature"
gh label create "skill-request" --color "fbca04" --description "Request for new skill"
gh label create "agent-request" --color "c5def5" --description "Request for new agent"
gh label create "template-improvement" --color "7057ff" --description "Template improvements"
```

**Priority Labels** (4):
```bash
gh label create "P0" --color "b60205" --description "Critical priority"
gh label create "P1" --color "d93f0b" --description "High priority"
gh label create "P2" --color "fbca04" --description "Medium priority"
gh label create "P3" --color "0e8a16" --description "Low priority"
```

**Plan Labels** (4):
```bash
gh label create "plan" --color "0366d6" --description "Issue is a plan"
gh label create "plan-validated" --color "0e8a16" --description "Plan passed validation"
gh label create "task" --color "bfdadc" --description "Task from plan"
gh label create "subtask" --color "e4e669" --description "Subtask from task"
```

**Total**: 22 labels

---

### Step 4: Verify Setup

```bash
# Check secrets
gh secret list
# Expected: CLAUDE_CODE_OAUTH_TOKEN, PROJECTS_TOKEN

# Check labels
gh label list | wc -l
# Expected: 22+ labels

# Check workflows
gh workflow list
# Expected: 10 workflows

# Test with sample issue
gh issue create --title "Test Issue" --body "Testing automation" --label "question"
# Should auto-triage and add to project board
```

**Setup Complete!** ✅

---

## Usage Guide

### 1. Automatic Code Review

**How It Works**:
1. Create pull request
2. Claude review triggers automatically (30 seconds)
3. Review posted as comment (2-3 minutes)
4. Status check updates

**What Claude Reviews**:
- Code quality and best practices
- Security vulnerabilities
- Performance considerations
- Test coverage

**No action needed** - fully automatic!

---

### 2. Automatic Issue Closure on PR Merge

**How to Link Issues to PRs**:

In PR body, title, or commits, use:
```
Fixes #123
Closes #456
Resolves #789
Related to #111
```

**When PR Merges**:
- ✅ Issues closed automatically
- ✅ Comment added linking to PR
- ✅ Project board updated (status: done)
- ✅ Labels updated

**Example**:
```bash
# Create PR with linked issues
gh pr create \
  --title "feat: Add user authentication" \
  --body "Fixes #50, Closes #51"

# Merge PR
gh pr merge 123 --squash

# Result:
# → Issue #50 closed ✅
# → Issue #51 closed ✅
# → Both moved to Done on project board ✅
```

---

### 3. Issue Auto-Triage

**How It Works**:
1. Create issue
2. Triage triggers (30 seconds)
3. Labels applied (type + priority)
4. Added to project board
5. Summary comment posted

**Example**:
```bash
gh issue create \
  --title "Login button doesn't work on mobile" \
  --body "When I click login on iOS Safari, nothing happens."

# Claude adds:
# Labels: bug, P1
# Comment: Analysis and recommendations
# Board: Added to "To triage"
```

---

### 4. Plan-to-Tasks Automation

**Create a Plan**:
```bash
gh issue create \
  --title "Plan: User Authentication" \
  --label "plan" \
  --body "## Goal
Complete user authentication system

## Tasks
- [ ] Design login UI
- [ ] Implement JWT backend
- [ ] Add password reset
- [ ] Write tests
- [ ] Update docs"
```

**Automation Creates**:
- ✅ 5 task issues (one per checkbox)
- ✅ All linked to parent plan
- ✅ All added to project board
- ✅ Summary posted

**Important**: Keep plans to 5-10 tasks (enforced by plan-validator)

---

### 5. Status Synchronization

**Two Ways to Update**:

**Option A - Update Issue**:
```bash
gh issue edit 123 --add-label "status: in-progress"
# → Moves to "In Progress" on board
```

**Option B - Update Board**:
```
Drag issue to "In Progress" column on board
# → Adds "status: in-progress" label
```

**Status Flow**:
```
To triage → Backlog → Ready → In Progress → In Review → Done
```

**Special**: Moving to "Done" auto-closes the issue

---

## Emergency Procedures

### 🚨 IMMEDIATE: Disable All Workflows

**When to Use**: Runaway workflows, spam issues, critical bugs

```bash
# 1. Activate kill switch
echo "STATUS: DISABLED" > .github/WORKFLOW_KILLSWITCH
git add .github/WORKFLOW_KILLSWITCH
git commit -m "emergency: Disable all workflows"
git push origin main --no-verify

# All workflows will check this file and exit immediately
```

**Re-enable**:
```bash
echo "STATUS: ENABLED" > .github/WORKFLOW_KILLSWITCH
git commit -am "chore: Re-enable workflows"
git push
```

---

### 🧹 Clean Up Spam Issues

**If workflows created many incorrect issues**:

```bash
# Dry run first (see what would be closed)
chmod +x .github/EMERGENCY_CLEANUP.sh
.github/EMERGENCY_CLEANUP.sh true

# Actually close issues
.github/EMERGENCY_CLEANUP.sh false
```

The script targets issues with:
- "Task:" or "Subtask:" in title
- Created by automation
- Potentially incorrect format

---

### ⚡ Emergency Push (Bypass Reviews)

**Method 1: Use --no-verify Flag**
```bash
git push origin main --no-verify
# Skips pre-push hooks
```

**Method 2: PR with [EMERGENCY] Tag**
```bash
gh pr create --title "[EMERGENCY] Fix critical bug" --body "..."
# Review can be bypassed
```

**Method 3: Disable Branch Protection Temporarily**
1. Go to: Settings → Branches → main → Edit
2. Uncheck "Require status checks"
3. Push your fix
4. **RE-ENABLE immediately after** ⚠️

---

### 🔍 Monitor System Health

```bash
# Check workflow health
gh run list --status failure --limit 10

# Check rate limits
gh api rate_limit --jq '.resources.core.remaining, .resources.graphql.remaining'

# View recent activity
gh run list --limit 20
```

---

### 📋 Emergency Response Checklist

- [ ] Kill switch activated (STATUS: DISABLED)
- [ ] Spam issues cleaned up
- [ ] Rate limits checked
- [ ] Bug identified and fixed
- [ ] Fix tested on feature branch
- [ ] Code review completed
- [ ] Kill switch deactivated (STATUS: ENABLED)
- [ ] Monitor for 48 hours

---

## Troubleshooting

### Workflow Not Triggering

**Symptoms**: Created issue/PR but workflow didn't run

**Check**:
```bash
# Verify workflow exists
gh workflow list

# Check recent runs
gh run list --limit 10

# Check for syntax errors
yamllint .github/workflows/WORKFLOW.yml
```

**Solutions**:
- Verify workflow file on `main` branch
- Check `if` conditions aren't filtering
- Wait 5-10 minutes for GitHub to index
- Verify Actions enabled: Settings → Actions

---

### "Secret not found" Error

**Symptoms**: Workflow fails with secret error

**Check**:
```bash
gh secret list
```

**Solutions**:
- Add secret: Settings → Secrets → Actions
- Verify exact name (case-sensitive)
- Re-save if expired
- Check correct repository

---

### Project Board Sync Failing

**Symptoms**: "Could not resolve to a ProjectV2" or "403 Forbidden"

**Check**:
```bash
# Verify PROJECTS_TOKEN exists
gh secret list | grep PROJECTS_TOKEN

# Check project number matches workflows
# URL: https://github.com/users/USERNAME/projects/7
# Number: 7
```

**Solutions**:
- Verify PROJECTS_TOKEN has `repo` + `project` scopes
- Update project number in workflows
- Regenerate token if expired
- Ensure project accessible to token owner

---

### Infinite Sync Loops

**Symptoms**: Dozens of rapid runs, duplicate comments

**Check**:
```bash
# Check for rapid runs
gh run list --workflow=smart-sync.yml --limit 20
```

**Solutions**:
- Verify concurrency controls in workflow
- Check 10-second debounce is working
- Review recent changes for loop-causing logic

**Prevention**: Built-in safeguards prevent this

---

### Claude Review Takes Too Long

**Symptoms**: PR review >5 minutes or timeout

**Check**:
```bash
# View logs
gh run view RUN_ID --log

# Check PR size
gh pr diff PR_NUMBER | wc -l
```

**Solutions**:
- Split large PRs (<500 lines recommended)
- Check API rate limits: `gh api rate_limit`
- Re-run if transient: `gh run rerun RUN_ID`

---

### Labels Not Syncing

**Symptoms**: Board move doesn't update label

**Check**:
```bash
# Verify workflow triggered
gh run list --workflow=smart-sync.yml --limit 5

# Check label names
gh label list | grep "status:"
```

**Solutions**:
- Verify label names match exactly (hyphen not space)
- Check column names match mapping
- Manually trigger by re-labeling
- Check logs for GraphQL errors

---

### Wrong Priority Assigned

**Symptoms**: Auto-triage assigned wrong priority

**Solutions**:
```bash
# Manual override
gh issue edit ISSUE_NUM --remove-label "P2"
gh issue edit ISSUE_NUM --add-label "P0"

# Improve issue description for better classification
# Or accept and adjust manually
```

---

## Security Model

### 4-Layer Security Architecture

**Layer 1: GitHub Permissions**
```yaml
# Only team members trigger workflows
if: contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'),
             github.event.comment.author_association)
```

**Layer 2: Tool Restrictions**
```yaml
# Allowlist specific commands
claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh pr:*)"'
# Blocks: git push, rm -rf, curl, etc.
```

**Layer 3: Token Scoping**
- `CLAUDE_CODE_OAUTH_TOKEN`: Claude operations only
- `PROJECTS_TOKEN`: `repo` + `project` (no admin)
- `GITHUB_TOKEN`: Minimal read permissions

**Layer 4: Branch Protection**
- Required PR workflow
- Status checks required (claude-review)
- No force pushes
- Conversation resolution required

### Access Control Matrix

| User Type | Code Review | PR Auto-Close | Triage | Manual Triggers |
|-----------|-------------|---------------|--------|-----------------|
| **External** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **Collaborator** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Member/Owner** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

---

## Maintenance

### Weekly Tasks

```bash
# Review failed runs
gh run list --status failure --limit 10

# Check stale issues
gh issue list --label "status: in-progress" --json number,title,updatedAt

# Verify secrets valid
gh secret list
```

### Monthly Tasks

```bash
# Update workflow versions
# Check: https://github.com/anthropics/claude-code-action/releases

# Clean up labels
gh label list

# Analyze performance
gh api /repos/OWNER/REPO/actions/runs \
  --jq '.workflow_runs[] | {name: .name, duration: .run_duration_ms}'
```

### Quarterly Tasks

```bash
# Regenerate PROJECTS_TOKEN
# 1. Create new token (same scopes)
# 2. Update repository secret
# 3. Delete old token

# Review branch protection
gh api repos/OWNER/REPO/branches/main/protection

# Audit team access
gh api repos/OWNER/REPO/collaborators
```

### Backup Configuration

```bash
# Backup workflows
tar -czf workflows-backup-$(date +%Y%m%d).tar.gz .github/workflows/

# Backup labels
gh label list --json name,description,color > labels-$(date +%Y%m%d).json

# Backup branch protection
gh api repos/OWNER/REPO/branches/main/protection > protection-$(date +%Y%m%d).json
```

---

## Advanced Configuration

### Customize Project Number

**If using different project number**:

Update in these workflows:
- `issue-triage.yml` (gh project item-add)
- `plan-to-tasks.yml` (gh project item-add)
- `smart-sync.yml` (GraphQL queries)

**Find and replace**:
```bash
# Find current
grep -r "project item-add 7" .github/workflows/

# Replace with your number
sed -i 's/project item-add 7/project item-add YOUR_NUMBER/g' .github/workflows/*.yml
```

---

### Custom Status Columns

**If using different column names**:

1. **Create Custom Labels**:
```bash
gh label create "status: blocked" --color "d73a4a"
gh label create "status: testing" --color "1d76db"
```

2. **Update smart-sync.yml**:
   - Add column → label mappings
   - Add label → column mappings

---

### Team-Specific Auto-Assignment

**Add to issue-triage.yml**:
```yaml
- name: Auto-assign
  run: |
    if gh issue view ${{ github.event.issue.number }} --json labels --jq '.labels[].name' | grep -q "bug"; then
      gh issue edit ${{ github.event.issue.number }} --add-assignee @bug-team-lead
    fi
```

---

### Notification Integration

**Add Slack/Discord notifications**:

```yaml
- name: Notify Team
  if: contains(github.event.issue.labels.*.name, 'P0')
  run: |
    curl -X POST ${{ secrets.SLACK_WEBHOOK_URL }} \
      -H 'Content-Type: application/json' \
      -d '{"text":"🚨 P0 Issue: ${{ github.event.issue.html_url }}"}'
```

---

## Quick Reference

### Common Commands

```bash
# List workflow runs
gh run list --limit 10

# View specific workflow
gh run list --workflow=issue-triage.yml --limit 5

# Check run logs
gh run view RUN_ID --log

# Create plan issue
gh issue create --title "Plan: Feature Name" --label "plan" --body "..."

# Link issue to PR
gh pr create --title "Fix bug" --body "Fixes #123"

# Add status label
gh issue edit ISSUE_NUM --add-label "status: ready"

# Check rate limits
gh api rate_limit
```

### Labels Quick Reference

**Status** (6): triage, backlog, ready, in-progress, in-review, done
**Type** (8): bug, feature, documentation, question, enhancement, skill-request, agent-request, template-improvement
**Priority** (4): P0 (Critical), P1 (High), P2 (Medium), P3 (Low)
**Plan** (4): plan, plan-validated, task, subtask

---

## Benefits

### For Developers
- ✅ Instant code review feedback
- ✅ No manual issue closing after PR merge
- ✅ No manual issue labeling
- ✅ Flexible status updates
- ✅ Clear project visibility

### For Project Managers
- ✅ Complete visibility across team
- ✅ Automatic progress tracking
- ✅ Consistent categorization
- ✅ Real-time status updates
- ✅ Plan/task hierarchy visualization

### For the Team
- ✅ 70% reduction in manual overhead
- ✅ Faster triage and categorization
- ✅ Better organization
- ✅ Complete audit trail
- ✅ Automatic issue lifecycle management

---

## Important Notes

### Testing Workflow Changes

**NEVER push workflow changes directly to main!**

**Correct Process**:
1. Create feature branch
2. Make workflow changes
3. Test on feature branch (limited)
4. Code review
5. Merge one workflow at a time
6. Monitor for 24 hours before next

---

### Kill Switch File

**Location**: `.github/WORKFLOW_KILLSWITCH`

**All workflows check this file before running**

**Current Status**:
```bash
cat .github/WORKFLOW_KILLSWITCH
# STATUS: ENABLED
```

---

### Rate Limits

**GitHub API Limits**:
- Personal: 5,000/hour
- OAuth: 5,000/hour
- Actions: 1,000/hour per repo

**Monitor**:
```bash
gh api rate_limit
```

**Circuit Breaker**: Workflows require 50+ remaining before executing

---

## Support

**Documentation**:
- This guide (complete reference)
- Workflow files in `.github/workflows/`
- HIERARCHY.md (plan/task tree visualization)

**External Resources**:
- Claude Code Docs: https://docs.claude.com/claude-code
- GitHub Actions: https://docs.github.com/actions
- GitHub Projects: https://docs.github.com/issues/planning-and-tracking-with-projects

**Getting Help**:
- Create issue with `question` label
- Check troubleshooting section above
- Review workflow logs: `gh run view RUN_ID --log`

---

## Version History

**v2.0.0** (2025-10-28):
- Consolidated from 6 files into single source of truth
- Added PR-to-issue auto-close documentation
- Enhanced emergency procedures
- Improved troubleshooting guide
- Updated with all 10 active workflows

**v1.0.0** (2025-10-24):
- Initial documentation (split across multiple files)
- Emergency response after incident
- Kill switch and cleanup systems

---

**This is the single source of truth for GitHub automation. All essential information consolidated here.**

**Last Updated**: October 28, 2025
**Status**: ✅ Production Ready, Battle-Tested
**Workflows Active**: 10/10
