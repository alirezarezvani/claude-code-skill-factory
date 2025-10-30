# /codex-exec - Execute Codex CLI Commands

**Easy wrapper for running Codex CLI commands from Claude Code with proper syntax.**

---

## Usage

```
/codex-exec [analysis|edit|search|resume] "your task"
/codex-exec --model [gpt-5|gpt-5-codex] "your task"
/codex-exec --help
```

---

## What This Command Does

**Executes Codex CLI commands with**:
- ✅ Correct syntax (always uses `codex exec`)
- ✅ Intelligent model selection
- ✅ Appropriate sandbox modes
- ✅ High reasoning effort
- ✅ Error handling

**CRITICAL**: Always uses `codex exec` not plain `codex` (required for Claude Code environment)

---

## Command Types

### Analysis (Read-Only)

Safe code analysis without modifications.

**Usage**:
```
/codex-exec analysis "analyze security vulnerabilities"
```

**Executes**:
```bash
codex exec -m gpt-5 -s read-only \
  -c model_reasoning_effort=high \
  --skip-git-repo-check \
  "analyze security vulnerabilities"
```

**Use for**:
- Code review
- Security analysis
- Architecture review
- Documentation reading
- Performance analysis

---

### Edit (Workspace Write)

Code editing and file modifications.

**Usage**:
```
/codex-exec edit "refactor main.py for async patterns"
```

**Executes**:
```bash
codex exec -m gpt-5-codex -s workspace-write \
  -c model_reasoning_effort=high \
  --full-auto \
  --skip-git-repo-check \
  "refactor main.py for async patterns"
```

**Use for**:
- Code refactoring
- Bug fixes
- Feature implementation
- Test generation
- Documentation updates

---

### Search (Web Search Enabled)

Tasks requiring latest information from the web.

**Usage**:
```
/codex-exec search "research latest Python async patterns"
```

**Executes**:
```bash
codex exec -m gpt-5 -s read-only \
  -c model_reasoning_effort=high \
  --search \
  --skip-git-repo-check \
  "research latest Python async patterns"
```

**Use for**:
- Technology research
- Best practices lookup
- Library comparisons
- Latest trends
- Documentation lookup

---

### Resume (Continue Session)

Resume previous Codex session.

**Usage**:
```
/codex-exec resume
```

**Executes**:
```bash
codex exec resume --last
```

**Use for**:
- Continuing previous work
- Adding to prior analysis
- Iterative development
- Follow-up questions

---

## Model Selection

### GPT-5 (General Reasoning)

**Default for**: Analysis, Search, General tasks

**Best for**:
- Architecture design
- Code review
- Documentation
- Planning
- Research

**Characteristics**:
- High reasoning capability
- General-purpose
- Best for non-coding tasks

---

### GPT-5-Codex (Code Specialized)

**Default for**: Edit tasks

**Best for**:
- Code refactoring
- Bug fixing
- Feature implementation
- Test generation
- Code translation

**Characteristics**:
- Optimized for coding
- Better at code editing
- Specialized knowledge

---

## Examples

### Example 1: Security Analysis

**User**:
```
/codex-exec analysis "analyze this codebase for security vulnerabilities"
```

**What happens**:
1. Uses GPT-5 (general reasoning)
2. Read-only mode (safe)
3. High reasoning effort
4. Analyzes entire codebase
5. Returns security report

**Output**:
```
🚀 Executing Codex CLI command...

Security Analysis Report:
- Found 3 SQL injection vulnerabilities
- Missing CSRF protection on 2 endpoints
- Weak password validation
- Recommendations: [detailed fixes]

✅ Analysis complete
```

---

### Example 2: Code Refactoring

**User**:
```
/codex-exec edit "refactor database.py to use connection pooling"
```

**What happens**:
1. Uses GPT-5-Codex (code specialized)
2. Workspace-write mode (can modify files)
3. Full-auto enabled
4. Refactors database.py
5. Implements connection pooling

**Output**:
```
🚀 Executing Codex CLI command...

Refactored database.py:
- Added connection pool (max_connections=20)
- Implemented context managers
- Added retry logic
- Updated all database calls
- Added tests

✅ Refactoring complete
Files modified: database.py, tests/test_database.py
```

---

### Example 3: Research Task

**User**:
```
/codex-exec search "compare FastAPI vs Flask for microservices"
```

**What happens**:
1. Uses GPT-5 with web search
2. Researches latest information
3. Compares frameworks
4. Provides recommendations

**Output**:
```
🚀 Executing Codex CLI command...

Framework Comparison: FastAPI vs Flask

FastAPI:
+ Modern async support
+ Automatic API documentation (OpenAPI)
+ Type hints and validation (Pydantic)
+ Better performance (async)
- Smaller ecosystem
- Less mature

Flask:
+ Large ecosystem
+ Mature and stable
+ Flexible and minimal
- Synchronous by default
- Manual API documentation

Recommendation: FastAPI for new microservices

✅ Research complete
```

---

### Example 4: Continue Previous Work

**User**:
```
/codex-exec resume
```

