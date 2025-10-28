# /validate-output - Validate Generated Skills, Prompts, or Agents

**Check that your generated output is properly formatted and ready to use.**

---

## Usage

```
/validate-output skill [path]
/validate-output prompt
/validate-agent [path]
```

---

## What This Command Does

Validates generated output to ensure:
- ✅ YAML frontmatter is correct
- ✅ Naming conventions followed (kebab-case)
- ✅ Required files present
- ✅ Format is proper
- ✅ Quality standards met

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

🎉 Skill validation PASSED! Ready to install.

Next steps:
1. /install-skill generated-skills/my-skill
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

## Quick Validation

**Just ran an agent that generated output?**

```
/validate-output skill
```

Claude will check the most recently generated skill in the conversation.

---

## When to Use

**Use /validate-output**:
- ✅ After generating any skill/prompt/agent
- ✅ Before installing
- ✅ Before sharing with team
- ✅ If something doesn't work as expected
- ✅ To learn proper formatting

**Benefits**:
- Catch formatting errors early
- Learn what makes valid output
- Ensure quality before installation
- Save time debugging

---

## Related Commands

- `/build` - Generate skills/prompts/agents
- `/install-skill` - Install after validation passes
- `/test-factory` - Test installed skills/agents
- `/factory-status` - See all validated outputs

---

**Ensure quality before installation!** ✅
