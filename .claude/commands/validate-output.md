# /validate-output - Validate Generated Skills, Prompts, Agents, or Hooks

**Check that your generated output is properly formatted and ready to use.**

---

## Usage

```
/validate-output skill [path]
/validate-output prompt
/validate-agent [path]
/validate-output hook [path]
```

---

## What This Command Does

Validates generated output and creates distribution files:
- ✅ YAML frontmatter is correct
- ✅ Naming conventions followed (kebab-case)
- ✅ Required files present
- ✅ Format is proper
- ✅ Quality standards met
- ✅ **Creates ZIP file** (if validation passes for skills)

---

## Validate a Skill

```
/validate-output skill generated-skills/my-skill
```

**Checks**:

1. **YAML Frontmatter**:
```yaml
---
name: skill-name-kebab-case  ✅ Check format
description: One-line description  ✅ Check present
---
```

2. **Naming**:
- ✅ Skill name is kebab-case (not Title Case, snake_case, camelCase)
- ✅ Folder name matches skill name
- ✅ Python files are snake_case (if present)

3. **Required Files**:
- ✅ SKILL.md exists
- ✅ HOW_TO_USE.md exists (or usage instructions in SKILL.md)
- ✅ Python files (if skill needs code)
- ✅ sample_input.json and expected_output.json (if applicable)

4. **Quality**:
- ✅ SKILL.md has clear capabilities section
- ✅ Input/output formats documented
- ✅ Examples provided
- ✅ No placeholder text

**Output**:
```
Validating: generated-skills/my-skill/

✅ YAML Frontmatter: Valid
✅ Skill Name: my-skill (kebab-case ✓)
✅ Required Files: All present
   - SKILL.md ✓
   - HOW_TO_USE.md ✓
   - calculator.py ✓
   - sample_input.json ✓
✅ Quality: Documentation complete

🎉 Skill validation PASSED!

Creating ZIP file for Claude Desktop...

cd generated-skills && zip -r my-skill.zip my-skill/ -x "*.pyc" "*__pycache__*" "*.DS_Store"

✅ ZIP created: generated-skills/my-skill.zip (35KB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Ready to use!

**For Claude Desktop** (Easiest):
Drag and drop: generated-skills/my-skill.zip

**For Claude Code**:
/install-skill generated-skills/my-skill

Next steps:
1. Import ZIP to Claude Desktop OR install to Claude Code
2. /test-factory my-skill
```

**If Issues Found**:
```
Validating: generated-skills/bad-skill/

❌ YAML Frontmatter: Invalid
   Issue: Name is "Bad Skill" (Title Case)
   Fix: Change to "bad-skill" (kebab-case)

❌ Required Files: Missing
   Issue: HOW_TO_USE.md not found
   Fix: Add usage documentation

⚠️ Quality: Incomplete
   Issue: No examples in SKILL.md
   Recommendation: Add 2-3 usage examples

Validation FAILED. Fix issues and run /validate-output again.
```

---

## Validate a Prompt

```
/validate-output prompt
```

**Checks**:

1. **Format Structure**:
- ✅ XML: Has `<mega_prompt>` tags, properly nested
- ✅ Claude: Has clear sections (Role, Mission, Workflow, etc.)
- ✅ ChatGPT: Has both required sections
- ✅ Gemini: Has role configuration

2. **Completeness**:
- ✅ No placeholder text ([TODO], [FILL IN], etc.)
- ✅ All sections have content
- ✅ Examples included (at least 2)

