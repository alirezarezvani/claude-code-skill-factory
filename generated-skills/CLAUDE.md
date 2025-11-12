# generated-skills/CLAUDE.md

This file provides guidance for working with production-ready generated skills in this repository.

---

## Production-Ready Skills Catalog

The `generated-skills/` folder contains complete, production-ready skills created using the Skills Factory Prompt template. These skills demonstrate professional-grade implementations and can be used as-is or customized for specific needs.

---

## ⚠️ CRITICAL: Skill Generation Standards

### Critical Validation Rule

**"Always validate your output against official native examples before declaring complete."**

When generating skills in this folder:
1. Compare output against official Anthropic documentation
2. Check reference examples in `../documentation/references/`
3. Verify all required sections/fields are present (e.g., project structure diagrams for CLAUDE.md skills)
4. Cross-check against similar generated examples in this folder
5. **Never assume completion without validation**

This prevents gaps like missing native format sections, setup instructions, or other required components.

### File Inclusion Rules

When generating or modifying skills in this folder, follow these strict rules:

### What MUST BE INCLUDED in skill folders:
- ✅ `SKILL.md` - Main skill definition with YAML frontmatter
- ✅ `README.md` - Installation guide and overview
- ✅ `HOW_TO_USE.md` - Usage examples
- ✅ `*.py` - Python modules (implementation)
- ✅ `sample_input_*` - Sample data files
- ✅ `expected_output.*` - Validation data
- ✅ `config.example.*` - Configuration templates

### What MUST NEVER be included:
- ❌ Backup files (`.backup`, `.bak`, `.old`, `*~`)
- ❌ Python cache (`__pycache__/`, `*.pyc`, `*.pyo`)
- ❌ System files (`.DS_Store`, `Thumbs.db`)
- ❌ Temporary files (`*.tmp`, `*.temp`)
- ❌ Internal summaries (`*_SUMMARY.md`, `*_NOTES.md`)
- ❌ Redundant documentation (multiple installation guides)
- ❌ Development artifacts (`.pytest_cache/`, `*.log`)

### What MUST NEVER be in generated-skills/ root:
- ❌ ANY `.md` files except `CLAUDE.md`
- ❌ Summary documents (`*_SUMMARY.md`)
- ❌ Internal documentation
- ❌ Backup files
- ❌ Temporary files

### Cleanup Process (MANDATORY before completion):
1. ✅ Remove all backup files created during editing
2. ✅ Delete `__pycache__/` directories
3. ✅ Remove internal summary/notes documents
4. ✅ Verify only deliverable files remain
5. ✅ Regenerate clean ZIP package
6. ✅ Use Edit tool instead of creating backup copies

### File Creation Rules:
- ✅ Create files directly (no intermediate backups)
- ✅ Use Edit tool for modifications (automatic backup handling)
- ❌ NEVER create `.backup`, `.bak`, or `.old` files manually
- ❌ NEVER leave `__pycache__/` in deliverables
- ❌ NEVER create summary docs outside skill folders

**Why this matters**: Users receive these skills as-is. Backup files and internal docs are unprofessional and pollute the catalog. Keep deliverables clean.

---

## Available Skills

### 1. AWS Solution Architect (53 KB)

**Location**: `aws-solution-architect/`

**Files**:
- `SKILL.md` - Skill definition and documentation
- `architecture_designer.py` - Architecture design engine
- `cost_optimizer.py` - Cost optimization analyzer
- `serverless_stack.py` - Serverless stack builder

**Purpose**: Expert AWS architecture design for startups - serverless, scalable, cost-effective infrastructure

**Key Classes**:
- `ArchitectureDesigner` - Designs AWS architectures based on requirements
- `CostOptimizer` - Analyzes and optimizes AWS costs
- `ServerlessStackBuilder` - Builds serverless infrastructure templates

**Pattern**: Architecture design → IaC templates → cost optimization

**Use Cases**:
- Design scalable AWS architectures
- Generate Infrastructure as Code (IaC) templates
- Optimize AWS costs for startups
- Create serverless application stacks
- Implement best practices for AWS services

---

### 2. Content Trend Researcher (35 KB)

**Location**: `content-trend-researcher/`

**Files**:
- `SKILL.md` - Skill definition and documentation
- `trend_analyzer.py` - Multi-platform trend analysis
- `intent_analyzer.py` - User intent analysis
- `platform_insights.py` - Platform-specific insights
- `outline_generator.py` - Content outline generation

