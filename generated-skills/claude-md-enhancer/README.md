# claude-md-enhancer

> **Analyze, generate, and enhance CLAUDE.md files for any project type with intelligent templates and best practices.**

A comprehensive Claude Code skill that helps teams create and maintain high-quality CLAUDE.md files. Supports analysis, validation, generation, and enhancement with tech stack customization, team size adaptation, and modular architecture.

## Features

🆕 **Interactive Initialization** - Explore repository, detect project context, and create CLAUDE.md through conversational workflow
✨ **100% Native Format Compliance** - All generated files follow official Claude Code format with project structure diagrams, setup instructions, architecture sections, and file structure explanations
✅ **Intelligent Analysis** - Scan and evaluate existing CLAUDE.md files for quality and completeness
🎯 **Best Practice Validation** - Check against Anthropic guidelines and community standards
🚀 **Smart Generation** - Create customized CLAUDE.md files from scratch
🔧 **Enhancement** - Add missing sections and improve existing files
📦 **Modular Architecture** - Support context-specific files (backend/, frontend/, database/)
🛠️ **Tech Stack Customization** - Tailor guidelines to your technologies
👥 **Team Size Adaptation** - Adjust complexity for solo, small, medium, or large teams
📊 **Quality Scoring** - Get 0-100 quality scores with actionable recommendations

---

## Quick Start

### Installation

#### Option 1: Claude Code (Project-Level)

```bash
# Copy skill folder to your project
cp -r claude-md-enhancer /path/to/your/project/.claude/skills/

# Restart Claude Code or reload skills
```

#### Option 2: Claude Code (User-Level)

```bash
# Copy skill folder to user skills directory
cp -r claude-md-enhancer ~/.claude/skills/

# Available across all your projects
```

#### Option 3: Claude Apps

```
1. Open Claude in browser
2. Go to Skills settings
3. Upload claude-md-enhancer.zip
4. Enable the skill
```

### Basic Usage

#### New Project (Interactive Initialization)

```
Hey Claude—I just added the "claude-md-enhancer" skill. I don't have a CLAUDE.md file yet. Can you help me create one for this project?
```

Claude will:
1. Explore your repository
2. Detect project type, tech stack, team size
3. Show discoveries and ask for confirmation
4. Create customized CLAUDE.md file(s)

