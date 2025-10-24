# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 🚨 MANDATORY WORKFLOW REQUIREMENT

**CRITICAL**: All work on this project MUST follow this workflow. **NO EXCEPTIONS.**

### Required Process for Every User Request

1. **PLAN MODE FIRST**
   - Use plan mode to create a detailed implementation plan
   - Break down the work into clear, actionable steps
   - **KEEP PLANS SMALL: 5-10 tasks maximum**
   - Estimate effort and identify potential challenges

2. **GET USER APPROVAL**
   - Present the plan to the user
   - Wait for explicit approval before proceeding
   - Address any questions or concerns

3. **CREATE GITHUB ISSUE**
   - Create a GitHub issue with the `plan` label
   - Include the approved plan in the issue body
   - Use markdown checkboxes for tasks: `- [ ] Task name`
   - **MAXIMUM 5-10 TASKS** - The plan-to-issues automation creates one issue per task
   - **For large initiatives**: Create multiple small plan issues, NOT one giant plan

4. **AUTOMATION CREATES SUBTASKS**
   - GitHub workflow creates individual issues for each task
   - All subtasks are linked to the parent issue
   - All added to project board for tracking
   - **WARNING**: 40+ tasks = API rate limits and issue spam

5. **START IMPLEMENTATION**
   - Begin work on subtasks in priority order
   - Update issue status as you progress
   - Reference issue numbers in commits

### Why This Matters

- ✅ **Proper tracking**: Every task is tracked in GitHub issues and project board
- ✅ **Clear planning**: Prevents scope creep and ensures thoughtful approach
- ✅ **Team visibility**: Everyone can see what's being worked on
- ✅ **Audit trail**: Complete history of decisions and implementation
- ✅ **Automation leverage**: Uses the excellent GitHub automation built into this repo

### Example Workflows

**✅ CORRECT - Small Plan (5 tasks)**:
```
User: "Add a new skill for data visualization"

1. Enter plan mode
2. Create plan with 5 tasks:
   - Research data visualization libraries
   - Design SKILL.md structure
   - Implement Python visualization classes
   - Create sample data and HOW_TO_USE.md
   - Test with real data
3. Present plan to user, get approval
4. Create GitHub issue with 'plan' label containing 5 tasks
5. Automation creates 5 subtask issues
6. Begin implementation
```

**❌ WRONG - Too Many Tasks**:
```
User: "Create comprehensive Wiki documentation"

DON'T DO THIS:
- Create issue with 40+ tasks in checkboxes
- Results in 40+ GitHub issues created
- Hits API rate limits
- Creates issue spam

DO THIS INSTEAD:
- Break into 3-4 small plan issues:
  - Plan #1: Wiki Foundation (5 tasks)
  - Plan #2: Core Wiki Pages (6 tasks)
  - Plan #3: Advanced Documentation (5 tasks)
```

**GOLDEN RULE: 5-10 TASKS MAXIMUM PER PLAN ISSUE**

---

## 📋 Task Hierarchy (Plan → Task → Subtask)

### Three-Level Structure

```
PLAN ISSUE (#100)                      - Epic or feature
  ├─ TASK #101 (5-10 tasks)           - Major work item
  │   ├─ SUBTASK #103 (0-5 subtasks)  - Atomic work
  │   ├─ SUBTASK #104
  │   └─ SUBTASK #105
  ├─ TASK #102
  │   ├─ SUBTASK #106
  │   └─ SUBTASK #107
  └─ TASK #108
```

### Level 1: PLAN Issues
- **Purpose**: High-level feature or epic
- **Task Count**: 5-10 tasks (enforced by plan-validator workflow)
- **Labels**: `plan`, `plan-validated`
- **Created**: Manually by team
- **Format**:
  ```markdown
  ## Goal
  [What we're building and why]

  ## Tasks
  - [ ] Task 1: Clear, actionable description
  - [ ] Task 2: Clear, actionable description
  - [ ] Task 3-10: ...

  ## Acceptance Criteria
  - [ ] Criterion 1
  - [ ] Criterion 2
  ```

### Level 2: TASK Issues
- **Purpose**: Major work item (can be completed independently)
- **Title**: "Task: [description]" (auto-generated)
- **Labels**: `task`, `plan-item`, `skip-triage`
- **Created**: Automatically by plan-to-tasks workflow
- **Parent**: Always linked to parent PLAN
- **Subtasks**: Optional (0-5 subtasks, triggered by `needs-subtasks` label)
- **Scope**: Focused piece of work (1-3 days)

