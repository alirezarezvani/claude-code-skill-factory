# /enhance-claude-md Slash Command

Initialize or enhance CLAUDE.md files using the `claude-md-enhancer` skill with interactive workflow and 100% native format compliance.

## Features

- **Multi-Phase Discovery**: Automatically detects if CLAUDE.md exists and determines appropriate action
- **Interactive Workflow**: For new projects, explores repository and asks for confirmation before creating files
- **Quality Analysis**: For existing projects, analyzes current CLAUDE.md and provides actionable recommendations
- **100% Native Format Compliance**: Generates files with project structure diagrams, setup instructions, architecture sections
- **Modular Architecture Support**: Creates context-specific CLAUDE.md files (backend/, frontend/, database/)

## Installation

### Option 1: Project-Level (Current Project Only)

```bash
# Copy command to your project
cp -r generated-commands/enhance-claude-md /path/to/your/project/.claude/commands/

# Or create symlink
ln -s $(pwd)/generated-commands/enhance-claude-md /path/to/your/project/.claude/commands/enhance-claude-md
```

### Option 2: User-Level (All Projects)

```bash
# Copy command to user commands directory
cp -r generated-commands/enhance-claude-md ~/.claude/commands/

# Restart Claude Code
```

## Usage

### Basic Usage (Auto-Detect)

```bash
/enhance-claude-md
```

Claude will:
1. Check if CLAUDE.md exists in your project
2. If **not found**: Run interactive initialization workflow
3. If **found**: Analyze and offer enhancement recommendations

### New Project (No CLAUDE.md)

When you run `/enhance-claude-md` on a new project:

```
Phase 1: Discovery
- Checks for existing CLAUDE.md files
- Examines project structure
- Reviews git status

Phase 2: Analysis
- Detects project type (web_app, api, fullstack, etc.)
- Identifies tech stack (TypeScript, Python, React, etc.)
- Estimates team size and development phase

Phase 3: Task
- Shows you the discoveries
- Asks for confirmation
- Creates customized CLAUDE.md file(s)
- Applies native format (project structure diagrams, setup, architecture)
```

**Example Output**:
```
Based on my exploration, here's what I discovered:

📦 Project Type: Full-Stack Application
🛠️ Tech Stack: TypeScript, React, Node.js, PostgreSQL
👥 Team Size: Small (5 developers)
🚀 Development Phase: MVP

📋 Recommended Structure:
- Root CLAUDE.md (~100 lines)
- backend/CLAUDE.md (~150 lines)
- frontend/CLAUDE.md (~175 lines)

Would you like me to create these files?
```

### Existing Project (CLAUDE.md exists)

When you run `/enhance-claude-md` on an existing project:

```
Phase 1: Discovery
- Finds existing CLAUDE.md
- Checks for modular files

Phase 2: Analysis
- Analyzes current file for quality
- Calculates quality score (0-100)
- Identifies missing sections

Phase 3: Task
- Shows quality report
- Recommends improvements
- Offers to enhance with missing sections
```

**Example Output**:
```
Current CLAUDE.md Quality Score: 65/100

Missing Sections:
- Project Structure (ASCII diagram)
- Setup & Installation
- Architecture

Issues:
- File length: 320 lines (recommend <300)
- No project structure diagram
- Missing setup instructions

Would you like me to enhance your CLAUDE.md with these sections?
```

## Command Structure

The command follows the **Multi-Phase Pattern** (similar to `codebase-analyze`):

### Phase 1: Discovery
- Checks for CLAUDE.md existence
- Examines project structure
- Reviews git status

### Phase 2: Analysis
- Determines appropriate workflow (initialize vs. enhance)
- Provides context about current state

### Phase 3: Task
- Invokes `claude-md-enhancer` skill
- Executes appropriate workflow based on analysis

## Prerequisites

**Required**:
- `claude-md-enhancer` skill must be installed
  - Project-level: `.claude/skills/claude-md-enhancer/`
  - User-level: `~/.claude/skills/claude-md-enhancer/`

**Recommended**:
- Git repository (for better context detection)
- Project files in place (package.json, requirements.txt, etc.)

## Advanced Usage

### Specify Project Type

```
/enhance-claude-md

"I need a CLAUDE.md for my Python FastAPI project with PostgreSQL"
```

### Request Modular Architecture

```
/enhance-claude-md

"Create a modular CLAUDE.md setup with separate files for backend, frontend, and database"
```

### Analyze Only

```
/enhance-claude-md

"Just analyze my current CLAUDE.md, don't make changes yet"
```

### Enhance Specific Sections

```
/enhance-claude-md

"Add Project Structure and Setup & Installation sections to my CLAUDE.md"
```

## Output

The command can invoke either the `claude-md-enhancer` skill directly OR the `claude-md-guardian` agent (recommended for maintenance).

### Option A: Direct Skill Invocation