3. **Quality** (from prompt-factory's 7-point validation):
- ✅ Token count reasonable (3-6K Core, 8-12K Advanced)
- ✅ Actionable workflow present
- ✅ Best practices mentioned
- ✅ Clear role and mission

**Output**:
```
Validating generated prompt...

✅ Format: XML (properly structured)
✅ Completeness: No placeholders
✅ Examples: 3 examples found
✅ Token Count: ~5,200 tokens (Core mode, optimal)
✅ Quality: 7/7 gates passed

🎉 Prompt validation PASSED! Ready to use.

How to use:
1. Copy the <mega_prompt> block
2. Paste into Claude/ChatGPT/Gemini
3. Start using your customized AI!
```

---

## Validate an Agent

```
/validate-agent .claude/agents/my-agent
```

**Checks**:

1. **YAML Frontmatter**:
```yaml
---
name: agent-name-kebab-case  ✅
description: When to invoke...  ✅
tools: Read, Write, Edit  ✅ Comma-separated string
model: sonnet  ✅ Valid value
color: green  ✅ Valid color
field: frontend  ✅ Domain
expertise: expert  ✅ Level
---
```

2. **Naming**:
- ✅ Agent name is kebab-case
- ✅ File name matches agent name
- ✅ No special characters

3. **Tools Format**:
- ✅ Comma-separated string (not array)
- ✅ Valid tool names
- ✅ Appropriate for agent type

4. **Description Quality**:
- ✅ Describes WHEN to invoke (not just what it does)
- ✅ Specific enough for auto-discovery
- ✅ Clear and actionable

**Output**:
```
Validating: .claude/agents/my-agent.md

✅ YAML Frontmatter: Valid
✅ Agent Name: my-agent (kebab-case ✓)
✅ Tools: "Read, Write, Edit" (proper format ✓)
✅ Model: sonnet (valid ✓)
✅ Color: green (valid ✓)
✅ Description: Specific and clear ✓

🎉 Agent validation PASSED! Ready to use.

The agent will auto-invoke when:
[Description from agent]

Or invoke manually:
"Use the my-agent agent to [task]"
```

---

## Validate a Hook

```
/validate-output hook generated-hooks/my-hook
```

**Checks**:

1. **JSON Structure**:
```json
{
  "matcher": { ... },  ✅ Valid object
  "hooks": [ ... ]     ✅ Non-empty array
}
```

2. **Safety Patterns**:
- ✅ Tool detection present (`command -v tool`)
- ✅ Silent failure mode (`|| exit 0`)
- ✅ No destructive operations (no `rm -rf`, `git push --force`)
- ✅ File path validation (quoted paths, no `..`)

3. **Event Type Validation**:
- ✅ Appropriate timeout for event type
- ✅ Matcher appropriate for event (empty for SessionStart, SubagentStop)
- ✅ Command complexity matches event timing

4. **Hook Commands**:
- ✅ No path traversal attempts
- ✅ External tools have detection wrappers
- ✅ Error handling present
- ✅ Commands are safe (no dangerous patterns)

**Output**:
```
Validating: generated-hooks/my-hook/hook.json

✅ JSON Structure: Valid
   - matcher object: ✓
   - hooks array: 1 command ✓
✅ Safety Patterns: All present
   - Tool detection: ✓
   - Silent failure: ✓
   - No destructive ops: ✓
   - Path safety: ✓
✅ Event Type: PostToolUse
   - Timeout: 60s (appropriate ✓)
   - Matcher: tool_names + paths ✓
✅ Security: PASSED
   - No path traversal ✓
   - Proper quoting ✓
   - Error handling ✓

🎉 Hook validation PASSED!

Security Score: 5/5
━━━━━━━━━━━━━━━━━━━━
✅ Tool detection present
✅ Silent failure mode
✅ No destructive operations
✅ Path safety validated
✅ Error handling complete

Next steps:
1. /install-hook generated-hooks/my-hook
2. Restart Claude Code
3. Test by triggering the hook event
```

**Validation using hook-factory validator**:
```bash
python3 generated-skills/hook-factory/validator.py generated-hooks/my-hook/hook.json
```

**If Issues Found**:
```
Validating: generated-hooks/bad-hook/hook.json

❌ JSON Structure: Invalid
   Issue: "matcher" is string, should be object
   Fix: Change to {"tool_names": ["Write"]}

❌ Safety Patterns: Missing
   Issue: No tool detection for "black" command
   Fix: Add "command -v black" check

❌ Security: FAILED
   Issue: Path traversal detected (..)
   Fix: Remove ".." from file paths

⚠️ Event Type: Mismatched
   Issue: SubagentStop with tool_names matcher
   Fix: SubagentStop should have empty matcher {}

Validation FAILED. Fix issues and run /validate-output again.
```

---

## Quick Validation

**Just ran an agent that generated output?**

```
/validate-output skill
```

Claude will check the most recently generated skill in the conversation.

---

## When to Use

**Use /validate-output**:
- ✅ After generating any skill/prompt/agent/hook
- ✅ Before installing
- ✅ Before sharing with team
- ✅ If something doesn't work as expected
- ✅ To learn proper formatting
- ✅ For hooks: CRITICAL before installation (security check)

**Benefits**:
- Catch formatting errors early
- Learn what makes valid output
- Ensure quality before installation
- Save time debugging

---

## Related Commands

- `/build` - Generate skills/prompts/agents/hooks
- `/install-skill` - Install skills after validation passes
- `/install-hook` - Install hooks after validation passes
- `/test-factory` - Test installed skills/agents
- `/factory-status` - See all validated outputs

---

**Ensure quality before installation!** ✅
