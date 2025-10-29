---
name: slash-command-factory
description: Generate custom Claude Code slash commands through intelligent 5-7 question flow. Creates powerful commands for business research, content analysis, healthcare compliance, API integration, documentation automation, and workflow optimization. Outputs organized commands to generated-commands/ with validation and installation guidance.
---

# Slash Command Factory

A comprehensive system for generating production-ready Claude Code slash commands through a simple question-based workflow.

---

## What This Skill Does

This skill helps you create custom slash commands for Claude Code by:
- Asking 5-7 straightforward questions about your command needs
- Generating complete command .md files with proper YAML frontmatter
- Providing 10 powerful preset commands for common use cases
- Validating command format and syntax
- Creating well-organized folder structures
- Offering installation guidance

**Output**: Complete slash commands ready to use in Claude Code

---

## Official Command Structure Patterns

This skill generates commands following **three official patterns** from Anthropic documentation:

### Pattern A: Simple (Context → Task)

**Best for**: Straightforward tasks with clear input/output
**Example**: Code review, file updates, simple analysis
**Official Reference**: code-review.md

**Structure**:
```markdown
---
allowed-tools: Bash(git diff:*), Bash(git log:*)
description: Purpose description
---

## Context
- Current state: !`bash command`
- Additional data: !`another command`

## Your task
[Clear instructions with numbered steps]
[Success criteria]
```

**When to use**:
- Simple, focused tasks
- Quick analysis or reviews
- Straightforward workflows
- 1-3 bash commands for context

---

### Pattern B: Multi-Phase (Discovery → Analysis → Task)

**Best for**: Complex discovery and documentation tasks
**Example**: Codebase analysis, comprehensive audits, system mapping
**Official Reference**: codebase-analysis.md

**Structure**:
```markdown
---
allowed-tools: Bash(find:*), Bash(tree:*), Bash(ls:*), Bash(grep:*), Bash(wc:*), Bash(du:*)
description: Comprehensive purpose
---

# Command Title

## Phase 1: Project Discovery
### Directory Structure
!`find . -type d | sort`

### File Count Analysis
!`find . -type f | wc -l`

## Phase 2: Detailed Analysis
[More discovery commands]
[File references with @]

## Phase 3: Your Task
Based on all discovered information, create:

1. **Deliverable 1**
   - Subsection
   - Details

2. **Deliverable 2**
   - Subsection
   - Details

At the end, write output to [filename].md
```

**When to use**:
- Comprehensive analysis needed
- Multiple discovery phases
- Large amounts of context gathering
- 10+ bash commands for data collection
- Generate detailed documentation files

---

### Pattern C: Agent-Style (Role → Process → Guidelines)

**Best for**: Specialized expert roles and coordination
**Example**: Domain experts, orchestrators, specialized advisors
**Official Reference**: openapi-expert.md

**Structure**:
```markdown
---
name: command-name
description: |
  Multi-line description for complex purpose
  explaining specialized role
color: yellow
---

You are a [specialized role] focusing on [domain expertise].

**Core Responsibilities:**

1. **Responsibility Area 1**
   - Specific tasks
   - Expected outputs

2. **Responsibility Area 2**
   - Specific tasks
   - Expected outputs

**Working Process:**

1. [Step 1 in workflow]
2. [Step 2 in workflow]
3. [Step 3 in workflow]

**Important Considerations:**

- [Guideline 1]
- [Guideline 2]
- [Constraint or best practice]

When you encounter [scenario], [action to take].
```

**When to use**:
- Need specialized domain expertise
- Orchestrating complex workflows
- Coordinating multiple sub-processes
- Acting as expert advisor
- Require specific procedural guidelines

---

## Comprehensive Naming Convention

### Command File Naming Rules

All slash command files MUST follow kebab-case convention:

**Format**: `[verb]-[noun].md`, `[noun]-[verb].md`, or `[domain]-[action].md`

**Rules**:
1. **Case**: Lowercase only with hyphens as separators
2. **Length**: 2-4 words maximum
3. **Characters**: Only `[a-z0-9-]` allowed (letters, numbers, hyphens)
4. **Start/End**: Must begin and end with letter or number (not hyphen)
5. **No**: Spaces, underscores, camelCase, TitleCase, or special characters