**Purpose**: Multi-platform trend analysis (Google, Reddit, YouTube, Medium, LinkedIn, X, etc.) and data-driven article outline generation

**Key Classes**:
- `TrendAnalyzer` - Analyzes trends across multiple platforms
- `IntentAnalyzer` - Analyzes user search intent
- `PlatformInsights` - Provides platform-specific insights
- `OutlineGenerator` - Generates SEO-optimized content outlines

**Pattern**: Platform trend analysis → user intent analysis → content gaps → SEO-optimized outlines

**Use Cases**:
- Research content trends across platforms
- Analyze user search intent
- Identify content gaps
- Generate SEO-optimized article outlines
- Data-driven content strategy

---

### 3. Microsoft 365 Tenant Manager (40 KB)

**Location**: `ms365-tenant-manager/`

**Files**:
- `SKILL.md` - Skill definition and documentation
- `tenant_setup.py` - Tenant configuration
- `user_management.py` - User lifecycle management
- `powershell_generator.py` - PowerShell script generation

**Purpose**: Comprehensive M365 tenant administration and PowerShell automation

**Key Classes**:
- `TenantManager` - Manages M365 tenant configuration
- `UserLifecycle` - Handles user provisioning, updates, and deprovisioning
- `PowerShellScriptGenerator` - Generates PowerShell scripts for automation

**Pattern**: Configuration requirements → PowerShell scripts → validation checklists

**Use Cases**:
- Automate M365 tenant setup
- Manage user lifecycle operations
- Generate PowerShell automation scripts
- Configure security and compliance settings
- Bulk user provisioning and management

---

### 4. Psychology Advisor (31 KB)

**Location**: `psychology-advisor/`

**Files**:
- `SKILL.md` - Skill definition and documentation
- `cbt_techniques.py` - Cognitive Behavioral Therapy techniques
- `mindfulness_tools.py` - Mindfulness and meditation exercises
- `stress_assessment.py` - Stress and anxiety assessment

**Purpose**: Evidence-based psychological advisory with CBT techniques, mindfulness exercises, and stress management

**Key Classes**:
- `CBTTechniques` - Implements CBT therapeutic techniques
- `MindfulnessTools` - Provides mindfulness and meditation exercises
- `StressAssessment` - Assesses stress levels and provides coping strategies

**Pattern**: Cognitive distortion detection → thought reframing → coping strategies → practice plans

**Use Cases**:
- Identify cognitive distortions
- Provide CBT-based interventions
- Teach mindfulness techniques
- Assess stress and anxiety levels
- Create personalized coping strategy plans

---

### 5. Agent Factory (12 KB)

**Location**: `agent-factory/`

**Files**:
- `SKILL.md` - Skill definition and documentation
- `agent_generator.py` - Agent generation engine

**Purpose**: Generate custom Claude Code agents/sub-agents with enhanced YAML frontmatter, tool patterns, and MCP integration

**Key Classes**:
- `AgentGenerator` - Generates Claude Code agent .md files

**Pattern**: Agent requirements → YAML validation → agent .md file generation

**Template**: Uses `documentation/templates/AGENTS_FACTORY_PROMPT.md` for generation

**Use Cases**:
- Create custom Claude Code agents
- Generate agent YAML frontmatter
- Configure tool access patterns
- Set up MCP integration
- Create specialized sub-agents

---

### 6. Prompt Factory (427 KB)

**Location**: `prompt-factory/`

**Files**:
- `SKILL.md` - Skill definition and documentation
- `generate_prompt.py` - Prompt generation engine
- `validator.py` - Prompt validation
- `optimizer.py` - Prompt optimization
- `batch_generator.py` - Batch prompt generation

**Purpose**: World-class prompt powerhouse generating production-ready mega-prompts for any role, industry, and task through intelligent question flow

**Key Classes**:
- `PromptGenerator` - Generates prompts through 7-question flow
- `PromptValidator` - Validates prompt quality and completeness
- `PromptOptimizer` - Optimizes prompts for specific LLMs
- `BatchPromptGenerator` - Generates multiple prompts in batch

**Pattern**: 7-question flow → preset selection (69 presets, 15 domains) → quality validation → multi-format output (XML/Claude/ChatGPT/Gemini)

