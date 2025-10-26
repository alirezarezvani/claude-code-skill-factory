---
name: prompt-factory
description: World-class prompt powerhouse that generates production-ready mega-prompts for any role, industry, and task through intelligent 7-question flow, 69 comprehensive presets across 15 professional domains (technical, business, creative, legal, finance, HR, design, customer, executive, manufacturing, R&D, regulatory, specialized-technical, research, creative-media), multiple output formats (XML/Claude/ChatGPT/Gemini), quality validation gates, and contextual best practices from OpenAI/Anthropic/Google. Supports both core and advanced modes with testing scenarios and prompt variations.
---

# Prompt Factory - World-Class Prompt Powerhouse

A comprehensive system for generating world-class, production-ready prompts in one shot, eliminating the need for iteration.

---

## ⚠️ CRITICAL CONSTRAINTS - READ FIRST

**This skill generates PROMPTS only. It does NOT implement the work described in the prompt.**

### What This Skill DOES:
✅ Generate a comprehensive PROMPT (text document in chosen format)
✅ **Ask 5-7 questions to understand requirements** (MANDATORY - no skipping)
✅ Validate prompt quality before delivery
✅ Output a SINGLE prompt document with token count
✅ Provide the prompt ready to copy and use elsewhere

### What This Skill DOES NOT DO:
❌ Implement the actual work (no code files, no diagrams, no APIs)
❌ Create architectural diagrams or technical implementations
❌ Write actual marketing campaigns or business strategies
❌ Build infrastructure or deploy anything
❌ Create multiple files or deliverables
❌ Execute the prompt after generating it

### Expected Workflow:
1. User asks for help creating a prompt
2. **Skill MUST ask 5-7 questions** (even if context seems obvious)
3. User answers questions with specific details
4. Skill generates ONE comprehensive prompt document
5. Skill announces token count (e.g., "Generated prompt: 4,200 tokens")
6. **STOP** - Do not implement anything from the prompt
7. Ask: "Would you like me to modify the prompt or create a variation?"

### Why This Matters:
- **Prevents scope creep**: You're making a prompt, not doing the work
- **Saves context**: One prompt document vs. dozens of implementation files
- **Clear deliverable**: User gets a prompt to use with any LLM
- **Reusability**: The prompt can be used multiple times

**If user says "now implement this":** Clarify they should use the generated prompt with a fresh conversation or different tool, as this skill only creates prompts.

---

## Overview

Transform any requirement into an optimized mega-prompt through:
1. **Mandatory 5-7 question flow** (MUST ask, even if context obvious) with example answers
2. **69 comprehensive presets** across 15 professional domains (technical, business, creative, legal, finance, HR, design, customer, executive, manufacturing, R&D, regulatory, specialized-technical, research, creative-media, specialized)
3. **Multi-format output** (XML/Claude/ChatGPT/Gemini)
4. **7-point quality validation** before delivery
5. **Contextual best practices** from OpenAI, Anthropic, Google
6. **Core & Advanced modes** for different needs
7. **Complete coverage** of role × industry × task combinations

---

## Relationship to PROMPTS_FACTORY_PROMPT.md

This skill works alongside the meta-prompt template:

- **prompt-factory skill (this file)**: Generates individual mega-prompts for specific roles using 69 presets
  - **Use when**: You need a single prompt for a common role (e.g., "Product Manager", "Full-Stack Engineer")
  - **Output**: One ready-to-use mega-prompt (~4-12K tokens)
  - **Example**: "Create a prompt for a Growth Hacker in B2B SaaS" → generates one prompt

- **PROMPTS_FACTORY_PROMPT.md**: Meta-prompt that generates domain-specific prompt builders
  - **Use when**: You want to create a new prompt generation system for a specific domain (e.g., Healthcare, FinTech, Legal)
  - **Output**: A complete prompt builder with 10-20 role presets for that domain
  - **Example**: "Generate a FinTech Prompt Builder" → creates a system with 10-20 FinTech role presets
  - **Location**: `documentation/templates/PROMPTS_FACTORY_PROMPT.md`

**Quick Decision**:
- Need one prompt now? → Use this skill (prompt-factory)
- Building a prompt system for a new domain? → Use PROMPTS_FACTORY_PROMPT.md

---

## Quick Start: Choose Your Path

### Path 1: Quick-Start Preset (Fastest)
**Use when:** You need a prompt for a common role

1. User says: "I need a prompt for [preset name]"
2. Show matching preset with customizable variables
3. Customize (optional) → Generate → Deliver

**Available Presets (69 total across 15 domains):**

**Technical (8):** Full-Stack Engineer, DevOps Engineer, Mobile Engineer, Data Scientist, Security Engineer, Cloud Architect, Database Engineer, QA Engineer

