# Claude Code Skills & Agents Factory

A comprehensive toolkit for generating production-ready Claude Skills and Claude Code Agents at scale. This repository provides templates, examples, and powerful prompt engineering systems to create custom skills and specialized agents for Claude AI across all platforms (Claude apps, Claude Code, and API).

**🆕 NEW**: Interactive navigation agents + slash commands for guided skill building! [See Interactive Navigation System](#interactive-navigation-system)

## Table of Contents

- [Interactive Navigation System](#interactive-navigation-system)
  - [The 4 Guide Agents](#the-4-guide-agents)
  - [5 Slash Commands](#5-slash-commands)
  - [Complete Workflow Example](#complete-workflow-example)
- [What Are Claude Skills?](#what-are-claude-skills)
- [What Are Claude Code Agents?](#what-are-claude-code-agents)
- [Repository Contents](#repository-contents)
- [Quick Start](#quick-start)
  - [Option A: Generate Claude Skills](#option-a-generate-claude-skills-multi-file-capabilities)
  - [Option B: Generate Claude Code Agents](#option-b-generate-claude-code-agents-single-file-specialists)
  - [Option C: Generate Production-Ready Prompts](#option-c-generate-production-ready-prompts-prompt-factory)
- [Example Skills Included](#example-skills-included)
  - [1. Analyzing Financial Statements](#1-analyzing-financial-statements)
  - [2. Creating Financial Models](#2-creating-financial-models)
  - [3. Applying Brand Guidelines](#3-applying-brand-guidelines)
- [Generated Skills](#generated-skills)
  - [4. AWS Solution Architect](#4-aws-solution-architect)
  - [5. Content Trend Researcher](#5-content-trend-researcher)
  - [6. Microsoft 365 Tenant Manager](#6-microsoft-365-tenant-manager)
  - [7. Prompt Factory](#7-prompt-factory)
  - [8. Slash Command Factory](#8-slash-command-factory)
  - [9. Codex CLI Bridge](#9-codex-cli-bridge)
- [Key Features](#key-features)
- [Skill Architecture Patterns](#skill-architecture-patterns)
- [Best Practices](#best-practices)
- [Customization Guide](#customization-guide)
- [YAML Frontmatter Rules](#yaml-frontmatter-rules)
- [Technical Details](#technical-details)
- [Resources](#resources)
- [Public Gists (SEO & AEO)](#public-gists-seo--aeo)
- [Complementary Resources](#complementary-resources)
- [Real-World Examples](#real-world-examples)
- [Contributing](#contributing)
- [License](#license)
- [Version](#version)
- [Quick Reference](#quick-reference)

---

## What Are Claude Skills?

Claude Skills are specialized capabilities that teach Claude how to perform specific tasks. They're packaged as folders containing:

- **SKILL.md**: Structured instructions with YAML frontmatter
- **Python files** (optional): Functional code for calculations, data processing, or file generation
- **Sample data**: JSON examples showing inputs and expected outputs
- **Usage guide**: Clear invocation examples

Skills are **composable** (work together), **portable** (same format everywhere), and **efficient** (loaded only when relevant).

## What Are Claude Code Agents?

Claude Code Agents (also called sub-agents) are specialized AI assistants that handle specific types of tasks. They're single Markdown files with YAML frontmatter containing:

- **Enhanced YAML frontmatter**: name, description, tools, model, color, field, expertise, MCP integrations
- **System prompt**: Detailed instructions for the agent's behavior and approach
- **Auto-invocation**: Claude automatically uses them when the description matches the task

Agents are **focused** (one responsibility), **efficient** (separate context window), **flexible** (configurable tool access), and **composable** (multiple agents work together on complex workflows).

**Key Difference:**
- **Skills** = Multi-file capabilities (folders with SKILL.md + Python + samples)
- **Agents** = Single-file specialists (.md files in `.claude/agents/`)

## Repository Contents

```
claude-code-skills-factory/
├── README.md                              # This file
├── CLAUDE.md                              # Repository guidance for Claude Code
├── AGENTS.md                              # Codex CLI documentation (auto-generated)
├── claude-skills-instructions.md          # Full Skills documentation from Anthropic
├── claude-agents-instructions.md          # Full Agents documentation from Anthropic
├── .claude/
│   └── commands/                          # Slash commands
│       ├── sync-agents-md.md              # Regenerate AGENTS.md from CLAUDE.md
│       └── codex-exec.md                  # Execute Codex CLI commands
├── claude-skills-examples/                # Reference skill implementations
│   ├── analyzing_financial_statements.md
│   ├── calculate_ratios.py
│   ├── interpret_ratios.py
│   ├── creating-financial-models.md
│   ├── dcf_model.py
│   ├── sensitivity_analysis.py
│   ├── brand_guidelines.md
│   └── apply_brand.py
├── documentation/
│   ├── references/                        # Official documentation examples
│   │   ├── slash-commands-instructions.md
│   │   ├── slash-command-code-review-example.md
│   │   ├── slash-command-codebase-analysis-example.md
│   │   ├── slash-command-open-api-example.md
│   │   ├── slash-command-update-claude-md-example.md
│   │   └── slash-commands-ultrathink-example.md
│   └── templates/                         # Factory prompt templates
│       ├── SKILLS_FACTORY_PROMPT.md       # Generate Claude Skills (multi-file)
│       ├── AGENTS_FACTORY_PROMPT.md       # Generate Claude Code Agents (single .md)
│       ├── PROMPTS_FACTORY_PROMPT.md      # Generate domain prompt builders
│       └── MASTER_SLASH_COMMANDS_PROMPT.md # Generate slash commands (official patterns)
└── generated-skills/                      # Production-ready generated skills
    ├── aws-solution-architect/            # AWS architecture (53 KB)
    ├── content-trend-researcher/          # Multi-platform content research (35 KB)
    ├── ms365-tenant-manager/              # Microsoft 365 administration (40 KB)
    ├── psychology-advisor/                # Mental wellness & CBT techniques (31 KB)
    ├── agent-factory/                     # Claude Code agent generation (12 KB)
    ├── prompt-factory/                    # Prompt generation powerhouse (427 KB)
    ├── slash-command-factory/             # Slash command generation - 17 presets (26 KB)
    └── codex-cli-bridge/                  # Claude Code ↔ Codex CLI interoperability (48 KB)
```

## Quick Start

### Option A: Generate Claude Skills (Multi-file Capabilities)

#### 1. Use the Skills Factory Prompt

Open [documentation/templates/SKILLS_FACTORY_PROMPT.md](documentation/templates/SKILLS_FACTORY_PROMPT.md) and scroll to the bottom.

Fill in the template variables:

```
=== FILL IN YOUR DETAILS BELOW ===

BUSINESS_TYPE: SaaS startup (project management tool)

USE_CASES: Analyze user feedback sentiment, Generate feature prioritization reports, Create customer success playbooks

NUMBER_OF_SKILLS: 3

ADDITIONAL_CONTEXT: Use data-driven decision making, modern tech stack
```

### 2. Generate Your Skills

Copy the entire prompt (including your filled variables) and paste it into:
- **Claude.ai** (any plan with Skills enabled)
- **Claude Code**
- **Claude API** (with Code Execution Tool)

Claude will generate complete skill packages with:
- ✅ Properly formatted SKILL.md files (kebab-case names in YAML)
- ✅ Python implementation files (when functional code is needed)
- ✅ Sample input/output JSON files
- ✅ HOW_TO_USE.md with invocation examples
- ✅ ZIP files ready for import into Claude AI desktop

### 3. Install Your Skills

**Claude AI Desktop:**
- Import the generated `.zip` files directly through the Skills menu

**Claude Code:**
- Copy skill folders to `~/.claude/skills/`

**Claude Apps (Browser):**
- Use the "skill-creator" skill to import

**API:**
- Use the `/v1/skills` endpoint to upload

### Option B: Generate Claude Code Agents (Single-file Specialists)

#### 1. Use the Agents Factory Prompt

Open [documentation/templates/AGENTS_FACTORY_PROMPT.md](documentation/templates/AGENTS_FACTORY_PROMPT.md) and scroll to the bottom.

Fill in the template variables:

```
=== FILL IN YOUR DETAILS BELOW ===

AGENT_NAME: api-integration-specialist
AGENT_TYPE: Implementation
DOMAIN_FIELD: backend
DESCRIPTION: API integration expert. Use when building API clients.
TOOLS_NEEDED: Read, Write, Edit, Bash
MODEL: sonnet
COLOR: green
EXPERTISE_LEVEL: expert
MCP_TOOLS: mcp__github
```

#### 2. Generate Your Agent

Copy the entire prompt and paste into Claude. You'll get a complete agent .md file:

```markdown
---
name: api-integration-specialist
description: API integration expert...
tools: Read, Write, Edit, Bash
model: sonnet
color: green
field: backend
expertise: expert
mcp_tools: mcp__github
---

System prompt with detailed instructions...
```

#### 3. Install Your Agent

**Project-level** (shared with team):
```bash
cp api-integration-specialist.md .claude/agents/
```

**User-level** (available everywhere):
```bash
cp api-integration-specialist.md ~/.claude/agents/
```

Agent auto-invokes when Claude detects relevant tasks!

### Option C: Generate Production-Ready Prompts (Prompt Factory)

#### 1. Use the Prompt Factory Skill

The Prompt Factory is a ready-to-use skill (not a template) that generates world-class mega-prompts for any role, industry, and task.

**Install the skill**:
```bash
# Copy to your skills directory
cp -r generated-skills/prompt-factory ~/.claude/skills/

# Or import the ZIP in Claude Desktop
# File: generated-skills/prompt-factory.zip (403 KB)
```

#### 2. Generate Your Prompt

**Interactive Mode** (Recommended):
```
I need a prompt for a Senior Full-Stack Engineer
```

Claude will ask 5-7 questions and generate a complete mega-prompt.

**Custom Mode**:
```
Create a custom prompt for [your specific role/need]
```

Answer the intelligent question flow (max 7 questions) and select:
- **Format**: XML, Claude, ChatGPT, Gemini, or All
- **Mode**: Core (~5K tokens) or Advanced (~12K tokens with testing scenarios)

#### 3. Use Your Generated Prompt

Copy the generated prompt and use it in:
- **Claude AI**: Paste at start of conversation
- **ChatGPT**: Use Custom Instructions feature
- **Gemini**: Paste as system configuration
- **Any LLM**: Universal XML format

**Features**:
- ✅ 69 quick-start presets across 15 professional domains
- ✅ Technical (8), Business (8), Legal (4), Finance (4), HR (4), Design (4), Customer (4), Executive (7), Specialized-Technical (6), Research (3), Creative-Media (4), Manufacturing (4), R&D (2), Regulatory (1), Specialized (3)
- ✅ Multiple output formats (XML/Claude/ChatGPT/Gemini)
- ✅ 7-point quality validation before delivery
- ✅ Contextual best practices from OpenAI, Anthropic, Google
- ✅ Core & Advanced modes (with testing scenarios and variations)
- ✅ Token count optimization and reporting

**Pattern**: 7-question flow → preset matching → template synthesis → quality validation → multi-format output

**See**: [generated-skills/prompt-factory/](generated-skills/prompt-factory/) for complete documentation

### 8. Slash Command Factory (v2.0)
**Purpose**: Generate custom Claude Code slash commands following official Anthropic patterns for workflows, automation, and productivity

**Files**:
- [SKILL.md](generated-skills/slash-command-factory/SKILL.md)
- [command_generator.py](generated-skills/slash-command-factory/command_generator.py)
- [validator.py](generated-skills/slash-command-factory/validator.py)
- [presets.json](generated-skills/slash-command-factory/presets.json)
- [HOW_TO_USE.md](generated-skills/slash-command-factory/HOW_TO_USE.md)

**Capabilities**:
- **17 preset slash commands** (10 original + 7 official Anthropic examples): business research, content analysis, medical translation, compliance audit, API building, test automation, documentation generation, knowledge extraction, workflow optimization, agent coordination, code review, codebase analysis, OpenAPI sync, ultrathink coordination
- **Three official command patterns integrated**:
  - **Simple Pattern** (code-review): Context → Task (straightforward workflows)
  - **Multi-Phase Pattern** (codebase-analyze): Discovery → Analysis → Task (complex documentation)
  - **Agent-Style Pattern** (ultrathink, openapi-sync): Role → Process → Guidelines (expert coordination)
- **5-7 question flow** for custom command creation with auto-detect structure pattern
- **Comprehensive validation** (4 layers): Command name (kebab-case, 2-4 words), bash permissions (specific commands only, NEVER wildcard `Bash`), arguments usage ($ARGUMENTS, never $1/$2/$3), YAML structure
- **Smart generation**: Auto-detect command structure, auto-generate bash permissions (git commands, discovery commands, comprehensive commands), automatic kebab-case naming conversion
- Generates properly formatted command .md files with YAML frontmatter
- Outputs to `generated-commands/[name]/` in user's project
- Excellent folder organization (all .md in root, standards/examples/scripts/ separate)

**Official Presets**:
- **Business Intelligence**: /research-business, /research-content
- **Healthcare & Compliance**: /medical-translate, /compliance-audit
- **Development**: /api-build, /test-auto, /code-review, /openapi-sync
- **Documentation**: /docs-generate, /knowledge-mine, /update-docs
- **Analysis**: /codebase-analyze, /deps-audit, /metrics-report
- **Productivity**: /workflow-analyze, /batch-agents, /ultrathink

**Pattern**: Preset selection (17 commands) OR custom generation (5-7 questions) → auto-detect structure pattern → YAML frontmatter creation → strict validation → organized output

**Based on**: 6 official Anthropic slash command examples in [documentation/references/](documentation/references/)

**See**: [HOW_TO_USE.md](generated-skills/slash-command-factory/HOW_TO_USE.md) for complete usage guide and [MASTER_SLASH_COMMANDS_PROMPT.md](documentation/templates/MASTER_SLASH_COMMANDS_PROMPT.md) for the master template

### 9. Codex CLI Bridge
**Purpose**: Seamless interoperability between Claude Code and OpenAI Codex CLI for cross-tool team collaboration

**Files**:
- [SKILL.md](generated-skills/codex-cli-bridge/SKILL.md)
- [bridge.py](generated-skills/codex-cli-bridge/bridge.py) - Main orchestrator
- [safety_mechanism.py](generated-skills/codex-cli-bridge/safety_mechanism.py) - Environment validation
- [claude_parser.py](generated-skills/codex-cli-bridge/claude_parser.py) - CLAUDE.md parser
- [project_analyzer.py](generated-skills/codex-cli-bridge/project_analyzer.py) - Project structure analysis
- [agents_md_generator.py](generated-skills/codex-cli-bridge/agents_md_generator.py) - AGENTS.md generation
- [skill_documenter.py](generated-skills/codex-cli-bridge/skill_documenter.py) - Skill documentation
- [codex_executor.py](generated-skills/codex-cli-bridge/codex_executor.py) - Codex CLI helpers
- [README.md](generated-skills/codex-cli-bridge/README.md), [HOW_TO_USE.md](generated-skills/codex-cli-bridge/HOW_TO_USE.md)

**Capabilities**:
- **CLAUDE.md → AGENTS.md translation** - Automatic generation of Codex CLI-compatible documentation
- **Reference-based architecture** - Links to existing files, no content duplication
- **Skill documentation for Codex users** - Different approaches for functional vs prompt-based skills
- **Safety mechanisms** - Auto-validates Codex CLI installation, auto-runs /init if CLAUDE.md missing
- **Codex execution helpers** - Python wrappers for Codex CLI commands (always uses `codex exec`, intelligent model selection)
- **Slash command integration** - `/sync-agents-md` and `/codex-exec` commands
- **Cross-tool compatibility** - Enables teams to use both Claude Code and Codex CLI seamlessly

**Use Cases**:
- Cross-tool teams (Claude Code + Codex CLI users)
- Project migration (Claude Code ↔ Codex CLI)
- CI/CD integration (auto-sync AGENTS.md when CLAUDE.md changes)
- Skills marketplace (universal compatibility)

**Pattern**: Safety validation → CLAUDE.md parsing → project analysis → AGENTS.md generation → reference-based documentation

**Output**: AGENTS.md file in project root with complete skill documentation, workflow patterns, and command reference for Codex CLI users

**See**: [HOW_TO_USE.md](generated-skills/codex-cli-bridge/HOW_TO_USE.md) for comprehensive usage guide and examples

## Example Skills Included

This repository includes three fully-functional example skills:

### 1. Analyzing Financial Statements
**Purpose**: Calculate and interpret financial ratios (ROE, ROA, liquidity, leverage, etc.)

**Files**:
- [analyzing_financial_statements.md](claude-skills-examples/analyzing_financial_statements.md)
- [calculate_ratios.py](claude-skills-examples/calculate_ratios.py)
- [interpret_ratios.py](claude-skills-examples/interpret_ratios.py)

**Pattern**: Calculation engine + interpretation layer

### 2. Creating Financial Models
**Purpose**: DCF valuation, Monte Carlo simulation, sensitivity analysis

**Files**:
- [creating-financial-models.md](claude-skills-examples/creating-financial-models.md)
- [dcf_model.py](claude-skills-examples/dcf_model.py)
- [sensitivity_analysis.py](claude-skills-examples/sensitivity_analysis.py)

**Pattern**: Historical data → projections → valuation

### 3. Applying Brand Guidelines
**Purpose**: Apply consistent corporate branding to documents

**Files**:
- [brand_guidelines.md](claude-skills-examples/brand_guidelines.md)
- [apply_brand.py](claude-skills-examples/apply_brand.py)

**Pattern**: Brand definition + application logic

## Generated Skills

This repository also includes production-ready skills generated using the Skills Factory Prompt, demonstrating the quality and completeness of output you can expect.

### 4. AWS Solution Architect
**Purpose**: Expert AWS architecture design for startups - serverless, scalable, and cost-effective cloud infrastructure

**Files**:
- [SKILL.md](generated-skills/aws-solution-architect/SKILL.md)
- [architecture_designer.py](generated-skills/aws-solution-architect/architecture_designer.py)
- [cost_optimizer.py](generated-skills/aws-solution-architect/cost_optimizer.py)
- [serverless_stack.py](generated-skills/aws-solution-architect/serverless_stack.py)

**Capabilities**:
- Serverless architecture design (Lambda, API Gateway, DynamoDB, EventBridge)
- Infrastructure as Code (CloudFormation, CDK, Terraform)
- Cost optimization and budget management
- Security best practices and compliance
- CI/CD pipeline setup
- Multi-region deployment strategies

**Pattern**: Architecture design → IaC templates → cost optimization

### 5. Content Trend Researcher
**Purpose**: Advanced content research analyzing trends across 10+ platforms to generate data-driven article outlines

**Files**:
- [SKILL.md](generated-skills/content-trend-researcher/SKILL.md)
- [trend_analyzer.py](generated-skills/content-trend-researcher/trend_analyzer.py)
- [intent_analyzer.py](generated-skills/content-trend-researcher/intent_analyzer.py)
- [platform_insights.py](generated-skills/content-trend-researcher/platform_insights.py)
- [outline_generator.py](generated-skills/content-trend-researcher/outline_generator.py)

**Capabilities**:
- Multi-platform trend analysis (Google Trends, Reddit, YouTube, Medium, Substack, LinkedIn, X, etc.)
- User intent analysis (informational, commercial, transactional)
- Content gap identification
- SEO-optimized article outline generation
- Platform-specific best practices and publishing strategies

**Pattern**: Trend analysis → intent analysis → content gap discovery → outline generation

### 6. Microsoft 365 Tenant Manager
**Purpose**: Comprehensive M365 tenant administration for setup, security, user management, and organizational optimization

**Files**:
- [SKILL.md](generated-skills/ms365-tenant-manager/SKILL.md)
- [tenant_setup.py](generated-skills/ms365-tenant-manager/tenant_setup.py)
- [user_management.py](generated-skills/ms365-tenant-manager/user_management.py)
- [powershell_generator.py](generated-skills/ms365-tenant-manager/powershell_generator.py)

**Capabilities**:
- Tenant setup and configuration
- User and group lifecycle management
- Security and compliance policies (Conditional Access, MFA, DLP)
- SharePoint, OneDrive, and Teams administration
- Exchange Online management
- PowerShell automation script generation
- License management and cost optimization

**Pattern**: Configuration requirements → PowerShell scripts → validation checklists

### 7. Prompt Factory
**Purpose**: World-class prompt powerhouse for generating production-ready mega-prompts for any role, industry, and task

**Files**:
- [SKILL.md](generated-skills/prompt-factory/SKILL.md)
- [generate_prompt.py](generated-skills/prompt-factory/scripts/generate_prompt.py)
- [validator.py](generated-skills/prompt-factory/scripts/validator.py)
- [optimizer.py](generated-skills/prompt-factory/scripts/optimizer.py)
- [batch_generator.py](generated-skills/prompt-factory/scripts/batch_generator.py)

**Capabilities**:
- 69 comprehensive presets across 15 professional domains
- Intelligent 7-question flow for requirement gathering
- Multiple output formats (XML/Claude/ChatGPT/Gemini)
- 7-point quality validation before delivery
- Contextual best practices from OpenAI, Anthropic, Google
- Core & Advanced modes with testing scenarios
- Complete coverage: Technical (8), Business (8), Legal (4), Finance (4), HR (4), Design (4), Customer (4), Executive (7), Specialized-Technical (6), Research (3), Creative-Media (4), Manufacturing (4), R&D (2), Regulatory (1), Specialized (3)

**Pattern**: 7-question flow → preset selection → quality validation → multi-format output

## Key Features

### 🎯 Production-Ready Output
Every generated skill follows enterprise standards:
- Proper YAML frontmatter with kebab-case names
- Type-annotated Python with error handling
- Safe operations (division by zero, missing data)
- Minimal, focused sample data

### 🔗 Composable Design
Skills are designed to work together:
- `data-extractor` → `data-analyzer` → `report-generator` → `brand-formatter`
- No duplicate functionality
- Clear input/output contracts

### 📦 Complete Packaging
Each skill includes everything needed:
- SKILL.md with structured documentation
- Python files (multi-file when needed)
- sample_input.json and expected_output.json
- HOW_TO_USE.md with invocation examples
- .zip file containing entire skill folder

### ⚡ Smart Implementation Detection
The prompt automatically determines:
- When Python code is needed vs. prompt-only
- Multi-file structure for complex skills
- Appropriate sample data formats

## Skill Architecture Patterns

### Prompt-Only Skills
For instructional or template-based tasks:
- Style guides and tone of voice
- Decision frameworks
- Content guidelines
- Brand voice standards

**No Python needed** - just structured instructions in SKILL.md

### Functional Skills
For computation, processing, or generation:
- Financial calculations
- Data analysis and transformation
- File generation (Excel, PDF, etc.)
- API interactions

**Python files included** - class-based, type-annotated, with safe operations

### Multi-File Skills
For complex functionality:
- `calculate_*.py` - Core computations
- `interpret_*.py` - Analysis and insights
- `format_*.py` - Output formatting
- `validate_*.py` - Input validation

## Best Practices

### When Creating Skills

1. **Keep skills focused** - One clear purpose per skill
2. **Make them composable** - Output of one skill feeds another
3. **Validate inputs** - Handle missing or invalid data gracefully
4. **Use kebab-case** - For YAML name fields and folder names
5. **Provide context** - Industry-specific considerations in documentation
6. **Include examples** - Clear invocation patterns in HOW_TO_USE.md

### When Using Skills

1. **Match to task** - Use the skill that fits your specific need
2. **Provide complete data** - Skills work best with full input data
3. **Check outputs** - Validate results against your requirements
4. **Combine skills** - Chain multiple skills for complex workflows

## Customization Guide

### Adapting Example Skills

To customize the included examples:

1. **Update YAML frontmatter** - Change `name` and `description` to match your use case
2. **Modify constants** - Replace Acme Corporation branding with yours
3. **Adjust calculations** - Modify formulas for your industry
4. **Extend functionality** - Add new methods to existing classes
5. **Simplify** - Remove features you don't need

### Creating New Skills

Use the Skills Factory Prompt with your specific:
- Business type and industry
- Specific use cases and tasks
- Number of skills needed
- Technical requirements and constraints

## YAML Frontmatter Rules

**CRITICAL**: Every SKILL.md must start with properly formatted YAML:

```yaml
---
name: skill-name-in-kebab-case
description: Brief one-line description of what this skill does
---
```

**Correct:**
```yaml
---
name: financial-ratios
description: Calculates key financial ratios from financial statement data
---
```

**Incorrect:**
```yaml
---
name: Financial Ratios  ❌ Title Case
name: financial_ratios  ❌ snake_case
name: financialRatios   ❌ camelCase
---
```

## Technical Details

### Python Standards

All Python files follow these conventions:
- Type hints for all functions and classes
- Docstrings with Args and Returns sections
- Safe operations (e.g., `safe_divide` to avoid division by zero)
- Class-based structure for stateful operations
- Modular design with separation of concerns

### File Naming

- **Folders**: `skill-name/` (kebab-case)
- **YAML name**: `name: skill-name` (kebab-case)
- **Python files**: `calculate_metrics.py` (snake_case - Python convention)
- **ZIP files**: `skill-name.zip` (kebab-case)

### Sample Data

Keep sample files minimal and focused:
- **sample_input.json**: Just enough data to test the skill
- **expected_output.json**: Clear structure showing what skill produces
- Use realistic but simple values
- Include all required fields

## Resources

### Documentation
- **Anthropic Skills Documentation**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- **Skills Marketplace**: https://github.com/anthropics/skills
- **Engineering Blog**: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

### Support
- **Claude Help Center**: https://support.claude.com/en/articles/12512176-what-are-skills
- **API Documentation**: https://docs.claude.com/en/api/skills-guide

## Public Gists (SEO & AEO)

Comprehensive guides published as GitHub Gists for improved visibility, SEO rankings, and Answer Engine Optimization (AEO) for ChatGPT, Perplexity, Claude, and other AI search engines.

### 🏥 Health SDK Builder - Healthcare AI Complete Guide
**Gist**: [health-sdk-builder-healthcare-ai-claude-agent.md](https://gist.github.com/alirezarezvani/d1efa1cf2fdab48c67467fb17abd769c)

Comprehensive guide for building HIPAA/GDPR/DSGVO-compliant healthcare applications with multilingual support (German + English), all therapy modalities (CBT, Psychodynamic, Psychoanalysis, Depth Psychology), German PTV 10 automation, and 2025 Claude API features.

**Keywords**: Healthcare AI, HIPAA compliance, GDPR, Mental health apps, Psychotherapy software, German PTV 10, Medical AI, Patient empowerment

### 🏭 Claude Skills & Agents Factory - Complete Guide
**Gist**: [claude-skills-agents-factory-complete-guide.md](https://gist.github.com/alirezarezvani/c12f2906d3801dfaacdb65ebe19a3ffe)

Overview of the entire factory system for generating Claude Skills, Claude Code Agents, and production-ready prompts. Includes all 6 production skills, healthcare specialization, and 2025 API features.

**Keywords**: Claude Skills, Claude Agents, Agent SDK, AI Automation, Healthcare AI, Multilingual AI, 2025 Claude API

### 🎯 Prompt Factory - AI Prompt Generation Tool
**Gist**: [prompt-factory-ai-prompt-generation-tool.md](https://gist.github.com/alirezarezvani/3f31fc5435eaa3fcb260d774286587ef)

World-class prompt generation with 69 professional presets across 15 domains, multi-format output (XML/Claude/ChatGPT/Gemini), and 7-point quality validation.

**Keywords**: Prompt Engineering, AI Prompts, ChatGPT Custom Instructions, Claude Prompts, Gemini Prompts, Multi-LLM Support

**See**: [GISTS.md](GISTS.md) for complete SEO/AEO strategy and update guidelines.

## Complementary Resources

Looking for ready-to-use Claude augmentation tools? These companion repositories provide battle-tested implementations that complement the factories in this project:

### 🔧 Claude Code Tresor
**Repository**: [alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)

A comprehensive collection of professional-grade utilities that supercharge your Claude Code development workflow. While this factory helps you **create** custom skills and agents, Claude Code Tresor provides **ready-to-use** implementations you can install immediately.

**What It Includes**:
- **8 Autonomous Skills (v2.0)**: Background helpers for code quality, testing, git commits, security auditing, documentation maintenance
- **8 Specialized Agents**: Expert sub-agents for code review, system architecture, debugging, performance optimization, refactoring
- **4 Slash Commands**: `/scaffold`, `/review`, `/test-gen`, `/docs-gen` for rapid workflow automation
- **20+ Prompt Templates**: Curated prompts for common development tasks
- **5 Development Standards**: Style guides and best practices
- **200+ Components**: Additional utilities in source library

**Installation**: One-command setup via `./scripts/install.sh` (completes in under 2 minutes)

**Perfect For**: Developers who want immediate productivity gains with proven patterns for code quality, testing, documentation, and architecture.

---

### 📚 Claude Skills Library
**Repository**: [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)

A production-ready library of 37+ domain-specific skills across 8 professional areas. While this factory provides **templates** for creating skills, the Skills Library offers **complete, specialized implementations** for specific business functions.

**What It Provides**:
- **37+ Production Skills**: Marketing (3), C-Level Advisory (2), Product Teams (5), Project Management (6), Engineering (9), and more
- **Domain Expertise Packages**: Each skill includes comprehensive documentation, Python analysis tools (CLI-based, no API dependencies), knowledge bases, and ready-to-use templates
- **Proven Results**: 40%+ time savings, 30%+ quality improvements through battle-tested frameworks

**Skill Categories**:
- **Marketing**: Content creation, demand generation, product marketing strategy
- **C-Level Advisory**: CEO and CTO strategic guidance
- **Product Teams**: PM toolkit, agile practices, UX research, design systems
- **Project Management**: Senior PM, Scrum mastery, Atlassian (Jira/Confluence) expertise
- **Engineering**: Architecture, frontend/backend, fullstack, QA, DevOps, security, code review

**Perfect For**: Teams and professionals seeking domain-specific expertise in marketing, product management, engineering, or business leadership with immediate deployment and no external API dependencies.

---

### How They Work Together

**This Factory (claude-code-skills-factory)**:
- ✨ **Create** custom skills and agents tailored to your specific needs
- 🏗️ Templates and generation systems for building from scratch
- 📖 Learning resource with detailed examples and patterns

**Claude Code Tresor**:
- ⚡ **Deploy** ready-made development workflow tools immediately
- 🛠️ Pre-built agents, commands, and automation for daily coding tasks
- 🎯 Focus on code quality, testing, and documentation automation

**Claude Skills Library**:
- 🎓 **Adopt** domain-specific professional expertise instantly
- 📦 Complete skill packages for specific business functions
- 💼 Battle-tested frameworks for marketing, product, engineering, and leadership

**Recommended Workflow**:
1. Start with **Claude Code Tresor** for immediate development productivity
2. Browse **Claude Skills Library** for domain-specific capabilities you need
3. Use **this Factory** to generate custom skills for unique requirements not covered by the other repositories

All three repositories work seamlessly with Claude AI and Claude Code across all platforms (desktop, browser, CLI, API).

---

**Legend**:
- 🔵 **claude-code-skills-factory** - This repository (Skills & Agents Factory)
- 🟢 **claude-code-tresor** - Development workflow utilities
- 🟠 **claude-skills** - Domain-specific skill library

## Real-World Examples

The `generated-skills/` folder contains actual production-ready skills created using the Skills Factory Prompt:

### AWS Solution Architect
Generated for startup infrastructure needs - includes architecture design, cost optimization, and IaC templates.

**See**: [generated-skills/aws-solution-architect/](generated-skills/aws-solution-architect/)

### Content Trend Researcher
Generated for content creators and marketers - analyzes trends across 10+ platforms and creates data-driven outlines.

**See**: [generated-skills/content-trend-researcher/](generated-skills/content-trend-researcher/)

### Microsoft 365 Tenant Manager (40 KB)
Generated for IT administrators - manages M365 tenant setup, security, and generates PowerShell automation scripts.

**See**: [generated-skills/ms365-tenant-manager/](generated-skills/ms365-tenant-manager/)

### Psychology Advisor (31 KB)
Evidence-based mental wellness skill with CBT techniques, mindfulness exercises, stress management, and emotional regulation tools.

**Key Features**: 10 cognitive distortion types, 4 breathing techniques, RAIN method, stress assessment, behavioral activation

**See**: [generated-skills/psychology-advisor/](generated-skills/psychology-advisor/)

### Content Trend Researcher (35 KB)
Multi-platform content research analyzing trends across Google, Reddit, YouTube, Medium, LinkedIn, X, Substack, and more to generate data-driven article outlines.

**Key Features**: User intent analysis, content gap discovery, platform-specific strategies, SEO-optimized outlines

**See**: [generated-skills/content-trend-researcher/](generated-skills/content-trend-researcher/)

### Agent Factory (12 KB)
Claude Code agent generation system that creates custom agents/sub-agents with enhanced YAML frontmatter, tool patterns, and MCP integration.

**Key Features**: Enhanced YAML (color, field, expertise), tool access patterns, execution safety, MCP tool suggestions

**See**: [generated-skills/agent-factory/](generated-skills/agent-factory/)
**Template**: [documentation/templates/AGENTS_FACTORY_PROMPT.md](documentation/templates/AGENTS_FACTORY_PROMPT.md)

### Prompt Factory (427 KB)
World-class prompt powerhouse that generates production-ready mega-prompts for any role, industry, and task through intelligent 7-question flow.

**Key Features**: 69 comprehensive presets across 15 professional domains (Technical, Business, Legal, Finance, HR, Design, Customer, Executive, Manufacturing, R&D, Regulatory, Specialized-Technical, Research, Creative-Media), multiple output formats (XML/Claude/ChatGPT/Gemini), 7-point quality validation gates, contextual best practices from OpenAI/Anthropic/Google

**Domains Covered**: Full-Stack Engineer, DevOps, Product Manager, Legal Counsel, CFO, HR Manager, UI/UX Designer, Customer Success, CEO, ML Engineer, Research Scientist, Copywriter, Manufacturing Engineer, Clinical Specialist, and 55+ more roles

**See**: [generated-skills/prompt-factory/](generated-skills/prompt-factory/)

Each includes full implementation, sample data, HOW_TO_USE guide, and ready-to-import ZIP files.

---

## Interactive Navigation System

**The easiest way to build Skills, Prompts, and Agents** - guided conversation with specialized agents!

### Quick Start

```
I want to build something
```

→ **factory-guide** asks what you want to build
→ Delegates to specialist
→ Specialist asks 3-6 questions
→ Complete output generated

### The 4 Guide Agents

**🟣 factory-guide** (Orchestrator) - Entry point, delegates to specialists
**🔵 skills-guide** (Skills) - Build multi-file Claude Skills (4-5 questions)
**🟠 prompts-guide** (Prompts) - Generate mega-prompts (3-4 questions, 69 presets)
**🟢 agents-guide** (Agents) - Build Claude Code Agents (5-6 questions)

**Docs**: [.claude/agents/README.md](.claude/agents/README.md)

### 5 Slash Commands

**Workflow**: `/build` → `/validate-output` → `/install-skill` → `/test-factory` → `/factory-status`

**Docs**: [.claude/commands/README.md](.claude/commands/README.md)

### Example: Build Healthcare Skill (15 min)
```
/build skill → Answer questions → /validate-output → /install-skill → /test-factory → Done!
```

---

## Contributing

This is a reference repository. To contribute:
1. Fork the repository
2. Add new example skills to `claude-skills-examples/`
3. Ensure skills follow all formatting standards
4. Include complete implementation with samples
5. Submit a pull request

## License

This repository provides examples and templates for creating Claude Skills. The skills you generate using these templates are yours to use as you see fit.

## Version

**Current Version**: 1.3.0
**Last Updated**: October 29, 2025
**Compatible With**: Claude Skills (all platforms), Claude Code Agents, and Claude Code Slash Commands

**Latest Changes** (v1.3.0):
- Added MASTER_SLASH_COMMANDS_PROMPT.md template - Comprehensive master template for generating slash commands following official Anthropic patterns
- Enhanced Slash Command Factory to v2.0 (26 KB) - Now includes 17 presets (10 original + 7 official Anthropic examples)
- Integrated three official command structure patterns: Simple (code-review), Multi-Phase (codebase-analyze), Agent-Style (ultrathink, openapi-sync)
- Added comprehensive four-layer validation: command name (kebab-case), bash permissions (specific only, never wildcard), arguments usage ($ARGUMENTS), YAML structure
- Added documentation/references/ folder with 6 official Anthropic slash command examples
- Smart auto-detection of command structure patterns and automatic bash permission generation

**Previous Changes** (v1.2.0):
- Added Prompt Factory skill (427 KB) - World-class prompt generation with 69 presets across 15 domains
- Expanded coverage: Technical, Business, Legal, Finance, HR, Design, Customer, Executive, Manufacturing, R&D, Regulatory, Specialized-Technical, Research, Creative-Media domains
- Multi-format output support (XML/Claude/ChatGPT/Gemini)

---

## Quick Reference

- **Create Skills**: Use [SKILLS_FACTORY_PROMPT.md](documentation/templates/SKILLS_FACTORY_PROMPT.md)
- **Create Agents**: Use [AGENTS_FACTORY_PROMPT.md](documentation/templates/AGENTS_FACTORY_PROMPT.md)
- **Create Prompt Builders**: Use [PROMPTS_FACTORY_PROMPT.md](documentation/templates/PROMPTS_FACTORY_PROMPT.md)
- **Create Slash Commands**: Use [MASTER_SLASH_COMMANDS_PROMPT.md](documentation/templates/MASTER_SLASH_COMMANDS_PROMPT.md)
- **See Examples**: Check [claude-skills-examples/](claude-skills-examples/)
- **Generated Skills**: Explore [generated-skills/](generated-skills/)
- **Official Slash Command Examples**: See [documentation/references/](documentation/references/)
- **Read Guide**: See [CLAUDE.md](CLAUDE.md) for repository structure
- **Learn More (Skills)**: Read [claude-skills-instructions.md](claude-skills-instructions.md)
- **Learn More (Agents)**: Read [claude-agents-instructions.md](claude-agents-instructions.md)

- **Ready to build?** Open a prompt template, fill in your details, and start generating production-ready skills, agents, prompts, or slash commands for your Claude Code project!

## Star History

<a href="https://www.star-history.com/#alirezarezvani/claude-code-skills-factory&alirezarezvani/claude-code-tresor&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=alirezarezvani/claude-code-skills-factory,alirezarezvani/claude-code-tresor&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=alirezarezvani/claude-code-skills-factory,alirezarezvani/claude-code-tresor&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=alirezarezvani/claude-code-skills-factory,alirezarezvani/claude-code-tresor&type=date&legend=top-left" />
 </picture>
</a>
