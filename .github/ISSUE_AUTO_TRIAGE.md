# Issue Auto-Triage System

## Overview

The **Issue Auto-Triage** system uses Claude AI to automatically analyze, categorize, and prioritize GitHub issues within seconds of creation. This provides instant, consistent, and intelligent issue management without manual effort.

**Status**: ✅ Active
**Workflow**: [issue-triage.yml](workflows/issue-triage.yml)
**Trigger**: Automatically on every new issue

---

## 🎯 What It Does

When a new issue is created, Claude automatically:

1. **Analyzes** the issue title and description
2. **Classifies** the issue type (bug, feature, documentation, etc.)
3. **Assigns** priority level (P0-P3) with justification
4. **Evaluates** clarity and completeness
5. **Suggests** appropriate labels
6. **Identifies** affected repository components
7. **Searches** for related/duplicate issues
8. **Recommends** next actions
9. **Applies** labels automatically
10. **Posts** comprehensive triage analysis as comment

**Timeline**: ~30-60 seconds from issue creation to complete triage

---

## 📊 Classification Framework

### Issue Types

| Label | Description | Examples |
|-------|-------------|----------|
| **bug** | Something isn't working correctly | Skill fails to load, script error, broken link |
| **feature** | New capability request | Add new skill type, support new format |
| **documentation** | Docs improvements | README updates, examples needed, clarifications |
| **question** | User needs help | How do I use X? What does Y mean? |
| **enhancement** | Improve existing functionality | Make skill faster, better error handling |
| **skill-request** | Request for new skill example | Need skill for X domain, Y use case |
| **agent-request** | Request for new agent example | Need agent for Z role, W task |
| **template-improvement** | Improve generation templates | Better prompts, more presets, validation |

### Priority Levels

| Priority | Description | Response Time | Examples |
|----------|-------------|---------------|----------|
| **P0** | **Critical** - Blocks all users | Immediate | Security vulnerability, data loss, complete breakage |
| **P1** | **High** - Major functionality broken | Same day | Key skill fails, workflow broken for many users |
| **P2** | **Medium** - Important but has workaround | 2-7 days | Feature missing, moderate bugs, documentation gaps |
| **P3** | **Low** - Nice to have, minimal impact | When capacity allows | Cosmetic issues, minor enhancements, suggestions |

### Clarity Score (1-5 ⭐)

- **⭐** - Extremely vague, unusable
- **⭐⭐** - Missing critical information
- **⭐⭐⭐** - Acceptable but needs clarification
- **⭐⭐⭐⭐** - Good, mostly complete
- **⭐⭐⭐⭐⭐** - Excellent, immediately actionable

### Actionability Status

- **Yes** - Can be worked on immediately
- **Needs Info** - Requires additional context from author
- **Blocked** - Depends on other issues or decisions

---

## 🤖 Triage Analysis Format

Every triaged issue receives a comment with this structure:

```markdown
## 🤖 Automatic Triage Analysis

**Issue Type**: bug
**Priority**: P2
**Clarity Score**: ⭐⭐⭐⭐
**Actionable**: Yes

---

### 📋 Summary
[Brief 2-3 sentence description of the issue]

### 🏷️ Suggested Labels
Primary: `bug`
Additional: `skills`, `P2`

### 🎯 Priority Justification
**P2**: [Explanation of why this priority level]

### ✅ Completeness Check
- [x] Clear description
- [x] Steps to reproduce
- [x] Expected behavior described
- [ ] Error logs provided

**Missing Information**: Error logs would help diagnose the issue faster

### 💡 Recommended Action
[Specific next steps or who should handle this]

**Estimated Effort**: Moderate
**Affected Components**: claude-skills-examples/analyzing_financial_statements

### 🔗 Related Issues
#15, #23 - Similar issues with financial calculations

---

*🤖 Triaged automatically by Claude Code in ~30 seconds*
*Human review recommended before applying labels*
```

---

## 🏷️ Label System

### Automatic Label Application

Claude automatically applies labels based on high-confidence analysis:

- **Always applied**: Primary issue type (bug/feature/documentation/etc.)
- **Always applied**: Priority level (P0/P1/P2/P3)
- **Conditionally applied**: Component labels (skills/agents/templates/workflows)
- **Conditionally applied**: Status labels (needs-info/duplicate)

### Available Labels

**Type Labels**:
- `bug` - Something broken
- `feature` - New functionality
- `documentation` - Docs improvements
- `question` - Help needed
- `enhancement` - Improve existing
- `skill-request` - New skill wanted
- `agent-request` - New agent wanted
- `template-improvement` - Template enhancements

**Priority Labels**:
- `P0` - Critical (immediate response)
- `P1` - High (same day)
- `P2` - Medium (2-7 days)
- `P3` - Low (when capacity allows)

**Status Labels**:
- `needs-info` - Missing information
- `duplicate` - Already exists
- `wontfix` - Not addressing
- `good-first-issue` - Good for newcomers
- `help-wanted` - Community help welcome