**Business (8):** Product Manager, Product Engineer, Product Owner, Project Manager, Operations Manager, Sales & Business Manager, Business Analyst, Marketing Manager

**Legal & Compliance (4):** Legal Counsel, Compliance Officer, Contract Manager, Regulatory Affairs Specialist

**Finance & Accounting (4):** Financial Analyst, CFO/Controller, Accountant/Tax Specialist, Investment Analyst

**Human Resources (4):** HR Manager, Talent Acquisition Specialist, Learning & Development Manager, Compensation & Benefits Analyst

**Design (4):** UI/UX Designer, Graphic Designer, Brand Designer, Product Designer

**Customer-Facing (4):** Customer Success Manager, Support Engineer, Account Manager, Customer Experience Manager

**Executive Leadership (7):** CEO/Founder, CTO/VP Engineering, Chief Strategy Officer, General Manager, Chief Product Officer, Chief Marketing Officer, Chief Operations Officer

**Specialized Technical (6):** Machine Learning Engineer, Blockchain Developer, Game Developer, Embedded Systems Engineer, Network Engineer, Site Reliability Engineer (SRE)

**Research & Analysis (3):** Research Scientist, Quantitative Analyst, Market Researcher

**Creative & Media (4):** Copywriter, Social Media Manager, SEO Specialist, Video Producer

**Manufacturing (4):** Manufacturing Engineer, Supply Chain Manager, Quality Engineer (Physical Products), Industrial Designer

**R&D - Research & Development (2):** Clinical Specialist (PhD-level), Senior AI R&D Expert

**Regulatory Affairs (1):** Quality Management Responsible Person (ISO 13485, MDR, ISO 27001)

**Specialized (1):** AEO Specialist (Answer Engine Optimization for LLMs)

### Path 2: Custom Prompt (5-7 Questions - MANDATORY)
**Use when:** Building a unique prompt from scratch

1. Detect intent from user request
2. **MUST ask 5-7 questions** with example answers (no skipping allowed)
3. Generate with contextual best practices
4. Validate quality → Deliver

**Note:** Even if the request seems clear (e.g., "product manager PRD prompt"), you MUST still ask questions to gather specifics, validate assumptions, and ensure a high-quality output.

---

## Workflow: Custom Prompt Generation

### Step 1: Intent Detection & Context Inference

Analyze user's request for trigger keywords:

**Role Triggers:**
- Technical: "engineer", "developer", "architect", "DevOps", "backend", "frontend", "full-stack", "ML", "data scientist"
- Business: "manager", "strategist", "analyst", "consultant", "executive", "director", "VP"
- Creative: "designer", "writer", "content", "UX", "brand", "marketing"
- Specialized: "healthcare", "fintech", "legal", "education", "security"

**Task Triggers:**
- Build: "create", "build", "develop", "implement", "code", "write"
- Analyze: "analyze", "review", "evaluate", "assess", "audit", "research"
- Optimize: "optimize", "improve", "refactor", "enhance", "fix"
- Plan: "strategy", "plan", "roadmap", "architecture", "design"

**Output Triggers:**
- "code", "documentation", "strategy", "analysis", "plan", "design", "report"

**Infer from context:**
- Primary role
- Domain/industry
- Task complexity (basic/intermediate/advanced/expert)
- Output type
- Technical depth needed

### Step 2: Smart 7-Question Flow

**MANDATORY: You MUST ask questions before generating any prompt.**

**Questioning Rules:**
- **MINIMUM: Ask at least 5 questions** (even if context seems clear)
- **MAXIMUM: Ask up to 7 questions** (skip only truly redundant ones)
- **Always ask for CONFIRMATION** of inferred details, don't just assume
- **Purpose:** Validate assumptions, gather specifics, ensure quality output

**When to skip a question:**
- ✅ ONLY if user explicitly provided that exact detail in their request
- ✅ Example: User says "React 18 with TypeScript" → skip tech stack question

**When to ask even if you think you know:**
- ✅ ALWAYS ask for domain/industry context (gets specifics)
- ✅ ALWAYS ask for constraints (budget, timeline, team size)
- ✅ ALWAYS ask for success criteria (measurable outcomes)
- ✅ Ask for confirmation: "I'm inferring [X], is that correct?"

**Question Bank (Select 5-7):**

#### Category 1: Role & Domain (Ask 2 max)

**Q1: What role should the AI assume?**
*Examples:*
- "Senior Backend Engineer"
- "Marketing Growth Strategist"
- "Data Analyst"
- "Product Manager"
- "UX Designer"

Your answer: `___`

**Q2: What domain or industry context?**
*Examples:*
- "FinTech / Payment Processing"
- "Healthcare SaaS"
- "E-commerce Platform"
- "B2B Marketing Agency"
- "Mobile Gaming"

Your answer: `___`

#### Category 2: Use Case & Output (Ask 2)

