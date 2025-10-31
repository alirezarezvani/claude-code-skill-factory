---
name: hook-factory
description: Generate production-ready Claude Code hooks from natural language requests or templates with automatic validation and safety checks
version: 1.0.0
author: Claude Code Skills Factory
tags: [hooks, automation, code-generation, workflow, productivity]
---

# Hook Factory

**Generate production-ready Claude Code hooks with automatic validation and safety checks.**

## What This Skill Does

Hook Factory is an interactive skill that helps you create Claude Code hooks from simple natural language requests. It:

- **Analyzes** your request to determine the best hook pattern
- **Generates** complete hook configuration with safety wrappers
- **Validates** the hook for correctness and safety
- **Creates** comprehensive documentation and installation guides
- **Saves** everything to `generated-hooks/` ready to use

## When to Use This Skill

Use hook-factory when you want to:

- Auto-format code after editing
- Automatically stage files with git
- Run tests when agents complete
- Load project context at session start
- Create custom workflow automation
- Learn how hooks work through examples

## Capabilities

### Supported Hook Patterns

1. **PostToolUse Auto-Format**
   - Auto-format Python, JavaScript, TypeScript, Rust, or Go files
   - Triggers immediately after editing
   - Uses language-specific formatters (black, prettier, rustfmt, gofmt)

2. **PostToolUse Git Auto-Add**
   - Automatically stage modified files with git
   - Simplifies git workflow
   - Silent failure if not a git repository

3. **SubagentStop Test Runner**
   - Run tests when agent completes work
   - Supports pytest, jest, cargo test, go test
   - Quality gate before continuing

4. **SessionStart Context Loader**
   - Load project context when session starts
   - Display TODO lists, project status, git changes
   - Fast read-only operations

### Languages Supported

- Python (black formatter, pytest)
- JavaScript (prettier, jest)
- TypeScript (prettier, jest)
- Rust (rustfmt, cargo test)
- Go (gofmt, go test)

### Safety Features

Every generated hook includes:
- ✅ Tool detection (checks if required tools are installed)
- ✅ Silent failure mode (never interrupts your workflow)
- ✅ Appropriate timeout settings
- ✅ No destructive operations
- ✅ Comprehensive validation before generation
- ✅ Clear documentation and troubleshooting guides

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

## Limitations (Simple Version)

This is the simple version of Hook Factory. Current limitations:

- Supports 4 core hook patterns (more coming)
- Simple keyword matching for natural language
- Manual installation required (no automated install script yet)
- Limited customization options during generation

Future enhancements will add:
- Interactive questioning for advanced options
- Automated installation scripts
- More hook patterns (PreToolUse, PrePush, etc.)
- Template composition (combine multiple patterns)
- Educational annotations explaining design choices

## Technical Details

### Files in This Skill

- `SKILL.md` - This manifest file
- `hook_factory.py` - Main orchestrator (CLI interface)
- `generator.py` - Template substitution and hook generation
- `validator.py` - JSON validation and safety checks
- `templates.json` - Hook pattern templates (4 core patterns)
- `README.md` - Skill usage guide and examples
- `examples/` - Reference examples for each pattern

### Dependencies

- Python 3.7+
- Standard library only (no external dependencies)

### Architecture

```
User Request
    ↓
[Keyword Matching]
    ↓
[Template Selection]
    ↓
[Variable Substitution]
    ↓
[Safety Validation]
    ↓
[File Generation]
    ↓
Generated Hook in generated-hooks/
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
