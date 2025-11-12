# Generated Agents

Specialized Claude Code agents created for specific workflows and background tasks. These agents work independently to automate maintenance and coordination tasks.

---

## 🤖 Available Agents

### 1. claude-md-guardian

**Purpose**: Background maintenance agent that keeps CLAUDE.md files synchronized with project changes

**Type**: Documentation / Coordination Agent
**Model**: haiku (token-efficient)
**Color**: purple
**Expertise**: intermediate

**Features**:
- 🔄 **Auto-Sync**: Updates CLAUDE.md based on detected changes
- 🎯 **Smart Detection**: Only updates when significant changes occur (git diff analysis)
- ⚡ **Token-Efficient**: Uses haiku model for routine updates
- 🔇 **Silent Operation**: No interruptions during active development
- 📦 **Milestone-Aware**: Triggers after feature completion, refactoring, etc.
- ✨ **Native Format**: Ensures 100% Claude Code format compliance

**When Invoked**:
- **Automatically** (with SessionStart hook): Beginning of each session
- **Manually**: After major milestones (feature completion, refactoring, new dependencies, architecture changes)
- **Via Command**: `/enhance-claude-md` can invoke this agent

**What It Does**:
1. Detects changes via git diff (dependencies, structure, configuration)
2. Determines update necessity (skips minor changes)
3. Invokes `claude-md-enhancer` skill for targeted updates
4. Reports changes concisely

**Output Example**:
```
✅ CLAUDE.md updated:
- Tech Stack: Added 2 dependencies
- Project Structure: Updated diagram
- Setup: New environment variable

Changes: 3 sections modified, 12 lines changed
```

**Documentation**: [claude-md-guardian/README.md](claude-md-guardian/README.md)

**Related Components**:
- **Skill**: [claude-md-enhancer](../generated-skills/claude-md-enhancer/) - Core capability
- **Slash Command**: [/enhance-claude-md](../generated-commands/enhance-claude-md/) - Manual invocation

**Installation**:
```bash
# User-level (all projects)
cp generated-agents/claude-md-guardian/claude-md-guardian.md ~/.claude/agents/

# Project-level (current project)
cp generated-agents/claude-md-guardian/claude-md-guardian.md .claude/agents/

# Restart Claude Code
```

---

## 🚀 Installation

### User-Level (Recommended)

Available in all your Claude Code projects:

```bash
# Copy agent to user directory
cp generated-agents/[agent-name]/[agent-name].md ~/.claude/agents/

# Restart Claude Code
```

### Project-Level

Available only in current project:

```bash
# Create agents directory
mkdir -p .claude/agents

# Copy agent
cp generated-agents/[agent-name]/[agent-name].md .claude/agents/

# Restart Claude Code
```

---

## 📁 Agent Structure

Each agent folder contains:

```
agent-name/
├── agent-name.md        # Agent definition with enhanced YAML frontmatter
└── README.md            # Installation guide and documentation
```

**Required YAML Fields**:
- `name`: kebab-case agent name
- `description`: Clear description of agent purpose and invocation triggers
- `tools`: Tool access list (Bash, Read, Write, Edit, Grep, Glob, Skill, etc.)
- `model`: haiku (efficient) / sonnet (complex) / opus (advanced)
- `color`: blue (strategic) / green (implementation) / red (quality) / purple (coordination)
- `field`: Domain area (documentation, development, testing, etc.)
- `expertise`: beginner / intermediate / advanced / expert
- `mcp_tools`: MCP tool requirements (none, playwright, context7, etc.)

---

## 🛠️ Creating New Agents

Use the **Agent Factory** skill to generate new agents:

1. **Use the factory skill**:
   ```bash
   # Ensure agent-factory skill is installed
   cp -r generated-skills/agent-factory ~/.claude/skills/

   # Ask Claude
   "I need an agent for [task description]"
   ```

2. **Follow the Q&A workflow**:
   - Agent purpose and naming
   - Tool access requirements
   - Model selection (haiku/sonnet/opus)
   - Field and expertise level
   - Invocation triggers

3. **Output location**: Agents should be placed in `generated-agents/[agent-name]/`

**Template**: [../documentation/templates/AGENTS_FACTORY_PROMPT.md](../documentation/templates/AGENTS_FACTORY_PROMPT.md)

**Skill**: [../generated-skills/agent-factory/](../generated-skills/agent-factory/)

---

## 🎨 Agent Types

### Strategic Agents (Blue)
- Planning and research
- Lightweight tools (Read, Write, Grep only)
- No code execution
- Example: Planning agents, analysis agents

### Implementation Agents (Green)
- Code writing and modification
- Full tool access including Bash
- Build features and implement solutions
- Example: Frontend, backend, fullstack engineers

### Quality Agents (Red)
- Testing and validation
- Heavy Bash usage (test runners)
- Sequential execution only
- Example: QA leads, test runners, security engineers

### Coordination Agents (Purple)
- Orchestration and management
- Lightweight, manages other agents
- Background operation
- Example: **claude-md-guardian**, project managers

---

## 📖 Best Practices

### Agent Design
1. **Single Responsibility**: Each agent should have one clear purpose
2. **Background Operation**: Don't interrupt other agents
3. **Token Efficiency**: Use haiku for routine tasks, escalate when needed
4. **Smart Triggers**: Only activate when actually needed
5. **Concise Output**: Report what changed, not full content

### Tool Access
1. **Strategic**: Read, Write, Edit, Grep, Glob only
2. **Implementation**: Add Bash for code execution
3. **Quality**: Heavy Bash, sequential only
4. **Coordination**: Minimal tools + Skill invocation

### Model Selection
- **haiku**: Routine tasks, background maintenance, simple coordination
- **sonnet**: Complex implementation, multi-step workflows
- **opus**: Advanced reasoning, strategic planning, research

---

## 🔗 Related Resources

- **Factory Skill**: [../generated-skills/agent-factory/](../generated-skills/agent-factory/)
- **Templates**: [../documentation/templates/AGENTS_FACTORY_PROMPT.md](../documentation/templates/AGENTS_FACTORY_PROMPT.md)
- **Official Guide**: [../documentation/references/claude-agents-instructions.md](../documentation/references/claude-agents-instructions.md)
- **Project Guide**: [../CLAUDE.md](../CLAUDE.md)

---

**Version**: 1.0.0
**Last Updated**: November 2025
**Total Agents**: 1 (claude-md-guardian)