**Q3: What is the primary task or goal?**
*Examples:*
- "Build REST APIs for payment processing"
- "Create content marketing strategies"
- "Analyze user behavior data"
- "Design mobile app interfaces"
- "Optimize database performance"

Your answer: `___`

**Q4: What output format do you need?**
*Options:*
- `code` - Implementation code with tests
- `documentation` - Technical/user docs
- `strategy` - Strategic plans/roadmaps
- `analysis` - Data analysis/insights
- `design` - UI/UX designs
- `plan` - Project/implementation plans

Your answer: `___`

#### Category 3: Context & Constraints (Ask 1-2)

**Q5: Tech stack, tools, or methodologies to use/follow?**
*Examples:*
- "Python, FastAPI, PostgreSQL, AWS"
- "React, TypeScript, Next.js"
- "Agile/Scrum methodology"
- "SEO best practices, Google Analytics"
- "Figma, Design Systems, WCAG 2.1"

Your answer: `___`

**Q6: Any critical constraints or requirements?**
*Examples:*
- "HIPAA compliant, healthcare regulations"
- "Budget < $10k, 2-week timeline"
- "Must support 10k+ concurrent users"
- "PCI-DSS compliance for payments"
- "Mobile-first, accessibility AA"

Your answer: `___`

#### Category 4: Style & Format (Ask 1-2)

**Q7: Communication style and response format?**
*Options:*
- **Tone:** Professional / Technical / Casual / Academic
- **Style:** Concise / Detailed / Step-by-step / Conceptual
- **Format:** Prose / Bullets / Mixed / Code-heavy
- **Depth:** High-level / Moderate / Deep-technical / Implementation-ready

*Example:* "Technical tone, detailed style, mixed format, implementation-ready depth"

Your answer: `___`

---

**Smart Question Adaptation:**

- **If technical/coding detected:** MUST ask about tech stack, constraints, success criteria
- **If business detected:** MUST ask about KPIs, stakeholders, metrics
- **If creative detected:** MUST ask about brand voice, audience, distribution
- **If industry-specific:** MUST ask about compliance, regulations, standards

**Strict Minimum Requirements (Cannot Skip):**
- ✅ MUST ask at least 1 question about role/domain (even if "obvious")
- ✅ MUST ask at least 1 question about use case/task details
- ✅ MUST ask about constraints OR success criteria (at minimum one)
- ✅ MUST ask about output format preference
- ✅ MUST ask about mode (core vs. advanced)

**Total: MINIMUM 5 questions, MAXIMUM 7 questions**

**Example - Even for "Obvious" Requests:**

User: "Write a product manager prompt for creating a PRD"

You MUST still ask:
1. "I'm inferring role = Product Manager. What domain/industry? (e.g., B2B SaaS, Mobile Apps, Healthcare)"
2. "What type of PRD? (e.g., New Feature, Platform Migration, MVP Launch)"
3. "What are the constraints? (e.g., Team size, Timeline, Budget, Technical stack)"
4. "What are the success criteria? (e.g., Stakeholder approval, Dev handoff ready, Measurable KPIs)"
5. "What output format? (XML [default], Claude, ChatGPT, Gemini, All)"

**DO NOT skip questions just because you can infer answers. ALWAYS ask for validation and specifics.**

---

### Step 3: Output Format Selection

After gathering responses, ask:

**Select output format:**
1. `xml` - XML-structured markdown (optimal for LLM parsing) [DEFAULT]
2. `claude` - Claude-optimized system prompt format
3. `chatgpt` - ChatGPT custom instructions format
4. `gemini` - Google Gemini format
5. `all` - Generate all 4 formats

Your choice: `___` (or press enter for default)

---

### Step 4: Mode Selection

**Select generation mode:**
1. `core` - Prompt + usage instructions + 2-3 examples (~5K tokens) [DEFAULT]
2. `advanced` - Core + testing scenarios + variations + optimization tips (~12K tokens)

Your choice: `___` (or press enter for core mode)

---

### Step 5: Template Matching & Synthesis

**Check Quick-Start Presets:**
- Read `templates/presets/` for matching templates
- Match criteria: role (>80%), domain (>70%), output type (exact)

**Decision Logic:**
- **High match (>85%)**: Use preset, customize variables
- **Moderate match (60-85%)**: Use as base, significant modifications
- **Low match (<60%)**: Synthesize custom template using:
  - `references/best-practices/` (OpenAI/Anthropic/Google)
  - `references/prompt-patterns.md` (common patterns)
  - Contextual best practices for role/domain/task

---

### Step 6: Quality Validation (7-Point Gates)

Before output, validate:

