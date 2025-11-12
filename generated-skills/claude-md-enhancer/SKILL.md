---
name: claude-md-enhancer
description: Analyzes, generates, and enhances CLAUDE.md files for any project type using best practices, modular architecture support, and tech stack customization. Use when setting up new projects, improving existing CLAUDE.md files, or establishing AI-assisted development standards.
---

# CLAUDE.md File Enhancer

This skill provides comprehensive CLAUDE.md file generation and enhancement for Claude Code projects. It analyzes existing files, validates against best practices, and generates customized guidelines tailored to your project type, tech stack, and team size.

## Capabilities

- **🆕 Interactive Initialization**: Intelligent workflow that explores your repository, detects project type and tech stack, asks for confirmation, then creates customized CLAUDE.md files
- **✨ 100% Native Format Compliance**: All generated files follow official Claude Code format with project structure diagrams, setup instructions, architecture sections, and file structure explanations (matching `/update-claude-md` slash command)
- **Analyze Existing Files**: Scan and evaluate current CLAUDE.md files for structure, completeness, and quality
- **Validate Best Practices**: Check against Anthropic guidelines (file length, required sections, formatting standards)
- **Generate New Files**: Create complete CLAUDE.md files from scratch for new projects
- **Enhance Existing Files**: Add missing sections, improve structure, and update to latest best practices
- **Modular Architecture**: Support context-specific CLAUDE.md files in subdirectories (backend/, frontend/, docs/)
- **Tech Stack Customization**: Tailor guidelines to specific technologies (TypeScript, Python, Go, React, Vue, etc.)
- **Team Size Adaptation**: Adjust complexity based on team size (solo, small <10, large 10+)
- **Template Selection**: Choose appropriate template based on project complexity and development phase

## Input Requirements

### For Analysis and Enhancement

Provide existing CLAUDE.md file content or file path:

```json
{
  "mode": "enhance",
  "file_path": "CLAUDE.md",
  "content": "[existing CLAUDE.md content]",
  "project_context": {
    "type": "web_app",
    "tech_stack": ["typescript", "react", "node", "postgresql"],
    "team_size": "small",
    "phase": "mvp"
  }
}
```

### For New File Generation

Provide project context:

```json
{
  "mode": "create",
  "project_context": {
    "type": "api",
    "tech_stack": ["python", "fastapi", "postgresql", "docker"],
    "team_size": "medium",
    "phase": "production",
    "workflows": ["tdd", "cicd", "documentation_first"]
  },
  "modular": true,
  "subdirectories": ["backend", "database", "docs"]
}
```

### Context Parameters

- **type**: Project type (`web_app`, `api`, `fullstack`, `cli`, `library`, `mobile`, `desktop`)
- **tech_stack**: Array of technologies (e.g., `["typescript", "react", "node"]`)
- **team_size**: `solo`, `small` (<10), `medium` (10-50), `large` (50+)
- **phase**: Development phase (`prototype`, `mvp`, `production`, `enterprise`)
- **workflows**: Key workflows (`tdd`, `cicd`, `documentation_first`, `agile`, etc.)

## Output Formats

### Analysis Report

```json
{
  "analysis": {
    "file_size": 450,
    "line_count": 320,
    "sections_found": [
      "Quick Navigation",
      "Core Principles",
      "Tech Stack",
      "Workflow Instructions"
    ],
    "missing_sections": [
      "Testing Requirements",
      "Error Handling Patterns"
    ],
    "issues": [
      {
        "type": "length_warning",
        "severity": "medium",
        "message": "File exceeds recommended 300 lines (320 lines)"
      },
      {
        "type": "missing_section",
        "severity": "low",
        "message": "Consider adding 'Testing Requirements' section"
      }
    ],
    "quality_score": 75,
    "recommendations": [
      "Split into modular files (backend/CLAUDE.md, frontend/CLAUDE.md)",
      "Add testing requirements section",
      "Reduce root file to <150 lines"
    ]
  }
}
```