### Level 3: SUBTASK Issues
- **Purpose**: Atomic work unit (smallest unit)
- **Title**: "Subtask: [description]" (auto-generated)
- **Labels**: `subtask`, `skip-triage`
- **Created**: Automatically by task-to-subtasks workflow
- **Parent**: Linked to parent TASK and grandparent PLAN
- **Scope**: Single, focused piece of work (1-3 hours)
- **Maximum**: 5 subtasks per task (enforced)

### Workflow States & Labels

**Triage Control**:
- `skip-triage` - Skips automatic classification (removed when ready)
- `needs-subtasks` - Triggers subtask creation (on TASK issues only)

**Status Tracking** (synced with project board):
- `status: triage` - Needs classification
- `status: backlog` - Planned but not ready
- `status: ready` - Ready to start
- `status: in-progress` - Actively being worked on
- `status: in-review` - Under review
- `status: done` - Completed (auto-applied when issue closed)

### Smart Bidirectional Synchronization

**Workflow**: `.github/workflows/smart-sync.yml`

The smart-sync workflow replaces the old issue-to-project-sync and project-to-issue-sync workflows with a single, intelligent system that prevents sync loops and respects rate limits.

**Key Features**:
- ✅ **10-second debouncing**: Prevents rapid back-and-forth updates
- ✅ **Circuit breaker**: Checks rate limits before executing (requires 50+ remaining)
- ✅ **Direction detection**: Automatically determines sync direction based on event source
- ✅ **Silent operation**: No notification spam (updates without comments)
- ✅ **Loop prevention**: One-way sync logic prevents ping-pong loops

**How It Works**:

1. **Event Triggers**:
   - Issue labeled/closed/reopened → Syncs Issue → Project Board
   - Project board status changed → Syncs Project Board → Issue

2. **Safety Checks**:
   - Rate limit check (circuit breaker)
   - 10-second debounce delay
   - Concurrency control (cancel in-progress runs)

3. **Sync Operations**:

   **Issue → Project Board**:
   - Adds issue to project if not present
   - Maps issue status labels to project board columns
   - Updates project board status field
   - Closes/reopens based on issue state

   **Project Board → Issue**:
   - Removes old status labels
   - Adds new status label based on project board column
   - Closes issue if moved to "Done"
   - Reopens issue if moved from "Done"

4. **Status Mapping**:
   ```
   Issue Label          ↔  Project Board Column
   ─────────────────────────────────────────────
   status: triage       ↔  To triage
   status: backlog      ↔  Backlog
   status: ready        ↔  Ready
   status: in-progress  ↔  In Progress
   status: in-review    ↔  In Review
   status: done         ↔  Done
   (closed state)       ↔  Done
   ```

**Best Practices**:
- ✅ DO: Change status on project board OR issue (not both at once)
- ✅ DO: Wait 10 seconds between rapid status changes
- ✅ DO: Use status labels for tracking (they sync automatically)
- ❌ DON'T: Manually update both issue and project board (creates duplicate syncs)
- ❌ DON'T: Make rapid status changes (triggers rate limit protection)

**Troubleshooting**:
- If sync appears stuck: Check rate limits with `gh api rate_limit`
- If status out of sync: Manually trigger by re-labeling or moving on board
- If getting rate limit warnings: Wait for cooldown (syncs will resume automatically)

### How to Use the Hierarchy

**Creating a Plan**:
1. Create issue with `plan` label
2. Add 5-10 tasks in checklist format
3. Validation workflow checks count & rate limits
4. If valid, adds `plan-validated` label
5. Plan-to-tasks workflow creates TASK issues automatically

**Breaking Down a Task**:
1. Open a TASK issue
2. Add `needs-subtasks` label
3. Create checklist in task body (max 5 items)
4. Task-to-subtasks workflow creates SUBTASK issues automatically

**Working on Tasks/Subtasks**:
1. Remove `skip-triage` label when ready for classification
2. Auto-triage workflow classifies and prioritizes
3. Move to "In Progress" on project board when starting work
4. Close issue when done (auto-syncs to "Done" on board)

### Best Practices

