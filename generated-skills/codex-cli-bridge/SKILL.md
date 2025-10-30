---
name: codex-cli-bridge
description: Bridge between Claude Code and OpenAI Codex CLI - generates AGENTS.md from CLAUDE.md, provides Codex CLI execution helpers, and enables seamless interoperability between both tools
---

# Codex CLI Bridge Skill

## Purpose

This skill creates a comprehensive bridge between **Claude Code** and **OpenAI's Codex CLI**, enabling seamless interoperability through:

1. **Documentation Translation**: Converts CLAUDE.md → AGENTS.md (reference-based, no file duplication)
2. **Execution Helpers**: Python wrappers for Codex CLI commands (always uses `codex exec`)
3. **Skill Documentation**: Makes Claude Skills accessible to Codex CLI users

## Key Capabilities

### 1. CLAUDE.md → AGENTS.md Generation
- Parses CLAUDE.md and project structure
- Scans `.claude/skills/`, `.claude/agents/`, `documentation/` folders
- Generates comprehensive AGENTS.md with file path references
- **Reference-based**: No file duplication, only links to existing files
- Documents Skills with most relevant usage method (bash scripts vs prompt references)

### 2. Safety Mechanism
- **Auto-checks Codex CLI installation** (`codex --version`)
- **Auto-runs `/init`** if CLAUDE.md missing (with user notification)
- Validates authentication and environment
- User-friendly error messages

### 3. Codex CLI Execution Helpers
- `exec_analysis()` - Read-only analysis tasks (gpt-5, read-only sandbox)
- `exec_edit()` - Code editing tasks (gpt-5-codex, workspace-write)
- `exec_with_search()` - Web search-enabled tasks
- `resume_session()` - Continue last Codex session
- **Always uses `codex exec`** (never plain `codex` - critical for Claude Code)

### 4. Skill Documentation for Codex CLI
- **Prompt-only skills**: Show how to reference in Codex prompts
- **Functional skills**: Show how to execute Python scripts directly
- **Complex skills**: Show both methods
- Includes proper `codex exec` command syntax
- Model selection guidance (gpt-5 vs gpt-5-codex)

## Input Requirements

### For AGENTS.md Generation
```json
{
  "action": "generate-agents-md",
  "project_root": "/path/to/project",
  "options": {
    "validate_codex": true,
    "auto_init": true,
    "include_mcp": true,
    "skill_detail_level": "relevant"
  }
}
```

### For Codex Execution
```json
{
  "action": "codex-exec",
  "task_type": "analysis|edit|search",
  "prompt": "Your task description",
  "model": "gpt-5|gpt-5-codex",
  "sandbox": "read-only|workspace-write|danger-full-access"
}
```

## Output Formats

### AGENTS.md Structure
```markdown
# AGENTS.md

## Project Overview
[From CLAUDE.md]

## Available Skills
### Skill Name
**Location**: `path/to/skill/`
**Using from Codex CLI**: [Most relevant method]

## Workflow Patterns
[Slash commands → Codex equivalents]

## MCP Integration
[MCP server references]

## Command Reference
| Claude Code | Codex CLI |
|-------------|-----------|
[Mappings]
```

### Execution Helper Output
```python
{
  "status": "success|error",
  "output": "Command output",
  "session_id": "uuid",
  "model_used": "gpt-5|gpt-5-codex",
  "command": "codex exec ..."
}
```

## Python Scripts

### safety_mechanism.py
- Check Codex CLI installation
- Validate CLAUDE.md exists (auto-run /init if missing)
- Environment validation
- User notifications

### claude_parser.py
- Parse CLAUDE.md sections
- Scan skills, agents, commands
- Extract quality gates and MCP configuration
- Return file paths only (no content duplication)

### project_analyzer.py
- Auto-detect project structure
- Discover all Claude Code assets
- Generate project metadata
- Build reference map

### agents_md_generator.py
- Template-based AGENTS.md generation
- File path references (no duplication)
- Skill documentation (most relevant method)
- Workflow translation (Claude → Codex)

### skill_documenter.py
- Document skills for Codex CLI users
- Determine most relevant usage method per skill type
- Generate bash examples for Python scripts
- Create Codex prompt templates

### codex_executor.py
- Python wrappers for Codex CLI commands
- Intelligent model selection (gpt-5 vs gpt-5-codex)
- Sandbox mode helpers
- Session management
- **Always uses `codex exec`**

## Usage Examples

### Example 1: Generate AGENTS.md

**User prompt**:
```
Generate AGENTS.md for this project
```

