# /build-hook - Build Custom Claude Code Hooks

**Interactive guide for creating custom hooks with Q&A workflow and automatic validation.**

> **Note**: This command is also available as `/build hook` for consistency with other factories (skills, agents, prompts). Both work identically - use whichever you prefer!
>
> - **Consistent pattern**: `/build hook` (recommended)
> - **Alias**: `/build-hook` (this command)

---

## Usage

```
/build-hook
/build-hook notification
/build-hook formatting
/build-hook testing
/build-hook git
```

---

## What This Command Does

**Two Ways to Build Hooks**:

### 1. Agent-Guided (Recommended for Beginners)

**Without arguments** (`/build-hook`):
- Invokes the **hooks-guide** agent for interactive Q&A
- Asks 5-7 straightforward questions about your hook needs
- Generates complete hook configuration with validation
- Creates README.md with installation guide
- Validates safety (no destructive ops, proper error handling)
- Saves to `generated-hooks/[hook-name]/`

**With argument** (`/build-hook [type]`):
- Suggests hook template based on type
- Continues with interactive questions
- Customizes template for your needs

### 2. Direct CLI (Advanced Users)

**Interactive Mode**:
```bash
cd generated-skills/hook-factory
python3 hook_factory.py -i
```
- 7-question guided flow with smart defaults
- Comprehensive input validation
- Optional auto-install to user/project level
- Faster workflow for experienced users

**Template Mode**:
```bash
python3 hook_factory.py -t post_tool_use_format -l python
```
- Direct template generation
- Requires template knowledge
- Manual installation needed

---

## Examples

### Build Any Hook (Interactive)

```
/build-hook
```

**Output**:
```
Welcome to the Claude Code Hooks Factory! 🔧

I'll help you build a custom hook through 5-7 straightforward questions.

Hooks are workflow automation that run when events occur:
- SessionStart: Load context when Claude starts
- PostToolUse: Auto-format code after editing
- SubagentStop: Run tests when agents complete
- And 4 more event types...

Let's get started!

Question 1: What should this hook do?
Examples:
- Auto-format Python files
- Run tests automatically
- Send notifications
- Auto-commit to git

Your answer: ___
```

---

### Build Notification Hook (Suggested)

```
/build-hook notification
```

**Output**:
```
Great! Building a notification hook.

I'll ask you a few questions to customize it:

Question 1: When should notifications be sent?
1. When any agent completes (SubagentStop)
2. When specific agent completes (SubagentStop + filter)
3. After every file edit (PostToolUse)
4. At session start (SessionStart)

Your choice (1-4): ___
```

→ Continues with hooks-guide Q&A
→ Generates notification hook with macOS/Linux support

---

### Build Auto-Format Hook (Suggested)

```
/build-hook formatting
```

**Output**:
```
Perfect! Building an auto-formatting hook.

Question 1: Which language should be formatted?
1. Python (black)
2. JavaScript/TypeScript (prettier)
3. Rust (rustfmt)
4. Go (gofmt)
5. Multiple languages

Your choice (1-5): ___
```

→ Generates PostToolUse hook with formatter
→ Includes tool detection and silent failure

---

### Build Test Runner Hook (Suggested)

```
/build-hook testing
```

**Output**:
```
Excellent! Building a test runner hook.

Question 1: Which test framework?
1. pytest (Python)
2. jest (JavaScript/TypeScript)
3. cargo test (Rust)
4. go test (Go)

Your choice (1-4): ___
```

→ Generates SubagentStop hook for automatic testing
→ Configures appropriate timeout (120s)

---

### Build Git Hook (Suggested)

```
/build-hook git
```

**Output**:
```
Great! Building a git automation hook.

Question 1: What git operation?
1. Auto-stage files (git add)
2. Auto-commit with message
3. Check before push (validation)
4. Load git status at session start

Your choice (1-4): ___
```

→ Generates git workflow automation
→ Includes repository detection

---

## What Happens Next

### After Running /build-hook

**The hooks-guide agent will**:
1. Ask you 5-7 straightforward questions
2. Generate complete hook.json configuration
3. Validate for safety and correctness
4. Create README.md with installation guide
5. Save to `generated-hooks/[hook-name]/`
6. Provide installation instructions
7. Give testing guidance