**Component Labels**:
- `skills` - Affects skill examples
- `agents` - Affects agent examples
- `templates` - Affects generation templates
- `workflows` - Affects GitHub workflows
- `docs` - Affects documentation

---

## 🔍 Intelligence Features

### Duplicate Detection

Claude automatically searches for similar issues:
```bash
gh issue list --search "keywords from title and body"
```

If potential duplicates found:
- Links them in the triage comment
- Suggests closing as duplicate if confidence high
- Asks author to confirm relationship

### Related Issue Discovery

Claude identifies related issues even if not duplicates:
- Issues mentioning same components
- Issues with similar symptoms
- Issues by same author on related topics

### Context Awareness

Claude understands repository structure:
- References [CLAUDE.md](../CLAUDE.md) for standards
- Knows about skill examples in `claude-skills-examples/`
- Knows about generated skills in `generated-skills/`
- Understands template structure in `documentation/templates/`

---

## 📈 Benefits

### For Repository Maintainers

✅ **Instant triage** - Every issue categorized in 30 seconds
✅ **Consistent analysis** - No variation in quality or approach
✅ **Priority clarity** - Objective priority assignment
✅ **Duplicate prevention** - Automatic detection of similar issues
✅ **Better organization** - All issues properly labeled
✅ **Time savings** - No manual triage needed

### For Issue Authors

✅ **Fast feedback** - Know classification immediately
✅ **Clear expectations** - Understand priority and timeline
✅ **Better communication** - Prompted for missing info
✅ **Transparency** - See exactly how issue was analyzed

### For Contributors

✅ **Easy filtering** - Find issues by type/priority/component
✅ **Effort estimation** - Know complexity before starting
✅ **Component clarity** - Understand which parts affected
✅ **Related context** - Linked to similar issues automatically

---

## ⚙️ Configuration

### Workflow File

Location: [.github/workflows/issue-triage.yml](workflows/issue-triage.yml)

**Triggers**:
```yaml
on:
  issues:
    types: [opened]
```

**Permissions**:
```yaml
permissions:
  contents: read
  issues: write      # Add labels and comments
  id-token: write    # OIDC authentication
```

**Concurrency Control**:
```yaml
concurrency:
  group: triage-${{ github.event.issue.number }}
  cancel-in-progress: false  # Never cancel triage
```

### Customization Options

#### Modify Triage Prompt

Edit the `prompt:` section in [issue-triage.yml](workflows/issue-triage.yml:41-175) to:
- Add custom issue types
- Change priority criteria
- Adjust analysis framework
- Include project-specific context

#### Add Custom Labels

1. Create labels in GitHub: Settings → Labels
2. Update workflow prompt with new label names
3. Add to "Available Labels" section in prompt

#### Change Analysis Depth

**Quick Triage** (15 seconds):
```yaml
prompt: |
  Provide quick classification only:
  - Type: [label]
  - Priority: [P0-P3]
  - One sentence summary
```

**Deep Analysis** (60+ seconds):
```yaml
prompt: |
  Include full analysis plus:
  - Security implications
  - Performance impact
  - Breaking change assessment
  - API compatibility review
```

#### Disable Auto-Labeling

To make labels suggestions-only without auto-applying:

Remove this from prompt:
```yaml
# REMOVE THIS SECTION:
5. **Apply labels**: After posting comment, use `gh issue edit...`
```

---

## 🧪 Testing

### Test Auto-Triage

Create a test issue to verify the system:

```bash
gh issue create \
  --title "Test Issue: Verify Auto-Triage System" \
  --body "This is a test issue to verify that Claude automatically:

  1. Analyzes the issue within 60 seconds
  2. Posts a comprehensive triage comment
  3. Applies appropriate labels
  4. Identifies this as a test/question

  Expected: Should be labeled as 'question' with P3 priority."
```

**Expected results** (within 60 seconds):
1. ✅ Workflow triggers: `.github/workflows/issue-triage.yml`
2. ✅ Comment posted with full analysis
3. ✅ Labels applied: `question`, `P3`
4. ✅ Triage complete

### Verify Workflow Runs

Check triage workflow status:
```bash
# View recent runs
gh run list --workflow=issue-triage.yml --limit 5

# View specific run details
gh run view <run-id> --log
```

### Monitor Performance

Track triage timing:
```bash
# List issues with their creation and first comment time
gh issue list --json number,title,createdAt,comments --jq '.[] | {
  number: .number,
  title: .title,
  created: .createdAt,
  first_comment: .comments[0].createdAt,
  triage_time: ((.comments[0].createdAt | fromdateiso8601) - (.createdAt | fromdateiso8601))
}'
```

---

## 🔧 Troubleshooting

### Issue Not Triaged

**Symptom**: New issue created but no triage comment appears

**Possible causes**:
1. **Workflow hasn't run yet** - Check workflow runs:
   ```bash
   gh run list --workflow=issue-triage.yml --limit 1
   ```