**Coverage**: 69 comprehensive presets across:
- Technical (Software Engineer, DevOps, Data Scientist, etc.)
- Business (Product Manager, Business Analyst, etc.)
- Legal (Corporate Lawyer, Compliance Officer, etc.)
- Finance (Financial Analyst, Investment Banker, etc.)
- HR (HR Manager, Recruiter, etc.)
- Design (UX Designer, Product Designer, etc.)
- Customer (Customer Success Manager, Support Engineer, etc.)
- Executive (CEO, CTO, COO, etc.)
- Manufacturing (Operations Manager, Quality Engineer, etc.)
- R&D (Research Scientist, Innovation Manager, etc.)
- Regulatory (Regulatory Affairs Specialist, etc.)
- Specialized-Technical (ML Engineer, Security Architect, etc.)
- Research (Academic Researcher, Market Researcher, etc.)
- Creative-Media (Content Creator, Marketing Manager, etc.)

**Use Cases**:
- Generate prompts for any role or industry
- Create multi-format prompts (XML, Claude, ChatGPT, Gemini)
- Optimize prompts for specific LLMs
- Batch generate prompts for teams
- Build domain-specific prompt libraries

---

### 7. Slash Command Factory v2.0 (26 KB) 🆕

**Location**: `slash-command-factory/`

**Files**:
- `SKILL.md` - Skill definition and documentation
- `command_generator.py` - Slash command generation engine
- `validator.py` - Command validation
- `presets.json` - Command presets library
- `HOW_TO_USE.md` - Detailed usage guide

**Purpose**: Generate custom Claude Code slash commands through 5-7 question flow for business research, content analysis, development automation, compliance checking, and workflow optimization - following official Anthropic patterns

**Key Classes**:
- `SlashCommandGenerator` - Generates slash commands with structure detection, naming validation, bash permission generation
- `CommandValidator` - Comprehensive four-layer validation

**Pattern**: Preset selection (17 presets: 10 original + 7 official examples) OR custom generation → auto-detect structure pattern → YAML frontmatter creation → strict validation → organized output to generated-commands/

**Official Patterns Integrated**:
- **Simple Pattern** (code-review): Context → Task (straightforward workflows)
- **Multi-Phase Pattern** (codebase-analyze): Discovery → Analysis → Task (complex documentation)
- **Agent-Style Pattern** (ultrathink, openapi-sync): Role → Process → Guidelines (expert coordination)

**Validation Layers**:
- Command name (kebab-case, 2-4 words)
- Bash permissions (specific commands only, NEVER wildcard `Bash`)
- Arguments usage ($ARGUMENTS, never $1/$2/$3)
- YAML structure validation

**Coverage**:
- Business research automation
- Content research and analysis
- Medical translation systems
- Compliance audit workflows
- API building automation
- Test automation frameworks
- Documentation generation
- Knowledge extraction
- Workflow analysis
- Batch agent coordination
- Code review automation
- Codebase analysis
- OpenAPI synchronization
- Ultrathink coordination

**Output**: Commands to user's project `./generated-commands/[command-name]/` with proper folder organization (all .md in root, standards/examples/scripts/ separate)

**Bash Permissions**: Auto-generates specific patterns (git commands, discovery commands, comprehensive commands) - never uses wildcard

**Naming Convention**: Automatic kebab-case conversion with validation (verb-noun, noun-verb patterns)

**Documentation**: See [slash-command-factory/HOW_TO_USE.md](slash-command-factory/HOW_TO_USE.md) and [../documentation/templates/MASTER_SLASH_COMMANDS_PROMPT.md](../documentation/templates/MASTER_SLASH_COMMANDS_PROMPT.md)

**Use Cases**:
- Create custom slash commands for workflows
- Automate business research processes
- Build content analysis pipelines
- Generate compliance audit systems
- Create API development automation
- Build test automation frameworks
- Generate documentation workflows

---

### 8. Hook Factory v2.0 (92 KB) 🆕

**Location**: `hook-factory/`

**Files**:
- `SKILL.md` - Skill definition and documentation (v2.0.0)
- `hook_factory.py` - Interactive CLI with 7-question flow
- `generator.py` - Hook generation engine with template substitution
- `validator.py` - Enhanced validation (4 layers: structure, safety, secrets, events)
- `installer.py` - Automated installer with atomic operations (536 lines)
- `install-hook.sh` - Bash installer for macOS/Linux (148 lines)
- `templates.json` - 10 production hook templates

**Purpose**: Generate production-ready Claude Code hooks through interactive Q&A with automated installation, comprehensive validation, and 10 pre-built templates covering 7 event types

