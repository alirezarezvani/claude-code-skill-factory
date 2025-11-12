# GitHub Workflow Implementation Tracker

**Project**: Claude Code Skills Factory
**Timeline**: 2 Weeks (Nov 12 - Nov 26, 2025)
**Approach**: Full Implementation (modify existing, create when missing)
**Status**: 🟡 In Progress

---

## 📅 2-Week Timeline Overview

### Week 1: Foundation & Core Workflows
**Focus**: Branch protection, composite actions, core PR validation

- **Day 1-2** (Nov 12-13): Setup & Branch Protection
- **Day 3-4** (Nov 14-15): Composite Actions & PR Validation
- **Day 5-7** (Nov 16-18): Auto-Branch Creation & Testing

### Week 2: Commands & Integration
**Focus**: Slash commands, auto-merge, documentation

- **Day 8-10** (Nov 19-21): Slash Commands
- **Day 11-12** (Nov 22-23): Auto-Merge & Cleanup
- **Day 13-14** (Nov 24-26): Documentation & Team Training

---

## Week 1: Foundation & Core Workflows

### Day 1: Tuesday, Nov 12, 2025 ✅ IN PROGRESS

**Goal**: Push `dev` branch, configure branch protection, clean up old branches

**Tasks**:
- [ ] 1.1: Push `dev` branch to origin
  ```bash
  git checkout dev
  git push -u origin dev
  ```

- [ ] 1.2: Apply branch protection rules in GitHub Settings
  - Follow: `.github/BRANCH_PROTECTION_CONFIG.md`
  - Protect `main` branch
  - Protect `dev` branch
  - Set `dev` as default branch

- [ ] 1.3: Clean up old branches that don't match naming convention
  ```bash
  # Close PRs or rename branches
  # Delete: claude/issue-*, feat-*, docs/* (if using docs/)
  # Keep: feat/*, fix/*, hotfix/*
  ```

- [ ] 1.4: Document current state
  - Take screenshot of branch protection settings
  - Note any issues or blockers
  - Update this tracker

**Acceptance Criteria**:
- ✅ `dev` branch exists on origin
- ✅ Branch protection configured for `main` and `dev`
- ✅ `dev` set as default branch
- ✅ Old branches cleaned up or renamed

**Estimated Time**: 2-3 hours

---

### Day 2: Wednesday, Nov 13, 2025

**Goal**: Create composite actions for reusability (DRY principle)

**Tasks**:
- [ ] 2.1: Create `.github/actions/` directory structure
  ```bash
  mkdir -p .github/actions/fork-safety
  mkdir -p .github/actions/quality-gates
  mkdir -p .github/actions/branch-cleanup
  ```

- [ ] 2.2: Create `fork-safety` composite action
  - Source: Blueprint's `.github/actions/fork-safety/action.yml`
  - Purpose: Detect if PR is from fork
  - Outputs: `is-fork`, `should-skip-writes`

- [ ] 2.3: Create `quality-gates` composite action
  - Check if scripts exist: `npm run lint`, `npm run type-check`, `npm test`
  - Run checks with graceful fallback (continue-on-error)
  - Purpose: Reusable quality validation

- [ ] 2.4: Create `branch-cleanup` composite action (for later use)
  - Delete merged branches
  - Post cleanup confirmation
  - Purpose: Auto-cleanup after PR merge

**Files Created**:
- `.github/actions/fork-safety/action.yml`
- `.github/actions/quality-gates/action.yml`
- `.github/actions/branch-cleanup/action.yml`
- `.github/actions/README.md` (documentation)

**Acceptance Criteria**:
- ✅ Three composite actions created and tested
- ✅ Actions documented in README
- ✅ Actions can be called from workflows

**Estimated Time**: 3-4 hours

---

### Day 3: Thursday, Nov 14, 2025

**Goal**: Create/modify PR validation workflow for `dev` branch