#### Existing Project

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you analyze my CLAUDE.md and suggest improvements?
```

See [HOW_TO_USE.md](HOW_TO_USE.md) for comprehensive examples.

---

## Architecture

### Module Overview

```
claude-md-enhancer/
├── SKILL.md                    # Skill definition with YAML frontmatter
├── analyzer.py                 # Analyzes existing CLAUDE.md files
├── validator.py                # Validates against best practices
├── generator.py                # Generates new content
├── template_selector.py        # Selects appropriate templates
├── sample_input.json           # Example inputs
├── expected_output.json        # Expected outputs
├── HOW_TO_USE.md               # Usage examples
└── README.md                   # This file
```

### Python Modules

#### `workflow.py` - Initialization Workflow (New!)

**Class**: `InitializationWorkflow`

**Key Methods**:
- `check_claude_md_exists()` - Detect if CLAUDE.md exists
- `generate_exploration_prompt()` - Guide Claude to explore repository
- `analyze_discoveries(results)` - Analyze exploration results to detect project context
- `generate_confirmation_prompt(context)` - Create user confirmation prompt
- `get_workflow_steps()` - Get complete 7-step workflow

**Workflow Steps**:
1. Check for existing CLAUDE.md
2. Explore repository (built-in Claude Code command)
3. Analyze discoveries (project type, tech stack, team size)
4. Request user confirmation
5. Create CLAUDE.md file(s)
6. Enhance with best practices
7. Provide summary

**Detection Capabilities**:
- **Project Types**: web_app, api, fullstack, cli, library, mobile, desktop
- **Tech Stacks**: TypeScript, Python, Go, React, Vue, FastAPI, Django, PostgreSQL, Docker, Kubernetes, etc.
- **Team Sizes**: solo, small (<10), medium (10-50), large (50+)
- **Development Phases**: prototype, mvp, production, enterprise
- **Workflows**: TDD, CI/CD, documentation-first, agile

#### `analyzer.py` - File Analysis

**Class**: `CLAUDEMDAnalyzer`

**Key Methods**:
- `analyze_file()` - Comprehensive file analysis
- `detect_sections()` - Identify all sections and subsections
- `calculate_quality_score()` - Score 0-100 based on multiple factors
- `generate_recommendations()` - Actionable improvement suggestions

**Quality Score Breakdown** (0-100):
- Length appropriateness: 25 points
- Section completeness: 25 points
- Formatting quality: 20 points
- Content specificity: 15 points
- Modular organization: 15 points

#### `validator.py` - Best Practices Validation

**Class**: `BestPracticesValidator`

**Key Methods**:
- `validate_length()` - Check file length (20-300 lines recommended)
- `validate_structure()` - Verify required sections and hierarchy
- `validate_formatting()` - Check markdown formatting quality
- `validate_completeness()` - Ensure critical content included
- `validate_all()` - Run all validation checks

**Validation Categories**:
- File length (MUST be 20-300 lines)
- Structure (required sections: Core Principles, Workflow)
- Formatting (balanced code blocks, heading hierarchy)
- Completeness (code examples, links, lists)
- Anti-patterns (hardcoded secrets, placeholders, broken links)

#### `generator.py` - Content Generation

**Class**: `ContentGenerator`

**Key Methods**:
- `generate_root_file()` - Create main CLAUDE.md (navigation hub)
- `generate_context_file(context)` - Create context-specific files
- `generate_section(name)` - Generate individual sections
- `merge_with_existing(content, sections)` - Enhance existing files

**Supported Contexts**:
- `backend` - API design, database, error handling
- `frontend` - Components, state, styling, performance
- `database` - Schema, migrations, query optimization
- `docs` - Documentation standards
- `.github` - CI/CD workflows

#### `template_selector.py` - Template Selection

**Class**: `TemplateSelector`

**Key Methods**:
- `select_template()` - Choose template based on project context
- `customize_template(template)` - Generate customized content
- `recommend_modular_structure()` - Determine if modular architecture needed

**Template Matrix**:

| Project Type | Team Size | Target Lines | Complexity |
|--------------|-----------|--------------|------------|
| Web App | Solo | 75 | Minimal |
| API | Small (<10) | 125 | Core |
| Full-Stack | Medium (10-50) | 200 | Detailed |
| Library | Large (50+) | 275 | Comprehensive |

**Supported Project Types**:
- `web_app` - Frontend-focused (React, Vue, Angular)
- `api` - Backend services (REST, GraphQL)
- `fullstack` - Integrated frontend + backend
- `cli` - Command-line tools
- `library` - Reusable packages
- `mobile` - React Native, Flutter
- `desktop` - Electron, Tauri

**Supported Tech Stacks**:
- TypeScript/JavaScript (React, Vue, Angular, Node)
- Python (Django, FastAPI, Flask)
- Go (Gin, Echo)
- Java/Kotlin (Spring Boot)
- Ruby (Rails)
- And more...

---

## Use Cases

### 1. Analyze Existing CLAUDE.md

**Scenario**: You have a CLAUDE.md file and want quality feedback.

**Input**: Existing file content + project context

**Output**:
- Quality score (0-100)
- Missing sections identified
- Issues and warnings
- Prioritized recommendations

**Example**:
```
Quality Score: 75/100

Missing Sections:
- Testing Requirements
- Error Handling Patterns

