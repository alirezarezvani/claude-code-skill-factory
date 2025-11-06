# Prompt Factory - 5 Complete Examples

This directory contains 5 comprehensive examples demonstrating the **Prompt Factory skill** across different complexity levels and prompting techniques, from basic to master level.

---

## Overview Table

| # | Example | Complexity | Techniques | Tokens | Use Case | File |
|---|---------|------------|------------|--------|----------|------|
| 1 | **Code Reviewer** | ⭐ Basic | Role-based prompting, clear constraints | ~3,200 | Team code quality standards | [basic-code-reviewer.md](basic-code-reviewer.md) |
| 2 | **Data Analyst** | ⭐⭐ Intermediate | Few-shot learning, chain of thought | ~5,800 | Business intelligence, data analysis | [intermediate-data-analyst.md](intermediate-data-analyst.md) |
| 3 | **System Architect** | ⭐⭐⭐ Advanced | Tree of Thoughts, multi-path reasoning | ~8,400 | Enterprise architecture decisions | [advanced-system-architect.md](advanced-system-architect.md) |
| 4 | **Research Analyst** | ⭐⭐⭐⭐ Expert | Meta-prompting, self-consistency, recursive reasoning | ~10,200 | Strategic research, market analysis | [expert-research-analyst.md](expert-research-analyst.md) |
| 5 | **Strategic Consultant** | ⭐⭐⭐⭐⭐ Master | Multi-agent simulation, first-principles, constrained generation | ~11,800 | Board-level strategy, M&A, investments | [master-strategic-consultant.md](master-strategic-consultant.md) |

---

## Example 1: Code Reviewer (Basic)

**Complexity**: ⭐ Basic
**File**: [example-1-basic-code-reviewer.md](basic-code-reviewer.md)

### Prompting Techniques
- **Role-based prompting**: Clear role definition with specific constraints
- **Structured workflow**: 6-phase review process
- **Concrete examples**: Shows exactly how to format feedback
- **Severity categorization**: Critical/High/Medium/Low prioritization

### Key Features
- Simple, straightforward approach
- Clear boundaries (actionable feedback, no style nitpicking)
- Comprehensive examples showing expected behavior
- Perfect for establishing consistent code review standards

### When to Use
- Setting up team code review processes
- Training junior developers on code quality
- Establishing baseline quality standards
- Quick, consistent code reviews

### Sample Output
```markdown
**[CRITICAL] SQL Injection Vulnerability**
- **Location**: Line 2 - query construction
- **Problem**: User input directly interpolated into SQL query
- **Impact**: Attacker can bypass authentication
- **Suggestion**: Use parameterized queries (code example provided)
```

---

## Example 2: Data Analyst (Intermediate)

**Complexity**: ⭐⭐ Intermediate
**File**: [intermediate-data-analyst.md](intermediate-data-analyst.md)

### Prompting Techniques
- **Few-shot learning**: Detailed examples teaching the pattern
- **Chain of thought**: Step-by-step reasoning at each phase
- **Thinking patterns**: Pre-defined phrases guiding internal reasoning
- **Business context**: Translates data into actionable insights

### Key Features
- Shows reasoning process transparently
- Multiple detailed examples (simple and complex)
- Compares metrics against benchmarks/historical data
- Validates findings with data at each step

### When to Use
- Business intelligence and analytics
- Data-driven decision making
- Explaining insights to non-technical stakeholders
- Building trust in analysis through transparent reasoning

### Sample Output
```markdown
**Step 1: Validate the decline**
- Previous week: $850,000
- Last week: $722,000
- Change: -15% (outside normal variance of ±5%)
✅ Confirmed - significant drop

**Step 2: Break down by components**
Sales = Traffic × Conversion × AOV
- Traffic: -1.1% ✅ Stable
- Conversion: -14.3% ⚠️ Problem found
- AOV: 0% ✅ Stable

**Insight**: Issue is conversion rate...
```

