# Claude Skills Reference

**Complete guide to creating and using specialized capabilities (Skills) in Claude**

---

## Table of Contents

- [Introduction](#introduction)
- [What Are Claude Skills](#what-are-claude-skills)
- [How Skills Work](#how-skills-work)
- [Skills Across Claude Products](#skills-across-claude-products)
- [Creating Skills](#creating-skills)
- [Skill Structure](#skill-structure)
- [Best Practices](#best-practices)
- [Skills vs Agents](#skills-vs-agents)
- [Getting Started](#getting-started)
- [Related Resources](#related-resources)

---

## Introduction

Claude Skills are specialized capabilities that teach Claude how to perform specific tasks. They're packaged as folders containing instructions, scripts, and resources that Claude loads when relevant to the task at hand.

**Key Concept**: Skills make Claude better at specialized tasks like working with Excel, following brand guidelines, or executing custom workflows—without requiring manual skill selection.

---

## What Are Claude Skills

### Definition

Skills are folders that include:
- **SKILL.md** - Structured instructions with YAML frontmatter
- **Python scripts** (optional) - Executable code for reliable task execution
- **Resources** - Sample data, templates, or reference files
- **Documentation** - Usage examples and guidelines

### Core Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Composable** | Skills stack together - Claude coordinates multiple skills automatically |
| **Portable** | Same format across Claude apps, Claude Code, and API |
| **Efficient** | Only loads minimal needed information when relevant |
| **Powerful** | Can include executable code for tasks requiring traditional programming |

### When Skills Load

Claude scans available skills while working on tasks and loads only relevant ones with minimal information needed, keeping Claude fast while accessing specialized expertise.

**Think of Skills as**: Custom onboarding materials that package expertise, making Claude a specialist in what matters most to you.

---

## How Skills Work

### Automatic Skill Detection

**Process**:
1. User provides a task
2. Claude scans available skills for relevant matches
3. When a match is found, Claude loads only minimal needed files
4. Skill is applied to the task
5. Result is returned with skill usage visible in chain of thought

### Skill Composition

**Multiple Skills**: Claude automatically identifies which skills are needed and coordinates their use together.

**Example Workflow**:
```
User Task: "Create a branded Excel report from this data"
         ↓
Claude identifies:
  - excel-handler skill (data processing)
  - brand-guidelines skill (styling)
         ↓
Both skills work together
         ↓
Branded Excel report generated
```

### Code Execution

**Why Code Matters**: For tasks where traditional programming is more reliable than token generation, skills can include executable Python code.

**Security Note**: Skills have access to execute code. Use only trusted sources to keep your data safe.

---

## Skills Across Claude Products

### 1. Claude Apps (Claude.ai)

**Availability**: Pro, Max, Team, and Enterprise users

**Features**:
- Anthropic-provided skills for common tasks (Excel, PowerPoint, Word, PDF)
- Example skills you can customize
- Ability to create custom skills
- Automatic skill invocation based on task relevance
- Skills visible in Claude's chain of thought

**Creating Skills**:
- Use the built-in "skill-creator" skill
- Interactive guidance through workflow
- Automatic folder structure generation
- SKILL.md formatting handled automatically
- No manual file editing required

**Enabling**:
1. Go to Settings → Features
2. Enable Skills
3. Team/Enterprise: Admin must enable org-wide first

**Video Guide**: [Creating custom Skills with Claude](https://www.youtube.com/watch?v=kS1MJFZWMq4)

### 2. Claude Developer Platform (API)

**Availability**: All API users

**Access Methods**:
- Add skills to Messages API requests
- Use `/v1/skills` endpoint for management
- Create, view, and upgrade skill versions via Console

**Requirements**:
- [Code Execution Tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool) beta
- Provides secure environment for skill execution

**Built-in Skills**:
- Excel spreadsheets with formulas
- PowerPoint presentations
- Word documents
- Fillable PDFs

**Custom Skills**: Developers can create custom skills for specific use cases

**Documentation**: [API Skills Guide](https://docs.claude.com/en/api/skills-guide)

### 3. Claude Code

**Availability**: All Claude Code users

**Installation Methods**:

**Option A: Marketplace (Recommended)**
```bash
# Install from anthropics/skills repository
# Skills install automatically via plugins
```

**Option B: Manual Installation**
```bash
# Copy skill folder to user skills directory
cp -r my-skill ~/.claude/skills/

# Or install project-level
cp -r my-skill .claude/skills/
```

**Features**:
- Claude loads skills automatically when relevant
- Share skills through version control
- Team collaboration via project-level skills
- Same skills work across team members

**Claude Agent SDK**: Provides same Agent Skills support for building custom agents

**Documentation**: [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)

---

## Creating Skills

### Method 1: Interactive Creation (Claude Apps)

**Using skill-creator**:

1. **Invoke skill-creator**:
   ```
   "I need to create a skill for [your use case]"
   ```

2. **Answer guided questions**:
   - What workflows does your skill support?
   - What resources are needed?
   - What should the skill produce?

3. **Claude generates**:
   - Complete folder structure
   - Formatted SKILL.md file
   - Required Python scripts (if needed)
   - Sample data
   - Documentation

4. **Review and refine**:
   - Test the generated skill
   - Adjust instructions as needed
   - Add additional resources

**Video**: [Claude Skills: Specialized capabilities you can customize](https://www.youtube.com/watch?v=IoqpBKrNaZI)

### Method 2: Manual Creation

**Create Skill Folder**:
```bash
mkdir -p my-skill
cd my-skill
```

**Create SKILL.md**:
```markdown
---
name: my-skill-name
description: Brief description of what this skill does
---

# Skill Name

## Purpose
[What problem this skill solves]

## Capabilities
- [Capability 1]
- [Capability 2]

## Usage
[How to invoke this skill]

## Files Included
- script.py - [Description]
- templates/ - [Description]
```

**Add Implementation** (optional):
```python
# script.py
def main():
    """Execute skill functionality"""
    # Your code here
    pass

if __name__ == "__main__":
    main()
```

**Add Resources**:
```bash
# Add templates, sample data, etc.
mkdir templates
echo "sample" > templates/example.txt
```

### Method 3: Customize Existing Skills

**GitHub Repository**: [anthropics/skills](https://github.com/anthropics/skills)

**Steps**:
1. Browse example skills
2. Clone or download skill folder
3. Customize SKILL.md instructions
4. Modify Python scripts if needed
5. Update resources for your use case
6. Install to your Claude environment

---

## Skill Structure

### Required: SKILL.md

**Format**:
```markdown
---
name: skill-name-in-kebab-case
description: One-line description of skill purpose and usage
---

# Skill Title

[Detailed instructions for Claude on how to use this skill]

## Capabilities
[What the skill can do]

## Input Requirements
[What data or format is needed]

## Output
[What the skill produces]

## Examples
[Usage examples]
```

**YAML Frontmatter Rules**:
- `name`: kebab-case (lowercase with hyphens)
- `description`: Clear, concise, action-oriented

### Optional: Python Scripts

**When to Include Code**:
- Complex calculations
- File format conversions
- Data transformations
- API integrations
- Tasks requiring guaranteed reliability

**Example Structure**:
```python
#!/usr/bin/env python3
"""
Skill: My Skill Name
Purpose: [Brief description]
"""

def main():
    """Main entry point for skill execution"""
    # Implementation
    pass

if __name__ == "__main__":
    main()
```

### Optional: Resources

**Common Resources**:
- `templates/` - Template files
- `examples/` - Sample input/output
- `data/` - Reference data
- `config/` - Configuration files
- `README.md` - Additional documentation

---

## Best Practices

### 1. Clear Instructions

**Good**:
```markdown
## Usage
When the user requests a financial report:
1. Extract data from provided sources
2. Calculate key metrics (ROI, ROE, margins)
3. Format using company template
4. Include executive summary
```

**Avoid**:
```markdown
## Usage
Create financial reports
```

### 2. Focused Skills

**Recommended**: One clear purpose per skill
```
✅ excel-formatter - Formats Excel with specific styles
✅ data-validator - Validates data against schemas
```

**Avoid**: Multiple unrelated capabilities
```
❌ office-helper - Does Excel, PowerPoint, Word, and email
```

### 3. Include Examples

**Best Practice**:
```markdown
## Examples

### Example 1: Basic Usage
Input: Raw sales data CSV
Output: Formatted Excel with charts

### Example 2: With Filtering
Input: Sales data + date range
Output: Filtered report for period
```

### 4. Executable vs Prompt-Only

**Use Python Scripts When**:
- Exact calculations required
- Complex file format handling
- Performance-critical operations
- Guaranteed deterministic output

**Use Prompt-Only When**:
- Flexible creative output
- Natural language processing
- Contextual decision-making
- Template-based generation

### 5. Version Control

**For Teams**:
```bash
# Project-level skills (shared)
.claude/skills/
├── team-style-guide/
└── data-processor/

# Add to version control
git add .claude/skills/
git commit -m "Add team skills"
```

**For Personal Use**:
```bash
# User-level skills (not shared)
~/.claude/skills/
├── my-workflow/
└── personal-templates/
```

---

## Skills vs Agents

### Comparison

| Aspect | Skills | Agents (Subagents) |
|--------|--------|---------------------|
| **Format** | Multi-file folders | Single .md file |
| **Purpose** | Specialized capabilities | Task delegation |
| **Code** | Can include Python scripts | Prompt-based only |
| **Context** | Shared with main thread | Separate context window |
| **Use Case** | Domain expertise | Workflow automation |
| **Location** | `~/.claude/skills/` | `~/.claude/agents/` |

### When to Use Each

**Use Skills For**:
- Domain-specific expertise (Excel, finance, design)
- Code execution requirements
- Resource bundles (templates, data, scripts)
- Cross-platform portability (API + Claude Code + Apps)

**Use Agents For**:
- Task delegation and workflow control
- Preserving main context
- Simple prompt-based specialization
- Quick iteration without files

**Use Both Together**:
```
Agent: code-reviewer
  ↓ Uses
Skill: code-quality-standards
  ↓ Contains
- style-guide.md
- linting-rules.py
- best-practices.md
```

---

## Getting Started

### Quick Start Checklist

- [ ] **Choose your platform**: Claude apps, API, or Claude Code
- [ ] **Enable skills**: Check settings or configuration
- [ ] **Try built-in skills**: Test Excel, PowerPoint skills
- [ ] **Browse examples**: Visit [github.com/anthropics/skills](https://github.com/anthropics/skills)
- [ ] **Create custom skill**: Use skill-creator or manual method
- [ ] **Test thoroughly**: Verify skill works as expected
- [ ] **Share with team**: Add to version control (if applicable)

### Learning Path

**Beginner**:
1. Read [Skills User Guide](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)
2. Try built-in skills in Claude apps
3. Customize an example skill

**Intermediate**:
4. Create custom skill with skill-creator
5. Add Python scripts to a skill
6. Share skills with your team

**Advanced**:
7. Use Skills via API
8. Create complex multi-skill workflows
9. Integrate skills with CI/CD

---

## Related Resources

### Official Documentation

- **Claude Apps User Guide**: [Skills Help Center](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)
- **API Documentation**: [Skills API Guide](https://docs.claude.com/en/api/skills-guide)
- **Claude Code**: [Skills for Claude Code](https://docs.claude.com/en/docs/claude-code/skills)
- **Engineering Blog**: [Agent Skills Design Pattern](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### Example Skills

- **GitHub Repository**: [anthropics/skills](https://github.com/anthropics/skills)
- **Skill Examples**: Browse production-ready skills to customize

### Learning Resources

- **Anthropic Academy**: [Build with Claude](https://www.anthropic.com/learn/build-with-claude)
- **Video Tutorials**: YouTube - Anthropic Channel
- **Community**: Share skills and get help

### Security & Safety

- **Security Considerations**: [Using Skills Safely](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_2746475e70)
- **Best Practice**: Only use skills from trusted sources
- **Code Review**: Review Python scripts before installation

---

## Partner Testimonials

### Box
> "Skills teaches Claude how to work with Box content. Users can transform stored files into PowerPoint presentations, Excel spreadsheets, and Word documents that follow their organization's standards—saving hours of effort."
>
> — Yashodha Bhavnani, Head of AI, Box

### Notion
> "With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results."
>
> — MJ Felix, Product Manager, Notion

### Canva
> "Canva plans to leverage Skills to customize agents and expand what they can do. This unlocks new ways to bring Canva deeper into agentic workflows—helping teams capture their unique context and create stunning, high-quality designs effortlessly."
>
> — Anwar Haneef, GM & Head of Ecosystem, Canva

### Rakuten
> "Skills streamline our management accounting and finance workflows. Claude processes multiple spreadsheets, catches critical anomalies, and generates reports using our procedures. What once took a day, we can now accomplish in an hour."
>
> — Yusuke Kaji, General Manager AI, Rakuten

---

## What's Next

**Upcoming Features**:
- Simplified skill creation workflows
- Enterprise-wide deployment capabilities
- Team skill distribution improvements
- Enhanced skill marketplace

**Stay Updated**:
- Follow [Anthropic News](https://www.anthropic.com/news)
- Check [Changelog](https://developers.openai.com/codex/changelog) regularly
- Join community discussions

---

**Version**: 1.0.0
**Last Updated**: October 30, 2025
**Source**: https://www.anthropic.com/news/skills
**Official Documentation**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
