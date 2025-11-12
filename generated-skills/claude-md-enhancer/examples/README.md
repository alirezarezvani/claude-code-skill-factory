# CLAUDE.md Reference Examples

This folder contains reference implementations of CLAUDE.md files for different project types and team sizes.

**✨ NEW**: All examples now follow **100% native Claude Code format** with proper project structure diagrams, setup instructions, architecture sections, and file structure explanations - matching the official `/update-claude-md` slash command format.

## Available Examples

### By Complexity Level

| Example | Lines | Team Size | Use Case |
|---------|-------|-----------|----------|
| `minimal-solo-CLAUDE.md` | ~75 | Solo | Prototypes, hackathons, quick projects |
| `core-small-team-CLAUDE.md` | ~175 | Small (5) | MVPs, small team projects |
| `modular-root-CLAUDE.md` | ~150 | Medium (12) | Full-stack production apps (root file) |
| `python-api-CLAUDE.md` | ~225 | Small (6) | Python FastAPI backend projects |

### By Project Type

| Example | Project Type | Tech Stack |
|---------|--------------|------------|
| `minimal-solo-CLAUDE.md` | Web App Prototype | TypeScript, React, Node |
| `core-small-team-CLAUDE.md` | Web Application MVP | React, Node, PostgreSQL |
| `python-api-CLAUDE.md` | Backend API | Python, FastAPI, PostgreSQL |
| `modular-root-CLAUDE.md` | Full-Stack App (root) | React, Node, PostgreSQL |
| `modular-backend-CLAUDE.md` | Backend (context-specific) | Node, Express, PostgreSQL |
| `modular-frontend-CLAUDE.md` | Frontend (context-specific) | React, TypeScript, Tailwind |

## Modular Architecture Examples

For projects with multiple major components, use separate CLAUDE.md files:

**Root Navigation Hub**:
- `modular-root-CLAUDE.md` - Root file with navigation (~150 lines)

**Context-Specific Files**:
- `modular-backend-CLAUDE.md` - Backend guidelines (~200 lines)
- `modular-frontend-CLAUDE.md` - Frontend guidelines (~225 lines)

## How to Use These Examples

### 1. Starting a New Project

```bash
# Copy appropriate template to your project
cp examples/core-small-team-CLAUDE.md /path/to/your/project/CLAUDE.md

# Customize for your tech stack and workflows
```

### 2. Setting Up Modular Architecture

```bash
# Copy root file to project root
cp examples/modular-root-CLAUDE.md /path/to/your/project/CLAUDE.md

# Copy context-specific files to subdirectories
cp examples/modular-backend-CLAUDE.md /path/to/your/project/backend/CLAUDE.md
cp examples/modular-frontend-CLAUDE.md /path/to/your/project/frontend/CLAUDE.md
```

### 3. Using with claude-md-enhancer Skill

These examples demonstrate the output quality you can expect from the skill:

```
Hey Claude—I just added the "claude-md-enhancer" skill.
Can you create a CLAUDE.md similar to the core-small-team example
but customized for my Go API project?
```

## Template Selection Guide

### Choose Minimal Template When:
- Solo developer
- Prototype or proof-of-concept
- Hackathon or time-boxed project
- Need quick setup with minimal guidance

### Choose Core Template When:
- Small team (2-10 developers)
- MVP or early-stage product
- Standard web application
- Need comprehensive but concise guidelines

### Choose Modular Architecture When:
- Medium/large team (10+ developers)
- Full-stack or complex application
- Multiple major components (frontend, backend, database, etc.)
- Production or enterprise environment

### Choose Tech-Specific Template When:
- Specific tech stack (Python/FastAPI, Go, etc.)
- Team needs stack-specific best practices
- Want language-specific examples and patterns

## Quality Metrics

### Native Format Sections (100% Compliance)

All examples now include these **native Claude Code sections**:

- ✅ **Overview** - Concise project description
- ✅ **Project Structure** - ASCII tree diagram showing folder hierarchy
- ✅ **File Structure** - Detailed explanations of directories and their purpose
- ✅ **Setup & Installation** - Step-by-step setup commands
- ✅ **Architecture** - System architecture and component flow (for complex projects)
- ✅ **Core Principles** - Development philosophies and standards
- ✅ **Tech Stack** - Technologies with versions
- ✅ **Development Workflow** - Step-by-step development process
- ✅ **Testing Requirements** - Testing strategy and coverage targets
- ✅ **Error Handling** - Error handling patterns and best practices
- ✅ **Common Commands** - Frequently used commands with descriptions

**Why This Matters**: These sections match the official `/update-claude-md` slash command format, ensuring Claude Code can navigate and understand your codebase efficiently.

### Expected Quality Scores

| Example | Quality Score |
|---------|---------------|
| `minimal-solo-CLAUDE.md` | 70-75/100 |
| `core-small-team-CLAUDE.md` | 85-90/100 |
| `modular-root-CLAUDE.md` | 80-85/100 |
| `modular-backend-CLAUDE.md` | 90-95/100 |
| `modular-frontend-CLAUDE.md` | 90-95/100 |
| `python-api-CLAUDE.md` | 85-90/100 |

## Customization Tips

1. **Update Tech Stack**: Replace technologies with your actual stack
2. **Adjust Workflows**: Modify development process to match your team
3. **Add Team Standards**: Include team-specific conventions
4. **Update Commands**: Replace commands with your actual npm/yarn/poetry scripts
5. **Add Context**: Include project-specific context that helps Claude understand your goals

## Contributing

These examples represent best practices as of November 2025. If you have improvements or additional examples, please contribute them!