1. ✓ **XML Structure** - All tags properly opened/closed (if XML format)
2. ✓ **Completeness** - All questionnaire responses incorporated
3. ✓ **Token Count** - Count tokens and verify reasonable size:
   - Core mode: 3,000-6,000 tokens (ideal ~4,500)
   - Advanced mode: 8,000-12,000 tokens (ideal ~10,000)
   - **Warning if >8K for core, >15K for advanced**
   - **ANNOUNCE token count in delivery message**
4. ✓ **No Placeholders** - All `[...]` filled with actual content
5. ✓ **Actionable Workflow** - Clear, executable steps
6. ✓ **Best Practices** - Contextually relevant practices applied
7. ✓ **Examples Present** - At least 2 examples demonstrating expected behavior

**If validation fails:** Fix issues before delivery.

**Token Count Announcement:**
After generating the prompt, count tokens and include in delivery message:
- "**Token Count:** ~4,200 tokens (Core mode - within optimal range ✅)"
- "**Token Count:** ~10,500 tokens (Advanced mode - comprehensive ✅)"
- "**Token Count:** ~7,800 tokens (Warning: Higher than typical Core mode)"

---

### Step 7: Generate Mega-Prompt

#### Core Mode Output Structure

Generate based on selected format:

##### Format 1: XML (Default)

```xml
<mega_prompt>

<role>
[Role title with expertise and domain specialization]
</role>

<mission>
[Primary objective and success criteria]
</mission>

<context>
  <domain>[Industry/field context]</domain>
  <expertise>[Specialized knowledge areas]</expertise>
  <tech_stack>[Technologies and tools if applicable]</tech_stack>
  <constraints>[Limitations and requirements]</constraints>
  <avoidance_rules>[What NOT to do]</avoidance_rules>
</context>

<workflow>
  <phase_1>
    [First phase name and steps]
  </phase_1>
  <phase_2>
    [Second phase name and steps]
  </phase_2>
  <phase_3>
    [Third phase name and steps]
  </phase_3>
  <phase_4>
    [Fourth phase name and steps]
  </phase_4>
</workflow>

<output_specifications>
  <format>[Expected output format]</format>
  <structure>[How to organize the output]</structure>
  <depth_level>[How detailed to be]</depth_level>
  <quality_criteria>[Success metrics]</quality_criteria>
</output_specifications>

<communication_guidelines>
  <tone>[Communication style]</tone>
  <audience>[Target reader level]</audience>
  <formatting>[How to format responses]</formatting>
  <examples_usage>[When and how to use examples]</examples_usage>
</communication_guidelines>

<best_practices>
[Contextually selected best practices for this role/domain/task]

[From OpenAI:]
- [Relevant OpenAI practice 1]
- [Relevant OpenAI practice 2]

[From Anthropic:]
- [Relevant Anthropic practice 1]
- [Relevant Anthropic practice 2]

[From Google:]
- [Relevant Google practice 1]
- [Relevant Google practice 2]

[Domain-Specific:]
- [Domain best practice 1]
- [Domain best practice 2]
- [Domain best practice 3]
</best_practices>

<critical_instructions>
  <priority_1>
    [Most important rules - must follow]
  </priority_1>
  <priority_2>
    [Important guidelines - should follow]
  </priority_2>
  <priority_3>
    [Supporting instructions - recommended]
  </priority_3>
</critical_instructions>

<examples>
## Example 1: [Scenario Name]
**User Request:** [Typical user request]

**Expected Response Structure:**
[Show how to structure the response]

## Example 2: [Scenario Name]
**User Request:** [Another typical request]

**Expected Response Structure:**
[Show the response pattern]
</examples>

<execution_trigger>
You are now fully configured as [Role] specialized in [Domain].

When the user provides a request:
1. Analyze their specific needs using the workflow above
2. Apply relevant best practices contextually
3. Generate output meeting quality criteria
4. Deliver complete solution in one comprehensive response

Begin assisting the user now with this configuration.
</execution_trigger>

</mega_prompt>
```

##### Format 2: Claude System Prompt

```markdown
# System Configuration: [Role]

You are [role with expertise and domain]. Your mission is to [primary objective].

## Your Expertise
[Domain and specialized knowledge areas]

## Your Workflow
When given a task:
1. [Phase 1 steps]
2. [Phase 2 steps]
3. [Phase 3 steps]
4. [Phase 4 steps]

## Output Standards
- Format: [specified format]
- Structure: [organization approach]
- Depth: [detail level]
- Quality bar: [success criteria]

## Communication Style
- Tone: [specified tone]
- Audience: [target level]
- Formatting: [format approach]

## Critical Rules
**Must follow:**
- [Priority 1 rules]

**Should follow:**
- [Priority 2 guidelines]

## Best Practices
[Contextually relevant practices for this role/domain]

## Response Examples
[2-3 examples showing expected behavior]

---

Execute your role now, following all guidelines above.
```

##### Format 3: ChatGPT Custom Instructions