---

### Conversion Algorithm

**User Input** → **Command Name**

```
Input: "Analyze customer feedback and generate insights"
↓
1. Extract action: "analyze"
2. Extract target: "feedback"
3. Combine: "analyze-feedback"
4. Validate: Matches [a-z0-9-]+ pattern ✓
5. Output: analyze-feedback.md
```

**More Examples**:
- "Review pull requests" → `pr-review.md` or `review-pr.md`
- "Generate API documentation" → `api-document.md` or `document-api.md`
- "Update README files" → `update-readme.md` or `readme-update.md`
- "Audit security compliance" → `security-audit.md` or `compliance-audit.md`
- "Research market trends" → `research-market.md` or `market-research.md`
- "Analyze code quality" → `code-analyze.md` or `analyze-code.md`

---

### Official Examples (From Anthropic Docs)

**Correct**:
- ✅ `code-review.md` (verb-noun)
- ✅ `codebase-analysis.md` (noun-noun compound)
- ✅ `update-claude-md.md` (verb-noun-qualifier)
- ✅ `openapi-expert.md` (domain-role)

**Incorrect**:
- ❌ `code_review.md` (snake_case - wrong)
- ❌ `CodeReview.md` (PascalCase - wrong)
- ❌ `codeReview.md` (camelCase - wrong)
- ❌ `review.md` (too vague - needs target)
- ❌ `analyze-customer-feedback-data.md` (too long - >4 words)

---

## Bash Permission Patterns

### Critical Rule: No Wildcards

**❌ NEVER ALLOWED**:
```yaml
allowed-tools: Bash
```
This wildcard permission is **prohibited** per official Anthropic patterns.

**✅ ALWAYS REQUIRED**:
```yaml
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git log:*)
```
Must specify **exact commands** with wildcards only for subcommands.

---

### Official Permission Patterns

Based on Anthropic's documented examples:

**Git Operations** (code-review, update-docs):
```yaml
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git branch:*), Bash(git add:*), Bash(git commit:*)
```

**File Discovery** (codebase-analysis):
```yaml
allowed-tools: Bash(find:*), Bash(tree:*), Bash(ls:*), Bash(du:*)
```

**Content Analysis** (comprehensive discovery):
```yaml
allowed-tools: Bash(grep:*), Bash(wc:*), Bash(head:*), Bash(tail:*), Bash(cat:*)
```

**Data Processing** (custom analysis):
```yaml
allowed-tools: Bash(awk:*), Bash(sed:*), Bash(sort:*), Bash(uniq:*)
```

**Combined Patterns** (multi-phase commands):
```yaml
allowed-tools: Bash(find:*), Bash(tree:*), Bash(ls:*), Bash(grep:*), Bash(wc:*), Bash(du:*), Bash(head:*), Bash(tail:*), Bash(cat:*), Bash(touch:*)
```

---

### Permission Selection Guide

| Command Type | Bash Permissions | Example Commands |
|--------------|------------------|------------------|
| **Git Commands** | `git status, git diff, git log, git branch` | code-review, commit-assist |
| **Discovery** | `find, tree, ls, du` | codebase-analyze, structure-map |
| **Analysis** | `grep, wc, head, tail, cat` | search-code, count-lines |
| **Update** | `git diff, find, grep` | update-docs, sync-config |
| **Data Processing** | `awk, sed, sort, uniq` | parse-data, format-output |
| **Comprehensive** | All of the above | full-audit, system-analyze |

---

## Two Paths to Generate Commands

### Path 1: Quick-Start Presets (30 seconds)

Choose from 10 powerful preset commands:

**Business & Research**:
1. **/research-business** - Comprehensive market research and competitive analysis
2. **/research-content** - Multi-platform content trend analysis and SEO strategy

**Healthcare & Compliance**:
3. **/medical-translate** - Translate medical terminology to 8th-10th grade (German/English) 
4. **/compliance-audit** - HIPAA/GDPR/DSGVO compliance validation

