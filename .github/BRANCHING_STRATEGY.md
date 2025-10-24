# Git Branching Strategy & Workflow

**Version**: 1.0.0
**Last Updated**: 2025-10-24
**Status**: ✅ Production Standard

Comprehensive branching strategy for the Claude Code Skills & Agents Factory project, optimized for solo development with Claude Code agents and automated workflows.

---

## Table of Contents

- [Overview](#overview)
- [Branch Types & Naming](#branch-types--naming)
- [Workflow Process](#workflow-process)
- [Branch Lifecycle](#branch-lifecycle)
- [Commit Message Standards](#commit-message-standards)
- [Pull Request Standards](#pull-request-standards)
- [Integration with Automation](#integration-with-automation)
- [Examples](#examples)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## Overview

### Philosophy

This branching strategy is designed for:
- **Solo developer + AI agents**: Streamlined for one human developer working with Claude Code
- **Quality automation**: Leverages automatic code review and issue tracking
- **Fast iteration**: Short-lived feature branches with quick merges
- **Clean history**: Meaningful commits that tell the story of changes

### Key Principles

1. **Main is sacred** - Always production-ready, protected by required reviews
2. **One issue = One branch** - Clear scope, easy to review and track
3. **Short-lived branches** - Merge within 1-3 days maximum
4. **Automation-first** - Let workflows handle triage, review, and status sync
5. **Conventional commits** - Clear, searchable, and release-note friendly

---

## Branch Types & Naming

### Naming Convention

**Format**: `<type>/<issue-number>-<short-description>`

All branch names use:
- **Lowercase letters only**
- **Hyphens** for word separation (not underscores or spaces)
- **Issue number** from GitHub (links branch to issue automatically)
- **Short description** that fits on one line

### Branch Types

#### 1. Feature Branches (`feat/`)

**Purpose**: New capabilities, enhancements, or significant additions

**Naming**:
```
feat/57-create-wiki-home-page
feat/63-add-serverless-skill
feat/71-implement-batch-generator
```

**When to use**:
- Adding new skills or agents
- Creating new templates
- Implementing new automation workflows
- Adding major documentation sections

**Lifespan**: 1-3 days

---

#### 2. Fix Branches (`fix/`)

**Purpose**: Bug fixes, corrections, and problem resolution

**Naming**:
```
fix/123-correct-readme-typo
fix/98-repair-broken-link
fix/145-resolve-workflow-error
```

**When to use**:
- Fixing bugs in skills or agents
- Correcting errors in documentation
- Resolving workflow failures
- Fixing broken links or references

**Lifespan**: Hours to 1 day

---

#### 3. Docs Branches (`docs/`)

**Purpose**: Documentation changes, updates, and improvements

**Naming**:
```
docs/56-add-branching-strategy
docs/82-update-installation-guide
docs/104-consolidate-github-docs
```

**When to use**:
- Adding new documentation files
- Updating README or CLAUDE.md
- Improving examples or guides
- Consolidating or reorganizing docs

**Lifespan**: 1-2 days

---

#### 4. Refactor Branches (`refactor/`)

**Purpose**: Code restructuring without changing functionality

**Naming**:
```
refactor/67-simplify-ratio-calculator
refactor/89-reorganize-skill-structure
refactor/112-extract-validation-logic
```

**When to use**:
- Improving code structure
- Extracting reusable components
- Reorganizing file structure
- Optimizing implementations

**Lifespan**: 1-2 days

---

#### 5. Test Branches (`test/`)

**Purpose**: Adding or improving tests

**Naming**:
```
test/91-add-dcf-model-tests
test/128-validate-skill-generation
test/156-integration-test-suite
```

**When to use**:
- Adding new test files
- Improving test coverage
- Creating validation scripts
- Setting up test automation

**Lifespan**: 1-2 days

---

#### 6. Chore Branches (`chore/`)

**Purpose**: Maintenance tasks, dependencies, configuration

**Naming**:
```
chore/44-update-dependencies
chore/77-cleanup-old-files
chore/103-configure-eslint
```

**When to use**:
- Updating dependencies
- Cleaning up unused files
- Configuring tools
- Routine maintenance

**Lifespan**: Hours to 1 day

---

#### 7. Hotfix Branches (`hotfix/`)

**Purpose**: Critical urgent fixes for production issues

**Naming**:
```
hotfix/emergency-security-patch
hotfix/critical-workflow-failure
hotfix/data-loss-prevention
```

**When to use**:
- Security vulnerabilities
- Critical bugs blocking all users
- Data integrity issues
- Urgent production problems

**Lifespan**: Hours (immediate priority)

**Special rules**:
- Can be created from `main` and merged immediately
- May skip normal review if truly critical
- Always document reason for emergency merge

---

## Workflow Process

### Complete Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    1. CREATE GITHUB ISSUE                        │
│  - Use issue templates or create manually                       │
│  - Auto-triage workflow labels it (bug/feature/docs + P0-P3)   │
│  - Issue auto-added to project board in "To triage" column     │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              2. CREATE BRANCH FROM MAIN                          │
│  git checkout main                                               │
│  git pull origin main                                            │
│  git checkout -b feat/123-add-new-skill                         │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              3. UPDATE ISSUE STATUS (Optional)                   │
│  gh issue edit 123 --add-label "status: in-progress"           │
│  → Issue-to-Project sync moves to "In Progress" on board       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                 4. IMPLEMENT CHANGES                             │
│  - Make your code/doc changes                                   │
│  - Test locally if applicable                                   │
│  - Follow coding standards from CLAUDE.md                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              5. COMMIT WITH PROPER MESSAGE                       │
│  git add .                                                       │
│  git commit -m "feat(skills): add serverless architecture skill │
│                                                                  │
│  Implements comprehensive AWS serverless skill with Lambda,     │
│  API Gateway, and DynamoDB patterns.                            │
│                                                                  │
│  Closes #123"                                                   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              6. PUSH BRANCH TO ORIGIN                            │
│  git push -u origin feat/123-add-new-skill                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              7. CREATE PULL REQUEST                              │
│  gh pr create --title "feat: Add serverless architecture skill" │
│              --body "Closes #123"                               │
│  → Claude Code Review workflow triggers automatically           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              8. WAIT FOR CLAUDE REVIEW                           │
│  - Claude reviews code automatically (2-3 minutes)              │
│  - Review posted as PR comment                                  │
│  - Status check: claude-review (pass/fail)                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              9. ADDRESS FEEDBACK (if needed)                     │
│  - Read Claude's review comments                                │
│  - Make requested changes                                       │
│  - Commit and push updates                                      │
│  - Claude re-reviews automatically                              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              10. UPDATE ISSUE STATUS                             │
│  gh issue edit 123 --add-label "status: in-review"             │
│  → Auto-sync moves issue to "In Review" on project board       │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              11. MERGE PULL REQUEST                              │
│  - Ensure claude-review check passes ✅                         │
│  - Ensure branch is up-to-date with main                        │
│  - Click "Merge pull request" (or use gh pr merge)             │
│  - Delete branch automatically after merge                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              12. AUTO-CLOSE ISSUE                                │
│  - PR merge closes issue automatically (if "Closes #123")      │
│  - Issue moves to "Done" on project board                       │
│  - Label updated to "status: done"                             │
└─────────────────────────────────────────────────────────────────┘
```

---

### Quick Command Reference

```bash
# Start new work on issue #123
git checkout main
git pull origin main
git checkout -b feat/123-short-description
gh issue edit 123 --add-label "status: in-progress"

# Make changes, then commit
git add .
git commit -m "feat(scope): description

Detailed explanation if needed.

Closes #123"

# Push and create PR
git push -u origin feat/123-short-description
gh pr create --fill

# After review passes, merge
gh pr merge --squash --delete-branch

# Clean up local branch
git checkout main
git pull origin main
git branch -d feat/123-short-description
```

---

## Branch Lifecycle

### Creation

**When to create a branch**:
- GitHub issue exists for the work
- Issue has been triaged and labeled
- Scope is clear and well-defined
- You're ready to start implementation

**How to create**:
```bash
# Always branch from latest main
git checkout main
git pull origin main
git checkout -b <type>/<issue>-<description>
```

**Best practices**:
- ✅ Create branch AFTER issue is created
- ✅ Include issue number in branch name
- ✅ Use descriptive but concise name
- ✅ Verify you're on latest main first
- ❌ Don't create branch before issue exists
- ❌ Don't reuse old branches for new work

---

### Active Development

**How long branches should live**:
- **Documentation changes**: Hours to 1 day
- **Bug fixes**: Hours to 1 day
- **Small features**: 1-2 days
- **Medium features**: 2-3 days
- **Large features**: Break into multiple issues/branches

**Keeping branch updated**:
```bash
# If main has advanced while you're working
git checkout main
git pull origin main
git checkout feat/123-your-branch
git rebase main  # Preferred: clean linear history

# OR if you prefer merge commits
git merge main
```

**When to rebase vs merge**:
- **Use rebase** (preferred): Clean history, feature branch has few commits
- **Use merge**: Branch has many commits, preserving timeline is important
- **Rule of thumb**: If unsure, use rebase for cleaner history

---

### Review Stage

**Moving to review**:
```bash
# Update issue status
gh issue edit 123 --add-label "status: in-review"

# Ensure branch is up-to-date
git checkout main
git pull origin main
git checkout feat/123-your-branch
git rebase main
git push --force-with-lease  # Safe force push after rebase
```

**During review**:
- Respond to Claude's automated review comments
- Make requested changes in new commits (easier to review)
- Push updates trigger automatic re-review
- Keep commits logical and atomic

---

### Merge & Deletion

**Ready to merge when**:
- ✅ `claude-review` status check passes
- ✅ Branch is up-to-date with main
- ✅ All review feedback addressed
- ✅ Commits follow message standards
- ✅ No merge conflicts

**Merge options**:

**Option 1: Squash Merge** (recommended for most features)
```bash
gh pr merge --squash --delete-branch
```
- Combines all commits into one
- Clean main branch history
- Loses individual commit details
- **Use for**: Features with many small commits

**Option 2: Merge Commit** (for significant features)
```bash
gh pr merge --merge --delete-branch
```
- Preserves all commits
- Creates merge commit
- Full history visible
- **Use for**: Important features with meaningful commit progression

**Option 3: Rebase Merge** (for single commits)
```bash
gh pr merge --rebase --delete-branch
```
- Replays commits onto main
- No merge commit
- Linear history
- **Use for**: Single-commit branches or already rebased clean history

**After merge**:
```bash
# Clean up local branch
git checkout main
git pull origin main
git branch -d feat/123-your-branch

# Verify issue closed and moved to "Done"
gh issue view 123
```

---

## Commit Message Standards

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type Prefixes

**Required types** (use these exactly):

| Type | Purpose | Example |
|------|---------|---------|
| `feat` | New feature or capability | `feat(skills): add AWS serverless skill` |
| `fix` | Bug fix | `fix(workflows): correct project sync logic` |
| `docs` | Documentation changes | `docs(readme): update installation steps` |
| `refactor` | Code restructuring | `refactor(agents): simplify prompt generation` |
| `test` | Adding/updating tests | `test(skills): add DCF model validation` |
| `chore` | Maintenance tasks | `chore(deps): update dependencies` |
| `style` | Code formatting only | `style(python): format with black` |
| `perf` | Performance improvements | `perf(dcf): optimize calculation loops` |

### Scope Guidelines

**Common scopes**:
- `skills` - Changes to skill examples
- `agents` - Changes to agent examples
- `templates` - Changes to generation templates
- `workflows` - GitHub workflow changes
- `docs` - Documentation files
- `examples` - Example code or demonstrations

**Scope rules**:
- Use lowercase
- Be specific but concise
- Optional but recommended
- Omit only if change affects entire project

### Subject Line

**Rules**:
- Start with lowercase verb (imperative mood)
- No period at end
- Maximum 50 characters
- Be specific and descriptive

**Good examples**:
```
feat(skills): add content trend researcher skill
fix(workflows): resolve infinite sync loop
docs(contributing): add PR guidelines
refactor(templates): extract validation logic
```

**Bad examples**:
```
Added new skill                    # Missing type and scope
fix: Fixed a bug in the workflow.  # Period at end, vague
FEAT(SKILLS): New AWS skill        # Wrong capitalization
feat: changes                      # Too vague
```

### Body

**When to include**:
- Change is non-trivial
- Context or reasoning needed
- Multiple related changes
- Breaking changes

**Format**:
- Wrap at 72 characters
- Separate from subject with blank line
- Explain WHAT and WHY, not HOW
- Use bullet points for multiple items

**Example**:
```
feat(skills): add psychology advisor skill

Implements comprehensive mental wellness skill with CBT techniques,
mindfulness exercises, and stress management tools.

Key features:
- 10 cognitive distortion types with reframing
- 4 breathing techniques (Box, 4-7-8, etc.)
- RAIN mindfulness method
- Stress assessment and coping strategies

Closes #87
```

### Footer

**Required footers**:

**Issue references**:
```
Closes #123
Fixes #456
Resolves #789
Related to #101
```

**Breaking changes**:
```
BREAKING CHANGE: Template format changed from XML to YAML
```

**Co-authors** (when working with Claude):
```
Co-authored-by: Claude <noreply@anthropic.com>
```

### Complete Examples

**Simple documentation fix**:
```
docs(readme): fix broken link to skill template

Closes #234
```

**Feature with context**:
```
feat(workflows): add bidirectional status sync

Implements automatic synchronization between GitHub issues and
project board columns in both directions.

Changes:
- Issue label changes → Board column moves
- Board column moves → Issue label updates
- Prevents infinite sync loops with concurrency controls
- Posts status update comments for visibility

Closes #49
```

**Bug fix with explanation**:
```
fix(workflows): prevent infinite loop in project sync

Added concurrency controls to ensure only one sync operation
runs per issue at a time. Previous implementation could trigger
cascading updates when both workflows ran simultaneously.

Fixes #156
```

**Refactoring with multiple files**:
```
refactor(skills): consolidate validation logic

Extracted common validation patterns from multiple skills into
shared validation module. No functional changes.

Files affected:
- aws-solution-architect/architecture_designer.py
- content-trend-researcher/trend_analyzer.py
- ms365-tenant-manager/tenant_setup.py

Related to #203
```

---

## Pull Request Standards

### PR Title Format

**Format**: Same as commit message subject line

```
<type>(<scope>): <description>
```

**Examples**:
```
feat(skills): add serverless architecture skill
fix(workflows): resolve project sync timeout
docs(contributing): add branching strategy guide
```

### PR Description Template

Use this template for all PRs:

```markdown
## Summary

[2-3 sentence summary of what this PR does and why]

## Changes

- [ ] Change 1 with brief explanation
- [ ] Change 2 with brief explanation
- [ ] Change 3 with brief explanation

## Issue Reference

Closes #123

## Type of Change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Documentation update
- [ ] Refactoring (no functional changes)
- [ ] Breaking change (fix or feature that breaks existing functionality)

## Testing

[Describe how you tested these changes]

- [ ] Manually tested feature X
- [ ] Verified workflow Y runs successfully
- [ ] Validated documentation renders correctly
- [ ] Tested on [environment/platform]

## Screenshots (if applicable)

[Add screenshots for UI changes or documentation updates]

## Additional Context

[Any additional information reviewers should know]

## Checklist

- [ ] Code follows project style guidelines
- [ ] Documentation updated (README, CLAUDE.md if applicable)
- [ ] Commit messages follow conventions
- [ ] No breaking changes (or documented if necessary)
- [ ] All conversations resolved
```

### Creating a PR

**Option 1: GitHub CLI (recommended)**:
```bash
# Auto-fill from commits
gh pr create --fill

# Or specify details
gh pr create \
  --title "feat(skills): add new skill template" \
  --body "Closes #123"
```

**Option 2: GitHub Web UI**:
1. Push branch to origin
2. Navigate to repository on GitHub
3. Click "Compare & pull request"
4. Fill in title and description
5. Click "Create pull request"

### PR Review Process

**Automatic review** (always happens):
1. PR created/updated
2. `claude-code-review` workflow triggers
3. Claude analyzes all changes
4. Review comment posted (2-3 minutes)
5. Status check updates (pass/fail)

**What Claude reviews**:
- Code quality and best practices
- Potential bugs or issues
- Security concerns
- Performance considerations
- Documentation completeness
- Test coverage

**Responding to review**:
```bash
# Make requested changes
git add .
git commit -m "fix: address review feedback"
git push

# Claude automatically re-reviews updated PR
```

### Merge Requirements

**Branch protection rules enforce**:
- ✅ Pull request required (no direct pushes to main)
- ✅ `claude-review` status check passes
- ✅ Branch up-to-date with main
- ✅ All conversations resolved

**Before merging**:
```bash
# Verify status checks
gh pr checks

# Ensure up-to-date with main
git checkout main
git pull origin main
git checkout feat/123-your-branch
git rebase main
git push --force-with-lease

# Merge when ready
gh pr merge --squash --delete-branch
```

---

## Integration with Automation

### How Branching Integrates with Workflows

```
┌─────────────────────────────────────────────────────────────┐
│                    GITHUB ISSUE CREATED                      │
│                                                             │
│  → issue-triage.yml triggers                                │
│  → Claude analyzes and labels (bug/feature + P0-P3)        │
│  → Issue added to project board ("To triage")              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    BRANCH CREATED                            │
│                                                             │
│  git checkout -b feat/123-description                       │
│  gh issue edit 123 --add-label "status: in-progress"       │
│                                                             │
│  → issue-to-project-sync.yml triggers                       │
│  → Issue moves to "In Progress" on board                    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    PULL REQUEST CREATED                      │
│                                                             │
│  gh pr create --fill                                        │
│                                                             │
│  → claude-code-review.yml triggers                          │
│  → Claude reviews code automatically                        │
│  → Review posted as comment                                 │
│  → Status check updated (pass/fail)                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    PR REVIEW COMPLETED                       │
│                                                             │
│  gh issue edit 123 --add-label "status: in-review"         │
│                                                             │
│  → issue-to-project-sync.yml triggers                       │
│  → Issue moves to "In Review" on board                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    PR MERGED                                 │
│                                                             │
│  gh pr merge --squash --delete-branch                       │
│                                                             │
│  → Issue auto-closed (if "Closes #123" in PR)              │
│  → project-to-issue-sync.yml triggers                       │
│  → Issue moves to "Done" on board                           │
│  → Label updated to "status: done"                         │
└─────────────────────────────────────────────────────────────┘
```

### Plan-to-Issues Workflow

**For complex features requiring multiple branches**:

1. **Create plan issue**:
```bash
gh issue create \
  --title "Plan: User Authentication System" \
  --label "plan" \
  --body "## Tasks
- [ ] Design login UI components
- [ ] Implement JWT backend
- [ ] Add password reset flow
- [ ] Write integration tests
- [ ] Update documentation"
```

2. **Automation executes**:
- `plan-to-issues.yml` triggers
- Creates 5 child issues (one per task)
- Links all to parent issue
- Adds all to project board

3. **Work on subtasks**:
```bash
# For each subtask issue
git checkout -b feat/201-design-login-ui
# ... implement and PR ...
gh pr merge --squash --delete-branch

git checkout -b feat/202-implement-jwt-backend
# ... implement and PR ...
gh pr merge --squash --delete-branch
```

4. **Parent issue closes when all subtasks complete**

### Status Sync (Two-Way)

**Update via issue labels**:
```bash
gh issue edit 123 --add-label "status: in-progress"
# → Issue-to-Project sync moves issue on board
```

**Update via project board**:
```
Drag issue to "In Progress" column on board
# → Project-to-Issue sync adds "status: in-progress" label
```

Both methods keep issue and board perfectly synchronized.

---

## Examples

### Example 1: Simple Documentation Fix

**Scenario**: Fix typo in README.md

```bash
# 1. Create issue
gh issue create \
  --title "Fix typo in installation instructions" \
  --label "documentation,P3" \
  --body "README has 'pip instal' instead of 'pip install'"

# Issue #234 created and auto-triaged

# 2. Create branch
git checkout main
git pull origin main
git checkout -b docs/234-fix-installation-typo

# 3. Make change
# Edit README.md to fix typo

# 4. Commit
git add README.md
git commit -m "docs(readme): fix typo in installation command

Changed 'pip instal' to 'pip install'.

Closes #234"

# 5. Push and create PR
git push -u origin docs/234-fix-installation-typo
gh pr create --fill

# 6. Wait for Claude review (passes automatically)

# 7. Merge
gh pr merge --squash --delete-branch

# Issue #234 auto-closes and moves to "Done"
```

---

### Example 2: Feature Implementation

**Scenario**: Add new skill for AWS Lambda optimization

```bash
# 1. Create issue with plan label
gh issue create \
  --title "Plan: AWS Lambda Optimization Skill" \
  --label "plan,skill-request" \
  --body "## Goal
Create comprehensive skill for AWS Lambda performance optimization.

## Tasks
- [ ] Design skill structure and API
- [ ] Implement cost analyzer module
- [ ] Add performance profiling tools
- [ ] Create sample data and examples
- [ ] Write documentation and HOW_TO_USE
- [ ] Generate ZIP package"

# Issue #156 created
# plan-to-issues.yml creates 6 subtask issues: #157-162

# 2. Work on first subtask (#157)
git checkout -b feat/157-design-lambda-skill-structure

# 3. Update status
gh issue edit 157 --add-label "status: in-progress"

# 4. Implement
# Create SKILL.md with frontmatter and structure

# 5. Commit
git add generated-skills/lambda-optimizer/
git commit -m "feat(skills): design AWS Lambda optimization skill structure

Created initial SKILL.md with:
- YAML frontmatter
- Capability definitions
- Input/output specifications
- Usage examples

This is the foundation for the complete skill implementation.

Closes #157"

# 6. Push and PR
git push -u origin feat/157-design-lambda-skill-structure
gh pr create --fill

# 7. Claude reviews automatically

# 8. Address feedback if needed
# Make changes based on review
git add .
git commit -m "fix: address Claude review feedback"
git push

# 9. Update status
gh issue edit 157 --add-label "status: in-review"

# 10. Merge when approved
gh pr merge --squash --delete-branch

# 11. Repeat for remaining subtasks (#158-162)
# Each gets its own branch, PR, review, and merge

# 12. Parent issue #156 auto-closes when all subtasks done
```

---

### Example 3: Bug Fix with Testing

**Scenario**: Workflow timeout causing sync failures

```bash
# 1. Issue reported and auto-triaged as P1 bug
# Issue #189: "Project sync fails with timeout error"

# 2. Create branch
git checkout main
git pull origin main
git checkout -b fix/189-project-sync-timeout

# 3. Update status
gh issue edit 189 --add-label "status: in-progress"

# 4. Investigate and fix
# Edit .github/workflows/project-to-issue-sync.yml
# Increase timeout from 5 to 10 minutes
# Add retry logic for GraphQL queries

# 5. Test locally
# Trigger workflow manually to verify fix

# 6. Commit with detailed explanation
git add .github/workflows/
git commit -m "fix(workflows): resolve project sync timeout errors

Increased timeout from 5 to 10 minutes for large projects.
Added exponential backoff retry logic for GraphQL queries.

Testing:
- Manually triggered workflow 5 times
- All runs completed successfully
- Average duration: 3.2 minutes

Root cause: Large project boards (>100 issues) require more time
for GraphQL queries to complete.

Fixes #189"

# 7. Push and create PR
git push -u origin fix/189-project-sync-timeout
gh pr create --fill

# 8. Wait for Claude review
# Claude validates changes and posts approval

# 9. Update status
gh issue edit 189 --add-label "status: in-review"

# 10. Merge
gh pr merge --squash --delete-branch

# Issue #189 auto-closes
```

---

### Example 4: Hotfix for Critical Issue

**Scenario**: Security vulnerability in skill execution

```bash
# 1. Critical security issue discovered
# Create P0 issue immediately

gh issue create \
  --title "CRITICAL: Arbitrary code execution in skill loader" \
  --label "bug,P0" \
  --body "Security vulnerability allows untrusted code execution.

Impact: All users
Severity: Critical
Requires immediate fix."

# Issue #245 created and marked P0

# 2. Create hotfix branch
git checkout main
git pull origin main
git checkout -b hotfix/245-security-code-execution

# 3. Mark in progress
gh issue edit 245 --add-label "status: in-progress"

# 4. Implement fix immediately
# Sanitize input, add validation, restrict execution

# 5. Test thoroughly
# Run security audit, validate fix

# 6. Commit with security details
git add .
git commit -m "fix(security): prevent arbitrary code execution in skill loader

SECURITY FIX - Addresses critical vulnerability CVE-XXXX

Changes:
- Added input validation and sanitization
- Restricted execution to allowlist
- Implemented sandbox for skill code
- Added comprehensive security tests

Testing:
- Penetration tested attack vectors
- All security tests pass
- No regression in functionality

Fixes #245

BREAKING CHANGE: Skills must now declare required permissions"

# 7. Push and create urgent PR
git push -u origin hotfix/245-security-code-execution
gh pr create \
  --title "HOTFIX: Critical security fix for code execution" \
  --body "URGENT SECURITY FIX

Addresses critical vulnerability allowing arbitrary code execution.

Closes #245

cc @security-team"

# 8. Fast-track review
# Claude reviews immediately
# Manual security review if needed

# 9. Merge immediately when approved
gh pr merge --merge --delete-branch  # Use merge commit for hotfix

# 10. Verify issue closed
gh issue view 245

# 11. Create release and security advisory
gh release create v1.2.1 \
  --title "Security Release v1.2.1" \
  --notes "Critical security fix. All users should update immediately."
```

---

## Best Practices

### Branch Management

#### ✅ DO

- **Create branch from latest main**
  ```bash
  git checkout main
  git pull origin main
  git checkout -b feat/123-new-feature
  ```

- **Keep branches small and focused**
  - One issue = one branch
  - Single responsibility per branch
  - Easy to review (< 500 lines changed)

- **Use descriptive branch names**
  ```bash
  feat/67-add-serverless-skill       # ✅ Clear and specific
  docs/89-update-installation-guide  # ✅ Describes the change
  ```

- **Update from main regularly**
  ```bash
  # If main has advanced
  git checkout main
  git pull origin main
  git checkout feat/123-your-branch
  git rebase main
  ```

- **Delete branches after merge**
  ```bash
  gh pr merge --squash --delete-branch
  git branch -d feat/123-your-branch
  ```

#### ❌ DON'T

- **Don't create branches without issues**
  - Always create GitHub issue first
  - Issue gets auto-triaged and tracked

- **Don't use vague branch names**
  ```bash
  fix-bug          # ❌ Which bug?
  updates          # ❌ What updates?
  feat-123         # ❌ Missing description
  ```

- **Don't let branches get stale**
  - Merge within 1-3 days
  - If taking longer, break into smaller issues

- **Don't work on main directly**
  ```bash
  # ❌ NEVER do this
  git checkout main
  # make changes
  git commit -m "changes"
  git push origin main  # Blocked by branch protection
  ```

- **Don't reuse old branches**
  ```bash
  # ❌ Bad practice
  git checkout old-feature-branch
  # work on different feature

  # ✅ Create new branch instead
  git checkout -b feat/new-issue-description
  ```

---

### Commit Practices

#### ✅ DO

- **Make atomic commits**
  - One logical change per commit
  - Commit compiles/works independently
  - Easy to revert if needed

- **Write meaningful messages**
  ```bash
  # ✅ Good
  feat(skills): add DCF valuation model

  Implements complete DCF analysis with:
  - Free cash flow calculations
  - WACC computation
  - Terminal value estimation

  Closes #78
  ```

- **Reference issues in commits**
  ```bash
  Closes #123      # Closes issue when PR merges
  Fixes #456       # Same as Closes
  Resolves #789    # Same as Closes
  Related to #101  # Links without closing
  ```

- **Commit early and often (locally)**
  - Save progress frequently
  - Can squash before pushing
  - Easy to rollback mistakes

#### ❌ DON'T

- **Don't make giant commits**
  ```bash
  # ❌ Bad
  git add .
  git commit -m "lots of changes"
  # (500 files changed, 10000 lines modified)
  ```

- **Don't use vague messages**
  ```bash
  # ❌ Bad commit messages
  git commit -m "fix"
  git commit -m "updates"
  git commit -m "changes"
  git commit -m "wip"
  ```

- **Don't commit broken code**
  - Test before committing
  - Ensure code runs
  - Don't break CI/CD

- **Don't commit secrets or sensitive data**
  ```bash
  # ❌ Never commit
  - .env files with API keys
  - credentials.json
  - Private tokens
  - Personal information
  ```

---

### PR Best Practices

#### ✅ DO

- **Fill out PR template completely**
  - Clear summary
  - All checkboxes addressed
  - Testing details provided

- **Keep PRs focused**
  - Single issue/feature per PR
  - Related changes only
  - Easy to review

- **Respond to reviews promptly**
  - Address feedback within 24 hours
  - Ask questions if unclear
  - Push updates when ready

- **Keep PR description updated**
  - If scope changes, update description
  - Document why changes were made
  - Keep checklist current

- **Link to related PRs/issues**
  ```markdown
  Related to #123
  Depends on #456
  Follows up #789
  ```

#### ❌ DON'T

- **Don't create PRs without description**
  - Always explain what and why
  - Use the template
  - Provide context

- **Don't mix unrelated changes**
  ```bash
  # ❌ Bad PR
  - Add new skill
  - Fix typo in README
  - Update dependencies
  - Refactor old code

  # ✅ Create separate PRs
  ```

- **Don't ignore review feedback**
  - Address all comments
  - Explain if you disagree
  - Don't force-merge

- **Don't merge without passing checks**
  - Wait for claude-review
  - Ensure branch is up-to-date
  - Resolve all conversations

---

### Merge Strategies

**Use squash merge (default)** when:
- ✅ Feature has many small commits
- ✅ Commit history isn't important
- ✅ Want clean main branch history
- ✅ Most features and bug fixes

**Use merge commit** when:
- ✅ Important feature with meaningful commits
- ✅ Want to preserve commit details
- ✅ Hotfixes or emergency changes
- ✅ Multiple contributors on branch

**Use rebase merge** when:
- ✅ Single clean commit
- ✅ Want linear history
- ✅ Small documentation fixes
- ✅ Already rebased and clean

---

## Troubleshooting

### Common Issues

#### Branch out of date with main

**Symptom**: PR shows merge conflicts or "branch out of date"

**Solution**:
```bash
git checkout main
git pull origin main
git checkout feat/123-your-branch
git rebase main

# If conflicts occur
# 1. Resolve conflicts in files
# 2. git add <resolved-files>
# 3. git rebase --continue

git push --force-with-lease
```

---

#### Accidentally committed to main

**Symptom**: Made changes on main branch instead of feature branch

**Solution**:
```bash
# Don't panic - main is protected, you can't push

# Option 1: Move changes to new branch
git checkout -b feat/123-intended-branch
git push -u origin feat/123-intended-branch

# Option 2: Stash and create branch
git stash
git checkout -b feat/123-intended-branch
git stash pop
git add .
git commit -m "feat: description"
git push -u origin feat/123-intended-branch

# Reset main to origin
git checkout main
git reset --hard origin/main
```

---

#### Pushed wrong commit message

**Symptom**: Commit message has typo or wrong format

**Solution**:
```bash
# If haven't pushed yet
git commit --amend -m "corrected message"

# If already pushed to feature branch (safe)
git commit --amend -m "corrected message"
git push --force-with-lease

# If already in PR, just add new commit
git commit --allow-empty -m "fix: correct previous commit message"
git push
```

---

#### Need to combine multiple commits

**Symptom**: Too many small commits, want to combine before merging

**Solution**:
```bash
# Interactive rebase to squash commits
git rebase -i HEAD~3  # Combine last 3 commits

# In editor, change 'pick' to 'squash' for commits to combine
# Save and edit combined commit message

git push --force-with-lease

# Or just use squash merge when merging PR
gh pr merge --squash --delete-branch
```

---

#### Merge conflicts

**Symptom**: Can't merge because of conflicts

**Solution**:
```bash
# Update with latest main
git checkout main
git pull origin main
git checkout feat/123-your-branch
git rebase main

# Conflicts will be shown
# Edit conflicted files (look for <<<<<<< markers)
# Choose which changes to keep

# After resolving each file
git add <resolved-file>

# Continue rebase
git rebase --continue

# If stuck, abort and try merge instead
git rebase --abort
git merge main  # Creates merge commit instead
```

---

#### Claude review fails

**Symptom**: `claude-review` status check fails or times out

**Solution**:
```bash
# 1. Check workflow logs
gh run list --workflow=claude-code-review.yml --limit 5
gh run view RUN_ID --log

# 2. Common causes:
# - PR too large (>500 lines) → split into smaller PRs
# - Timeout → re-run workflow
# - Syntax errors → fix and push update

# 3. Re-run workflow
gh run rerun RUN_ID

# 4. If persists, request manual review
# Add comment: "@claude please review again"
```

---

#### Deleted branch too early

**Symptom**: Need to reference or restore deleted branch

**Solution**:
```bash
# Find deleted branch commit
git reflog

# Look for: "commit: <message>" from your branch
# Note the commit hash (e.g., abc123)

# Recreate branch
git checkout -b feat/123-restored abc123

# Or cherry-pick specific commits
git checkout main
git checkout -b feat/123-new-branch
git cherry-pick abc123 def456
```

---

### Getting Help

**If you're stuck**:

1. **Check workflow logs**:
   ```bash
   gh run list --limit 10
   gh run view RUN_ID --log
   ```

2. **Review documentation**:
   - This guide (BRANCHING_STRATEGY.md)
   - CONTRIBUTING.md
   - .github/WORKFLOWS.md

3. **Ask Claude**:
   ```bash
   # In issue or PR comment
   @claude I'm having trouble with [specific problem]
   ```

4. **Create issue**:
   ```bash
   gh issue create \
     --title "Question: [your question]" \
     --label "question"
   ```

---

## Quick Reference Card

### Create & Start Work
```bash
git checkout main && git pull origin main
git checkout -b <type>/<issue>-<description>
gh issue edit <issue> --add-label "status: in-progress"
```

### Commit & Push
```bash
git add .
git commit -m "<type>(<scope>): <subject>

<body>

Closes #<issue>"
git push -u origin <branch-name>
```

### Create PR & Merge
```bash
gh pr create --fill
gh issue edit <issue> --add-label "status: in-review"
gh pr merge --squash --delete-branch
```

### Branch Cleanup

**Philosophy**: Clean repository = clear organization. Delete branches promptly after merge to maintain clarity and prevent confusion.

#### Automatic Remote Branch Deletion (Recommended)

**Enable in GitHub Settings** (one-time setup):
1. Go to: Repository → Settings → General → Pull Requests
2. Check: ✅ "Automatically delete head branches"
3. Save changes

**Result**: Remote branches automatically deleted when PR merges

#### Manual Cleanup After Merge

**If automatic deletion is enabled** (recommended):
```bash
# After PR merge, only need to clean up local branch
git checkout main
git pull origin main
git branch -d feat/123-your-branch  # Delete local branch
```

**If automatic deletion is NOT enabled**:
```bash
# After PR merge, clean up both remote and local
git checkout main
git pull origin main

# Delete remote branch
git push origin --delete feat/123-your-branch

# Delete local branch
git branch -d feat/123-your-branch
```

**Using GitHub CLI** (easiest - does both):
```bash
# When merging PR, use --delete-branch flag
gh pr merge --squash --delete-branch

# This deletes:
# ✅ Remote branch on GitHub
# (You still need to delete local branch manually)

# Then clean up local:
git checkout main
git pull origin main
git branch -d feat/123-your-branch
```

#### Periodic Cleanup

**Clean up stale local branches** (weekly or monthly):

```bash
# List merged branches (safe to delete)
git branch --merged main | grep -v "^\*\|main"

# Delete all merged branches
git branch --merged main | grep -v "^\*\|main" | xargs -n 1 git branch -d

# Prune remote-tracking references to deleted branches
git fetch --prune

# List all local branches and their status
git branch -vv
```

**Clean up remote-tracking references**:
```bash
# Remove references to deleted remote branches
git fetch --prune origin

# Or prune all remotes
git remote prune origin
```

**Check for stale branches**:
```bash
# List branches by last commit date
git for-each-ref --sort=-committerdate refs/heads/ \
  --format='%(refname:short)|%(committerdate:short)|%(subject)' \
  | column -t -s '|'

# Find branches older than 30 days
git for-each-ref --sort=-committerdate refs/heads/ \
  --format='%(refname:short)|%(committerdate:short)' \
  | awk -F'|' '{if($2 < "'$(date -v-30d +%Y-%m-%d 2>/dev/null || date -d '30 days ago' +%Y-%m-%d)'") print $1}'
```

#### Cleanup Checklist

**After Every PR Merge**:
- [ ] Remote branch automatically deleted (if auto-delete enabled)
- [ ] Switch to main: `git checkout main`
- [ ] Pull latest: `git pull origin main`
- [ ] Delete local branch: `git branch -d <branch-name>`
- [ ] Verify deletion: `git branch`

**Weekly/Monthly Maintenance**:
- [ ] Prune stale remote references: `git fetch --prune`
- [ ] List merged branches: `git branch --merged main`
- [ ] Delete merged local branches
- [ ] Review branch age report
- [ ] Clean up branches older than 30 days (if forgotten)

#### Troubleshooting Cleanup

**Branch won't delete** (unmerged changes):
```bash
# Use -D to force delete (CAUTION: loses unmerged work)
git branch -D feat/123-your-branch

# Or verify if actually merged
git branch --merged main | grep feat/123
```

**Still seeing deleted remote branches**:
```bash
# Prune stale references
git fetch --prune origin

# Verify cleanup
git branch -r
```

**Accidentally deleted wrong branch**:
```bash
# Find commit in reflog
git reflog

# Restore branch
git checkout -b feat/123-restored <commit-hash>
```

### Update Branch
```bash
git checkout main && git pull origin main
git checkout <branch-name>
git rebase main
git push --force-with-lease
```

---

**Version**: 1.0.0
**Last Updated**: 2025-10-24
**Status**: ✅ Production Standard

This branching strategy is production-ready and battle-tested. Follow these guidelines for clean, maintainable, and collaborative development workflow.
