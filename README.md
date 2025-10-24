# Claude Code Skills & Agents Factory

A comprehensive toolkit for generating production-ready Claude Skills and Claude Code Agents at scale. This repository provides templates, examples, and powerful prompt engineering systems to create custom skills and specialized agents for Claude AI across all platforms (Claude apps, Claude Code, and API).

## Table of Contents

- [What Are Claude Skills?](#what-are-claude-skills)
- [What Are Claude Code Agents?](#what-are-claude-code-agents)
- [Repository Contents](#repository-contents)
- [Quick Start](#quick-start)
  - [Option A: Generate Claude Skills](#option-a-generate-claude-skills-multi-file-capabilities)
  - [Option B: Generate Claude Code Agents](#option-b-generate-claude-code-agents-single-file-specialists)
- [Example Skills Included](#example-skills-included)
  - [1. Analyzing Financial Statements](#1-analyzing-financial-statements)
  - [2. Creating Financial Models](#2-creating-financial-models)
  - [3. Applying Brand Guidelines](#3-applying-brand-guidelines)
- [Generated Skills](#generated-skills)
  - [4. AWS Solution Architect](#4-aws-solution-architect)
  - [5. Content Trend Researcher](#5-content-trend-researcher)
  - [6. Microsoft 365 Tenant Manager](#6-microsoft-365-tenant-manager)
  - [7. Prompt Suite](#7-prompt-suite)
- [Key Features](#key-features)
- [Skill Architecture Patterns](#skill-architecture-patterns)
- [Best Practices](#best-practices)
- [Customization Guide](#customization-guide)
- [YAML Frontmatter Rules](#yaml-frontmatter-rules)
- [Technical Details](#technical-details)
- [Resources](#resources)
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
├── claude-skills-instructions.md          # Full Skills documentation from Anthropic
├── claude-agents-instructions.md          # Full Agents documentation from Anthropic
├── claude-skills-examples/                # Reference skill implementations
│   ├── analyzing_financial_statements.md
│   ├── calculate_ratios.py
│   ├── interpret_ratios.py
│   ├── creating-financial-models.md
│   ├── dcf_model.py
│   ├── sensitivity_analysis.py
│   ├── brand_guidelines.md
│   └── apply_brand.py
├── generated-skills/                      # Production-ready generated skills
│   ├── aws-solution-architect/            # AWS architecture (53 KB)
│   ├── content-trend-researcher/          # Multi-platform content research (35 KB)
│   ├── ms365-tenant-manager/              # Microsoft 365 administration (40 KB)
│   ├── psychology-advisor/                # Mental wellness & CBT techniques (31 KB)
│   ├── agent-factory/                     # Claude Code agent generation (12 KB)
│   └── prompt-suite/                      # Prompt generation powerhouse (427 KB)
└── documentation/
    └── templates/
        ├── SKILLS_FACTORY_PROMPT.md       # Template for generating Skills
        └── AGENTS_FACTORY_PROMPT.md       # Template for generating Agents
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

### 7. Prompt Suite
**Purpose**: World-class prompt powerhouse for generating production-ready mega-prompts for any role, industry, and task

**Files**:
- [SKILL.md](generated-skills/prompt-suite/SKILL.md)
- [generate_prompt.py](generated-skills/prompt-suite/scripts/generate_prompt.py)
- [validator.py](generated-skills/prompt-suite/scripts/validator.py)
- [optimizer.py](generated-skills/prompt-suite/scripts/optimizer.py)
- [batch_generator.py](generated-skills/prompt-suite/scripts/batch_generator.py)

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

### Prompt Suite (427 KB)
World-class prompt powerhouse that generates production-ready mega-prompts for any role, industry, and task through intelligent 7-question flow.

**Key Features**: 69 comprehensive presets across 15 professional domains (Technical, Business, Legal, Finance, HR, Design, Customer, Executive, Manufacturing, R&D, Regulatory, Specialized-Technical, Research, Creative-Media), multiple output formats (XML/Claude/ChatGPT/Gemini), 7-point quality validation gates, contextual best practices from OpenAI/Anthropic/Google

**Domains Covered**: Full-Stack Engineer, DevOps, Product Manager, Legal Counsel, CFO, HR Manager, UI/UX Designer, Customer Success, CEO, ML Engineer, Research Scientist, Copywriter, Manufacturing Engineer, Clinical Specialist, and 55+ more roles

**See**: [generated-skills/prompt-suite/](generated-skills/prompt-suite/)

Each includes full implementation, sample data, HOW_TO_USE guide, and ready-to-import ZIP files.

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

**Current Version**: 1.2.0
**Last Updated**: October 23, 2025
**Compatible With**: Claude Skills (all platforms) and Claude Code Agents

**Latest Changes** (v1.2.0):
- Added Prompt Suite skill (427 KB) - World-class prompt generation with 69 presets across 15 domains
- Expanded coverage: Technical, Business, Legal, Finance, HR, Design, Customer, Executive, Manufacturing, R&D, Regulatory, Specialized-Technical, Research, Creative-Media domains
- Multi-format output support (XML/Claude/ChatGPT/Gemini)

---

## Quick Reference

**Create Skills**: Use [SKILLS_FACTORY_PROMPT.md](documentation/templates/SKILLS_FACTORY_PROMPT.md)
**Create Agents**: Use [AGENTS_FACTORY_PROMPT.md](documentation/templates/AGENTS_FACTORY_PROMPT.md)
**See Examples**: Check [claude-skills-examples/](claude-skills-examples/)
**Generated Skills**: Explore [generated-skills/](generated-skills/)
**Read Guide**: See [CLAUDE.md](CLAUDE.md) for repository structure
**Learn More (Skills)**: Read [claude-skills-instructions.md](claude-skills-instructions.md)
**Learn More (Agents)**: Read [claude-agents-instructions.md](claude-agents-instructions.md)

**Ready to build?** Open a prompt template, fill in your details, and start generating production-ready skills or agents!
