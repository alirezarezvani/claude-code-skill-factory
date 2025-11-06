---
name: hook-factory
description: Generate production-ready Claude Code hooks with interactive Q&A, automated installation, and enhanced validation. Supports 10 templates across 7 event types for comprehensive workflow automation.
version: 2.0.0
author: Claude Code Skills Factory
tags: [hooks, automation, code-generation, workflow, productivity, interactive, installer]
---

# Hook Factory v2.0

**Generate production-ready Claude Code hooks with interactive Q&A, automated installation, and enhanced validation.**

## What This Skill Does

Hook Factory v2.0 is a comprehensive hook generation system with three modes:

1. **Interactive Mode** (NEW!) - 7-question guided flow with smart defaults
2. **Natural Language** - Describe what you want in plain English
3. **Template Mode** - Direct generation from 10 production templates

**Key Features:**
- **Interactive Q&A** - 7 questions with validation and smart defaults
- **Automated Installation** - Python and Bash installers with backup/rollback
- **Enhanced Validation** - Secrets detection, event-specific rules, command validation
- **10 Templates** - Covering 7 event types (PostToolUse, SubagentStop, SessionStart, PreToolUse, UserPromptSubmit, Stop, PrePush)
- **Comprehensive Safety** - Tool detection, silent failure, atomic operations
- **macOS/Linux Support** - Production-ready for Unix environments

## When to Use This Skill

Use hook-factory when you want to:

- Auto-format code after editing
- Automatically stage files with git
- Run tests when agents complete
- Load project context at session start
- Create custom workflow automation
- Learn how hooks work through examples

## Capabilities

### Three Generation Modes

**1. Interactive Mode (Recommended)**
```bash
python3 hook_factory.py -i
```
- 7-question guided flow
- Smart defaults based on event type
- Input validation and safety warnings
- Optional auto-install

**2. Natural Language Mode**
```bash
python3 hook_factory.py -r "auto-format Python files after editing"
```
- Simple keyword matching
- Quick generation for common patterns

**3. Template Mode (Advanced)**
```bash
python3 hook_factory.py -t post_tool_use_format -l python
```
- Direct template selection
- Full customization control

### Supported Hook Templates (10 Total)

**Formatting & Code Quality:**
1. **post_tool_use_format** - Auto-format after editing (Python, JS, TS, Rust, Go)
2. **post_tool_use_git_add** - Auto-stage files with git

**Testing & Validation:**
3. **subagent_stop_test_runner** - Run tests when agent completes
4. **pre_tool_use_validation** - Validate before tool execution
5. **pre_push_validation** - Check before git push

**Session Management:**
6. **session_start_load_context** - Load context at session start
7. **stop_session_cleanup** - Cleanup at session end

**User Interaction:**
8. **user_prompt_submit_preprocessor** - Pre-process user prompts
9. **notify_user_desktop** - Desktop notifications (macOS/Linux)

**Security:**
10. **security_scan_code** - Security scanning with semgrep/bandit

### Languages Supported

- Python (black formatter, pytest)
- JavaScript (prettier, jest)
- TypeScript (prettier, jest)
- Rust (rustfmt, cargo test)
- Go (gofmt, go test)

### Enhanced Validation (v2.0)

**4-Layer Validation System:**

1. **Structure Validation** - JSON syntax, required fields, types
2. **Safety Validation** - No destructive ops, tool detection, silent failure
3. **Matcher Validation** - Valid glob patterns, tool names, file paths
4. **Event-Specific Validation** - Rules per event type (PreToolUse, SessionStart, etc.)

**NEW in v2.0:**
- ✅ **Secrets Detection** - AWS keys, JWT tokens, API keys, private keys (20+ patterns)
- ✅ **Event-Specific Rules** - PreToolUse must have tool matcher, SessionStart read-only, etc.
- ✅ **Command Validation** - Bash syntax, Unix commands, path validation, dangerous operations
- ✅ **macOS/Linux Validation** - Platform-specific command checks

### Safety Features

Every generated hook includes:
- ✅ Tool detection (checks if required tools are installed)
- ✅ Silent failure mode (never interrupts your workflow)
- ✅ Appropriate timeout settings (5s-120s based on event type)
- ✅ No destructive operations
- ✅ Comprehensive validation before generation
- ✅ Clear documentation and troubleshooting guides
- ✅ Automatic backup during installation