2. **OIDC authentication failed** - Check run logs for token errors:
   ```bash
   gh run view <run-id> --log | grep -i "oidc\|token"
   ```

3. **Permissions insufficient** - Verify workflow has `issues: write`

4. **Concurrency conflict** - Check if another triage is running

### Workflow Fails

**Common errors**:

**Error**: "gh: command not found"
- **Cause**: GitHub CLI not available in runner
- **Fix**: Workflow uses `ubuntu-latest` which includes `gh` by default

**Error**: "403 Forbidden"
- **Cause**: Insufficient permissions
- **Fix**: Add `issues: write` to workflow permissions

**Error**: "OIDC token failed"
- **Cause**: Missing `id-token: write` permission
- **Fix**: Already included in workflow permissions

### Labels Not Applied

**Symptom**: Triage comment posted but labels not applied

**Possible causes**:
1. **Labels don't exist** - Create missing labels in repository settings
2. **Label names mismatch** - Check exact spelling in workflow prompt
3. **Command syntax error** - Verify `gh issue edit` command in Claude's response

**Fix**: Manually apply labels or re-run workflow

### Duplicate/Similar Issues Not Detected

**Symptom**: Claude doesn't find related issues that exist

**Cause**: Search keywords not matching existing issues

**Improvement**: Add more search variations in prompt:
```yaml
# Search with multiple keyword combinations
gh issue list --search "keyword1 OR keyword2 OR keyword3"
```

---

## 📊 Metrics & Insights

### Track Triage Performance

**Average triage time**:
```bash
# Calculate average triage time from last 20 issues
gh issue list --limit 20 --json number,comments --jq '[.[] | select(.comments | length > 0)] | map((.comments[0].createdAt | fromdateiso8601) - (.createdAt | fromdateiso8601)) | add / length'
```

**Triage accuracy** (manual verification):
- Review 10 random triaged issues
- Confirm type classification matches reality
- Verify priority is appropriate
- Check if labels are accurate

**Label distribution**:
```bash
# Count issues by label
gh issue list --json labels --jq '[.[] | .labels[].name] | group_by(.) | map({label: .[0], count: length}) | sort_by(.count) | reverse'
```

### Success Criteria

A healthy auto-triage system shows:
- ✅ 95%+ of issues triaged within 60 seconds
- ✅ 90%+ type classification accuracy
- ✅ 85%+ priority assignment accepted without change
- ✅ 80%+ duplicate detection rate
- ✅ <5% workflow failures

---

## 🚀 Advanced Features

### Multi-Stage Triage

For complex issues, implement staged analysis:

**Stage 1**: Quick classification (30 seconds)
**Stage 2**: Deep analysis if P0/P1 (60 seconds)
**Stage 3**: Component team notification (immediate)

### Integration with Project Boards

Auto-add issues to project boards based on triage:
```yaml
# Add to prompt
9. **Add to project board**: Use `gh project item-add` to add P0/P1 to active sprint board
```

### Team Mentions

Notify specific teams based on component:
```yaml
# Add to prompt
10. **Notify team**:
   - skills issues → @team-skills
   - agents issues → @team-agents
   - templates issues → @team-templates
```

### SLA Tracking

Automatically set due dates based on priority:
```yaml
# Add to prompt
11. **Set milestone**:
   - P0 → Current week milestone
   - P1 → Current sprint milestone
   - P2/P3 → Backlog milestone
```

---

## 📚 References

- **Workflow**: [.github/workflows/issue-triage.yml](workflows/issue-triage.yml)
- **Security Model**: [SECURITY.md](SECURITY.md)
- **Repository Structure**: [../CLAUDE.md](../CLAUDE.md)
- **Claude Code Action**: https://github.com/anthropics/claude-code-action

---

## 🎓 Best Practices

### For Issue Authors

**Help Claude triage accurately**:
- ✅ Use descriptive titles (not "Help!" or "Broken")
- ✅ Include relevant context (skill name, file path, error message)
- ✅ Describe expected vs actual behavior
- ✅ Mention related issues if known
- ✅ Specify which component is affected

### For Repository Maintainers

**Maintain triage quality**:
- 🔄 Review triage accuracy weekly
- 🔄 Adjust prompt based on misclassifications
- 🔄 Keep label list up to date
- 🔄 Monitor workflow failure rate
- 🔄 Provide feedback to improve analysis

### For Contributors

**Leverage triage data**:
- 🔍 Filter by `good-first-issue` for easy wins
- 🔍 Check component labels to find your expertise
- 🔍 Review related issues before starting work
- 🔍 Use priority to understand urgency
- 🔍 Check completeness score before diving in

---

**System Status**: ✅ Active and operational
**Last Updated**: 2025-10-24
**Documentation Version**: 1.0.0

*Auto-triage system implemented as part of the claude-code-skills-factory GitHub automation suite.*
