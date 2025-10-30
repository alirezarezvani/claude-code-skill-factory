# generated-skills/CLAUDE.md

This file provides guidance for working with production-ready generated skills in this repository.

---

## Production-Ready Skills Catalog

The `generated-skills/` folder contains complete, production-ready skills created using the Skills Factory Prompt template. These skills demonstrate professional-grade implementations and can be used as-is or customized for specific needs.

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
| Slash Command Factory | 26 KB | Medium |
| Psychology Advisor | 31 KB | Medium |
| Content Trend Researcher | 35 KB | Medium |
| Microsoft 365 Tenant Manager | 40 KB | Medium |
| AWS Solution Architect | 53 KB | High |
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
