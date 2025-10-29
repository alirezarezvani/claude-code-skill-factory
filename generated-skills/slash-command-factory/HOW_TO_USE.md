# How to Use Slash Command Factory

Generate custom Claude Code slash commands in minutes!

---

## Quick Start

### Use a Preset (30 seconds)

```
@slash-command-factory

Use the /research-business preset
```

→ Instant business research command ready to install

### Create Custom Command (2-3 minutes)

```
@slash-command-factory

Create a command for analyzing customer feedback and generating product insights
```

→ Answers 5-7 questions → Complete custom command generated

---

## 10 Available Presets

1. **/research-business** - Market research, competitor SWOT, strategic insights
2. **/research-content** - Multi-platform trends, SEO strategy, content gaps
3. **/medical-translate** - Medical terms → 8th grade (DE/EN)
4. **/compliance-audit** - HIPAA/GDPR/DSGVO validation
5. **/api-build** - Complete API client with tests
6. **/test-auto** - Auto-generate test suites
7. **/docs-generate** - Documentation automation
8. **/knowledge-mine** - Extract insights from documents
9. **/workflow-analyze** - Process optimization
10. **/batch-agents** - Multi-agent coordination

---

## Official Command Structures

This skill uses **three official patterns** from Anthropic documentation:

### Simple Pattern (code-review)
- **Best for**: Straightforward tasks with clear input/output
- **Structure**: Context → Task
- **Example Presets**: code-review, deps-audit, metrics-report

### Multi-Phase Pattern (codebase-analyze)
- **Best for**: Complex discovery and documentation
- **Structure**: Discovery → Analysis → Task
- **Example Preset**: codebase-analyze

### Agent-Style Pattern (ultrathink)
- **Best for**: Specialized expert roles and coordination
- **Structure**: Role → Process → Guidelines
- **Example Presets**: ultrathink, openapi-sync, batch-agents

**The skill auto-detects** which pattern fits your command purpose!

---

## Naming Convention

All commands follow **kebab-case** (lowercase with hyphens):

**Valid**:
- ✅ `code-review`
- ✅ `api-document`
- ✅ `update-docs`

**Invalid**:
- ❌ `code_review` (underscores)
- ❌ `CodeReview` (CamelCase)
- ❌ `review` (too short)

The skill **automatically converts** your purpose to valid command names!

---

## Installation

**After generation**, commands are in: `generated-commands/[command-name]/`

**To install**:

**Project-level** (this project only):
```bash
cp generated-commands/[command-name]/[command-name].md .claude/commands/
```

**User-level** (all projects):
```bash
cp generated-commands/[command-name]/[command-name].md ~/.claude/commands/
```

**Then**: Restart Claude Code

---

## Usage Examples

### Business Research Command

```
@slash-command-factory
Use /research-business preset

[Command generated: generated-commands/research-business/]

# Install
cp generated-commands/research-business/research-business.md .claude/commands/

# Use
/research-business "Tesla" "EV market"
```

### Custom Healthcare Command

```
@slash-command-factory
Create command for German PTV 10 application generation

Q1: Purpose? Generate PTV 10 therapy applications
Q2: Tools? Read, Write, Task
Q3: Agents? Yes - health-sdk-builder agents
Q4: Output? Files
Q5: Model? Sonnet

[Command generated: generated-commands/generate-ptv10/]

# Install
cp generated-commands/generate-ptv10/generate-ptv10.md .claude/commands/

# Use
/generate-ptv10 "Patient info" "60 sessions"
```

---

## Output Structure

**Simple command**:
```
generated-commands/my-command/
├── my-command.md         # The command file
└── README.md             # Installation guide
```

**Complex command**:
```
generated-commands/my-command/
├── my-command.md         # Command (ROOT)
├── README.md             # Install guide (ROOT)
├── TEST_EXAMPLES.md     # Testing (ROOT)
├── standards/            # Standards folder
├── examples/             # Examples folder
└── scripts/              # Helper scripts
```

**Organization**: All .md in root, folders separate

---

## Testing Generated Commands

```bash
# After installation
/my-command test-arguments

# Check it works as expected
```

See TEST_EXAMPLES.md in each command folder for specific test cases.

---

## Tips

- Use presets for speed (30 seconds)
- Custom for unique needs (2-3 minutes)
- Always validate before installing
- Test with simple cases first
- Customize .md files if needed

---

**Generate powerful slash commands in minutes!** ⚡
