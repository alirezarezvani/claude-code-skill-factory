# documentation/CLAUDE.md

This file provides guidance for working with documentation, references, and factory templates in this repository.

---

## Documentation Structure

The `documentation/` folder contains two main subdirectories:

### references/
Official documentation and reference materials:

- **[claude-skills-instructions.md](references/claude-skills-instructions.md)** - Complete Claude Skills documentation
- **[claude-agents-instructions.md](references/claude-agents-instructions.md)** - Complete Claude Agents documentation
- **[openai-codex-cli-instructions.md](references/openai-codex-cli-instructions.md)** - Complete OpenAI Codex CLI reference
- **[slash-commands-instructions.md](references/slash-commands-instructions.md)** - Slash commands overview
- **[slash-command-code-review-example.md](references/slash-command-code-review-example.md)** - Code review command example
- **[slash-command-codebase-analysis-example.md](references/slash-command-codebase-analysis-example.md)** - Codebase analysis command example
- **[slash-command-open-api-example.md](references/slash-command-open-api-example.md)** - OpenAPI sync command example
- **[slash-command-update-claude-md-example.md](references/slash-command-update-claude-md-example.md)** - Update CLAUDE.md command example
- **[slash-commands-ultrathink-example.md](references/slash-commands-ultrathink-example.md)** - Ultrathink command example

### templates/
Factory prompt templates for generation:

- **[SKILLS_FACTORY_PROMPT.md](templates/SKILLS_FACTORY_PROMPT.md)** - Generate Claude Skills (multi-file)
- **[AGENTS_FACTORY_PROMPT.md](templates/AGENTS_FACTORY_PROMPT.md)** - Generate Claude Code Agents (single .md)
- **[PROMPTS_FACTORY_PROMPT.md](templates/PROMPTS_FACTORY_PROMPT.md)** - Generate domain prompt builders
- **[MASTER_SLASH_COMMANDS_PROMPT.md](templates/MASTER_SLASH_COMMANDS_PROMPT.md)** - Generate slash commands (official patterns)

---

## Templates for Generation

The `templates/` folder contains four powerful prompt templates for creating different types of Claude Code capabilities.

### SKILLS_FACTORY_PROMPT.md

**Purpose**: Generate complete Claude Skills (folders with SKILL.md + Python files)

**Use for**: Creating capabilities like financial analysis, content research, data processing

**Output**:
- Skill folders with SKILL.md, Python files, samples, and ZIP files
- Complete skill package ready for installation

**Location**: Skills go in `.claude/skills/` or `~/.claude/skills/`

**Example Skills**:
- Financial statement analyzer
- AWS solution architect
- Content trend researcher
- Microsoft 365 tenant manager
- Psychology advisor

---

### AGENTS_FACTORY_PROMPT.md

**Purpose**: Generate Claude Code agents/sub-agents (single .md files)

**Use for**: Creating specialized agents like code reviewers, developers, testers

**Output**:
- Agent .md files with enhanced YAML frontmatter
- Includes color, field, expertise, MCP tools configuration
- Tool access patterns and delegation logic

**Location**: Agents go in `.claude/agents/` or `~/.claude/agents/`

**Key Features**:
- YAML frontmatter validation
- Tool access patterns (Read/Write/Edit/Bash/Grep/Glob)
- Model selection (sonnet/opus/haiku)
- MCP integration support
- Color coding for agent types

**Example Agents**:
- Code reviewer
- Frontend developer
- Backend developer
- Test automation specialist
- Security engineer

---

### PROMPTS_FACTORY_PROMPT.md

**Purpose**: Generate domain-specific prompt builders (complete prompt generation systems)

**Use for**: Creating specialized prompt builders for specific industries (Healthcare, Legal, FinTech, etc.)

**Output**:
- Complete prompt builder systems with 10-20 role presets
- Custom 7-question flow for prompt generation
- Domain compliance rules (HIPAA, GDPR, SOC2, etc.)
- Multi-format output (XML/Claude/ChatGPT/Gemini)

**Example**: Generate "Healthcare Prompt Builder" with:
- 15 medical role presets (Physician, Nurse Practitioner, Medical Researcher, etc.)
- HIPAA compliance validation
- Clinical documentation standards
- Medical terminology optimization

**Key Features**:
- Domain-specific preset libraries
- Compliance validation (HIPAA, GDPR, SOC2, PCI-DSS)
- Industry-specific workflows
- Multi-LLM output formats
- Quality validation layer

---