---

## Example 3: System Architect (Advanced)

**Complexity**: ⭐⭐⭐ Advanced
**File**: [advanced-system-architect.md](advanced-system-architect.md)

### Prompting Techniques
- **Tree of Thoughts (ToT)**: Explores multiple solution paths before deciding
- **Multi-path reasoning**: Develops 3-5 distinct approaches in parallel
- **Self-critique**: Explicitly challenges own recommendations
- **Quantitative evaluation**: Scores approaches across 9 dimensions
- **Scenario planning**: Considers alternative futures and fallbacks

### Key Features
- Systematic exploration of 3+ architectural approaches
- Multi-dimensional evaluation matrix with weighted scoring
- Cost modeling with specific dollar amounts
- Performance projections with confidence levels
- Risk assessment with probability × impact
- Implementation roadmap with phases and decision gates

### When to Use
- Enterprise architecture decisions
- Cloud migration planning
- Technology selection for major systems
- High-stakes technical decisions requiring rigorous analysis

### Sample Output
```markdown
### Approach Exploration (Tree of Thoughts)

**Approach A: Serverless Data Lake**
- Cost: $3,000/month
- Query latency: 3-5 seconds ❌ FAILS requirement
- Conclusion: Eliminated

**Approach B: Kafka + Druid**
- Cost: $7,000/month
- Query latency: 200-800ms ✅ Meets requirement
- Conclusion: Recommended

**Approach C: TimescaleDB**
- Cost: $3,800/month
- Query latency: 500ms-1.5s ⚠️ Borderline
- Scaling concern: Limited headroom

**Winner**: Approach B (scores 7.55/10 vs 7.20/10)
```

---

## Example 4: Research Analyst (Expert)

**Complexity**: ⭐⭐⭐⭐ Expert
**File**: [expert-research-analyst.md](expert-research-analyst.md)

### Prompting Techniques
- **Meta-prompting**: Questions the question itself before answering
- **Self-consistency**: Multiple independent reasoning paths, then cross-validation
- **Recursive reasoning**: Questions each conclusion, traces back to evidence
- **Red team exercise**: Explicitly argues against own findings
- **Confidence calibration**: Quantifies certainty with percentages
- **Assumption mapping**: Makes implicit assumptions explicit, then tests them