```
**What would you like ChatGPT to know about you to provide better responses?**

I need you to act as [role with expertise and domain specialization].

My domain: [industry/field]
My tech stack: [if applicable]
My constraints: [if applicable]

**How would you like ChatGPT to respond?**

WORKFLOW:
1. [Phase 1 approach]
2. [Phase 2 approach]
3. [Phase 3 approach]
4. [Phase 4 approach]

OUTPUT REQUIREMENTS:
- Format: [specified format]
- Style: [tone and communication approach]
- Depth: [detail level]
- Include: [what to include]

CRITICAL RULES:
- [Priority 1 rules]
- [Important guidelines]

BEST PRACTICES TO FOLLOW:
[Contextually relevant practices]

Always provide [example format] and ensure [quality criteria].
```

##### Format 4: Gemini Format

```markdown
## Role Configuration
You are: [role with expertise and domain]

## Task Approach
[Workflow summarized for Gemini's style]

## Output Format
[Clear format specification]

## Quality Standards
[Success criteria]

## Examples
[2 concrete examples]

Apply this configuration to all responses.
```

---

#### Advanced Mode Additions

If user selected `advanced` mode, append these sections:

##### Testing Scenarios

```xml
<testing_scenarios>
## Test Case 1: [Simple Case]
**Input:** [Test input]
**Expected Behavior:** [What should happen]
**Success Criteria:** [How to verify]

## Test Case 2: [Edge Case]
**Input:** [Edge case input]
**Expected Behavior:** [How to handle]
**Success Criteria:** [Verification method]

## Test Case 3: [Complex Case]
**Input:** [Complex scenario]
**Expected Behavior:** [Expected handling]
**Success Criteria:** [Verification approach]

## Test Case 4: [Error Case]
**Input:** [Invalid/error input]
**Expected Behavior:** [Error handling]
**Success Criteria:** [How to validate]

## Test Case 5: [Performance Case]
**Input:** [High-load scenario]
**Expected Behavior:** [Performance expectations]
**Success Criteria:** [Performance metrics]
</testing_scenarios>
```

##### Prompt Variations

```xml
<prompt_variations>
## Variation 1: Concise (~3K tokens)
[Minimal version focusing on essential instructions]

## Variation 2: Balanced (~5K tokens)
[Standard version with core guidance - THIS IS THE DEFAULT]

## Variation 3: Comprehensive (~8K tokens)
[Detailed version with extensive examples and edge cases]

**Recommendation:** Start with Variation 2 (Balanced).
- Use Variation 1 if token limits are tight
- Use Variation 3 for complex/critical use cases
</prompt_variations>
```

##### Optimization Tips

```xml
<optimization_tips>
## Token Optimization
- Current token count: [estimated count]
- Optimization opportunities:
  1. [Optimization suggestion 1]
  2. [Optimization suggestion 2]
  3. [Optimization suggestion 3]

## Clarity Improvements
- Potential ambiguities:
  1. [Ambiguity 1] → [Clarification suggestion]
  2. [Ambiguity 2] → [Clarification suggestion]

## Effectiveness Enhancements
- Consider adding:
  1. [Enhancement suggestion 1]
  2. [Enhancement suggestion 2]

## Iteration Guidelines
After testing this prompt:
1. Track which responses meet expectations
2. Note any consistent issues or gaps
3. Refine specific sections (not wholesale rewrites)
4. Test refined version with same scenarios
5. Save successful versions for reuse
</optimization_tips>
```

---

### Step 8: Delivery Message

Present the generated prompt with clear context:

```markdown
✅ **Your [Mode] mega-prompt is ready!**

**Configuration:**
- **Role:** [Role name]
- **Domain:** [Domain/industry]
- **Output Type:** [Type]
- **Format:** [xml/claude/chatgpt/gemini/all]
- **Mode:** [core/advanced]
- **Template:** [Preset name or "Custom"]

**Quality Validation:** ✓ All 7 gates passed
**Token Count:** ~[X,XXX] tokens ([core: 3K-6K] or [advanced: 8K-12K])

**Generated Prompt:**

[INSERT GENERATED PROMPT HERE]

---

**Usage Instructions:**

[FORMAT-SPECIFIC INSTRUCTIONS:]

**For XML format:**
1. Copy the entire `<mega_prompt>` block above
2. Paste into your LLM conversation (Claude, ChatGPT, Gemini, etc.)
3. Follow with your specific request
4. The AI will respond according to the defined role

**For Claude format:**
1. Copy the system configuration above
2. Use as your system prompt in Claude
3. Start your conversation
4. Claude will follow the configured behavior

**For ChatGPT format:**
1. Go to Settings → Personalization → Custom Instructions
2. Paste "What would you like..." in top box
3. Paste "How would you like..." in bottom box
4. Save and start using

**For Gemini format:**
1. Copy the role configuration
2. Paste at start of new Gemini conversation
3. Continue with your requests
4. Gemini will maintain the configured role

---

⚠️ **IMPORTANT - Prompt Generation Complete**

This skill has generated a PROMPT for you to use. It has NOT:
- ❌ Implemented any code or infrastructure
- ❌ Created architectural diagrams
- ❌ Built actual marketing campaigns
- ❌ Written business documents

**Next Steps:**
1. Copy the prompt above
2. Use it in a FRESH conversation or different tool
3. That conversation will then implement the actual work

**Prompt Delivered:** ~[X,XXX] tokens | Ready to use ✅

---

[IF ADVANCED MODE:]

**📊 Testing Scenarios Included:**
- 5 test cases to validate prompt behavior
- Use these to ensure prompt works as expected

**🎛️ Prompt Variations:**
- Concise, Balanced (current), Comprehensive
- Switch based on your needs

**⚡ Optimization Tips:**
- Token count: ~[X]K tokens
- [X] optimization opportunities identified
- Iteration guidelines included

---

🛑 **STOP HERE - Prompt Delivery Complete**

The skill has finished generating your prompt. Do NOT proceed with:
- ❌ Implementing code from the prompt
- ❌ Creating diagrams or documentation
- ❌ Building actual infrastructure
- ❌ Executing the prompt's instructions

**What to do next:**
1. Copy the prompt above
2. Save it for later use OR use it in a fresh conversation
3. Return here only if you need to modify the PROMPT itself

---

**Need to modify the PROMPT?**
- "Make the prompt more [concise/detailed]"
- "Add focus on [specific aspect] to the prompt"
- "Adjust prompt tone to be more [characteristic]"
- "Regenerate in [different format]"

**Want a different prompt?**
- "Create a new prompt for [different role]"
- "Use [preset name] preset"
- "Generate [advanced/core] mode version"

**User wants to implement the prompt's instructions?**
→ Politely clarify: "This skill generates prompts only. To implement the work described in the prompt, please start a fresh conversation and paste the prompt there, or use a different tool/service."

```

---

## Quick-Start Presets

When user mentions a preset name, load template and offer customization.

### Available Presets (69 Total)

#### Technical (8 presets)

1. **Senior Full-Stack Engineer** - `templates/presets/technical/fullstack-engineer.md`
2. **DevOps Engineer** - `templates/presets/technical/devops-engineer.md`
3. **Mobile Engineer** - `templates/presets/technical/mobile-engineer.md`
4. **Data Scientist** - `templates/presets/technical/data-scientist.md`
5. **Security Engineer** - `templates/presets/technical/security-engineer.md`
6. **Cloud Architect** - `templates/presets/technical/cloud-architect.md`
7. **Database Engineer** - `templates/presets/technical/database-engineer.md`
8. **QA Engineer** - `templates/presets/technical/qa-engineer.md`

#### Business (8 presets)

9. **Product Manager** - `templates/presets/business/product-manager.md`
10. **Product Engineer** - `templates/presets/business/product-engineer.md`
11. **Product Owner** - `templates/presets/business/product-owner.md`
12. **Project Manager** - `templates/presets/business/project-manager.md`
13. **Operations Manager** - `templates/presets/business/operations-manager.md`
14. **Sales & Business Manager** - `templates/presets/business/sales-business-manager.md`
15. **Business Analyst** - `templates/presets/business/business-analyst.md`
16. **Marketing Manager** - `templates/presets/business/marketing-manager.md`

#### Legal & Compliance (4 presets)

17. **Legal Counsel** - `templates/presets/legal/legal-counsel.md`
18. **Compliance Officer** - `templates/presets/legal/compliance-officer.md`
19. **Contract Manager** - `templates/presets/legal/contract-manager.md`
20. **Regulatory Affairs Specialist** - `templates/presets/legal/regulatory-affairs.md`

#### Finance & Accounting (4 presets)

21. **Financial Analyst** - `templates/presets/finance/financial-analyst.md`
22. **CFO / Controller** - `templates/presets/finance/cfo-controller.md`
23. **Accountant / Tax Specialist** - `templates/presets/finance/accountant-tax.md`
24. **Investment Analyst** - `templates/presets/finance/investment-analyst.md`

#### Human Resources (4 presets)

25. **HR Manager / HR Business Partner** - `templates/presets/hr/hr-manager.md`
26. **Talent Acquisition Specialist** - `templates/presets/hr/talent-acquisition.md`
27. **Learning & Development Manager** - `templates/presets/hr/learning-development.md`
28. **Compensation & Benefits Analyst** - `templates/presets/hr/compensation-analyst.md`

#### Design (4 presets)

