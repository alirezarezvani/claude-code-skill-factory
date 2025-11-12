# Claude Code Skills & Agents Factory

A comprehensive toolkit for generating production-ready Claude Skills and Claude Code Agents at scale. This repository provides templates, examples, and powerful prompt engineering systems to create custom skills and specialized agents for Claude AI across all platforms.

## 🚀 Quick Start (3 Shortcuts)

### Shortcut 1: Interactive Builder (Fastest)
```
I want to build something
```
The **factory-guide** agent asks what you need and delegates to specialist guides.

### Shortcut 2: Use Slash Commands
```bash
/build skill              # Interactive skill builder
/build agent              # Interactive agent builder
/build prompt             # Interactive prompt builder
/build hook               # Interactive hook builder
```

### Shortcut 3: Use Ready-Made Skills
```bash
# Install Prompt Factory (69 professional presets)
cp -r generated-skills/prompt-factory ~/.claude/skills/

# Ask Claude
"I need a prompt for [role name]"
```

---

## 📋 Built-in Commands

This toolkit includes **10 slash commands** and **5 interactive agents** to streamline your workflow:

### Workflow Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `/build` | Interactive builder (skill/agent/prompt/hook) | `/build skill` or `/build hook` |
| `/build-hook` | Build Claude Code hooks (Q&A, alias) | `/build-hook` |
| `/validate-output` | Validate generated output + auto-ZIP | `/validate-output hook [path]` |
| `/install-skill` | Install skills to Claude Code | `/install-skill [path]` |
| `/install-hook` | Install hooks to settings | `/install-hook [path] [user\|project]` |
| `/test-factory` | Run test examples | `/test-factory` |
| `/factory-status` | Check system status (all factories) | `/factory-status` |
| `/sync-agents-md` | Generate AGENTS.md from CLAUDE.md | `/sync-agents-md` |
| `/codex-exec` | Execute Codex CLI commands | `/codex-exec analysis "task"` |
| `/sync-todos-to-github` | Convert TodoWrite tasks to GitHub issues | `/sync-todos-to-github "Sprint 12"` |

### Interactive Guide Agents

| Agent | Purpose | Activation |
|-------|---------|-----------|
| **factory-guide** | Orchestrator - delegates to specialists | "I want to build something" |
| **skills-guide** | Build Claude Skills (4-5 questions) | "Build a skill" |
| **prompts-guide** | Use Prompt Factory (69 presets) | "Generate a prompt" |
| **agents-guide** | Build Claude Code Agents (5-6 questions) | "Create an agent" |
| **hooks-guide** | Build Claude Code Hooks (5-7 questions) | "Build a hook" |

See [.claude/agents/README.md](.claude/agents/README.md) and [.claude/commands/README.md](.claude/commands/README.md) for complete documentation.

---

## 🎯 Main Capabilities

### 1. Skills Factory
Generate complete, production-ready Claude Skills with:
- Properly formatted SKILL.md with YAML frontmatter
- Python implementation files (when needed)
- Sample input/output data
- Complete documentation and usage guides
- ZIP packages for easy distribution

**Template**: [SKILLS_FACTORY_PROMPT.md](documentation/templates/SKILLS_FACTORY_PROMPT.md)
**Shortcut**: `/build skill` or "I want to build a skill"

### 2. Agents Factory
Create specialized Claude Code Agents with:
- Enhanced YAML frontmatter (name, description, tools, model, color, field, expertise)
- MCP integration support
- Auto-invocation capabilities
- Tool access configuration

**Template**: [AGENTS_FACTORY_PROMPT.md](documentation/templates/AGENTS_FACTORY_PROMPT.md)
**Shortcut**: `/build agent` or "I want to create an agent"

### 3. Prompt Factory
Generate mega-prompts for any role with:
- 69 professional presets across 15 domains
- Multiple output formats (XML, Claude, ChatGPT, Gemini)
- 7-point quality validation
- Core & Advanced modes