**Plan Issues**:
- ✅ DO: Keep to 5-10 tasks
- ✅ DO: Make tasks independent when possible
- ✅ DO: Write clear, actionable task descriptions
- ❌ DON'T: Create 20+ task plans (split into multiple plans)
- ❌ DON'T: Make tasks too vague or too detailed

**Task Issues**:
- ✅ DO: Add `needs-subtasks` if task is complex
- ✅ DO: Keep subtask count to 5 or fewer
- ✅ DO: Link to parent PLAN in description
- ❌ DON'T: Create subtasks manually (use automation)
- ❌ DON'T: Skip the `skip-triage` label removal step

**Subtask Issues**:
- ✅ DO: Keep scope small and focused (1-3 hours)
- ✅ DO: Link to both parent TASK and grandparent PLAN
- ✅ DO: Close promptly when completed
- ❌ DON'T: Create sub-subtasks (3 levels max)
- ❌ DON'T: Make subtasks too granular

### Examples

**Good Plan (7 tasks)**:
```markdown
## Goal
Implement user authentication system

## Tasks
- [ ] Design login UI components
- [ ] Implement JWT authentication backend
- [ ] Add password reset flow
- [ ] Create user profile management
- [ ] Implement session handling
- [ ] Add OAuth integration (Google, GitHub)
- [ ] Write authentication tests

## Acceptance Criteria
- [ ] Users can log in with email/password
- [ ] JWT tokens expire after 24h
- [ ] OAuth integration works
- [ ] 90%+ test coverage
```

