# /factory-status - Check Factory Build Progress

**See what you've built, what's validated, what's installed, and what's next.**

---

## Usage

```
/factory-status
```

---

## What This Command Does

Shows comprehensive status of your factory work:
- Skills generated (in generated-skills/)
- Agents created (in .claude/agents/ or ~/.claude/agents/)
- Hooks generated (in generated-hooks/)
- Prompts generated (in conversation)
- Validation status
- Installation status
- Next recommended steps

---

## Example Output

```
/factory-status
```

**Output**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Factory Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Claude Skills Generated (2)

1. healthcare-analyzer/
   Location: generated-skills/healthcare-analyzer/
   Size: 45KB (SKILL.md + 3 Python files)
   Status: ✅ Validated ✅ Installed ⏳ Not tested yet
   Next: /test-factory skill healthcare-analyzer

2. financial-reports/
   Location: generated-skills/financial-reports/
   Size: 32KB (SKILL.md + 2 Python files)
   Status: ✅ Validated ❌ Not installed yet
   Next: /install-skill generated-skills/financial-reports

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 Claude Agents Created (1)

1. code-reviewer
   Location: .claude/agents/code-reviewer.md
   Size: 8KB
   Status: ✅ Validated ✅ Active (project-level)
   Next: Test with: "Review my recent code changes"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 Claude Hooks Generated (3)

1. auto-format-python
   Location: generated-hooks/auto-format-python/
   Event Type: PostToolUse
   Language: Python (Black formatter)
   Status: ✅ Validated ✅ Installed (user-level)
   Next: Test by editing a .py file

2. test-runner-js
   Location: generated-hooks/test-runner-js/
   Event Type: SubagentStop
   Language: JavaScript (Jest)
   Status: ✅ Validated ⏳ Not installed yet
   Next: /install-hook generated-hooks/test-runner-js

3. git-auto-add
   Location: generated-hooks/git-auto-add/
   Event Type: PostToolUse
   Language: Generic (Git)
   Status: ⏳ Not validated yet
   Next: /validate-output hook generated-hooks/git-auto-add

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Mega-Prompts Generated (1)

1. Senior Backend Engineer Prompt
   Format: XML + Claude formats
   Size: ~5,200 tokens
   Status: ✅ Generated ⏳ Not tested yet
   Next: Copy to Claude.ai and test

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Summary

Total Generated: 7 outputs (2 skills, 1 agent, 3 hooks, 1 prompt)
Validated: 5/7 (71%)
Installed: 3/7 (43%)
Tested: 0/7 (0%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Recommended Next Steps

1. Validate git-auto-add hook:
   /validate-output hook generated-hooks/git-auto-add

2. Install test-runner-js hook:
   /install-hook generated-hooks/test-runner-js

3. Install financial-reports skill:
   /install-skill generated-skills/financial-reports

4. Test healthcare-analyzer skill:
   /test-factory skill healthcare-analyzer

5. Test auto-format-python hook:
   Edit a .py file and check if Black runs

6. Test Senior Backend Engineer prompt:
   Copy to Claude.ai and try a test request

7. Test code-reviewer agent:
   Make some code changes and see if it auto-invokes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Need help?
- Build more: /build skill|prompt|agent|hook
- Validate: /validate-output [type] [path]
- Install: /install-skill [path] or /install-hook [path]
- Test: /test-factory [type] [name]
```

---

## Detection Logic

The command scans:

**For Skills**:
```bash
# Check generated-skills/ directory
ls generated-skills/*/SKILL.md

# Check if installed
ls ~/.claude/skills/*/SKILL.md
```

**For Agents**:
```bash
# Check project-level
ls .claude/agents/*.md

# Check user-level
ls ~/.claude/agents/*.md
```

**For Prompts**:
- Analyzes recent conversation
- Looks for generated prompts (XML, Claude, ChatGPT, Gemini formats)
- Checks token count announcements

**For Hooks**:
```bash
# Check generated-hooks/ directory
ls generated-hooks/*/hook.json

# Check if installed (user-level)
grep -r "hook.json" ~/.claude/settings.json

# Check if installed (project-level)
grep -r "hook.json" .claude/settings.json
```

---

## Status Indicators

**Validation Status**:
- ✅ Validated - Passed /validate-output checks
- ⏳ Not validated - Run /validate-output
- ❌ Issues found - Fix validation errors

**Installation Status**:
- ✅ Installed - Found in ~/.claude/skills/ or .claude/agents/
- ⏳ Not installed - Run /install-skill
- ❌ Not found - Check installation path

**Testing Status**:
- ✅ Tested - User has tested functionality
- ⏳ Not tested - Run /test-factory
- ❌ Test failed - Review and fix issues

---

## Empty State

```
/factory-status
```

**If nothing generated yet**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Factory Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

No skills, prompts, agents, or hooks generated yet.

Ready to start building?

Quick start:
/build

Or be specific:
/build skill     - Build a custom Claude Skill
/build prompt    - Generate a mega-prompt
/build agent     - Create a Claude Code Agent
/build hook      - Create a Claude Code Hook

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Progress Tracking

The command helps you track:
- **What's complete**: Generated, validated, installed, tested
- **What's pending**: Needs validation, installation, or testing
- **What's next**: Clear action items
- **Overall progress**: Percentage complete

---

## Use Cases

### Check After Building

```
# Generate something
/build skill
[Answer questions]
[Skill generated]

# Check status
/factory-status

Output:
✅ 1 skill generated
⏳ Not validated yet
Next: /validate-output skill generated-skills/my-skill
```

### Track Session Progress

```
# At any time
/factory-status

See:
- Everything built this session
- What still needs attention
- Recommended next actions
```

### Before Ending Session

```
# Before you finish
/factory-status

Ensure:
- All outputs validated ✅
- All outputs installed ✅
- All outputs tested ✅
- Ready to use in production
```

---

## Example Session

```
User: /build skill
[Generates healthcare-analyzer]

User: /factory-status
Output: 1 skill, not validated

User: /validate-output skill generated-skills/healthcare-analyzer
Output: ✅ Validation passed

User: /factory-status
Output: 1 skill, validated, not installed

User: /install-skill generated-skills/healthcare-analyzer
[Installation complete]

User: /factory-status
Output: 1 skill, validated, installed, not tested

User: /test-factory skill healthcare-analyzer
[Testing successful]

User: /factory-status
Output: 1 skill, ✅ complete (validated, installed, tested)
```

---

## Tips

**Use /factory-status to**:
- Track what you've built
- See what needs attention
- Get next-step recommendations
- Verify completeness before sharing

**Run it**:
- After each /build
- Before /install-skill
- After testing
- Before ending session

---

## Related Commands

- `/build` - Generate skills/prompts/agents/hooks
- `/validate-output` - Check quality
- `/install-skill` - Install skills
- `/install-hook` - Install hooks
- `/test-factory` - Test functionality

---

**Track your progress from start to finish!** 📊