**Ready-to-use Skill**: [generated-skills/prompt-factory/](generated-skills/prompt-factory/)
**Shortcut**: Install skill, then "I need a prompt for [role]"

### 4. Hooks Factory
Generate Claude Code hooks for workflow automation with:
- 7 event types (SessionStart, PostToolUse, SubagentStop, etc.)
- Safety validation (tool detection, silent failure, no destructive ops)
- Language-specific templates (Python/Black, JS/Prettier, Rust/rustfmt, Go/gofmt)
- Interactive Q&A generation (5-7 questions)
- Automatic security checks before installation

**Template**: [HOOKS_FACTORY_PROMPT.md](documentation/templates/HOOKS_FACTORY_PROMPT.md)
**Implementation**: [generated-skills/hook-factory/](generated-skills/hook-factory/)
**Shortcut**: `/build hook` or "I want to build a hook"

### 5. Slash Command Factory
Create custom slash commands with:
- 17 preset commands (business, development, documentation, analysis)
- Three official Anthropic patterns (Simple, Multi-Phase, Agent-Style)
- Comprehensive 4-layer validation
- Auto-generated bash permissions

**Template**: [MASTER_SLASH_COMMANDS_PROMPT.md](documentation/templates/MASTER_SLASH_COMMANDS_PROMPT.md)
**Shortcut**: Use template directly or `/build` with custom workflow

### 6. Codex CLI Bridge
Enable Claude Code ↔ Codex CLI interoperability with:
- Automatic CLAUDE.md → AGENTS.md translation
- Reference-based architecture (no duplication)
- Safety mechanisms and auto-validation
- Cross-tool team collaboration support

**Skill**: [generated-skills/codex-cli-bridge/](generated-skills/codex-cli-bridge/)
**Shortcut**: `/sync-agents-md` to sync documentation

---

## 🔄 Complete Workflow Examples

### Example 1: Build a Skill in 2 Minutes
```bash
# Step 1: Start builder
/build skill

# Step 2: Answer 4-5 questions
# (Claude guides you through the process)

# Step 3: Validate output
/validate-output

# Step 4: Install
/install-skill

# Done! Your skill is ready to use
```

### Example 2: Generate Cross-Platform Prompt
```bash
# Step 1: Install Prompt Factory (one-time)
cp -r generated-skills/prompt-factory ~/.claude/skills/

# Step 2: Ask Claude
"I need a prompt for a Senior DevOps Engineer"

# Step 3: Answer 5-7 questions
# (Select format: XML, Claude, ChatGPT, or Gemini)

# Done! Copy and paste into your preferred LLM
```

### Example 3: Sync for Codex CLI Team
```bash
# Step 1: Ensure CLAUDE.md exists in your project
# (If missing, run /init first)

# Step 2: Generate AGENTS.md for Codex CLI users
/sync-agents-md

# Step 3: Commit to repo
git add AGENTS.md
git commit -m "docs: Add AGENTS.md for Codex CLI compatibility"

# Done! Codex CLI users can now reference your skills
```

---

## 📁 Repository Structure