**Tasks**:
- [ ] 3.1: Create `pr-into-dev.yml` workflow (NEW FILE)
  - Source: Blueprint's `.github/workflows/pr-into-dev.yml`
  - Trigger: PR to `dev` branch
  - Validations:
    - Branch name format (feature/*, fix/*, etc.)
    - PR title (conventional commits)
    - Issue linking (at least one issue)
    - Quality gates (use composite action)
    - Fork safety check

- [ ] 3.2: Test PR validation workflow
  - Create test feature branch: `feature/test-pr-validation`
  - Create test PR targeting `dev`
  - Verify all checks run
  - Fix any issues

- [ ] 3.3: Modify `ci-commit-branch-guard.yml` (EXISTING FILE)
  - **Keep existing logic**
  - Add support for new branch prefixes if needed
  - Ensure compatibility with PR validation
  - Test with existing PRs

**Files Modified/Created**:
- `.github/workflows/pr-into-dev.yml` (NEW)
- `.github/workflows/ci-commit-branch-guard.yml` (MODIFIED - minor updates)

**Acceptance Criteria**:
- ✅ PR validation workflow runs on PR to dev
- ✅ Invalid branch names are rejected
- ✅ Invalid PR titles are rejected
- ✅ Quality gates run successfully

**Estimated Time**: 4-5 hours

---

### Day 4: Friday, Nov 15, 2025

**Goal**: Create release validation workflow for `main` branch

**Tasks**:
- [ ] 4.1: Create `dev-to-main.yml` workflow (NEW FILE)
  - Source: Blueprint's `.github/workflows/dev-to-main.yml`
  - Trigger: PR to `main` branch
  - Validations:
    - Source must be `dev` or `release/*` (reject feature/* branches)
    - Production build succeeds
    - All quality gates pass
    - Smoke tests (optional)

- [ ] 4.2: Add production build steps (adapt for this repo)
  - This repo may not have build step
  - Focus on YAML validation for skills
  - Validate all skills have proper frontmatter

- [ ] 4.3: Test release workflow
  - Create test PR from `dev` to `main`
  - Verify validation works
  - Ensure proper error messages

**Files Created**:
- `.github/workflows/dev-to-main.yml` (NEW)

**Acceptance Criteria**:
- ✅ Release validation workflow runs on PR to main
- ✅ Only `dev` and `release/*` can PR to main
- ✅ Feature branches are rejected with helpful error
- ✅ Production validations pass

**Estimated Time**: 3-4 hours

---

### Weekend: Nov 16-17, 2025 (Optional Work)

**Goal**: Buffer time for catching up or getting ahead

**Optional Tasks**:
- Review and test all workflows created so far
- Fix any bugs or issues found
- Read ahead for Week 2 tasks
- Document learnings and improvements

---

### Day 5: Monday, Nov 18, 2025

**Goal**: Create auto-branch creation workflow

**Tasks**:
- [ ] 5.1: Create `create-branch-on-issue.yml` workflow (NEW FILE)
  - Source: Blueprint's `.github/workflows/create-branch-on-issue.yml`
  - Trigger: Issue labeled with `claude-code` + `status:ready`
  - Logic:
    - Extract issue number and title
    - Detect branch type from labels (type:feature, type:fix, etc.)
    - Create slug from title (max 50 chars, kebab-case)
    - Build branch name: `{type}/issue-{number}-{slug}`
    - Create branch from `dev` base
    - Post checkout instructions as comment

- [ ] 5.2: Test auto-branch creation
  - Create test issue
  - Label with `claude-code` + `status:ready` + `type:feature`
  - Verify branch is created automatically
  - Verify comment is posted with instructions

- [ ] 5.3: Document auto-branch workflow
  - Add to `.github/CLAUDE.md`
  - Add usage examples

**Files Created**:
- `.github/workflows/create-branch-on-issue.yml` (NEW)

**Files Modified**:
- `.github/CLAUDE.md` (add auto-branch documentation)

**Acceptance Criteria**:
- ✅ Branch automatically created when issue labeled
- ✅ Branch name follows convention
- ✅ Comment posted with checkout instructions
- ✅ Works with different issue types (feature, fix, etc.)

**Estimated Time**: 3-4 hours

---

## Week 2: Commands & Integration

### Day 6: Tuesday, Nov 19, 2025

**Goal**: Create `/commit-smart` slash command

**Tasks**:
- [ ] 6.1: Create `.claude/commands/github/` directory
  ```bash
  mkdir -p .claude/commands/github
  ```

- [ ] 6.2: Create `/commit-smart` command (NEW FILE)
  - Source: Blueprint's `.claude/commands/github/commit-smart.md`
  - Features:
    - Git status check
    - Interactive staging
    - Secret detection (API keys, tokens)
    - Quality checks
    - Conventional commit guidance
    - Auto co-author (Claude)

- [ ] 6.3: Test `/commit-smart` command
  - Make test changes
  - Run `/commit-smart` in Claude Code
  - Verify all steps work
  - Test secret detection

- [ ] 6.4: Create command documentation
  - Add to `.claude/commands/README.md`
  - Add usage examples

**Files Created**:
- `.claude/commands/github/commit-smart.md` (NEW)
- `.claude/commands/github/README.md` (NEW - documentation)

**Acceptance Criteria**:
- ✅ `/commit-smart` command works in Claude Code
- ✅ Secret detection prevents committing sensitive data
- ✅ Quality checks run before commit
- ✅ Conventional commit format enforced

**Estimated Time**: 4-5 hours

---

### Day 7: Wednesday, Nov 20, 2025

**Goal**: Create `/create-pr` slash command

**Tasks**:
- [ ] 7.1: Create `/create-pr` command (NEW FILE)
  - Source: Blueprint's `.claude/commands/github/create-pr.md`
  - Features:
    - Branch detection and validation
    - Auto-push if not pushed
    - Target branch selection (default: `dev`)
    - Quality gates before PR
    - Extract issue number from branch
    - Build PR body from template
    - Create PR with `gh pr create`

- [ ] 7.2: Create PR template (if not exists)
  - Check if `.github/pull_request_template.md` exists
  - Modify if needed to include:
    - Issue linking section
    - Testing checklist
    - Claude Code attribution

- [ ] 7.3: Test `/create-pr` command
  - Create test feature branch
  - Make changes and commit
  - Run `/create-pr`
  - Verify PR is created correctly

**Files Created**:
- `.claude/commands/github/create-pr.md` (NEW)

**Files Modified**:
- `.github/pull_request_template.md` (MODIFIED if exists, or NEW)

**Acceptance Criteria**:
- ✅ `/create-pr` command creates PR targeting dev
- ✅ PR body includes issue links
- ✅ Quality gates run before PR creation
- ✅ Helpful error messages if validation fails

**Estimated Time**: 3-4 hours

---

### Day 8: Thursday, Nov 21, 2025

**Goal**: Create supporting slash commands

**Tasks**:
- [ ] 8.1: Create `/switch-to-dev` command (NEW FILE)
  - Features:
    - Check current branch
    - Warn if uncommitted changes
    - Offer to stash if requested
    - Switch to `dev`
    - Pull latest changes
    - Confirm ready for next task

- [ ] 8.2: Create `/start-task` command (NEW FILE)
  - Features:
    - Ensure on `dev` branch
    - Pull latest changes
    - Ask for task description
    - Create GitHub issue (or use existing)
    - Label issue appropriately
    - Wait for auto-branch creation
    - Checkout new branch

- [ ] 8.3: Test both commands
  - Test `/switch-to-dev` from feature branch
  - Test `/start-task` workflow end-to-end

**Files Created**:
- `.claude/commands/github/switch-to-dev.md` (NEW)
- `.claude/commands/github/start-task.md` (NEW)

**Acceptance Criteria**:
- ✅ `/switch-to-dev` safely switches to dev
- ✅ `/start-task` creates issue and branch
- ✅ Commands work together smoothly

**Estimated Time**: 4-5 hours

---

### Day 9: Friday, Nov 22, 2025

**Goal**: Create auto-merge and cleanup workflow

**Tasks**:
- [ ] 9.1: Create `pr-cleanup.yml` workflow (NEW FILE)
  - Trigger: PR approved and all checks pass
  - Actions:
    - Auto-merge PR to dev (squash merge)
    - Delete source branch
    - Post cleanup confirmation comment
    - Optionally switch local branch to dev

- [ ] 9.2: Configure auto-merge settings
  - Check GitHub repository settings
  - Enable "Allow auto-merge"
  - Configure merge methods (squash preferred)

- [ ] 9.3: Test auto-merge workflow
  - Create test PR
  - Approve PR
  - Verify auto-merge happens
  - Verify branch is deleted

**Files Created**:
- `.github/workflows/pr-cleanup.yml` (NEW)

**Acceptance Criteria**:
- ✅ PR auto-merges after approval
- ✅ Source branch is deleted
- ✅ Confirmation comment posted
- ✅ Works with both dev and main PRs

**Estimated Time**: 3-4 hours

---

### Weekend: Nov 23-24, 2025 (Optional Work)

**Goal**: Buffer time and preparation for final week

**Tasks**:
- Review all workflows and commands
- Fix bugs found during testing
- Prepare documentation for final review
- Clean up code and comments

---

### Day 10: Monday, Nov 25, 2025

**Goal**: Comprehensive documentation

**Tasks**:
- [ ] 10.1: Create `GITHUB_WORKFLOW.md` (NEW FILE)
  - Complete workflow guide
  - How to start a task
  - How to commit and create PR
  - How to merge to main
  - Emergency procedures
  - Troubleshooting

- [ ] 10.2: Update `.github/CLAUDE.md` (MODIFY)
  - Add branching workflow section
  - Add slash commands reference
  - Add common workflows examples
  - Add troubleshooting tips

- [ ] 10.3: Update root `README.md` (MODIFY)
  - Add workflow section
  - Link to GITHUB_WORKFLOW.md
  - Add quick start guide

- [ ] 10.4: Update `WORKFLOW_ADAPTATION_PLAN.md` (MODIFY)
  - Mark completed phases
  - Document any deviations from plan
  - Add lessons learned

**Files Created**:
- `.github/GITHUB_WORKFLOW.md` (NEW)

**Files Modified**:
- `.github/CLAUDE.md` (MODIFIED)
- `README.md` (MODIFIED)
- `WORKFLOW_ADAPTATION_PLAN.md` (MODIFIED)

**Acceptance Criteria**:
- ✅ Complete workflow documentation exists
- ✅ All files cross-reference each other
- ✅ Examples and screenshots included
- ✅ Troubleshooting guide comprehensive

**Estimated Time**: 4-5 hours

---

### Day 11: Tuesday, Nov 26, 2025

**Goal**: Final testing, cleanup, and handoff

**Tasks**:
- [ ] 11.1: End-to-end workflow testing
  - Start task with `/start-task`
  - Make changes
  - Commit with `/commit-smart`
  - Create PR with `/create-pr`
  - Get review (automated Claude review)
  - Approve and auto-merge
  - Return to dev with `/switch-to-dev`

- [ ] 11.2: Create workflow testing checklist
  - Document all test scenarios
  - Create automated tests if possible
  - Verify all edge cases

- [ ] 11.3: Team training materials
  - Create quick reference card
  - Create video walkthrough (optional)
  - Prepare FAQ document

- [ ] 11.4: Final cleanup
  - Delete test branches
  - Close test issues
  - Clean up test PRs
  - Archive old branches

- [ ] 11.5: Update implementation tracker (this file)
  - Mark all tasks complete
  - Document final state
  - Note any follow-up items

**Deliverables**:
- ✅ Complete, tested workflow system
- ✅ Comprehensive documentation
- ✅ Training materials
- ✅ Clean repository

**Acceptance Criteria**:
- ✅ All workflows working correctly
- ✅ All commands functional
- ✅ Documentation complete
- ✅ Repository clean

**Estimated Time**: Full day (6-8 hours)

---

## 📊 Progress Tracking

### Overall Completion

- **Week 1**: 0% (0/6 days complete)
- **Week 2**: 0% (0/5 days complete)
- **Total**: 0% (0/11 days complete)

### Component Status

**Infrastructure** (Week 1):
- [ ] Branch protection configured
- [ ] Composite actions created
- [ ] Dev branch established as default
- [ ] Old branches cleaned up

**Workflows** (Week 1):
- [ ] PR validation (dev) - `pr-into-dev.yml`
- [ ] Release validation (main) - `dev-to-main.yml`
- [ ] Auto-branch creation - `create-branch-on-issue.yml`

**Slash Commands** (Week 2):
- [ ] `/commit-smart` - Smart commits
- [ ] `/create-pr` - PR creation
- [ ] `/switch-to-dev` - Branch switching
- [ ] `/start-task` - Task initiation

**Automation** (Week 2):
- [ ] Auto-merge and cleanup - `pr-cleanup.yml`
- [ ] Claude Code review integration (existing, verify)

**Documentation** (Week 2):
- [ ] GITHUB_WORKFLOW.md
- [ ] Updated .github/CLAUDE.md
- [ ] Updated README.md
- [ ] Training materials

---

## 🚧 Blockers & Issues

**Current Blockers**: None

**Potential Issues**:
- GitHub API rate limits during testing
- Existing workflows may conflict with new ones
- Team adoption and training time
- Emergency procedures may need refinement

**Mitigation**:
- Use workflow concurrency controls
- Test thoroughly before full rollout
- Create comprehensive documentation
- Plan for gradual adoption

---

## 📝 Daily Status Updates

### Day 1: Nov 12, 2025
**Status**: 🟡 In Progress
**Completed**:
- ✅ Created BRANCH_PROTECTION_CONFIG.md
- ✅ Created this tracker document
- [ ] Pending: Push dev branch
- [ ] Pending: Apply branch protection

**Notes**: Starting implementation

---

## 🎓 Team Training Plan

### Training Sessions

**Session 1: Workflow Overview** (1 hour)
- Introduction to new branching strategy
- Why we're making this change
- Benefits and goals
- Q&A

**Session 2: Hands-on Practice** (2 hours)
- Walkthrough of complete workflow
- Practice creating issues, branches, PRs
- Practice using slash commands
- Troubleshooting common issues

**Session 3: Advanced Topics** (1 hour)
- Emergency procedures
- Hotfix workflow
- Conflict resolution
- Best practices

### Training Materials

- [ ] Quick reference card (1-page PDF)
- [ ] Video walkthrough (10-15 min)
- [ ] FAQ document
- [ ] Troubleshooting guide

---

## 🎯 Success Metrics

**Week 1 Goals**:
- ✅ Branch protection configured
- ✅ Core workflows operational
- ✅ Auto-branch creation working

**Week 2 Goals**:
- ✅ All slash commands functional
- ✅ Auto-merge working
- ✅ Documentation complete

**Final Success Criteria**:
- ✅ Zero direct pushes to main
- ✅ All PRs go through dev
- ✅ Automated branch creation working
- ✅ Claude Code reviews integrated
- ✅ Team trained and comfortable with workflow
- ✅ Documentation comprehensive and up-to-date

---

**Last Updated**: Nov 12, 2025
**Next Review**: Nov 15, 2025 (end of Week 1)
**Final Review**: Nov 26, 2025 (end of implementation)
