# OpenAI Codex CLI Reference

Complete command-line interface reference for OpenAI Codex CLI - the intelligent code generation and editing tool.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Global Flags](#global-flags)
4. [Command Overview](#command-overview)
5. [Command Details](#command-details)
   - [codex (interactive)](#codex-interactive)
   - [codex exec](#codex-exec)
   - [codex login](#codex-login)
   - [codex logout](#codex-logout)
   - [codex resume](#codex-resume)
   - [codex apply](#codex-apply)
   - [codex sandbox](#codex-sandbox)
   - [codex completion](#codex-completion)
   - [codex mcp](#codex-mcp)
   - [codex mcp-server](#codex-mcp-server)
   - [codex app-server](#codex-app-server)
   - [codex cloud](#codex-cloud)
6. [Flag Combinations & Safety Tips](#flag-combinations--safety-tips)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)
9. [Related Resources](#related-resources)

---

## Introduction

**OpenAI Codex CLI** is a command-line interface for the Codex code generation model. It enables developers to:

- Generate code from natural language prompts
- Edit existing code interactively
- Run automated code generation tasks in CI/CD
- Integrate with Model Context Protocol (MCP) servers
- Execute tasks in sandboxed environments
- Resume previous sessions and conversations

**Key Features**:
- **Interactive TUI**: Terminal UI for real-time collaboration
- **Non-interactive execution**: CI-friendly `codex exec` mode
- **Sandbox support**: macOS Seatbelt and Linux Landlock security
- **MCP integration**: Connect to external context servers
- **Cloud tasks**: Execute tasks on Codex Cloud
- **Session management**: Resume conversations by ID

---

## Installation

```bash
# Install Codex CLI (visit official docs for latest instructions)
# https://developers.openai.com/codex/cli

# Verify installation
codex --version

# Authenticate
codex login

# Start interactive session
codex
```

**Requirements**:
- macOS, Linux, or Windows (WSL)
- Git repository (unless using `--skip-git-repo-check`)
- OpenAI account or API key
- Optional: Ollama for local OSS models

---

## Global Flags

Global flags apply to the base `codex` command and propagate to subcommands.

### General Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--help, -h` | boolean | - | Show help for the command |
| `--version` | boolean | - | Print Codex CLI version and exit |

### Model & Provider

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--model, -m` | string | config | Override the configured model (e.g., `gpt-4`, `gpt-3.5-turbo`) |
| `--oss` | boolean | false | Use local open source provider (requires Ollama) |

### Agents & Context

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--agents` | paths | - | Load agent markdown files for the session (repeatable) |

### Security & Sandboxing

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--sandbox, -s` | enum | config | Sandbox policy: `read-only`, `workspace-write`, `danger-full-access` |
| `--add-dir` | path | - | Grant additional directories write access (repeatable) |
| `--dangerously-bypass-approvals-and-sandbox, --yolo` | boolean | false | Bypass all safety prompts (use only in isolated environments) |

### Features & Configuration

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--search` | boolean | false | Enable web browsing during the session |
| `--full-auto` | boolean | false | Apply low-friction automation preset (workspace-write + approvals on failure) |
| `--enable` | feature | - | Force-enable a feature flag (repeatable, translates to `-c features.<name>=true`) |
| `--disable` | feature | - | Force-disable a feature flag (repeatable, translates to `-c features.<name>=false`) |
| `--config, -c` | key=value | - | Override configuration values (JSON-parsed if possible, otherwise literal string) |

### Debugging

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--debug` | boolean | false | Print debug-level logs including raw API requests/responses |

---

## Command Overview

| Command | Status | Alias | Description |
|---------|--------|-------|-------------|
| `codex` | stable | - | Launch the interactive terminal UI |
| `codex exec` | stable | `codex e` | Run Codex non-interactively (CI-friendly) |
| `codex login` | stable | - | Authenticate using ChatGPT OAuth, device auth, or API key |
| `codex logout` | stable | - | Remove stored authentication credentials |
| `codex resume` | stable | - | Continue a previous interactive session by ID |
| `codex apply` | stable | `codex a` | Apply latest diff from Codex Cloud task to local tree |
| `codex sandbox` | platform-specific | - | Run commands inside Codex sandboxes (macOS/Linux) |
| `codex completion` | stable | - | Generate shell completion scripts (Bash, Zsh, Fish, PowerShell) |
| `codex mcp` | experimental | - | Manage Model Context Protocol servers |
| `codex mcp-server` | experimental | - | Run Codex as an MCP server over stdio |
| `codex app-server` | experimental | - | Launch Codex app server for local development |
| `codex cloud` | experimental | `codex cloud-tasks` | Browse or execute Codex Cloud tasks from terminal |

---

## Command Details

### codex (interactive)

Launch the interactive terminal UI (TUI) for real-time code generation.

**Usage**:
```bash
codex [PROMPT] [OPTIONS]
```

**Arguments**:
- `PROMPT` (optional): Initial instruction for the agent
- Image attachments supported via global flags

**Key Options**:
- `--search`: Enable web browsing
- `--full-auto`: Run most commands without prompts
- All global flags apply

**Examples**:
```bash
# Start interactive session
codex

# Start with initial prompt
codex "refactor this function to use async/await"

# Enable web search
codex --search "find latest React best practices"

# Full automation mode
codex --full-auto "optimize database queries"
```

---

### codex exec

Run Codex non-interactively for scripted or CI-style runs. Results stream to stdout or JSONL format.

**Usage**:
```bash
codex exec [PROMPT] [OPTIONS]
```

**Arguments**:
- `PROMPT`: Initial instruction (use `-` to pipe from stdin)

**Key Options**:

| Flag | Type | Description |
|------|------|-------------|
| `--image, -i` | path[,path...] | Attach images to first message (repeatable, comma-separated) |
| `--model, -m` | string | Override configured model |
| `--oss` | boolean | Use local OSS provider (requires Ollama) |
| `--sandbox, -s` | enum | Sandbox policy: `read-only`, `workspace-write`, `danger-full-access` |
| `--profile, -p` | string | Select configuration profile from config.toml |
| `--full-auto` | boolean | Workspace-write sandbox + approvals on failure |
| `--yolo` | boolean | Bypass approvals and sandboxing (dangerous!) |
| `--cd, -C` | path | Set workspace root before executing |
| `--skip-git-repo-check` | boolean | Allow running outside Git repository |
| `--output-schema` | path | JSON Schema file for validating final response |
| `--color` | enum | Control ANSI color: `always`, `never`, `auto` |
| `--json` | boolean | Print newline-delimited JSON events |
| `--output-last-message, -o` | path | Write assistant's final message to file |
| `-c, --config` | key=value | Inline configuration override (repeatable) |

**Examples**:
```bash
# Basic non-interactive execution
codex exec "add type hints to all functions"

# CI-friendly JSON output
codex exec --json --output-last-message result.txt "run tests and fix failures"

# Full automation for CI/CD
codex exec --full-auto "update dependencies and fix breaking changes"

# Pipe prompt from stdin
echo "optimize imports" | codex exec -

# With output schema validation
codex exec --output-schema schema.json "generate API response"
```

#### Resume Subcommand

Continue a previous `codex exec` session.

**Usage**:
```bash
codex exec resume [SESSION_ID] [PROMPT] [OPTIONS]
```

**Arguments**:
- `SESSION_ID` (optional): UUID of session to resume
- `PROMPT` (optional): Follow-up instruction after resuming

**Key Options**:
- `--last`: Resume most recent session automatically (skip picker)

**Examples**:
```bash
# Resume specific session
codex exec resume a1b2c3d4-e5f6-7890-abcd-ef1234567890

# Resume most recent session
codex exec resume --last

# Resume with follow-up prompt
codex exec resume --last "now add error handling"
```

---

### codex login

Authenticate the CLI with a ChatGPT account or API key.

**Usage**:
```bash
codex login [OPTIONS]
```

**Key Options**:
- `--with-api-key`: Read API key from stdin

**Examples**:
```bash
# Browser-based ChatGPT OAuth (default)
codex login

# API key authentication
printenv OPENAI_API_KEY | codex login --with-api-key

# Check authentication status
codex login status
```

#### Status Subcommand

Check active authentication mode and credentials.

**Usage**:
```bash
codex login status
```

**Exit Codes**:
- `0`: Logged in successfully
- Non-zero: Not authenticated

**Example**:
```bash
# Check if logged in (useful in scripts)
if codex login status; then
  echo "Authenticated"
else
  echo "Not logged in"
  exit 1
fi
```

---

### codex logout

Remove all stored authentication credentials (API key and ChatGPT).

**Usage**:
```bash
codex logout
```

**Example**:
```bash
# Remove all credentials
codex logout
```

---

### codex resume

Continue a previous interactive session by ID or resume the most recent conversation.

**Usage**:
```bash
codex resume [SESSION_ID] [PROMPT] [OPTIONS]
```

**Arguments**:
- `SESSION_ID` (optional): UUID of session to resume
- `PROMPT` (optional): Follow-up instruction after resuming

**Key Options**:
- `--last`: Resume most recent conversation automatically
- All global flags apply (model, sandbox overrides, etc.)

**Examples**:
```bash
# Resume with session picker
codex resume

# Resume specific session
codex resume a1b2c3d4-e5f6-7890-abcd-ef1234567890

# Resume most recent session
codex resume --last

# Resume with follow-up prompt
codex resume --last "add unit tests for the new code"
```

---

### codex apply

Apply the latest diff from a Codex Cloud task to your local repository.

**Usage**:
```bash
codex apply TASK_ID
```

**Arguments**:
- `TASK_ID`: Identifier of Codex Cloud task

**Requirements**:
- Authenticated with Codex Cloud
- Access to the specified task

**Behavior**:
- Prints patched files to stdout
- Exits non-zero if `git apply` fails (e.g., conflicts)

**Examples**:
```bash
# Apply task diff to local repository
codex apply task-a1b2c3d4

# Review diff before applying
codex apply task-a1b2c3d4 --dry-run
```

---

### codex sandbox

Run arbitrary commands inside Codex-provided sandboxes (macOS Seatbelt or Linux Landlock).

**Usage**:
```bash
codex sandbox [OPTIONS] -- COMMAND...
```

#### macOS Seatbelt

**Options**:

| Flag | Type | Description |
|------|------|-------------|
| `--full-auto` | boolean | Grant write access to workspace and `/tmp` |
| `--config, -c` | key=value | Configuration overrides (repeatable) |
| `COMMAND...` | var-args | Shell command to execute (after `--`) |

**Example**:
```bash
# Run command in macOS Seatbelt sandbox
codex sandbox --full-auto -- npm test
```

#### Linux Landlock

**Options**:

| Flag | Type | Description |
|------|------|-------------|
| `--full-auto` | boolean | Grant write access to workspace and `/tmp` |
| `--config, -c` | key=value | Configuration overrides (repeatable) |
| `COMMAND...` | var-args | Command to execute under Landlock + seccomp (after `--`) |

**Example**:
```bash
# Run command in Linux Landlock sandbox
codex sandbox --full-auto -- python3 script.py
```

---

### codex completion

Generate shell completion scripts for enhanced command-line experience.

**Usage**:
```bash
codex completion SHELL
```

**Arguments**:
- `SHELL`: Target shell (bash, zsh, fish, power-shell, elvish)

**Output**: Completion script printed to stdout

**Examples**:
```bash
# Generate Zsh completions
codex completion zsh > "${fpath[1]}/_codex"

# Generate Bash completions
codex completion bash > /etc/bash_completion.d/codex

# Generate Fish completions
codex completion fish > ~/.config/fish/completions/codex.fish
```

---

### codex mcp

Manage Model Context Protocol (MCP) server entries stored in `~/.codex/config.toml`.

**Subcommands**:

| Subcommand | Arguments | Description |
|------------|-----------|-------------|
| `list` | `--json` (optional) | List configured MCP servers |
| `get <name>` | `--json` (optional) | Show specific server configuration |
| `add <name>` | stdio or HTTP options | Register new MCP server |
| `remove <name>` | - | Delete stored MCP server definition |
| `login <name>` | `--scopes` (optional) | OAuth login for HTTP server |
| `logout <name>` | - | Remove OAuth credentials for HTTP server |

#### Add Subcommand Options

**stdio Transport**:

| Flag | Type | Description |
|------|------|-------------|
| `COMMAND...` | var-args | Executable + arguments (after `--`) |
| `--env KEY=VALUE` | repeatable | Environment variables for stdio server |

**Streamable HTTP Transport**:

| Flag | Type | Description |
|------|------|-------------|
| `--url` | https://… | HTTP server URL (mutually exclusive with stdio) |
| `--bearer-token-env-var` | ENV_VAR | Environment variable for bearer token |

**Examples**:
```bash
# List all MCP servers
codex mcp list

# Add stdio MCP server
codex mcp add my-server -- python3 /path/to/server.py

# Add stdio server with environment variables
codex mcp add my-server --env API_KEY=secret --env DEBUG=true -- node server.js

# Add HTTP MCP server
codex mcp add remote-server --url https://mcp.example.com

# Add HTTP server with bearer token
codex mcp add auth-server --url https://api.example.com --bearer-token-env-var MCP_TOKEN

# Get server configuration
codex mcp get my-server --json

# OAuth login for HTTP server (requires experimental_use_rmcp_client = true)
codex mcp login remote-server --scopes read,write

# Remove server
codex mcp remove my-server
```

**Notes**:
- OAuth actions require `experimental_use_rmcp_client = true`
- OAuth only works with streamable HTTP servers

---

### codex mcp-server

Run Codex as an MCP server over stdio, allowing other tools to connect.

**Usage**:
```bash
codex mcp-server [OPTIONS]
```

**Behavior**:
- Inherits global configuration overrides
- Exits when downstream client closes connection

**Example**:
```bash
# Run Codex as MCP server
codex mcp-server

# With custom configuration
codex mcp-server -c model=gpt-4
```

---

### codex app-server

Launch the Codex app server locally for development and debugging.

**Usage**:
```bash
codex app-server [OPTIONS]
```

**Note**: Primarily for development; may change without notice.

**Example**:
```bash
# Launch app server
codex app-server
```

---

### codex cloud

Interact with Codex Cloud tasks from the terminal.

**Usage**:
```bash
codex cloud [QUERY] [OPTIONS]
codex cloud exec QUERY [OPTIONS]
```

**Arguments**:
- `QUERY`: Task prompt (omit for interactive picker)

**Key Options**:

| Flag | Type | Description |
|------|------|-------------|
| `--env` | ENV_ID | Target Codex Cloud environment (required) |
| `--attempts` | 1-4 | Number of assistant attempts (best-of-N) |

**Examples**:
```bash
# Interactive task picker
codex cloud

# Submit task directly
codex cloud exec "refactor authentication module" --env prod-env

# Multiple attempts (best-of-3)
codex cloud exec "optimize query performance" --env staging-env --attempts 3
```

**Requirements**:
- Authenticated with Codex Cloud
- Valid environment identifier

**Exit Codes**:
- `0`: Task submitted successfully
- Non-zero: Task submission failed

---

## Flag Combinations & Safety Tips

### Best Practices

1. **Unattended Local Work**:
   ```bash
   # Safe automation for local development
   codex exec --full-auto "update dependencies"
   ```
   - Use `--full-auto` for unattended work
   - Avoid combining with `--yolo` unless in dedicated sandbox VM

2. **Additional Directory Access**:
   ```bash
   # Grant write access to specific directories
   codex --add-dir /data --add-dir /logs "process data files"
   ```
   - Prefer `--add-dir` over `--sandbox danger-full-access`
   - More secure than full filesystem access

3. **CI/CD Integration**:
   ```bash
   # Machine-readable output with final summary
   codex exec --json --output-last-message summary.txt "run test suite"
   ```
   - Use `--json` for machine-readable events
   - Combine with `--output-last-message` for final summary

4. **Experimental Features**:
   ```bash
   # Enable experimental MCP client
   codex --enable experimental_use_rmcp_client mcp login my-server

   # Or update config permanently
   codex -c experimental_use_rmcp_client=true
   ```
   - Use `--enable` for one-time feature activation
   - Update config.toml for persistent settings

### Safety Guidelines

| Scenario | Recommended Flags | Avoid |
|----------|-------------------|-------|
| Local development | `--full-auto` | `--yolo` (unless in VM) |
| CI/CD pipeline | `--json --output-last-message` | Interactive prompts |
| Additional directories | `--add-dir /path` | `--sandbox danger-full-access` |
| Testing changes | `--sandbox read-only` | Workspace write without review |
| Production tasks | Review each step | `--dangerously-bypass-approvals-and-sandbox` |

---

## Best Practices

### Session Management

```bash
# Name sessions for easy resumption
codex --session-name "feature-auth-refactor" "refactor authentication"

# Resume by name
codex resume --session-name "feature-auth-refactor"
```

### Configuration Profiles

```bash
# Use profiles for different environments
codex --profile production "deploy latest changes"
codex --profile staging "run integration tests"
```

### Sandbox Security

```bash
# Read-only for code review
codex --sandbox read-only "review this pull request"

# Workspace-write for development
codex --sandbox workspace-write "implement feature"

# Full access only when necessary
codex --sandbox danger-full-access "system-level modifications"
```

### Agent Management

```bash
# Load project-specific agents
codex --agents ./.codex/agents/code-reviewer.md "review recent changes"

# Multiple agents for complex tasks
codex --agents ./agents/security.md --agents ./agents/performance.md "audit codebase"
```

---

## Troubleshooting

### Common Issues

#### Authentication Failures

**Problem**: `codex login` fails or credentials not recognized

**Solutions**:
```bash
# Clear cached credentials
codex logout

# Re-authenticate with OAuth
codex login

# Use API key if OAuth fails
printenv OPENAI_API_KEY | codex login --with-api-key

# Check authentication status
codex login status
```

#### Sandbox Permissions

**Problem**: Commands fail due to sandbox restrictions

**Solutions**:
```bash
# Grant specific directory access
codex --add-dir /path/to/data "process files"

# Use workspace-write for development
codex --sandbox workspace-write "build project"

# Review sandbox policy in config
cat ~/.codex/config.toml | grep sandbox
```

#### MCP Server Connection

**Problem**: MCP server fails to connect or crashes

**Solutions**:
```bash
# List configured servers
codex mcp list

# Test server configuration
codex mcp get server-name --json

# Remove and re-add server
codex mcp remove server-name
codex mcp add server-name -- python3 server.py

# Check server logs
codex --debug "use MCP server"
```

#### Session Resume Failures

**Problem**: Cannot resume previous session

**Solutions**:
```bash
# List available sessions
codex resume

# Resume most recent
codex resume --last

# Check session directory
ls -la ~/.codex/sessions/
```

### Debug Mode

Enable detailed logging for troubleshooting:

```bash
# Show debug logs
codex --debug "your task"

# Debug with JSON output
codex exec --debug --json "your task" 2> debug.log
```

---

## Related Resources

### Official Documentation

- **Codex CLI Overview**: https://developers.openai.com/codex/cli
- **Codex Configuration**: https://developers.openai.com/codex/local-config#cli
- **AGENTS.md Specification**: https://agents.md/

### Configuration

- **Config File**: `~/.codex/config.toml`
- **Sessions Directory**: `~/.codex/sessions/`
- **MCP Servers**: Defined in config.toml `[mcp]` section

### Community

- **GitHub Issues**: Report bugs and request features
- **Discord**: Join the developer community
- **Documentation**: Browse latest guides and tutorials

---

**Version**: Based on Codex CLI 0.48.0+
**Last Updated**: October 30, 2025
**Source**: https://developers.openai.com/codex/cli-reference
**Official Documentation**: https://developers.openai.com/codex/