The skill generates:

#### For New Projects

- **Root CLAUDE.md**: Navigation hub with native format sections
- **Context Files** (if modular): backend/CLAUDE.md, frontend/CLAUDE.md, etc.

**Native Format Sections Included**:
- Overview
- Project Structure (ASCII tree diagram)
- File Structure (directory explanations)
- Setup & Installation
- Architecture (for complex projects)
- Core Principles
- Tech Stack
- Development Workflow
- Testing Requirements
- Error Handling
- Common Commands

#### For Existing Projects

- **Quality Report**: Score, missing sections, issues, recommendations
- **Enhanced CLAUDE.md**: Updated with missing sections (if requested)

### Option B: Agent Invocation (Recommended for Maintenance)

The `claude-md-guardian` agent provides:

- **Auto-Sync**: Detects changes and updates CLAUDE.md automatically
- **Smart Detection**: Only updates when significant changes occur
- **Targeted Updates**: Modifies specific sections based on detected changes
- **Token-Efficient**: Uses haiku model for routine updates
- **Concise Reporting**: Reports only what changed

**Agent triggers on**:
- Feature completion
- Major refactoring
- New dependencies added
- Architecture changes
- Manual invocation via this command

**Agent output**:
```
✅ CLAUDE.md updated:
- Tech Stack: Added 2 dependencies
- Project Structure: Updated diagram
- Setup: New environment variable

Changes: 3 sections modified, 12 lines changed
```

## Validation

The command enforces the critical validation rule:

**"Always validate your output against official native examples before declaring complete."**

All generated CLAUDE.md files:
- Follow official `/update-claude-md` slash command format
- Include project structure diagrams
- Have setup & installation instructions
- Document architecture for complex projects
- Match native Claude Code format 100%

## Examples

### Example 1: New TypeScript React Project

```bash
/enhance-claude-md
```

**Claude Response**:
```
Discovered: TypeScript + React + Node.js project
Team size: Small (5 devs)
Phase: MVP

I'll create:
- CLAUDE.md (~125 lines) with full native format

Proceed?
```

### Example 2: Existing Project Missing Sections

```bash
/enhance-claude-md
```

**Claude Response**:
```
Quality Score: 55/100

Missing:
- Project Structure diagram
- Setup & Installation
- Architecture section

I can add these native format sections to improve quality to ~85/100.

Proceed?
```

### Example 3: Large Full-Stack Project

```bash
/enhance-claude-md
```

**Claude Response**:
```
Discovered: Full-stack TypeScript project
Recommend: Modular architecture

I'll create:
- Root CLAUDE.md (~100 lines)
- backend/CLAUDE.md (~200 lines)
- frontend/CLAUDE.md (~225 lines)

Proceed?
```

## Troubleshooting

### "Skill not found" error

**Solution**: Install the `claude-md-enhancer` skill first:
```bash
cp -r generated-skills/claude-md-enhancer ~/.claude/skills/
```

### Command not recognized

**Solution**: Ensure command is in correct location:
- Project: `.claude/commands/enhance-claude-md/enhance-claude-md.md`
- User: `~/.claude/commands/enhance-claude-md/enhance-claude-md.md`

Then restart Claude Code.

### No project structure detected

**Solution**: Ensure project has recognizable files:
- Node.js: `package.json`
- Python: `requirements.txt`, `pyproject.toml`
- Go: `go.mod`
- Rust: `Cargo.toml`

## Integration with claude-md-guardian Agent

This slash command can invoke the `claude-md-guardian` agent for automatic CLAUDE.md maintenance:

### How They Work Together

```
/enhance-claude-md (command)
    ↓
Discovery → Analysis → Task
    ↓
Invokes claude-md-guardian (agent)
    ↓
Agent uses claude-md-enhancer (skill)
    ↓
CLAUDE.md updated and synchronized
```

### When to Use the Agent

**Via this command**:
- After feature completion
- After major refactoring
- When new dependencies added
- After architecture changes
- For periodic synchronization

**Automatic** (with SessionStart hook):
- Beginning of each session
- Silent if no significant changes
- Updates only when needed

**See**: `generated-agents/claude-md-guardian/README.md` for complete agent documentation

## Related Resources

- **Skill Documentation**: `generated-skills/claude-md-enhancer/README.md`
- **Skill Examples**: `generated-skills/claude-md-enhancer/examples/`
- **Agent Documentation**: `generated-agents/claude-md-guardian/README.md`
- **Official Slash Command Reference**: `documentation/references/slash-command-update-claude-md-example.md`

## Version

- **Version**: 1.0.0
- **Last Updated**: November 2025
- **Compatible**: Claude Code 2.0+
- **Dependencies**: claude-md-enhancer skill v1.0.0+

---

**Quick Start**: Run `/enhance-claude-md` in any project to initialize or enhance your CLAUDE.md file with 100% native format compliance!
