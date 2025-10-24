# Plan to Issues Automation

## Overview

Automatically convert GitHub issue plans into trackable subtask issues. When you create an issue with the `plan` label, Claude automatically creates child issues for each task and links everything together.

**Status**: ✅ Active
**Workflow**: [plan-to-issues.yml](workflows/plan-to-issues.yml)
**Trigger**: Issues with `plan` label

---

## 🎯 What It Does

**You create one plan issue** → **Automation creates multiple subtask issues**

```
Plan Issue (#100)
├── Task Issue (#101) - Design UI
├── Task Issue (#102) - Implement backend
├── Task Issue (#103) - Add tests
└── Task Issue (#104) - Update docs
```

**Each subtask**:
- ✅ Separate GitHub issue (trackable)
- ✅ Linked to parent plan
- ✅ Added to project board
- ✅ Labeled as `subtask` and `plan-item`

---

## 📝 How to Create a Plan

### Step 1: Create GitHub Issue

Use markdown checkboxes for tasks:

```markdown
Title: Plan: User Authentication Feature
Label: plan

## Goal
Implement complete user authentication system with login, JWT tokens, and password reset.

## Tasks
- [ ] Design login UI components
- [ ] Implement backend JWT authentication
- [ ] Add password reset flow
- [ ] Write integration tests
- [ ] Update documentation

## Context
This is needed for the MVP release targeting Q1 2025.
Priority: High
```

### Step 2: Add `plan` Label

**Via CLI**:
```bash
gh issue create \
  --title "Plan: User Authentication Feature" \
  --label "plan" \
  --body-file plan-template.md
```

**Via GitHub UI**:
1. Create issue
2. Add label: `plan`
3. Save issue

### Step 3: Wait for Automation (~30-60 seconds)

The workflow will:
1. ✅ Detect `plan` label
2. ✅ Parse tasks from issue body
3. ✅ Create child issue for each task
4. ✅ Link all issues to parent
5. ✅ Add everything to project board
6. ✅ Post summary comment

---

## 🎨 Supported Task Formats

The automation recognizes multiple formats:

### ✅ Markdown Checkboxes (Recommended)
```markdown
- [ ] Design login UI
- [ ] Implement JWT auth
- [ ] Add password reset
```

### ✅ Numbered Lists
```markdown
1. Design login UI
2. Implement JWT auth
3. Add password reset
```

### ✅ Bulleted Lists
```markdown
- Design login UI
- Implement JWT auth
- Add password reset
```

**Mix and match** - The automation handles all formats!

---

## 📊 Example Plan Issue

**Title**: `Plan: Mobile App Dashboard Feature`

**Body**:
```markdown
## Goal
Build a mobile dashboard with key metrics, charts, and real-time updates.

## Background
Users need to quickly view their top metrics on mobile. Desktop dashboard exists, now need mobile-optimized version.

## Tasks
- [ ] Design mobile dashboard UI mockups
- [ ] Implement chart components (React Native)
- [ ] Add real-time data sync
- [ ] Optimize for iOS and Android
- [ ] Write E2E tests with Playwright
- [ ] Update mobile documentation

## Success Criteria
- Dashboard loads in <2 seconds
- Charts update in real-time
- Works offline with cached data
- 100% test coverage

## Timeline
Target: 2 weeks (10 business days)
```

**After automation runs**, you'll get:

### Parent Issue Updated
```markdown
## 🤖 Plan Automation Complete

This plan has been converted into trackable subtask issues:

### Subtasks Created

- [ ] #105 - Task: Design mobile dashboard UI mockups
- [ ] #106 - Task: Implement chart components (React Native)
- [ ] #107 - Task: Add real-time data sync
- [ ] #108 - Task: Optimize for iOS and Android
- [ ] #109 - Task: Write E2E tests with Playwright
- [ ] #110 - Task: Update mobile documentation

**Total Subtasks**: 6
**Project Board**: All tasks added to @claude-skills-factory
```

### 6 Child Issues Created

**Issue #105**:
```markdown
Title: Task: Design mobile dashboard UI mockups
Labels: subtask, plan-item

## Parent Plan

This task is part of #104: Plan: Mobile App Dashboard Feature

## Task Description

Design mobile dashboard UI mockups

## Context

Build a mobile dashboard with key metrics, charts, and real-time updates.

---

**Parent**: #104
**Created**: Automatically from plan automation
**Project**: @claude-skills-factory
```