### Key Features
- 3 parallel research paths (top-down, bottom-up, analogical)
- Meta-cognitive framework (self-monitoring questions)
- Weighted synthesis based on confidence levels
- Sensitivity analysis for key assumptions
- Evidence hierarchy (quality assessment)
- Limitation mapping (what's unknown)

### When to Use
- Strategic business research
- Competitive intelligence
- Market analysis and sizing
- High-stakes research where accuracy matters
- Due diligence investigations

### Sample Output
```markdown
### Cross-Path Synthesis

**Path A (Top-Down)**: $18-22B (🟢 85% confidence)
**Path B (Bottom-Up)**: $20-25B (🟡 60% confidence)
**Path C (Analogical)**: $15-20B (🟡 55% confidence)

**Where Paths Converge**: $18-22B range
**Final Estimate**: $20B (🟡 65% confidence)

**Self-Critique**: "If I'm wrong, it's likely because..."
- Path B overestimates vendor AI revenue
- Path C analogy may not hold
- Weighted average: $20.8B

**Confidence Justification**:
- 3 independent methods converge ✅
- High-quality data sources ✅
- Assumptions tested ✅
- Red team didn't find fatal flaws ✅
```

---

## Example 5: Strategic Consultant (Master)

**Complexity**: ⭐⭐⭐⭐⭐ Master
**File**: [master-strategic-consultant.md](master-strategic-consultant.md)

### Prompting Techniques
- **Multi-agent simulation**: Simulates 5 distinct expert personas (CFO, COO, CSO, CTO, Board)
- **First-principles thinking**: Strips away assumptions, rebuilds from fundamental truths
- **Socratic method**: Uses systematic questioning to test logic
- **Constrained generation**: Forces structured outputs (500-word exec summary, required sections)
- **Structured outputs**: Decision matrices, financial models, risk registers, roadmaps
- **Fatal flaw analysis**: Identifies deal-breakers before recommending

### Key Features
- 5 expert agent simulations with distinct perspectives and incentives
- First-principles deconstruction of strategic problems
- Socratic dialogue challenging each perspective
- Weighted decision matrix with quantified criteria
- 3-scenario financial model (base/upside/downside)
- Top-10 risk register with probability × impact scores
- Phased implementation roadmap with decision gates
- Fatal flaw analysis with go/no-go assessment
- Executive summary constrained to 500 words

### When to Use
- Board-level strategy decisions
- M&A evaluation and due diligence
- Major capital investments
- Market entry decisions
- Business transformation planning

### Sample Output
```markdown
### Executive Summary (467 words)

**RECOMMENDATION**: PROCEED with acquisition at $375-425M (7.5-8.5x revenue)

**Multi-Agent Perspectives**:
- **CFO**: NPV negative at $500M, positive at $400M → negotiate down
- **COO**: Integration feasible but complex (18-24 months) → keep separate initially
- **CSO**: Strategically critical, don't lose to competitor → act now
- **CTO**: Technology sound, prefer API integration → federated architecture
- **Board**: Governance concerns, need safeguards → require fairness opinion

**Conflict Resolution**:
CFO vs CSO on price: Set hard ceiling at $425M (CFO constraint) but prioritize deal (CSO urgency)

**Synthesis**: Acquire at $300M + $125M earn-out (derisks execution)

**Expected NPV**: $95M (base case), probability-weighted $103.5M

**CONDITIONS FOR APPROVAL**:
1. Price ≤ $400M all-in
2. Founder commits 3 years minimum
3. Customer churn risk < 20%
4. API integration validated

**Fatal Flaws Assessed**: None unmitigatable ✅
```

---

## Progression of Techniques Across Examples

### Example 1 → 2: Adding Learning
- **1**: Role-based (what to do)
- **2**: Few-shot (how to do it, through examples) + Chain of thought (show reasoning)

### Example 2 → 3: Adding Exploration
- **2**: Single analysis path (straightforward)
- **3**: Multiple paths explored in parallel (Tree of Thoughts) before deciding

### Example 3 → 4: Adding Validation
- **3**: Evaluates alternatives objectively
- **4**: Validates own conclusions through self-consistency checking and red teaming

### Example 4 → 5: Adding Perspectives
- **4**: Single analyst perspective with self-checking
- **5**: Multiple expert personas with genuinely different viewpoints and incentives

---

## Complexity Comparison

| Aspect | Basic | Intermediate | Advanced | Expert | Master |
|--------|-------|--------------|----------|--------|--------|
| **Reasoning Paths** | 1 | 1 with examples | 3-5 parallel | 3 with validation | 5 agents + synthesis |
| **Self-Checking** | None | Implicit | Self-critique | Red team + recursive | Socratic + first-principles |
| **Output Structure** | Basic format | Step-by-step | Multi-dimensional | Confidence-weighted | Fully constrained |
| **Examples** | 2 examples | 2 detailed | 1 comprehensive | 1 multi-path | 1 master-level |
| **Quantification** | Minimal | Moderate | Extensive | Statistical | Financial modeling |
| **Decision Support** | Guidelines | Recommendations | Decision matrix | Risk-adjusted | Board-ready |

---

## When to Use Each Level

### Use Basic (Example 1) When:
- ✅ Clear, straightforward task with established best practices
- ✅ Need consistency across team
- ✅ Quick turnaround required
- ✅ Low risk if wrong
- **Example**: Code reviews, content moderation, basic classification

### Use Intermediate (Example 2) When:
- ✅ Need to explain reasoning to stakeholders
- ✅ Building trust through transparency
- ✅ Learning new domain/pattern
- ✅ Medium complexity with some ambiguity
- **Example**: Business analysis, data storytelling, diagnostic troubleshooting

### Use Advanced (Example 3) When:
- ✅ High-stakes decision with multiple viable alternatives
- ✅ Need rigorous evaluation of trade-offs
- ✅ Complex system with many interacting factors
- ✅ Significant investment or risk
- **Example**: Architecture decisions, technology selection, strategic planning

### Use Expert (Example 4) When:
- ✅ Research accuracy is critical
- ✅ High cost of being wrong
- ✅ Need to defend findings to skeptical audience
- ✅ Limited data requires careful inference
- **Example**: Market research, competitive intelligence, investment thesis, due diligence

### Use Master (Example 5) When:
- ✅ Board-level decisions with $MM+ impact
- ✅ Need to synthesize conflicting expert opinions
- ✅ Stakeholders have different incentives
- ✅ Requires structured decision-making framework
- **Example**: M&A decisions, major investments, corporate strategy, transformation

---

## How These Examples Were Generated

All examples were created using the **Prompt Factory skill** with different questionnaire responses:

### Generation Process:
1. **Define role and domain** (e.g., "Senior Code Reviewer", "Strategic Consultant")
2. **Specify prompting technique** (e.g., "Few-shot learning", "Multi-agent simulation")
3. **Answer 7 questions** from the Prompt Factory skill
4. **Select format** (XML for all examples)
5. **Choose mode** (Core for Examples 1-2, Advanced for Examples 3-5)

### Example Questionnaire (Example 5 - Master Level):

```
1. Role: "Senior Strategic Consultant / Management Consultant"
2. Domain: "Corporate Strategy - C-Suite Advisory"
3. Primary Goal: "Provide strategic recommendations by simulating expert perspectives"
4. Output Type: "strategy + analysis"
5. Tech Stack: "Strategy frameworks (BCG, McKinsey), scenario planning"
6. Constraints: "Must simulate diverse expert viewpoints, provide structured outputs"
7. Communication Style: "Socratic, first-principles, multi-perspectival, rigorous"

Format: XML
Mode: Advanced
```

---

## Key Takeaways

1. **Start Simple**: Use basic prompts (Example 1) for straightforward tasks
2. **Add Complexity as Needed**: Progress to advanced techniques only when justified by stakes/complexity
3. **Examples Teach**: Few-shot examples (Example 2) are highly effective for teaching patterns
4. **Multiple Paths Prevent Blind Spots**: Tree of Thoughts (Example 3) reveals alternatives you'd otherwise miss
5. **Self-Validation Builds Trust**: Self-consistency and red teaming (Example 4) catch errors before they matter
6. **Perspectives Reveal Truth**: Multi-agent simulation (Example 5) exposes conflicts and drives better synthesis

---

## Further Reading

- **Prompt Factory Skill**: [../generated-skills/prompt-factory/SKILL.md](../generated-skills/prompt-factory/SKILL.md)
- **Comprehensive Guide**: [../generated-skills/prompt-factory/HOW_TO_USE.md](../generated-skills/prompt-factory/HOW_TO_USE.md)
- **PROMPTS_FACTORY_PROMPT**: [../documentation/templates/PROMPTS_FACTORY_PROMPT.md](../documentation/templates/PROMPTS_FACTORY_PROMPT.md) (for creating domain-specific prompt builders)

---

## Contributing

To add more examples:
1. Use the Prompt Factory skill to generate a new prompt
2. Choose a unique role and prompting technique combination
3. Create detailed example showing real-world usage
4. Document the prompting technique and when to use it
5. Add to this README with summary

---

**Generated**: October 26, 2025
**Skill Used**: Prompt Factory (v1.0)
**Total Examples**: 5 (Basic → Master progression)