**Development & Integration**:
5. **/api-build** - Generate complete API integration code with tests
6. **/test-auto** - Auto-generate comprehensive test suites

**Documentation & Knowledge**:
7. **/docs-generate** - Automated documentation creation
8. **/knowledge-mine** - Extract and structure insights from documents

**Workflow & Productivity**:
9. **/workflow-analyze** - Analyze and optimize business processes
10. **/batch-agents** - Launch and coordinate multiple agents for complex tasks

### Path 2: Custom Command (5-7 Questions)

Create a completely custom command for your specific needs.

---

## Question Flow (Custom Path)

### Question 1: Command Purpose

"What should this slash command do?

Be specific about its purpose and when you'll use it.

Examples:
- 'Analyze customer feedback and generate actionable insights'
- 'Generate HIPAA-compliant API documentation'
- 'Research market trends and create content strategy'
- 'Extract key insights from research papers'

Your command's purpose: ___"

---

### Question 2: Arguments (Auto-Determined)

The skill automatically determines if your command needs arguments based on the purpose.

**If arguments are needed**, they will use `$ARGUMENTS` format:
- User types: `/your-command argument1 argument2`
- Command receives: `$ARGUMENTS` = "argument1 argument2"

**Examples**:
- `/research-business "Tesla" "EV market"` → $ARGUMENTS = "Tesla EV market"
- `/medical-translate "Myokardinfarkt" "de"` → $ARGUMENTS = "Myokardinfarkt de"

**No user input needed** - skill decides intelligently.

---

### Question 3: Which Tools?

"Which Claude Code tools should this command use?

Available tools:
- **Read** - Read files
- **Write** - Create files
- **Edit** - Modify files
- **Bash** - Execute shell commands (MUST specify exact commands)
- **Grep** - Search code
- **Glob** - Find files by pattern
- **Task** - Launch agents

**CRITICAL**: For Bash, you MUST specify exact commands, not wildcards.

**Bash Examples**:
- ✅ Bash(git status:*), Bash(git diff:*), Bash(git log:*)
- ✅ Bash(find:*), Bash(tree:*), Bash(ls:*)
- ✅ Bash(grep:*), Bash(wc:*), Bash(head:*)
- ❌ Bash (wildcard not allowed per official patterns)

**Tool Combination Examples**:
- Git command: Read, Bash(git status:*), Bash(git diff:*)
- Code generator: Read, Write, Edit
- Discovery command: Bash(find:*), Bash(tree:*), Bash(grep:*)
- Analysis command: Read, Grep, Task (launch agents)

Your tools (comma-separated): ___"

---

### Question 4: Agent Integration

"Does this command need to launch agents for specialized tasks?

Examples of when to use agents:
- Complex analysis (launch rr-architect, rr-security)
- Implementation tasks (launch rr-frontend, rr-backend)
- Quality checks (launch rr-qa, rr-test-runner)

Options:
1. **No agents** - Command handles everything itself
2. **Launch agents** - Delegate to specialized agents

Your choice (1 or 2): ___"

If "2", ask: "Which agents should it launch? ___"

---

### Question 5: Output Type

"What type of output should this command produce?

1. **Analysis** - Research report, insights, recommendations
2. **Files** - Generated code, documentation, configs
3. **Action** - Execute tasks, run workflows, deploy
4. **Report** - Structured report with findings and next steps

Your choice (1, 2, 3, or 4): ___"

---

### Question 6: Model Preference (Optional)

"Which Claude model should this command use?

1. **Default** - Inherit from main conversation (recommended)
2. **Sonnet** - Best for complex tasks
3. **Haiku** - Fastest, cheapest (for simple commands)
4. **Opus** - Maximum capability (for critical tasks)

Your choice (1, 2, 3, or 4) or press Enter for default: ___"

---

### Question 7: Additional Features (Optional)

"Any special features?

Optional features:
- **Bash execution** - Run shell commands and include output (!`command`)
- **File references** - Include file contents (@file.txt)
- **Context gathering** - Read project files for context

Features you need (comma-separated) or press Enter to skip: ___"

---

## Generation Process

