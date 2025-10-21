---
name: content-trend-researcher
description: Advanced content and topic research skill that analyzes trends across Google Analytics, Google Trends, Substack, Medium, Reddit, LinkedIn, X, blogs, podcasts, and YouTube to generate data-driven article outlines based on user intent analysis
---

# Content Trend Researcher

A comprehensive content research and analysis skill designed for content creators, marketers, and publishers who need to create high-performing content based on real-world trends and user intent signals.

## What This Skill Does

This skill acts as your content intelligence system, analyzing trends across 10+ platforms to help you:

1. **Identify trending topics** - Find what's gaining traction across platforms
2. **Understand user intent** - Analyze search patterns and engagement signals
3. **Discover content gaps** - Find underserved topics with high demand
4. **Generate outlines** - Create data-driven article structures optimized for engagement
5. **Platform-specific insights** - Understand where different content types perform best

## Capabilities

### Multi-Platform Trend Analysis
- **Google Trends** - Search volume trends, rising queries, regional interest
- **Google Analytics** - Traffic patterns, user behavior, conversion signals
- **Substack** - Newsletter trends, subscriber growth patterns
- **Medium** - Article performance, tags, claps, reading time
- **Reddit** - Subreddit activity, upvotes, comment engagement, trending discussions
- **LinkedIn** - Professional content trends, engagement metrics
- **X (Twitter)** - Viral topics, hashtag performance, thread engagement
- **Blogs** - Top-ranking blog posts, backlink profiles
- **Podcasts** - Episode popularity, download trends, ratings
- **YouTube** - Video performance, view trends, watch time, engagement

### User Intent Analysis
- **Informational intent** - "How to", "What is", "Guide to"
- **Commercial intent** - "Best", "Review", "Comparison", "vs"
- **Transactional intent** - "Buy", "Pricing", "Discount"
- **Navigational intent** - Brand searches, specific resource lookups
- **Problem-solving intent** - "Fix", "Troubleshoot", "Solution"

### Content Strategy Intelligence
- Optimal content formats per platform
- Best publishing times based on engagement data
- Headline formulas with proven performance
- Content length recommendations
- Topic clustering and pillar content identification

### Outline Generation
Creates comprehensive article outlines including:
- SEO-optimized titles with user intent matching
- H2/H3 structure based on search patterns
- Key points to cover from top-performing content
- Suggested word count and content depth
- Internal linking opportunities
- Call-to-action recommendations
- Multimedia suggestions (images, videos, infographics)

## When to Use This Skill

**Before creating any content:**
- Research trending topics in your niche
- Validate content ideas with data
- Find content gaps competitors are missing
- Understand what format works best for your topic

**For content strategy:**
- Build editorial calendars based on trends
- Identify pillar content opportunities
- Plan content clusters around hot topics
- Optimize existing content for better performance

**For competitive analysis:**
- See what's working for competitors
- Find underserved audiences
- Discover new content angles
- Benchmark your performance

## Example Invocations

### Basic Topic Research
```
@content-trend-researcher

Topic: "AI automation for small businesses"
Platforms: Google Trends, Reddit, LinkedIn, YouTube
Intent: Informational
```

### Deep Platform Analysis
```
@content-trend-researcher

Topic: "Remote work productivity tools"
Platforms: ALL
Include: User intent breakdown, content gap analysis, 3 article outlines
Target audience: SaaS founders and product managers
```

### Competitive Content Research
```
@content-trend-researcher

Topic: "Email marketing strategies 2025"
Platforms: Medium, Substack, Top blogs
Analyze: Top 10 performing articles
Output: Outline that fills content gaps
```

### Multi-Format Strategy
```
@content-trend-researcher

Topic: "Sustainable fashion"
Platforms: Instagram, TikTok, YouTube, Pinterest, Blogs
Output: Platform-specific content ideas + 1 long-form blog outline
```

## Input Format

Provide the following information:

```json
{
  "topic": "Your main topic or keyword",
  "platforms": ["Google Trends", "Reddit", "YouTube", "etc."],
  "intent_focus": "informational|commercial|transactional|all",
  "target_audience": "Description of your audience",
  "content_type": "blog|article|newsletter|video script|social post",
  "analysis_depth": "quick|standard|deep",
  "number_of_outlines": 1-5
}
```

## Output Format

The skill returns a comprehensive research report:

```json
{
  "topic_overview": {
    "search_volume": "Monthly search volume estimate",
    "trend_direction": "rising|stable|declining",
    "competition_level": "low|medium|high",
    "opportunity_score": 1-100
  },
  "platform_insights": [
    {
      "platform": "Platform name",
      "trending_content": [],
      "engagement_metrics": {},
      "best_practices": [],
      "content_format": "Recommended format"
    }
  ],
  "user_intent_analysis": {
    "primary_intent": "Intent type",
    "intent_breakdown": {
      "informational": "percentage",
      "commercial": "percentage",
      "transactional": "percentage"
    },
    "top_questions": [],
    "search_patterns": []
  },
  "content_gaps": [
    {
      "gap": "Description of underserved topic",
      "opportunity": "Why this is valuable",
      "difficulty": "low|medium|high"
    }
  ],
  "article_outlines": [
    {
      "title": "SEO-optimized title",
      "subtitle": "Engaging subtitle",
      "target_word_count": 1500-2000,
      "structure": [
        {
          "heading": "H2 heading",
          "subheadings": ["H3", "H3"],
          "key_points": [],
          "research_notes": "Data supporting this section"
        }
      ],
      "seo_keywords": [],
      "internal_links": [],
      "multimedia_suggestions": [],
      "cta": "Suggested call-to-action"
    }
  ],
  "recommendations": {
    "publishing_schedule": "Best days/times",
    "content_format": "Recommended format",
    "promotion_strategy": "Where to share",
    "follow_up_topics": []
  }
}
```

## Best Practices

1. **Be specific with topics** - "AI for small business accounting" beats "AI"
2. **Choose relevant platforms** - Where your audience actually consumes content
3. **Analyze intent carefully** - Match your content to what users want
4. **Look for gaps** - The best content fills needs others miss
5. **Use data to validate** - Don't assume, verify with trend data
6. **Update regularly** - Trends change; research monthly for active topics

## Limitations

- Real-time data requires API access to platforms (not included in skill)
- Some platforms limit data access (e.g., X API changes)
- Search volume estimates are approximations
- Trend data represents past performance, not future guarantees
- Platform-specific metrics depend on data availability

## Integration with Other Skills

This skill works great combined with:
- **SEO optimization skills** - Use outlines for optimized content
- **Social media scheduling skills** - Plan promotion around trends
- **Email newsletter skills** - Create newsletters based on trending topics
- **Competitive analysis skills** - Deeper competitor research
- **Content calendar skills** - Schedule content based on trend timing

## Technical Notes

- Uses trend analysis algorithms to identify rising topics
- Intent classification based on keyword patterns and SERP analysis
- Outline generation follows proven content frameworks (AIDA, PAS, etc.)
- Platform insights based on engagement metrics and algorithm signals
- Content gap identification through comparative analysis

## Privacy & Ethics

- Does not access private user data
- Uses publicly available trend data and metrics
- Respects platform terms of service
- No scraping of paywalled or private content
- Trend analysis is statistical, not surveillance

---

**Version**: 1.0.0
**Last Updated**: October 21, 2025
**Compatibility**: Claude.ai, Claude Code, Claude API (with Code Execution Tool)
