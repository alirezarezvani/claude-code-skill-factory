# Prompt Engineering Best Practices Reference

## Table of Contents
1. [Universal Best Practices](#universal-best-practices)
2. [Role-Specific Best Practices](#role-specific-best-practices)
3. [Output Format Best Practices](#output-format-best-practices)
4. [Quality Validation Best Practices](#quality-validation-best-practices)
5. [Common Pitfalls to Avoid](#common-pitfalls-to-avoid)

---

## Universal Best Practices

### Prompt Structure
- **Clear role definition**: Always start with a specific, expert role
- **Explicit domain context**: Define the problem space and industry
- **Measurable objectives**: Include quantifiable success criteria
- **Constraints acknowledgment**: Be realistic about limitations (budget, time, resources)
- **Structured workflow**: Break complex tasks into phases with deliverables

### Clarity and Specificity
- **Use concrete examples**: Show, don't just tell
- **Avoid vague language**: Replace "improve" with "increase by 25%"
- **Define technical terms**: Don't assume shared vocabulary
- **Specify edge cases**: Document error scenarios and exceptions
- **Include success criteria**: Define "done" with measurable outcomes

### Context Provision
- **Background information**: Provide relevant history and current state
- **Stakeholder landscape**: Identify who cares and why
- **Technical environment**: Specify tech stack, tools, platforms
- **Resource availability**: Team size, skills, budget, timeline
- **Business context**: Connect technical work to business outcomes

### Actionability
- **Step-by-step guidance**: Break down complex tasks
- **Code examples**: Provide actual implementation snippets
- **Tool recommendations**: Suggest specific tools and frameworks
- **Decision frameworks**: Help with trade-off analysis
- **Validation steps**: Include testing and quality checks

---

## Role-Specific Best Practices

### Technical Roles (Engineers, DevOps, Architects)

**Code Quality**
- Use modern language features and idiomatic patterns
- Follow SOLID principles and clean code practices
- Include error handling and edge cases
- Provide unit and integration tests
- Document assumptions and trade-offs

**Technical Depth**
- Specify exact versions (Node.js 18+, Python 3.11+)
- Include configuration details (environment variables, settings)
- Document API contracts (OpenAPI, GraphQL schemas)
- Provide database schemas and migrations
- Show monitoring and observability setup

**Production Readiness**
- Address scalability and performance
- Include security best practices
- Plan for disaster recovery and backups
- Set up CI/CD pipelines
- Implement logging and alerting

**Example Pattern:**
```xml
<technical_specifications>
- Stack: React 18, TypeScript 5.0, Node.js 18 LTS
- Database: PostgreSQL 15 with connection pooling
- Testing: Jest (unit), Playwright (e2e), 80%+ coverage
- Deployment: Docker on AWS ECS with auto-scaling
- Monitoring: CloudWatch + Datadog for APM
</technical_specifications>
```

### Business Roles (Product Managers, Strategists)

**Strategic Thinking**
- Tie tactics to business metrics (revenue, retention, NPS)
- Use prioritization frameworks (RICE, MoSCoW, KANO)
- Include competitive analysis
- Balance user needs and business goals
- Plan for measurement and iteration

**Stakeholder Communication**
- Executive summary for leadership
- Detailed specs for engineering
- User stories for the whole team
- Visual diagrams for clarity
- Regular status updates

**User-Centered Approach**
- Start with user pain points and jobs-to-be-done
- Include persona definitions
- Map to buyer journey stages
- Validate with user research
- Test assumptions with data

**Example Pattern:**
```xml
<success_metrics>
Business Metrics:
- Increase MRR from $125K to $200K (60% growth)
- Reduce CAC from $600 to $500 (17% improvement)
- Improve LTV:CAC ratio from 3:1 to 4:1

User Metrics:
- Trial-to-paid conversion: 15% → 22% (47% improvement)
- NPS score: 35 → 45 (promoter status)
- Daily Active Users: +25% increase

Timeline: 90 days (Q1 2025)
</success_metrics>
```

### Creative Roles (Content, Design, Marketing)

**Audience Focus**
- Define target personas with demographics and psychographics
- Identify pain points and desired outcomes
- Map content to awareness/consideration/decision stages
- Use voice-of-customer language
- Test messaging with target audience

**Data-Driven Creativity**
- Use keyword research for SEO content
- A/B test headlines, CTAs, designs
- Analyze competitor approaches
- Track engagement metrics
- Optimize based on performance data

**Multi-Channel Thinking**
- Plan distribution across platforms
- Repurpose content into multiple formats
- Tailor messaging to platform norms
- Schedule for optimal engagement times
- Track attribution across channels

**Example Pattern:**
```xml
<content_strategy>
Content Pillars:
1. AI in Customer Support (Primary keyword: 4,800 searches/month)
   - Cluster: 8 articles, 2,000-2,500 words each
   - Formats: Blog, infographic, video explainer
   - Distribution: Blog, LinkedIn, email newsletter

Funnel Alignment:
- ToFu (40%): "10 Customer Support Trends 2025"
- MoFu (40%): "AI vs Human Support: Finding Balance"
- BoFu (20%): "Zendesk vs [Our Product] Comparison"

Publishing Schedule: 2 articles/week, Tuesdays and Thursdays
</content_strategy>
```

---

## Output Format Best Practices

### XML Format (Recommended for Claude)
**When to use**: Complex, structured prompts with multiple sections

**Structure**:
```xml
<role>Define expert persona</role>
<domain>Specify problem space</domain>
<objective>Clear, measurable goal</objective>
<context>Background and constraints</context>
<requirements>
  <functional_requirements>What it must do</functional_requirements>
  <non_functional_requirements>How well it must do it</non_functional_requirements>
</requirements>
<output_specifications>Expected deliverables</output_specifications>
<workflow>Step-by-step phases</workflow>
<best_practices>Domain-specific guidance</best_practices>
<examples>Concrete implementation examples</examples>
<success_criteria>Measurable outcomes</success_criteria>
```

**Advantages**:
- Clear hierarchy and structure
- Easy to parse programmatically
- Works well with long, complex prompts
- Familiar to Claude models

### System Prompt Format (Claude, ChatGPT)
**When to use**: Conversational agents, long-running sessions

**Structure**:
```
# Role
You are a [specific role] with expertise in [domain].

## Capabilities
- [Capability 1]
- [Capability 2]

## Communication Style
- Tone: [Professional/Casual/Technical]
- Format: [Lists/Paragraphs/Code-heavy]

## Workflow
1. [Step 1]
2. [Step 2]

## Constraints
- [Constraint 1]
- [Constraint 2]
```

**Advantages**:
- Human-readable
- Easy to edit and iterate
- Good for iterative conversations
- Works across multiple LLM providers

### Custom Instructions Format (ChatGPT)
**When to use**: User-level configurations, persistent preferences

**Structure**:
```
What would you like ChatGPT to know about you to provide better responses?
- [Personal context]
- [Professional role]
- [Technical environment]

How would you like ChatGPT to respond?
- [Tone and style preferences]
- [Output format preferences]
- [Detail level]
```

### Gemini Format (Google)
**When to use**: Google Gemini models with grounding and tools

**Structure**:
```
Context: [Background information]

Task: [Specific request]

Requirements:
- [Requirement 1]
- [Requirement 2]

Output format:
[Specify structure]

Use tools if needed:
- Google Search for current data
- Code execution for calculations
```

---

## Quality Validation Best Practices

### 7-Point Validation Gates

**1. Structure Validation**
- Check for proper XML/markdown formatting
- Verify all required sections present
- Ensure logical flow and hierarchy
- Validate internal consistency

**2. Completeness Check**
- All sections have substantial content (not placeholders)
- Requirements cover functional and non-functional aspects
- Workflow includes all necessary phases
- Examples demonstrate key concepts

**3. Token Count Optimization**
- Core mode: 3,000-6,000 tokens (efficient)
- Advanced mode: 8,000-12,000 tokens (comprehensive)
- Avoid redundancy and verbosity
- Use concise, precise language

**4. Placeholder Detection**
- No [PLACEHOLDER] or [TODO] markers
- No "insert X here" instructions
- No generic "example.com" or "user@example.com"
- All examples use realistic data

**5. Actionable Workflow**
- Each phase has concrete tasks
- Deliverables are clearly defined
- Dependencies are noted
- Timeline is realistic

**6. Best Practices Integration**
- Domain-specific guidance included
- Industry standards referenced
- Common pitfalls addressed
- Quality standards defined

**7. Example Quality**
- Examples are realistic and detailed
- Code examples are syntactically correct
- Examples demonstrate actual use cases
- Variety of examples across different scenarios

### Testing Your Prompts

**Before Deployment:**
1. Run through the prompt yourself manually
2. Test with the target LLM
3. Validate output against success criteria
4. Check for ambiguities and edge cases
5. Iterate based on results

**After Deployment:**
1. Collect feedback from users
2. Measure success metrics
3. Identify common failure modes
4. Refine based on real-world usage
5. Version control your prompts

---

## Common Pitfalls to Avoid

### Prompt Design Pitfalls

**1. Vague Requirements**
❌ "Build a good API"
✅ "Build a REST API with <5 endpoints, <200ms latency, JWT auth, OpenAPI docs"

**2. Excessive Length Without Value**
❌ Repeating the same point in multiple sections
✅ State each point once, in the most relevant section

**3. Missing Context**
❌ "Implement user authentication"
✅ "Implement JWT authentication for Node.js Express API, storing refresh tokens in Redis"

**4. Unrealistic Constraints**
❌ "Build enterprise-grade system with $100 budget in 1 week"
✅ "Build MVP with core features, $5K budget, 4-week timeline, plan for future scaling"

**5. No Success Criteria**
❌ "Make the app better"
✅ "Reduce page load time from 3s to <1s, increase conversion rate by 15%"

### Technical Pitfalls

**1. Version Ambiguity**
❌ "Use React and Node.js"
✅ "Use React 18.2+ with TypeScript 5.0 and Node.js 18 LTS"

**2. Missing Error Handling**
❌ Only showing happy path code
✅ Include error handling, edge cases, retry logic, fallback mechanisms

**3. Ignoring Scale**
❌ "Store data in memory"
✅ "Use Redis for caching with eviction policies, PostgreSQL for persistent data"

**4. No Testing Guidance**
❌ "Write tests"
✅ "80% coverage with Jest: unit tests for business logic, integration tests for APIs, E2E with Playwright"

**5. Security as Afterthought**
❌ No mention of security
✅ "JWT auth, input validation, SQL injection prevention, rate limiting, HTTPS, CORS config"

### Business Pitfalls

**1. No Business Justification**
❌ "Build this feature because it's cool"
✅ "Build this feature to increase retention by 15% based on user feedback (50 requests)"

**2. Ignoring Stakeholders**
❌ Only considering engineering perspective
✅ Include product, design, sales, support perspectives and requirements

**3. Missing Metrics**
❌ "Improve user experience"
✅ "Increase NPS from 35 to 45, reduce support tickets by 20%, improve task completion rate to 80%"

**4. No Prioritization**
❌ Everything is "must have"
✅ Use MoSCoW: Must have (60%), Should have (30%), Could have (10%)

**5. Unrealistic Timelines**
❌ "Launch in 2 weeks" for 3-month project
✅ "Phase 1 (core features): 6 weeks, Phase 2 (advanced): 4 weeks, Phase 3 (polish): 2 weeks"

### Content Pitfalls

**1. Keyword Stuffing**
❌ Repeat target keyword 50 times unnaturally
✅ Use primary keyword 3-5 times naturally, include semantic variations

**2. No Search Intent Alignment**
❌ Writing about product when user wants how-to guide
✅ Match content type and depth to what users actually want when searching

**3. Missing Distribution Plan**
❌ "Publish and hope people find it"
✅ "Publish on blog, share on LinkedIn, email to 10K subscribers, submit to Reddit r/programming"

**4. No Measurement Plan**
❌ "Create content and never check results"
✅ "Track organic traffic, time on page, conversions, keyword rankings monthly, optimize based on data"

**5. Forgetting Funnel Stages**
❌ All content is product-focused
✅ 40% awareness (ToFu), 40% consideration (MoFu), 20% decision (BoFu)

---

## Quick Reference Checklist

Before finalizing any prompt, verify:

**Structure**
- [ ] Clear role definition
- [ ] Specific domain context
- [ ] Measurable objectives
- [ ] Realistic constraints
- [ ] Structured workflow

**Content**
- [ ] No placeholders or TODOs
- [ ] Concrete examples included
- [ ] Best practices integrated
- [ ] Success criteria defined
- [ ] Validation checklist provided

**Technical**
- [ ] Specific versions and tools
- [ ] Error handling addressed
- [ ] Security considerations included
- [ ] Testing strategy defined
- [ ] Deployment plan outlined

**Business**
- [ ] Business metrics tied to tactics
- [ ] Stakeholders identified
- [ ] User needs addressed
- [ ] Timeline realistic
- [ ] Budget acknowledged

**Quality**
- [ ] Token count appropriate (3K-12K)
- [ ] No redundancy or verbosity
- [ ] Actionable and implementable
- [ ] Examples are realistic
- [ ] Passes 7-point validation

---

## Version History
- v1.0 (2025-01-23): Initial comprehensive reference
- Compiled from OpenAI, Anthropic, and Google best practices
- Based on 1,000+ hours of prompt engineering experience
- Validated across technical, business, and creative domains

---

## Additional Resources

**Official Documentation:**
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Google Gemini Best Practices](https://ai.google.dev/docs/prompt_best_practices)

**Community Resources:**
- [Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering)
- [LangChain Prompt Templates](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)
- [Prompt Engineering Reddit](https://reddit.com/r/PromptEngineering)

**Tools:**
- [Claude Console](https://console.anthropic.com/) - Test prompts
- [OpenAI Playground](https://platform.openai.com/playground) - Experiment with prompts
- [PromptPerfect](https://promptperfect.jina.ai/) - Optimize prompts
