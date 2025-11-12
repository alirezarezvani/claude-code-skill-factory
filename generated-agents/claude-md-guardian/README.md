# claude-md-guardian Agent

Background maintenance agent that keeps CLAUDE.md files synchronized with project changes.

## Overview

The `claude-md-guardian` is a specialized Claude Code agent that monitors your project and automatically updates CLAUDE.md files when significant changes occur. It works independently in the background without interrupting development workflows.

## Key Features

- 🔄 **Auto-Sync**: Updates CLAUDE.md based on git changes
- 🎯 **Smart Detection**: Only updates when significant changes occur
- ⚡ **Token-Efficient**: Uses haiku model for routine updates
- 🔇 **Silent Operation**: No interruptions during active development
- 📦 **Milestone-Aware**: Triggers after feature completion, refactoring, etc.
- ✨ **Native Format**: Ensures 100% Claude Code format compliance

## When It's Invoked

### Automatic Triggers

**SessionStart** (beginning of each session):
- Checks git changes since last update
- Silent exit if no significant changes
- Updates only when needed

### Manual Triggers

**After Major Milestones**:
- ✅ Feature completion
- ✅ Major refactoring
- ✅ New dependencies added
- ✅ Architecture changes
- ✅ Configuration updates

**Via Commands**:
- `/enhance-claude-md` slash command
- Direct invocation: "Claude, invoke claude-md-guardian"

## Installation

### Option 1: User-Level (Recommended)

Available in all your Claude Code projects:

```bash
# Copy agent to user directory
cp generated-agents/claude-md-guardian/claude-md-guardian.md ~/.claude/agents/

# Restart Claude Code
```

### Option 2: Project-Level

Available only in current project:

```bash
# Create agents directory
mkdir -p .claude/agents

# Copy agent
cp generated-agents/claude-md-guardian/claude-md-guardian.md .claude/agents/

# Restart Claude Code
```

### Option 3: With SessionStart Hook

Automatically check for updates at session start:

```bash
# Add to .claude/settings.json or ~/.claude/settings.json
{
  "hooks": {
    "SessionStart": {
      "command": "echo 'Checking CLAUDE.md updates...'",
      "timeout": 5000,
      "description": "Trigger claude-md-guardian awareness"
    }
  }
}
```

**Note**: The hook creates awareness, but the agent only updates if significant changes detected.

## Prerequisites

**Required**:
- `claude-md-enhancer` skill must be installed
  - User-level: `~/.claude/skills/claude-md-enhancer/`
  - Project-level: `.claude/skills/claude-md-enhancer/`

**Optional** (but recommended):
- `/enhance-claude-md` slash command
- Git repository (for change detection)

## Usage Examples

### Example 1: Session Start (Auto)

```
# You start Claude Code session
# Agent checks changes automatically

Agent: ✓ CLAUDE.md current (no significant changes detected)
# Silent - continues session normally
```

### Example 2: After Feature Completion (Manual)

```
You: "Feature complete - user authentication system implemented"
You: "Claude, invoke claude-md-guardian to update CLAUDE.md"

Agent: Analyzing changes for user authentication feature...

Updates applied:
- Architecture: Added authentication flow
- API Documentation: New /auth endpoints
- Security Practices: JWT implementation notes
- Database: User table schema

✅ CLAUDE.md updated to reflect authentication system
```

### Example 3: New Dependencies Added

```
# You added react-query and tailwindcss to package.json
# Next session starts

Agent: Detected 2 new dependencies.

Updating CLAUDE.md:
- Tech Stack section (added React Query, Tailwind CSS)
- Setup & Installation (updated installation steps)

✅ CLAUDE.md updated (2 sections modified)
```

### Example 4: Via Slash Command

```bash
/enhance-claude-md

# Slash command discovers changes and invokes agent

Agent: 🔄 Analyzing project changes...

Updates applied:
- Project Structure: New components/ directory
- File Structure: Updated directory explanations
- Common Commands: Added new npm scripts

✅ CLAUDE.md synchronized (3 sections modified)
```

## What the Agent Does

### 1. Change Detection

Analyzes git history for:
- New dependencies (package.json, requirements.txt, etc.)
- New directories/file structure changes
- Configuration updates (.env.example, config files)
- Architecture pattern changes

### 2. Scope Determination

**Minor Updates** (1-2 sections):
- New dependency added
- Single directory created
- Minor configuration change

**Moderate Updates** (3-4 sections):
- Multiple dependencies
- Structure reorganization
- Feature completion

**Major Updates** (Full quality check):
- Architecture refactoring
- Multiple major changes
- First-time generation

### 3. Targeted Updates

Uses `claude-md-enhancer` skill to update only affected sections:
- **Tech Stack**: Dependency changes
- **Project Structure**: Directory changes
- **Setup & Installation**: Configuration changes
- **Architecture**: Pattern changes
- **Common Commands**: Script changes