### MASTER_SLASH_COMMANDS_PROMPT.md

**Purpose**: Generate custom Claude Code slash commands following official Anthropic patterns

**Use for**: Creating slash commands for business automation, development workflows, compliance checking, research, and specialized tasks

**Output**:
- Self-contained .md files with YAML frontmatter
- Proper bash permissions (specific commands only)
- $ARGUMENTS usage (never $1, $2, $3)
- Organized in `generated-commands/[command-name]/` folders

**Key Features**:
- **Three official patterns**:
  - **Simple Pattern** (code-review): Context → Task (straightforward workflows)
  - **Multi-Phase Pattern** (codebase-analyze): Discovery → Analysis → Task (complex documentation)
  - **Agent-Style Pattern** (ultrathink, openapi-sync): Role → Process → Guidelines (expert coordination)
- Strict validation (command naming, bash permissions, arguments usage, YAML structure)
- Kebab-case naming convention (verb-noun, noun-verb patterns)
- Auto-generated bash permissions (git commands, discovery commands, comprehensive commands)

**Location**: Generated commands go in:
- Project-level: `generated-commands/[command-name]/`
- User-level: `~/.claude/commands/`

**Based on**: 6 official Anthropic slash command examples in `documentation/references/`

**Example Commands**:
- Business research automation
- Content analysis workflows
- Medical translation systems
- Compliance audit automation
- API building workflows
- Test automation frameworks

---

## Key Differences

| Type | Structure | Files | Installation |
|------|-----------|-------|--------------|
| **Skills** | Multi-file capability | SKILL.md + Python files + resources | `.claude/skills/` |
| **Agents** | Single-file specialist | .md with YAML frontmatter | `.claude/agents/` |
| **Prompts** | Meta-prompt system | Complete prompt builder | Use as template |
| **Slash Commands** | Self-contained workflow | .md with YAML + bash integration | `.claude/commands/` or `generated-commands/` |

---

## Installation Locations

### Skills
- **Claude Code Project**: Copy skill folder to `.claude/skills/`
- **Claude Code Personal**: Copy skill folder to `~/.claude/skills/`
- **Claude Apps**: Use the "skill-creator" skill to import
- **API**: Use the `/v1/skills` endpoint

### Agents
- **Claude Code Project**: Copy .md file to `.claude/agents/`
- **Claude Code Personal**: Copy .md file to `~/.claude/agents/`
- **CLI**: Use `--agents` flag for session-specific agents

### Slash Commands
- **Project-level**: Place in `generated-commands/[command-name]/`
- **User-level**: Place in `~/.claude/commands/`
- **Invocation**: `/command-name [arguments]`

---

## Documentation Best Practices

### When Creating Documentation

1. **Use References**: Link to existing official documentation (Anthropic, OpenAI)
2. **Stay Current**: Update documentation when APIs or patterns change
3. **Include Examples**: Always provide working code examples
4. **Preserve Details**: All important technical details must be preserved
5. **Professional Format**: Use clear TOC, tables, and code blocks

### When Using Templates

1. **Start with Examples**: Review existing skills/agents before generating new ones
2. **Follow Patterns**: Use official patterns (Simple, Multi-Phase, Agent-Style)
3. **Validate Output**: Check YAML syntax, bash permissions, naming conventions
4. **Test Locally**: Install and test generated output before deployment
5. **Iterate**: Refine templates based on real-world usage

### When Organizing Documentation

1. **Separation of Concerns**: Keep references separate from templates
2. **Logical Hierarchy**: Group related documentation together
3. **Easy Navigation**: Use clear folder names and consistent structure
4. **Version Control**: Track changes to documentation in git
5. **Contextual Loading**: Use sub-CLAUDE.md files for focused guidance

---

## Related Resources

- **Main README**: [../README.md](../README.md) - Project overview
- **Root CLAUDE.md**: [../CLAUDE.md](../CLAUDE.md) - Orchestration layer
- **Skills Examples**: [../claude-skills-examples/](../claude-skills-examples/) - Reference skill implementations
- **Generated Skills**: [../generated-skills/](../generated-skills/) - Production-ready skills catalog
- **GitHub Workflows**: [../.github/CLAUDE.md](../.github/CLAUDE.md) - GitHub automation guidance

---

## External Links

- **Anthropic Skills Docs**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- **Skills Marketplace**: https://github.com/anthropics/skills
- **Claude Code Docs**: https://docs.claude.com/en/docs/claude-code
- **OpenAI Codex CLI**: https://developers.openai.com/codex/cli