**Key Features**:
- **Interactive Mode**: 7-question guided flow with smart defaults and validation
- **10 Templates**: PostToolUse (format, git-add), SubagentStop (test-runner), SessionStart (context-loader), PreToolUse (validation), UserPromptSubmit (preprocessor), Stop (cleanup), PrePush (validation), Notification (desktop-notify, security-scan)
- **Automated Installation**: Python and Bash installers with atomic operations, backup/rollback
- **Enhanced Validation**: 4-layer validation (structure, safety, secrets detection, event-specific rules)
- **Template Variables**: Language-specific substitution (Python/JavaScript/TypeScript/Rust/Go)

**Pattern**: Interactive Q&A → Template selection → Validation → Auto-install (optional)

**Templates (10 Total)**:
1. `post_tool_use_format` - Auto-format code after editing (black, prettier, rustfmt, gofmt)
2. `post_tool_use_git_add` - Auto-stage files after editing
3. `subagent_stop_test_runner` - Run tests when agent completes
4. `session_start_context_loader` - Load context on session start
5. `pre_tool_use_validation` - Validate inputs before tool execution
6. `user_prompt_submit_preprocessor` - Pre-process user prompts
7. `stop_session_cleanup` - Cleanup on session end
8. `pre_push_validation` - Validate before git push
9. `notify_user_desktop` - Desktop notifications (macOS/Linux)
10. `security_scan_code` - Security scanning (semgrep, bandit)

**Validation Features**:
- Secrets detection (AWS keys, RSA, JWT, env vars)
- Event-specific rules (timing, matchers, blocking requirements)
- Destructive command detection (rm -rf, chmod 777, sudo rm, etc.)
- Tool detection patterns (ensure external tools exist before running)

**Installer Features**:
- Atomic operations (temp file → rename pattern)
- Automatic backups with timestamps
- Rollback on failure
- List/install/uninstall commands
- Both user (~/.claude/) and project (.claude/) levels

**Use Cases**:
- Automate code formatting after edits
- Auto-stage files for git commits
- Run tests when agents complete work
- Load project context on session start
- Validate inputs before dangerous operations
- Pre-process user prompts for better results
- Cleanup temporary files on exit
- Run security scans before git push
- Desktop notifications for long-running operations

**Documentation**: See [hook-factory/README.md](hook-factory/README.md) and [hook-factory/SKILL.md](hook-factory/SKILL.md)

---

### 9. CLAUDE.md Enhancer (50 KB) 🆕

**Location**: `claude-md-enhancer/`

**Files**:
- `SKILL.md` - Skill definition and documentation
- `workflow.py` - Interactive initialization workflow (329 lines)
- `analyzer.py` - File analysis and quality scoring
- `validator.py` - Best practices validation
- `generator.py` - Content generation engine
- `template_selector.py` - Template selection logic
- `README.md` - Installation guide and overview
- `HOW_TO_USE.md` - Comprehensive usage examples
- `sample_input.json` - Example inputs (7 scenarios)
- `expected_output.json` - Expected outputs
- `examples/` - 7 built-in reference CLAUDE.md files

**Purpose**: Analyze, generate, and enhance CLAUDE.md files for any project type with intelligent templates, best practices validation, and interactive initialization workflow

**Key Classes**:
- `InitializationWorkflow` - 7-step interactive workflow with repository exploration and user confirmation
- `CLAUDEMDAnalyzer` - Quality scoring (0-100) and section analysis
- `BestPracticesValidator` - 5-layer validation (length, structure, formatting, completeness, anti-patterns)
- `ContentGenerator` - Generates root files and context-specific files (backend/, frontend/, database/)
- `TemplateSelector` - Matrix-based template selection (project type × team size × phase)

**Pattern**: Repository exploration → context detection (project type, tech stack, team size, phase, workflows) → user confirmation → CLAUDE.md generation → enhancement → validation

**Interactive Initialization** (🆕 New Feature):
1. Check if CLAUDE.md exists
2. Explore repository (built-in Claude Code command)
3. Detect project context automatically:
   - Project types: web_app, api, fullstack, cli, library, mobile, desktop
   - Tech stacks: TypeScript, Python, React, FastAPI, PostgreSQL, Docker, etc.
   - Team sizes: solo, small (<10), medium (10-50), large (50+)
   - Development phases: prototype, mvp, production, enterprise
   - Workflows: TDD, CI/CD, documentation-first, agile
4. Show discoveries to user for confirmation
5. Create customized CLAUDE.md file(s) after approval
6. Enhance with best practices
7. Provide summary of created files

