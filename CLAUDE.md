# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 🚨 MANDATORY WORKFLOW REQUIREMENT

**CRITICAL**: All work on this project MUST follow this workflow. **NO EXCEPTIONS.**

### Required Process for Every User Request

1. **PLAN MODE FIRST**
   - Use plan mode to create a detailed implementation plan
   - Break down the work into clear, actionable steps
   - Estimate effort and identify potential challenges

2. **GET USER APPROVAL**
   - Present the plan to the user
   - Wait for explicit approval before proceeding
   - Address any questions or concerns

3. **CREATE GITHUB ISSUE**
   - Create a GitHub issue with the `plan` label
   - Include the approved plan in the issue body
   - Use markdown checkboxes for tasks: `- [ ] Task name`
   - The plan-to-issues automation will automatically create subtasks

4. **AUTOMATION CREATES SUBTASKS**
   - GitHub workflow creates individual issues for each task
   - All subtasks are linked to the parent issue
   - All added to project board for tracking

5. **START IMPLEMENTATION**
   - Begin work on subtasks in priority order
   - Update issue status as you progress
   - Reference issue numbers in commits

### Why This Matters

- ✅ **Proper tracking**: Every task is tracked in GitHub issues and project board
- ✅ **Clear planning**: Prevents scope creep and ensures thoughtful approach
- ✅ **Team visibility**: Everyone can see what's being worked on
- ✅ **Audit trail**: Complete history of decisions and implementation
- ✅ **Automation leverage**: Uses the excellent GitHub automation built into this repo

### Example Workflow

```
User: "Add a new skill for data visualization"

❌ WRONG: Start implementing immediately

✅ CORRECT:
1. Enter plan mode
2. Create plan with tasks:
   - Research data visualization libraries
   - Design SKILL.md structure
   - Implement Python visualization classes
   - Create sample data and examples
   - Write HOW_TO_USE.md
   - Test with real data
3. Present plan to user, get approval
4. Create GitHub issue with 'plan' label containing tasks
5. Wait for automation to create subtasks
6. Begin implementation
```

**NEVER START WORK WITHOUT FOLLOWING THIS PROCESS.**

---

## Repository Purpose

This repository is a **Claude Code Skills factory** - a collection of example skills that demonstrate how to create specialized capabilities for Claude Code. Skills are folders with instructions and resources that Claude loads when relevant to the user's task.

**Key Point**: This is NOT a development project itself. It's a reference repository that users can customize and extend for their own projects. Focus on helping users understand, adapt, and create their own skills based on these examples.

## Repository Structure

```
claude-code-skills-factory/
├── claude-skills-instructions.md    # Full documentation from Anthropic blog post
├── claude-skills-examples/          # Example skills with implementation
│   ├── analyzing_financial_statements.md  # Skill: Financial ratio analysis
│   ├── calculate_ratios.py                # Implementation for ratios
│   ├── interpret_ratios.py                # Ratio interpretation logic
│   ├── creating-financial-models.md       # Skill: DCF & financial modeling
│   ├── dcf_model.py                       # DCF valuation engine
│   ├── sensitivity_analysis.py            # Sensitivity testing framework
│   ├── brand_guidelines.md                # Skill: Corporate branding
│   └── apply_brand.py                     # Brand application module
├── documentation/
│   └── templates/
│       ├── SKILLS_FACTORY_PROMPT.md    # Template for generating Claude Skills
│       └── AGENTS_FACTORY_PROMPT.md    # Template for generating Claude Code agents
└── generated-skills/                   # Production-ready generated skills
    ├── aws-solution-architect/         # AWS architecture and IaC
    ├── content-trend-researcher/       # Content research and trend analysis
    ├── ms365-tenant-manager/           # Microsoft 365 administration
    ├── psychology-advisor/             # Mental wellness and CBT techniques
    ├── agent-factory/                  # Claude Code agent generation system
    └── prompt-suite/                   # World-class prompt generation (69 presets)
```

## Skill Architecture

Each skill follows a standard pattern:

### Skill Definition (.md file)
- **Frontmatter**: `name` and `description` in YAML format
- **Capabilities**: What the skill can do
- **Input Requirements**: What data/format is needed
- **Output Formats**: What the skill produces
- **Scripts**: Python files that implement functionality
- **Best Practices**: Guidelines for using the skill