*(Same format for issues #106-#110)*

---

## 🚀 Workflow Timeline

**What happens when you create a plan issue:**

```
Issue Created with 'plan' label
    ↓
~5-10 seconds: Workflow triggers
    ↓
~30-60 seconds: Claude parses plan
    ↓
~5 seconds per task: Create child issues
    ↓
~5 seconds: Link everything
    ↓
~5 seconds: Add to project board
    ↓
~5 seconds: Post summary
    ↓
✅ Complete!
```

**Total time**: ~1-2 minutes for 5 tasks

---

## 🎯 Benefits

### For Project Management
- ✅ **Visual hierarchy** - Parent + child structure
- ✅ **Trackable progress** - Check off tasks as completed
- ✅ **Project board** - All tasks visible in one place
- ✅ **Assignment** - Assign subtasks to team members
- ✅ **Discussion** - Each task has its own comment thread

### For Team Collaboration
- ✅ **Clear ownership** - Assign each subtask
- ✅ **Parallel work** - Multiple people on different tasks
- ✅ **Progress tracking** - See what's done/in-progress/todo
- ✅ **Dependency management** - Link related tasks

### For Automation
- ✅ **No manual creation** - Save 5-10 minutes per plan
- ✅ **Consistent format** - All tasks follow same structure
- ✅ **Auto-linked** - No forgetting to link issues
- ✅ **Project integration** - Auto-added to board

---

## 📚 Advanced Usage

### Nested Plans

Want to create a plan with sub-plans?

**Epic Issue** (label: `plan`):
```markdown
## Goal
Launch V2 of the platform

## Tasks
- [ ] Complete user authentication feature
- [ ] Complete dashboard feature
- [ ] Complete API improvements
```

Each subtask can itself be labeled `plan` to create another level!

### Task Dependencies

Indicate dependencies in task descriptions:

```markdown
## Tasks
- [ ] Design database schema
- [ ] Implement API endpoints (requires: database schema)
- [ ] Build UI components (requires: API endpoints)
- [ ] Write integration tests (requires: UI components)
```

### Priority Levels

Add priority to task descriptions:

```markdown
## Tasks
- [ ] [P0] Fix critical security bug
- [ ] [P1] Implement user login
- [ ] [P2] Add profile page
- [ ] [P3] Polish UI animations
```

### Assignees

Mention who should handle each task:

```markdown
## Tasks
- [ ] Design UI mockups (@designer)
- [ ] Implement backend (@backend-dev)
- [ ] Write tests (@qa-engineer)
```

Automation will mention these in the created issues.

---

## 🔧 Customization

### Change Task Prefix

By default, subtasks are titled "Task: [name]". To change:

Edit [plan-to-issues.yml](workflows/plan-to-issues.yml:82):
```yaml
--title "Task: [extracted task text]"  # Change "Task:" to anything
```

### Add Custom Labels

Add more labels to subtasks:

Edit [plan-to-issues.yml](workflows/plan-to-issues.yml:83):
```yaml
--label "subtask,plan-item,needs-review"  # Add more labels
```

### Change Project

Currently adds to project #7. To change:

Edit [plan-to-issues.yml](workflows/plan-to-issues.yml:115):
```yaml
gh project item-add 7  # Change 7 to your project number
```

---

## 🧪 Testing

### Test Plan Creation

```bash
gh issue create \
  --title "Plan: Test Plan Automation" \
  --label "plan" \
  --body "## Goal
Test the plan-to-issues automation

## Tasks
- [ ] First test task
- [ ] Second test task
- [ ] Third test task

This is a test plan to verify automation works."
```

**Expected results** (within 2 minutes):
1. ✅ 3 child issues created (#N, #N+1, #N+2)
2. ✅ All labeled `subtask` and `plan-item`
3. ✅ Parent issue updated with links
4. ✅ All issues added to project board
5. ✅ Summary comment posted

### Verify Workflow

```bash
# Check workflow runs
gh run list --workflow=plan-to-issues.yml --limit 5

# View specific run
gh run view <run-id> --log

# Check created issues
gh issue list --label "subtask" --limit 10
```

---

## ❓ Troubleshooting

### No Subtasks Created

**Symptom**: Plan issue created but no child issues appear

**Possible causes**:

1. **Missing `plan` label**
   - **Fix**: Add `plan` label to issue
   - Workflow triggers on label addition

2. **No tasks detected**
   - **Check**: Issue body has checkboxes/lists
   - **Fix**: Add tasks in supported format (see formats above)

3. **Workflow didn't run**
   - **Check**: `gh run list --workflow=plan-to-issues.yml --limit 1`
   - **Fix**: Check workflow logs for errors

### Workflow Failed

**Check logs**:
```bash
gh run list --workflow=plan-to-issues.yml --limit 1
gh run view <run-id> --log | grep -i error
```

**Common errors**:

1. **Token permissions**
   - Ensure `PROJECTS_TOKEN` has `repo` and `project` scopes
   - Recreate token if needed

2. **Label doesn't exist**
   - Create `plan` label: `gh label create plan --color "0366d6"`
   - Create `subtask` label: `gh label create subtask --color "bfdadc"`
   - Create `plan-item` label: `gh label create plan-item --color "d4c5f9"`

3. **Project not found**
   - Verify project #7 exists
   - Update workflow if using different project number

### Subtasks Not Added to Project

**Symptom**: Issues created but not in project board

**Cause**: Token missing `project` scope or wrong project number

**Fix**:
1. Verify token has `project` scope
2. Check project number is correct (currently: 7)
3. Manually add: `gh project item-add 7 --owner alirezarezvani --url ISSUE_URL`

---

## 🎓 Best Practices

### Writing Good Plans

✅ **DO**:
- Write clear, actionable tasks
- Include context and goals
- Use consistent task format
- Add priority/assignees in descriptions
- Keep tasks focused and specific

❌ **DON'T**:
- Make tasks too vague ("Do the thing")
- Mix multiple concerns in one task
- Create overly long task lists (>15 tasks)
- Forget to add the `plan` label

### Managing Plans

✅ **DO**:
- Review generated subtasks
- Assign tasks to team members
- Update parent issue as progress happens
- Close parent when all subtasks complete
- Link related plans together

❌ **DON'T**:
- Manually create subtasks (let automation do it)
- Delete parent issue before subtasks complete
- Forget to add priority/context

---

## 📊 Metrics & Insights

### Track Plan Progress

```bash
# Count open plans
gh issue list --label "plan" --state "open" | wc -l

# Count open subtasks
gh issue list --label "subtask" --state "open" | wc -l

# View all plans
gh issue list --label "plan"

# View subtasks for plan #100
gh issue list --search "parent:100"
```

### Performance Monitoring

```bash
# View recent plan automations
gh run list --workflow=plan-to-issues.yml --limit 10

# Check success rate
gh run list --workflow=plan-to-issues.yml --json conclusion | jq '[.[] | select(.conclusion != null)] | group_by(.conclusion) | map({conclusion: .[0].conclusion, count: length})'
```

---

## 🔗 Integration

### With Issue Triage

Plan issues are also triaged automatically:
- Parent issue gets triaged with type/priority
- Subtasks can be triaged individually

### With Project Board

All issues automatically added to project board:
- **Parent**: Shows overall plan
- **Children**: Individual trackable tasks
- **Status**: Move tasks through workflow columns

### With GitHub Milestones

Assign plans to milestones:
```bash
gh issue edit <plan-number> --milestone "Q1 2025"
```

All subtasks inherit the context.

---

## 📖 Examples

### Sprint Planning
```markdown
Title: Plan: Sprint 1 - MVP Features
Label: plan

## Goal
Complete MVP features for Q1 2025 launch

## Tasks
- [ ] User registration and login
- [ ] Profile management
- [ ] Dashboard with metrics
- [ ] Settings page
- [ ] Help documentation

## Timeline
Sprint: Jan 1-14, 2025
```

### Bug Fix Campaign
```markdown
Title: Plan: Q4 Bug Bash
Label: plan

## Goal
Resolve all P0/P1 bugs before year-end

## Tasks
- [ ] Fix authentication timeout bug (#45)
- [ ] Resolve memory leak in dashboard (#67)
- [ ] Fix mobile layout issues (#89)
- [ ] Address API rate limiting (#92)

## Success Criteria
- 0 P0 bugs remaining
- <5 P1 bugs remaining
```

### Feature Development
```markdown
Title: Plan: Real-time Notifications
Label: plan

## Goal
Implement real-time notification system

## Tasks
- [ ] Design notification UI/UX
- [ ] Set up WebSocket server
- [ ] Implement notification types (info, warning, error)
- [ ] Add notification preferences
- [ ] Add push notifications (mobile)
- [ ] Write E2E tests
- [ ] Performance testing

## Tech Stack
- Backend: Socket.IO
- Frontend: React hooks
- Mobile: React Native push
```

---

## 🎯 Current Status

✅ **Workflow active** - Ready to use
✅ **Documentation complete** - This guide
✅ **PROJECTS_TOKEN configured** - Automation ready
⚠️ **Labels needed** - Create `plan`, `subtask`, `plan-item` labels
📋 **Project board** - https://github.com/users/alirezarezvani/projects/7

---

## 📚 References

- **Workflow**: [.github/workflows/plan-to-issues.yml](workflows/plan-to-issues.yml)
- **Issue Triage**: [ISSUE_AUTO_TRIAGE.md](ISSUE_AUTO_TRIAGE.md)
- **Project Integration**: [PROJECT_INTEGRATION_SETUP.md](PROJECT_INTEGRATION_SETUP.md)
- **GitHub Tasklists**: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-tasklists

---

**Last Updated**: 2025-10-24
**Version**: 1.0.0
**Status**: ✅ Production ready
