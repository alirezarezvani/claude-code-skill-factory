# Factory Slash Commands

**5 essential commands for building Skills, Prompts, and Agents from start to finish.**

---

## 🎯 Complete Workflow Commands

```
/build              → Start building (invoke orchestrator)
/validate-output    → Check quality
/install-skill      → Install outputs
/test-factory       → Test functionality
/factory-status     → Track progress
```

---

## 📋 The 5 Commands

### 1. /build - Start Building

**Purpose**: Main entry point - invoke factory-guide orchestrator or specialists

**Usage**:
```
/build                 # Ask what to build
/build skill           # Directly invoke skills-guide
/build prompt          # Directly invoke prompts-guide
/build agent           # Directly invoke agents-guide
```

**What happens**:
- Invokes appropriate navigation agent
- Guides through Q&A (3-11 questions)
- Generates complete output
- Validates and helps install

**When to use**: Start of any factory workflow

---

### 2. /validate-output - Quality Check

**Purpose**: Validate generated skills/prompts/agents

**Usage**:
```
/validate-output skill [path]      # Check skill format
/validate-output prompt            # Check prompt quality
/validate-agent [path]             # Check agent format
```

**What it checks**:
- ✅ YAML frontmatter validity
- ✅ Naming conventions (kebab-case)
- ✅ Required files present
- ✅ Format correctness
- ✅ Quality standards

**When to use**: After generation, before installation

---

### 3. /install-skill - Installation Helper

**Purpose**: Step-by-step installation guidance

**Usage**:
```
/install-skill [path-to-skill]     # Install skill
/install-skill [path-to-agent]     # Install agent (works for both)
```

**What it provides**:
- Multiple installation options (Desktop, Code, Browser)
- Detailed commands for each method
- Verification steps
- Troubleshooting help

**When to use**: After validation passes

---

### 4. /test-factory - Quick Test

**Purpose**: Test generated outputs work correctly

**Usage**:
```
/test-factory skill [skill-name]   # Test skill
/test-factory agent [agent-name]   # Test agent
/test-factory prompt               # Test prompt
```

**What it provides**:
- Test invocation examples
- Expected behavior description
- Verification checklist
- Troubleshooting steps

**When to use**: After installation

---

### 5. /factory-status - Progress Check

**Purpose**: Track what's built, validated, installed, tested

**Usage**:
```
/factory-status
```

**What it shows**:
- All skills generated (with status)
- All agents created (with status)
- All prompts generated (with status)
- Overall progress (%)
- Next recommended actions

**When to use**: Anytime to see progress

---

## 🔄 Complete Workflow

### Start to Finish

```
# 1. Start
/build

Choose: 1 (Skill)
[Answer 4-5 questions]
→ Skill generated

# 2. Validate
/validate-output skill generated-skills/my-skill
→ ✅ Validation passed

# 3. Install
/install-skill generated-skills/my-skill
Choose: Option 2 (Claude Code)
→ Installed to ~/.claude/skills/my-skill/

# 4. Test
/test-factory skill my-skill
→ Test examples provided, verified working

# 5. Check Complete
/factory-status
→ Shows: 1 skill (✅ validated, ✅ installed, ✅ tested)
```

**Total time**: 10-15 minutes from idea to working skill!

---

## 💡 Command Combinations

### Quick Build (Experienced Users)

```
/build skill
[Answer questions]
/validate-output skill generated-skills/[name]
/install-skill generated-skills/[name]
/test-factory skill [name]
```

### Check Then Continue

```
/factory-status
[See what needs attention]
/validate-output skill [pending-skill]
/install-skill [validated-skill]
```

### Verify Before Sharing

```
/factory-status
[Ensure all outputs: validated ✅, installed ✅, tested ✅]
```

---

## 🎯 Use Cases

### New User - First Skill

```
User: "I want to build my first skill"

Commands:
1. /build skill
2. [Answer questions]
3. /validate-output skill generated-skills/[name]
4. /install-skill generated-skills/[name]
5. /test-factory skill [name]
6. /factory-status (verify complete)

Result: Complete, tested skill ready to use
```

### Experienced User - Batch Creation