### Implementation (.py files)
- **Class-based structure**: Main class encapsulates functionality
- **Type hints**: Full typing for clarity and IDE support
- **Safe operations**: Error handling (e.g., `safe_divide` to avoid division by zero)
- **Modular design**: Separate concerns (calculate vs interpret, model vs analyze)

## Example Skills Included

### 1. Analyzing Financial Statements
- **Files**: `analyzing_financial_statements.md`, `calculate_ratios.py`, `interpret_ratios.py`
- **Purpose**: Calculate and interpret financial ratios (profitability, liquidity, leverage, efficiency, valuation)
- **Key Class**: `FinancialRatioCalculator` - accepts financial statement data, calculates all major ratios
- **Pattern**: Calculation engine + interpretation layer

### 2. Creating Financial Models
- **Files**: `creating-financial-models.md`, `dcf_model.py`, `sensitivity_analysis.py`
- **Purpose**: DCF valuation, Monte Carlo simulation, sensitivity analysis, scenario planning
- **Key Class**: `DCFModel` - builds complete discounted cash flow models
- **Pattern**: Historical data → projections → valuation with multiple analysis methods

### 3. Applying Brand Guidelines
- **Files**: `brand_guidelines.md`, `apply_brand.py`
- **Purpose**: Apply consistent corporate branding to documents (colors, fonts, layouts)
- **Key Class**: `BrandFormatter` - applies Acme Corporation brand standards
- **Pattern**: Brand definition (colors, fonts, layouts) + application logic

## Generated Skills (Production-Ready)

The `generated-skills/` folder contains complete, production-ready skills created using the Skills Factory Prompt:

### 4. AWS Solution Architect
- **Files**: `SKILL.md`, `architecture_designer.py`, `cost_optimizer.py`, `serverless_stack.py`
- **Purpose**: Expert AWS architecture design for startups - serverless, scalable, cost-effective infrastructure
- **Key Classes**: `ArchitectureDesigner`, `CostOptimizer`, `ServerlessStackBuilder`
- **Pattern**: Architecture design → IaC templates → cost optimization

### 5. Content Trend Researcher
- **Files**: `SKILL.md`, `trend_analyzer.py`, `intent_analyzer.py`, `platform_insights.py`, `outline_generator.py`
- **Purpose**: Multi-platform trend analysis and data-driven content outline generation
- **Key Classes**: `TrendAnalyzer`, `IntentAnalyzer`, `PlatformInsights`, `OutlineGenerator`
- **Pattern**: Trend analysis → intent analysis → content gap discovery → outline generation

### 6. Microsoft 365 Tenant Manager
- **Files**: `SKILL.md`, `tenant_setup.py`, `user_management.py`, `powershell_generator.py`
- **Purpose**: Comprehensive M365 tenant administration and PowerShell automation
- **Key Classes**: `TenantManager`, `UserLifecycle`, `PowerShellScriptGenerator`
- **Pattern**: Configuration requirements → PowerShell scripts → validation checklists

### 7. Psychology Advisor
- **Files**: `SKILL.md`, `cbt_techniques.py`, `mindfulness_tools.py`, `stress_assessment.py`
- **Purpose**: Evidence-based psychological advisory with CBT techniques, mindfulness exercises, and stress management
- **Key Classes**: `CBTTechniques`, `MindfulnessTools`, `StressAssessment`
- **Pattern**: Cognitive distortion detection → thought reframing → coping strategies → practice plans

### 8. Content Trend Researcher
- **Files**: `SKILL.md`, `trend_analyzer.py`, `intent_analyzer.py`, `platform_insights.py`, `outline_generator.py`
- **Purpose**: Multi-platform trend analysis (Google, Reddit, YouTube, Medium, LinkedIn, X, etc.) and data-driven article outline generation
- **Key Classes**: `TrendAnalyzer`, `IntentAnalyzer`, `PlatformInsights`, `OutlineGenerator`
- **Pattern**: Platform trend analysis → user intent analysis → content gaps → SEO-optimized outlines

### 9. Agent Factory
- **Files**: `SKILL.md`, `agent_generator.py`
- **Purpose**: Generate custom Claude Code agents/sub-agents with enhanced YAML frontmatter, tool patterns, and MCP integration
- **Key Classes**: `AgentGenerator`
- **Pattern**: Agent requirements → YAML validation → agent .md file generation
- **Template**: Uses `documentation/templates/AGENTS_FACTORY_PROMPT.md` for generation