```
claude-code-skills-factory/
├── README.md                              # This file
├── CLAUDE.md                              # Repository guidance
├── AGENTS.md                              # Codex CLI documentation (auto-generated)
├── CHANGELOG.md                           # Version history
├── .claude/
│   ├── agents/                            # 5 interactive guide agents
│   │   ├── factory-guide.md              # Orchestrator
│   │   ├── skills-guide.md               # Skills builder
│   │   ├── prompts-guide.md              # Prompts generator
│   │   ├── agents-guide.md               # Agents creator
│   │   └── hooks-guide.md                # Hooks builder
│   └── commands/                          # 8 slash commands
│       ├── build.md                       # Interactive builder
│       ├── build-hook.md                  # Hook builder
│       ├── validate-output.md             # Validation + ZIP
│       ├── install-skill.md               # Installation guide
│       ├── test-factory.md                # Test runner
│       ├── factory-status.md              # Status checker
│       ├── sync-agents-md.md              # CLAUDE.md → AGENTS.md
│       └── codex-exec.md                  # Codex CLI executor
├── claude-skills-examples/                # 3 reference implementations
├── documentation/
│   ├── references/                        # Official Anthropic examples
│   └── templates/                         # 4 factory prompt templates
├── generated-skills/                      # 9 production-ready skills
│   ├── aws-solution-architect/            # AWS architecture & IaC
│   ├── content-trend-researcher/          # Multi-platform content research
│   ├── ms365-tenant-manager/              # Microsoft 365 administration
│   ├── agent-factory/                     # Agent generation system
│   ├── prompt-factory/                    # Prompt generation powerhouse
│   ├── slash-command-factory/             # Slash command generation
│   ├── codex-cli-bridge/                  # Claude Code ↔ Codex CLI bridge
│   ├── hook-factory/                      # Claude Code hooks automation
│   └── claude-md-enhancer/                # CLAUDE.md generation & maintenance
├── generated-agents/                      # Specialized agents
│   └── claude-md-guardian/                # CLAUDE.md maintenance agent
└── generated-commands/                    # Custom slash commands
    └── enhance-claude-md/                 # CLAUDE.md enhancement command
```

---

## 🎁 Production Skills Included

All skills include complete implementation, documentation, samples, and distribution packages:

### 1. AWS Solution Architect (53 KB)
Serverless architecture, IaC templates, cost optimization
- [View Skill](generated-skills/aws-solution-architect/)

### 2. Content Trend Researcher (35 KB)
Multi-platform trend analysis, SEO-optimized outlines
- [View Skill](generated-skills/content-trend-researcher/)

### 3. Microsoft 365 Tenant Manager (40 KB)
M365 administration, PowerShell automation
- [View Skill](generated-skills/ms365-tenant-manager/)

### 4. Agent Factory (12 KB)
Generate custom Claude Code agents with enhanced YAML
- [View Skill](generated-skills/agent-factory/)

### 5. Prompt Factory (427 KB)
69 professional presets, multi-format output, 7-point validation
- [View Skill](generated-skills/prompt-factory/)
- **Most Popular** - Install first for instant productivity

### 6. Slash Command Factory (26 KB)
17 presets, official Anthropic patterns, 4-layer validation
- [View Skill](generated-skills/slash-command-factory/)

### 7. Codex CLI Bridge (48 KB)
Claude Code ↔ Codex CLI interoperability, AGENTS.md generation
- [View Skill](generated-skills/codex-cli-bridge/)
- Enables cross-tool team collaboration

### 8. Hook Factory v2.0 (92 KB) 🆕
Build custom Claude Code hooks through interactive 7-question Q&A with automated installation and enhanced validation
- [View Skill](generated-skills/hook-factory/)
- **v2.0** - 10 production templates, automated installer (Python + Bash), secrets detection, event-specific validation

### 9. CLAUDE.md Enhancer (50 KB) 🆕
Analyze, generate, and enhance CLAUDE.md files with 100% native format compliance, interactive initialization, and automatic maintenance
- [View Skill](generated-skills/claude-md-enhancer/)
- **Ecosystem**: Skill + Agent + Slash Command for complete CLAUDE.md lifecycle management
- **Features**: Interactive workflow, quality scoring (0-100), modular architecture, 7 built-in examples
- **Companion Agent**: [claude-md-guardian](generated-agents/claude-md-guardian/) - Background maintenance with auto-sync
- **Slash Command**: `/enhance-claude-md` - Initialize or enhance CLAUDE.md files

---

## 💡 Reference Examples

Three fully-functional example skills demonstrating different patterns:

- **Analyzing Financial Statements** - Calculation engine + interpretation layer
- **Creating Financial Models** - DCF valuation, sensitivity analysis, Monte Carlo simulation
- **Applying Brand Guidelines** - Corporate branding application

See [claude-skills-examples/](claude-skills-examples/) for implementation details.

