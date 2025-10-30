# Claude Code Skills & Agents Factory

A comprehensive toolkit for generating production-ready Claude Skills and Claude Code Agents at scale. This repository provides templates, examples, and powerful prompt engineering systems to create custom skills and specialized agents for Claude AI across all platforms.

## Overview

This factory enables you to:
- **Generate Claude Skills** - Multi-file capabilities with Python implementations
- **Generate Claude Code Agents** - Single-file specialist assistants
- **Generate Production Prompts** - World-class mega-prompts for any role/industry
- **Generate Slash Commands** - Custom workflow automation following official Anthropic patterns
- **Bridge Tools** - Interoperability between Claude Code and OpenAI Codex CLI

## Main Capabilities

### 1. Skills Factory
Generate complete, production-ready Claude Skills with:
- Properly formatted SKILL.md with YAML frontmatter
- Python implementation files (when needed)
- Sample input/output data
- Complete documentation and usage guides
- ZIP packages for easy distribution

**Template**: [SKILLS_FACTORY_PROMPT.md](documentation/templates/SKILLS_FACTORY_PROMPT.md)

### 2. Agents Factory
Create specialized Claude Code Agents with:
- Enhanced YAML frontmatter (name, description, tools, model, color, field, expertise)
- MCP integration support
- Auto-invocation capabilities
- Tool access configuration

**Template**: [AGENTS_FACTORY_PROMPT.md](documentation/templates/AGENTS_FACTORY_PROMPT.md)

### 3. Prompt Factory
Generate mega-prompts for any role with:
- 69 professional presets across 15 domains
- Multiple output formats (XML, Claude, ChatGPT, Gemini)
- 7-point quality validation
- Core & Advanced modes

**Ready-to-use Skill**: [generated-skills/prompt-factory/](generated-skills/prompt-factory/)

### 4. Slash Command Factory
Create custom slash commands with:
- 17 preset commands (business, development, documentation, analysis)
- Three official Anthropic patterns (Simple, Multi-Phase, Agent-Style)
- Comprehensive 4-layer validation
- Auto-generated bash permissions

**Template**: [MASTER_SLASH_COMMANDS_PROMPT.md](documentation/templates/MASTER_SLASH_COMMANDS_PROMPT.md)

### 5. Codex CLI Bridge
Enable Claude Code ↔ Codex CLI interoperability with:
- Automatic CLAUDE.md → AGENTS.md translation
- Reference-based architecture (no duplication)
- Safety mechanisms and auto-validation
- Cross-tool team collaboration support

**Skill**: [generated-skills/codex-cli-bridge/](generated-skills/codex-cli-bridge/)

## Quick Start

### Generate a Claude Skill

1. Open [SKILLS_FACTORY_PROMPT.md](documentation/templates/SKILLS_FACTORY_PROMPT.md)
2. Fill in your business type, use cases, and requirements at the bottom
3. Copy the entire prompt and paste into Claude (any platform)
4. Receive complete skill package with code, docs, and samples

### Generate a Claude Agent

1. Open [AGENTS_FACTORY_PROMPT.md](documentation/templates/AGENTS_FACTORY_PROMPT.md)
2. Fill in agent details (name, type, field, tools, model)
3. Copy and paste into Claude
4. Install the generated .md file to `.claude/agents/`

### Use the Prompt Factory

1. Install: `cp -r generated-skills/prompt-factory ~/.claude/skills/`
2. Ask Claude: "I need a prompt for [role name]"
3. Answer 5-7 questions
4. Receive production-ready mega-prompt in your preferred format

### Interactive Guide System

The fastest way to build skills, agents, or prompts:

```
I want to build something
```

The **factory-guide** agent will ask what you need and delegate to specialist guides. Or use slash commands:

- `/build` - Interactive skill/agent/prompt builder
- `/validate-output` - Validate generated output
- `/install-skill` - Install to appropriate location
- `/factory-status` - Check system status

See [.claude/agents/README.md](.claude/agents/README.md) and [.claude/commands/README.md](.claude/commands/README.md) for details.

## Repository Structure

```
claude-code-skills-factory/
├── README.md                              # This file
├── CLAUDE.md                              # Repository guidance
├── AGENTS.md                              # Codex CLI documentation (auto-generated)
├── .claude/
│   ├── agents/                            # Guide agents (factory-guide, skills-guide, etc.)
│   └── commands/                          # Slash commands (/build, /sync-agents-md, etc.)
├── claude-skills-examples/                # 3 reference implementations
├── documentation/
│   ├── references/                        # Official Anthropic examples
│   └── templates/                         # 4 factory prompt templates
└── generated-skills/                      # 9 production-ready skills
    ├── aws-solution-architect/            # AWS architecture & IaC
    ├── content-trend-researcher/          # Multi-platform content research
    ├── ms365-tenant-manager/              # Microsoft 365 administration
    ├── psychology-advisor/                # Mental wellness & CBT
    ├── agent-factory/                     # Agent generation system
    ├── prompt-factory/                    # Prompt generation powerhouse
    ├── slash-command-factory/             # Slash command generation
    └── codex-cli-bridge/                  # Claude Code ↔ Codex CLI bridge
```

## Production Skills Included

All skills include complete implementation, documentation, samples, and distribution packages:

1. **AWS Solution Architect** (53 KB) - Serverless architecture, IaC templates, cost optimization
   - [View Skill](generated-skills/aws-solution-architect/)