**You'll get**:
- `hook.json` - Complete, validated configuration
- `README.md` - Installation, usage, troubleshooting
- Safety report - Validation results
- Installation steps - How to activate the hook

---

## Hook Event Types

**SessionStart** - Run when Claude Code starts/resumes
- Examples: Load TODO.md, show project status, check dependencies
- Timing: Once per session (<10s recommended)
- Templates: `session_start_load_context`

**PostToolUse** - Run after Write/Edit/Bash tools
- Examples: Auto-format code, auto-add to git, update imports
- Timing: Must be fast (<5s)
- Templates: `post_tool_use_format`, `post_tool_use_git_add`

**SubagentStop** - Run when agent completes task
- Examples: Run tests, quality checks, send notifications
- Timing: Can be slower (<120s)
- Templates: `subagent_stop_test_runner`, `notify_user_desktop`

**PreToolUse** - Run before tool executes
- Examples: Validate inputs, check permissions, prevent errors
- Timing: Fast (<5s), can block operation
- Templates: `pre_tool_use_validation`

**UserPromptSubmit** - Run before processing user prompt
- Examples: Add context, validate request, check safety
- Timing: Fast (<5s), can block
- Templates: `user_prompt_submit_preprocessor`

**Stop** - Run when session ends
- Examples: Cleanup, save state, generate reports
- Timing: Fast (<30s)
- Templates: `stop_session_cleanup`

**PrePush** - Run before git push
- Examples: Run tests, check commits, validate branch
- Timing: Medium (<60s), can block push
- Templates: `pre_push_validation`, `security_scan_code`

---

## Safety & Validation

**Every generated hook includes**:
- ✅ Tool detection (checks if required tools exist)
- ✅ Silent failure mode (never interrupts workflow)
- ✅ Appropriate timeouts (based on event type)
- ✅ No destructive operations
- ✅ Error handling
- ✅ Platform compatibility checks

**Validation checks**:
- JSON syntax correctness
- Required fields present
- Safety patterns (tool detection, error handling)
- No dangerous commands (rm -rf, git push --force, etc.)
- Valid glob patterns
- Appropriate event type usage

---

## Generated Files

```
generated-hooks/
└── [hook-name]/
    ├── hook.json           # Complete hook configuration (validated)
    └── README.md           # Installation guide, usage, troubleshooting
```

**hook.json example**:
```json
{
  "matcher": {
    "tool_names": ["Write", "Edit"]
  },
  "hooks": [
    {
      "type": "command",
      "command": "# Safe command with tool detection...",
      "timeout": 60
    }
  ],
  "_metadata": {
    "generated_by": "hook-factory",
    "event_type": "PostToolUse",
    "hook_name": "auto-format-python"
  }
}
```

---

## Installation

### Automated Installation (Recommended)

**Using Python Installer**:
```bash
cd generated-skills/hook-factory

# Install to user level (~/.claude/settings.json)
python3 installer.py install generated-hooks/[hook-name] user

# Install to project level (.claude/settings.json)
python3 installer.py install generated-hooks/[hook-name] project
```

**Using Bash Script** (macOS/Linux):
```bash
cd generated-skills/hook-factory

# Install to user level
./install-hook.sh generated-hooks/[hook-name] user

# Install to project level
./install-hook.sh generated-hooks/[hook-name] project
```

**Features**:
- ✅ Automatic backup with timestamp
- ✅ JSON validation before/after
- ✅ Atomic write operations
- ✅ Rollback on failure
- ✅ Keeps last 5 backups
- ✅ Duplicate detection

**Uninstall Hook**:
```bash
# Python
python3 installer.py uninstall [hook-name] user

# Bash (manual - edit settings.json)
vim ~/.claude/settings.json  # Remove hook entry
```

**List Installed Hooks**:
```bash
python3 installer.py list user
python3 installer.py list project
```

### Manual Installation (Legacy)

1. Open Claude Code settings:
   ```bash
   # Project-level
   vim .claude/settings.json

   # User-level
   vim ~/.claude/settings.json
   ```

2. Add hook configuration:
   ```json
   {
     "hooks": {
       "PostToolUse": [
         { ...paste hook config from hook.json... }
       ]
     }
   }
   ```

3. Restart Claude Code

---

