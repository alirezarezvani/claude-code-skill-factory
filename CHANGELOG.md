# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.5.0] - 2025-11-06

### Added
- **3 Production-Ready Skills**:
  - Scrum Master Agent (15 files) - Sprint analytics, backlog prioritization, multi-tool integration
  - TDD Guide (15 files) - Test generation, coverage analysis, multi-framework support
  - Tech Stack Evaluator (14 files) - TCO calculation, security assessment, migration analysis
- **GitHub CI/CD Specialist Mega-Prompt** (~4,800 tokens) - Complete GitHub Actions workflow blueprint
- **Git Governance Workflows**:
  - Commit validation (conventional commits with commitlint)
  - Branch naming enforcement (feat/*, fix/*, docs/*, etc.)
  - CI quality gates (Python syntax, markdown links, security audit)
  - Release orchestration
- **10 Git Slash Commands** for workflow automation

### Changed
- Disabled yamllint check in CI (creates false positives with markdown in bash strings)
- Updated SKILLS_FACTORY_PROMPT with file cleanliness standards

### Fixed
- Branch naming convention validation (slash instead of dash)
- YAML syntax in workflow files (heredoc format for multiline strings)

---

## [1.4.0] - 2025-10-30

### Added
- **Codex CLI Bridge** skill (48 KB) - Seamless interoperability between Claude Code and OpenAI Codex CLI
  - Reference-based architecture (no file duplication)
  - Automatic CLAUDE.md → AGENTS.md translation
  - Cross-tool team collaboration support
- **7 Python modules** for bridge functionality:
  - bridge.py - Main orchestrator with CLI interface
  - safety_mechanism.py - Environment validation (Codex CLI + CLAUDE.md checks)
  - claude_parser.py - CLAUDE.md parser with YAML frontmatter support
  - project_analyzer.py - Project structure and metadata analysis
  - agents_md_generator.py - Template-based AGENTS.md generation
  - skill_documenter.py - Different approaches for functional vs prompt-based skills
  - codex_executor.py - Codex CLI helpers (always uses 'codex exec')
- **2 new slash commands**:
  - /sync-agents-md - Regenerate AGENTS.md from CLAUDE.md (integrates with /init, /update-claude, /check-docs)
  - /codex-exec - Execute Codex CLI commands with proper syntax (analysis, edit, search, resume types)
- **AGENTS.md generation** - Auto-generates Codex CLI-compatible documentation from CLAUDE.md
  - 19 KB output for claude-code-skills-factory (629 lines, 13 skills, 59 agents)
  - Workflow pattern translations (Claude commands → Codex equivalents)
  - Command reference table (Claude Code ↔ Codex CLI)
  - MCP integration documentation
- **Safety mechanisms**:
  - Auto-validates Codex CLI installation
  - Auto-runs /init if CLAUDE.md missing (with user notification)
  - Minimal CLAUDE.md fallback generation
  - Comprehensive error handling
- **Package distribution** - package.sh script creates distributable ZIP (48 KB) with SHA256 checksum

### Changed
- **README.md completely revised** for better focus on shortcuts and efficiency
  - Added "Quick Start (3 Shortcuts)" section at top
  - Added "Built-in Commands" section with tables for 7 slash commands and 4 interactive agents
  - Added "Complete Workflow Examples" with 3 real-world scenarios
  - Enhanced Repository Structure with detailed .claude/ breakdown
  - Improved Production Skills section with "Most Popular" and "New" badges
  - Added emojis for better scannability
  - Reduced from 876 to 367 lines while adding more practical content
- **Repository structure** - Added AGENTS.md to root and new slash commands to .claude/commands/

### Documentation
- **Use Cases**: Cross-tool teams, project migration, CI/CD integration, skills marketplace compatibility
- **Model selection helpers**: gpt-5 (general reasoning) vs gpt-5-codex (code editing)
- **Sandbox modes**: read-only, workspace-write, danger-full-access
- **Workflow integration**: /sync-agents-md integrates with existing Claude Code commands
- **Complete documentation** (6 files): SKILL.md, README, HOW_TO_USE, INSTALL, CHANGELOG, samples

### Fixed
- Consolidated README.md for 58% reduction in length (876 → 367 lines) while adding practical shortcuts
- Better focus on built-in commands and workflow efficiency

---

## [2.2.0] - 2025-10-29

### Added
- **MASTER_SLASH_COMMANDS_PROMPT.md** - Comprehensive master template (~1500 lines) for generating slash commands following official Anthropic patterns
- **documentation/references/** folder - 6 official Anthropic slash command examples for pattern reference
- **Three official command structure patterns** integrated into slash-command-factory:
  - Simple Pattern (code-review) - Context → Task for straightforward workflows
  - Multi-Phase Pattern (codebase-analyze) - Discovery → Analysis → Task for complex documentation
  - Agent-Style Pattern (ultrathink, openapi-sync) - Role → Process → Guidelines for expert coordination
- **7 new official presets** - code-review, codebase-analyze, update-docs, openapi-sync, ultrathink, deps-audit, metrics-report
- **Comprehensive four-layer validation** - Command name (kebab-case), bash permissions (specific only), arguments usage ($ARGUMENTS), YAML structure
- **Smart generation features**:
  - Auto-detect command structure pattern based on purpose
  - Auto-generate bash permissions (git, discovery, comprehensive patterns)
  - Automatic kebab-case naming conversion with validation
- **Test command** - marketing-research.md generated and validated as demonstration

### Changed
- **Slash Command Factory enhanced to v2.0** (26 KB)
  - Expanded from 10 to 17 presets (10 original + 7 official examples)
  - SKILL.md enhanced with official patterns documentation (~1000 lines)
  - command_generator.py enhanced with structure detection, naming validation, bash permission generation
  - validator.py enhanced with comprehensive four-layer validation system
  - presets.json expanded with 7 new official preset commands
  - HOW_TO_USE.md updated with pattern guide and naming convention examples
- **README.md updated** to version 1.3.0
  - Repository structure diagram includes all 4 templates and documentation/references/
  - Slash Command Factory section enhanced with v2.0 details
  - Quick Reference updated with MASTER_SLASH_COMMANDS_PROMPT.md
  - Version section updated with comprehensive v1.3.0 changelog
- **CLAUDE.md updated**
  - Repository structure diagram includes all 4 templates and documentation/references/
  - Templates for Generation section enhanced with MASTER_SLASH_COMMANDS_PROMPT.md details
  - Slash Command Factory (#11) description enhanced with comprehensive v2.0 capabilities

### Documentation
- **Validation strictness** - All generated commands must pass four-layer validation
- **Bash permission patterns** - Never uses wildcard `Bash`, always specific commands (`Bash(git status:*)`)
- **Naming convention** - Enforced kebab-case (2-4 words) with automatic conversion algorithm
- **Arguments standard** - Always `$ARGUMENTS`, never positional `$1, $2, $3`

---

## [2.1.0] - 2025-10-29

### Added
- **Slash Command Factory** skill - Generate custom Claude Code slash commands with 10 powerful presets
- **Interactive Navigation Agents** (4 agents) - Conversational guides for building Skills, Prompts, Agents, and Commands
  - factory-guide (orchestrator) - Delegates to appropriate specialist
  - skills-guide - Builds Claude Skills through 4-5 questions
  - prompts-guide - Guides prompt-factory usage (69 presets)
  - agents-guide - Builds Claude Code Agents through 5-6 questions
- **5 Workflow Slash Commands** - Complete start-to-finish workflow
  - /build - Start building (invokes orchestrator or specialists)
  - /validate-output - Quality check with auto-ZIP creation
  - /install-skill - Installation guidance
  - /test-factory - Testing examples
  - /factory-status - Progress tracking
- **Public Gist** - Slash Command Factory guide for SEO/AEO
- **10 Slash Command Presets** - Business research, content analysis, medical translation, compliance audit, API building, test automation, docs generation, knowledge extraction, workflow optimization, agent coordination

### Changed
- **README reorganized** - Navigation system moved to end (before Contributing)
- **README enhanced** - Added Slash Command Factory (#8 in Generated Skills)
- **/validate-output** - Now auto-creates ZIP files on successful validation
- **CLAUDE.md** - Added Slash Command Factory (#11) documentation
- **GISTS.md** - Added 4th public gist (Slash Command Factory)
- **Documentation references** - Updated with slash-command-factory links

### Added Documentation
- `.claude/agents/` - 4 navigation agents (orchestrator + 3 specialists)
- `.claude/commands/` - 5 workflow commands
- `generated-skills/slash-command-factory/` - Complete skill with presets
- `documentation/references/` - Slash command examples from Anthropic

---

## [2.0.0] - 2025-10-28

### Added
- **Health SDK Builder** skill - Comprehensive healthcare Agent SDK builder with HIPAA/GDPR/DSGVO/PTV 10 compliance
- **Multilingual support** - German + English mandatory for healthcare applications
- **Therapy modalities** - CBT, Psychodynamic, Psychoanalysis, Depth Psychology
- **German PTV 10 automation** - 60-session therapy applications (2.5 DIN A4 pages)
- **Medical terminology translation** - 8th-10th grade reading level for patients
- **2025 Claude API features** - Computer Use, Code Execution, Files API, Extended Caching
- **PR-to-issue auto-close workflow** - Automatically close linked issues when PRs merge
- **README Option C** - Prompt Factory as third quick-start path
- **Public Gists** - 3 comprehensive guides for SEO and Answer Engine Optimization
- **Professional standards** - CONTRIBUTING.md, LICENSE (MIT), .editorconfig
- **.github consolidation** - 6 files merged into single GITHUB_WORKFLOWS_GUIDE.md
- **.archive structure** - Organized historical documents
- **Security audit** - Complete security audit and SECURITY.md policy

### Changed
- **README enhanced** - Added Complementary Resources (Claude Code Tresor, Claude Skills Library)
- **README structure** - Three-path quick start (Skills, Agents, Prompts)
- **prompt-suite → prompt-factory** - Renamed for clarity
- **Repository size** - Reduced from 37MB to 10MB (73% reduction)
- **.gitignore updated** - Proper exclusions for test/development content

### Removed
- **test-workspace/** - Moved to separate testing repository (31MB freed)
- **github-docs/** - Temporary reference files deleted (48KB)
- **.DS_Store files** - macOS metadata cleaned (7 files)
- **claude-skills-examples/** from tracking - Reference material, gitignored
- **Outdated workflow docs** - 6 files consolidated into 1
- **Internal files** from tracking - TEST_CLAUDE_REVIEW.md, claude-skills-instructions.md

### Fixed
- **Skill naming** - health-sdk-builder (removed "claude" reserved word)
- **Gitignore rules** - Proper exclusions for all test/dev content
- **Documentation references** - Updated to point to consolidated guides

### Security
- **API key isolation** - Separate testing repository for SDK development
- **Gitignore enhanced** - All sensitive files excluded
- **.archive/** - Internal documents organized and excluded

---

## [1.2.0] - 2025-10-23

### Added
- Prompt Factory skill (403KB) - World-class prompt generation with 69 presets
- PROMPTS_FACTORY_PROMPT.md template
- Generated prompts examples (5 sample outputs)
- Marketing growth prompt builder

### Changed
- Expanded coverage to 15 professional domains
- Multi-format output (XML/Claude/ChatGPT/Gemini)

---

## [1.1.0] - 2025-10-21

### Added
- Psychology Advisor skill (31KB) - Evidence-based mental wellness
- CBT techniques (cognitive distortions, thought records)
- Mindfulness exercises
- Stress management tools

---

## [1.0.0] - 2025-10-20

### Added
- Initial repository structure
- SKILLS_FACTORY_PROMPT.md template
- AGENTS_FACTORY_PROMPT.md template
- Example skills (Financial Analysis, Brand Guidelines, Financial Models)
- AWS Solution Architect skill (53KB)
- Content Trend Researcher skill (35KB)
- Microsoft 365 Tenant Manager skill (40KB)
- Agent Factory skill (12KB)
- GitHub automation workflows (10 workflows)
- Documentation structure

---

## Version Guidelines

**Major version** (X.0.0): Breaking changes, major new features
**Minor version** (0.X.0): New features, backward compatible
**Patch version** (0.0.X): Bug fixes, documentation updates

---

**Current Version**: 1.4.0
**Last Updated**: October 30, 2025