## How to Invoke

### Natural Language Requests

Simply describe what you want the hook to do:

```
"I want to auto-format Python files after editing"
"Create a hook that runs tests when agents complete"
"Auto-add files to git after editing"
"Load my TODO.md at session start"
```

### Explicit Template Selection

If you know which template you want:

```
"Generate a hook using the post_tool_use_format template for JavaScript"
"Create a test runner hook for Rust"
```

### List Available Templates

```
"Show me all available hook templates"
"List hook templates"
```

## Example Interactions

### Example 1: Auto-Format Python

**You:** "I need a hook to auto-format my Python code after editing"

**Hook Factory:**
- Detects template: `post_tool_use_format`
- Detects language: Python
- Generates hook with black formatter
- Validates configuration
- Saves to `generated-hooks/auto-format-code-after-editing-python/`
- Creates `hook.json` and `README.md`

### Example 2: Git Auto-Add

**You:** "Automatically stage files with git when I edit them"

**Hook Factory:**
- Detects template: `post_tool_use_git_add`
- Generates git auto-add hook
- Validates git commands
- Saves to `generated-hooks/auto-add-files-to-git-after-editing/`

### Example 3: Test Runner

**You:** "Run my JavaScript tests after the agent finishes coding"

**Hook Factory:**
- Detects template: `subagent_stop_test_runner`
- Detects language: JavaScript
- Configures jest/npm test
- Saves to `generated-hooks/run-tests-when-agent-completes-javascript/`

## Output Structure

For each hook, Hook Factory creates:

```
generated-hooks/
└── [hook-name]/
    ├── hook.json        # Complete hook configuration (validated)
    └── README.md        # Installation guide, usage, troubleshooting
```

### hook.json

Valid JSON configuration ready to copy into your Claude Code settings:

```json
{
  "matcher": {
    "tool_names": ["Write", "Edit"]
  },
  "hooks": [
    {
      "type": "command",
      "command": "if ! command -v black &> /dev/null; then\n    exit 0\nfi\n\nif [[ \"$CLAUDE_TOOL_FILE_PATH\" == *.py ]]; then\n    black \"$CLAUDE_TOOL_FILE_PATH\" || exit 0\nfi",
      "timeout": 60
    }
  ]
}
```

### README.md

Comprehensive documentation including:
- Overview and how it works
- Prerequisites
- Installation instructions (manual)
- Configuration options
- Safety notes
- Troubleshooting guide
- Advanced customization tips

## Installation of Generated Hooks

### Automated Installation (NEW in v2.0!)

**Using Python Installer:**
```bash
cd generated-skills/hook-factory

# Install to user level (~/.claude/settings.json)
python3 installer.py install generated-hooks/[hook-name] user

# Install to project level (.claude/settings.json)
python3 installer.py install generated-hooks/[hook-name] project

# Uninstall
python3 installer.py uninstall [hook-name] user

# List installed hooks
python3 installer.py list user
```

**Using Bash Script (macOS/Linux):**
```bash
cd generated-skills/hook-factory

# Install
./install-hook.sh generated-hooks/[hook-name] user

# Features:
# - Automatic backup with timestamp
# - JSON validation before/after
# - Atomic write operations
# - Rollback on failure
# - Keeps last 5 backups
```

**Auto-Install from Interactive Mode:**
- Answer 'y' to Q7 (Auto-Install)
- Hook is automatically installed
- No manual steps required

### Manual Installation (Legacy)

1. **Review Generated Files**
   ```bash
   cd generated-hooks/[hook-name]
   cat README.md
   cat hook.json
   ```

2. **Manual Installation**
   - Open `.claude/settings.json` (project) or `~/.claude/settings.json` (user)
   - Copy the hook configuration from `hook.json`
   - Add to the appropriate event type array
   - Save and restart Claude Code

3. **Verify**
   - Check Claude Code logs: `~/.claude/logs/`
   - Test the hook by performing the trigger action

## Validation

Every hook is validated for:

