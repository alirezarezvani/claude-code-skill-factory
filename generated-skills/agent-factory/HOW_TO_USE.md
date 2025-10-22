# How to Use the Agent Factory

This guide shows you how to create custom Claude Code agents using the Agent Factory system.

## Quick Start

### Step 1: Open the Prompt Template

Navigate to: **[documentation/templates/AGENTS_FACTORY_PROMPT.md](../../documentation/templates/AGENTS_FACTORY_PROMPT.md)**

### Step 2: Scroll to Bottom

Find the template variables section:

```
=== FILL IN YOUR DETAILS BELOW ===

AGENT_TYPE: [Your choice]
AGENT_NAME: [kebab-case-name]
...
```

### Step 3: Fill In Your Details

```
AGENT_TYPE: Implementation
AGENT_NAME: api-integration-specialist
DOMAIN_FIELD: backend
DESCRIPTION: API integration expert for third-party services. Use when building API clients.
CAPABILITIES: OAuth flows, REST clients, error handling, rate limiting
TOOLS_NEEDED: Read, Write, Edit, Bash, Grep
MODEL: sonnet
COLOR: green
EXPERTISE_LEVEL: expert
MCP_TOOLS: mcp__github
SYSTEM_PROMPT: You are an expert backend developer...
NUMBER_OF_AGENTS: 1
```

### Step 4: Copy Entire Prompt

Copy the ENTIRE prompt template including your filled variables.

### Step 5: Generate with Claude

Paste into:
- **Claude.ai** (any plan)
- **Claude Code**
- **Claude API**

Claude will generate complete agent .md file(s).

### Step 6: Install Your Agent

**Project-level** (shared with team):
```bash
# Copy generated agent file
cp api-integration-specialist.md .claude/agents/

# Commit to git
git add .claude/agents/api-integration-specialist.md
git commit -m "Add API integration specialist agent"
```

**User-level** (personal, available everywhere):
```bash
# Copy to user agents folder
cp api-integration-specialist.md ~/.claude/agents/
```

### Step 7: Use Your Agent

**Automatic invocation**:
```
> Build a Stripe payment integration
```
(Claude automatically uses api-integration-specialist agent)

**Explicit invocation**:
```
> Use the api-integration-specialist agent to connect to the GitHub API
```

---

## Example Use Cases

### Example 1: Create a Test Automation Agent

**Fill template:**
```
AGENT_TYPE: Quality
AGENT_NAME: playwright-test-runner
DOMAIN_FIELD: testing
DESCRIPTION: Playwright E2E test specialist. Use after feature implementation.
CAPABILITIES: E2E tests, visual testing, test reports
TOOLS_NEEDED: Read, Write, Edit, Bash, Grep, Glob
EXECUTION_PATTERN: sequential
MODEL: sonnet
COLOR: red
EXPERTISE_LEVEL: expert
MCP_TOOLS: mcp__playwright
SYSTEM_PROMPT: You are a Playwright testing expert. Write and run E2E tests, generate reports, handle test failures.
NUMBER_OF_AGENTS: 1
```

**Generated agent**: `.claude/agents/playwright-test-runner.md`

**Usage**: "Run E2E tests for the checkout flow" → Agent auto-invokes

---

### Example 2: Create a Frontend Component Builder

**Fill template:**
```
AGENT_TYPE: Implementation
AGENT_NAME: react-component-builder
DOMAIN_FIELD: frontend
DESCRIPTION: React component specialist. Use for building reusable UI components.
CAPABILITIES: React components, TypeScript, styled-components, tests
TOOLS_NEEDED: Read, Write, Edit, Bash, Grep, Glob
EXECUTION_PATTERN: coordinated
MODEL: sonnet
COLOR: green
EXPERTISE_LEVEL: expert
MCP_TOOLS: mcp__playwright
NUMBER_OF_AGENTS: 1
```

**Usage**: "Build a ProductCard component" → Agent auto-invokes

---

### Example 3: Create Multiple Related Agents

**Fill template:**
```
AGENT_TYPE: Strategic, Implementation, Quality
NUMBER_OF_AGENTS: 3

Agent 1:
AGENT_NAME: feature-planner
DESCRIPTION: Feature planning specialist. Use for creating feature specs.
DOMAIN_FIELD: product
COLOR: blue
EXPERTISE_LEVEL: expert

Agent 2:
AGENT_NAME: fullstack-builder
DESCRIPTION: Full-stack developer. Use for implementing complete features.
DOMAIN_FIELD: fullstack
COLOR: green
EXPERTISE_LEVEL: expert

Agent 3:
AGENT_NAME: integration-tester
DESCRIPTION: Integration testing specialist. Use to validate feature integration.
DOMAIN_FIELD: testing
COLOR: red
EXPERTISE_LEVEL: expert
```

**Workflow**: Plan → Build → Test (complete feature pipeline)

---

## Enhanced YAML Fields Explained

### Color Coding

Choose color based on agent type:

| Color | When to Use | Examples |
|-------|-------------|----------|
| **blue** | Planning, research, strategy | product-planner, architect, researcher |
| **green** | Code writing, building | frontend-dev, backend-dev, api-builder |
| **red** | Testing, review, validation | test-runner, code-reviewer, qa-specialist |
| **purple** | Coordination, orchestration | fullstack-coordinator, workflow-manager |
| **orange** | Domain specialists | data-scientist, ml-engineer, finance-analyst |

### Field Categories

Organize by domain:

**Development**: `frontend`, `backend`, `fullstack`, `mobile`, `devops`
**Quality**: `testing`, `security`, `performance`, `quality`
**Strategic**: `product`, `architecture`, `research`, `design`
**Domain**: `data`, `ai`, `content`, `finance`, `infrastructure`

### Expertise Levels

- **beginner**: Simple tasks, limited scope (e.g., file-formatter, linter)
- **intermediate**: Moderate workflows (e.g., component-builder, api-tester)
- **expert**: Complex operations (e.g., system-architect, security-auditor)

### MCP Tools

Add comma-separated MCP server tools:

```yaml
mcp_tools: mcp__github, mcp__playwright, mcp__context7
```

Common integrations:
- `mcp__github` → PR reviews, issue management
- `mcp__playwright` → E2E testing, screenshots
- `mcp__context7` → Documentation search
- `mcp__filesystem` → Advanced file ops

---

## Tool Access Patterns

Follow these recommendations:

### Strategic Agents
```yaml
tools: Read, Write, Grep
color: blue
```
- Lightweight, parallel-safe
- No code execution

### Implementation Agents
```yaml
tools: Read, Write, Edit, Bash, Grep, Glob
color: green
```
- Full tool access
- Coordinated execution

### Quality Agents
```yaml
tools: Read, Write, Edit, Bash, Grep, Glob
color: red
```
- Heavy Bash operations
- **Sequential only!**

---

## Common Workflows

### Workflow 1: Full-Stack Feature

Create 3 agents:
1. **product-planner** (blue, strategic) → Requirements
2. **frontend-developer** (green, implementation) → UI
3. **backend-developer** (green, implementation) → API
4. **test-runner** (red, quality) → Validation

**Execution**:
- Step 1: Solo
- Steps 2-3: Parallel
- Step 4: Sequential

### Workflow 2: Bug Fix

Create 2 agents:
1. **debugger** (red, quality) → Find root cause
2. **code-fixer** (green, implementation) → Apply fix

**Execution**: Sequential

### Workflow 3: Code Review

Create 2 agents:
1. **code-reviewer** (red, quality) → Quality check
2. **security-auditor** (red, quality) → Security scan

**Execution**: Can run in parallel (both read-only)

---

## Tips for Success

### 1. Write Clear Descriptions

The `description` field is CRITICAL for auto-invocation:

✅ **Good**: "React component specialist. Use for building UI components."
❌ **Bad**: "Helps with frontend"

### 2. Keep Agents Focused

One agent, one job:

✅ **Good**: Separate `frontend-developer` and `backend-developer`
❌ **Bad**: One `fullstack-developer` that does everything

### 3. Follow Tool Patterns

Match tools to agent type for safety and performance.

### 4. Test Incrementally

Start with one simple agent, verify it works, then create more.

### 5. Use MCP When Available

If you have MCP servers configured, leverage them in your agents.

---

## Troubleshooting

### "My agent isn't being invoked automatically"

**Check description field**:
- Is it specific and action-oriented?
- Does it describe WHEN to use the agent?
- Try making it more explicit

### "YAML validation error"

**Common issues**:
- Name not in kebab-case
- Tools in array format `["Read"]` instead of comma-separated `Read, Write`
- Missing closing `---`

### "Agent crashes or freezes"

**Check execution pattern**:
- Quality agents MUST run sequential only
- Too many agents in parallel (>5)
- Check process count: `ps aux | grep claude | wc -l`

### "Tools not working"

**Verify**:
- Tools are comma-separated: `Read, Write, Edit`
- Not array format
- Tool names match exactly (case-sensitive)

---

## Installation Locations

### Project Agents (Shared with Team)
```
your-project/
└── .claude/
    └── agents/
        ├── custom-agent-1.md
        └── custom-agent-2.md
```

Commit to git - team gets them automatically.

### Personal Agents (Available Everywhere)
```
~/.claude/
└── agents/
    ├── my-personal-agent.md
    └── another-agent.md
```

Available across all your projects.

### Priority

When same name exists:
1. Project agents (highest priority)
2. Personal agents
3. Plugin agents (lowest priority)

---

## Next Steps

1. **Try the template** - Generate your first agent
2. **Install and test** - Verify it works
3. **Iterate** - Refine based on usage
4. **Create workflows** - Build complementary agents
5. **Share with team** - Commit project agents to git

---

## Reference

**Prompt Template**: [documentation/templates/AGENTS_FACTORY_PROMPT.md](../../documentation/templates/AGENTS_FACTORY_PROMPT.md)

**Claude Code Agents Documentation**: https://docs.claude.com/en/docs/claude-code/sub-agents

**Managing Agents**: Use `/agents` command in Claude Code

**Examples**: See `claude-agents-instructions.md` for complete examples

---

**Ready to create your first agent? Open the prompt template and start building!** 🚀
