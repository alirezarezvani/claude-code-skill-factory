# How to Use /marketing-research

A comprehensive marketing research slash command that analyzes market opportunities, audience insights, competitive positioning, and delivers data-driven marketing strategies.

---

## Installation

### Option 1: Project-Level (Recommended for Teams)
```bash
# Copy to your project's .claude/commands/ folder
cp marketing-research.md /path/to/your-project/.claude/commands/

# Now available to all team members working on the project
```

### Option 2: User-Level (Available Everywhere)
```bash
# Copy to your global Claude Code commands folder
cp marketing-research.md ~/.claude/commands/

# Now available in all Claude Code sessions
```

---

## Usage

### Basic Usage
```
/marketing-research Nike Athletic Footwear
```

### With Industry Context
```
/marketing-research Tesla Electric Vehicles
```

### With Product Specificity
```
/marketing-research HubSpot Marketing Automation B2B SaaS
```

---

## What It Does

This command performs comprehensive marketing research covering:

### 1. Market & Audience Analysis
- Target audience profiling (demographics, psychographics, behavioral patterns)
- Customer journey mapping (Awareness → Consideration → Decision → Retention)
- Market segmentation with priorities
- Positioning and messaging framework per segment

### 2. Competitive Marketing Analysis
- Top 3-5 competitors with brand positioning
- Marketing mix analysis (4Ps: Product, Price, Place, Promotion)
- Campaign examples and creative approaches
- USP identification

### 3. Digital Marketing Landscape
- Channel performance (SEO, Content, Social, Paid Ads, Email, Influencer)
- Marketing technology stack analysis
- Budget allocation insights
- Analytics and attribution systems

### 4. Content & Creative Strategy
- Content themes and topics with engagement data
- Content formats and messaging tone
- Campaign analysis with metrics
- Visual identity patterns

### 5. Marketing Opportunities & Strategy
- Market gaps and underserved segments
- Recommended marketing strategy with budget allocation
- Campaign ideas with expected ROI
- Quick wins (30 days) and long-term initiatives (3-12 months)
- Success metrics and KPIs

### 6. Deliverable
Complete marketing research report including:
- Executive summary (2-3 pages)
- Detailed analysis (10-15 pages)
- Action plan (1-2 pages)
- Appendix with sources and references

---

## Output Structure

The command generates:

```
marketing-research-report.md
├── Executive Summary
│   ├── Key Findings
│   ├── Strategic Recommendations
│   └── Priority Action Items
├── Detailed Analysis
│   ├── Audience Personas
│   ├── Competitive Matrix
│   ├── Channel Opportunities
│   └── Content Strategy
├── Action Plan
│   ├── 30-Day Quick Wins
│   ├── 90-Day Roadmap
│   ├── Budget Recommendations
│   └── Resource Requirements
└── Appendix
    ├── Data Sources
    ├── Competitor Profiles
    └── Research References
```

---

## Examples

### Example 1: New Product Launch
```
/marketing-research Apple Vision Pro Spatial Computing
```

**Result**: Comprehensive marketing research for Apple Vision Pro covering target audience (early adopters, tech enthusiasts, creative professionals), competitive analysis vs Meta Quest, content strategy for spatial computing education, and go-to-market recommendations.

---

### Example 2: Brand Repositioning
```
/marketing-research Patagonia Sustainable Outdoor Apparel
```

**Result**: Market analysis of sustainable outdoor segment, competitive positioning vs REI/North Face, audience insights on eco-conscious consumers, content strategy for environmental activism, and brand differentiation recommendations.

---

### Example 3: Market Entry Strategy
```
/marketing-research Stripe Payment Processing European Market
```

**Result**: European payment processing landscape, local competitors (Adyen, Klarna), regulatory considerations, localization strategy, partnership opportunities, and phased market entry plan.

---

## Success Criteria

You know the command succeeded when you get:
- ✅ Comprehensive audience analysis with actionable personas
- ✅ Data-driven competitive intelligence with specific examples
- ✅ Clear marketing strategy with channel prioritization
- ✅ Realistic action plan with ROI projections
- ✅ Deliverable ready for marketing team execution

---

## Tips for Best Results

1. **Be Specific**: Include company/product name and industry context
   - Good: `/marketing-research Notion Productivity SaaS`
   - Less good: `/marketing-research productivity tool`

2. **Add Industry Context**: Helps narrow competitive analysis
   - Good: `/marketing-research Peloton Connected Fitness`
   - Less good: `/marketing-research Peloton`

3. **Follow Up**: Ask clarifying questions if needed
   - "Can you expand on the influencer marketing opportunities?"
   - "What would a 30-day content calendar look like?"

4. **Combine with Other Commands**: Use research to inform strategy
   - `/marketing-research` → `/content-strategy` → `/campaign-plan`

---

## Command Structure

This command follows **Pattern A: Simple** from official Anthropic documentation:
- ✅ **Context → Task** structure for straightforward workflows
- ✅ Uses `$ARGUMENTS` for flexible argument handling
- ✅ Specific bash permissions (`Bash(find:*)`, `Bash(grep:*)`) - never wildcard
- ✅ Clear success criteria and deliverable format

---

## Validation

This command has been validated with the slash-command-factory v2.0 validator:
- ✅ YAML frontmatter properly formatted
- ✅ Uses $ARGUMENTS (not positional $1, $2, $3)
- ✅ Includes argument-hint for user guidance
- ✅ Bash permissions are specific (no wildcard)
- ✅ Follows official Anthropic patterns

---

## Troubleshooting

**Issue**: Command not found
- **Solution**: Make sure you copied the file to `.claude/commands/` or `~/.claude/commands/`
- **Check**: Run `ls ~/.claude/commands/` to verify file is present

**Issue**: Generic results
- **Solution**: Provide more specific company/product and industry context in arguments
- **Example**: Instead of "fitness app", use "Strava Social Fitness Tracking"

**Issue**: Missing competitive data
- **Solution**: Ask follow-up questions about specific competitors you want analyzed
- **Example**: "Can you do deeper analysis on Nike's content strategy?"

---

## Generated With

This slash command was generated using [slash-command-factory v2.0](../../generated-skills/slash-command-factory/) following official Anthropic patterns for Claude Code slash commands.

**Version**: v2.0
**Pattern**: Simple (Context → Task)
**Validation**: ✅ All checks passed
**Compatible With**: Claude Code (all platforms)