**Quality Scoring** (0-100):
- Length appropriateness: 25 points
- Section completeness: 25 points
- Formatting quality: 20 points
- Content specificity: 15 points
- Modular organization: 15 points

**Template Matrix**:
| Project Type | Team Size | Target Lines | Complexity |
|--------------|-----------|--------------|------------|
| Web App | Solo | 75 | Minimal |
| API | Small (<10) | 125 | Core |
| Full-Stack | Medium (10-50) | 200 | Detailed |
| Library | Large (50+) | 275 | Comprehensive |

**Modular Architecture Support**:
- Root CLAUDE.md (navigation hub, <150 lines)
- backend/CLAUDE.md (API and database guidelines)
- frontend/CLAUDE.md (component standards, state management)
- database/CLAUDE.md (schema, migrations, queries)
- .github/CLAUDE.md (CI/CD workflows)

**Built-in Examples** (7 Reference Files):
1. `minimal-solo-CLAUDE.md` (~50 lines) - Solo developer prototypes
2. `core-small-team-CLAUDE.md` (~125 lines) - Small team MVPs
3. `modular-root-CLAUDE.md` (~100 lines) - Full-stack root navigation
4. `modular-backend-CLAUDE.md` (~150 lines) - Backend-specific guidelines
5. `modular-frontend-CLAUDE.md` (~175 lines) - Frontend-specific guidelines
6. `python-api-CLAUDE.md` (~150 lines) - Python FastAPI projects
7. `examples/README.md` - Examples catalog and selection guide

**Use Cases**:
- Interactive initialization for new projects (conversational workflow)
- Analyze existing CLAUDE.md files for quality (score 0-100)
- Generate customized CLAUDE.md from scratch (tech stack-specific)
- Enhance existing files with missing sections
- Validate before commits (5-layer validation)
- Create modular architecture for complex projects
- Adapt to team size changes (solo → small → medium → large)
- Tech stack migration support (update guidelines)

**Documentation**: See [claude-md-enhancer/README.md](claude-md-enhancer/README.md) and [claude-md-enhancer/HOW_TO_USE.md](claude-md-enhancer/HOW_TO_USE.md)

---

## Installation

### General Installation Process

1. **Choose a skill** from the catalog above
2. **Copy the entire folder** to installation location:
   - **Claude Code Project**: `.claude/skills/[skill-name]/`
   - **Claude Code Personal**: `~/.claude/skills/[skill-name]/`
3. **Restart Claude Code** or reload skills
4. **Invoke the skill** when relevant to your task

### Example

```bash
# Install AWS Solution Architect skill (personal)
cp -r generated-skills/aws-solution-architect ~/.claude/skills/

# Install Prompt Factory skill (project)
cp -r generated-skills/prompt-factory .claude/skills/

# Restart Claude Code
# Skill will be automatically loaded when relevant
```

---

## Customization

All skills can be customized for specific needs:

1. **Edit SKILL.md**: Modify skill description, capabilities, or instructions
2. **Update Python files**: Change implementation logic or add new features
3. **Add resources**: Include sample data, templates, or additional files
4. **Test locally**: Verify changes before deployment

**Best Practice**: Create a copy before customizing to preserve the original.

---

## Skill Size Reference

| Skill | Size | Complexity |
|-------|------|------------|
| Agent Factory | 12 KB | Simple |
| Slash Command Factory v2.0 | 26 KB | Medium |
| Psychology Advisor | 31 KB | Medium |
| Content Trend Researcher | 35 KB | Medium |
| Microsoft 365 Tenant Manager | 40 KB | Medium |
| CLAUDE.md Enhancer | 50 KB | Medium |
| AWS Solution Architect | 53 KB | High |
| Hook Factory v2.0 | 92 KB | High |
| Prompt Factory | 427 KB | Very High |

---

## Related Resources

- **Main README**: [../README.md](../README.md) - Project overview
- **Root CLAUDE.md**: [../CLAUDE.md](../CLAUDE.md) - Orchestration layer
- **Documentation**: [../documentation/CLAUDE.md](../documentation/CLAUDE.md) - Templates and references
- **Skills Examples**: [../claude-skills-examples/](../claude-skills-examples/) - Reference implementations
- **GitHub Workflows**: [../.github/CLAUDE.md](../.github/CLAUDE.md) - GitHub automation

---

## Support

For questions, issues, or contributions:
- Open a GitHub issue
- Refer to individual skill HOW_TO_USE.md files
- Check the Skills Factory template for generation instructions
