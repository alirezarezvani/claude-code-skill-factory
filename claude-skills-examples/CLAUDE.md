# claude-skills-examples/CLAUDE.md

This file provides guidance for working with example skills and understanding skill architecture patterns.

---

## Purpose

This folder contains **reference skill implementations** that demonstrate how to create specialized capabilities for Claude Code. These examples show professional patterns and best practices for skill development.

**Key Point**: These are teaching examples - use them to understand skill architecture, then create your own or use the production-ready skills in `generated-skills/`.

---

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

---

## Example Skills Included

### 1. Analyzing Financial Statements

**Files**:
- `analyzing_financial_statements.md` - Skill definition
- `calculate_ratios.py` - Ratio calculation engine
- `interpret_ratios.py` - Ratio interpretation layer

**Purpose**: Calculate and interpret financial ratios (profitability, liquidity, leverage, efficiency, valuation)

**Key Class**: `FinancialRatioCalculator` - accepts financial statement data, calculates all major ratios

**Pattern**: Calculation engine + interpretation layer

**Architecture**:
```
Financial Data Input
     ↓
FinancialRatioCalculator
     ↓
Profitability, Liquidity, Leverage, Efficiency, Valuation Ratios
     ↓
RatioInterpreter
     ↓
Industry-specific Analysis & Recommendations
```

**Use Cases**:
- Analyze company financial health
- Compare companies in same industry
- Identify financial trends over time
- Generate investment analysis reports

---

### 2. Creating Financial Models

**Files**:
- `creating-financial-models.md` - Skill definition
- `dcf_model.py` - DCF valuation engine
- `sensitivity_analysis.py` - Sensitivity testing framework

**Purpose**: DCF valuation, Monte Carlo simulation, sensitivity analysis, scenario planning

**Key Class**: `DCFModel` - builds complete discounted cash flow models

**Pattern**: Historical data → projections → valuation with multiple analysis methods

**Architecture**:
```
Historical Financial Data
     ↓
DCFModel (projection engine)
     ↓
Free Cash Flow Projections
     ↓
Discount to Present Value
     ↓
SensitivityAnalyzer
     ↓
Valuation Range with Scenarios
```

**Use Cases**:
- Value companies for M&A
- Create investment theses
- Model different growth scenarios
- Assess valuation sensitivity to assumptions

---

### 3. Applying Brand Guidelines

**Files**:
- `brand_guidelines.md` - Skill definition with brand standards
- `apply_brand.py` - Brand application module

**Purpose**: Apply consistent corporate branding to documents (colors, fonts, layouts)

**Key Class**: `BrandFormatter` - applies Acme Corporation brand standards

**Pattern**: Brand definition (colors, fonts, layouts) + application logic

**Architecture**:
```
Brand Standards Definition
  (colors, fonts, spacing, layouts)
     ↓
BrandFormatter
     ↓
Document Input
     ↓
Apply Brand Standards
     ↓
Branded Document Output
```

**Use Cases**:
- Apply corporate branding to documents
- Ensure brand consistency
- Generate branded templates
- Customize branding for different document types

---

## Common Development Patterns

### 1. Data Structure

Skills use dictionaries for flexible data input:

```python
financial_data = {
    'income_statement': {
        'revenue': 1000000,
        'cogs': 400000,
        'operating_expenses': 300000,
        'net_income': 250000
    },
    'balance_sheet': {
        'current_assets': 500000,
        'total_assets': 2000000,
        'current_liabilities': 200000,
        'total_liabilities': 800000,
        'equity': 1200000
    },
    'cash_flow': {
        'operating_cash_flow': 300000,
        'investing_cash_flow': -150000,
        'financing_cash_flow': -50000
    },
    'market_data': {
        'share_price': 50.00,
        'shares_outstanding': 1000000
    }
}
```

**Why Dictionaries?**
- Flexible and extensible
- Easy to validate and transform
- Supports optional fields
- Clear key-value mapping

---

### 2. Safe Operations

All calculations use safe divide patterns to avoid division by zero:

```python
def safe_divide(self, numerator: float, denominator: float, default: float = 0.0) -> float:
    """
    Safely divide two numbers, returning a default value if denominator is zero.

    Args:
        numerator: The dividend
        denominator: The divisor
        default: Value to return if denominator is zero (default: 0.0)

    Returns:
        Result of division or default value
    """
    if denominator == 0:
        return default
    return numerator / denominator
```

**Example Usage**:
```python
# Calculate profit margin safely
profit_margin = self.safe_divide(net_income, revenue, default=0.0)

# Calculate ROE safely
roe = self.safe_divide(net_income, equity, default=0.0)
```

---

### 3. Type Annotations

Full typing for clarity and IDE support:

```python
from typing import Dict, List, Tuple, Optional

def calculate_profitability_ratios(self) -> Dict[str, float]:
    """
    Calculate all profitability ratios.

    Returns:
        Dictionary of ratio names to values
    """
    return {
        'gross_margin': self._calculate_gross_margin(),
        'operating_margin': self._calculate_operating_margin(),
        'net_margin': self._calculate_net_margin()
    }

def analyze_trends(self, data: List[Dict[str, float]]) -> Optional[str]:
    """
    Analyze financial trends over time.

    Args:
        data: List of financial data dictionaries by period

    Returns:
        Trend analysis summary or None if insufficient data
    """
    if len(data) < 2:
        return None

    # Analysis logic...
```

**Benefits**:
- IDE autocomplete and error checking
- Self-documenting code
- Easier to understand data flow
- Catches type errors early

---

### 4. Configuration Constants

Brand/style information stored as class constants:

```python
class BrandFormatter:
    """Applies Acme Corporation brand standards to documents."""

    COLORS = {
        'primary': {
            'acme_blue': {'hex': '#0066CC', 'rgb': (0, 102, 204)},
            'acme_dark_blue': {'hex': '#003366', 'rgb': (0, 51, 102)}
        },
        'secondary': {
            'acme_green': {'hex': '#00CC66', 'rgb': (0, 204, 102)},
            'acme_orange': {'hex': '#FF6600', 'rgb': (255, 102, 0)}
        },
        'neutral': {
            'acme_gray': {'hex': '#666666', 'rgb': (102, 102, 102)},
            'acme_light_gray': {'hex': '#CCCCCC', 'rgb': (204, 204, 204)}
        }
    }

    FONTS = {
        'headings': 'Helvetica Neue Bold',
        'body': 'Helvetica Neue Regular',
        'code': 'Courier New'
    }

    SPACING = {
        'section_margin': 24,
        'paragraph_spacing': 12,
        'line_height': 1.5
    }
```

**Benefits**:
- Centralized configuration
- Easy to customize for different brands
- Type-safe access
- Self-documenting standards

---

## How Skills Work

1. **Skill Discovery**: Claude scans available skills based on task description
2. **Minimal Loading**: Only loads necessary files when skill matches
3. **Execution**: Runs Python scripts using Claude's code execution environment
4. **Composability**: Multiple skills can work together
5. **Portability**: Same skill works across Claude apps, Claude Code, and API

**Loading Process**:
```
User Task Request
     ↓
Claude scans skill descriptions
     ↓
Matches task to relevant skills
     ↓
Loads SKILL.md frontmatter
     ↓
Executes Python scripts as needed
     ↓
Returns results to user
```

---

## Customization Guidelines

When helping users adapt these skills:

### 1. Modify the Frontmatter

Change `name` and `description` to match their use case:

```yaml
---
name: financial-analyzer
description: Calculate and interpret financial ratios for tech startups
---
```

Becomes:

```yaml
---
name: saas-financial-analyzer
description: Calculate SaaS metrics (MRR, CAC, LTV, Churn) and interpret for B2B companies
---
```

### 2. Update Brand Constants

Replace Acme Corporation with their company details:

```python
# Before
COLORS = {
    'primary': {'acme_blue': {'hex': '#0066CC', 'rgb': (0, 102, 204)}}
}

# After
COLORS = {
    'primary': {'company_red': {'hex': '#CC0000', 'rgb': (204, 0, 0)}}
}
```

### 3. Adjust Calculations

Modify ratio calculations or financial assumptions for their industry:

```python
# Generic calculation
def calculate_current_ratio(self) -> float:
    return self.safe_divide(self.current_assets, self.current_liabilities)

# Industry-specific (e.g., SaaS)
def calculate_magic_number(self) -> float:
    """Calculate SaaS Magic Number (ARR growth / S&M spend)."""
    arr_growth = self.current_arr - self.previous_arr
    return self.safe_divide(arr_growth, self.sales_marketing_spend)
```

### 4. Add New Capabilities

Extend classes with additional methods:

```python
class FinancialRatioCalculator:
    # Existing methods...

    def calculate_saas_metrics(self) -> Dict[str, float]:
        """Calculate SaaS-specific metrics."""
        return {
            'mrr': self._calculate_mrr(),
            'arr': self._calculate_arr(),
            'cac': self._calculate_cac(),
            'ltv': self._calculate_ltv(),
            'churn_rate': self._calculate_churn()
        }
```

### 5. Simplify

Remove unnecessary features they won't use:

```python
# If users only need basic ratios, remove advanced features
# Remove: Monte Carlo simulation, scenario analysis, sensitivity testing
# Keep: Basic ratio calculations and interpretation
```

---

## Key Principles

1. **Don't overengineer**: Skills should be as simple as possible while solving the problem
2. **Edit existing**: When making changes, prefer editing existing skill files over creating new ones
3. **Validate inputs**: Always check for missing/invalid data before calculations
4. **Document assumptions**: Financial models especially need clear assumption documentation
5. **Industry context**: Many calculations (ratios, valuations) require industry-specific interpretation

---

## Testing Skills Locally

### Quick Test Process

1. **Copy skill folder** to `.claude/skills/` or `~/.claude/skills/`
2. **Restart Claude Code** or reload skills
3. **Create test task** that matches skill description
4. **Verify execution**: Check that skill loads and produces correct output
5. **Iterate**: Refine based on testing results

### Example Test

```python
# Test financial ratio calculator
financial_data = {
    'income_statement': {'revenue': 1000000, 'net_income': 100000},
    'balance_sheet': {'total_assets': 500000, 'equity': 300000}
}

calculator = FinancialRatioCalculator(financial_data)
ratios = calculator.calculate_profitability_ratios()

assert ratios['net_margin'] == 0.10  # 10% net margin
assert ratios['roe'] == 0.33  # 33% ROE
```

---

## Related Resources

- **Main README**: [../README.md](../README.md) - Project overview
- **Root CLAUDE.md**: [../CLAUDE.md](../CLAUDE.md) - Orchestration layer
- **Documentation**: [../documentation/CLAUDE.md](../documentation/CLAUDE.md) - Templates and references
- **Generated Skills**: [../generated-skills/CLAUDE.md](../generated-skills/CLAUDE.md) - Production-ready catalog
- **Skills Factory Template**: [../documentation/templates/SKILLS_FACTORY_PROMPT.md](../documentation/templates/SKILLS_FACTORY_PROMPT.md)

---

## Next Steps

1. **Study these examples** to understand skill patterns
2. **Try customizing** an example for your use case
3. **Use the Skills Factory** template to generate new skills
4. **Refer to production skills** in `generated-skills/` for advanced examples