---

## ✨ Key Features

- **Production-Ready Output** - Proper YAML frontmatter, type-annotated Python, error handling
- **Interactive Workflows** - Guided conversations through 4 specialist agents
- **Built-in Automation** - 7 slash commands for common tasks
- **Complete Packaging** - Documentation, samples, ZIP files included
- **Smart Detection** - Automatically determines when Python code is needed vs prompt-only
- **Multi-Format Support** - XML, Claude, ChatGPT, Gemini output formats
- **Official Patterns** - Based on Anthropic documentation and examples
- **Cross-Platform** - Works with Claude AI (desktop/browser), Claude Code, and API
- **Cross-Tool Compatibility** - Bridge to OpenAI Codex CLI

---

## 📚 Documentation

- **Skills Guide**: [documentation/references/claude-skills-instructions.md](documentation/references/claude-skills-instructions.md) - Complete Anthropic documentation
- **Agents Guide**: [documentation/references/claude-agents-instructions.md](documentation/references/claude-agents-instructions.md) - Complete Anthropic documentation
- **Codex CLI Reference**: [documentation/references/openai-codex-cli-instructions.md](documentation/references/openai-codex-cli-instructions.md) - Complete OpenAI Codex CLI documentation
- **Slash Commands Examples**: [documentation/references/](documentation/references/) - Official Anthropic examples
- **Factory Templates**: [documentation/templates/](documentation/templates/) - 4 generation templates
- **Project Guide**: [CLAUDE.md](CLAUDE.md) - Repository structure and workflows
- **Interactive Agents**: [.claude/agents/README.md](.claude/agents/README.md) - Guide agent documentation
- **Slash Commands**: [.claude/commands/README.md](.claude/commands/README.md) - Command reference

---

## 🔗 Complementary Resources

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

---

## 🌐 External Resources

- **Anthropic Skills Docs**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- **Skills Marketplace**: https://github.com/anthropics/skills
- **Engineering Blog**: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- **API Documentation**: https://docs.claude.com/en/api/skills-guide

---

## 🤝 Contributing

This is a reference repository. To contribute:
1. Fork the repository
2. Add new example skills to `claude-skills-examples/`
3. Ensure skills follow formatting standards
4. Include complete implementation with samples
5. Submit a pull request

---

## 📄 License

This repository provides examples and templates for creating Claude Skills. The skills you generate using these templates are yours to use as you see fit.

---

## 📊 Version

**Current Version**: 1.4.0
**Last Updated**: October 30, 2025
**Compatible With**: Claude Skills (all platforms), Claude Code Agents, Claude Code Slash Commands

**Latest Changes** (v1.4.0):
- ✨ Added **Codex CLI Bridge** skill for Claude Code ↔ OpenAI Codex CLI interoperability
- ✨ Added `/sync-agents-md` and `/codex-exec` slash commands
- ✨ AGENTS.md auto-generation capability for cross-tool compatibility
- 📝 Consolidated README.md for better focus on main capabilities and shortcuts
- 🚀 Enhanced Quick Start with 3 shortcuts and workflow examples

**Previous Changes** (v1.3.0):
- MASTER_SLASH_COMMANDS_PROMPT.md template with official Anthropic patterns
- Slash Command Factory v2.0 with 17 presets and 4-layer validation
- Three official command patterns (Simple, Multi-Phase, Agent-Style)

**Previous Changes** (v1.2.0):
- Prompt Factory skill with 69 presets across 15 domains
- Multi-format output (XML/Claude/ChatGPT/Gemini)
- 7-point quality validation system

**See**: [CHANGELOG.md](CHANGELOG.md) for complete version history

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=alirezarezvani/claude-code-skill-factory&type=date&legend=bottom-right)](https://star-history.com/#alirezarezvani/claude-code-skill-factory&Date)

---

**Ready to build?** Try one of the shortcuts above, or explore the [factory templates](documentation/templates/) to start generating production-ready skills, agents, prompts, or slash commands!
