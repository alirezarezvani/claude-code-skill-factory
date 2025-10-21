# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository is a **Claude Code Skills factory** - a collection of example skills that demonstrate how to create specialized capabilities for Claude Code. Skills are folders with instructions and resources that Claude loads when relevant to the user's task.

**Key Point**: This is NOT a development project itself. It's a reference repository that users can customize and extend for their own projects. Focus on helping users understand, adapt, and create their own skills based on these examples.

## Repository Structure

```
claude-code-skills-factory/
├── claude-skills-instructions.md    # Full documentation from Anthropic blog post
└── claude-skills-examples/          # Example skills with implementation
    ├── analyzing_financial_statements.md  # Skill: Financial ratio analysis
    ├── calculate_ratios.py                # Implementation for ratios
    ├── interpret_ratios.py                # Ratio interpretation logic
    ├── creating-financial-models.md       # Skill: DCF & financial modeling
    ├── dcf_model.py                       # DCF valuation engine
    ├── sensitivity_analysis.py            # Sensitivity testing framework
    ├── brand_guidelines.md                # Skill: Corporate branding
    └── apply_brand.py                     # Brand application module
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

## Installation

Users can install these skills:
- **Claude Code**: Copy skill folder to `~/.claude/skills/`
- **Claude Apps**: Use the "skill-creator" skill to import
- **API**: Use the `/v1/skills` endpoint

## References

- Full documentation: [claude-skills-instructions.md](claude-skills-instructions.md)
- Anthropic Skills docs: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- Skills marketplace: https://github.com/anthropics/skills