After collecting answers:

1. **Generate YAML Frontmatter**:
```yaml
---
description: [From command purpose]
argument-hint: [If $ARGUMENTS needed]
allowed-tools: [From tool selection]
model: [If specified]
---
```

2. **Generate Command Body**:
```markdown
[Purpose-specific instructions]

[If uses agents]:
1. **Launch [agent-name]** with [specific task]
2. Coordinate workflow
3. Validate results

[If uses bash]:
- Context: !`bash command`

[If uses file refs]:
- Review: @file.txt

Success Criteria: [Based on output type]
```

3. **Create Folder Structure**:
```
generated-commands/[command-name]/
├── [command-name].md    # Command file (ROOT)
├── README.md            # Installation guide (ROOT)
├── TEST_EXAMPLES.md     # Testing examples (ROOT)
└── [folders if needed]  # standards/, examples/, scripts/
```

4. **Validate Format**:
- ✅ YAML frontmatter valid
- ✅ $ARGUMENTS syntax correct (if used)
- ✅ allowed-tools format proper
- ✅ Folder organization clean

5. **Provide Installation Instructions**:
```
Your command is ready!

Output location: generated-commands/[command-name]/

To install:
1. Copy the command file:
   cp generated-commands/[command-name]/[command-name].md .claude/commands/

2. Restart Claude Code (if already running)

3. Test:
   /[command-name] [arguments]
```

---

## Preset Command Details

### 1. /research-business

**Purpose**: Comprehensive business and market research

**Arguments**: `$ARGUMENTS` (company or market to research)

**YAML**:
```yaml
---
description: Comprehensive business and market research with competitor analysis
argument-hint: [company/market] [industry]
allowed-tools: Read, Bash, Grep
---
```

**What it does**:
- Market size and trends analysis
- Competitor SWOT analysis
- Opportunity identification
- Industry landscape overview
- Strategic recommendations

---

### 2. /research-content

**Purpose**: Multi-platform content trend analysis

**Arguments**: `$ARGUMENTS` (topic to research)

**YAML**:
```yaml
---
description: Multi-platform content trend analysis for data-driven content strategy
argument-hint: [topic] [platforms]
allowed-tools: Read, Bash
---
```

**What it does**:
- Analyze trends across Google, Reddit, YouTube, Medium, LinkedIn, X
- User intent analysis (informational, commercial, transactional)
- Content gap identification
- SEO-optimized outline generation
- Platform-specific publishing strategies

---

### 3. /medical-translate

**Purpose**: Translate medical terminology to patient-friendly language

**Arguments**: `$ARGUMENTS` (medical term and language)

**YAML**:
```yaml
---
description: Translate medical terminology to 8th-10th grade reading level (German/English)
argument-hint: [medical-term] [de|en]
allowed-tools: Read
---
```

**What it does**:
- Translate complex medical terms
- Simplify to 8th-10th grade reading level
- Validate with Flesch-Kincaid (EN) or Wiener Sachtextformel (DE)
- Preserve clinical accuracy
- Provide patient-friendly explanations

---

### 4. /compliance-audit

**Purpose**: Check code for regulatory compliance

**Arguments**: `$ARGUMENTS` (path and compliance standard)

**YAML**:
```yaml
---
description: Audit code for HIPAA/GDPR/DSGVO compliance requirements
argument-hint: [code-path] [hipaa|gdpr|dsgvo|all]
allowed-tools: Read, Grep, Task
---
```

**What it does**:
- Scan for PHI/PII handling
- Check encryption requirements
- Verify audit logging
- Validate data subject rights
- Generate compliance report

---

### 5. /api-build

**Purpose**: Generate complete API integration code

**Arguments**: `$ARGUMENTS` (API name and endpoints)

**YAML**:
```yaml
---
description: Generate complete API client with error handling and tests
argument-hint: [api-name] [endpoints]
allowed-tools: Read, Write, Edit, Bash, Task
---
```

**What it does**:
- Generate API client classes
- Add error handling and retries
- Create authentication logic
- Generate unit and integration tests
- Add usage documentation

---

### 6. /test-auto

