# /install-skill - Install Generated Skills or Agents

**Step-by-step guide to install your generated skills and agents to the correct locations.**

---

## Usage

```
/install-skill [path-to-skill]
/install-skill [path-to-agent]
```

---

## What This Command Does

Provides step-by-step installation instructions for:
- **Claude Skills** → `~/.claude/skills/` or Claude Desktop import
- **Claude Agents** → `.claude/agents/` (project) or `~/.claude/agents/` (user-level)

Shows multiple installation methods and helps choose the best one.

---

## Install a Skill

```
/install-skill generated-skills/my-skill
```

**Output**:
```
Installing: my-skill

You have 3 installation options:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Option 1: Claude Desktop (Easiest)

1. Locate ZIP file:
   generated-skills/my-skill.zip

2. Open Claude Desktop app

3. Drag and drop the ZIP file into Claude

4. Skill will load automatically!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Option 2: Claude Code (User-level)

Available across ALL your Claude Code projects:

```bash
# Copy skill folder
cp -r generated-skills/my-skill ~/.claude/skills/

# Verify installation
ls ~/.claude/skills/my-skill/

# Restart Claude Code (if currently running)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Option 3: Claude Apps (Browser)

1. Go to Claude.ai
2. Enable Skills (Settings → Features)
3. Use the "skill-creator" skill
4. Import the ZIP file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Which option? (1, 2, or 3): ___
```

**After user chooses**, provide detailed steps for that option.

---

## Install an Agent

```
/install-skill .claude/agents/my-agent
```

(Note: Works for both skills and agents despite command name)

**Output**:
```
Installing: my-agent.md (Claude Code Agent)

You have 2 installation options:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Option 1: Project-level (This project only)

Available only in the claude-code-skills-factory project:

```bash
# File already in correct location!
.claude/agents/my-agent.md

# Restart Claude Code to load
# Agent will auto-invoke when relevant tasks detected
```

✅ Recommended if: Agent is specific to this factory project

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Option 2: User-level (All projects)

Available across ALL your Claude Code projects:

```bash
# Copy to user-level location
cp .claude/agents/my-agent.md ~/.claude/agents/

# Verify installation
ls ~/.claude/agents/my-agent.md

# Restart Claude Code
```

✅ Recommended if: Agent is useful across multiple projects

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Which option? (1 or 2): ___
```

---

## Automatic Detection

**If path contains "skills"**:
→ Provides skill installation instructions (3 options)

**If path contains "agents"**:
→ Provides agent installation instructions (2 options)

**If unclear**:
```
What type of output are you installing?

1. Claude Skill (folder with SKILL.md, goes to ~/.claude/skills/)
2. Claude Agent (single .md file, goes to .claude/agents/ or ~/.claude/agents/)

Your choice: ___
```

---

## Verification Steps

**After installation**, the command helps verify:

**For Skills**:
```bash
# Check skill installed
ls ~/.claude/skills/my-skill/

# Verify SKILL.md
head -10 ~/.claude/skills/my-skill/SKILL.md

# In Claude Desktop: Skills menu should show "my-skill"
```

**For Agents**:
```bash
# Check agent installed
ls .claude/agents/my-agent.md
# or
ls ~/.claude/agents/my-agent.md

# In Claude Code: Run /agents
# Should list "my-agent" in available agents
```

---

## Common Installation Paths

**Claude Skills**:
- User-level: `~/.claude/skills/[skill-name]/`
- Desktop: Import ZIP via drag-and-drop
- Browser: Use skill-creator

**Claude Agents**:
- Project-level: `.claude/agents/[agent-name].md`
- User-level: `~/.claude/agents/[agent-name].md`

---

## Examples

### After Building a Healthcare Skill

```
# 1. Build
/build skill
[Answer questions about healthcare data analysis]
[Skill generated: generated-skills/healthcare-analyzer/]

# 2. Validate
/validate-output skill generated-skills/healthcare-analyzer
✅ Validation passed

# 3. Install
/install-skill generated-skills/healthcare-analyzer
Choose Option 2 (Claude Code user-level)
[Follow provided commands]

# 4. Verify
ls ~/.claude/skills/healthcare-analyzer/
✅ Installed
```

### After Building a Code Reviewer Agent

```
# 1. Build
/build agent
[Answer questions about code review]
[Agent generated: .claude/agents/code-reviewer.md]

# 2. Validate
/validate-agent .claude/agents/code-reviewer
✅ Validation passed

# 3. Install
/install-skill .claude/agents/code-reviewer
Choose Option 1 (Project-level, already in place)
[Just restart Claude Code]

# 4. Verify
/agents
✅ "code-reviewer" listed
```

---

## Troubleshooting

**"Skill not loading after installation"**:
- Restart Claude Code or Claude Desktop
- Check file is in correct location
- Verify YAML frontmatter is valid (/validate-output first)

**"Agent not auto-invoking"**:
- Check /agents to see if it's listed
- Verify description is specific enough
- Try manual invocation: "Use the [agent-name] agent to..."

**"ZIP import failing"**:
- Verify ZIP file exists and isn't corrupted
- Re-create ZIP if needed:
  ```bash
  cd generated-skills
  zip -r my-skill.zip my-skill/
  ```

---

## Tips

**Before Installing**:
- ✅ Always run /validate-output first
- ✅ Fix any validation errors
- ✅ Test locally if possible

**After Installing**:
- ✅ Restart Claude Code/Desktop
- ✅ Test with simple invocation
- ✅ Share with team (if useful)

**For Skills**:
- Desktop: Easiest (drag-and-drop)
- Code: Most flexible (edit files directly)
- Browser: Good for quick sharing

**For Agents**:
- Project-level: If agent is project-specific
- User-level: If agent is useful everywhere

---

## Related Commands

- `/build` - Generate skills/prompts/agents first
- `/validate-output` - Validate before installing
- `/test-factory` - Test after installing
- `/factory-status` - See installation status

---

**Make installation easy and error-free!** 📦
