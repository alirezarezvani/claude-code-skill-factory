# Installation Guide - Codex CLI Bridge Skill

Complete installation instructions for the Codex CLI Bridge skill.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Methods](#installation-methods)
3. [Verification](#verification)
4. [Configuration](#configuration)
5. [Troubleshooting](#troubleshooting)
6. [Uninstallation](#uninstallation)

---

## Prerequisites

### Required

**1. Codex CLI (v0.48.0 or higher)**

```bash
# Check if installed
codex --version

# Should output: codex-cli 0.48.0 or higher
```

**Installation**: Visit https://github.com/openai/codex for Codex CLI installation instructions.

**2. Python 3.7+**

```bash
# Check version
python3 --version

# Should output: Python 3.7.0 or higher
```

**3. PyYAML Library**

```bash
# Install PyYAML
pip3 install PyYAML

# Verify
python3 -c "import yaml; print('✅ PyYAML installed')"
```

### Optional

**1. Claude Code CLI** (for slash command integration)
```bash
# Check if installed
claude --version
```

**2. Git** (for version control)
```bash
git --version
```

---

## Installation Methods

### Method 1: User-Level Installation (Recommended)

Install for your user account. Works across all projects.

```bash
# 1. Create skills directory (if doesn't exist)
mkdir -p ~/.claude/skills

# 2. Copy skill to skills directory
cp -r /path/to/codex-cli-bridge ~/.claude/skills/

# 3. Verify installation
ls ~/.claude/skills/codex-cli-bridge
```

**Location**: `~/.claude/skills/codex-cli-bridge/`

**Accessible from**: All Claude Code projects

**Use when**: You want the skill available globally

---

### Method 2: Project-Level Installation

Install for a specific project only.

```bash
# 1. Navigate to your project
cd /your/project

# 2. Create project skills directory (if doesn't exist)
mkdir -p .claude/skills

# 3. Copy skill to project
cp -r /path/to/codex-cli-bridge .claude/skills/

# 4. Verify installation
ls .claude/skills/codex-cli-bridge
```

**Location**: `/your/project/.claude/skills/codex-cli-bridge/`

**Accessible from**: This project only

**Use when**: Project-specific customization needed

---

### Method 3: Direct Use (No Installation)

Use the skill directly without copying.

```bash
# Run bridge.py directly
python3 /path/to/codex-cli-bridge/bridge.py --project /your/project
```

**Location**: Original location

**Accessible from**: Anywhere (specify full path)

**Use when**: Testing or one-time use

---

### Method 4: Add to PATH

Add bridge.py to your PATH for easy access.

```bash
# 1. Add to PATH (in ~/.bashrc or ~/.zshrc)
echo 'export PATH="$PATH:/path/to/codex-cli-bridge"' >> ~/.bashrc

# 2. Reload shell
source ~/.bashrc

# 3. Make bridge.py executable
chmod +x /path/to/codex-cli-bridge/bridge.py

# 4. Use from anywhere
bridge.py --project /any/project
```

**Location**: Original location (linked via PATH)

**Accessible from**: Anywhere via command line

**Use when**: Frequent command-line use

---

## Verification

### Step 1: Verify Prerequisites

```bash
# Check all prerequisites
codex --version          # Codex CLI
python3 --version        # Python
python3 -c "import yaml" # PyYAML
```

**Expected Output**:
```
codex-cli 0.50.0
Python 3.10.0
(no output = PyYAML installed)
```

---

### Step 2: Verify Skill Installation

```bash
# Check skill files exist
ls ~/.claude/skills/codex-cli-bridge/

# Should show:
# SKILL.md
# bridge.py
# safety_mechanism.py
# claude_parser.py
# project_analyzer.py
# agents_md_generator.py
# skill_documenter.py
# codex_executor.py
# README.md
# HOW_TO_USE.md
# ...
```

---

### Step 3: Run Validation

```bash
# Navigate to skill directory
cd ~/.claude/skills/codex-cli-bridge

# Run validation
python3 bridge.py --validate
```

**Expected Output**:
```
================================================================
CODEX CLI BRIDGE - VALIDATION ONLY
================================================================

🔍 Running safety checks...

📦 Checking Codex CLI installation...
   ✅ Codex CLI installed and working

📄 Checking CLAUDE.md...
   ✅ CLAUDE.md exists (or can be created)

✅ All safety checks passed!

================================================================
✅ VALIDATION PASSED
================================================================
```

---

### Step 4: Test Generation

```bash
# Create test directory
mkdir -p /tmp/test-bridge
cd /tmp/test-bridge

# Create minimal CLAUDE.md
echo "# CLAUDE.md\n\nTest project" > CLAUDE.md

# Run bridge
python3 ~/.claude/skills/codex-cli-bridge/bridge.py

# Check output
ls -lh AGENTS.md
```

**Expected Output**:
```
✅ SUCCESS - AGENTS.MD GENERATED

📄 Output: AGENTS.md
📊 Skills documented: 0
🤖 Agents documented: 0
```

---

## Configuration

### Default Configuration

No configuration needed. The skill works out of the box with sensible defaults:

- **Auto-init**: Enabled (creates CLAUDE.md if missing)
- **Output**: AGENTS.md in project root
- **Approach**: Reference-based (no duplication)
- **Model**: Intelligent selection (gpt-5 vs gpt-5-codex)

### Optional Configuration

#### 1. Disable Auto-Init

```bash
# Run without auto-init
python3 bridge.py --no-auto-init
```

#### 2. Custom Python Path

If using non-standard Python:

```bash
# Edit bridge.py shebang (first line)
#!/usr/bin/env python3.10
```

#### 3. Environment Variables

```bash
# Set custom Codex CLI path
export CODEX_CLI_PATH=/custom/path/to/codex

# Set custom skill path
export CODEX_BRIDGE_SKILL=/custom/path/to/codex-cli-bridge
```

---

## Slash Command Installation

### Install /sync-agents-md Command

```bash
# Copy slash command to Claude commands directory
cp /path/to/codex-cli-bridge/.claude/commands/sync-agents-md.md \
   ~/.claude/commands/
```

**Verify**:
```bash
# In Claude Code
/sync-agents-md --help
```

---

### Install /codex-exec Command

```bash
# Copy slash command
cp /path/to/codex-cli-bridge/.claude/commands/codex-exec.md \
   ~/.claude/commands/
```

**Verify**:
```bash
# In Claude Code
/codex-exec --help
```

---

## Troubleshooting Installation

### Issue 1: "ModuleNotFoundError: No module named 'yaml'"

**Problem**: PyYAML not installed

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

### Issue 2: "Permission denied" when copying

**Problem**: No write permission to target directory

**Solution**:
```bash
# Use sudo for system directories
sudo cp -r codex-cli-bridge /usr/local/lib/claude/skills/

# Or use user directory
cp -r codex-cli-bridge ~/.claude/skills/

# Or change permissions
sudo chown -R $USER ~/.claude
```

---

### Issue 3: "Command not found: bridge.py"

**Problem**: bridge.py not executable or not in PATH

**Solution**:
```bash
# Make executable
chmod +x ~/.claude/skills/codex-cli-bridge/bridge.py

# Or use python explicitly
python3 ~/.claude/skills/codex-cli-bridge/bridge.py
```

---

### Issue 4: Codex CLI not found during validation

**Problem**: Codex CLI not installed or not in PATH

**Solution**:
```bash
# Check if installed
which codex

# If not found, install Codex CLI
# Visit: https://github.com/openai/codex

# Add to PATH if needed
export PATH="$PATH:/path/to/codex/directory"
```

---

### Issue 5: Skill not auto-loaded by Claude Code

**Problem**: Skill in wrong directory or missing SKILL.md

**Solution**:
```bash
# 1. Check location
ls ~/.claude/skills/codex-cli-bridge/SKILL.md

# 2. Verify YAML frontmatter
head -5 ~/.claude/skills/codex-cli-bridge/SKILL.md

# Should show:
# ---
# name: codex-cli-bridge
# description: ...
# ---

# 3. Restart Claude Code
```

---

## Uninstallation

### Remove User-Level Installation

```bash
# Remove skill directory
rm -rf ~/.claude/skills/codex-cli-bridge

# Remove slash commands
rm ~/.claude/commands/sync-agents-md.md
rm ~/.claude/commands/codex-exec.md

# Verify removal
ls ~/.claude/skills/ | grep codex-cli-bridge
# (should output nothing)
```

---

### Remove Project-Level Installation

```bash
# Navigate to project
cd /your/project

# Remove skill
rm -rf .claude/skills/codex-cli-bridge

# Verify removal
ls .claude/skills/ | grep codex-cli-bridge
# (should output nothing)
```

---

### Remove PATH Configuration

```bash
# Edit ~/.bashrc or ~/.zshrc
# Remove line:
# export PATH="$PATH:/path/to/codex-cli-bridge"

# Reload shell
source ~/.bashrc
```

---

### Clean Up Generated Files

```bash
# Optionally remove generated AGENTS.md files
# WARNING: This removes your generated documentation!

# Find all AGENTS.md files
find . -name "AGENTS.md" -type f

# Remove if desired
find . -name "AGENTS.md" -type f -delete
```

---

## Upgrade

### From v1.0.0 to Future Versions

```bash
# 1. Backup current installation
cp -r ~/.claude/skills/codex-cli-bridge \
      ~/.claude/skills/codex-cli-bridge.backup

# 2. Remove old version
rm -rf ~/.claude/skills/codex-cli-bridge

# 3. Install new version
cp -r /path/to/new/codex-cli-bridge ~/.claude/skills/

# 4. Verify new version
python3 ~/.claude/skills/codex-cli-bridge/bridge.py --help
```

---

## Post-Installation

### Next Steps

After installation:

1. **Read Documentation**:
   ```bash
   cat ~/.claude/skills/codex-cli-bridge/README.md
   cat ~/.claude/skills/codex-cli-bridge/HOW_TO_USE.md
   ```

2. **Generate AGENTS.md for First Project**:
   ```bash
   cd /your/project
   python3 ~/.claude/skills/codex-cli-bridge/bridge.py
   ```

3. **Test Slash Commands** (if installed):
   ```bash
   # In Claude Code
   /sync-agents-md --validate
   /codex-exec --help
   ```

4. **Read Examples**:
   ```bash
   cat ~/.claude/skills/codex-cli-bridge/sample_input.json
   cat ~/.claude/skills/codex-cli-bridge/expected_output.json
   ```

---

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| OS | macOS, Linux, Windows (WSL) | macOS, Linux |
| Python | 3.7 | 3.10+ |
| Codex CLI | 0.48.0 | 0.50.0+ |
| Disk Space | 1 MB | 5 MB |
| RAM | 100 MB | 250 MB |

---

## Support

**Installation Issues**:
- Check [HOW_TO_USE.md](./HOW_TO_USE.md) troubleshooting section
- Review [README.md](./README.md) for quick start
- Verify all prerequisites met

**Bug Reports**:
- GitHub Issues: https://github.com/your-repo/issues

**Feature Requests**:
- GitHub Issues: https://github.com/your-repo/issues

---

## License

Apache 2.0 - See LICENSE file

---

**Installation complete! Ready to bridge Claude Code and Codex CLI!** 🎉
