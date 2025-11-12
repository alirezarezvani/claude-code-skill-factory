# How to Use the claude-md-enhancer Skill

Hey Claude—I just added the "claude-md-enhancer" skill. Can you help me create or improve my project's CLAUDE.md file?

## Example Invocations

### Example 1: Initialize CLAUDE.md for New Project (🆕 Interactive Workflow)

**Use Case**: You don't have a CLAUDE.md file yet and want Claude to create one by understanding your project first.

```
Hey Claude—I just added the "claude-md-enhancer" skill. I don't have a CLAUDE.md file yet. Can you help me create one for this project?
```

**What Claude Will Do**:
1. Check if CLAUDE.md exists (it doesn't)
2. Explore your repository using built-in commands
3. Analyze project structure, tech stack, team size
4. Show you the discoveries and ask for confirmation
5. Create customized CLAUDE.md file(s) after your approval
6. Enhance with best practices

**Interactive Conversation Example**:

```
User: "I don't have a CLAUDE.md. Can you create one?"

Claude: "I'll explore your repository first to understand the project.

        [Exploring repository structure...]
        [Analyzing package.json, requirements.txt, etc...]
        [Detecting workflows and patterns...]

        Based on my exploration, here's what I discovered:

        📦 **Project Type**: Full-Stack Application
        🛠️ **Tech Stack**: TypeScript, React, Node.js, PostgreSQL, Docker
        👥 **Team Size**: Small (5 developers detected from git history)
        🚀 **Development Phase**: MVP (CI/CD present, production features in progress)
        ⚙️ **Workflows**: TDD (tests/ folder found), CI/CD (GitHub Actions detected)

        📋 **Recommended Structure**:
        Modular architecture - I recommend creating:
        - Root CLAUDE.md (navigation hub, ~100 lines)
        - backend/CLAUDE.md (API and database guidelines, ~150 lines)
        - frontend/CLAUDE.md (React component guidelines, ~175 lines)

        Would you like me to create these files with these settings?
        You can also ask me to adjust any of these if they don't look right."

User: "Yes, that looks perfect. Please proceed."

Claude: "Creating your customized CLAUDE.md files...

        ✅ Created CLAUDE.md (108 lines)
           - Quick Navigation section with links
           - 5 Core Principles (TDD-focused)
           - Tech Stack summary
           - Quick reference commands

        ✅ Created backend/CLAUDE.md (156 lines)
           - API Design guidelines (RESTful, versioning)
           - Database operations (migrations, queries)
           - Error handling patterns
           - Testing requirements (80% coverage)

        ✅ Created frontend/CLAUDE.md (182 lines)
           - React component standards (functional, hooks)
           - State management (Context API)
           - Styling guidelines (Tailwind)
           - Performance optimization

        🎉 Your project is now set up for efficient AI-assisted development!

        Next steps:
        1. Review the generated files
        2. Customize core principles for your team
        3. Add any project-specific conventions
        4. Start developing with Claude Code!"

User: "Perfect, thanks!"
```

**When to Use This**:
- New project without CLAUDE.md
- Want Claude to understand your project first
- Need recommendations on structure
- Prefer interactive, conversational setup

---

### Example 2: Quick Initialization (Skip Exploration)

**Use Case**: You know your project details and want to skip the exploration step.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Create a CLAUDE.md for my TypeScript React project with PostgreSQL. Small team (5 devs), MVP phase, using TDD and CI/CD.
```

**What Claude Will Do**:
- Skip exploration (you provided context)
- Generate CLAUDE.md immediately
- Customize for specified tech stack
- No confirmation needed (direct request)

---

### Example 3: Analyze Existing CLAUDE.md

**Use Case**: You have an existing CLAUDE.md file and want to know what's missing or could be improved.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you analyze my current CLAUDE.md file and tell me what's missing or could be improved? Here it is:

# CLAUDE.md

## Tech Stack
- TypeScript
- React
- Node.js

## Workflow
- Use Git for version control
- Write tests
```

**What Claude Will Do**:
- Analyze file structure and completeness
- Calculate quality score (0-100)
- Identify missing sections
- Provide actionable recommendations

---

### Example 2: Generate New CLAUDE.md for TypeScript React Project

**Use Case**: Starting a new TypeScript React project and need a CLAUDE.md file from scratch.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you create a CLAUDE.md file for my TypeScript React project? We're a team of 5 developers working on an MVP. We use PostgreSQL, Docker, and follow TDD practices.
```

**What Claude Will Do**:
- Generate complete CLAUDE.md tailored to TypeScript/React
- Include tech stack references
- Add TDD workflow guidelines
- Customize for small team (5 people)
- Include MVP-phase appropriate content

---

### Example 3: Enhance Existing File with Missing Sections

**Use Case**: You have a basic CLAUDE.md but it's missing important sections.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you enhance my existing CLAUDE.md by adding Testing Requirements, Error Handling Patterns, and Performance Guidelines sections? Here's what I have:

# CLAUDE.md

## Core Principles
1. Write tests first
2. Use TypeScript

## Tech Stack
- TypeScript
- React
- PostgreSQL
```

**What Claude Will Do**:
- Preserve your existing content
- Add the three requested sections
- Populate sections with relevant best practices
- Ensure consistency with your existing style

---

### Example 4: Generate Modular CLAUDE.md Architecture

**Use Case**: You have a complex full-stack project and want separate CLAUDE.md files for different parts.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you create a modular CLAUDE.md setup for my full-stack project? I need separate files for:
- Backend (Python/FastAPI)
- Frontend (React/TypeScript)
- Database (PostgreSQL)

We're a team of 8, building a production system.
```

**What Claude Will Do**:
- Generate root CLAUDE.md (navigation hub)
- Create backend/CLAUDE.md with API and service guidelines
- Create frontend/CLAUDE.md with React component standards
- Create database/CLAUDE.md with migration and query guidelines
- Customize for medium team size and production phase

---

### Example 5: Validate Existing CLAUDE.md

**Use Case**: You want to check if your CLAUDE.md follows best practices.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you validate my CLAUDE.md file against best practices? Here it is: [paste your CLAUDE.md content]
```

**What Claude Will Do**:
- Check file length (warns if >300 lines)
- Verify required sections are present
- Check markdown formatting quality
- Detect anti-patterns (hardcoded secrets, placeholders)
- Provide pass/fail status with detailed feedback

---

### Example 6: Create CLAUDE.md for Python API Project

**Use Case**: Building a Python FastAPI backend service.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you create a CLAUDE.md for my Python FastAPI project? We're building a microservice API with PostgreSQL, Redis, and deploying with Docker/Kubernetes. Team of 12 developers, enterprise production environment.
```

**What Claude Will Do**:
- Generate API-focused CLAUDE.md
- Include FastAPI-specific best practices
- Add microservices architecture guidelines
- Customize for large team (12 developers)
- Include enterprise-grade standards

---

### Example 7: Add Specific Section to Existing File

**Use Case**: You need to add just one specific section.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you add a "Security Checklist" section to my existing CLAUDE.md?
```

**What Claude Will Do**:
- Generate Security Checklist section
- Include relevant security best practices
- Merge seamlessly with existing content
- Maintain your file's existing structure

---

### Example 8: Convert Generic CLAUDE.md to Tech-Specific

**Use Case**: You have a generic CLAUDE.md and want to customize it for your tech stack.

```
Hey Claude—I just added the "claude-md-enhancer" skill. I have a generic CLAUDE.md file. Can you customize it for my Vue 3, Go (Gin), and MongoDB tech stack?
```

**What Claude Will Do**:
- Detect your current content
- Add Vue 3-specific component guidelines
- Add Go/Gin API patterns
- Add MongoDB query optimization practices
- Preserve your existing custom sections

---

### Example 9: Generate Context-Specific File Only

**Use Case**: You just need guidelines for one part of your project.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you create a backend/CLAUDE.md file for my Node.js Express API project?
```

**What Claude Will Do**:
- Generate backend-specific guidelines
- Include Express.js patterns
- Add API design best practices
- Include testing and error handling sections

---

### Example 10: Quick Quality Check

**Use Case**: Quick validation before committing your CLAUDE.md file.

```
Hey Claude—I just added the "claude-md-enhancer" skill. Can you do a quick quality check on my CLAUDE.md? Give me a quality score and top 3 improvements.
```

**What Claude Will Do**:
- Calculate quality score (0-100)
- Identify top 3 issues/improvements
- Provide concise, actionable feedback
- Highlight critical issues first

---

## What to Provide

When using this skill, provide any of the following:

### For Analysis
- Existing CLAUDE.md content (paste the full text)
- Project context (optional but helpful):
  - Project type (web app, API, mobile, etc.)
  - Tech stack (languages, frameworks, tools)
  - Team size (solo, small, medium, large)
  - Development phase (prototype, MVP, production)

### For Generation
- Project type (web_app, api, fullstack, cli, library, mobile, desktop)
- Tech stack (e.g., "TypeScript, React, Node, PostgreSQL")
- Team size (solo, small <10, medium 10-50, large 50+)
- Development phase (prototype, MVP, production, enterprise)
- Key workflows (TDD, CI/CD, documentation-first, agile)
- Modular architecture preference (yes/no)

### For Enhancement
- Current CLAUDE.md content
- Specific sections to add or improve
- Any new technologies adopted

---

## What You'll Get

### Analysis Output
- Quality score (0-100)
- Missing sections list
- Issues and warnings
- Prioritized recommendations
- Structure analysis

### Generation Output
- Complete CLAUDE.md file(s)
- Tailored to your tech stack
- Appropriate for your team size
- Customized for development phase
- Modular architecture if requested

### Validation Output
- Pass/fail status
- Detailed validation results
- Errors and warnings
- Specific improvement suggestions

### Enhancement Output
- Updated CLAUDE.md with new sections
- Preserved existing content
- Consistent formatting
- Integrated recommendations

---

## Pro Tips

1. **Start Simple**: For new projects, start with a minimal CLAUDE.md and expand as needed
2. **Use Modular Architecture**: For projects >3 major components, use separate files (backend/, frontend/, etc.)
3. **Keep Root File Concise**: Aim for <150 lines in root CLAUDE.md, use it as navigation
4. **Validate Regularly**: Run quality checks when team or tech stack changes
5. **Update Quarterly**: Review and update CLAUDE.md every 3 months or when stack changes
6. **Be Specific**: The more context you provide, the better the customization
7. **Iterate**: Start with generated content, then customize for your specific needs

---

## Common Scenarios

| Scenario | Recommended Approach |
|----------|---------------------|
| New project, solo developer | Generate minimal CLAUDE.md (~75 lines) |
| New project, small team | Generate core CLAUDE.md (~125 lines) |
| Existing project, needs cleanup | Analyze first, then enhance based on recommendations |
| Large project, multiple teams | Generate modular architecture (root + context files) |
| Pre-commit check | Quick validate with quality score |
| Tech stack changed | Enhance with new tech-specific guidelines |
| Team grew significantly | Regenerate with new team size configuration |

---

**Remember**: The goal is to make Claude Code more efficient and context-aware for your project. Start with what's helpful, iterate based on usage, and keep it maintainable!