### Generated Content

Complete CLAUDE.md file content or specific sections to add:

```markdown
# CLAUDE.md

This file provides guidance for Claude Code when working with this project.

## Quick Navigation

- [Backend Guidelines](backend/CLAUDE.md)
- [Frontend Guidelines](frontend/CLAUDE.md)
- [Database Operations](database/CLAUDE.md)
- [CI/CD Workflows](.github/CLAUDE.md)

## Core Principles

1. **Test-Driven Development**: Write tests before implementation
2. **Type Safety First**: Use TypeScript strict mode throughout
3. **Component Composition**: Favor small, reusable components
4. **Error Handling**: Always handle errors with proper logging
5. **Documentation Updates**: Keep docs in sync with code changes

[... additional sections based on template ...]
```

## How to Use

### Example 1: Initialize CLAUDE.md for New Project (Interactive)

```
Hey Claude—I just added the "claude-md-enhancer" skill. I don't have a CLAUDE.md file yet. Can you help me create one for this project?
```

**What Happens**:
1. Claude checks if CLAUDE.md exists (it doesn't)
2. Claude explores your repository using built-in commands
3. Claude analyzes: project type, tech stack, team size, workflows
4. Claude shows discoveries and asks for confirmation
5. You confirm the settings
6. Claude creates customized CLAUDE.md file(s)
7. Claude enhances with best practices

**Interactive Flow**:
- ✋ User must confirm before creation
- 🔍 Full visibility into what was discovered
- ⚙️ Option to adjust settings before proceeding

### Example 2: Analyze Existing CLAUDE.md

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you analyze my current CLAUDE.md file and tell me what's missing or could be improved?
```

### Example 2: Generate New CLAUDE.md for TypeScript Project

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you create a CLAUDE.md file for my TypeScript React project with a team of 5 developers? We use PostgreSQL, Docker, and follow TDD practices.
```

### Example 3: Enhance Existing File

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you enhance my existing CLAUDE.md by adding missing sections and improving the structure? Here's my current file: [paste content]
```

### Example 4: Generate Modular Architecture

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you create a modular CLAUDE.md setup for my full-stack project? I need separate files for backend (Python/FastAPI), frontend (React), and database (PostgreSQL).
```

## Initialization Workflow (New Projects)

When CLAUDE.md doesn't exist in your project, this skill provides an intelligent initialization workflow:

### Workflow Steps

**Step 1: Detection**
- Skill checks if CLAUDE.md exists in project root
- If not found, initialization workflow begins

**Step 2: Repository Exploration**
- Uses Claude Code's built-in `explore` command
- Analyzes project structure, files, and directories
- Examines configuration files (package.json, requirements.txt, go.mod, etc.)
- Reviews existing documentation

**Step 3: Intelligent Analysis**
- **Project Type Detection**: web_app, api, fullstack, cli, library, mobile, desktop
- **Tech Stack Detection**: TypeScript, Python, React, FastAPI, PostgreSQL, Docker, etc.
- **Team Size Estimation**: Based on project complexity (solo, small, medium, large)
- **Development Phase**: prototype, mvp, production, enterprise
- **Workflow Detection**: TDD, CI/CD, documentation-first, agile
- **Structure Recommendation**: Single file vs. modular architecture

**Step 4: User Confirmation** ✋
- Displays all discoveries in clear format
- Shows recommended CLAUDE.md structure
- Asks user to confirm or adjust settings
- **User must explicitly approve** before proceeding

**Step 5: File Creation**
- Generates customized CLAUDE.md based on confirmed settings
- Creates modular files if recommended (backend/, frontend/, etc.)
- Applies tech-specific best practices

**Step 6: Enhancement**
- Validates generated content
- Adds quality improvements
- Ensures completeness

**Step 7: Summary**
- Shows what files were created
- Provides next steps
- Ready for immediate use

### Interactive Example

```
User: "I need a CLAUDE.md for this project"

Claude: "I'll explore your repository first to understand the project.
        [Explores using built-in commands]

        Based on my exploration, here's what I discovered:

        Project Type: Full-Stack Application
        Tech Stack: TypeScript, React, Node.js, PostgreSQL, Docker
        Team Size: Small (2-9 developers)
        Development Phase: MVP
        Workflows: TDD, CI/CD

        Recommended Structure: Modular architecture
        - Root CLAUDE.md (navigation hub)
        - backend/CLAUDE.md (API guidelines)
        - frontend/CLAUDE.md (React guidelines)

        Would you like me to create these files?"

User: "Yes, please proceed"

Claude: "Creating customized CLAUDE.md files...
        ✅ Created CLAUDE.md (100 lines)
        ✅ Created backend/CLAUDE.md (150 lines)
        ✅ Created frontend/CLAUDE.md (175 lines)

        Your project is ready for AI-assisted development!"
```

## Scripts

### workflow.py
Manages the interactive initialization workflow for new projects.

**Key Functions**:
- `check_claude_md_exists()` - Detect if CLAUDE.md exists
- `generate_exploration_prompt()` - Guide Claude to explore repository
- `analyze_discoveries()` - Analyze exploration results
- `generate_confirmation_prompt()` - Create user confirmation prompt
- `get_workflow_steps()` - Get complete workflow steps

### analyzer.py
Analyzes existing CLAUDE.md files to identify structure, sections, and quality issues.

**Key Functions**:
- `analyze_file()` - Parse and analyze CLAUDE.md structure
- `detect_sections()` - Identify present and missing sections
- `calculate_quality_score()` - Score file quality (0-100)
- `generate_recommendations()` - Provide actionable improvement suggestions

### validator.py
Validates CLAUDE.md files against best practices and Anthropic guidelines.

**Key Functions**:
- `validate_length()` - Check file length (warn if >300 lines)
- `validate_structure()` - Verify required sections present
- `validate_formatting()` - Check markdown formatting quality
- `validate_completeness()` - Ensure critical information included

### generator.py
Generates new CLAUDE.md content or missing sections based on templates.

**Key Functions**:
- `generate_root_file()` - Create main CLAUDE.md orchestrator
- `generate_context_file()` - Create context-specific files (backend, frontend, etc.)
- `generate_section()` - Generate individual sections (tech stack, workflows, etc.)
- `merge_with_existing()` - Add new sections to existing files

### template_selector.py
Selects appropriate template based on project context.

**Key Functions**:
- `select_template()` - Choose template based on project type and team size
- `customize_template()` - Adapt template to tech stack
- `determine_complexity()` - Calculate appropriate detail level
- `recommend_modular_structure()` - Suggest subdirectory organization

## Best Practices

### Critical Validation Rule ⚠️

**"Always validate your output against official native examples before declaring complete."**

Before finalizing any CLAUDE.md generation:
1. Compare output against `/update-claude-md` slash command format
2. Check official Claude Code documentation for required sections
3. Verify all native format sections are present (Overview, Project Structure, File Structure, Setup & Installation, Architecture, etc.)
4. Cross-check against reference examples in `examples/` folder

### For New Projects
1. Start with minimal template (50-100 lines) and grow as needed
2. Use modular architecture for projects with >3 major components
3. Include tech stack reference immediately
4. Add workflow instructions before team grows beyond 5 people

### For Enhancement
1. Analyze before modifying - understand current structure first
2. Preserve custom content - only enhance, don't replace
3. Validate after changes - ensure improvements don't break existing patterns
4. Test with Claude Code - verify guidelines work as intended

### General Guidelines
1. **Keep root file concise** - Max 150 lines, use as navigation hub
2. **Use context-specific files** - backend/CLAUDE.md, frontend/CLAUDE.md, etc.
3. **Avoid duplication** - Each guideline should appear once
4. **Link to external docs** - Don't copy official documentation
5. **Update regularly** - Review guidelines quarterly or when stack changes

## Limitations

### Technical Constraints
- Requires valid project context for accurate template selection
- Tech stack detection is based on keywords, may need manual refinement
- Modular file generation assumes standard directory structure

### Scope Boundaries
- Focuses on CLAUDE.md structure, not project-specific business logic
- Best practice recommendations are general, may need industry-specific customization
- Validation is guideline-based, not enforcement (no automated fixes without approval)

### When NOT to Use
- For non-Claude AI tools (this is Claude Code specific)
- For projects that don't use Claude Code or similar AI assistants
- When you need highly specialized domain guidelines (legal, medical compliance)

## Template Categories

### By Size
- **Minimal** (50 lines) - Solo developers, prototypes, hackathons
- **Core** (100-150 lines) - Small teams, MVPs, standard projects
- **Detailed** (200-300 lines) - Large teams, production systems, enterprise

### By Project Type
- **Web App** - Frontend-focused (React, Vue, Angular)
- **API** - Backend services (REST, GraphQL, microservices)
- **Full-Stack** - Integrated frontend + backend
- **CLI** - Command-line tools and utilities
- **Library** - Reusable packages and frameworks
- **Mobile** - React Native, Flutter, native iOS/Android

### By Tech Stack
- **TypeScript/Node** - Modern JavaScript ecosystem
- **Python** - Django, FastAPI, Flask
- **Go** - Gin, Echo, native services
- **Java/Kotlin** - Spring Boot, enterprise Java
- **Ruby** - Rails, Sinatra

## Quality Metrics

### File Quality Score (0-100)

Calculated based on:
- **Length appropriateness** (25 points) - Not too short or long
- **Section completeness** (25 points) - Required sections present
- **Formatting quality** (20 points) - Proper markdown structure
- **Content specificity** (15 points) - Tailored to project, not generic
- **Modular organization** (15 points) - Uses subdirectory files when appropriate

### Recommendations Priority

- **Critical** - Missing required sections, file too long (>400 lines)
- **High** - Missing important sections, formatting issues
- **Medium** - Could add optional sections, minor improvements
- **Low** - Nice-to-have enhancements, stylistic suggestions

## Advanced Features

### Modular Architecture Support

Automatically generates context-specific files:

```
project-root/
├── CLAUDE.md                 # Root orchestrator (100-150 lines)
├── backend/
│   └── CLAUDE.md            # Backend-specific (150-200 lines)
├── frontend/
│   └── CLAUDE.md            # Frontend-specific (150-200 lines)
├── database/
│   └── CLAUDE.md            # Database operations (100-150 lines)
└── .github/
    └── CLAUDE.md            # CI/CD workflows (100-150 lines)
```

### Tech Stack Detection

Automatically detects technologies from:
- `package.json` (Node.js/TypeScript)
- `requirements.txt` or `pyproject.toml` (Python)
- `go.mod` (Go)
- `Cargo.toml` (Rust)
- `pom.xml` or `build.gradle` (Java)

### Team Size Adaptation

Adjusts detail level:
- **Solo**: Minimal guidelines, focus on efficiency
- **Small (<10)**: Core guidelines, workflow basics
- **Medium (10-50)**: Detailed guidelines, team coordination
- **Large (50+)**: Comprehensive guidelines, process enforcement

## References

- **Anthropic Claude Code Docs**: https://docs.claude.com/en/docs/claude-code
- **CLAUDE.md Best Practices**: Based on community patterns and Anthropic guidance
- **Example CLAUDE.md Files**: See `examples/` folder for 6 reference implementations covering different project types and team sizes

## Version

**Version**: 1.0.0
**Last Updated**: November 2025
**Compatible**: Claude Code 2.0+, Claude Apps, Claude API

Remember: The goal is to make Claude more efficient and context-aware, not to create bureaucracy. Start simple, iterate based on real usage, and automate quality checks where possible.