2. **Content Trend Researcher** (35 KB) - Multi-platform trend analysis, SEO-optimized outlines
   - [View Skill](generated-skills/content-trend-researcher/)

3. **Microsoft 365 Tenant Manager** (40 KB) - M365 administration, PowerShell automation
   - [View Skill](generated-skills/ms365-tenant-manager/)

4. **Psychology Advisor** (31 KB) - Evidence-based mental wellness, CBT techniques
   - [View Skill](generated-skills/psychology-advisor/)

5. **Agent Factory** (12 KB) - Generate custom Claude Code agents with enhanced YAML
   - [View Skill](generated-skills/agent-factory/)

6. **Prompt Factory** (427 KB) - 69 professional presets, multi-format output, 7-point validation
   - [View Skill](generated-skills/prompt-factory/)

7. **Slash Command Factory** (26 KB) - 17 presets, official Anthropic patterns, 4-layer validation
   - [View Skill](generated-skills/slash-command-factory/)

8. **Codex CLI Bridge** (48 KB) - Claude Code ↔ Codex CLI interoperability, AGENTS.md generation
   - [View Skill](generated-skills/codex-cli-bridge/)

## Reference Examples

Three fully-functional example skills demonstrating different patterns:

- **Analyzing Financial Statements** - Calculation engine + interpretation layer
- **Creating Financial Models** - DCF valuation, sensitivity analysis, Monte Carlo simulation
- **Applying Brand Guidelines** - Corporate branding application

See [claude-skills-examples/](claude-skills-examples/) for implementation details.

## Key Features

- **Production-Ready Output** - Proper YAML frontmatter, type-annotated Python, error handling
- **Composable Design** - Skills work together in workflows
- **Complete Packaging** - Documentation, samples, ZIP files included
- **Smart Detection** - Automatically determines when Python code is needed vs prompt-only
- **Multi-Format Support** - XML, Claude, ChatGPT, Gemini output formats
- **Official Patterns** - Based on Anthropic documentation and examples
- **Cross-Platform** - Works with Claude AI (desktop/browser), Claude Code, and API

## Documentation

- **Skills Guide**: [claude-skills-instructions.md](claude-skills-instructions.md) - Complete Anthropic documentation
- **Agents Guide**: [claude-agents-instructions.md](claude-agents-instructions.md) - Complete Anthropic documentation
- **Slash Commands**: [documentation/references/](documentation/references/) - Official Anthropic examples
- **Factory Templates**: [documentation/templates/](documentation/templates/) - 4 generation templates
- **Project Guide**: [CLAUDE.md](CLAUDE.md) - Repository structure and workflows

## Complementary Resources

**Claude Code Tresor** - [alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)
- Ready-to-use development workflow tools (8 skills, 8 agents, 4 slash commands)
- Immediate productivity gains with proven patterns
- One-command installation

**Claude Skills Library** - [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
- 37+ domain-specific production skills across 8 professional areas
- Marketing, Product, Engineering, C-Level Advisory expertise
- Battle-tested frameworks with proven ROI

**How They Work Together**:
- **This Factory**: Create custom skills/agents for unique requirements
- **Tresor**: Deploy ready-made development workflow tools
- **Skills Library**: Adopt domain-specific professional expertise

## External Resources

- **Anthropic Skills Docs**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- **Skills Marketplace**: https://github.com/anthropics/skills
- **Engineering Blog**: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- **API Documentation**: https://docs.claude.com/en/api/skills-guide

## Contributing

This is a reference repository. To contribute:
1. Fork the repository
2. Add new example skills to `claude-skills-examples/`
3. Ensure skills follow formatting standards
4. Include complete implementation with samples
5. Submit a pull request

## License

This repository provides examples and templates for creating Claude Skills. The skills you generate using these templates are yours to use as you see fit.

## Version

**Current Version**: 1.4.0
**Last Updated**: October 30, 2025
**Compatible With**: Claude Skills (all platforms), Claude Code Agents, Claude Code Slash Commands

**Latest Changes** (v1.4.0):
- Added Codex CLI Bridge skill for Claude Code ↔ OpenAI Codex CLI interoperability
- Added `/sync-agents-md` and `/codex-exec` slash commands
- AGENTS.md auto-generation capability for cross-tool compatibility
- Consolidated README.md for better focus on main capabilities

**Previous Changes** (v1.3.0):
- MASTER_SLASH_COMMANDS_PROMPT.md template with official Anthropic patterns
- Slash Command Factory v2.0 with 17 presets and 4-layer validation
- Three official command patterns (Simple, Multi-Phase, Agent-Style)

**Previous Changes** (v1.2.0):
- Prompt Factory skill with 69 presets across 15 domains
- Multi-format output (XML/Claude/ChatGPT/Gemini)
- 7-point quality validation system

---

**Ready to build?** Choose a factory template, fill in your details, and start generating production-ready skills, agents, prompts, or slash commands!

## Star History

<a href="https://www.star-history.com/#alirezarezvani/claude-code-skills-factory&alirezarezvani/claude-code-tresor&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=alirezarezvani/claude-code-skills-factory,alirezarezvani/claude-code-tresor&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=alirezarezvani/claude-code-skills-factory,alirezarezvani/claude-code-tresor&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=alirezarezvani/claude-code-skills-factory,alirezarezvani/claude-code-tresor&type=date&legend=top-left" />
 </picture>
</a>
