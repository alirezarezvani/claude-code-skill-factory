---
name: agent-factory
description: Claude Code agent generation system that creates custom agents and sub-agents with enhanced YAML frontmatter, tool access patterns, and MCP integration support following proven production patterns
---

# Agent Factory

A comprehensive system for generating production-ready Claude Code agents and sub-agents. This skill provides templates, standards, and generation tools to create custom agents that seamlessly integrate with Claude Code's agent system.

## What This Skill Does

This skill helps you create custom Claude Code agents for any domain or workflow. It generates properly formatted agent files that Claude Code can automatically discover and invoke when relevant.

### Capabilities

1. **Generate Custom Agents** - Create specialized agents for any domain (frontend, backend, testing, product, etc.)
2. **Enhanced YAML Frontmatter** - Rich metadata including color coding, field categorization, expertise levels
3. **Tool Access Guidance** - Recommends optimal tool configurations based on agent type
4. **MCP Integration** - Suggests relevant MCP server tools for enhanced capabilities
5. **Execution Pattern Assignment** - Ensures proper parallel/sequential execution for safety
6. **Validation** - Checks agent configuration against best practices

## Agent Types Supported

### Strategic Agents (Lightweight, Parallel-Safe)
- **Purpose**: Planning, research, analysis
- **Tools**: Read, Write, Grep only
- **Execution**: 4-5 agents can run in parallel
- **Color**: Blue
- **Examples**: product-planner, market-researcher, architect

### Implementation Agents (Full Tools, Coordinated)
- **Purpose**: Code writing, feature building
- **Tools**: Read, Write, Edit, Bash, Grep, Glob
- **Execution**: 2-3 agents coordinated
- **Color**: Green
- **Examples**: frontend-developer, backend-developer, api-builder

### Quality Agents (Heavy Bash, Sequential Only)
- **Purpose**: Testing, validation, review
- **Tools**: Read, Write, Edit, Bash, Grep, Glob
- **Execution**: 1 agent at a time (NEVER parallel)
- **Color**: Red
- **Examples**: test-runner, code-reviewer, security-auditor

### Coordination Agents (Lightweight, Orchestration)
- **Purpose**: Manages other agents, validates integration
- **Tools**: Read, Write, Grep
- **Execution**: Orchestrates others
- **Color**: Purple
- **Examples**: fullstack-coordinator, workflow-manager

## Enhanced YAML Frontmatter

Every generated agent includes rich metadata:

```yaml
---
name: agent-name-kebab-case
description: When to invoke this agent
tools: Read, Write, Edit  # Comma-separated
model: sonnet  # sonnet|opus|haiku|inherit
color: green  # Visual categorization
field: frontend  # Domain area
expertise: expert  # beginner|intermediate|expert
mcp_tools: mcp__playwright  # MCP integrations
---
```

### Field Categories

**Development**: `frontend`, `backend`, `fullstack`, `mobile`, `devops`
**Quality**: `testing`, `security`, `performance`
**Strategic**: `product`, `architecture`, `research`, `design`
**Domain**: `data`, `ai`, `content`, `finance`, `infrastructure`

### Color Coding

- **Blue**: Strategic/planning agents
- **Green**: Implementation/development agents
- **Red**: Quality/testing agents
- **Purple**: Coordination/orchestration agents
- **Orange**: Domain-specific specialists

### Expertise Levels

- **Beginner**: Simple, focused tasks
- **Intermediate**: Moderate complexity workflows
- **Expert**: Advanced, complex operations

## How to Use

### Quick Start

1. **Open the prompt template**: [documentation/templates/AGENTS_FACTORY_PROMPT.md](../../documentation/templates/AGENTS_FACTORY_PROMPT.md)
2. **Scroll to bottom** - Find template variables
3. **Fill in your details**:
   ```
   AGENT_NAME: my-custom-agent
   DESCRIPTION: What this agent does and when to invoke it
   DOMAIN_FIELD: frontend
   TOOLS_NEEDED: Read, Write, Edit, Bash
   ```
4. **Copy entire prompt** - Include filled variables
5. **Paste into Claude** - Claude.ai, Claude Code, or API
6. **Receive agent file** - Complete .md file ready to use
7. **Install agent** - Copy to `.claude/agents/` or `~/.claude/agents/`