- **JSON Syntax**: Valid, parseable JSON
- **Structure**: Required fields present and correct types
- **Safety**: No destructive operations (rm -rf, etc.)
- **Tool Detection**: External tools have detection checks
- **Silent Failure**: Commands won't interrupt workflow
- **Timeouts**: Appropriate for event type
- **Matchers**: Valid glob patterns and tool names

## Best Practices

1. **Start Simple**: Use natural language requests for common patterns
2. **Review Before Installing**: Always read the generated README.md
3. **Test in Isolation**: Try hooks in a test project first
4. **Customize Gradually**: Start with defaults, customize later
5. **Monitor Logs**: Check `~/.claude/logs/` if hooks aren't working

## Limitations

**Platform Support:**
- ✅ macOS and Linux fully supported
- ❌ Windows not supported (Unix commands, bash-specific syntax)

**Customization:**
- Interactive mode provides smart defaults but limited deep customization
- Advanced users should use template mode + manual editing
- No GUI - CLI only

**Template System:**
- 10 templates cover common patterns
- Custom templates require manual addition to templates.json
- No template composition yet (combining multiple patterns)

## Technical Details

### Files in This Skill

**Core Files:**
- `SKILL.md` - This manifest file
- `hook_factory.py` - Main orchestrator with CLI interface (687 lines)
- `generator.py` - Template substitution and hook generation
- `validator.py` - Enhanced validation engine (700+ lines)
- `templates.json` - 10 production hook templates
- `README.md` - Skill usage guide and examples

**NEW in v2.0:**
- `installer.py` - Automated installation system (536 lines)
- `install-hook.sh` - Bash installation script (148 lines)
- `examples/` - 10 reference examples (10 folders × 2 files)

### Dependencies

- Python 3.7+
- Standard library only (no external dependencies)

### Architecture (v2.0)

**Interactive Mode Flow:**
```
User: python3 hook_factory.py -i
    ↓
[7-Question Flow with Smart Defaults]
    ↓
[Template Selection]
    ↓
[Variable Substitution]
    ↓
[4-Layer Validation]
    ↓
[File Generation]
    ↓
[Optional: Auto-Install via installer.py]
    ↓
Generated Hook in generated-hooks/ + Installed
```

**Natural Language Flow:**
```
User Request
    ↓
[Keyword Matching]
    ↓
[Template Selection]
    ↓
[Variable Substitution]
    ↓
[4-Layer Validation]
    ↓
[File Generation]
    ↓
Generated Hook in generated-hooks/
```

**Installation Flow:**
```
Hook Folder
    ↓
[installer.py or install-hook.sh]
    ↓
[Backup settings.json]
    ↓
[Load + Validate JSON]
    ↓
[Merge Hook]
    ↓
[Atomic Write (temp → rename)]
    ↓
[Validate Result]
    ↓
✅ Installed (or ❌ Rollback)
```

## Troubleshooting

### "Could not determine hook type from request"
- Use more specific keywords (format, test, git add, load)
- Or use explicit template selection
- Or list templates to see what's available

### Generated hook not working
- Check Claude Code logs
- Verify required tools are installed
- Test command manually in terminal
- Review README.md troubleshooting section

### Validation errors
- Review error messages and fix suggestions
- Common issues: missing tool detection, destructive commands
- Modify template if needed

## Examples Directory

The `examples/` directory contains reference implementations:

```
examples/
├── auto-format-python/      # PostToolUse format example
├── git-auto-add/            # PostToolUse git example
├── test-runner/             # SubagentStop test example
└── load-context/            # SessionStart context example
```

Each example includes working `hook.json` and `README.md` files you can copy directly.

## Contributing

To add new hook patterns:

1. Add template to `templates.json`
2. Update keyword matching in `generator.py`
3. Add example to `examples/`
4. Update this SKILL.md

## Version History

- **1.0.0** (2025-10-30): Initial release
  - 4 core hook patterns
  - Natural language generation
  - Comprehensive validation
  - Simple keyword matching

## Support

- **Documentation**: See README.md in skill directory
- **Examples**: See examples/ directory
- **Validation Issues**: Check validator.py output
- **Claude Code Hooks**: https://docs.claude.com/en/docs/claude-code/hooks

---

**Generated by Claude Code Skills Factory**
**Last Updated:** 2025-10-30