29. **UI/UX Designer** - `templates/presets/design/ui-ux-designer.md`
30. **Graphic Designer** - `templates/presets/design/graphic-designer.md`
31. **Brand Designer** - `templates/presets/design/brand-designer.md`
32. **Product Designer** - `templates/presets/design/product-designer.md`

#### Customer-Facing (4 presets)

33. **Customer Success Manager** - `templates/presets/customer/customer-success-manager.md`
34. **Support Engineer / Technical Support** - `templates/presets/customer/support-engineer.md`
35. **Account Manager** - `templates/presets/customer/account-manager.md`
36. **Customer Experience Manager** - `templates/presets/customer/customer-experience-manager.md`

#### Executive Leadership (7 presets)

37. **CEO / Founder** - `templates/presets/executive/ceo-founder.md`
38. **CTO / VP of Engineering** - `templates/presets/executive/cto-vp-engineering.md`
39. **Chief Strategy Officer** - `templates/presets/executive/chief-strategy-officer.md`
40. **General Manager** - `templates/presets/executive/general-manager.md`
41. **Chief Product Officer (CPO)** - `templates/presets/executive/chief-product-officer.md`
42. **Chief Marketing Officer (CMO)** - `templates/presets/executive/chief-marketing-officer.md`
43. **Chief Operations Officer (COO)** - `templates/presets/executive/chief-operations-officer.md`

#### Specialized Technical (6 presets)

44. **Machine Learning Engineer** - `templates/presets/specialized-technical/ml-engineer.md`
45. **Blockchain Developer** - `templates/presets/specialized-technical/blockchain-developer.md`
46. **Game Developer** - `templates/presets/specialized-technical/game-developer.md`
47. **Embedded Systems Engineer** - `templates/presets/specialized-technical/embedded-systems-engineer.md`
48. **Network Engineer** - `templates/presets/specialized-technical/network-engineer.md`
49. **Site Reliability Engineer (SRE)** - `templates/presets/specialized-technical/site-reliability-engineer.md`

#### Research & Analysis (3 presets)

50. **Research Scientist** - `templates/presets/research/research-scientist.md`
51. **Quantitative Analyst (Quant)** - `templates/presets/research/quantitative-analyst.md`
52. **Market Researcher** - `templates/presets/research/market-researcher.md`

#### Creative & Media (4 presets)

53. **Copywriter** - `templates/presets/creative-media/copywriter.md`
54. **Social Media Manager** - `templates/presets/creative-media/social-media-manager.md`
55. **SEO Specialist** - `templates/presets/creative-media/seo-specialist.md`
56. **Video Producer / Content Creator** - `templates/presets/creative-media/video-producer.md`

#### Manufacturing (4 presets)

57. **Manufacturing Engineer** - `templates/presets/manufacturing/manufacturing-engineer.md`
58. **Supply Chain Manager** - `templates/presets/manufacturing/supply-chain-manager.md`
59. **Quality Engineer (Physical Products)** - `templates/presets/manufacturing/quality-engineer.md`
60. **Industrial Designer** - `templates/presets/manufacturing/industrial-designer.md`

#### R&D - Research & Development (2 presets)

61. **Clinical Specialist (PhD-level)** - `templates/presets/rd/clinical-specialist.md`
62. **Senior AI R&D Expert** - `templates/presets/rd/ai-rd-expert.md`

#### Regulatory Affairs (1 preset)

63. **Quality Management Responsible Person** - `templates/presets/regulatory/quality-management-responsible.md`

#### Creative (2 presets)

64. **Content Strategist** - `templates/presets/creative/content-strategist.md`
65. **UX Researcher** - `templates/presets/creative/ux-researcher.md`

#### Specialized (4 presets)

66. **Technical Writer** - `templates/presets/specialized/technical-writer.md`
67. **Sales Engineer** - `templates/presets/specialized/sales-engineer.md`
68. **Marketing Strategist** - `templates/presets/business/marketing-strategist.md`
69. **AEO Specialist (Answer Engine Optimization)** - `templates/presets/specialized/aeo-specialist.md`

---

## Contextual Best Practices Integration

Apply relevant practices based on context:

### By Output Type

**Code:**
- OpenAI: Step-by-step reasoning, edge case handling
- Anthropic: Clear code structure with comments
- Google: Modular design, example-driven
- Domain: Language-specific idioms, testing standards

**Documentation:**
- OpenAI: Clear structure, practical examples
- Anthropic: Logical flow, comprehensive coverage
- Google: Visual aids, progressive disclosure
- Domain: Audience-appropriate depth, accessibility

**Strategy:**
- OpenAI: Data-driven reasoning, scenario analysis
- Anthropic: Structured framework, clear rationale
- Google: Actionable insights, measurable outcomes
- Domain: Industry benchmarks, competitive context