**Purpose**: Auto-generate comprehensive test suites

**Arguments**: `$ARGUMENTS` (file path and test type)

**YAML**:
```yaml
---
description: Auto-generate comprehensive test suite with coverage analysis
argument-hint: [file-path] [unit|integration|e2e]
allowed-tools: Read, Write, Bash
---
```

**What it does**:
- Analyze code to test
- Generate test cases (happy path, edge cases, errors)
- Add test fixtures and mocks
- Calculate coverage
- Provide testing documentation

---

### 7. /docs-generate

**Purpose**: Automated documentation generation

**Arguments**: `$ARGUMENTS` (code path and doc type)

**YAML**:
```yaml
---
description: Auto-generate documentation from code (API docs, README, architecture)
argument-hint: [code-path] [api|readme|architecture|all]
allowed-tools: Read, Write, Grep
---
```

**What it does**:
- Extract code structure and functions
- Generate API documentation
- Create README with usage examples
- Build architecture diagrams (Mermaid)
- Add code examples

---

### 8. /knowledge-mine

**Purpose**: Extract structured insights from documents

**Arguments**: `$ARGUMENTS` (document path and output format)

**YAML**:
```yaml
---
description: Extract and structure knowledge from documents into actionable insights
argument-hint: [doc-path] [faq|summary|kb|all]
allowed-tools: Read, Grep
---
```

**What it does**:
- Read and analyze documents
- Extract key insights
- Generate FAQs
- Create knowledge base articles
- Summarize findings

---

### 9. /workflow-analyze

**Purpose**: Analyze and optimize business workflows

**Arguments**: `$ARGUMENTS` (workflow description)

**YAML**:
```yaml
---
description: Analyze workflows and provide optimization recommendations
argument-hint: [workflow-description]
allowed-tools: Read, Task
---
```

**What it does**:
- Map current workflow
- Identify bottlenecks
- Suggest automation opportunities
- Calculate efficiency gains
- Create implementation roadmap

---

### 10. /batch-agents

**Purpose**: Launch multiple coordinated agents

**Arguments**: `$ARGUMENTS` (agent names and task)

**YAML**:
```yaml
---
description: Launch and coordinate multiple agents for complex tasks
argument-hint: [agent-names] [task-description]
allowed-tools: Task
---
```

**What it does**:
- Parse agent list
- Launch agents in parallel (if safe) or sequential
- Coordinate outputs
- Integrate results
- Provide comprehensive summary

---

## Output Structure

Commands are generated in your project's root directory:

```
[your-project]/
└── generated-commands/
    └── [command-name]/
        ├── [command-name].md      # Command file (ROOT level)
        ├── README.md              # Installation guide (ROOT level)
        ├── TEST_EXAMPLES.md       # Testing guide (ROOT level - if applicable)
        │
        ├── standards/             # Only if command has standards
        ├── examples/              # Only if command has examples
        └── scripts/               # Only if command has helper scripts
```

**Organization Rules**:
- All .md files in ROOT directory
- Supporting folders separate (standards/, examples/, scripts/)
- No mixing of different types in same folder
- Clean, hierarchical structure

---

## Installation

**After generation**:

1. **Review output**:
   ```bash
   ls generated-commands/[command-name]/
   ```

2. **Copy to Claude Code** (when ready):
   ```bash
   # Project-level (this project only)
   cp generated-commands/[command-name]/[command-name].md .claude/commands/

   # User-level (all projects)
   cp generated-commands/[command-name]/[command-name].md ~/.claude/commands/
   ```

3. **Restart Claude Code** (if running)

4. **Test command**:
   ```bash
   /[command-name] [arguments]
   ```

---

## Usage Examples

### Generate a Preset Command

```
@slash-command-factory

Use the /research-business preset
```

**Output**: Complete business research command ready to install

---

### Generate a Custom Command

```
@slash-command-factory

Create a custom command for analyzing customer feedback and generating product insights
```

**Skill asks 5-7 questions** → **Generates complete command** → **Validates format** → **Provides installation steps**

---

## Command Format (What Gets Generated)

**Example generated command** (`my-command.md`):