### Example Invocation

```
@agent-factory

Create a custom agent:
Name: api-integration-specialist
Type: Implementation
Domain: backend
Description: API integration expert for third-party services
Capabilities: OAuth, REST clients, error handling
Tools: Read, Write, Edit, Bash
MCP: mcp__github
```

**Output**: Complete `.claude/agents/api-integration-specialist.md` file

## Generated Agent Structure

Each generated agent is a single Markdown file:

```markdown
---
name: custom-agent
description: Triggers auto-invocation
tools: Read, Write, Edit
model: sonnet
color: green
field: backend
expertise: expert
mcp_tools: mcp__github
---

You are a [role] specializing in [domain].

When invoked:
1. [Step 1]
2. [Step 2]
3. [Step 3]

[Detailed instructions]
[Checklists]
[Best practices]
[Output format]
```

## Integration Workflows

### Workflow 1: Feature Development
```
1. product-planner → Creates requirements
2. frontend-developer + backend-developer → Build (parallel)
3. test-runner → Validates (sequential)
4. code-reviewer → Reviews (sequential)
```

### Workflow 2: Bug Fix
```
1. debugger → Analyzes issue
2. [appropriate-dev-agent] → Fixes
3. test-runner → Validates fix
```

### Workflow 3: Code Review
```
1. code-reviewer → Quality review (can run solo)
2. security-auditor → Security scan (can run solo)
```

## MCP Tool Integration

Common MCP servers to integrate:

- **mcp__github**: PR reviews, issues, repo operations
- **mcp__playwright**: E2E testing, screenshots, browser automation
- **mcp__context7**: Documentation search, knowledge queries
- **mcp__filesystem**: Advanced file operations
- **Custom MCP servers**: Any user-configured MCP tools

Agents automatically reference MCP tools in their capabilities when configured.

## Safety & Performance

### Process Monitoring

Agents consume system resources. Monitor with:
```bash
ps aux | grep -E "mcp|npm|claude" | wc -l
```

**Safe ranges:**
- 15-20: Strategic agents (parallel)
- 20-30: Implementation agents (coordinated)
- 12-18: Quality agents (sequential)

**Warnings:**
- >30: Reduce parallelization
- >60: Critical - restart system

### Execution Rules

✅ **Safe**: 4-5 strategic agents in parallel
✅ **Safe**: 2-3 implementation agents coordinated
❌ **Unsafe**: Quality agents in parallel (crashes system)

## Best Practices

1. **Keep agents focused** - One clear responsibility per agent
2. **Use descriptive descriptions** - Enables auto-invocation
3. **Follow tool access patterns** - Match tools to agent type
4. **Specify execution pattern** - Prevents performance issues
5. **Leverage MCP tools** - Enhance agent capabilities
6. **Test agents incrementally** - Start simple, add complexity
7. **Version control agents** - Check project agents into git

## Limitations

- Agents are templates - customize for your specific needs
- Tool suggestions are guidelines, not requirements
- MCP tools require servers to be configured
- Performance depends on system resources
- Generated agents need testing in your environment

## Installation

**Generated Agent Files:**

Place in one of these locations:

**Project agents** (shared with team):
```bash
.claude/agents/custom-agent.md
```

**Personal agents** (available everywhere):
```bash
~/.claude/agents/custom-agent.md
```

## When to Use This Skill

**Create custom agents for:**
- Domain-specific workflows (data science, ML, finance)
- Team-specific conventions (your code style, testing approach)
- Specialized tools or frameworks (Shopify, AWS, Kubernetes)
- Custom MCP server integrations
- Rapid prototyping of agent ideas

**Use the AGENTS_FACTORY_PROMPT.md template when:**
- You need multiple related agents
- You want consistent agent patterns
- You're building an agentic framework
- You want to test agent concepts quickly

---

**Version**: 1.0.0
**Last Updated**: October 22, 2025
**Compatibility**: Claude Code (agents system)
**Template Location**: [documentation/templates/AGENTS_FACTORY_PROMPT.md](../../documentation/templates/AGENTS_FACTORY_PROMPT.md)
