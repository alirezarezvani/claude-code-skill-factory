# How to Use: Codex CLI Bridge Skill

Complete guide to using the Codex CLI Bridge skill for seamless interoperability between Claude Code and OpenAI's Codex CLI.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Basic Usage](#basic-usage)
5. [Advanced Usage](#advanced-usage)
6. [Codex Execution Helpers](#codex-execution-helpers)
7. [Troubleshooting](#troubleshooting)
8. [Examples](#examples)

---

## Quick Start

**Generate AGENTS.md for your project in 3 steps**:

```bash
# 1. Navigate to your Claude Code project
cd /path/to/your/project

# 2. Run the bridge
python /path/to/codex-cli-bridge/bridge.py

# 3. Done! AGENTS.md created
```

---

## Prerequisites

### Required

1. **Codex CLI installed and authenticated**:
   ```bash
   codex --version  # Should show v0.48.0 or higher
   codex login      # If not authenticated
   ```

2. **Python 3.7+** with PyYAML:
   ```bash
   python3 --version
   pip3 install PyYAML
   ```

3. **Claude Code project** (or skill will auto-create minimal CLAUDE.md)

### Optional

- Claude Code CLI (for /init, /update-claude commands)
- Git (for version control)

---

## Installation

### Option 1: Use in Place (Recommended)

No installation needed - just run the bridge script:

```bash
python /path/to/codex-cli-bridge/bridge.py --project /path/to/your/project
```

### Option 2: Copy to Claude Skills Folder

```bash
# Copy entire skill to Claude skills directory
cp -r codex-cli-bridge ~/.claude/skills/

# Or to project-specific skills
cp -r codex-cli-bridge /your/project/.claude/skills/
```

### Option 3: Add to PATH

```bash
# Add bridge.py to your PATH
export PATH="$PATH:/path/to/codex-cli-bridge"

# Then use anywhere
bridge.py --project /any/project
```

---

## Basic Usage

### 1. Generate AGENTS.md

**Default (current directory)**:
```bash
python bridge.py
```

**Specific project**:
```bash
python bridge.py --project /path/to/project
```

**Output**:
- Creates `AGENTS.md` in project root
- Reference-based (links to existing files, no duplication)
- Documents all skills with Codex CLI usage examples

### 2. Validate Environment

Check if everything is ready without generating:

```bash
python bridge.py --validate
```

**Checks**:
- ✅ Codex CLI installed
- ✅ CLAUDE.md exists (or can be created)
- ✅ Python dependencies

### 3. Show Status

```bash
python bridge.py --status
```

**Shows**:
- Project root
- CLAUDE.md status
- Codex CLI version
- Authentication status

---

## Advanced Usage

### Disable Auto-Init

By default, if CLAUDE.md is missing, the skill auto-runs `/init`. To disable:

```bash
python bridge.py --no-auto-init
```

### Regenerate AGENTS.md

**After updating CLAUDE.md**:
```bash
python bridge.py  # Overwrites existing AGENTS.md
```

**Keep in sync**:
```bash
# Update CLAUDE.md
vim CLAUDE.md

# Regenerate AGENTS.md
python bridge.py
```

### Use with Different Project Types

**GREENFIELD_NEW** (default):
```bash
python bridge.py --project /new/project
```

**ENTERPRISE_REFACTOR**:
```bash
# Project type auto-detected from CLAUDE.md
python bridge.py --project /existing/enterprise/project
```

**LEGACY_MODERNIZATION**:
```bash
# Auto-detected if CLAUDE.md mentions legacy modernization
python bridge.py --project /legacy/project
```

---

## Codex Execution Helpers

The skill provides Python wrappers for Codex CLI commands.

### Execute Analysis Task

```python
from codex_executor import CodexExecutor, CodexModel

executor = CodexExecutor()

# Read-only analysis (safe)
result = executor.exec_analysis(
    prompt="Analyze this codebase for security vulnerabilities",
    model=CodexModel.GPT5
)

print(result.stdout)
```

### Execute Code Editing

```python
# Code editing with gpt-5-codex (specialized)
result = executor.exec_edit(
    prompt="Refactor main.py to use async patterns",
    model=CodexModel.GPT5_CODEX
)

if result.success:
    print("✅ Code edited successfully")
else:
    print(f"❌ Error: {result.stderr}")
```

### Resume Session

```python
# Resume last Codex session
result = executor.resume_session()
```

### Execute with Web Search

```python
# Enable web search for tasks needing latest info
result = executor.exec_with_search(
    prompt="Research latest Python async patterns and apply them"
)
```

### Generate Command String (for documentation)

```python
from codex_executor import SandboxMode, ReasoningEffort

cmd = executor.generate_command_string(
    prompt="Your task",
    model=CodexModel.GPT5,
    sandbox=SandboxMode.READ_ONLY,
    reasoning=ReasoningEffort.HIGH
)

print(cmd)
# Output:
# codex exec -m gpt-5 -s read-only \
#   -c model_reasoning_effort=high \
#   --skip-git-repo-check \
#   "Your task"
```

---

## Troubleshooting

### Error: "Codex CLI not found"

**Symptom**:
```
❌ Codex CLI not found!
```

**Solution**:
```bash
# Check if Codex is in PATH
which codex

# If not, install Codex CLI
# (See https://github.com/openai/codex)

# Verify installation
codex --version
```

---

### Error: "CLAUDE.md not found"

**Symptom**:
```
⚠️  CLAUDE.md not found
```

**Solution 1** (Auto-init enabled by default):
```bash
# Skill auto-runs /init and creates CLAUDE.md
python bridge.py  # Just run normally
```

**Solution 2** (Manual):
```bash
# Run /init manually
/init

# Then run bridge
python bridge.py
```

**Solution 3** (Minimal CLAUDE.md):
```bash
# Skill creates minimal CLAUDE.md automatically
python bridge.py  # With auto-init enabled
```

---

### Error: "ModuleNotFoundError: No module named 'yaml'"

**Symptom**:
```
ModuleNotFoundError: No module named 'yaml'
```

**Solution**:
```bash
# Install PyYAML
pip3 install PyYAML

# Or with user flag
pip3 install --user PyYAML

# Or with system packages (if needed)
pip3 install PyYAML --break-system-packages
```

---

### AGENTS.md Out of Sync

**Symptom**: CLAUDE.md was updated but AGENTS.md is stale

**Solution**:
```bash
# Regenerate AGENTS.md
python bridge.py

# Or use command integration (if installed)
/sync-agents-md
```

---

### Codex CLI "stdout is not a terminal" Error

**Symptom**:
```
Error: stdout is not a terminal
```

**Cause**: Using plain `codex` instead of `codex exec`

**Solution**:
```bash
# ❌ WRONG
codex -m gpt-5 "task"

# ✅ CORRECT
codex exec -m gpt-5 "task"
```

**Note**: This skill ALWAYS uses `codex exec` (never plain `codex`).

---

## Examples

### Example 1: New Project Setup

```bash
# 1. Create new project
mkdir my-project && cd my-project

# 2. Initialize with Claude Code (optional)
/init

# 3. Generate AGENTS.md
python /path/to/codex-cli-bridge/bridge.py

# Result:
# - CLAUDE.md created (if didn't exist)
# - AGENTS.md generated
# - Ready for both Claude Code and Codex CLI
```

---

### Example 2: Existing Project Migration

```bash
# You have a Claude Code project with:
# - CLAUDE.md
# - .claude/skills/
# - .claude/agents/

# Generate AGENTS.md for Codex CLI users
cd /your/project
python /path/to/codex-cli-bridge/bridge.py

# Result:
# - AGENTS.md created
# - All skills documented with Codex usage examples
# - Team can use Claude Code OR Codex CLI
```

---

### Example 3: Validate Before CI/CD

```bash
# In CI/CD pipeline, validate environment
python bridge.py --validate

if [ $? -eq 0 ]; then
  echo "✅ Environment valid, proceed with deployment"
else
  echo "❌ Environment validation failed"
  exit 1
fi
```

---

### Example 4: Auto-Sync Workflow

```bash
#!/bin/bash
# auto-sync.sh - Keep AGENTS.md in sync with CLAUDE.md

# Watch for CLAUDE.md changes
fswatch -o CLAUDE.md | while read; do
  echo "CLAUDE.md changed, regenerating AGENTS.md..."
  python /path/to/bridge.py
  echo "✅ AGENTS.md updated"
done
```

---

### Example 5: Cross-Tool Team Workflow

**Scenario**: Team uses both Claude Code and Codex CLI

**Setup**:
```bash
# 1. Maintain CLAUDE.md as source of truth (Claude Code users)
vim CLAUDE.md

# 2. Generate AGENTS.md for Codex CLI users
python bridge.py

# 3. Commit both files
git add CLAUDE.md AGENTS.md
git commit -m "docs: Update project configuration"
git push
```

**Result**:
- Claude Code users: Use CLAUDE.md
- Codex CLI users: Use AGENTS.md
- Both files reference same skills, agents, documentation

---

## Command Reference

| Command | Description |
|---------|-------------|
| `bridge.py` | Generate AGENTS.md for current directory |
| `bridge.py --project /path` | Generate for specific project |
| `bridge.py --validate` | Validate environment only |
| `bridge.py --no-auto-init` | Don't auto-run /init if CLAUDE.md missing |
| `bridge.py --status` | Show status report |
| `bridge.py --help` | Show help |

---

## Tips & Best Practices

### 1. Keep CLAUDE.md as Source of Truth

✅ **DO**:
- Edit CLAUDE.md
- Regenerate AGENTS.md
- Commit both files

❌ **DON'T**:
- Edit AGENTS.md directly (will be overwritten)
- Keep AGENTS.md without regenerating

### 2. Regenerate After Major Changes

**Regenerate when**:
- Added new skills
- Updated CLAUDE.md sections
- Changed project structure
- Added/removed agents

### 3. Use in CI/CD

```yaml
# .github/workflows/sync-agents-md.yml
name: Sync AGENTS.md

on:
  push:
    paths:
      - 'CLAUDE.md'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate AGENTS.md
        run: python /path/to/bridge.py
      - name: Commit if changed
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add AGENTS.md
          git commit -m "docs: Auto-sync AGENTS.md" || exit 0
          git push
```

### 4. Document Skills Well

Good SKILL.md = Good AGENTS.md section

**SKILL.md should include**:
- Clear description
- Usage examples
- Python script documentation
- Input/output formats

### 5. Test with Codex CLI

After generating, test commands:

```bash
# Test a documented command from AGENTS.md
codex exec -m gpt-5 -s read-only "Test task"

# Verify skill references work
codex exec "Using skill at path/to/SKILL.md, do task"
```

---

## Further Reading

- **SKILL.md**: Complete skill reference
- **AGENTS.md**: Example output (this repository)
- **Codex CLI Docs**: https://github.com/openai/codex
- **Claude Code Docs**: https://docs.claude.com/claude-code

---

**Version**: 1.0.0
**Last Updated**: 2025-10-30
**Maintained For**: Cross-tool team collaboration (Claude Code ↔ Codex CLI)
