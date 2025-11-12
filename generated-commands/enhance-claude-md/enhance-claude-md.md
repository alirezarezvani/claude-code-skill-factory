---
allowed-tools: Bash(ls:*), Bash(find:*), Bash(git status:*), Read, Glob, Skill
description: Initialize or enhance CLAUDE.md files using the claude-md-enhancer skill with interactive workflow and 100% native format compliance
---

# CLAUDE.md Enhancer Command

This command uses the `claude-md-enhancer` skill to initialize or enhance CLAUDE.md files for your project.

---

## Phase 1: Discovery - Check Current State

### Check if CLAUDE.md exists

!`ls -la CLAUDE.md 2>/dev/null || echo "CLAUDE.md not found"`

### Check for modular CLAUDE.md files

!`find . -name "CLAUDE.md" -type f -not -path "./node_modules/*" -not -path "./.git/*" | head -10`

### Get repository status

!`git status --short 2>/dev/null || echo "Not a git repository"`

### Check project structure

!`ls -la`

---

## Phase 2: Analysis - Determine Action

Based on the discovery above, I need to determine the appropriate action:

**If CLAUDE.md does NOT exist** → Interactive Initialization Workflow
**If CLAUDE.md exists** → Analysis and Enhancement Workflow

### For New Projects (No CLAUDE.md):

The `claude-md-enhancer` skill will:
1. Explore your repository structure
2. Detect project type, tech stack, team size, development phase
3. Show you the discoveries and ask for confirmation
4. Create customized CLAUDE.md file(s) after your approval
5. Apply 100% native format compliance (project structure diagrams, setup instructions, architecture sections)

### For Existing Projects (CLAUDE.md exists):

The `claude-md-enhancer` skill will:
1. Analyze current CLAUDE.md for quality and completeness
2. Calculate quality score (0-100)
3. Identify missing sections
4. Provide actionable recommendations
5. Offer to enhance with missing native format sections

---

## Phase 3: Task - Execute with Skill or Agent

### Option A: Direct Skill Invocation

I can invoke the `claude-md-enhancer` skill directly to handle the appropriate workflow based on what I discovered above.

The skill provides:
- ✨ **100% Native Format Compliance**: All generated files follow official Claude Code format with project structure diagrams, setup instructions, architecture sections, and file structure explanations
- 🆕 **Interactive Initialization**: For new projects, explores repository and asks for confirmation before creating files
- ✅ **Intelligent Analysis**: For existing projects, scans and evaluates for quality and completeness
- 🚀 **Smart Generation**: Creates customized CLAUDE.md files from scratch
- 🔧 **Enhancement**: Adds missing sections and improves existing files
- 📦 **Modular Architecture**: Supports context-specific files (backend/, frontend/, database/)

### Option B: Agent Invocation (Recommended for Maintenance)

For ongoing maintenance and automatic updates throughout your project lifecycle, I can invoke the `claude-md-guardian` agent instead:

**When to use the agent**:
- After feature completion
- After major refactoring
- When new dependencies are added
- After architecture changes
- For periodic CLAUDE.md synchronization

**Agent benefits**:
- 🔄 **Auto-Sync**: Updates CLAUDE.md based on detected changes
- 🎯 **Smart Detection**: Only updates when significant changes occur
- ⚡ **Token-Efficient**: Uses haiku model for routine updates
- 📦 **Milestone-Aware**: Triggers after completion signals
- ✨ **Native Format**: Ensures 100% Claude Code format compliance

### Your Task

I'm ready to proceed. What would you like me to do?

**For new projects**: I'll run the interactive initialization workflow (skill)
**For existing projects**: I'll analyze your current CLAUDE.md and suggest improvements (skill)
**For maintenance**: I'll invoke claude-md-guardian agent to check for updates and synchronize

Please confirm how you'd like to proceed, or let me know if you have specific requirements (e.g., "Create a CLAUDE.md for my Python FastAPI project" or "Invoke claude-md-guardian to update my CLAUDE.md").
