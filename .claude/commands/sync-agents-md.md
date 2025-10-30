# /sync-agents-md - Regenerate AGENTS.md from CLAUDE.md

**Synchronize AGENTS.md with current CLAUDE.md using the codex-cli-bridge skill.**

---

## Usage

```
/sync-agents-md
/sync-agents-md --validate
/sync-agents-md --status
```

---

## What This Command Does

**Default** (`/sync-agents-md`):
- Runs the **codex-cli-bridge** skill
- Validates environment (Codex CLI + CLAUDE.md)
- Parses CLAUDE.md and project structure
- Regenerates AGENTS.md with latest changes
- Overwrites existing AGENTS.md

**With `--validate`**:
- Validates environment only (no regeneration)
- Checks Codex CLI installation
- Checks CLAUDE.md exists
- Shows status report

**With `--status`**:
- Shows current sync status
- Displays when AGENTS.md was last updated
- Lists documented skills and agents

---

## When to Use

**Run this command when**:
- ✅ CLAUDE.md has been updated
- ✅ New skills added to `.claude/skills/`
- ✅ New agents added to `.claude/agents/`
- ✅ Project structure changed
- ✅ AGENTS.md is out of sync
- ✅ Team needs latest Codex CLI documentation

**Don't need to run when**:
- ❌ Only code changes (no config changes)
- ❌ AGENTS.md already current
- ❌ Working only with Claude Code (not Codex CLI)

---

## How It Works

### Step 1: Environment Validation
```
🔍 Checking Codex CLI installation...
   ✅ Found: /path/to/codex
   Version: codex-cli 0.50.0

📄 Checking CLAUDE.md...
   ✅ Found: /project/CLAUDE.md

✅ All safety checks passed!
```

### Step 2: Project Analysis
```
📖 Parsing Claude Code project...
   ✅ Found 13 skills
   ✅ Found 59 agents
   ✅ Found 58 CLAUDE.md sections

📊 Project: your-project
📁 Type: GREENFIELD_NEW
```

### Step 3: AGENTS.md Generation
```
📝 Generating AGENTS.md...
   ✅ AGENTS.md generated successfully

📄 Output: /project/AGENTS.md
📊 Skills documented: 13
🤖 Agents documented: 59
```

---

## Examples

### Example 1: Basic Sync

**User**:
```
/sync-agents-md
```

**What happens**:
1. Validates Codex CLI installed
2. Checks CLAUDE.md exists
3. Parses project structure
4. Regenerates AGENTS.md
5. Success message with statistics

**Output**:
```
✅ SUCCESS - AGENTS.MD REGENERATED

📄 Output: AGENTS.md
📊 Skills documented: 13
🤖 Agents documented: 59

AGENTS.md is now in sync with CLAUDE.md
```

---

### Example 2: Validate Only

**User**:
```
/sync-agents-md --validate
```

**What happens**:
1. Checks Codex CLI installation
2. Checks CLAUDE.md exists
3. Shows status report
4. **Does NOT regenerate AGENTS.md**

**Output**:
```
✅ VALIDATION PASSED

Environment is ready for AGENTS.md generation.

Codex CLI: v0.50.0 ✅
CLAUDE.md: Found ✅
AGENTS.md: Exists (last updated: 2025-10-30)

To regenerate: /sync-agents-md
```

---

### Example 3: Status Check

**User**:
```
/sync-agents-md --status
```

**What happens**:
Shows current project status

**Output**:
```
📊 SYNC STATUS

Project: claude-code-skills-factory
CLAUDE.md: ✅ Exists
AGENTS.md: ✅ Exists (in sync)
Last updated: 2025-10-30 15:52

Skills: 13 (8 functional, 5 prompt-based)
Agents: 59
Codex CLI: v0.50.0 installed
```

---

## What Gets Updated

When you run `/sync-agents-md`, the following sections in AGENTS.md are regenerated:

### ✅ Updated Sections

1. **Project Overview**
   - From CLAUDE.md Repository Purpose section
   - Project type (GREENFIELD_NEW, etc.)
   - Description

2. **Available Skills**
   - All skills from `.claude/skills/`
   - Skills from `~/.claude/skills/`
   - Generated skills from `generated-skills/`
   - With Codex CLI usage examples

3. **Project Structure**
   - Current folder layout
   - Key files
   - Documentation references

4. **Workflow Patterns**
   - Slash commands → Codex CLI equivalents
   - Based on CLAUDE.md workflows section

5. **Command Reference**
   - Updated command mapping table
   - Claude Code ↔ Codex CLI

### ❌ What Doesn't Change

- Skill implementation files (unchanged)
- CLAUDE.md (source of truth)
- Project code
- Documentation files (just referenced)

---

## Common Workflows

### Workflow 1: After Updating CLAUDE.md

