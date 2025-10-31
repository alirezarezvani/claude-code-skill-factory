# /build - Start Building Skills, Prompts, Agents, or Hooks

**Quick access to the factory-guide orchestrator for building custom Skills, Prompts, Agents, or Hooks.**

---

## Usage

```
/build
/build skill
/build prompt
/build agent
/build hook
```

---

## What This Command Does

**Without arguments** (`/build`):
- Invokes the **factory-guide** orchestrator
- Asks what you want to build (Skill, Prompt, Agent, or Hook)
- Delegates to appropriate specialist
- Guides you through complete process

**With argument** (`/build skill|prompt|agent|hook`):
- Directly delegates to the specialist:
  - `/build skill` → **skills-guide** agent
  - `/build prompt` → **prompts-guide** agent
  - `/build agent` → **agents-guide** agent
  - `/build hook` → **hooks-guide** agent

---

## Examples

### Build Anything (Guided)


```
/build
```

**Output**:
```
Welcome to the Claude Code Skills Factory! 🏭

What would you like to create today?
1. Claude Skill (multi-file capability)
2. Mega-Prompt (for any LLM)
3. Claude Agent (workflow specialist)
4. Claude Hook (workflow automation)

Enter 1, 2, 3, or 4: ___
```

---

### Build a Skill (Direct)

```
/build skill
```

**Output**:
```
Let's build your custom Claude Skill! I'll ask you 4-5 straightforward questions.

Question 1: What's your business type or domain?
Examples: FinTech, Healthcare, E-commerce, SaaS

Your answer: ___
```

→ Continues with skills-guide agent's question flow
→ Generates complete skill folder + ZIP

---

### Build a Prompt (Direct)

```
/build prompt
```

**Output**:
```
I'll help you generate a mega-prompt using the prompt-factory skill.

Quick-Start Preset (30 seconds) or Custom Prompt (2 minutes)?

Choice: ___
```

→ Continues with prompts-guide agent
→ Generates production-ready prompt

---

### Build an Agent (Direct)

```
/build agent
```

**Output**:
```
Let's build your custom Claude Code Agent!

Question 1: What should this agent do?

Examples:
- Review code for security vulnerabilities
- Build React components
- Run tests and analyze failures

Your agent's purpose: ___
```

→ Continues with agents-guide agent
→ Generates agent .md file

---

### Build a Hook (Direct)

```
/build hook
```

**Output**:
```
Let's build your custom Claude Code Hook!

Question 1: What should this hook do?

Examples:
- Auto-format code after editing
- Run tests when agent completes
- Send notifications
- Auto-stage files with git

Your hook's purpose: ___
```

→ Continues with hooks-guide agent's question flow
→ Generates hook.json + README.md with validation

---

## What Happens Next

### After Running /build

**The orchestrator or specialist will**:
1. Ask you straightforward questions (3-11 total depending on path)
2. Generate complete output (skill/prompt/agent/hook)
3. Validate format and quality
4. Create all necessary files
5. Provide installation instructions
6. Give testing guidance

**You'll get**:
- Complete, working output
- Validated format (YAML, naming, structure)
- Installation help
- Usage examples

---

## Related Commands

**After building**:
- `/validate-output skill|hook` - Check format and quality
- `/install-skill path/to/skill` - Install generated skill
- `/install-hook path/to/hook` - Install generated hook
- `/test-factory skill-name` - Test it works
- `/factory-status` - See what you've built

---

## Common Workflows

### Build → Validate → Install → Test

```
# 1. Build
/build skill

[Answer questions, skill generated]

# 2. Validate
/validate-output skill

# 3. Install
/install-skill generated-skills/my-skill

# 4. Test
/test-factory my-skill

# 5. Check status
/factory-status
```

---

## Tips

**For faster workflow**:
- Use `/build skill|prompt|agent|hook` to skip the "what to build" question
- Be specific in your initial request
- Answer questions with examples when helpful

**If unsure**:
- Just use `/build` and let factory-guide guide you
- The agents will ask clarifying questions
- You can always regenerate or customize

---

**The simplest way to start building custom Skills, Prompts, Agents, and Hooks!** 🚀