### 10. Prompt Suite
- **Files**: `SKILL.md`, `generate_prompt.py`, `validator.py`, `optimizer.py`, `batch_generator.py`
- **Purpose**: World-class prompt powerhouse generating production-ready mega-prompts for any role, industry, and task through intelligent question flow
- **Key Classes**: `PromptGenerator`, `PromptValidator`, `PromptOptimizer`, `BatchPromptGenerator`
- **Pattern**: 7-question flow → preset selection (69 presets, 15 domains) → quality validation → multi-format output (XML/Claude/ChatGPT/Gemini)
- **Coverage**: 69 comprehensive presets across Technical, Business, Legal, Finance, HR, Design, Customer, Executive, Manufacturing, R&D, Regulatory, Specialized-Technical, Research, Creative-Media domains

## Common Development Patterns

### 1. Data Structure
Skills use dictionaries for flexible data input:
```python
financial_data = {
    'income_statement': {...},
    'balance_sheet': {...},
    'cash_flow': {...},
    'market_data': {...}
}
```

### 2. Safe Operations
All calculations use safe divide patterns:
```python
def safe_divide(self, numerator: float, denominator: float, default: float = 0.0) -> float:
    if denominator == 0:
        return default
    return numerator / denominator
```

### 3. Type Annotations
Full typing for clarity:
```python
def calculate_profitability_ratios(self) -> Dict[str, float]:
```

### 4. Configuration Constants
Brand/style information stored as class constants:
```python
COLORS = {
    'primary': {'acme_blue': {'hex': '#0066CC', 'rgb': (0, 102, 204)}},
    ...
}
```

## How Skills Work

1. **Skill Discovery**: Claude scans available skills based on task description
2. **Minimal Loading**: Only loads necessary files when skill matches
3. **Execution**: Runs Python scripts using Claude's code execution environment
4. **Composability**: Multiple skills can work together
5. **Portability**: Same skill works across Claude apps, Claude Code, and API

## Customization Guidelines

When helping users adapt these skills:

1. **Modify the frontmatter**: Change `name` and `description` to match their use case
2. **Update brand constants**: Replace Acme Corporation with their company details
3. **Adjust calculations**: Modify ratio calculations or financial assumptions for their industry
4. **Add new capabilities**: Extend classes with additional methods
5. **Simplify**: Remove unnecessary features they won't use

## Key Principles

- **Don't overengineer**: Skills should be as simple as possible while solving the problem
- **Edit existing**: When making changes, prefer editing existing skill files over creating new ones
- **Validate inputs**: Always check for missing/invalid data before calculations
- **Document assumptions**: Financial models especially need clear assumption documentation
- **Industry context**: Many calculations (ratios, valuations) require industry-specific interpretation

## Templates for Generation

The `documentation/templates/` folder contains two powerful prompt templates:

### SKILLS_FACTORY_PROMPT.md
- **Purpose**: Generate complete Claude Skills (folders with SKILL.md + Python files)
- **Use for**: Creating capabilities like financial analysis, content research, data processing
- **Output**: Skill folders with SKILL.md, Python files, samples, and ZIP files
- **Location**: Skills go in `.claude/skills/` or `~/.claude/skills/`

### AGENTS_FACTORY_PROMPT.md
- **Purpose**: Generate Claude Code agents/sub-agents (single .md files)
- **Use for**: Creating specialized agents like code reviewers, developers, testers
- **Output**: Agent .md files with enhanced YAML frontmatter (color, field, expertise, MCP tools)
- **Location**: Agents go in `.claude/agents/` or `~/.claude/agents/`

**Key Difference:**
- **Skills** = Multi-file capabilities (folders)
- **Agents** = Single-file specialists (.md only)

## Installation

Users can install these skills and agents:

**Skills**:
- **Claude Code**: Copy skill folder to `~/.claude/skills/`
- **Claude Apps**: Use the "skill-creator" skill to import
- **API**: Use the `/v1/skills` endpoint

**Agents**:
- **Claude Code Project**: Copy .md file to `.claude/agents/`
- **Claude Code Personal**: Copy .md file to `~/.claude/agents/`
- **CLI**: Use `--agents` flag for session-specific agents

## References

- Full documentation: [claude-skills-instructions.md](claude-skills-instructions.md)
- Anthropic Skills docs: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- Skills marketplace: https://github.com/anthropics/skills
