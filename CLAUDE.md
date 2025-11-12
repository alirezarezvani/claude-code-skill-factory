# CLAUDE.md - Skills Factory Orchestration

This file provides top-level guidance for working with this Claude Code Skills Factory repository.

---

## Repository Purpose

This repository is a **Claude Code Skills factory** - a collection of example skills that demonstrate how to create specialized capabilities for Claude Code. Skills are folders with instructions and resources that Claude loads when relevant to the user's task.

**Key Point**: This is NOT a development project itself. It's a reference repository that users can customize and extend for their own projects. Focus on helping users understand, adapt, and create their own skills based on these examples.

---

## Modular CLAUDE.md Architecture

This repository uses **modular CLAUDE.md files** for different contexts. Claude automatically loads the appropriate file based on your working directory.

### Navigation Map

| Location | Purpose | When Claude Loads It |
|----------|---------|---------------------|
| **[.github/CLAUDE.md](.github/CLAUDE.md)** | GitHub workflows, task hierarchy, automation | Working with GitHub issues, PRs, workflows |
| **[claude-skills-examples/CLAUDE.md](claude-skills-examples/CLAUDE.md)** | Skill architecture patterns, examples | Browsing or modifying example skills |
| **[generated-skills/CLAUDE.md](generated-skills/CLAUDE.md)** | Production-ready skills catalog | Exploring or installing generated skills |
| **[documentation/CLAUDE.md](documentation/CLAUDE.md)** | Templates and references structure | Working with templates or documentation |

**How It Works**: Claude loads the most relevant CLAUDE.md based on your current task context, giving you focused guidance without information overload.

---

## Repository Structure

```
claude-code-skills-factory/
├── README.md                    # Project overview and quick start
├── CLAUDE.md                    # This file - orchestration layer
├── .github/
│   ├── CLAUDE.md               # GitHub workflows & task hierarchy
│   └── workflows/              # Automation (smart-sync, plan-auto-close, etc.)
├── claude-skills-examples/
│   ├── CLAUDE.md               # Skill patterns & architecture
│   └── *.md, *.py              # Reference skill implementations
├── documentation/
│   ├── CLAUDE.md               # Templates & references guide
│   ├── references/             # Official docs (Skills, Agents, Codex CLI)
│   └── templates/              # Factory templates (SKILLS, AGENTS, PROMPTS, SLASH_COMMANDS)
└── generated-skills/
    ├── CLAUDE.md               # Production skills catalog
    └── */                      # Production-ready skills (AWS, Prompt Factory, etc.)
```

---

## Key Principles

### 0. Critical Validation Rule ⚠️

**"Always validate your output against official native examples before declaring complete."**

When generating skills, agents, prompts, or slash commands:
1. Compare output against official Anthropic documentation
2. Check reference examples in `documentation/references/`
3. Verify all required sections/fields are present
4. Cross-check against similar generated examples
5. **Never assume completion without validation**

This prevents gaps like missing project structure diagrams, setup instructions, or other native format requirements.

### 1. Don't Overengineer
Skills should be as simple as possible while solving the problem. Avoid unnecessary complexity.

### 2. Edit Existing Files
Prefer editing existing skill files over creating new ones. This maintains consistency and reduces clutter.

### 3. Validate Inputs
Always check for missing/invalid data before calculations. Use safe operations (e.g., `safe_divide` to avoid division by zero).

### 4. Document Assumptions
Financial models and domain-specific calculations need clear assumption documentation.

### 5. Industry Context
Many calculations (ratios, valuations, metrics) require industry-specific interpretation.

---

## Quick Reference

### Factory Templates

Generate new capabilities using these templates:

| Template | Purpose | Output | Location |
|----------|---------|--------|----------|
| **Skills** | Multi-file capabilities | SKILL.md + Python files | `~/.claude/skills/` |
| **Agents** | Single-file specialists | .md with YAML frontmatter | `~/.claude/agents/` |
| **Prompts** | Meta-prompt systems | Domain-specific prompt builders | Use as template |
| **Slash Commands** | Workflow automation | .md with YAML + bash | `~/.claude/commands/` |
| **Hooks** | Event-driven automation | hook.json + README.md | `.claude/settings.json` or `~/.claude/settings.json` |

**Templates Location**: [documentation/templates/](documentation/templates/)

### Installation Locations

**Skills**:
- Project-level: `.claude/skills/[skill-name]/`
- User-level: `~/.claude/skills/[skill-name]/`

**Agents**:
- Project-level: `.claude/agents/[agent-name].md`
- User-level: `~/.claude/agents/[agent-name].md`

**Slash Commands**:
- Project-level: `generated-commands/[command-name]/`
- User-level: `~/.claude/commands/[command-name]/`

---

## Common Workflows

### Create a New Skill