**What happens**:
1. Safety mechanism checks Codex CLI installed
2. Checks CLAUDE.md exists (auto-runs /init if missing)
3. Parses CLAUDE.md and project structure
4. Generates AGENTS.md with file references
5. Documents all skills with most relevant usage method

**Output**: Complete AGENTS.md file in project root

---

### Example 2: Execute Codex Analysis Task

**User prompt**:
```
Use Codex to analyze this codebase for security vulnerabilities
```

**What happens**:
```python
from codex_executor import CodexExecutor

executor = CodexExecutor()
result = executor.exec_analysis(
    "Analyze this codebase for security vulnerabilities",
    model="gpt-5"
)
```

**Executes**:
```bash
codex exec -m gpt-5 -s read-only \
  -c model_reasoning_effort=high \
  "Analyze this codebase for security vulnerabilities"
```

---

### Example 3: Execute Codex Code Editing

**User prompt**:
```
Use Codex to refactor main.py for better async patterns
```

**What happens**:
```python
executor = CodexExecutor()
result = executor.exec_edit(
    "Refactor main.py for better async patterns",
    model="gpt-5-codex"
)
```

**Executes**:
```bash
codex exec -m gpt-5-codex -s workspace-write \
  -c model_reasoning_effort=high \
  "Refactor main.py for better async patterns"
```

---

### Example 4: Resume Codex Session

**User prompt**:
```
Continue the previous Codex session
```

**What happens**:
```python
executor = CodexExecutor()
result = executor.resume_session()
```

**Executes**:
```bash
codex exec resume --last
```

## Best Practices

### For AGENTS.md Generation
1. **Always run on projects with CLAUDE.md** (or let auto-init create it)
2. **Validate Codex CLI installed first**
3. **Keep skills documented with most relevant method** (bash vs prompt)
4. **Use reference-based approach** (no file duplication)

### For Codex Execution
1. **Use `codex exec` always** (never plain `codex` in Claude Code)
2. **Choose correct model**:
   - `gpt-5`: General reasoning, architecture, analysis
   - `gpt-5-codex`: Code editing, specialized coding tasks
3. **Choose correct sandbox**:
   - `read-only`: Safe analysis (default)
   - `workspace-write`: File modifications
   - `danger-full-access`: Network access (rarely needed)
4. **Enable search when needed** (`--search` flag)

### For Skill Documentation
1. **Prompt-only skills**: Reference in Codex prompts
2. **Functional skills**: Execute Python scripts directly
3. **Complex skills**: Show both methods
4. **Always provide working examples**

## Command Integration

This skill integrates with existing Claude Code commands:

- **`/init`**: Auto-generates AGENTS.md after CLAUDE.md creation
- **`/update-claude`**: Regenerates AGENTS.md when CLAUDE.md changes
- **`/check-docs`**: Validates AGENTS.md exists and is in sync
- **`/sync-agents-md`**: Manual AGENTS.md regeneration
- **`/codex-exec <task>`**: Wrapper using codex_executor.py

## Installation

### Prerequisites
1. **Codex CLI installed**:
   ```bash
   codex --version  # Should show v0.48.0 or higher
   ```

2. **Codex authenticated**:
   ```bash
   codex login
   ```

3. **Claude Code v1.0+**

### Install Skill

**Option 1: Copy to project**
```bash
cp -r generated-skills/codex-cli-bridge ~/.claude/skills/
```

**Option 2: Use from this repository**
```bash
# Skill auto-discovered when Claude Code loads this project
```

## Troubleshooting

### Error: "Codex CLI not found"
**Solution**: Install Codex CLI and ensure it's in PATH
```bash
which codex  # Should return path
codex --version  # Should work
```

### Error: "CLAUDE.md not found"
**Solution**: Skill auto-runs `/init` with notification. If it fails:
```bash
# Manually run /init
/init
```

### Error: "stdout is not a terminal"
**Solution**: Always use `codex exec`, never plain `codex`
```bash
❌ codex -m gpt-5 "task"
✅ codex exec -m gpt-5 "task"
```

### AGENTS.md Out of Sync
**Solution**: Regenerate manually
```bash
/sync-agents-md
```

## References

- **Codex CLI Docs**: `openai-codex-cli-instructions.md`
- **Claude Skills Docs**: `claude-skills-instructions.md`
- **Example Skills**: `claude-skills-examples/codex-cli-skill.md`
- **AGENTS.md Spec**: https://agents.md/

## Version

**v1.0.0** - Initial release (2025-10-30)

## License

Apache 2.0

---

**Created by**: Claude Code Skills Factory
**Maintained for**: Cross-tool team collaboration (Claude Code ↔ Codex CLI)
**Sync Status**: Reference-based bridge (one-way sync: CLAUDE.md → AGENTS.md)
