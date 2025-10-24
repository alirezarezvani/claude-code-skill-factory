# Contributing to Claude Code Skills & Agents Factory

**Version**: 1.0.0
**Last Updated**: 2025-10-24

Welcome! This guide will help you contribute effectively to the Claude Code Skills & Agents Factory project.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Documentation Standards](#documentation-standards)
- [Getting Help](#getting-help)

---

## Quick Start

### For First-Time Contributors

1. **Fork the repository**
   ```bash
   gh repo fork rezarezvani/claude-code-skills-factory --clone
   cd claude-code-skills-factory
   ```

2. **Create an issue** (or pick an existing one)
   ```bash
   gh issue create --title "Add new skill: [skill name]"
   ```

3. **Create a branch**
   ```bash
   git checkout -b feat/123-add-skill-name
   ```

4. **Make your changes** following our [coding standards](#coding-standards)

5. **Commit using conventional commits**
   ```bash
   git commit -m "feat(skills): add [skill name] skill"
   ```

6. **Create pull request**
   ```bash
   gh pr create --fill
   ```

7. **Wait for automatic Claude Code review** (~2-3 minutes)

8. **Address feedback and merge!**

---

## Code of Conduct

### Our Pledge

This project is committed to providing a welcoming and inspiring environment for all contributors.

### Expected Behavior

- ✅ Be respectful and inclusive
- ✅ Welcome newcomers and help them get started
- ✅ Give constructive feedback
- ✅ Focus on what's best for the community
- ✅ Show empathy towards other contributors

### Unacceptable Behavior

- ❌ Harassment, discrimination, or exclusionary comments
- ❌ Trolling, insulting, or derogatory remarks
- ❌ Personal or political attacks
- ❌ Publishing others' private information
- ❌ Any conduct which could reasonably be considered inappropriate

### Enforcement

Violations may result in temporary or permanent ban from the project. Report issues to the project maintainers.

---

## How Can I Contribute?

### Reporting Bugs

**Before submitting**:
- Search existing issues to avoid duplicates
- Check if it's already fixed in latest version
- Gather necessary information

**Bug report should include**:
- **Clear title**: "Bug: [brief description]"
- **Steps to reproduce**: Numbered list of exact steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, Claude version
- **Screenshots**: If applicable

**Example**:
```markdown
Title: Bug: DCF model fails with negative cash flows

## Steps to Reproduce
1. Load DCF model skill
2. Provide financial data with negative FCF
3. Run valuation calculation

## Expected Behavior
Model should handle negative cash flows gracefully

## Actual Behavior
Division by zero error in WACC calculation

## Environment
- OS: macOS 14.1
- Python: 3.11.5
- Skill version: 1.0.0
```

---

### Suggesting Features

**Before submitting**:
- Check if feature already exists or is planned
- Consider if it fits project scope
- Think through implementation approach

**Feature request should include**:
- **Clear title**: "Feature: [brief description]"
- **Problem statement**: What problem does this solve?
- **Proposed solution**: How should it work?
- **Alternatives considered**: Other approaches you've thought about
- **Additional context**: Examples, mockups, references

**Example**:
```markdown
Title: Feature: Add Monte Carlo simulation to DCF model

## Problem Statement
Current DCF model provides single point estimate, but users need
probabilistic valuation ranges for risk assessment.

## Proposed Solution
Add Monte Carlo simulation capability that:
- Accepts probability distributions for key inputs
- Runs 10,000 simulations
- Returns percentile-based valuation ranges (P10, P50, P90)
- Visualizes distribution with histogram

## Alternatives Considered
- Sensitivity analysis (already exists, but less comprehensive)
- Scenario analysis (too limited, only 3 scenarios)

## Additional Context
Similar to functionality in Excel/Python financial libraries.
```

---

### Contributing New Skills

**Skill contribution checklist**:
- [ ] SKILL.md with proper YAML frontmatter (kebab-case name)
- [ ] Python implementation files (if needed)
- [ ] Type hints and docstrings
- [ ] Sample input/output JSON files
- [ ] HOW_TO_USE.md with examples
- [ ] Tests or validation scripts
- [ ] ZIP file for easy import

**See**: [claude-skills-examples/](claude-skills-examples/) for reference implementations

**Process**:
1. Create issue with `skill-request` label
2. Use [SKILLS_FACTORY_PROMPT.md](documentation/templates/SKILLS_FACTORY_PROMPT.md) to generate
3. Review generated files for quality
4. Create PR following [standards](#pull-request-process)

---

### Contributing New Agents

**Agent contribution checklist**:
- [ ] Single .md file with YAML frontmatter
- [ ] Enhanced fields: name, description, tools, model, color, field, expertise
- [ ] Clear system prompt with role definition
- [ ] Usage examples and invocation patterns
- [ ] Tool access patterns documented

**See**: [documentation/templates/AGENTS_FACTORY_PROMPT.md](documentation/templates/AGENTS_FACTORY_PROMPT.md)

**Process**:
1. Create issue with `agent-request` label
2. Use AGENTS_FACTORY_PROMPT.md to generate
3. Test agent locally in `.claude/agents/`
4. Create PR with agent file and documentation

---

### Improving Documentation

**Documentation contributions are highly valued!**

Areas needing improvement:
- Skill examples and tutorials
- Setup and installation guides
- Use case demonstrations
- Troubleshooting guides
- API reference documentation

**Documentation checklist**:
- [ ] Clear and concise language
- [ ] Code examples tested and working
- [ ] Screenshots/diagrams for complex topics
- [ ] Links to related documentation
- [ ] Table of contents for long docs
- [ ] Updated CLAUDE.md if structure changes

---

### Improving Templates

**Template improvements welcome for**:
- SKILLS_FACTORY_PROMPT.md
- AGENTS_FACTORY_PROMPT.md
- Issue templates
- PR templates

**Template contribution checklist**:
- [ ] Backward compatible with existing uses
- [ ] Tested with multiple scenarios
- [ ] Documentation updated
- [ ] Examples provided

---

## Development Workflow

### Complete Workflow Diagram

```
┌──────────────────────────────────────────────────────────┐
│ 1. Create or Choose Issue                                │
│    - New issue: gh issue create                          │
│    - Existing: gh issue list --label "good-first-issue" │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ 2. Fork & Clone (first time only)                        │
│    gh repo fork USER/REPO --clone                        │
│    cd claude-code-skills-factory                         │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ 3. Create Branch                                          │
│    git checkout main                                      │
│    git pull upstream main                                 │
│    git checkout -b feat/123-description                  │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ 4. Make Changes                                           │
│    - Follow coding standards                              │
│    - Write tests if applicable                            │
│    - Update documentation                                 │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ 5. Commit (Conventional Commits)                          │
│    git add .                                              │
│    git commit -m "feat(skills): add new skill            │
│                                                           │
│    Detailed description.                                  │
│                                                           │
│    Closes #123"                                          │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ 6. Push to Your Fork                                      │
│    git push -u origin feat/123-description               │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ 7. Create Pull Request                                    │
│    gh pr create --repo USER/REPO --fill                  │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ 8. Automatic Claude Code Review                          │
│    - Triggers within 30 seconds                           │
│    - Reviews code quality, security, best practices       │
│    - Posts feedback as PR comment                         │
│    - Updates status check (pass/fail)                     │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ 9. Address Feedback                                       │
│    - Read review comments                                 │
│    - Make requested changes                               │
│    - Push updates (triggers re-review)                    │
└────────────────┬─────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────┐
│ 10. Merge!                                                │
│     - Maintainer merges PR                                │
│     - Issue auto-closes                                   │
│     - Your contribution is live!                          │
└──────────────────────────────────────────────────────────┘
```

---

## Coding Standards

### Python Code Standards

**Required**:
- ✅ Python 3.8+ compatible
- ✅ Type hints for all functions and classes
- ✅ Docstrings (Google style)
- ✅ PEP 8 compliant formatting
- ✅ No unused imports or variables

**Example**:
```python
from typing import Dict, List, Optional

class FinancialCalculator:
    """Performs financial calculations and analysis.

    This class provides methods for computing financial ratios,
    valuations, and other metrics.

    Attributes:
        data: Dictionary containing financial statement data
        currency: Currency code (default: USD)
    """

    def __init__(self, data: Dict[str, float], currency: str = "USD") -> None:
        """Initialize calculator with financial data.

        Args:
            data: Financial statement data dictionary
            currency: ISO currency code

        Raises:
            ValueError: If required data is missing
        """
        self.data = data
        self.currency = currency
        self._validate_data()

    def calculate_ratio(
        self,
        numerator: float,
        denominator: float,
        default: float = 0.0
    ) -> float:
        """Calculate financial ratio with safe division.

        Args:
            numerator: Top value in ratio
            denominator: Bottom value in ratio
            default: Value to return if denominator is zero

        Returns:
            Calculated ratio or default value
        """
        if denominator == 0:
            return default
        return numerator / denominator
```

**Formatting**:
```bash
# Use black for formatting
pip install black
black generated-skills/your-skill/

# Check with flake8
pip install flake8
flake8 generated-skills/your-skill/
```

---

### YAML Frontmatter Standards

**For Skills (SKILL.md)**:
```yaml
---
name: skill-name-in-kebab-case
description: Brief one-line description of what this skill does
---
```

**Rules**:
- ✅ `name` in kebab-case (lowercase, hyphens)
- ✅ `description` is one sentence, no period
- ❌ NO Title Case, snake_case, or camelCase
- ❌ NO multi-line descriptions in frontmatter

**For Agents (.md files)**:
```yaml
---
name: agent-name-in-kebab-case
description: Brief description when to use this agent
tools: Read, Write, Edit, Bash
model: sonnet
color: blue
field: backend
expertise: expert
mcp_tools: mcp__github, mcp__context7
---
```

---

### Documentation Standards

**Markdown formatting**:
- Use ATX-style headers (`#` not underlines)
- Code blocks with language specifiers
- Tables for structured data
- Relative links to other docs
- No trailing whitespace

**File naming**:
- All lowercase: `installation-guide.md`
- Hyphens for spaces: `api-reference.md`
- Descriptive names: `contributing-guide.md`

**Exceptions** (UPPERCASE only):
- README.md
- CLAUDE.md
- AGENTS.md
- CONTRIBUTING.md
- CHANGELOG.md

**Structure**:
```markdown
# Document Title

**Version**: 1.0.0
**Last Updated**: 2025-10-24

Brief introduction paragraph.

---

## Table of Contents

- [Section 1](#section-1)
- [Section 2](#section-2)

---

## Section 1

Content...

---

## Section 2

Content...
```

---

### Git Commit Standards

**Format**:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `refactor` - Code restructuring
- `test` - Adding tests
- `chore` - Maintenance tasks

**Examples**:
```bash
# Feature
git commit -m "feat(skills): add AWS Lambda optimization skill

Implements comprehensive Lambda performance and cost optimization.

Closes #156"

# Bug fix
git commit -m "fix(workflows): resolve project sync timeout

Increased timeout from 5 to 10 minutes for large projects.

Fixes #189"

# Documentation
git commit -m "docs(contributing): add git workflow examples

Closes #234"
```

**See**: [.github/BRANCHING_STRATEGY.md](.github/BRANCHING_STRATEGY.md#commit-message-standards) for complete standards

---

## Pull Request Process

### Before Creating PR

**Checklist**:
- [ ] Code follows Python/YAML standards
- [ ] All tests pass (if applicable)
- [ ] Documentation updated
- [ ] Commit messages follow conventions
- [ ] Branch is up-to-date with main
- [ ] No merge conflicts

```bash
# Update branch
git checkout main
git pull upstream main
git checkout feat/123-your-branch
git rebase main
git push --force-with-lease
```

---

### Creating the PR

**Use PR template**:

```markdown
## Summary

[2-3 sentence summary of what this PR does]

## Changes

- [ ] Added new skill: AWS Lambda Optimizer
- [ ] Included Python modules: cost_analyzer.py, performance_profiler.py
- [ ] Created sample data and HOW_TO_USE guide
- [ ] Generated ZIP package for import

## Issue Reference

Closes #156

## Type of Change

- [x] New feature (adds functionality)
- [ ] Bug fix
- [ ] Documentation update
- [ ] Refactoring

## Testing

- [x] Manually tested skill generation
- [x] Validated YAML frontmatter
- [x] Tested Python modules execute correctly
- [x] Verified ZIP import works

## Checklist

- [x] Code follows project style guidelines
- [x] Documentation updated
- [x] Commit messages follow conventions
- [x] No breaking changes
```

---

### During Review

**Automatic Claude Code Review**:
- Triggers within 30 seconds of PR creation/update
- Reviews code quality, security, best practices
- Posts feedback as comment (~2-3 minutes)
- Updates `claude-review` status check

**Responding to feedback**:
```bash
# Make requested changes
git add .
git commit -m "fix: address Claude review feedback"
git push

# Claude automatically re-reviews
```

**If review fails**:
- Read feedback carefully
- Ask questions if unclear (comment on PR)
- Make changes and push updates
- Don't force-merge failing reviews

---

### Merge Requirements

**PR cannot merge until**:
- ✅ `claude-review` status check passes
- ✅ Branch is up-to-date with main
- ✅ All conversations resolved
- ✅ Maintainer approval (for external contributors)

**Merge will happen when**:
- All requirements met
- Maintainer merges (usually within 24-48 hours)
- Issue auto-closes if referenced in PR

---

## Issue Guidelines

### Creating Good Issues

**Title format**:
```
<Type>: <Brief description>

Examples:
Bug: DCF model fails with negative cash flows
Feature: Add Monte Carlo simulation to DCF
Documentation: Improve installation guide
Question: How to create custom skill?
```

**Use labels**:
- `bug` - Something broken
- `feature` - New capability request
- `documentation` - Doc improvements
- `question` - Need help
- `good-first-issue` - Great for newcomers
- `help-wanted` - Community assistance needed

**Issue template**:

For bugs:
```markdown
## Description
[Clear description of the bug]

## Steps to Reproduce
1. Step one
2. Step two
3. Step three

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- OS: macOS 14.1
- Python: 3.11.5
- Version: 1.0.0

## Screenshots
[If applicable]
```

For features:
```markdown
## Problem Statement
[What problem does this solve?]

## Proposed Solution
[How should it work?]

## Alternatives Considered
[Other approaches]

## Additional Context
[Examples, references, mockups]
```

---

### Issue Triage

**Automatic triage**:
- New issues auto-triaged within 30 seconds
- Claude analyzes and applies labels
- Priority assigned (P0-P3)
- Added to project board
- Triage summary posted

**Manual triage** (for maintainers):
```bash
# Add labels
gh issue edit 123 --add-label "bug,P1"

# Assign to project
gh project item-add 7 --owner USER --url ISSUE_URL

# Add to milestone
gh issue edit 123 --milestone "v1.1.0"
```

---

## Documentation Standards

### When to Update Documentation

**Always update when**:
- Adding new skills or agents
- Changing templates
- Modifying workflows
- Adding/removing features
- Changing file structure

**Key files to update**:
- **README.md** - Main project overview
- **CLAUDE.md** - Repository guidance for Claude Code
- **AGENTS.md** - Agent catalog (if adding agents)
- **Skill/Agent documentation** - HOW_TO_USE, examples

---

### Documentation Structure

```
claude-code-skills-factory/
├── README.md                    # Main entry point
├── CLAUDE.md                    # Claude Code guidance
├── CONTRIBUTING.md              # This file
├── claude-skills-examples/      # Example skills
│   └── [skill-name]/
│       ├── SKILL.md
│       ├── *.py
│       └── HOW_TO_USE.md
├── generated-skills/            # Production skills
│   └── [skill-name]/
│       ├── SKILL.md
│       ├── scripts/*.py
│       ├── samples/
│       ├── HOW_TO_USE.md
│       └── [skill-name].zip
├── documentation/
│   └── templates/
│       ├── SKILLS_FACTORY_PROMPT.md
│       └── AGENTS_FACTORY_PROMPT.md
└── .github/
    ├── BRANCHING_STRATEGY.md
    ├── WORKFLOWS.md
    └── INSTRUCTION.md
```

---

## Getting Help

### Where to Ask Questions

**For general questions**:
```bash
gh issue create \
  --title "Question: [your question]" \
  --label "question"
```

**For contribution help**:
- Read [BRANCHING_STRATEGY.md](.github/BRANCHING_STRATEGY.md)
- Check existing issues and PRs
- Ask in your PR or issue comments

**For Claude Code help**:
- Official docs: https://docs.claude.com/claude-code
- Skills documentation: [claude-skills-instructions.md](claude-skills-instructions.md)
- Agents documentation: [claude-agents-instructions.md](claude-agents-instructions.md)

**In PR/issue comments**:
```
@claude [your question or request]
```
(Only works for team members)

---

## Recognition

### Contributors

All contributors will be:
- Listed in repository contributors
- Mentioned in release notes
- Credited in documentation (if significant contribution)

### First-Time Contributors

Look for issues labeled `good-first-issue`:
```bash
gh issue list --label "good-first-issue"
```

These are beginner-friendly and well-documented!

---

## Legal

### License

By contributing, you agree that your contributions will be licensed under the same license as the project.

### Contributor Agreement

- You have the right to submit the work
- You grant the project a perpetual license to use your contribution
- Your contribution is your original creation

---

## Quick Reference

### First-Time Setup
```bash
gh repo fork USER/REPO --clone
cd claude-code-skills-factory
git remote add upstream https://github.com/USER/REPO.git
```

### Start Work
```bash
git checkout main
git pull upstream main
git checkout -b feat/123-description
```

### Commit & Push
```bash
git add .
git commit -m "feat(scope): description

Closes #123"
git push -u origin feat/123-description
```

### Create PR
```bash
gh pr create --repo USER/REPO --fill
```

### Update Branch
```bash
git checkout main
git pull upstream main
git checkout feat/123-description
git rebase main
git push --force-with-lease
```

---

## Additional Resources

- **Branching Strategy**: [.github/BRANCHING_STRATEGY.md](.github/BRANCHING_STRATEGY.md)
- **Workflow Automation**: [.github/WORKFLOWS.md](.github/WORKFLOWS.md)
- **Setup Instructions**: [.github/INSTRUCTION.md](.github/INSTRUCTION.md)
- **Skills Documentation**: [claude-skills-instructions.md](claude-skills-instructions.md)
- **Agents Documentation**: [claude-agents-instructions.md](claude-agents-instructions.md)

---

**Thank you for contributing to Claude Code Skills & Agents Factory!**

Your contributions help developers worldwide create better Claude Code experiences.

**Version**: 1.0.0
**Last Updated**: 2025-10-24
**Status**: ✅ Ready for Contributors

Questions? Create an issue with the `question` label!
