# Prompt Factory - Comprehensive User Guide

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Path 1: Quick-Start Presets](#path-1-quick-start-presets)
4. [Path 2: Custom Prompts](#path-2-custom-prompts)
5. [Output Formats Explained](#output-formats-explained)
6. [Core vs Advanced Mode](#core-vs-advanced-mode)
7. [Complete Examples](#complete-examples)
8. [Python Scripts Usage](#python-scripts-usage)
9. [Tips & Best Practices](#tips--best-practices)
10. [Troubleshooting](#troubleshooting)

---

## Overview

**Prompt Factory** is your one-stop solution for creating world-class AI prompts without iteration. Whether you're building prompts for technical development, business strategy, creative work, or specialized domains, Prompt Factory delivers production-ready results in under 2 minutes.

### Key Features

✅ **Max 7 questions** - Get to results fast with smart questioning
✅ **69 quick-start presets** - One-click prompts across 15 professional domains
✅ **Multi-format output** - XML, Claude, ChatGPT, Gemini formats
✅ **Quality validation** - 7-point validation before delivery
✅ **Best practices** - Auto-applied from OpenAI, Anthropic, Google
✅ **15,000+ combinations** - Any role × industry × task

### Relationship to PROMPTS_FACTORY_PROMPT.md

**Quick Decision Guide:**

- **Need one prompt now?** → Use this skill (**Prompt Factory**)
  - Generates individual mega-prompts for specific roles
  - Example: "Create a prompt for a Growth Hacker" → One ready-to-use prompt

- **Building a prompt system for a new domain?** → Use **PROMPTS_FACTORY_PROMPT.md**
  - Meta-prompt that generates domain-specific prompt builders
  - Example: "Generate a FinTech Prompt Builder" → Complete system with 10-20 FinTech role presets
  - Location: `documentation/templates/PROMPTS_FACTORY_PROMPT.md`

---

## Quick Start

### 30-Second Start

**Want a preset?**
```
"I need a prompt for Senior Full-Stack Engineer"
```
→ Get customizable template immediately

**Want custom?**
```
"Help me create a prompt for [your role/need]"
```
→ Answer max 7 questions → Get validated prompt

---

## Path 1: Quick-Start Presets

### When to Use Presets

Use presets when you need a prompt for:
- **Common technical roles** (developer, architect, ML engineer, etc.)
- **Standard business roles** (product manager, marketer, analyst, etc.)
- **Creative positions** (designer, writer, strategist, etc.)
- **Specialized domains** (healthcare, fintech, legal, etc.)

### How to Use Presets

#### Step 1: Request a Preset

**Simple format:**
```
"Use the [preset name] preset"
```

**Examples:**
- "Use the Senior Full-Stack Engineer preset"
- "I need the Marketing Strategist preset"
- "Load the DevOps Engineer template"

#### Step 2: Review & Customize (Optional)

The skill will show you:
```
📋 **[Preset Name] Preset Loaded**

**Default Configuration:**
- Role: [role name]
- Domain: [default domain]
- Tech Stack: [default stack]
- Output Type: [default type]
- Style: [default style]

**Customization Options:**
1. Use as-is (press Enter)
2. Customize variables (answer questions below)

Would you like to customize? (yes/no)
```

#### Step 3: Select Format & Mode

```
**Select output format:**
1. xml (default)
2. claude
3. chatgpt
4. gemini
5. all

**Select mode:**
1. core (default)
2. advanced

Your choices: ___
```

#### Step 4: Get Your Prompt

The skill generates and validates your prompt, then delivers it ready to use.

### Available Presets

**Total Presets:** 69 across 15 professional domains

Below are highlighted examples. For the complete list of all 69 presets, see [SKILL.md](SKILL.md#available-presets-69-total).

#### Technical Presets (8 total - showing 5 examples)

**1. Senior Full-Stack Engineer**
- **Stack:** React, Node.js, PostgreSQL, AWS
- **Best for:** Web application development, API design, full-stack projects
- **Output:** Production-ready code with tests

**2. ML Engineer**
- **Stack:** Python, PyTorch/TensorFlow, MLOps tools
- **Best for:** Machine learning pipelines, model training, deployment
- **Output:** ML code, experiments, production pipelines

**3. DevOps Engineer**
- **Stack:** AWS/GCP/Azure, Kubernetes, Terraform, CI/CD
- **Best for:** Infrastructure automation, deployments, reliability
- **Output:** IaC templates, pipeline configs, documentation

**4. Mobile Engineer**
- **Stack:** React Native, Flutter, iOS/Android native
- **Best for:** Cross-platform mobile apps, native features
- **Output:** Mobile app code, platform-specific solutions

**5. Solutions Architect**
- **Stack:** Cloud platforms, enterprise systems, scalability patterns
- **Best for:** System architecture, technical strategy, scaling
- **Output:** Architecture diagrams, technical specs, decisions

#### Business Presets (8 total - showing 4 examples)

**6. Product Manager**
- **Focus:** Tech product strategy, roadmaps, user stories
- **Best for:** Product planning, requirement docs, prioritization
- **Output:** PRDs, roadmaps, user stories, strategies

**7. Marketing Strategist**
- **Focus:** B2B SaaS growth, digital marketing, content strategy
- **Best for:** Marketing campaigns, growth strategies, content plans
- **Output:** Marketing strategies, campaign plans, content calendars

**8. Business Analyst**
- **Focus:** Data-driven analysis, requirements gathering, business strategy
- **Best for:** Business analysis, requirements, process improvement
- **Output:** Analysis reports, requirements docs, recommendations

**9. Operations Manager**
- **Focus:** Process optimization, efficiency, operational excellence
- **Best for:** Process design, operational improvements, workflows
- **Output:** Process docs, optimization plans, SOPs

#### Creative & Design Presets (multiple domains - showing 3 examples)

**10. Content Strategist**
- **Focus:** SEO optimization, multi-channel content, audience targeting
- **Best for:** Content marketing, editorial planning, SEO strategy
- **Output:** Content strategies, editorial calendars, SEO plans

**11. UX Designer**
- **Focus:** User-centered design, accessibility, design systems
- **Best for:** UX research, interface design, user flows
- **Output:** Design specs, user flows, accessibility guidelines

**12. Technical Writer**
- **Focus:** API documentation, developer guides, technical content
- **Best for:** Documentation projects, technical writing, guides
- **Output:** Documentation, API references, tutorials

#### Specialized Industry Presets (Legal, Finance, Healthcare, etc. - showing 3 examples)

**13. Healthcare Tech Consultant**
- **Focus:** HIPAA compliance, clinical systems, health data
- **Best for:** Healthcare software, medical devices, compliance
- **Output:** Compliant solutions, healthcare architecture, docs

**14. FinTech Advisor**
- **Focus:** Financial compliance, payment systems, trading platforms
- **Best for:** Financial applications, payment processing, compliance
- **Output:** Compliant financial solutions, architecture, specs

**15. Legal Tech Specialist**
- **Focus:** Contract analysis, legal compliance, regulatory systems
- **Best for:** Legal software, compliance tools, contract management
- **Output:** Legal tech solutions, compliance frameworks, analysis

---

## Path 2: Custom Prompts

### When to Use Custom Path

Use custom creation when:
- Your role doesn't match any preset
- You need a highly specialized prompt
- You're combining multiple domains
- Your use case is unique

### The 7-Question Flow

The skill asks **maximum 7 questions** with example answers to guide you.

#### Example Session: Creating a Custom Prompt

**User says:**
```
"I need a custom prompt for analyzing cryptocurrency trading patterns"
```

**Skill responds:**
```
I'll create a custom prompt for you! Please answer these questions (max 7):

**1. What role should the AI assume?**
*Examples:*
- "Senior Backend Engineer"
- "Marketing Growth Strategist"
- "Data Analyst"
- "Product Manager"

Your answer: Cryptocurrency Trading Analyst

**2. What domain or industry context?**
*Examples:*
- "FinTech / Payment Processing"
- "Healthcare SaaS"
- "E-commerce Platform"

Your answer: Cryptocurrency Trading / DeFi

**3. What is the primary task or goal?**
*Examples:*
- "Build REST APIs for payment processing"
- "Create content marketing strategies"
- "Analyze user behavior data"

Your answer: Analyze on-chain data and trading patterns to identify opportunities

**4. What output format do you need?**
*Options:* code | documentation | strategy | analysis | design | plan

Your answer: analysis

**5. Tech stack, tools, or methodologies to use/follow?**
*Examples:*
- "Python, FastAPI, PostgreSQL, AWS"
- "React, TypeScript, Next.js"
- "SEO best practices, Google Analytics"

Your answer: Python, pandas, web3.py, TradingView, technical analysis

**6. Any critical constraints or requirements?**
*Examples:*
- "HIPAA compliant, healthcare regulations"
- "Budget < $10k, 2-week timeline"
- "Must support 10k+ concurrent users"

Your answer: Risk management focus, backtesting required, real-time analysis

**7. Communication style and response format?**
*Options:*
- Tone: Professional / Technical / Casual / Academic
- Style: Concise / Detailed / Step-by-step / Conceptual
- Format: Prose / Bullets / Mixed / Code-heavy
- Depth: High-level / Moderate / Deep-technical / Implementation-ready

Your answer: Technical tone, detailed style, mixed format, deep-technical depth

---

✅ All questions answered! Now select output format and mode...

**Select output format:**
1. xml (default)
2. claude
3. chatgpt
4. gemini
5. all

Your choice: 1

**Select generation mode:**
1. core (default)
2. advanced

Your choice: 2

---

🔄 Generating your advanced mega-prompt...
✓ Template synthesized
✓ Best practices applied
✓ Quality validation passed (7/7 gates)
✓ Generated successfully

[PROMPT DELIVERED]
```

### Smart Question Adaptation

The skill intelligently adapts questions based on your answers:

**If you mention tech stack in Q3:**
- Skips Q5 (tech stack question)

**If domain is obvious from role:**
- Skips Q2 (domain question)

**If no special constraints needed:**
- Skips Q6 (constraints question)

**Result:** Often 5-6 questions instead of 7!

---

## Output Formats Explained

### Format 1: XML (Default - Recommended)

**Best for:** All LLMs, maximum compatibility, clear structure

**Structure:**
```xml
<mega_prompt>
  <role>...</role>
  <mission>...</mission>
  <context>...</context>
  <workflow>...</workflow>
  <output_specifications>...</output_specifications>
  <communication_guidelines>...</communication_guidelines>
  <best_practices>...</best_practices>
  <critical_instructions>...</critical_instructions>
  <examples>...</examples>
  <execution_trigger>...</execution_trigger>
</mega_prompt>
```

**How to use:**
1. Copy entire `<mega_prompt>` block
2. Paste into your LLM conversation
3. Follow with your specific request
4. LLM responds according to prompt

**Pros:**
- ✅ Clear hierarchical structure
- ✅ Easy to modify specific sections
- ✅ Works with all LLMs
- ✅ Optimal for LLM parsing

---

### Format 2: Claude System Prompt

**Best for:** Claude conversations, system-level configuration

**Structure:**
```markdown
# System Configuration: [Role]

You are [role]...

## Your Expertise
[...]

## Your Workflow
[...]

## Output Standards
[...]

Execute your role now.
```

**How to use:**
1. Copy entire prompt
2. Paste as system prompt or start of conversation
3. Claude maintains this configuration throughout
4. Optimal for long conversations

**Pros:**
- ✅ Optimized for Claude's format preferences
- ✅ Natural language structure
- ✅ Great for extended conversations

---

### Format 3: ChatGPT Custom Instructions

**Best for:** ChatGPT persistent configuration

**Structure:**
```
**What would you like ChatGPT to know about you?**
[Context about user and domain]

**How would you like ChatGPT to respond?**
[Workflow, requirements, rules]
```

**How to use:**
1. Go to ChatGPT Settings → Personalization → Custom Instructions
2. Paste first section in "What would you like..." box
3. Paste second section in "How would you like..." box
4. Save - applies to all conversations

**Pros:**
- ✅ Persistent across all chats
- ✅ No need to re-paste
- ✅ Fits ChatGPT's UI perfectly

---

### Format 4: Gemini Format

**Best for:** Google Gemini conversations

**Structure:**
```markdown
## Role Configuration
You are: [role]

## Task Approach
[workflow]

## Output Format
[format specs]

Apply this to all responses.
```

**How to use:**
1. Copy entire prompt
2. Paste at start of Gemini conversation
3. Gemini maintains configuration
4. Optimized for Gemini's style

**Pros:**
- ✅ Streamlined for Gemini
- ✅ Concise format
- ✅ Quick setup

---

### Format 5: All Formats

**Best for:** Testing across LLMs, team distribution

Generates all 4 formats in one delivery:
- XML version
- Claude version
- ChatGPT version
- Gemini version

**Use case:** Share with team using different LLMs

---

## Core vs Advanced Mode

### Core Mode (Default)

**What you get:**
- ✅ Complete mega-prompt (~5K tokens)
- ✅ Usage instructions for your chosen format
- ✅ 2-3 example interactions showing expected behavior
- ✅ Quick customization notes

**Best for:**
- Most use cases
- Quick turnaround
- Standard requirements
- Token efficiency

**Delivery time:** < 1 minute

---

### Advanced Mode

**What you get (Core PLUS):**
- ✅ Everything in Core mode
- ✅ **5 testing scenarios** - Validate prompt behavior
- ✅ **3 prompt variations** - Concise, Balanced, Comprehensive
- ✅ **Optimization tips** - Token reduction, clarity improvements
- ✅ **Iteration guidelines** - How to refine the prompt

**Best for:**
- Critical use cases
- Complex requirements
- Team-wide deployment
- Quality assurance needed

**Delivery time:** ~2 minutes

---

### Advanced Mode Components Explained

#### Testing Scenarios

**Purpose:** Validate your prompt works as expected

**Example:**
```xml
<testing_scenarios>
## Test Case 1: Simple Request
**Input:** "Create a REST API endpoint for user authentication"
**Expected Behavior:**
- Analyzes authentication requirements
- Designs endpoint structure
- Implements with proper security
- Includes tests and documentation
**Success Criteria:**
- Code is production-ready
- Security best practices applied
- Tests pass

[4 more test cases covering edge cases, errors, performance]
</testing_scenarios>
```

**How to use:**
1. Test your prompt with each scenario
2. Verify expected behavior matches actual
3. If gaps found, refine specific prompt sections
4. Re-test until all scenarios pass

---

#### Prompt Variations

**Purpose:** Choose the right prompt size for your needs

**Variation 1: Concise (~3K tokens)**
- Minimal version
- Essential instructions only
- Fast, token-efficient
- Use when: Token limits tight, simple use cases

**Variation 2: Balanced (~5K tokens)** ← DEFAULT
- Standard version
- Core guidance included
- Good balance of detail and efficiency
- Use when: Most scenarios

**Variation 3: Comprehensive (~8K tokens)**
- Detailed version
- Extensive examples and edge cases
- Maximum guidance
- Use when: Complex/critical use cases, training

**How to choose:**
Start with Balanced. Switch to Concise if you hit token limits. Use Comprehensive for mission-critical applications.

---

#### Optimization Tips

**Purpose:** Improve your prompt after initial use

**Example:**
```xml
<optimization_tips>
## Token Optimization
- Current count: ~5,200 tokens
- Opportunities:
  1. Merge similar workflow steps → Save ~200 tokens
  2. Consolidate examples → Save ~150 tokens
  3. Simplify constraint descriptions → Save ~100 tokens

## Clarity Improvements
- Potential ambiguities:
  1. "Handle errors appropriately" → Specify error categories and responses
  2. "Use best practices" → List specific practices to follow

## Effectiveness Enhancements
- Consider adding:
  1. More specific examples for complex scenarios
  2. Common pitfall warnings
  3. Performance benchmarks

## Iteration Guidelines
After testing:
1. Note which responses meet expectations
2. Identify consistent gaps
3. Refine specific sections (not wholesale rewrites)
4. Test refined version with same scenarios
5. Save successful versions
</optimization_tips>
```

**How to use:**
1. Use prompt for 5-10 real queries
2. Note what works and what doesn't
3. Apply suggested optimizations
4. Re-test with same queries
5. Compare results

---

## Complete Examples

### Example 1: Quick Preset Usage

**Scenario:** Need a prompt for backend API development

**User:**
```
"Use the Senior Full-Stack Engineer preset"
```

**Skill:**
```
📋 **Senior Full-Stack Engineer Preset Loaded**

**Default Configuration:**
- Role: Senior Full-Stack Engineer
- Stack: React, Node.js, PostgreSQL, AWS
- Domain: Web Application Development
- Output: Production-ready code with tests
- Style: Technical, detailed, implementation-ready

Would you like to customize? (yes/no): no

**Select output format:** xml
**Select mode:** core

🔄 Generating...
✓ Preset customized
✓ Best practices applied
✓ Quality validated (7/7)

✅ **Your core mega-prompt is ready!**

[Full XML prompt delivered here]

**Usage:**
Copy the <mega_prompt> block and paste into your LLM...
```

**Time:** 30 seconds

---

### Example 2: Custom Prompt Creation

**Scenario:** Building AI for legal document analysis

**User:**
```
"Create a custom prompt for analyzing legal contracts"
```

**Skill asks 7 questions:**
1. Role: Legal AI Specialist
2. Domain: Contract Law / Legal Tech
3. Goal: Analyze contracts, identify risks, suggest revisions
4. Output: analysis
5. Stack: NLP, GPT-4, legal databases
6. Constraints: Must cite relevant laws, highlight compliance issues
7. Style: Professional, detailed, structured, implementation-ready

**Format:** xml
**Mode:** advanced

**Result:**
- Complete XML prompt
- 5 testing scenarios (simple contract, complex M&A deal, etc.)
- 3 variations (3K, 5K, 8K tokens)
- Optimization tips
- Iteration guidelines

**Time:** 2 minutes

---

### Example 3: Team-Wide Rollout

**Scenario:** Marketing team needs standardized AI assistance

**User:**
```
"Use Marketing Strategist preset, generate for all formats, advanced mode"
```

**Result:**
- XML version (for technical team)
- Claude version (for Claude users)
- ChatGPT version (for ChatGPT users)
- Gemini version (for Gemini users)
- Testing scenarios for team validation
- 3 variations for different use cases

**Distribution:**
- Technical marketers: Use XML or Claude format
- Content writers: Use ChatGPT custom instructions
- Analysts: Use Gemini format
- All get same core guidance, format optimized

**Time:** 2.5 minutes

---

## Python Scripts Usage

### Script 1: generate_prompt.py

**Purpose:** Generate prompts programmatically

**Usage:**
```bash
python scripts/generate_prompt.py \
  --responses responses.json \
  --format xml \
  --mode core \
  --output my-prompt.md
```

**responses.json example:**
```json
{
  "role": "Senior Data Engineer",
  "role_context": "specializing in real-time data pipelines",
  "domain": "E-commerce Analytics",
  "goal": "build scalable data pipelines for analytics",
  "output_type": "code",
  "success_criteria": "Handles 10K events/sec, 99.9% uptime",
  "tech_stack": "Python, Apache Kafka, Spark, AWS",
  "constraints": "Must be cost-effective, < $5K/month AWS",
  "must_avoid": "Vendor lock-in, over-engineering",
  "target_audience": "advanced",
  "tone": "technical",
  "detail_level": "implementation-ready",
  "format_preference": "mixed"
}
```

**Output:** Complete prompt in `my-prompt.md`

---

### Script 2: batch_generator.py

**Purpose:** Generate multiple prompts at once

**Usage:**
```bash
python scripts/batch_generator.py \
  --input team-prompts.csv \
  --format xml \
  --mode core \
  --output-dir ./team-prompts/
```

**team-prompts.csv example:**
```csv
name,role,domain,goal,output_type,tech_stack
backend-api,Senior Backend Engineer,FinTech,Build secure APIs,code,"Python,FastAPI,PostgreSQL"
frontend-ui,Senior Frontend Engineer,FinTech,Build responsive UIs,code,"React,TypeScript,Tailwind"
data-analyst,Data Analyst,FinTech,Analyze user behavior,analysis,"Python,pandas,SQL"
```

**Output:** 3 prompts in `./team-prompts/` directory

**Use case:** Onboard entire team with standardized prompts

---

### Script 3: validator.py

**Purpose:** Validate prompt quality

**Usage:**
```bash
python scripts/validator.py \
  --prompt my-existing-prompt.md \
  --report validation-report.json
```

**validation-report.json example:**
```json
{
  "overall_score": 6,
  "passed": false,
  "checks": {
    "xml_structure": {"passed": true, "score": 1},
    "completeness": {"passed": true, "score": 1},
    "token_count": {"passed": true, "score": 1, "count": 4856},
    "no_placeholders": {"passed": false, "score": 0, "issues": ["Found [TODO] at line 45"]},
    "actionable_workflow": {"passed": true, "score": 1},
    "best_practices": {"passed": true, "score": 1},
    "examples_present": {"passed": true, "score": 1}
  },
  "recommendations": [
    "Replace [TODO] placeholder at line 45 with actual content"
  ]
}
```

**Action:** Fix issues, re-run validator until 7/7 pass

---

### Script 4: optimizer.py

**Purpose:** Optimize existing prompts

**Usage:**
```bash
python scripts/optimizer.py \
  --prompt my-prompt.md \
  --target-tokens 4000 \
  --output optimized-prompt.md \
  --report optimization-report.json
```

**What it does:**
1. Analyzes current prompt
2. Identifies redundancies
3. Suggests consolidations
4. Rewrites for token efficiency
5. Validates quality maintained

**optimization-report.json example:**
```json
{
  "original_tokens": 6234,
  "optimized_tokens": 4012,
  "reduction": "35.6%",
  "changes": [
    "Merged 3 similar workflow steps",
    "Consolidated 4 examples into 2",
    "Simplified constraint descriptions",
    "Removed redundant best practices"
  ],
  "quality_maintained": true,
  "validation_score": "7/7"
}
```

---

## Tips & Best Practices

### Getting the Best Results

#### Tip 1: Be Specific in Questionnaire
**❌ Bad:**
- Role: "Developer"
- Goal: "Write code"

**✅ Good:**
- Role: "Senior Backend Engineer specializing in payment systems"
- Goal: "Build secure, PCI-compliant REST APIs for payment processing with sub-100ms latency"

**Why:** Specificity leads to contextual best practices and relevant examples.

---

#### Tip 2: Include Critical Constraints Early
**❌ Bad:**
- Constraints: "Make it good"

**✅ Good:**
- Constraints: "PCI-DSS Level 1 compliance required, 99.99% uptime SLA, <100ms API response time, budget $8K/month AWS"

**Why:** Constraints guide architecture decisions and best practices selection.

---

#### Tip 3: Use Presets as Starting Points
**Instead of:** Custom from scratch for common roles

**Do this:** Start with preset, customize variables

**Example:**
```
"Use DevOps Engineer preset, but change domain to Healthcare and add HIPAA compliance constraint"
```

**Why:** Faster + battle-tested foundation

---

#### Tip 4: Start with Core Mode
**For first use:** Always use core mode

**Switch to advanced when:**
- Deploying to production
- Training a team
- Mission-critical application
- Need comprehensive testing

**Why:** Iterative refinement is more effective than over-engineering upfront

---

#### Tip 5: Test with Real Scenarios
**After receiving prompt:**
1. Test with 3-5 actual queries you'll use
2. Note what works and what doesn't
3. Request specific refinements (not wholesale rewrite)
4. Re-test with same queries

**Example refinement request:**
```
"The prompt works well but responses are too verbose.
Adjust communication_guidelines to be more concise."
```

**Why:** Specific iterations > starting over

---

### Common Pitfalls to Avoid

#### Pitfall 1: Over-Specifying in Questionnaire
**Problem:** Answering every question with paragraphs of detail

**Solution:** Concise answers with key points only

**Example:**
- ❌ "I need the AI to understand that in our company we use React with TypeScript and we have a design system called Acme UI which uses Tailwind and we follow Atomic Design principles and we use Storybook for component documentation and Jest for testing and..."
- ✅ "React, TypeScript, Tailwind, Design System (Atomic Design)"

---

#### Pitfall 2: Ignoring Example Answers
**Problem:** Not looking at example answers, giving unclear responses

**Solution:** Use examples as templates for your answers

**The skill provides examples for a reason!**

---

#### Pitfall 3: Requesting "All Formats" Without Need
**Problem:** Generating all formats when you only use one

**Solution:** Pick the format you'll actually use

**Exception:** Team rollout across different LLMs

---

#### Pitfall 4: Skipping Testing Scenarios
**Problem:** Not validating prompt works as expected

**Solution:** If using advanced mode, actually run the test scenarios

**Why:** Prevents surprises in production use

---

#### Pitfall 5: Wholesale Rewrites Instead of Refinements
**Problem:** "This doesn't work, regenerate everything"

**Solution:** "Section X needs adjustment: [specific change]"

**Example:**
- ❌ "Regenerate the entire prompt, it's not working"
- ✅ "The workflow section needs to emphasize security validation. Add a dedicated security review phase between design and execution."

---

## Troubleshooting

### Issue: Prompt Too Generic

**Symptom:** Responses lack domain-specific depth

**Cause:** Vague questionnaire answers

**Solution:**
1. Regenerate with more specific domain/industry
2. Add detailed constraints
3. Request advanced mode with comprehensive examples

**Example fix:**
```
"Regenerate with these changes:
- Domain: 'FinTech Payment Processing with PCI-DSS compliance'
- Add constraint: 'Must handle credit card data securely, tokenization required'
- Use advanced mode for compliance examples"
```

---

### Issue: Prompt Too Verbose

**Symptom:** Responses are overly detailed, hitting token limits

**Cause:** Using comprehensive variation or over-specified requirements

**Solution:**
1. Switch to concise variation
2. Use optimizer.py script to reduce tokens
3. Adjust communication_style to favor brevity

**Example fix:**
```
"The prompt is too detailed. Please:
1. Use the concise variation (3K tokens)
2. Change communication_style depth to 'moderate' instead of 'deep-technical'"
```

---

### Issue: Missing Domain-Specific Knowledge

**Symptom:** Responses lack industry-specific best practices

**Cause:** Domain not specific enough or missing constraints

**Solution:**
1. Specify exact sub-domain
2. Add industry regulations as constraints
3. Request advanced mode for specialized examples

**Example fix:**
```
"Add these domain specifics:
- Sub-domain: 'Healthcare Telemedicine HIPAA-compliant systems'
- Constraint: 'BAA agreements required, PHI encryption at rest and transit'
- Add examples of HIPAA-compliant architecture patterns"
```

---

### Issue: Responses Don't Match Desired Style

**Symptom:** Tone or format doesn't match expectations

**Cause:** Communication guidelines not specific enough

**Solution:** Refine communication_guidelines section only

**Example fix:**
```
"Adjust communication_guidelines:
- Change tone from 'professional' to 'casual and friendly'
- Change format from 'mixed' to 'bullet-heavy'
- Add: 'Use analogies and metaphors to explain complex concepts'"
```

---

### Issue: XML Format Not Working

**Symptom:** LLM not parsing XML tags correctly

**Cause:** LLM preference or XML structure issue

**Solution:**
1. Regenerate in LLM-specific format (claude/chatgpt/gemini)
2. Validate XML structure with validator.py
3. Check for unclosed tags

**Example fix:**
```
"Regenerate in Claude format instead of XML"
```

---

### Issue: Validation Fails

**Symptom:** Quality validation reports issues

**Cause:** Placeholder text, missing sections, or structural problems

**Solution:**
1. Review validation report for specific issues
2. Run validator.py for detailed analysis
3. Request regeneration with fixes

**Example:**
```
"Validation failed on:
- No placeholders check: Found [TODO] at line 45
- Examples present check: Only 1 example, need 2+

Please fix and regenerate."
```

---

### Issue: Preset Doesn't Match Need

**Symptom:** Closest preset is still too different

**Cause:** Unique combination not covered by presets

**Solution:** Use custom path instead

**When presets work:** 70%+ match
**When to go custom:** <70% match

---

### Getting Help

**If issues persist:**

1. **Check Examples:** Review `examples/` folder for similar use cases
2. **Read References:** Check `references/` for best practices
3. **Validate Prompt:** Run `validator.py` for specific issues
4. **Iterate Specifically:** Don't regenerate, refine sections
5. **Test with Scenarios:** Use testing scenarios from advanced mode

**Advanced support:**
- GitHub Issues: [repo link]
- Documentation: `references/` folder
- Community: [community link]

---

## Summary: Your Prompt Factory Workflow

### Simple 3-Step Process

**Step 1: Choose Path**
- **Preset?** → Pick from 15 templates → Customize → Generate
- **Custom?** → Answer 7 questions → Generate

**Step 2: Select Options**
- **Format:** xml / claude / chatgpt / gemini / all
- **Mode:** core / advanced

**Step 3: Use & Refine**
- Test with real queries
- Note what works
- Refine specific sections
- Save successful version

**Total time:** 1-2 minutes from start to production-ready prompt

---

**Ready to create world-class prompts? Let's begin!**
