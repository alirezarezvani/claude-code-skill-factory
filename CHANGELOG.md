# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

**Current Version**: 2.0.0
**Last Updated**: October 28, 2025