## Related Commands

**After building**:
- `/validate-output hook` - Validate hook configuration
- `/test-factory [hook-name]` - Test hook works
- `/factory-status` - See all generated hooks

**For development**:
- `/build` - Build Skills, Prompts, or Agents
- `/codex-exec` - Run OpenAI Codex CLI commands

---

## Common Workflows

### Build → Validate → Install → Test

**Agent-Guided Workflow**:
```bash
# 1. Build hook
/build-hook

[Answer questions, hook generated]

# 2. Validate
/validate-output hook

# 3. Install (automated)
cd generated-skills/hook-factory
python3 installer.py install generated-hooks/[hook-name] user

# 4. Restart Claude Code

# 5. Test
# Trigger the event that activates the hook
```

**Direct CLI Workflow with Auto-Install**:
```bash
# 1. Navigate to hook factory
cd generated-skills/hook-factory

# 2. Run interactive mode
python3 hook_factory.py -i

# Answer 7 questions:
# - Q1: Event Type (1-7)
# - Q2: Language (1-6)
# - Q3: Tool Matcher
# - Q4: Command to Run
# - Q5: Timeout (1-5)
# - Q6: Installation Level (user/project)
# - Q7: Auto-Install (y/n)

# If you answered 'y' to Q7:
# ✅ Hook is automatically installed!

# 3. Restart Claude Code

# 4. Test
# Trigger the event that activates the hook
```

**Quick Template Generation**:
```bash
cd generated-skills/hook-factory

# Generate from template (no auto-install)
python3 hook_factory.py -t post_tool_use_format -l python

# Install manually
python3 installer.py install generated-hooks/[hook-name] user
```

---

## Available Templates (10 Total)

**Formatting & Code Quality**:
- `post_tool_use_format` - Auto-format code after editing (Python, JS, TS, Rust, Go)
- `post_tool_use_git_add` - Auto-stage files with git add

**Testing & Validation**:
- `subagent_stop_test_runner` - Run tests when agent completes
- `pre_tool_use_validation` - Validate before tool execution
- `pre_push_validation` - Check before git push

**Session Management**:
- `session_start_load_context` - Load context at session start
- `stop_session_cleanup` - Cleanup at session end

**User Interaction**:
- `user_prompt_submit_preprocessor` - Pre-process user prompts
- `notify_user_desktop` - Desktop notifications (macOS/Linux)

**Security**:
- `security_scan_code` - Security scanning with semgrep/bandit

**List templates**:
```bash
python3 hook_factory.py --list
```

---

## Tips

**For faster workflow**:
- Use `/build-hook [type]` to get template suggestions
- Or use `python3 hook_factory.py -i` for direct CLI with auto-install
- Be specific in your answers
- Review generated README.md for customization options

**If unsure**:
- Just use `/build-hook` and answer questions
- The agent will suggest safe defaults
- You can always regenerate or customize

**For advanced users**:
- Use direct CLI (`-i` flag) for faster iteration
- Enable auto-install (Q7) to skip manual installation
- Use `-t` flag with template name for quick generation
- Use installer.py for batch installation

**Platform-specific hooks**:
- macOS: Can use `afplay`, `osascript` for sounds/notifications
- Linux: Use `paplay`, `notify-send`
- Cross-platform: Stick to bash, git, language-specific tools

**Installer tips**:
- Always use 'user' level for global hooks (safer)
- Use 'project' level for project-specific hooks
- Installer creates automatic backups (keeps last 5)
- Use `list` command to see all installed hooks

---

## Examples of Hooks You Can Build

**Productivity**:
- Auto-format code after every edit
- Auto-stage files with git add
- Load TODO list at session start
- Display git status on startup

**Quality Assurance**:
- Run tests when agent completes
- Lint code after editing
- Security scan on code changes
- Check test coverage

**Notifications**:
- Alert when specific agent completes
- Notify on long-running tasks
- Sound on errors or completions

**DevOps**:
- Deploy to staging on push
- Run CI/CD checks locally
- Validate before git push
- Check dependencies on startup

**Custom Workflows**:
- Generate documentation on code changes
- Update changelog automatically
- Sync with external tools
- Custom logging and monitoring

---

**The easiest way to automate your Claude Code workflow!** 🔧🚀
