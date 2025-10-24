# GitHub Workflow Automation - Master Implementation Prompt

**Version**: 1.0.0
**Date**: 2025-10-24
**Purpose**: Complete blueprint for implementing comprehensive GitHub workflow automation with Claude Code integration, issue management, project board sync, and intelligent automation.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Architecture](#architecture)
4. [Implementation Steps](#implementation-steps)
5. [Workflow Specifications](#workflow-specifications)
6. [Security Model](#security-model)
7. [Testing & Validation](#testing--validation)
8. [Troubleshooting](#troubleshooting)

---

## Overview

This master prompt provides complete instructions for implementing a production-ready GitHub workflow automation system with:

### Core Features
- ✅ **Claude Code Integration** - AI-powered code reviews and assistance
- ✅ **Intelligent Issue Triage** - Automatic classification and labeling
- ✅ **Plan-to-Issues Automation** - Convert plans to trackable subtasks
- ✅ **Bidirectional Status Sync** - Issues ↔ Project Board synchronization
- ✅ **Branch Protection** - Enforce PR workflow with required reviews
- ✅ **Project Board Integration** - Automatic issue/PR tracking

### Benefits
- **Team Alignment**: Everyone stays in sync (issues, labels, board)
- **Automation**: Reduce manual overhead by 70%
- **Quality Gates**: Automated reviews and validation
- **Visibility**: Complete audit trail and status tracking

---

## Prerequisites

### Required Tokens & Secrets

#### 1. CLAUDE_CODE_OAUTH_TOKEN
- **Purpose**: Authenticate Claude Code GitHub Action
- **How to obtain**: Contact Anthropic or use provided token
- **Scope**: Full Claude Code capabilities
- **Where to add**: Repository → Settings → Secrets → Actions → `CLAUDE_CODE_OAUTH_TOKEN`

#### 2. PROJECTS_TOKEN (Personal Access Token - Classic)
- **Purpose**: Project board access (default GITHUB_TOKEN lacks permissions)
- **Required Scopes**:
  - `repo` (Full control of private repositories)
  - `project` (Full control of projects)
- **How to create**:
  1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  2. Generate new token (classic)
  3. Select scopes: `repo`, `project`
  4. Generate token and copy immediately
- **Where to add**: Repository → Settings → Secrets → Actions → `PROJECTS_TOKEN`

### Repository Configuration

```bash
# Enable Issues
Repository → Settings → Features → ✅ Issues

# Enable Projects
Repository → Settings → Features → ✅ Projects

# Enable Discussions (optional)
Repository → Settings → Features → ✅ Discussions
```

---

## Architecture

### System Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      GitHub Repository                          │
│                                                                 │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐      │
│  │   Issues     │   │ Pull Requests│   │ Project Board│      │
│  │              │   │              │   │              │      │
│  │ - Labels     │   │ - Reviews    │   │ - Columns    │      │
│  │ - State      │   │ - Checks     │   │ - Status     │      │
│  │ - Comments   │   │ - Comments   │   │ - Items      │      │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘      │
│         │                  │                   │              │
└─────────┼──────────────────┼───────────────────┼──────────────┘
          │                  │                   │
          ▼                  ▼                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                  GitHub Actions Workflows                        │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ 1. claude.yml - On-demand Claude assistance               │ │
│  │    Trigger: @claude mentions in issues/PRs                │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ 2. claude-code-review.yml - Automatic PR reviews          │ │
│  │    Trigger: Pull request opened/updated                   │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ 3. issue-triage.yml - Intelligent issue classification    │ │
│  │    Trigger: Issue opened                                  │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ 4. plan-to-issues.yml - Convert plans to subtasks         │ │
│  │    Trigger: Issue labeled with 'plan'                     │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ 5. issue-to-project-sync.yml - Issue → Board sync         │ │
│  │    Trigger: Issue labeled/closed/reopened                 │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ 6. project-to-issue-sync.yml - Board → Issue sync         │ │
│  │    Trigger: Project item moved/updated                    │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
          │                  │                   │
          ▼                  ▼                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Claude Code Action                            │
│                 (AI-Powered Automation)                          │
│                                                                 │
│  • Code review and analysis                                    │
│  • Issue classification and labeling                           │
│  • Plan parsing and subtask creation                           │
│  • Status synchronization logic                                │
│  • GraphQL queries for project board                           │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

**Issue Creation Flow**:
```
New Issue Created
    ↓
Issue Triage Workflow
    ↓ (Classifies & Labels)
Add to Project Board
    ↓
Issue-to-Project Sync
    ↓ (Sets initial status)
Project Board Updated
```

**Plan-to-Issues Flow**:
```
Issue with 'plan' label
    ↓
Plan-to-Issues Workflow
    ↓ (Parses tasks)
Create Child Issues (6x subtask)
    ↓
Link to Parent
    ↓
Add all to Project Board
    ↓
Post Summary Comment
```

**Status Sync Flow (Bidirectional)**:
```
Option A: Developer moves issue on board
    ↓
Project-to-Issue Sync
    ↓
Update issue labels & state
    ↓
Post status comment

Option B: Developer adds status label
    ↓
Issue-to-Project Sync
    ↓
Move project item to column
    ↓
Post confirmation comment
```

---

## Implementation Steps

### Phase 1: Repository Setup (15 min)

#### Step 1.1: Create Secrets

```bash
# Navigate to repository settings
Repository → Settings → Secrets and variables → Actions

# Add CLAUDE_CODE_OAUTH_TOKEN
- Click "New repository secret"
- Name: CLAUDE_CODE_OAUTH_TOKEN
- Value: [Your Claude Code token]
- Click "Add secret"

# Add PROJECTS_TOKEN
- Click "New repository secret"
- Name: PROJECTS_TOKEN
- Value: [Your Personal Access Token with repo + project scopes]
- Click "Add secret"
```

#### Step 1.2: Create Project Board

```bash
# Create new project (Projects V2)
User/Org → Projects → New project → Board

# Configure columns
Create columns in this exact order:
1. To triage
2. Backlog
3. Ready
4. In Progress
5. In Review
6. Done

# Note the project number (appears in URL)
Example: https://github.com/users/USERNAME/projects/7
Project number: 7
```

#### Step 1.3: Create Labels

```bash
# Status labels (for sync)
gh label create "status: triage" --color "fbca04" --description "To Triage column"
gh label create "status: backlog" --color "d4c5f9" --description "Backlog column"
gh label create "status: ready" --color "0e8a16" --description "Ready column"
gh label create "status: in-progress" --color "1d76db" --description "In Progress column"
gh label create "status: in-review" --color "d876e3" --description "In Review column"
gh label create "status: done" --color "2ea44f" --description "Done column"

# Issue type labels (for triage)
gh label create "bug" --color "d73a4a" --description "Something isn't working"
gh label create "feature" --color "a2eeef" --description "New feature request"
gh label create "documentation" --color "0075ca" --description "Documentation improvements"
gh label create "question" --color "d876e3" --description "Questions or help needed"
gh label create "enhancement" --color "84b6eb" --description "Enhancement to existing feature"
gh label create "skill-request" --color "fbca04" --description "Request for new skill"
gh label create "agent-request" --color "c5def5" --description "Request for new agent"

# Priority labels (for triage)
gh label create "P0" --color "b60205" --description "Critical priority"
gh label create "P1" --color "d93f0b" --description "High priority"
gh label create "P2" --color "fbca04" --description "Medium priority"
gh label create "P3" --color "0e8a16" --description "Low priority"

# Plan labels (for plan-to-issues)
gh label create "plan" --color "0366d6" --description "Issue is a plan to convert to subtasks"
gh label create "subtask" --color "bfdadc" --description "Task created from a plan"
gh label create "plan-item" --color "d4c5f9" --description "Item belonging to a plan"
```

### Phase 2: Workflow Files (30 min)

Create these workflow files in `.github/workflows/` directory:

#### File 1: claude.yml

```yaml
name: Claude Code

on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]

concurrency:
  group: claude-${{ github.event.issue.number || github.event.pull_request.number }}
  cancel-in-progress: false

jobs:
  claude:
    if: |
      (
        (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@claude') && contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)) ||
        (github.event_name == 'pull_request_review_comment' && contains(github.event.comment.body, '@claude') && contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association))
      )
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: read
      issues: read
      id-token: write
      actions: read

    steps:
      - uses: actions/checkout@v4

      - name: Run Claude
        uses: anthropics/claude-code-action@v1
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: |
            Help with the user's request in the comment above.
          claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh pr:*),Bash(npm:*)"'
```

#### File 2: claude-code-review.yml

```yaml
name: Claude Code Review

on:
  pull_request:
    types: [opened, synchronize, reopened]

concurrency:
  group: claude-review-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  claude-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
      id-token: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Review Pull Request
        uses: anthropics/claude-code-action@v1
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: |
            Review this pull request for:
            - Code quality and best practices
            - Potential bugs or issues
            - Performance considerations
            - Security concerns
            - Test coverage

            Provide constructive feedback and suggestions.
          claude_args: '--allowed-tools "Bash(gh pr:*),Bash(gh issue:*)"'
```

#### File 3: issue-triage.yml

```yaml
name: Issue Auto-Triage

on:
  issues:
    types: [opened]

concurrency:
  group: triage-${{ github.event.issue.number }}
  cancel-in-progress: false

jobs:
  triage:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
      id-token: write

    steps:
      - uses: actions/checkout@v4

      - name: Triage Issue
        uses: anthropics/claude-code-action@v1
        env:
          GH_TOKEN: ${{ secrets.PROJECTS_TOKEN }}
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: |
            # Issue Auto-Triage Task

            Analyze issue #${{ github.event.issue.number }} and perform comprehensive triage.

            ## Issue Information
            **Title**: ${{ github.event.issue.title }}
            **Body**:
            ```
            ${{ github.event.issue.body }}
            ```
            **Author**: @${{ github.event.issue.user.login }}

            ## Analysis Framework

            ### 1. Issue Type Classification
            Classify as ONE of:
            - **bug**: Something isn't working correctly
            - **feature**: New capability or enhancement request
            - **documentation**: Improvements to docs, README, or examples
            - **question**: User needs help or clarification
            - **enhancement**: Improvement to existing functionality
            - **skill-request**: Request for new skill example
            - **agent-request**: Request for new agent example
            - **template-improvement**: Improvements to generation templates

            ### 2. Priority Assessment (P0-P3)
            - **P0 (Critical)**: Blocks all users, security issue, data loss risk
            - **P1 (High)**: Major functionality broken, affects many users
            - **P2 (Medium)**: Important but has workaround, affects some users
            - **P3 (Low)**: Nice to have, minimal impact, cosmetic issues

            ### 3. Completeness Check
            Verify issue has:
            - Clear description of problem/request
            - Steps to reproduce (for bugs)
            - Expected vs actual behavior (for bugs)
            - Use case explanation (for features)

            If incomplete, request additional information via comment.

            ### 4. Duplicate Detection
            Search for similar issues:
            ```bash
            gh search issues --repo OWNER/REPO "[search terms]" --state all
            ```

            If duplicate found, add 'duplicate' label and reference original.

            ### 5. Apply Labels
            ```bash
            # Type label (ONE only)
            gh issue edit ${{ github.event.issue.number }} --add-label "bug"

            # Priority label (ONE only)
            gh issue edit ${{ github.event.issue.number }} --add-label "P2"
            ```

            ### 6. Add to Project Board
            After labeling, add to project board:
            ```bash
            gh project item-add 7 --owner OWNER --url ${{ github.event.issue.html_url }}
            ```

            ### 7. Post Triage Summary
            ```bash
            gh issue comment ${{ github.event.issue.number }} --body "## 🤖 Issue Triage Complete

            **Type**: [type]
            **Priority**: [priority]
            **Completeness**: [✅ Complete / ⚠️ Needs info]

            [Additional notes or requests for information]

            *Automated by issue-triage workflow*"
            ```

            ## Error Handling
            - If project add fails, continue (issue still labeled)
            - If duplicate detection fails, skip (not critical)
            - Always add at least type and priority labels

            ## Now Execute
            Perform the triage analysis and actions above.

          claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh search:*),Bash(gh project:*)"'
```

#### File 4: plan-to-issues.yml

```yaml
name: Plan to Issues Automation

on:
  issues:
    types: [opened, labeled]

concurrency:
  group: plan-to-issues-${{ github.event.issue.number }}
  cancel-in-progress: false

jobs:
  create-subtasks:
    if: |
      github.event.action == 'labeled' && github.event.label.name == 'plan' ||
      github.event.action == 'opened' && contains(toJSON(github.event.issue.labels.*.name), 'plan')
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
      id-token: write

    steps:
      - uses: actions/checkout@v4

      - name: Create Subtask Issues
        uses: anthropics/claude-code-action@v1
        env:
          GH_TOKEN: ${{ secrets.PROJECTS_TOKEN }}
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: |
            # Plan to Issues Automation

            Convert plan issue into trackable subtask issues.

            ## Plan Issue
            **Issue #**: ${{ github.event.issue.number }}
            **Title**: ${{ github.event.issue.title }}
            **Body**:
            ```
            ${{ github.event.issue.body }}
            ```

            ## Your Task
            1. Parse the plan and extract all tasks
            2. Create child issue for each task
            3. Link everything together
            4. Add all to project board

            ## Task Formats Supported
            - Markdown checkboxes: `- [ ] Task name`
            - Numbered lists: `1. Task name`
            - Bulleted lists: `- Task name` or `* Task name`

            ## Step-by-Step

            ### Step 1: Parse Tasks
            Extract all tasks from issue body above.

            ### Step 2: Create Child Issues
            For EACH task:
            ```bash
            gh issue create \
              --title "Task: [task text]" \
              --label "subtask,plan-item" \
              --body "## Parent Plan

            Part of #${{ github.event.issue.number }}: ${{ github.event.issue.title }}

            ## Task Description
            [task text]

            ---
            **Parent**: #${{ github.event.issue.number }}
            **Project**: [@project-name](PROJECT_URL)"
            ```

            ### Step 3: Add to Project Board
            ```bash
            gh project item-add PROJECT_NUMBER --owner OWNER --url [ISSUE_URL]
            ```

            ### Step 4: Post Summary
            ```bash
            gh issue comment ${{ github.event.issue.number }} --body "## 🤖 Plan Automation Complete

            ### Subtasks Created
            - [ ] #[num] - [title]
            - [ ] #[num] - [title]

            **Total**: [count]
            **Project Board**: All added

            *Automated by plan-to-issues workflow*"
            ```

            ## Execute
            Create subtasks now.

          claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh project:*)"'
```

#### File 5: issue-to-project-sync.yml

```yaml
name: Issue to Project Board Sync

on:
  issues:
    types: [labeled, closed, reopened]

concurrency:
  group: issue-sync-${{ github.event.issue.number }}
  cancel-in-progress: false

jobs:
  sync-to-project:
    if: |
      (github.event.action == 'labeled' && startsWith(github.event.label.name, 'status:')) ||
      github.event.action == 'closed' ||
      github.event.action == 'reopened'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: read
      id-token: write

    steps:
      - uses: actions/checkout@v4

      - name: Sync Issue to Project
        uses: anthropics/claude-code-action@v1
        env:
          GH_TOKEN: ${{ secrets.PROJECTS_TOKEN }}
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: |
            # Issue to Project Board Sync

            Synchronize issue status to project board.

            ## Issue Info
            **Issue**: #${{ github.event.issue.number }}
            **State**: ${{ github.event.issue.state }}
            **Action**: ${{ github.event.action }}
            **URL**: ${{ github.event.issue.html_url }}

            ## Task
            1. Find/add issue in project board
            2. Determine target status from labels
            3. Update project item status column

            ## Label to Status Mapping
            - `status: triage` → "To triage"
            - `status: backlog` → "Backlog"
            - `status: ready` → "Ready"
            - `status: in-progress` → "In Progress"
            - `status: in-review` → "In Review"
            - `status: done` → "Done"
            - Issue closed → "Done"

            ## Steps

            ### 1. Check if in project
            ```bash
            gh api graphql -f query='...' # Query for project item
            ```
            If not found, add it:
            ```bash
            gh project item-add PROJECT_NUMBER --owner OWNER --url ${{ github.event.issue.html_url }}
            ```

            ### 2. Get current labels
            ```bash
            gh issue view ${{ github.event.issue.number }} --json labels
            ```

            ### 3. Determine target status
            Priority order: done > in-review > in-progress > ready > backlog > triage

            ### 4. Update project item
            Use GraphQL mutation to update status field.

            ### 5. Post comment (only for label changes)
            ```bash
            gh issue comment ${{ github.event.issue.number }} --body "## 🔄 Project Board Updated

            Moved to **[status]** on project board.

            *Automated sync*"
            ```

            ## Execute
            Sync the status now.

          claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh api:*),Bash(gh project:*)"'
```

#### File 6: project-to-issue-sync.yml

```yaml
name: Project Board to Issue Sync

on:
  projects_v2_item:
    types: [edited]

concurrency:
  group: project-sync-${{ github.event.projects_v2_item.node_id }}
  cancel-in-progress: false

jobs:
  sync-status:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
      id-token: write

    steps:
      - uses: actions/checkout@v4

      - name: Sync Project Status to Issue
        uses: anthropics/claude-code-action@v1
        env:
          GH_TOKEN: ${{ secrets.PROJECTS_TOKEN }}
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          prompt: |
            # Project Board to Issue Sync

            Synchronize project board status changes to issue.

            ## Project Event
            **Item ID**: ${{ github.event.projects_v2_item.node_id }}
            **Changed By**: @${{ github.event.sender.login }}

            ## Task
            1. Get issue number from project item
            2. Get new status from project column
            3. Update issue labels and state
            4. Post status comment

            ## Status to Label Mapping
            - "To triage" → `status: triage`
            - "Backlog" → `status: backlog`
            - "Ready" → `status: ready`
            - "In Progress" → `status: in-progress`
            - "In Review" → `status: in-review`
            - "Done" → `status: done` + close issue

            ## Steps

            ### 1. Get issue from project item
            ```bash
            gh api graphql -f query='...' # Get issue number
            ```

            ### 2. Get project status
            ```bash
            gh api graphql -f query='...' # Get status field value
            ```

            ### 3. Remove old status labels
            ```bash
            for label in "status: triage" "status: backlog" "status: ready" "status: in-progress" "status: in-review" "status: done"; do
              gh issue edit ISSUE_NUM --remove-label "$label" 2>/dev/null || true
            done
            ```

            ### 4. Add new status label
            ```bash
            gh issue edit ISSUE_NUM --add-label "status: [new-status]"
            ```

            ### 5. Close/reopen if needed
            ```bash
            if [ "$STATUS" = "Done" ]; then
              gh issue close ISSUE_NUM --reason completed
            else
              gh issue reopen ISSUE_NUM
            fi
            ```

            ### 6. Post comment
            ```bash
            gh issue comment ISSUE_NUM --body "## 📊 Status Update

            **Status**: [new status]

            Moved on project board by @${{ github.event.sender.login }}

            *Automated sync*"
            ```

            ## Execute
            Sync the status now.

          claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh api:*)"'
```

### Phase 3: Branch Protection (10 min)

#### Step 3.1: Create Protection Config

Create `.github/branch-protection-config.json`:

```json
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
```

#### Step 3.2: Apply Protection

```bash
# Replace OWNER and REPO
gh api repos/OWNER/REPO/branches/main/protection \
  --method PUT \
  --input .github/branch-protection-config.json
```

### Phase 4: Documentation (15 min)

Create these documentation files in `.github/`:

1. **SECURITY.md** - Security model and access controls
2. **WORKFLOWS.md** - Workflow usage guide
3. **ISSUE_AUTO_TRIAGE.md** - Triage system documentation
4. **PLAN_TO_ISSUES.md** - Plan automation guide
5. **STATUS_SYNC.md** - Status synchronization guide
6. **PROJECT_INTEGRATION_SETUP.md** - Token setup instructions

---

## Workflow Specifications

### Workflow Naming Convention

```
[purpose]-[scope].yml

Examples:
- claude.yml (main Claude integration)
- claude-code-review.yml (PR reviews)
- issue-triage.yml (issue classification)
- plan-to-issues.yml (plan conversion)
- issue-to-project-sync.yml (issue → board)
- project-to-issue-sync.yml (board → issue)
```

### Trigger Patterns

```yaml
# On-demand (comment-based)
on:
  issue_comment:
    types: [created]

# Automatic (event-based)
on:
  pull_request:
    types: [opened, synchronize]

# Conditional (filtered)
on:
  issues:
    types: [labeled]
jobs:
  job:
    if: github.event.label.name == 'plan'
```

### Concurrency Control

```yaml
# Prevent duplicate runs
concurrency:
  group: workflow-${{ github.event.issue.number }}
  cancel-in-progress: false  # false = queue, true = cancel

# Per-resource locking
concurrency:
  group: sync-${{ github.event.projects_v2_item.node_id }}
  cancel-in-progress: false
```

### Permission Patterns

```yaml
# Minimal (read-only)
permissions:
  contents: read
  issues: read

# Standard (read + write)
permissions:
  contents: read
  issues: write
  pull-requests: write
  id-token: write  # Required for Claude Code OIDC

# Admin (full access)
permissions:
  contents: write
  issues: write
  pull-requests: write
  id-token: write
  actions: write
```

### Tool Allowlists

```yaml
# GitHub CLI only
claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh pr:*)"'

# Project board access
claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh project:*),Bash(gh api:*)"'

# Development tools
claude_args: '--allowed-tools "Bash(gh:*),Bash(npm:*),Bash(git:*)"'

# Search capabilities
claude_args: '--allowed-tools "Bash(gh search:*),Bash(gh issue:*)"'
```

---

## Security Model

### Access Control Layers

#### Layer 1: GitHub Permissions
```yaml
# Only team members trigger workflows
if: contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
```

#### Layer 2: Tool Restrictions
```yaml
# Allowlist specific commands only
claude_args: '--allowed-tools "Bash(gh issue:*)"'
# Blocks: git push, rm -rf, curl, etc.
```

#### Layer 3: Token Scoping
```yaml
# PROJECTS_TOKEN: repo + project only (no admin access)
# CLAUDE_CODE_OAUTH_TOKEN: Claude-specific operations only
```

#### Layer 4: Branch Protection
```json
{
  "enforce_admins": true,
  "required_status_checks": {"contexts": ["claude-review"]},
  "allow_force_pushes": false
}
```

### Threat Model

| Threat | Mitigation |
|--------|-----------|
| Malicious PR | Required claude-review check + team approval |
| Token exposure | Workflow-level secrets, no logging |
| Privilege escalation | Minimal permissions per workflow |
| Workflow manipulation | Branch protection prevents workflow changes in PRs |
| External contributor abuse | Author association checks on all triggers |

---

## Testing & Validation

### Pre-Deployment Checklist

```bash
# 1. Verify secrets exist
gh secret list

# Expected output:
# CLAUDE_CODE_OAUTH_TOKEN
# PROJECTS_TOKEN

# 2. Validate workflow syntax
for file in .github/workflows/*.yml; do
  yamllint "$file" || echo "❌ $file has syntax errors"
done

# 3. Check label creation
gh label list | grep -E "status:|P[0-3]|plan|subtask"

# 4. Verify project board
# Visit: https://github.com/users/USERNAME/projects/NUMBER
# Confirm columns: To triage, Backlog, Ready, In Progress, In Review, Done

# 5. Test branch protection
git push origin main  # Should fail (requires PR)
```

### Testing Scenarios

#### Test 1: Issue Triage
```bash
# Create test issue
gh issue create \
  --title "Test: Issue Triage System" \
  --body "This is a test bug report with insufficient details."

# Expected:
# - Workflow runs within 30 seconds
# - Issue labeled (type + priority)
# - Issue added to project board
# - Triage comment posted
# - Verify: gh run list --workflow=issue-triage.yml
```

#### Test 2: Plan-to-Issues
```bash
# Create plan issue
gh issue create \
  --title "Plan: Test Feature Implementation" \
  --label "plan" \
  --body "## Tasks
- [ ] Task 1: Design UI
- [ ] Task 2: Implement backend
- [ ] Task 3: Write tests"

# Expected:
# - 3 subtask issues created
# - All linked to parent
# - All added to project board
# - Summary comment on parent
```

#### Test 3: Status Sync
```bash
# Create issue
gh issue create --title "Test: Status Sync" --body "Testing bidirectional sync"

# Test A: Issue → Board
gh issue edit [NUM] --add-label "status: ready"
# Expected: Issue moves to "Ready" column on board

# Test B: Board → Issue
# Manually move issue to "In Progress" on project board
# Expected: status: in-progress label added, status: ready removed
```

#### Test 4: PR Review
```bash
# Create test branch and PR
git checkout -b test-pr-review
echo "test" > test.txt
git add test.txt
git commit -m "test: PR review"
git push -u origin test-pr-review
gh pr create --title "Test: Claude Code Review" --body "Testing automatic review"

# Expected:
# - claude-review workflow runs
# - Review comment posted within 2-3 minutes
# - Status check appears (required for merge)
```

### Monitoring & Debugging

```bash
# View recent workflow runs
gh run list --limit 10

# Check specific workflow
gh run list --workflow=issue-triage.yml --limit 5

# View run logs
gh run view RUN_ID --log

# Check for failures
gh run list --status failure --limit 10

# Monitor in real-time
watch -n 5 'gh run list --limit 5'
```

---

## Troubleshooting

### Common Issues

#### Issue: Workflow Not Triggering

**Symptoms**: Created issue but no triage workflow ran

**Diagnosis**:
```bash
# Check if workflow exists and is active
gh workflow list

# Check for syntax errors
yamllint .github/workflows/issue-triage.yml

# View recent runs (might be skipped)
gh run list --workflow=issue-triage.yml --limit 5
```

**Solutions**:
1. Verify workflow file is on main branch (not just local)
2. Check `if` conditions aren't filtering it out
3. Wait 5-10 minutes for GitHub to index new workflows
4. Check GitHub Actions is enabled: Settings → Actions → General

---

#### Issue: "Secret not found" Error

**Symptoms**: Workflow fails with "CLAUDE_CODE_OAUTH_TOKEN not found"

**Diagnosis**:
```bash
# List secrets
gh secret list

# Check workflow file references
grep -r "CLAUDE_CODE_OAUTH_TOKEN" .github/workflows/
```

**Solutions**:
1. Add secret: Repository → Settings → Secrets → Actions
2. Verify exact name match (case-sensitive)
3. Re-save secret if it exists (might be expired)
4. Check you're in correct repository

---

#### Issue: Project Board Sync Failing

**Symptoms**: "Could not resolve to a ProjectV2" or "403 Forbidden"

**Diagnosis**:
```bash
# Check if PROJECTS_TOKEN exists
gh secret list | grep PROJECTS_TOKEN

# Verify project number
# Visit: https://github.com/users/USERNAME/projects
# Check URL: .../projects/NUMBER
```

**Solutions**:
1. Verify PROJECTS_TOKEN has `repo` + `project` scopes
2. Update project number in workflows (search for `project item-add NUMBER`)
3. Regenerate token if expired
4. Ensure project is accessible to token owner

---

#### Issue: Infinite Sync Loops

**Symptoms**: Dozens of rapid workflow runs, duplicate comments

**Diagnosis**:
```bash
# Check for rapid successive runs
gh run list --workflow=issue-to-project-sync.yml --limit 20
gh run list --workflow=project-to-issue-sync.yml --limit 20

# Look for timing pattern (runs within seconds of each other)
```

**Solutions**:
1. Verify concurrency controls exist in workflow YAML
2. Check workflows aren't modifying their own triggers:
   - `issue-to-project-sync.yml` should ONLY modify project board
   - `project-to-issue-sync.yml` should ONLY modify issues
3. Add conditional checks to skip if already synced
4. Increase concurrency group specificity

---

#### Issue: Claude Review Takes Too Long

**Symptoms**: PR review takes >5 minutes or times out

**Diagnosis**:
```bash
# Check workflow run logs
gh run view RUN_ID --log

# Look for:
# - Large PR size (many files)
# - Network timeouts
# - API rate limits
```

**Solutions**:
1. Split large PRs into smaller ones (<500 lines)
2. Increase workflow timeout (default: 10 min)
3. Check GitHub API rate limits: `gh api rate_limit`
4. Review allowed-tools list (too broad = slow)

---

#### Issue: Labels Not Syncing

**Symptoms**: Move issue on board but label doesn't update

**Diagnosis**:
```bash
# Check workflow triggered
gh run list --workflow=project-to-issue-sync.yml --limit 5

# Check if workflow exists
gh workflow list | grep project-to-issue

# Verify label names match exactly
gh label list | grep "status:"
```

**Solutions**:
1. Verify status label names match exactly (case-sensitive)
2. Check project column names match mapping:
   - "To triage" → `status: triage`
   - "In Progress" → `status: in-progress` (hyphen, not space)
3. Manually trigger by removing/re-adding status label
4. Check workflow logs for GraphQL errors

---

## Customization Guide

### Adapting for Your Project

#### 1. Update Project Configuration

Find and replace these values throughout all workflow files:

```bash
# Project owner username
OLD: alirezarezvani
NEW: YOUR_USERNAME

# Project number
OLD: 7
NEW: YOUR_PROJECT_NUMBER

# Repository name
OLD: claude-code-skill-factory
NEW: YOUR_REPO_NAME

# Project URL
OLD: https://github.com/users/alirezarezvani/projects/7
NEW: https://github.com/users/YOUR_USERNAME/projects/YOUR_NUMBER
```

#### 2. Customize Status Columns

If your project board has different columns:

**In `issue-to-project-sync.yml`**:
```yaml
# Update label to status mapping
- `status: blocked` → "Blocked"
- `status: testing` → "Testing"
```

**In `project-to-issue-sync.yml`**:
```yaml
# Update status to label mapping
- "Blocked" → `status: blocked`
- "Testing" → `status: testing`
```

**Create custom labels**:
```bash
gh label create "status: blocked" --color "d73a4a" --description "Blocked column"
gh label create "status: testing" --color "1d76db" --description "Testing column"
```

#### 3. Modify Issue Types

Add custom issue types for your domain:

```bash
# Create domain-specific labels
gh label create "ui-bug" --color "fc8181" --description "UI/UX bug"
gh label create "api-bug" --color "f56565" --description "API/Backend bug"
gh label create "infrastructure" --color "4299e1" --description "Infrastructure task"
```

Update `issue-triage.yml` classification list.

#### 4. Adjust Triage Prompt

Customize the triage intelligence in `issue-triage.yml`:

```yaml
prompt: |
  # Add custom classification rules

  ## Domain-Specific Classification
  If issue mentions "UI" or "frontend" → add "ui-bug"
  If issue mentions "API" or "backend" → add "api-bug"
  If issue mentions "deployment" → add "infrastructure"

  ## Custom Priority Rules
  - Security issues → Always P0
  - User-facing bugs → P0 or P1
  - Internal tools → P2 or P3
```

#### 5. Team-Specific Workflows

Add team collaboration workflows:

```yaml
# Auto-assign based on labels
- name: Auto-assign
  if: contains(github.event.issue.labels.*.name, 'ui-bug')
  run: gh issue edit ${{ github.event.issue.number }} --add-assignee @ui-team-lead

# Notify team on high-priority
- name: Notify team
  if: contains(github.event.issue.labels.*.name, 'P0')
  run: |
    gh issue comment ${{ github.event.issue.number }} --body "@team Critical issue requires immediate attention"
```

---

## Best Practices

### Workflow Design

✅ **DO**:
- Use concurrency controls to prevent race conditions
- Implement minimal permissions (read when possible)
- Add error handling and graceful failures
- Use environment variables for configuration
- Document workflow purpose and triggers
- Test workflows in branches before merging to main

❌ **DON'T**:
- Give workflows write access they don't need
- Create circular dependencies (sync loops)
- Hard-code values (use variables/secrets)
- Skip input validation
- Ignore failed workflow runs
- Modify workflows directly on main branch

### Issue Management

✅ **DO**:
- Use status labels consistently
- Keep issue descriptions complete and clear
- Link related issues and PRs
- Update issue status as work progresses
- Close issues when truly done

❌ **DON'T**:
- Mix multiple problems in one issue
- Leave stale issues open indefinitely
- Skip the plan label on planning issues
- Manually sync labels (let automation handle it)
- Create duplicate labels with similar names

### Project Board

✅ **DO**:
- Move issues as status changes
- Use one primary status column per issue
- Archive completed items regularly
- Review board in team meetings
- Keep column names simple and clear

❌ **DON'T**:
- Have too many columns (6-8 max)
- Use confusing column names
- Skip columns (e.g., Backlog → Done)
- Manually add status labels (automation handles it)
- Create multiple project boards for same work

---

## Maintenance

### Regular Tasks

**Weekly**:
```bash
# Review failed workflow runs
gh run list --status failure --limit 20

# Check secret expiration (if applicable)
gh secret list

# Audit label usage
gh issue list --json labels --jq '.[] | .labels[].name' | sort | uniq -c | sort -rn
```

**Monthly**:
```bash
# Update Claude Code action version
# Check: https://github.com/anthropics/claude-code-action/releases

# Review and clean up stale labels
gh label list

# Analyze workflow performance
gh api /repos/OWNER/REPO/actions/runs --jq '.workflow_runs[] | {name: .name, duration: .run_duration_ms}'

# Update documentation for any workflow changes
```

**Quarterly**:
```bash
# Regenerate PROJECTS_TOKEN (security best practice)
# 1. Create new token with same scopes
# 2. Update repository secret
# 3. Delete old token

# Review and update branch protection rules
gh api repos/OWNER/REPO/branches/main/protection

# Audit team access and permissions
gh api repos/OWNER/REPO/collaborators
```

### Backup & Recovery

```bash
# Backup workflow files
tar -czf workflows-backup-$(date +%Y%m%d).tar.gz .github/workflows/

# Backup labels
gh label list --json name,description,color > labels-backup-$(date +%Y%m%d).json

# Backup branch protection config
gh api repos/OWNER/REPO/branches/main/protection > branch-protection-backup-$(date +%Y%m%d).json

# Export project board (manual)
# Visit project board → ... → Export to CSV
```

---

## Version History

**1.0.0** (2025-10-24)
- Initial release
- 6 core workflows
- Bidirectional status sync
- Plan-to-issues automation
- Comprehensive documentation

---

## Support & Contributing

### Getting Help

1. **Check Documentation**:
   - This master prompt
   - Individual workflow `.md` files in `.github/`
   - GitHub Actions documentation

2. **Debug Workflow Runs**:
   ```bash
   gh run list --workflow=WORKFLOW_NAME --limit 5
   gh run view RUN_ID --log
   ```

3. **Community Resources**:
   - Claude Code documentation: https://docs.claude.com/claude-code
   - GitHub Actions docs: https://docs.github.com/actions
   - GitHub Projects docs: https://docs.github.com/issues/planning-and-tracking-with-projects

### Reporting Issues

When reporting workflow issues, include:
- Workflow name and file
- Full error message
- Workflow run URL
- Steps to reproduce
- Expected vs actual behavior
- Relevant configuration (redact secrets!)

---

## License & Credits

This workflow automation system was designed for maximum reusability across projects.

**Components**:
- GitHub Actions (GitHub)
- Claude Code Action (Anthropic)
- GitHub CLI (`gh` command)

**Implementation**: Claude Code (Anthropic)
**Date**: 2025-10-24
**Version**: 1.0.0

---

## Quick Start Checklist

Use this checklist when implementing in a new project:

- [ ] Create CLAUDE_CODE_OAUTH_TOKEN secret
- [ ] Create PROJECTS_TOKEN secret (repo + project scopes)
- [ ] Create project board with 6 columns
- [ ] Note project number from URL
- [ ] Create all status labels (6)
- [ ] Create all type labels (8)
- [ ] Create all priority labels (4)
- [ ] Create all plan labels (3)
- [ ] Copy all 6 workflow files to `.github/workflows/`
- [ ] Update project number in workflows (find/replace)
- [ ] Update owner username in workflows (find/replace)
- [ ] Update repository name in workflows (find/replace)
- [ ] Apply branch protection rules
- [ ] Create documentation files in `.github/`
- [ ] Test issue triage (create test issue)
- [ ] Test plan-to-issues (create plan issue)
- [ ] Test status sync (add status label)
- [ ] Test PR review (create test PR)
- [ ] Verify project board sync works both ways
- [ ] Review workflow runs for errors
- [ ] Archive/delete test issues
- [ ] Update team on new workflows
- [ ] Schedule weekly workflow review

---

**End of Master Prompt**

Save this file and reference it whenever setting up GitHub workflow automation in a new project. Update the version number and changelog as you make improvements.
