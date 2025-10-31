# Claude Code Agents Reference

**Complete guide to creating and managing specialized AI agents (subagents) in Claude Code**

---

## Table of Contents

- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
- [Quick Start](#quick-start)
- [Agent Configuration](#agent-configuration)
- [Managing Agents](#managing-agents)
- [Using Agents Effectively](#using-agents-effectively)
- [Example Agents](#example-agents)
- [Best Practices](#best-practices)
- [Advanced Topics](#advanced-topics)
- [CLI Reference](#cli-reference)
- [Troubleshooting](#troubleshooting)

---

## Introduction

### What Are Claude Code Agents?

Claude Code Agents (also called **subagents**) are specialized AI assistants that handle specific types of tasks. Each agent operates independently with:

- **Dedicated Context Window** - Separate from the main conversation
- **Custom System Prompt** - Tailored instructions for specific domains
- **Configurable Tools** - Granular access control
- **Specific Expertise** - Fine-tuned for particular task types

**When to Use Agents**: Claude Code automatically delegates tasks to appropriate agents based on their descriptions, or you can invoke them explicitly.

### Key Benefits

| Benefit | Description |
|---------|-------------|
| **Context Preservation** | Each agent operates in its own context, keeping the main conversation focused on high-level objectives |
| **Specialized Expertise** | Agents can be fine-tuned with detailed instructions for specific domains, leading to higher success rates |
| **Reusability** | Once created, agents can be used across projects and shared with your team for consistent workflows |
| **Flexible Permissions** | Each agent can have different tool access levels, limiting powerful tools to specific agent types |
| **Team Collaboration** | Project-level agents can be version-controlled and shared across your team |

---

## Core Concepts

### Agent Hierarchy

Agents are loaded with the following priority order (highest to lowest):

| Priority | Type | Location | Scope | Override |
|----------|------|----------|-------|----------|
| **1** | Project Agents | `.claude/agents/` | Current project only | Highest |
| **2** | CLI Agents | `--agents` flag | Current session only | Medium-High |
| **3** | User Agents | `~/.claude/agents/` | All projects | Medium |
| **4** | Plugin Agents | Plugin `agents/` directory | All projects (when plugin enabled) | Lowest |

**Name Conflicts**: When agent names conflict, higher-priority agents override lower-priority ones.

### Context Management

**Separate Context Windows**:
- Each agent starts with a clean context when invoked
- Main conversation remains focused on high-level coordination
- Prevents context pollution and maintains clarity

**Trade-offs**:
- ✅ **Benefit**: Longer overall sessions (preserved main context)
- ⚠️ **Consideration**: Agents may add latency gathering required context

### Tool Access Control

**Two Configuration Modes**:

1. **Inherit All Tools** (default) - Omit `tools` field
   - Agent inherits all tools from main thread
   - Includes MCP server tools automatically
   - Simplest configuration

2. **Explicit Tool List** - Specify `tools` field
   - Granular control over permissions
   - Enhanced security for sensitive operations
   - Comma-separated list: `tools: Read, Write, Bash`

---

## Quick Start

### 1. Create Your First Agent

**Method A: Interactive (Recommended)**

```bash
# Open agents interface
/agents

# Select "Create New Agent"
# Choose project-level or user-level
# Generate with Claude first, then customize
# Save and use immediately
```

**Method B: Direct File Creation**

```bash
# Create project agent
mkdir -p .claude/agents
cat > .claude/agents/code-reviewer.md << 'EOF'
---
name: code-reviewer
description: Expert code review specialist. Use proactively after code changes.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer ensuring high standards.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review for: code quality, security, maintainability, performance.
EOF
```

### 2. Use Your Agent

**Automatic Invocation** (Claude decides):
```
> I just modified the authentication module
# Claude automatically uses code-reviewer agent
```

**Explicit Invocation** (you decide):
```
> Use the code-reviewer agent to check my recent changes
> Have code-reviewer look at the API endpoints
```

### 3. Manage Agents

```bash
/agents                 # View and manage all agents
/agents create          # Create new agent interactively
/agents edit <name>     # Edit existing agent
/agents delete <name>   # Remove agent
```

---

## Agent Configuration

### File Format

Each agent is a Markdown file with YAML frontmatter:

```markdown
---
name: agent-name-here
description: When and why this agent should be invoked
tools: Tool1, Tool2, Tool3  # Optional
model: sonnet               # Optional
---

System prompt goes here. Define the agent's role, capabilities,
and approach to solving problems.

Include specific instructions, best practices, and constraints.
```

### Required Fields

| Field | Required | Format | Description |
|-------|----------|--------|-------------|
| **name** | ✅ Yes | `kebab-case` | Unique identifier (lowercase, hyphens only) |
| **description** | ✅ Yes | Natural language | When the agent should be invoked |

### Optional Fields

| Field | Default | Options | Description |
|-------|---------|---------|-------------|
| **tools** | All tools inherited | Comma-separated list | Specific tools to grant access |
| **model** | Configured default | `sonnet`, `opus`, `haiku`, `inherit` | AI model to use |

### Model Selection

**Available Options**:

- **`sonnet`** - Balanced performance and capability (default for agents)
- **`opus`** - Highest capability, best for complex tasks
- **`haiku`** - Fastest, best for simple tasks
- **`inherit`** - Use same model as main conversation
- **Omitted** - Uses configured default for agents

**Example: Inherit Main Model**
```yaml
model: inherit  # Adapts to main conversation's model
```

### Tool Configuration

**Available Tools** (Common subset):

| Tool | Purpose | Security Level |
|------|---------|----------------|
| `Read` | Read files | Low risk |
| `Write` | Create/overwrite files | Medium risk |
| `Edit` | Modify files | Medium risk |
| `Bash` | Execute shell commands | High risk |
| `Grep` | Search file contents | Low risk |
| `Glob` | Find files by pattern | Low risk |
| `WebFetch` | Fetch web content | Medium risk |

**MCP Tools**: When `tools` field is omitted, agents inherit all MCP tools from configured MCP servers.

**Best Practice**: Use `/agents` command to manage tool access - it shows all available tools including MCP tools.

### Plugin Agents

**How Plugin Agents Work**:

- Plugins can provide custom agents in their `agents/` directory
- Appear in `/agents` interface alongside your agents
- Can be invoked automatically or explicitly
- Follow same format as user-defined agents

**Plugin Agent Invocation**:
```bash
# Automatic (Claude selects)
> Review this code for security issues
# May use security-plugin's code-reviewer

# Explicit
> Use the code-reviewer agent from security-plugin
```

### CLI-Based Configuration

**Session-Specific Agents**:

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer focusing on quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  },
  "test-runner": {
    "description": "Test automation expert. Use when running tests.",
    "prompt": "You run tests and fix failures while preserving test intent.",
    "tools": ["Bash", "Read", "Edit"],
    "model": "haiku"
  }
}'
```

**Use Cases**:
- Quick testing of agent configurations
- Session-specific agents (don't need to be saved)
- Automation scripts requiring custom agents
- Sharing agent definitions in documentation

**Priority**: CLI agents override user agents but not project agents.

---

## Managing Agents

### Interactive Management (Recommended)

**Access Agents Interface**:
```bash
/agents
```

**Available Operations**:

| Operation | Description |
|-----------|-------------|
| **View All** | List all available agents (built-in, user, project, plugin) |
| **Create New** | Guided setup with Claude generation |
| **Edit Existing** | Modify agent configuration and tools |
| **Delete Custom** | Remove user or project agents |
| **Inspect** | View agent configuration and system prompt |
| **Manage Tools** | Interactive tool selection with complete list |

**Advantages**:
- ✅ See all available tools (including MCP tools)
- ✅ Visual indication of active agents
- ✅ Conflict resolution (duplicate names)
- ✅ Generate initial agent with Claude
- ✅ Edit system prompt in your preferred editor

### Direct File Management

**Create Project Agent**:
```bash
mkdir -p .claude/agents
echo '---
name: test-runner
description: Use proactively to run tests and fix failures
tools: Bash, Read, Edit
---

You are a test automation expert. When you see code changes,
proactively run appropriate tests. If tests fail, analyze failures
and fix them while preserving original test intent.' > .claude/agents/test-runner.md
```

**Create User Agent**:
```bash
mkdir -p ~/.claude/agents
# Create agent file in ~/.claude/agents/
```

**Edit Agent**:
```bash
# Use your preferred editor
code .claude/agents/test-runner.md
vim ~/.claude/agents/debugger.md
```

**Delete Agent**:
```bash
rm .claude/agents/test-runner.md
rm ~/.claude/agents/debugger.md
```

### Version Control

**Project Agents** (Recommended for teams):
```bash
# Add to version control
git add .claude/agents/
git commit -m "Add code-reviewer and test-runner agents"

# Team members get agents automatically
git pull
```

**User Agents** (Personal preferences):
- Stored in `~/.claude/agents/`
- Not version-controlled
- Personal customizations

---

## Using Agents Effectively

### Automatic Delegation

**How Claude Selects Agents**:

1. Analyzes your request and current task
2. Compares task with agent `description` fields
3. Selects best-matching agent based on:
   - Description relevance
   - Available tools
   - Current context

**Encouraging Proactive Use**:

```yaml
# Good: Explicit trigger words
description: Use PROACTIVELY after code changes to review for quality and security

# Good: Clear action verbs
description: MUST BE USED when running tests or fixing test failures

# Weak: Vague description
description: Helps with code tasks
```

**Trigger Phrases** (in descriptions):
- "Use **proactively**" - Claude should use without being asked
- "**Must be used**" - Required for specific situations
- "**Automatically invoke**" - Use when conditions are met
- "**Immediately after**" - Timing-based triggers

### Explicit Invocation

**Request Specific Agent**:
```bash
# Direct request
> Use the test-runner agent to fix failing tests
> Have the code-reviewer agent look at my recent changes
> Ask the debugger agent to investigate this error

# Chained requests
> First use code-analyzer to find issues, then use optimizer to fix them
```

**Agent Selection Priority**:
1. Explicitly named agent
2. Best-matching agent by description
3. Main Claude (no delegation)

### Context Optimization

**Agent Context Lifecycle**:

```
1. Agent Invoked
   ↓
2. Clean Context Window Created
   ↓
3. Agent Gathers Required Context
   (reads files, runs commands, analyzes code)
   ↓
4. Agent Performs Task
   ↓
5. Agent Returns Results
   ↓
6. Context Window Discarded
```

**Optimization Tips**:
- Provide relevant file paths in your request
- Reference specific code sections
- Include error messages or logs
- Mention recent changes (e.g., "I just modified auth.ts")

---

## Example Agents

### 1. Code Reviewer

**Purpose**: Comprehensive code review focusing on quality, security, and maintainability.

```markdown
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer ensuring high standards of code quality and security.

## When Invoked

1. Run `git diff` to see recent changes
2. Focus on modified files
3. Begin review immediately without asking for confirmation

## Review Checklist

**Code Quality**:
- Code is simple and readable
- Functions and variables are well-named
- No duplicated code
- Proper separation of concerns

**Security**:
- No exposed secrets or API keys
- Input validation implemented
- Proper error handling
- No SQL injection vulnerabilities

**Maintainability**:
- Good test coverage
- Clear documentation
- Consistent code style
- Performance considerations addressed

## Output Format

Provide feedback organized by priority:

**Critical Issues** (must fix before merge):
- [Specific issue with file:line reference]
- [How to fix with code example]

**Warnings** (should fix):
- [Specific issue with file:line reference]
- [Recommended fix]

**Suggestions** (consider improving):
- [Improvement opportunity]
- [Why it matters]

Always include specific examples of how to fix issues.
```

### 2. Test Runner

**Purpose**: Automated test execution and failure analysis.

```markdown
---
name: test-runner
description: Test automation expert. Use proactively to run tests after code changes and fix failures while preserving test intent.
tools: Bash, Read, Edit, Grep
model: haiku
---

You are a test automation expert specializing in running tests and fixing failures.

## When Invoked

1. Identify appropriate test command for the project
2. Run tests immediately
3. If failures occur, analyze and fix
4. Verify fixes work

## Testing Process

**Test Execution**:
- Detect test framework (Jest, pytest, RSpec, etc.)
- Run appropriate test command
- Capture full output

**Failure Analysis**:
- Parse error messages and stack traces
- Identify root cause
- Check if test expectations changed
- Verify if code behavior changed

**Fix Implementation**:
- Fix the code if behavior is wrong
- Update test if expectations changed
- Add debug logging if needed
- Preserve original test intent

## Output Format

For each test failure:

**Failure**: [Test name]
**Root Cause**: [Brief explanation]
**Fix Applied**: [What was changed]
**Verification**: [How fix was confirmed]

Always run tests again after applying fixes.
```

### 3. Debugger

**Purpose**: Systematic debugging and root cause analysis.

```markdown
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues or exceptions.
tools: Read, Edit, Bash, Grep, Glob
model: sonnet
---

You are an expert debugger specializing in root cause analysis.

## When Invoked

1. Capture error message and full stack trace
2. Identify minimal reproduction steps
3. Isolate the failure location
4. Implement targeted fix
5. Verify solution works

## Debugging Process

**Information Gathering**:
- Analyze error messages and logs
- Check recent code changes (git diff)
- Identify affected files and functions
- Review related test failures

**Hypothesis Formation**:
- Form specific hypotheses about root cause
- Test each hypothesis systematically
- Eliminate possibilities through evidence

**Investigation Techniques**:
- Add strategic debug logging
- Inspect variable states
- Trace execution flow
- Check edge cases

**Fix Implementation**:
- Implement minimal fix addressing root cause
- Avoid fixing symptoms only
- Add tests to prevent regression
- Document why the issue occurred

## Output Format

**Error Summary**: [Brief description]

**Root Cause**: [Detailed explanation with evidence]

**Fix Applied**:
```[language]
[Code changes with file:line references]
```

**Testing**: [How the fix was verified]

**Prevention**: [How to avoid similar issues]
```

### 4. Documentation Writer

**Purpose**: Generate and maintain high-quality documentation.

```markdown
---
name: doc-writer
description: Documentation specialist. Use proactively to create or update README files, API documentation, and code comments.
tools: Read, Write, Edit, Grep, Glob
model: sonnet
---

You are a technical documentation specialist creating clear, comprehensive documentation.

## When Invoked

1. Understand the codebase structure
2. Identify documentation needs
3. Generate appropriate documentation
4. Ensure clarity and accuracy

## Documentation Standards

**README Files**:
- Clear project overview
- Installation instructions
- Usage examples with code
- API reference
- Contributing guidelines

**Code Comments**:
- Explain complex logic
- Document assumptions
- Describe edge cases
- Include examples for functions

**API Documentation**:
- Clear endpoint descriptions
- Request/response examples
- Error codes and meanings
- Authentication requirements

## Output Format

Write documentation in clear, concise language:
- Use active voice
- Include practical examples
- Organize with clear headings
- Add code snippets where helpful

Always verify accuracy against actual code.
```

### 5. Data Analyst

**Purpose**: SQL queries, data analysis, and insights generation.

```markdown
---
name: data-analyst
description: Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries.
tools: Bash, Read, Write
model: sonnet
---

You are a data analyst specializing in SQL and BigQuery analysis.

## When Invoked

1. Understand the data analysis requirement
2. Write efficient, optimized SQL queries
3. Use BigQuery CLI (bq) when appropriate
4. Analyze and summarize results
5. Present findings clearly

## Query Development

**SQL Best Practices**:
- Write optimized queries with proper filters
- Use appropriate indexes
- Limit result sets appropriately
- Include comments explaining complex logic
- Format queries for readability

**BigQuery Specifics**:
- Use partitioned tables when possible
- Avoid SELECT *
- Use approximate aggregations when exact isn't needed
- Consider query costs

## Analysis Approach

For each analysis:
1. **Understand Requirements**: Clarify what insights are needed
2. **Write Query**: Develop efficient SQL
3. **Execute**: Run query and capture results
4. **Analyze**: Interpret data and identify patterns
5. **Present**: Summarize findings with key takeaways

## Output Format

**Query**:
```sql
[Well-formatted, commented SQL]
```

**Results Summary**: [Key findings]

**Insights**: [Data-driven recommendations]

**Next Steps**: [Suggested follow-up analyses]
```

---

## Best Practices

### 1. Agent Design Principles

**Single Responsibility**:
```yaml
# Good: Focused agent
name: code-reviewer
description: Reviews code for quality, security, and maintainability

# Avoid: Multiple responsibilities
name: dev-helper
description: Reviews code, runs tests, writes documentation, and deploys
```

**Clear Descriptions**:
```yaml
# Good: Specific trigger
description: Use PROACTIVELY after code changes to review for security vulnerabilities and code quality

# Avoid: Vague trigger
description: Helps with code stuff
```

**Appropriate Tool Access**:
```yaml
# Good: Minimal necessary tools
tools: Read, Grep, Glob  # For code review (read-only)

# Avoid: Excessive permissions
tools: Read, Write, Edit, Bash, WebFetch  # Reviewer doesn't need write access
```

### 2. System Prompt Guidelines

**Structure Your Prompts**:

```markdown
# Role Definition
You are [specific role] specializing in [expertise area].

# When Invoked (Trigger Conditions)
[Clear conditions for when to use this agent]

# Process/Workflow
1. [First step]
2. [Second step]
3. [Final step]

# Standards/Checklist
- [Requirement 1]
- [Requirement 2]

# Output Format
[How to present results]
```

**Include Examples**:
- Show expected input/output
- Demonstrate edge cases
- Illustrate best practices
- Provide code templates

**Set Constraints**:
- Define what NOT to do
- Set response length limits
- Specify required validations
- Establish quality gates

### 3. Iteration and Improvement

**Start with Claude Generation**:
1. Use `/agents create` and describe your needs
2. Let Claude generate initial agent
3. Review and customize the generated agent
4. Test in real scenarios
5. Refine based on results

**Continuous Improvement**:
- Track agent success rates
- Collect feedback from team
- Update prompts based on learnings
- Version control changes
- Document improvements

### 4. Team Collaboration

**Project Agents for Teams**:
```bash
# Create standardized agents
.claude/agents/
├── code-reviewer.md      # Team code review standards
├── test-runner.md        # Consistent test execution
└── deployment-helper.md  # Standardized deploy process

# Version control
git add .claude/agents/
git commit -m "feat: Add standardized team agents"
```

**Personal Customizations**:
```bash
# User-level agents for personal workflow
~/.claude/agents/
├── my-debugger.md        # Personal debugging preferences
└── my-note-taker.md      # Individual note-taking style
```

### 5. Security Considerations

**Sensitive Operations**:
```yaml
# Limit tools for sensitive agents
name: security-scanner
tools: Read, Grep  # No write/execute permissions

# Grant carefully for automation
name: deployer
tools: Bash, Read, Write  # Full access for deployment
```

**Secret Management**:
- Never include secrets in agent prompts
- Use environment variables
- Leverage credential stores
- Audit agent access logs

---

## Advanced Topics

### Agent Chaining

**Sequential Processing**:
```bash
# Explicit chaining
> First use code-analyzer to find performance issues, then use optimizer to fix them

# Claude handles the sequence:
# 1. code-analyzer examines code
# 2. Returns findings
# 3. optimizer receives findings
# 4. Implements optimizations
```

**Parallel Processing**:
```bash
# Multiple independent tasks
> Use test-runner to verify tests and code-reviewer to check quality

# Claude may run concurrently:
# 1. test-runner executes tests
# 2. code-reviewer analyzes code
# 3. Results combined in main context
```

### Dynamic Agent Selection

**Context-Aware Delegation**:

Claude considers:
- User request keywords
- Current file context
- Recent operations
- Error states
- Project type

**Example Flow**:
```
User: "The tests are failing"
         ↓
Claude detects: test failure context
         ↓
Checks agent descriptions
         ↓
Finds: test-runner (description mentions "test failures")
         ↓
Automatically delegates to test-runner
```

### Custom Model Strategies

**Task-Based Model Selection**:

```yaml
# Fast iteration (haiku)
name: test-runner
model: haiku  # Quick feedback

# Complex analysis (opus)
name: architecture-reviewer
model: opus  # Deep reasoning

# Balanced (sonnet)
name: code-reviewer
model: sonnet  # Quality + speed

# Adapt to main (inherit)
name: documentation-writer
model: inherit  # Match user's choice
```

### MCP Integration

**MCP Tools in Agents**:

```yaml
# Inherit all MCP tools
name: database-admin
description: Database management expert
# tools field omitted - inherits MCP database tools

# Explicit MCP tools
name: github-manager
tools: mcp__github__create_issue, mcp__github__create_pr, Read, Write
```

**MCP Server Configuration**:
See [MCP Documentation](https://docs.claude.com/en/docs/claude-code/mcp) for server setup.

---

## CLI Reference

### CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `claude` | Start interactive REPL | `claude` |
| `claude "query"` | Start with initial prompt | `claude "review my code"` |
| `claude --continue` | Continue previous session | `claude --continue` |
| `claude --agents` | Define session agents (JSON) | See examples below |
| `/agents` | Manage agents (in REPL) | `/agents create` |

### Agents Flag Format

**Single Agent**:
```bash
claude --agents '{
  "reviewer": {
    "description": "Code reviewer. Use after changes.",
    "prompt": "You are a senior code reviewer.",
    "tools": ["Read", "Grep"],
    "model": "sonnet"
  }
}'
```

**Multiple Agents**:
```bash
claude --agents '{
  "reviewer": {
    "description": "Code reviewer",
    "prompt": "Senior code reviewer focusing on quality",
    "tools": ["Read", "Grep", "Glob"],
    "model": "sonnet"
  },
  "tester": {
    "description": "Test runner",
    "prompt": "Test automation expert",
    "tools": ["Bash", "Read"],
    "model": "haiku"
  }
}'
```

**Field Reference**:

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `description` | ✅ Yes | String | When to invoke the agent |
| `prompt` | ✅ Yes | String | System prompt for the agent |
| `tools` | No | String[] | Tool names (omit to inherit all) |
| `model` | No | String | Model alias or 'inherit' |

---

## Troubleshooting

### Common Issues

**Issue: Agent Not Being Used**

**Symptoms**:
- Claude doesn't delegate to your agent
- Tasks are handled in main context

**Solutions**:
1. Check `description` field is specific and action-oriented
2. Add trigger words: "Use PROACTIVELY", "MUST BE USED"
3. Verify agent name doesn't conflict (check `/agents list`)
4. Ensure tools are appropriate for the task

**Issue: Agent Lacks Context**

**Symptoms**:
- Agent asks for information already provided
- Agent doesn't see recent changes

**Solutions**:
1. Provide file paths explicitly in your request
2. Include error messages or logs in request
3. Mention specific files: "I just modified auth.ts"
4. Agent will gather context - may add latency

**Issue: Agent Has Wrong Permissions**

**Symptoms**:
- "Permission denied" errors
- Agent can't perform required operations

**Solutions**:
1. Check `tools` field includes necessary tools
2. Use `/agents edit <name>` to modify tools
3. Consider omitting `tools` field to inherit all
4. Verify MCP servers are configured if using MCP tools

**Issue: Agent Not Found**

**Symptoms**:
- "Agent 'name' not found" error

**Solutions**:
1. Check agent file exists in `.claude/agents/` or `~/.claude/agents/`
2. Verify filename matches agent name: `name.md`
3. Check YAML frontmatter is valid
4. Restart Claude Code to reload agents

### Debugging Agents

**Enable Verbose Logging**:
```bash
CLAUDE_LOG_LEVEL=debug claude
```

**Check Agent Configuration**:
```bash
/agents inspect <agent-name>
```

**Validate Agent File**:
```bash
# Check YAML syntax
cat .claude/agents/my-agent.md | head -n 10

# Expected format:
# ---
# name: my-agent
# description: ...
# ---
```

**Test Agent Explicitly**:
```bash
# Force agent use to test configuration
> Use the my-agent agent to [specific task]
```

---

## Related Documentation

- **[Claude Code Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)** - Multi-file capabilities vs single-file agents
- **[Slash Commands](https://docs.claude.com/en/docs/claude-code/slash-commands)** - Custom workflow automation
- **[Plugins](https://docs.claude.com/en/docs/claude-code/plugins)** - Extend Claude Code with custom agents
- **[MCP Servers](https://docs.claude.com/en/docs/claude-code/mcp)** - Model Context Protocol integration
- **[Hooks](https://docs.claude.com/en/docs/claude-code/hooks)** - Event-driven automation
- **[Settings](https://docs.claude.com/en/docs/claude-code/settings)** - Configure Claude Code behavior

---

## Appendix

### Quick Reference Card

```
AGENT MANAGEMENT
├─ /agents                    # Manage agents
├─ /agents create             # Create new agent
├─ /agents edit <name>        # Edit agent
└─ /agents delete <name>      # Delete agent

FILE LOCATIONS
├─ .claude/agents/            # Project agents (version control)
└─ ~/.claude/agents/          # User agents (personal)

PRIORITY ORDER (High → Low)
1. Project agents (.claude/agents/)
2. CLI agents (--agents flag)
3. User agents (~/.claude/agents/)
4. Plugin agents (plugin/agents/)

MODEL OPTIONS
├─ sonnet     # Balanced (default for agents)
├─ opus       # Highest capability
├─ haiku      # Fastest
└─ inherit    # Match main conversation

INVOCATION
├─ Automatic: Claude delegates based on description
└─ Explicit:  "Use the <agent-name> agent to..."
```

### Template Library

**Minimal Agent**:
```markdown
---
name: my-agent
description: Brief description of when to use this agent
---

You are [role]. [Instructions].
```

**Standard Agent**:
```markdown
---
name: my-agent
description: Detailed description with PROACTIVE trigger words
tools: Read, Write, Bash
model: sonnet
---

You are [detailed role description].

## When Invoked
[Specific conditions]

## Process
1. [Step 1]
2. [Step 2]

## Standards
- [Requirement 1]
- [Requirement 2]

## Output Format
[Expected output structure]
```

**Advanced Agent**:
```markdown
---
name: my-agent
description: |
  Comprehensive multi-line description.
  Use PROACTIVELY when [conditions].
  MUST BE USED for [specific scenarios].
tools: Read, Write, Edit, Bash, Grep, Glob, WebFetch
model: opus
---

# Role Definition
You are [detailed role] with expertise in [domain].

# Invocation Triggers
- Automatically invoke when: [condition 1]
- Must be used when: [condition 2]
- Proactive usage: [condition 3]

# Methodology
1. [Detailed step 1]
   - Sub-step a
   - Sub-step b
2. [Detailed step 2]

# Quality Standards
- [Standard 1 with rationale]
- [Standard 2 with examples]

# Constraints
- DO: [What to do]
- DON'T: [What to avoid]

# Output Template
[Structured output format with examples]

# Examples
[Concrete examples of input/output]
```

---

**Version**: 1.0.0
**Last Updated**: October 30, 2025
**Official Documentation**: https://docs.claude.com/en/docs/claude-code/agents