### 4. Validation

Ensures all updates follow:
- Native Claude Code format (project structure diagrams, etc.)
- 100% format compliance
- Critical validation rule

## Token Efficiency

### Model Selection

**haiku** (default):
- Routine updates
- Dependency additions
- Minor structure changes
- Cost-effective for background tasks

**sonnet** (escalation):
- Major architecture changes
- First-time CLAUDE.md generation
- Complex modular setups

### Update Strategy

**Targeted** (default):
- Edit specific sections only
- Preserve existing content
- Minimal token usage

**Full** (when necessary):
- Complete quality check
- Comprehensive enhancement
- Only for major milestones

## Coordination with Other Agents

### Works AFTER These Agents Complete

- `rr-frontend-engineer` - Frontend features
- `rr-backend-engineer` - Backend APIs
- `rr-fullstack-engineer` - Integration work
- Any agent marking tasks "completed"

### Independent Operation

- ✅ Doesn't block other agents
- ✅ Runs in background
- ✅ No interruptions to development
- ✅ Reports when done

### Never Invoked During

- ❌ Active development by other agents
- ❌ Minor code edits (typos, comments)
- ❌ Test-only changes
- ❌ Multiple times per session (unless milestones)

## Output Formats

### Silent (No Changes)

```
✓ CLAUDE.md current (no significant changes detected)
```

### Concise (Minor Updates)

```
✅ CLAUDE.md updated:
- Tech Stack: Added 2 dependencies
- Setup: New environment variable

Changes: 2 sections, 8 lines
```

### Detailed (Major Milestone)

```
🔄 Major changes detected - Full quality check performed

Updates applied:
- Architecture: New microservices pattern documented
- Tech Stack: 5 new dependencies added
- Setup & Installation: Updated for monorepo
- Common Commands: Added 3 new scripts

Quality Score: 75 → 88 (+13)
Changes: 6 sections, 45 lines

✅ CLAUDE.md fully synchronized
```

## Configuration

### Sensitivity Adjustment

In the agent file, you can adjust when updates trigger:

```yaml
# Current thresholds (in agent logic):
- Minimum files changed: 5
- Dependency threshold: 1 new dependency
- Structure change: 1 new directory
```

### Hook Timeout

```json
{
  "hooks": {
    "SessionStart": {
      "timeout": 5000  // 5 seconds
    }
  }
}
```

## Troubleshooting

### Agent Not Triggering

**Problem**: Agent doesn't update CLAUDE.md
**Solutions**:
1. Check `claude-md-enhancer` skill is installed
2. Verify git repository exists
3. Ensure changes meet significance threshold
4. Manually invoke: "Claude, invoke claude-md-guardian"

### Too Many Updates

**Problem**: Agent updates too frequently
**Solutions**:
1. Increase significance thresholds in agent
2. Remove SessionStart hook
3. Use manual invocation only

### Skill Not Found Error

**Problem**: "claude-md-enhancer skill not found"
**Solution**:
```bash
# Install the skill
cp -r generated-skills/claude-md-enhancer ~/.claude/skills/
# Restart Claude Code
```

## Integration

### With claude-md-enhancer Skill

The agent uses this skill as its core capability:
```
Agent detects changes → Invokes skill → Skill updates sections → Agent validates
```

### With /enhance-claude-md Command

The slash command can invoke the agent:
```bash
/enhance-claude-md
# → Discovery → Analysis → Invokes claude-md-guardian → Updates
```

### With Development Workflow

```
1. Developer works on feature
2. Other agents (frontend/backend) build code
3. Feature marked complete
4. claude-md-guardian invoked
5. CLAUDE.md updated
6. Ready for next feature
```

## Best Practices

### When to Invoke Manually

- ✅ After completing major feature
- ✅ After significant refactoring
- ✅ Before creating pull request
- ✅ After adding multiple dependencies
- ✅ After architecture changes

### When to Let Auto-Trigger Handle It

- ✅ Session start checks
- ✅ Routine dependency updates
- ✅ Minor structure changes

### When NOT to Invoke

- ❌ During active development
- ❌ After minor code changes
- ❌ Multiple times without actual changes

## Version

- **Version**: 1.0.0
- **Last Updated**: November 2025
- **Compatible**: Claude Code 2.0+
- **Dependencies**: claude-md-enhancer skill v1.0.0+

## Related Resources

- **Skill**: `generated-skills/claude-md-enhancer/`
- **Slash Command**: `generated-commands/enhance-claude-md/`
- **Agent File**: `generated-agents/claude-md-guardian/claude-md-guardian.md`

---

**Quick Start**: Copy agent to `~/.claude/agents/`, restart Claude Code, and the guardian will automatically maintain your CLAUDE.md files!