```
# 1. Edit CLAUDE.md
vim CLAUDE.md

# 2. Sync AGENTS.md
/sync-agents-md

# 3. Commit both files
git add CLAUDE.md AGENTS.md
git commit -m "docs: Update project configuration"
```

---

### Workflow 2: After Adding New Skill

```
# 1. Create skill
/build skill
[Generated: .claude/skills/my-new-skill]

# 2. Sync AGENTS.md (documents new skill)
/sync-agents-md

# 3. Verify
cat AGENTS.md | grep "my-new-skill"
```

---

### Workflow 3: Validate Before CI/CD

```
# In CI/CD pipeline

# 1. Validate environment
/sync-agents-md --validate

# 2. If valid, proceed with build
# 3. If invalid, fail pipeline
```

---

## Integration with Other Commands

This command works seamlessly with:

### `/init` - Auto-sync after initialization
```
/init
→ Creates CLAUDE.md
→ Auto-runs /sync-agents-md
→ Both files ready
```

### `/update-claude` - Auto-sync after update
```
/update-claude
→ Updates CLAUDE.md
→ Auto-runs /sync-agents-md
→ AGENTS.md stays in sync
```

### `/check-docs` - Validates sync status
```
/check-docs
→ Checks CLAUDE.md current
→ Checks AGENTS.md in sync
→ Suggests /sync-agents-md if needed
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
# Install Codex CLI
# Visit: https://github.com/openai/codex

# Verify
codex --version
```

---

### Error: "CLAUDE.md not found"

**Symptom**:
```
⚠️  CLAUDE.md not found
```

**Solution**:
```
# Option 1: Run /init to create CLAUDE.md
/init

# Option 2: Create manually
# Then run /sync-agents-md
```

---

### AGENTS.md Out of Date

**Symptom**: Changes to CLAUDE.md not reflected in AGENTS.md

**Solution**:
```
# Simply regenerate
/sync-agents-md

# AGENTS.md now updated with latest changes
```

---

### Permission Denied

**Symptom**:
```
❌ Failed to write AGENTS.md: Permission denied
```

**Solution**:
```bash
# Check permissions
ls -l AGENTS.md

# Fix if needed
chmod 644 AGENTS.md

# Try again
/sync-agents-md
```

---

## Best Practices

### 1. Keep CLAUDE.md as Source of Truth

✅ **DO**:
- Edit CLAUDE.md for all configuration changes
- Run `/sync-agents-md` after editing
- Commit both CLAUDE.md and AGENTS.md together

❌ **DON'T**:
- Edit AGENTS.md directly (will be overwritten)
- Forget to sync after CLAUDE.md changes
- Commit CLAUDE.md without regenerating AGENTS.md

---

### 2. Sync After Major Changes

**Always sync when**:
- Adding/removing skills
- Updating project description
- Changing project type
- Modifying workflows
- Adding agents

---

### 3. Validate in CI/CD

```yaml
# .github/workflows/validate-docs.yml
name: Validate Documentation

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Validate AGENTS.md sync
        run: |
          # Regenerate AGENTS.md
          python generated-skills/codex-cli-bridge/bridge.py

          # Check if changed
          git diff --exit-code AGENTS.md || {
            echo "❌ AGENTS.md is out of sync with CLAUDE.md"
            echo "Run: /sync-agents-md"
            exit 1
          }
```

---

### 4. Use in Pre-commit Hook

```bash
# .git/hooks/pre-commit
#!/bin/bash

# Check if CLAUDE.md was modified
if git diff --cached --name-only | grep -q "CLAUDE.md"; then
  echo "CLAUDE.md changed, regenerating AGENTS.md..."
  /sync-agents-md
  git add AGENTS.md
  echo "✅ AGENTS.md updated and staged"
fi
```

---

## Technical Details

**Command Type**: Slash command
**Skill Used**: codex-cli-bridge
**Python Script**: `generated-skills/codex-cli-bridge/bridge.py`
**Output**: AGENTS.md in project root
**Approach**: Reference-based (no file duplication)
**Sync Direction**: One-way (CLAUDE.md → AGENTS.md)

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/init` | Initialize project with CLAUDE.md (auto-syncs AGENTS.md) |
| `/update-claude` | Update CLAUDE.md from code changes (auto-syncs AGENTS.md) |
| `/check-docs` | Validate all documentation is current |
| `/sync-agents-md` | Manually regenerate AGENTS.md |

---

## See Also

- **SKILL.md**: codex-cli-bridge skill documentation
- **HOW_TO_USE.md**: Comprehensive usage guide
- **AGENTS.md**: Example output (this repository)
- **CLAUDE.md**: Source configuration file

---

**Version**: 1.0.0
**Last Updated**: 2025-10-30
**Maintained For**: Cross-tool team collaboration (Claude Code ↔ Codex CLI)

---

**Keep your documentation in sync!** 🔄
