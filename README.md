# Claude Code Skills Factory

A comprehensive toolkit for generating production-ready Claude Skills at scale. This repository provides templates, examples, and a powerful prompt engineering system to create custom skills for Claude AI across all platforms (Claude apps, Claude Code, and API).

## What Are Claude Skills?

Claude Skills are specialized capabilities that teach Claude how to perform specific tasks. They're packaged as folders containing:

- **SKILL.md**: Structured instructions with YAML frontmatter
- **Python files** (optional): Functional code for calculations, data processing, or file generation
- **Sample data**: JSON examples showing inputs and expected outputs
- **Usage guide**: Clear invocation examples

Skills are **composable** (work together), **portable** (same format everywhere), and **efficient** (loaded only when relevant).

## Repository Contents

```
claude-code-skills-factory/
├── README.md                              # This file
├── CLAUDE.md                              # Repository guidance for Claude Code
├── claude-skills-instructions.md          # Full Anthropic documentation
├── claude-skills-examples/                # Reference implementations
│   ├── analyzing_financial_statements.md
│   ├── calculate_ratios.py
│   ├── interpret_ratios.py
│   ├── creating-financial-models.md
│   ├── dcf_model.py
│   ├── sensitivity_analysis.py
│   ├── brand_guidelines.md
│   └── apply_brand.py
├── generated-skills/                      # Production-ready generated skills
│   ├── aws-solution-architect/            # AWS architecture and infrastructure
│   ├── content-trend-researcher/          # Content research and trend analysis
│   └── ms365-tenant-manager/              # Microsoft 365 administration
└── documentation/
    └── templates/
        └── SKILLS_FACTORY_PROMPT.md       # The main prompt template
```

## Quick Start

### 1. Use the Skills Factory Prompt

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

### Microsoft 365 Tenant Manager
Generated for IT administrators - manages M365 tenant setup, security, and generates PowerShell automation scripts.

**See**: [generated-skills/ms365-tenant-manager/](generated-skills/ms365-tenant-manager/)

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

**Current Version**: 1.0.0
**Last Updated**: October 21, 2025
**Compatible With**: Claude Skills (all platforms)

---

## Quick Reference

**Create Skills**: Use [SKILLS_FACTORY_PROMPT.md](documentation/templates/SKILLS_FACTORY_PROMPT.md)
**See Examples**: Check [claude-skills-examples/](claude-skills-examples/)
**Read Guide**: See [CLAUDE.md](CLAUDE.md) for repository structure
**Learn More**: Read [claude-skills-instructions.md](claude-skills-instructions.md)

**Ready to build?** Open the prompt template, fill in your details, and start generating production-ready skills!