```
User: "Need to create 3 skills for my project"

Commands:
# Build all 3
/build skill  # Skill 1
/build skill  # Skill 2
/build skill  # Skill 3

# Validate all
/validate-output skill generated-skills/skill-1
/validate-output skill generated-skills/skill-2
/validate-output skill generated-skills/skill-3

# Check progress
/factory-status

# Install all
/install-skill generated-skills/skill-1
/install-skill generated-skills/skill-2
/install-skill generated-skills/skill-3

# Verify
/factory-status
```

### Healthcare Developer

```
User: "Build healthcare skills for my mental health app"

Commands:
1. /build skill
   [Create: medical-terminology-translator]

2. /validate-output skill generated-skills/medical-terminology-translator

3. /install-skill generated-skills/medical-terminology-translator

4. /build skill
   [Create: therapy-session-tracker]

5. /factory-status
   [See both skills, track progress]
```

---

## 📊 Command Reference

| Command | Purpose | Input Required | Output |
|---------|---------|----------------|--------|
| **/build** | Start building | Optional: type | Invokes agent |
| **/validate-output** | Check quality | Type + path | Validation report |
| **/install-skill** | Install output | Path | Installation guide |
| **/test-factory** | Test output | Type + name | Test instructions |
| **/factory-status** | Show progress | None | Status report |

---

## 🚀 Quick Start

**First time?**

```
/build
```

**Know what you want?**

```
/build skill
/build prompt
/build agent
```

**After generation**:

```
/validate-output [type] [path]
/install-skill [path]
/test-factory [type] [name]
/factory-status
```

---

## 💡 Tips

**For best results**:
- Always validate before installing
- Test after installing
- Check /factory-status to track progress
- Use /build arguments for faster workflow

**If stuck**:
- Run /factory-status to see where you are
- Re-run validation if issues
- Use /build to start fresh

**Before sharing**:
- Ensure all outputs validated ✅
- Test everything works ✅
- Run /factory-status to verify complete

---

## 🔗 Integration with Agents

**Commands work with**:
- factory-guide (orchestrator)
- skills-guide (Skills specialist)
- prompts-guide (Prompts specialist)
- agents-guide (Agents specialist)

**Commands enhance**:
- Quick access (/build vs invoking agents manually)
- Progress tracking (/factory-status)
- Quality assurance (/validate-output)
- Installation help (/install-skill)
- Testing guidance (/test-factory)

---

## 📍 File Locations

**Commands**:
```
.claude/commands/build.md
.claude/commands/validate-output.md
.claude/commands/install-skill.md
.claude/commands/test-factory.md
.claude/commands/factory-status.md
.claude/commands/README.md (this file)
```

**Agents** (work with commands):
```
.claude/agents/factory-guide.md
.claude/agents/skills-guide.md
.claude/agents/prompts-guide.md
.claude/agents/agents-guide.md
```

---

## ✅ Complete Navigation System

**Agents** (Interactive guides):
- factory-guide (orchestrator)
- 3 specialists (skills, prompts, agents)

**Commands** (Quick access):
- /build (start)
- /validate-output (check)
- /install-skill (install)
- /test-factory (test)
- /factory-status (track)

**Together**: Complete start-to-finish workflow for building custom Skills, Prompts, and Agents!

---

---

## 🧭 Git & Governance Commands

| Command | Purpose |
|---------|---------|
| **/ci-guard** | Trigger commit/branch guard workflow |
| **/review** | Run local review checks + CI visibility |
| **/security-scan** | Run local security checks + workflow |
| **/run-release** | Launch release orchestrator workflow |
| **/sync-branch** | Rebase feature branch onto main |
| **/sync-todos-to-github** | Convert TodoWrite tasks to GitHub plan issue |

### Git Helpers (`.claude/commands/git/`)

| Command | Description |
|---------|-------------|
| **git/cm** | Stage & commit (no push) |
| **git/cp** | Stage, commit, push |
| **git/pr** | Create pull request |
| **git/rv** | Local review gate |
| **git/sc** | Local security gate |

Always run git helpers before triggering slash commands to surface results in CI and GitHub checks.

---

**Last Updated**: October 31, 2025
**Version**: 1.1.0
**Status**: ✅ Ready to use

**Build amazing Skills, Prompts, Agents, and stay release-ready with simple commands!** 🏭
