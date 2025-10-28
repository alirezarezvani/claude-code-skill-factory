# /test-factory - Test Generated Skills or Agents

**Quick testing helper for generated skills and agents to ensure they work correctly.**

---

## Usage

```
/test-factory skill [skill-name]
/test-factory agent [agent-name]
/test-factory prompt
```

---

## What This Command Does

Helps you test generated output:
- Provides test invocation examples
- Checks if skill/agent is loaded
- Suggests test cases
- Validates basic functionality

---

## Test a Skill

```
/test-factory skill my-skill
```

**Output**:
```
Testing: my-skill

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Verify Skill is Loaded

For Claude Desktop:
- Open Skills menu (⌘K or Ctrl+K)
- Search for "my-skill"
- Should appear in list

For Claude Code:
- Skill should be in ~/.claude/skills/my-skill/
- Check: ls ~/.claude/skills/my-skill/

Status: [Checks and reports if found]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 2: Test Invocation

Try these test commands:

**Basic Test**:
```
@my-skill

[Provide test input based on skill's purpose]
```

**Example Use Cases** (from skill documentation):
1. [Use case 1 from HOW_TO_USE.md]
2. [Use case 2 from HOW_TO_USE.md]
3. [Use case 3 from HOW_TO_USE.md]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 3: Verify Output

Expected behavior:
[Description from SKILL.md capabilities]

Test with sample data:
[Show sample_input.json if exists]

Expected output format:
[Show expected_output.json if exists]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Troubleshooting:

If skill doesn't respond:
1. Restart Claude Desktop or Claude Code
2. Verify installation: /install-skill generated-skills/my-skill
3. Check YAML frontmatter: /validate-output skill generated-skills/my-skill

If output is wrong:
1. Check input format matches documentation
2. Review HOW_TO_USE.md for examples
3. Customize SKILL.md if needed
```

---

## Test an Agent

```
/test-factory agent code-reviewer
```

**Output**:
```
Testing: code-reviewer agent

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Verify Agent is Loaded

Run this command:
```
/agents
```

You should see "code-reviewer" in the list of available agents.

Location:
- Project-level: .claude/agents/code-reviewer.md
- User-level: ~/.claude/agents/code-reviewer.md

Status: [Checks and reports]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 2: Test Auto-Invocation

The agent should auto-invoke when you:
[Description from agent's YAML frontmatter]

**Try this task**:
```
[Suggest a task that matches agent description]
```

Claude should automatically delegate to the code-reviewer agent.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 3: Test Manual Invocation

You can also invoke explicitly:
```
Use the code-reviewer agent to review my recent changes
```

This forces Claude to use this specific agent.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 4: Verify Agent Behavior

Expected:
- Agent uses its own context window (separate from main)
- Agent has access to: [Tools from YAML]
- Agent uses model: [Model from YAML]
- Agent returns results to main conversation

Watch for:
- Agent delegation message: "Using code-reviewer agent..."
- Agent completion message
- Results integrated back into main conversation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Troubleshooting:

If agent doesn't invoke:
1. Restart Claude Code
2. Check /agents lists it
3. Make description more specific
4. Try manual invocation

If agent has wrong tools:
1. Edit .claude/agents/code-reviewer.md
2. Update tools: field in YAML
3. Restart Claude Code
```

---

## Test a Prompt

```
/test-factory prompt
```

**Output**:
```
Testing: Generated Mega-Prompt

Since prompts are text (not installed files), here's how to test:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Copy Your Generated Prompt

Format: [XML/Claude/ChatGPT/Gemini]

[Shows preview of generated prompt]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 2: Test in Target LLM

**For Claude**:
1. Open new Claude conversation
2. Paste the prompt at the start
3. Test with a request matching the role

**For ChatGPT**:
1. Settings → Personalization → Custom Instructions
2. Paste sections in correct boxes
3. Start new chat and test

**For Gemini**:
1. Open new Gemini conversation
2. Paste the configuration
3. Test with a request

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 3: Verify Behavior

Test Cases:
1. Simple request: [Example based on role]
2. Complex request: [Example]
3. Edge case: [Example]

Expected:
- AI responds according to defined role
- Follows workflow from prompt
- Uses specified style and format
- Applies best practices mentioned

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Troubleshooting:

If AI doesn't follow prompt:
1. Ensure you pasted the complete prompt
2. Try in a fresh conversation
3. For ChatGPT: Save Custom Instructions first
4. Regenerate with /build prompt if needed
```

---

## Quick Tests

**Fastest way to test**:

**Skills**:
```
@skill-name

Quick test: [Minimal test input]
```

**Agents**:
```
# Just do a task that matches description
# Watch for auto-delegation
```

**Prompts**:
```
# Copy-paste into LLM
# Ask one question matching the role
```

---

## Testing Checklist

### For Skills
- [ ] Skill loads (appears in Skills menu or responds to @skill-name)
- [ ] Accepts input in documented format
- [ ] Produces output in expected format
- [ ] Python code executes without errors (if applicable)
- [ ] Examples from HOW_TO_USE.md work

### For Agents
- [ ] Agent appears in /agents list
- [ ] Auto-invokes when relevant (test with matching task)
- [ ] Manual invocation works
- [ ] Has access to specified tools
- [ ] Operates in separate context (watch delegation messages)

### For Prompts
- [ ] Prompt loads in target LLM
- [ ] AI follows role instructions
- [ ] Uses specified workflow
- [ ] Applies mentioned best practices
- [ ] Output matches expectations

---

## After Testing

**If tests pass** ✅:
```
/factory-status

[Shows your tested output as complete]
```

**If tests fail** ❌:
- Check /validate-output results
- Review installation steps
- Verify Claude restarted
- Check documentation
- Regenerate if needed

---

## Tips

**Best Practices**:
- Test with simple case first
- Then try edge cases
- Document any issues found
- Customize if needed before sharing

**Quick Iteration**:
- Test → Find issues → Edit files → Test again
- Skills: Edit ~/.claude/skills/[name]/SKILL.md
- Agents: Edit .claude/agents/[name].md or ~/.claude/agents/[name].md
- Prompts: Regenerate with /build prompt

---

## Related Commands

- `/build` - Generate outputs
- `/validate-output` - Check format before testing
- `/install-skill` - Install before testing
- `/factory-status` - See tested outputs

---

**Test early, test often!** 🧪