Recommendations:
1. Add testing requirements section
2. Reduce file length from 320 to <300 lines
3. Consider modular architecture
```

---

### 2. Generate New CLAUDE.md from Scratch

**Scenario**: Starting new project, need CLAUDE.md file.

**Input**: Project context (type, tech stack, team size, phase)

**Output**: Complete CLAUDE.md tailored to your specifications

**Generated Sections**:
- Quick Navigation (if modular)
- Core Principles
- Tech Stack
- Workflow Instructions
- Testing Requirements
- Error Handling
- Documentation Standards
- Performance Guidelines

---

### 3. Enhance Existing File

**Scenario**: Your CLAUDE.md is missing important sections.

**Input**: Current content + sections to add

**Output**: Enhanced file with new sections, preserving existing content

**Preservation**:
- Keeps all existing content intact
- Adds new sections seamlessly
- Maintains consistent formatting
- Respects your style choices

---

### 4. Generate Modular Architecture

**Scenario**: Large project needs separate CLAUDE.md files.

**Input**: Project context + modular flag + subdirectories

**Output**:
- Root CLAUDE.md (navigation hub, <150 lines)
- backend/CLAUDE.md (API, database, testing)
- frontend/CLAUDE.md (components, state, styling)
- database/CLAUDE.md (schema, migrations, queries)
- .github/CLAUDE.md (CI/CD workflows)

**When Recommended**:
- Full-stack projects
- Large teams (10+ developers)
- Production/enterprise phase
- 3+ major tech components

---

### 5. Validate Before Commit

**Scenario**: Quick quality check before committing.

**Input**: Current CLAUDE.md content

**Output**:
- Pass/fail status
- Validation results (5 checks)
- Errors and warnings
- Pass/fail counts

**Validation Checks**:
1. File length (20-300 lines)
2. Structure (required sections present)
3. Formatting (markdown quality)
4. Completeness (essential content)
5. Anti-patterns (security, placeholders)

---

## Sample Data

### Sample Input

See [sample_input.json](sample_input.json) for 6 realistic scenarios:

1. **analyze_existing** - Analyze basic CLAUDE.md file
2. **create_new_fullstack** - Generate modular full-stack setup
3. **enhance_with_missing_sections** - Add specific sections
4. **create_modular_architecture** - Large team, enterprise setup
5. **validate_existing** - Validate production-ready file
6. **generate_context_specific** - Backend-only file

### Expected Output

See [expected_output.json](expected_output.json) for:

- Analysis reports with quality scores
- Generated CLAUDE.md content
- Validation results
- Enhanced file examples

---

## Best Practices

### Critical Validation Rule ⚠️

**"Always validate your output against official native examples before declaring complete."**

Before finalizing any CLAUDE.md generation:
1. Compare output against `/update-claude-md` slash command format
2. Check official Claude Code documentation for required sections
3. Verify all native format sections are present (Overview, Project Structure, File Structure, Setup & Installation, Architecture, etc.)
4. Cross-check against reference examples in `examples/` folder

### For New Projects

1. **Start Minimal** - Generate 50-100 line file, expand as needed
2. **Add Tech Stack Early** - Include technologies immediately
3. **Update with Team Growth** - Regenerate when team size changes
4. **Consider Modular** - Use separate files if >3 major components

### For Existing Projects

1. **Analyze First** - Understand current state before changes
2. **Preserve Custom Content** - Don't overwrite your specific guidelines
3. **Validate Regularly** - Check quality when stack or team changes
4. **Iterate** - Start with enhancements, full regeneration if needed

### General Guidelines

1. **Keep Root Concise** - Max 150 lines, use as navigation hub
2. **Use Context Files** - backend/, frontend/, etc. for details
3. **Avoid Duplication** - Each guideline appears once
4. **Link External Docs** - Don't copy official documentation
5. **Update Quarterly** - Review and refresh every 3 months

---

## Configuration

### Project Context Parameters

```json
{
  "type": "fullstack",                              // Project type
  "tech_stack": ["typescript", "react", "node"],    // Technologies
  "team_size": "small",                             // Team size
  "phase": "mvp",                                   // Development phase
  "workflows": ["tdd", "cicd"],                     // Key workflows
  "modular": true,                                  // Modular architecture
  "subdirectories": ["backend", "frontend"]         // Subdirs for context files
}
```

#### Type Options
- `web_app` - Frontend-focused
- `api` - Backend services
- `fullstack` - Full-stack application
- `cli` - Command-line tool
- `library` - Reusable package
- `mobile` - Mobile application
- `desktop` - Desktop application

#### Team Size Options
- `solo` - 1 developer
- `small` - 2-9 developers
- `medium` - 10-49 developers
- `large` - 50+ developers

#### Phase Options
- `prototype` - Early exploration
- `mvp` - Minimum viable product
- `production` - Production system
- `enterprise` - Enterprise-grade

---

## Troubleshooting

### Quality Score Lower Than Expected

**Issue**: Quality score is 35/100

**Solutions**:
1. Check file length (should be 20-300 lines)
2. Add missing required sections (Core Principles, Workflow)
3. Include code examples
4. Add tech stack references
5. Consider modular architecture if >300 lines

---

### Generated Content Too Generic

**Issue**: CLAUDE.md lacks specific guidance

**Solutions**:
1. Provide detailed tech stack (specific frameworks/versions)
2. Specify workflows (TDD, CI/CD, documentation-first)
3. Include team size for appropriate complexity
4. Add development phase for priority focus
5. Customize generated content for your needs

---

### Modular Architecture Not Recommended

**Issue**: Single file generated, wanted modular

**Solutions**:
1. Set `"modular": true` explicitly
2. Ensure project type is `fullstack`
3. Use team size `medium` or `large`
4. Specify phase as `production` or `enterprise`
5. Provide 3+ tech stack components

---

## Version

**Version**: 1.0.0
**Last Updated**: November 2025
**Compatible**: Claude Code 2.0+, Claude Apps, Claude API

---

## Contributing

Found a bug or have a suggestion? This skill is part of the [claude-code-skills-factory](https://github.com/anthropics/claude-code-skills-factory) repository.

---

## License

MIT License - See LICENSE file for details

---

## Companion Agent: claude-md-guardian 🛡️

For automatic CLAUDE.md maintenance throughout your project lifecycle, use the **claude-md-guardian** agent:

### What It Does

- **Auto-Sync**: Updates CLAUDE.md based on project changes
- **Background Operation**: Works independently after milestones
- **Smart Detection**: Only updates when significant changes occur
- **Token-Efficient**: Uses haiku model for routine updates

### When It Triggers

**Automatically**:
- SessionStart (checks git changes)
- After feature completion
- After major refactoring
- After new dependencies added
- After architecture changes

**Manually**:
- Via `/enhance-claude-md` slash command
- Direct invocation

### Installation

```bash
# User-level (all projects)
cp generated-agents/claude-md-guardian/claude-md-guardian.md ~/.claude/agents/

# Project-level (current project)
cp generated-agents/claude-md-guardian/claude-md-guardian.md .claude/agents/
```

### How They Work Together

```
claude-md-guardian (agent) → Uses → claude-md-enhancer (skill)
                      ↓
         Detects changes → Invokes skill → Updates CLAUDE.md
```

**Result**: Your CLAUDE.md stays synchronized with your codebase automatically!

See `generated-agents/claude-md-guardian/README.md` for complete agent documentation.

---

## Support

- **Documentation**: See [SKILL.md](SKILL.md) for complete documentation
- **Examples**: See [HOW_TO_USE.md](HOW_TO_USE.md) for usage examples
- **Companion Agent**: See `../../generated-agents/claude-md-guardian/README.md`
- **Slash Command**: See `../../generated-commands/enhance-claude-md/README.md`
- **Issues**: Report bugs in the main repository
- **Community**: Share your CLAUDE.md setups and best practices

---

**Happy coding with Claude! 🚀**

Make your AI-assisted development more efficient with well-structured CLAUDE.md files and automatic maintenance via claude-md-guardian!