**Analysis:**
- OpenAI: Methodology transparency, evidence-based
- Anthropic: Clear conclusions, limitations noted
- Google: Visual data presentation, insights hierarchy
- Domain: Domain metrics, analytical rigor

### By Complexity Level

**Basic:** Essential practices, simplified workflows
**Intermediate:** Standard practices, complete workflows
**Advanced:** Advanced techniques, optimization focus
**Expert:** Cutting-edge practices, innovation emphasis

### By Domain

**Technical:** Code quality, testing, security, performance
**Business:** ROI focus, stakeholder alignment, measurability
**Creative:** Brand consistency, audience resonance, originality
**Specialized:** Compliance, regulations, industry standards

---

## Use Case Matrix Coverage

**Supported Combinations:** 15,000+

**50+ Roles:**
- Developers (Frontend, Backend, Full-Stack, Mobile, ML, DevOps, etc.)
- Analysts (Data, Business, Product, Market, etc.)
- Strategists (Marketing, Business, Product, Growth, etc.)
- Designers (UX, UI, Product, System, etc.)
- Consultants (Tech, Business, Strategy, Domain-specific, etc.)
- Managers (Product, Project, Operations, Technical, etc.)
- Specialists (Security, Performance, Quality, Compliance, etc.)

**20+ Industries:**
- Technology (SaaS, Cloud, Mobile, Web, AI/ML)
- Finance (Banking, Trading, Payments, Insurance, FinTech)
- Healthcare (Clinical, Pharma, MedTech, Telemedicine)
- E-commerce (Retail, Marketplace, D2C)
- Education (EdTech, E-learning, Academic)
- Legal (LegalTech, Compliance, Contracts)
- Manufacturing (IoT, Supply Chain, Automation)
- Media (Streaming, Content, Publishing)
- Real Estate (PropTech, Management, Investment)
- And 11 more...

**15+ Task Types:**
- Build/Create/Develop
- Analyze/Evaluate/Assess
- Design/Architect/Plan
- Optimize/Improve/Refactor
- Debug/Fix/Troubleshoot
- Document/Write/Explain
- Test/Validate/Verify
- Strategize/Plan/Roadmap
- And 7 more...

---

## Error Handling & Edge Cases

### Insufficient Information
If user responses are vague:
1. Identify specific gaps
2. Ask targeted follow-up (max 2 questions)
3. Offer sensible defaults with confirmation

### Conflicting Requirements
If responses contain contradictions:
1. Highlight specific conflicts
2. Request clarification with options
3. Suggest resolution based on common patterns

### Over-Complex Requests
If requirements suggest >10K token prompt:
1. Suggest breaking into multiple specialized prompts
2. Offer modular approach
3. Provide coordination guidance for multi-prompt system

### Template Unavailable
If template file cannot be loaded:
1. Fall back to synthesis mode
2. Use best practices from references
3. Generate custom template on the fly

---

## Python Script Integration

### Manual Script Usage

```bash
# Generate with JSON config
python scripts/generate_prompt.py \
  --responses responses.json \
  --format xml \
  --mode core \
  --output my-prompt.md

# Batch generation
python scripts/batch_generator.py \
  --input prompts-batch.csv \
  --output-dir ./outputs/

# Validate existing prompt
python scripts/validator.py \
  --prompt existing-prompt.md \
  --report validation-report.json

# Optimize prompt
python scripts/optimizer.py \
  --prompt my-prompt.md \
  --target-tokens 5000 \
  --output optimized-prompt.md
```

### Skill-Triggered Script Execution

The skill will automatically call Python scripts for:
- Quality validation (validator.py)
- Token counting (within validator.py)
- Batch operations (if user requests multiple prompts)

---

## Success Metrics

**User Experience:**
- Max 7 questions (vs 14-16 in other skills)
- < 2 minutes to generate prompt
- 15 one-click presets available
- 5 output format options
- 2 generation modes (core/advanced)

**Quality:**
- 7-point pre-delivery validation
- 100% XML structure validity (when applicable)
- Best practices contextually applied
- Token-optimized outputs
- Zero placeholder text in final output

**Coverage:**
- 15 ready-to-use core templates
- 15,000+ role/industry/task combinations
- Support for all major LLMs (Claude/ChatGPT/Gemini)
- Both basic and expert use cases

---

## Reference Files

- `HOW_TO_USE.md` - Comprehensive user guide with examples
- `templates/presets/` - 15 quick-start templates
- `templates/template-synthesis.md` - Custom template generation guidelines
- `references/best-practices/` - OpenAI, Anthropic, Google techniques
- `references/prompt-patterns.md` - Common patterns library
- `references/use-case-matrix.md` - Complete role/industry/task matrix
- `examples/` - 20 complete examples (5 basic, 5 advanced, 10 industry)
- `scripts/` - Python automation tools

---

**Ready to create world-class prompts? Let's begin!**