**What happens**:
1. Resumes last Codex session
2. Continues context from previous work
3. No need to repeat information

**Output**:
```
🚀 Resuming last Codex session...

Continuing from: "refactor database.py"

Ready to continue. What's next?
```

---

## Advanced Usage

### Custom Model Selection

```
/codex-exec --model gpt-5 edit "task"
```

Forces GPT-5 instead of default GPT-5-Codex for edit tasks.

---

### Show Command Only (Dry Run)

```
/codex-exec --dry-run analysis "task"
```

Shows the command that would be executed without running it.

**Output**:
```
Would execute:
codex exec -m gpt-5 -s read-only \
  -c model_reasoning_effort=high \
  --skip-git-repo-check \
  "task"
```

---

## Troubleshooting

### Error: "Codex CLI not found"

**Solution**:
```bash
# Install Codex CLI
which codex  # Check if installed
codex --version  # Verify works
```

---

### Error: "stdout is not a terminal"

**Cause**: Using plain `codex` instead of `codex exec`

**Solution**: This command automatically uses `codex exec` ✅

---

### Task Times Out

**Symptom**: Command runs for > 5 minutes and times out

**Solution**:
```
# Break into smaller tasks
/codex-exec analysis "analyze auth module only"

# Instead of
/codex-exec analysis "analyze entire codebase"
```

---

### Wrong Model Used

**Symptom**: Using GPT-5 for coding tasks (slow)

**Solution**:
```
# Use edit for coding tasks (auto-uses gpt-5-codex)
/codex-exec edit "implement feature"

# Or force model
/codex-exec --model gpt-5-codex "implement feature"
```

---

## Best Practices

### 1. Choose Right Command Type

| Task Type | Command | Why |
|-----------|---------|-----|
| Review code | `analysis` | Read-only, safe |
| Fix bug | `edit` | Can modify files |
| Research library | `search` | Web search enabled |
| Continue work | `resume` | Maintains context |

---

### 2. Be Specific

✅ **GOOD**:
```
/codex-exec analysis "check auth.py for SQL injection vulnerabilities"
```

❌ **VAGUE**:
```
/codex-exec analysis "check security"
```

---

### 3. Use Appropriate Scope

**For large codebases**:
```
# Break into modules
/codex-exec analysis "analyze auth module security"
/codex-exec analysis "analyze API module security"
```

**Not**:
```
# Too broad
/codex-exec analysis "analyze entire 100K line codebase"
```

---

### 4. Resume for Iterative Work

```
# First task
/codex-exec analysis "review authentication"

[Review results]

# Continue
/codex-exec resume
→ "Now check the authorization logic"
```

---

## Comparison: Claude Code vs Codex CLI

| Feature | Claude Code | /codex-exec (via Codex CLI) |
|---------|-------------|----------------------------|
| Model | Claude Sonnet | GPT-5 / GPT-5-Codex |
| Context | 200K tokens | Varies |
| Skills | Native support | Reference in prompts |
| Agents | Native | Not applicable |
| Reasoning | High | Configurable |
| Persistence | Session-based | Session resumable |

**Use Claude Code when**:
- Working with Claude Skills
- Using Claude Agents
- Leveraging 200K context
- Integrated workflow

**Use /codex-exec when**:
- Want GPT-5 perspective
- Testing multiple approaches
- Specific Codex features needed
- Team uses both tools

---

## Integration with Bridge Skill

Works seamlessly with codex-cli-bridge:

```
# 1. Generate AGENTS.md
/sync-agents-md

# 2. Reference in Codex command
/codex-exec analysis "Using AGENTS.md, review project structure"

# 3. Use skill documentation
/codex-exec "Using skill at path/to/SKILL.md, implement feature"
```

---

## Technical Details

**Command Type**: Slash command wrapper
**Skill Used**: codex-cli-bridge (codex_executor.py)
**Python Module**: CodexExecutor class
**Timeout**: 5 minutes (300 seconds)
**Models**: GPT-5, GPT-5-Codex
**Sandbox Modes**: read-only, workspace-write, danger-full-access

---

## Command Reference

| Command | Model | Sandbox | Use Case |
|---------|-------|---------|----------|
| `/codex-exec analysis "task"` | gpt-5 | read-only | Safe analysis |
| `/codex-exec edit "task"` | gpt-5-codex | workspace-write | Code editing |
| `/codex-exec search "task"` | gpt-5 | read-only | Web research |
| `/codex-exec resume` | Previous | Previous | Continue session |
| `/codex-exec --model gpt-5 "task"` | gpt-5 | read-only | Force model |
| `/codex-exec --dry-run "task"` | - | - | Show command |

---

## See Also

- **`/sync-agents-md`**: Regenerate AGENTS.md
- **codex-cli-bridge SKILL.md**: Complete skill documentation
- **codex_executor.py**: Python implementation
- **Codex CLI Docs**: https://github.com/openai/codex

---

**Version**: 1.0.0
**Last Updated**: 2025-10-30
**Maintained For**: Easy Codex CLI execution from Claude Code

---

**Execute Codex commands the right way!** 🚀