```markdown
---
description: Brief description of what the command does
argument-hint: [arg1] [arg2]
allowed-tools: Read, Write, Bash
model: claude-3-5-sonnet-20241022
---

# Command Instructions

Do [task] with "$ARGUMENTS":

1. **Step 1**: First action
2. **Step 2**: Second action
3. **Step 3**: Generate output

**Success Criteria**:
- Criterion 1
- Criterion 2
- Criterion 3
```

---

## Validation

Every generated command is automatically validated for:
- ✅ Valid YAML frontmatter (proper syntax, required fields)
- ✅ Correct argument format ($ARGUMENTS, not $1 $2 $3)
- ✅ allowed-tools syntax (comma-separated string)
- ✅ Clean folder organization (if folders used)
- ✅ No placeholder text

**If validation fails**, you'll get specific fix instructions.

---

## Best Practices

**For Command Design**:
- Keep commands focused (one clear purpose)
- Use descriptive names (kebab-case for files)
- Document expected arguments clearly
- Include success criteria
- Add examples in TEST_EXAMPLES.md

**For Tool Selection**:
- Read: For analyzing files
- Write/Edit: For generating/modifying files
- Bash: For system commands, web research
- Task: For launching agents
- Grep/Glob: For searching code

**For Agent Integration**:
- Use Task tool to launch agents
- Specify which agents clearly
- Coordinate outputs
- Document agent roles

---

## Important Notes

**Arguments**:
- ✅ Always use `$ARGUMENTS` (all arguments as one string)
- ❌ Never use `$1`, `$2`, `$3` (positional - not used by this factory)

**Folder Organization**:
- ✅ All .md files in command root directory
- ✅ Supporting folders separate (standards/, examples/, scripts/)
- ✅ No mixing of different types

**Output Location**:
- Commands generate to: `./generated-commands/[command-name]/`
- User copies to: `.claude/commands/[command-name].md` (when ready)

---

## Example Invocations

### Use a Preset

```
@slash-command-factory

Generate the /research-content preset command
```

→ Creates content research command with all features

---

### Create Custom Healthcare Command

```
@slash-command-factory

Create a command that generates German PTV 10 therapy applications
```

**Skill asks**:
- Purpose? (Generate PTV 10 applications)
- Tools? (Read, Write, Task)
- Agents? (Yes - health-sdk-builder related agents)
- Output? (Files - therapy application documents)
- Model? (Sonnet - for quality)

**Result**: `/generate-ptv10` command ready to use

---

### Create Business Intelligence Command

```
@slash-command-factory

Build a command for competitive SWOT analysis
```

**Skill asks 5-7 questions** → **Generates `/swot-analysis` command** → **Validates** → **Ready to install**

---

## Integration with Factory Agents

**Works with**:
- factory-guide (can delegate to this skill via prompts-guide pattern)
- Existing slash commands (/build, /validate-output, etc.)

**Complements**:
- skills-guide (builds Skills)
- prompts-guide (builds Prompts)
- agents-guide (builds Agents)
- slash-command-factory (builds Commands) ← This skill

**Complete ecosystem** for building all Claude Code augmentations!

---

## Output Validation

Generated commands are validated for:

**YAML Frontmatter**:
- Has `description` field
- Proper YAML syntax
- Valid frontmatter fields only

**Arguments**:
- Uses $ARGUMENTS if needed
- Has argument-hint if $ARGUMENTS used
- No $1, $2, $3 positional args

**Tools**:
- Valid tool names
- Proper comma-separated format
- Appropriate for command purpose

**Organization**:
- .md files in root
- Folders properly separated
- No scattered files

---

## Success Criteria

Generated commands should:
- ✅ Have valid YAML frontmatter
- ✅ Use $ARGUMENTS (never positional)
- ✅ Work when copied to .claude/commands/
- ✅ Execute correctly with arguments
- ✅ Produce expected output
- ✅ Follow organizational standards

---

**Version**: 1.0.0
**Last Updated**: October 28, 2025
**Compatible**: Claude Code (all versions with slash command support)

**Build powerful custom slash commands in minutes!** ⚡