1. Review examples in `claude-skills-examples/`
2. Use `documentation/templates/SKILLS_FACTORY_PROMPT.md`
3. Generate skill with SKILL.md + Python files
4. Install to `.claude/skills/` or `~/.claude/skills/`
5. Test with relevant task

### Create a New Agent

1. Review `documentation/templates/AGENTS_FACTORY_PROMPT.md`
2. Generate agent .md file with YAML frontmatter
3. Install to `.claude/agents/` or `~/.claude/agents/`
4. Test with `--agents` flag or automatic delegation

### Create a Slash Command

1. Review official examples in `documentation/references/`
2. Use `documentation/templates/MASTER_SLASH_COMMANDS_PROMPT.md`
3. Generate command with YAML + bash permissions
4. Install to `.claude/commands/` or `generated-commands/`
5. Test with `/command-name [args]`

### Create a Hook

1. Use `/build-hook` slash command or run `python3 hook_factory.py -i` for interactive mode
2. Answer 7 questions about hook purpose and behavior (event type, language, matcher, command, timeout, install level, auto-install)
3. Generated files: `generated-hooks/[hook-name]/hook.json` + README.md
4. Install automatically (if selected) or manually:
   - Automated: `python3 installer.py install generated-hooks/[hook-name] user|project`
   - Manual: Add hook.json config to `.claude/settings.json` (project) or `~/.claude/settings.json` (user)
5. Restart Claude Code to activate hook
6. Test hook with relevant events

### Work with GitHub Issues

1. Read [.github/CLAUDE.md](.github/CLAUDE.md) for workflow requirements
2. Create plan issue with `plan` label (5-10 tasks max)
3. Automation creates TASK and SUBTASK issues
4. Work on tasks in priority order
5. Close issues when complete (auto-syncs to project board)

---

## Key Files to Know

### Documentation

- **[Claude Skills Guide](documentation/references/claude-skills-instructions.md)** - Complete Anthropic documentation
- **[Claude Agents Guide](documentation/references/claude-agents-instructions.md)** - Complete Anthropic documentation
- **[Claude Hooks Guide](documentation/references/claude-hooks-instructions.md)** - Complete Anthropic hooks documentation
- **[OpenAI Codex CLI Reference](documentation/references/openai-codex-cli-instructions.md)** - Complete CLI documentation

### Templates

- **[SKILLS_FACTORY_PROMPT.md](documentation/templates/SKILLS_FACTORY_PROMPT.md)** - Generate multi-file skills
- **[AGENTS_FACTORY_PROMPT.md](documentation/templates/AGENTS_FACTORY_PROMPT.md)** - Generate single-file agents
- **[PROMPTS_FACTORY_PROMPT.md](documentation/templates/PROMPTS_FACTORY_PROMPT.md)** - Generate domain prompt builders
- **[MASTER_SLASH_COMMANDS_PROMPT.md](documentation/templates/MASTER_SLASH_COMMANDS_PROMPT.md)** - Generate slash commands

### Examples

- **[Example Skills](claude-skills-examples/)** - Financial analysis, branding, DCF models
- **[Generated Skills](generated-skills/)** - AWS architect, Prompt factory, Content researcher, etc.

---

## Getting Help

### Context-Specific Guidance

Navigate to the relevant folder and Claude will load the appropriate CLAUDE.md:

- **GitHub workflows?** → Open [.github/CLAUDE.md](.github/CLAUDE.md)
- **Skill patterns?** → Open [claude-skills-examples/CLAUDE.md](claude-skills-examples/CLAUDE.md)
- **Production skills?** → Open [generated-skills/CLAUDE.md](generated-skills/CLAUDE.md)
- **Templates?** → Open [documentation/CLAUDE.md](documentation/CLAUDE.md)

### External Resources

- **Anthropic Skills Docs**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- **Skills Marketplace**: https://github.com/anthropics/skills
- **Claude Code Docs**: https://docs.claude.com/en/docs/claude-code
- **OpenAI Codex CLI**: https://developers.openai.com/codex/cli

---

## File Organization

### What Goes Where

**Root Directory** (this level):
- README.md - Project overview
- CLAUDE.md - This orchestration file
- CHANGELOG.md - Version history
- CONTRIBUTING.md - Contribution guidelines

**NO .md files in root except the ones above** - All other documentation goes in appropriate subfolders with their own CLAUDE.md files.

### Subfolder CLAUDE.md Files

Each major folder has its own CLAUDE.md for focused guidance:

- `.github/CLAUDE.md` - 303 lines of GitHub-specific guidance
- `claude-skills-examples/CLAUDE.md` - Skill architecture and patterns
- `generated-skills/CLAUDE.md` - Production skills catalog
- `documentation/CLAUDE.md` - Templates and references

**Benefit**: You get exactly the guidance you need, when you need it, without scrolling through 665 lines.

---

**Version**: 2.0 (Modular Architecture)
**Last Updated**: October 30, 2025
**Lines**: ~155 (down from 665, 77% reduction)