**Good Task with Subtasks** (Task #101):
```markdown
Title: Task: Design login UI components
Labels: task, plan-item, needs-subtasks

## Description
Create all UI components needed for user authentication

## Subtasks
- [ ] Create LoginForm component
- [ ] Create SignupForm component
- [ ] Add form validation
- [ ] Design password strength indicator
- [ ] Create forgot password UI
```

This creates 5 subtask issues automatically.

---

## Repository Purpose

This repository is a **Claude Code Skills factory** - a collection of example skills that demonstrate how to create specialized capabilities for Claude Code. Skills are folders with instructions and resources that Claude loads when relevant to the user's task.

**Key Point**: This is NOT a development project itself. It's a reference repository that users can customize and extend for their own projects. Focus on helping users understand, adapt, and create their own skills based on these examples.

## Repository Structure

```
claude-code-skills-factory/
├── claude-skills-instructions.md    # Full documentation from Anthropic blog post
├── claude-skills-examples/          # Example skills with implementation
│   ├── analyzing_financial_statements.md  # Skill: Financial ratio analysis
│   ├── calculate_ratios.py                # Implementation for ratios
│   ├── interpret_ratios.py                # Ratio interpretation logic
│   ├── creating-financial-models.md       # Skill: DCF & financial modeling
│   ├── dcf_model.py                       # DCF valuation engine
│   ├── sensitivity_analysis.py            # Sensitivity testing framework
│   ├── brand_guidelines.md                # Skill: Corporate branding
│   └── apply_brand.py                     # Brand application module
├── documentation/
│   └── templates/
│       ├── SKILLS_FACTORY_PROMPT.md    # Template for generating Claude Skills
│       └── AGENTS_FACTORY_PROMPT.md    # Template for generating Claude Code agents
└── generated-skills/                   # Production-ready generated skills
    ├── aws-solution-architect/         # AWS architecture and IaC
    ├── content-trend-researcher/       # Content research and trend analysis
    ├── ms365-tenant-manager/           # Microsoft 365 administration
    ├── psychology-advisor/             # Mental wellness and CBT techniques
    ├── agent-factory/                  # Claude Code agent generation system
    └── prompt-suite/                   # World-class prompt generation (69 presets)
```

## Skill Architecture

Each skill follows a standard pattern:

### Skill Definition (.md file)
- **Frontmatter**: `name` and `description` in YAML format
- **Capabilities**: What the skill can do
- **Input Requirements**: What data/format is needed
- **Output Formats**: What the skill produces
- **Scripts**: Python files that implement functionality
- **Best Practices**: Guidelines for using the skill

### Implementation (.py files)
- **Class-based structure**: Main class encapsulates functionality
- **Type hints**: Full typing for clarity and IDE support
- **Safe operations**: Error handling (e.g., `safe_divide` to avoid division by zero)
- **Modular design**: Separate concerns (calculate vs interpret, model vs analyze)

## Example Skills Included

### 1. Analyzing Financial Statements
- **Files**: `analyzing_financial_statements.md`, `calculate_ratios.py`, `interpret_ratios.py`
- **Purpose**: Calculate and interpret financial ratios (profitability, liquidity, leverage, efficiency, valuation)
- **Key Class**: `FinancialRatioCalculator` - accepts financial statement data, calculates all major ratios
- **Pattern**: Calculation engine + interpretation layer

### 2. Creating Financial Models
- **Files**: `creating-financial-models.md`, `dcf_model.py`, `sensitivity_analysis.py`
- **Purpose**: DCF valuation, Monte Carlo simulation, sensitivity analysis, scenario planning
- **Key Class**: `DCFModel` - builds complete discounted cash flow models
- **Pattern**: Historical data → projections → valuation with multiple analysis methods

### 3. Applying Brand Guidelines
- **Files**: `brand_guidelines.md`, `apply_brand.py`
- **Purpose**: Apply consistent corporate branding to documents (colors, fonts, layouts)
- **Key Class**: `BrandFormatter` - applies Acme Corporation brand standards
- **Pattern**: Brand definition (colors, fonts, layouts) + application logic

## Generated Skills (Production-Ready)

The `generated-skills/` folder contains complete, production-ready skills created using the Skills Factory Prompt:

### 4. AWS Solution Architect
- **Files**: `SKILL.md`, `architecture_designer.py`, `cost_optimizer.py`, `serverless_stack.py`
- **Purpose**: Expert AWS architecture design for startups - serverless, scalable, cost-effective infrastructure
- **Key Classes**: `ArchitectureDesigner`, `CostOptimizer`, `ServerlessStackBuilder`
- **Pattern**: Architecture design → IaC templates → cost optimization

### 5. Content Trend Researcher
- **Files**: `SKILL.md`, `trend_analyzer.py`, `intent_analyzer.py`, `platform_insights.py`, `outline_generator.py`
- **Purpose**: Multi-platform trend analysis and data-driven content outline generation
- **Key Classes**: `TrendAnalyzer`, `IntentAnalyzer`, `PlatformInsights`, `OutlineGenerator`
- **Pattern**: Trend analysis → intent analysis → content gap discovery → outline generation

### 6. Microsoft 365 Tenant Manager
- **Files**: `SKILL.md`, `tenant_setup.py`, `user_management.py`, `powershell_generator.py`
- **Purpose**: Comprehensive M365 tenant administration and PowerShell automation
- **Key Classes**: `TenantManager`, `UserLifecycle`, `PowerShellScriptGenerator`
- **Pattern**: Configuration requirements → PowerShell scripts → validation checklists

### 7. Psychology Advisor
- **Files**: `SKILL.md`, `cbt_techniques.py`, `mindfulness_tools.py`, `stress_assessment.py`
- **Purpose**: Evidence-based psychological advisory with CBT techniques, mindfulness exercises, and stress management
- **Key Classes**: `CBTTechniques`, `MindfulnessTools`, `StressAssessment`
- **Pattern**: Cognitive distortion detection → thought reframing → coping strategies → practice plans

### 8. Content Trend Researcher
- **Files**: `SKILL.md`, `trend_analyzer.py`, `intent_analyzer.py`, `platform_insights.py`, `outline_generator.py`
- **Purpose**: Multi-platform trend analysis (Google, Reddit, YouTube, Medium, LinkedIn, X, etc.) and data-driven article outline generation
- **Key Classes**: `TrendAnalyzer`, `IntentAnalyzer`, `PlatformInsights`, `OutlineGenerator`
- **Pattern**: Platform trend analysis → user intent analysis → content gaps → SEO-optimized outlines

### 9. Agent Factory
- **Files**: `SKILL.md`, `agent_generator.py`
- **Purpose**: Generate custom Claude Code agents/sub-agents with enhanced YAML frontmatter, tool patterns, and MCP integration
- **Key Classes**: `AgentGenerator`
- **Pattern**: Agent requirements → YAML validation → agent .md file generation
- **Template**: Uses `documentation/templates/AGENTS_FACTORY_PROMPT.md` for generation

### 10. Prompt Suite
- **Files**: `SKILL.md`, `generate_prompt.py`, `validator.py`, `optimizer.py`, `batch_generator.py`
- **Purpose**: World-class prompt powerhouse generating production-ready mega-prompts for any role, industry, and task through intelligent question flow
- **Key Classes**: `PromptGenerator`, `PromptValidator`, `PromptOptimizer`, `BatchPromptGenerator`
- **Pattern**: 7-question flow → preset selection (69 presets, 15 domains) → quality validation → multi-format output (XML/Claude/ChatGPT/Gemini)
- **Coverage**: 69 comprehensive presets across Technical, Business, Legal, Finance, HR, Design, Customer, Executive, Manufacturing, R&D, Regulatory, Specialized-Technical, Research, Creative-Media domains

## Common Development Patterns

### 1. Data Structure
Skills use dictionaries for flexible data input:
```python
financial_data = {
    'income_statement': {...},
    'balance_sheet': {...},
    'cash_flow': {...},
    'market_data': {...}
}
```

### 2. Safe Operations
All calculations use safe divide patterns:
```python
def safe_divide(self, numerator: float, denominator: float, default: float = 0.0) -> float:
    if denominator == 0:
        return default
    return numerator / denominator
```

### 3. Type Annotations
Full typing for clarity:
```python
def calculate_profitability_ratios(self) -> Dict[str, float]:
```

### 4. Configuration Constants
Brand/style information stored as class constants:
```python
COLORS = {
    'primary': {'acme_blue': {'hex': '#0066CC', 'rgb': (0, 102, 204)}},
    ...
}
```

## How Skills Work

1. **Skill Discovery**: Claude scans available skills based on task description
2. **Minimal Loading**: Only loads necessary files when skill matches
3. **Execution**: Runs Python scripts using Claude's code execution environment
4. **Composability**: Multiple skills can work together
5. **Portability**: Same skill works across Claude apps, Claude Code, and API

## Customization Guidelines

When helping users adapt these skills:

1. **Modify the frontmatter**: Change `name` and `description` to match their use case
2. **Update brand constants**: Replace Acme Corporation with their company details
3. **Adjust calculations**: Modify ratio calculations or financial assumptions for their industry
4. **Add new capabilities**: Extend classes with additional methods
5. **Simplify**: Remove unnecessary features they won't use

## Key Principles

- **Don't overengineer**: Skills should be as simple as possible while solving the problem
- **Edit existing**: When making changes, prefer editing existing skill files over creating new ones
- **Validate inputs**: Always check for missing/invalid data before calculations
- **Document assumptions**: Financial models especially need clear assumption documentation
- **Industry context**: Many calculations (ratios, valuations) require industry-specific interpretation

## Templates for Generation

The `documentation/templates/` folder contains two powerful prompt templates:

### SKILLS_FACTORY_PROMPT.md
- **Purpose**: Generate complete Claude Skills (folders with SKILL.md + Python files)
- **Use for**: Creating capabilities like financial analysis, content research, data processing
- **Output**: Skill folders with SKILL.md, Python files, samples, and ZIP files
- **Location**: Skills go in `.claude/skills/` or `~/.claude/skills/`

### AGENTS_FACTORY_PROMPT.md
- **Purpose**: Generate Claude Code agents/sub-agents (single .md files)
- **Use for**: Creating specialized agents like code reviewers, developers, testers
- **Output**: Agent .md files with enhanced YAML frontmatter (color, field, expertise, MCP tools)
- **Location**: Agents go in `.claude/agents/` or `~/.claude/agents/`

**Key Difference:**
- **Skills** = Multi-file capabilities (folders)
- **Agents** = Single-file specialists (.md only)

## Installation

Users can install these skills and agents:

**Skills**:
- **Claude Code**: Copy skill folder to `~/.claude/skills/`
- **Claude Apps**: Use the "skill-creator" skill to import
- **API**: Use the `/v1/skills` endpoint

**Agents**:
- **Claude Code Project**: Copy .md file to `.claude/agents/`
- **Claude Code Personal**: Copy .md file to `~/.claude/agents/`
- **CLI**: Use `--agents` flag for session-specific agents

## References

- Full documentation: [claude-skills-instructions.md](claude-skills-instructions.md)
- Anthropic Skills docs: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- Skills marketplace: https://github.com/anthropics/skills
