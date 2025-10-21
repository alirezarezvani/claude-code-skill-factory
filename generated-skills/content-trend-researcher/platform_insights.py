"""
Platform Insights Generator
Provides platform-specific content recommendations and publishing strategies.
"""

from typing import Dict, List, Any
from datetime import datetime, time


class PlatformInsights:
    """Generates platform-specific content recommendations."""

    # Platform characteristics
    PLATFORM_PROFILES = {
        "Medium": {
            "optimal_length": "1200-1800 words",
            "best_formats": ["Personal stories", "How-to guides", "Opinion pieces"],
            "audience": "Educated professionals, thought leaders",
            "engagement_drivers": ["Quality writing", "Unique perspective", "Strong narrative"]
        },
        "Substack": {
            "optimal_length": "800-1500 words",
            "best_formats": ["Analysis", "Commentary", "Industry insights"],
            "audience": "Niche enthusiasts, loyal subscribers",
            "engagement_drivers": ["Consistency", "Exclusive content", "Personal voice"]
        },
        "LinkedIn": {
            "optimal_length": "1000-1500 words for articles, 150-300 for posts",
            "best_formats": ["Professional insights", "Career advice", "Industry trends", "Carousels"],
            "audience": "Professionals, decision-makers, recruiters",
            "engagement_drivers": ["Professional relevance", "Actionable advice", "Personal stories"]
        },
        "Reddit": {
            "optimal_length": "Varies - detailed for guides, concise for discussions",
            "best_formats": ["AMAs", "Detailed guides", "Discussion starters"],
            "audience": "Enthusiasts, specific interest communities",
            "engagement_drivers": ["Authenticity", "Community value", "Engagement with comments"]
        },
        "X": {
            "optimal_length": "Threads: 8-12 tweets, Single: concise",
            "best_formats": ["Threads", "Quick tips", "Hot takes", "News commentary"],
            "audience": "Broad, fast-paced content consumers",
            "engagement_drivers": ["Timeliness", "Controversy", "Visual content", "Strong hooks"]
        },
        "YouTube": {
            "optimal_length": "10-20 minutes",
            "best_formats": ["Tutorials", "Reviews", "Vlogs", "Deep dives"],
            "audience": "Visual learners, broad demographics",
            "engagement_drivers": ["Thumbnail quality", "First 30 seconds", "Production value"]
        },
        "Blogs": {
            "optimal_length": "2000-3000 words",
            "best_formats": ["Comprehensive guides", "SEO-optimized articles", "Resource lists"],
            "audience": "Search-driven, solution-seeking readers",
            "engagement_drivers": ["SEO optimization", "Comprehensive coverage", "Visual elements"]
        },
        "Podcasts": {
            "optimal_length": "30-45 minutes",
            "best_formats": ["Interviews", "Solo commentary", "Roundtables"],
            "audience": "Passive consumers, commuters, multitaskers",
            "engagement_drivers": ["Audio quality", "Guest quality", "Consistent schedule"]
        }
    }

    def __init__(self, topic: str):
        """
        Initialize platform insights generator.

        Args:
            topic: The topic being researched
        """
        self.topic = topic

    def generate_platform_strategy(self, platforms: List[str]) -> Dict[str, Any]:
        """
        Generate comprehensive platform strategy.

        Args:
            platforms: List of platforms to create strategy for

        Returns:
            Platform-specific content strategies
        """
        return {
            "platform_recommendations": [
                self._generate_platform_recommendation(platform)
                for platform in platforms
            ],
            "cross_platform_strategy": self._generate_cross_platform_strategy(platforms),
            "content_calendar": self._generate_content_calendar(platforms),
            "promotion_workflow": self._generate_promotion_workflow(platforms)
        }

    def _generate_platform_recommendation(self, platform: str) -> Dict[str, Any]:
        """Generate specific recommendations for a platform."""
        profile = self.PLATFORM_PROFILES.get(platform, {})

        if platform == "Medium":
            return self._medium_strategy()
        elif platform == "Substack":
            return self._substack_strategy()
        elif platform == "LinkedIn":
            return self._linkedin_strategy()
        elif platform == "Reddit":
            return self._reddit_strategy()
        elif platform == "X":
            return self._x_strategy()
        elif platform == "YouTube":
            return self._youtube_strategy()
        elif platform == "Blogs":
            return self._blog_strategy()
        elif platform == "Podcasts":
            return self._podcast_strategy()
        else:
            return self._generic_strategy(platform, profile)

    def _medium_strategy(self) -> Dict[str, Any]:
        """Generate Medium-specific strategy."""
        return {
            "platform": "Medium",
            "content_approach": {
                "optimal_length": "1200-1800 words (8-12 min read)",
                "best_headline_types": [
                    "Personal transformation stories",
                    "Numbered lists with insights",
                    "Contrarian viewpoints",
                    "Deep expertise pieces"
                ],
                "formatting_tips": [
                    "Use compelling subtitle",
                    "Lead with strong hook",
                    "Break text with subheadings every 300-400 words",
                    "Include relevant images (3-5 per article)",
                    "Use pull quotes for key insights"
                ]
            },
            "publishing_strategy": {
                "best_days": ["Monday", "Tuesday", "Wednesday"],
                "best_times": ["9-11 AM EST", "1-3 PM EST"],
                "frequency": "2-3 times per week",
                "tag_strategy": "Use 5 tags - mix popular and niche"
            },
            "engagement_tactics": [
                "Respond to all comments within 24 hours",
                "Engage with other writers in your niche",
                "Submit to relevant publications",
                "Use Medium's partner program for monetization",
                "Build email list via newsletter CTA"
            ],
            "content_ideas": [
                f"Personal journey learning {self.topic}",
                f"5 {self.topic} lessons that changed my perspective",
                f"What nobody tells you about {self.topic}",
                f"The {self.topic} mistake I'll never make again"
            ]
        }

    def _substack_strategy(self) -> Dict[str, Any]:
        """Generate Substack-specific strategy."""
        return {
            "platform": "Substack",
            "content_approach": {
                "optimal_length": "800-1500 words",
                "newsletter_structure": [
                    "Compelling subject line (30-40 chars)",
                    "Preview text (100 chars)",
                    "Personal opening",
                    "Main content with 2-3 key points",
                    "Call-to-action",
                    "P.S. with engagement prompt"
                ],
                "voice": "Personal, conversational, authoritative"
            },
            "publishing_strategy": {
                "frequency": "Weekly (same day, same time)",
                "best_days": ["Tuesday", "Wednesday", "Thursday"],
                "best_times": ["9-10 AM EST"],
                "consistency": "CRITICAL - never skip a week"
            },
            "growth_tactics": [
                "Enable recommendations from other newsletters",
                "Cross-promote with complementary newsletters",
                "Offer free content with paid bonus sections",
                "Create compelling welcome series (3-5 emails)",
                "Share best newsletters on social media"
            ],
            "monetization": {
                "free_tier": f"Weekly {self.topic} insights and tips",
                "paid_tier": f"Deep dives, expert interviews, exclusive resources",
                "suggested_price": "$5-10/month or $50-100/year"
            },
            "content_ideas": [
                f"{self.topic} weekly roundup",
                f"Expert interview series on {self.topic}",
                f"{self.topic} trends analysis",
                f"Subscriber Q&A on {self.topic}"
            ]
        }

    def _linkedin_strategy(self) -> Dict[str, Any]:
        """Generate LinkedIn-specific strategy."""
        return {
            "platform": "LinkedIn",
            "content_approach": {
                "post_types": [
                    {
                        "type": "Carousel",
                        "length": "8-12 slides",
                        "best_for": "Step-by-step guides, data visualization",
                        "performance": "Excellent engagement"
                    },
                    {
                        "type": "Text post",
                        "length": "150-300 words",
                        "best_for": "Personal stories, quick insights",
                        "performance": "High reach"
                    },
                    {
                        "type": "Article",
                        "length": "1000-1500 words",
                        "best_for": "Thought leadership, in-depth analysis",
                        "performance": "Authority building"
                    },
                    {
                        "type": "Video",
                        "length": "1-3 minutes",
                        "best_for": "Tips, behind-the-scenes, commentary",
                        "performance": "Growing format"
                    }
                ],
                "hook_formulas": [
                    "I spent [time] learning [topic]. Here's what worked:",
                    "Everyone talks about [topic]. Nobody mentions [insight]:",
                    "3 years ago, I struggled with [problem]. Today, [result]:",
                    "[Controversial statement about topic]. Here's why:"
                ]
            },
            "publishing_strategy": {
                "frequency": "3-5 times per week",
                "best_days": ["Tuesday", "Wednesday", "Thursday"],
                "best_times": ["7-9 AM EST", "12-1 PM EST", "5-6 PM EST"],
                "post_timing": "Capture morning commute, lunch break, evening wind-down"
            },
            "engagement_tactics": [
                "Comment on posts in first hour after posting",
                "Reply to every comment on your post",
                "Use 3-5 relevant hashtags",
                "Tag relevant people (but don't overdo it)",
                "Engage with target audience's content daily"
            ],
            "content_ideas": [
                f"Career lesson from implementing {self.topic}",
                f"Data-driven {self.topic} insights (carousel)",
                f"{self.topic} transformation story",
                f"Mistakes I made with {self.topic} (and how to avoid them)"
            ]
        }

    def _reddit_strategy(self) -> Dict[str, Any]:
        """Generate Reddit-specific strategy."""
        return {
            "platform": "Reddit",
            "content_approach": {
                "critical_rules": [
                    "Read and follow subreddit rules CAREFULLY",
                    "Never self-promote without providing value first",
                    "Engage authentically - Redditors detect bs instantly",
                    "Contribute to discussions before posting your content"
                ],
                "post_types": [
                    "Detailed guides (highly valuable)",
                    "Ask Me Anything (build credibility)",
                    "Discussion starters (genuine questions)",
                    "Tool/resource shares (if genuinely helpful)"
                ],
                "formatting": [
                    "Use markdown formatting",
                    "TL;DR at top for long posts",
                    "Clear structure with headings",
                    "Include sources and citations"
                ]
            },
            "subreddit_strategy": {
                "research_phase": [
                    f"Find relevant subreddits about {self.topic}",
                    "Lurk for 1-2 weeks before posting",
                    "Understand community culture and norms",
                    "Note what content performs well"
                ],
                "participation_ratio": "10:1 (10 helpful comments for every self-promotional post)",
                "karma_building": "Build karma through helpful comments first"
            },
            "engagement_tactics": [
                "Respond to EVERY comment on your post",
                "Post during high-activity times (evenings, weekends)",
                "Use descriptive, non-clickbait titles",
                "Never delete posts - own your mistakes",
                "Cross-post carefully to relevant subs only"
            ],
            "content_ideas": [
                f"I analyzed 100+ {self.topic} resources. Here's what actually works.",
                f"[Guide] Complete beginner's roadmap to {self.topic}",
                f"What are your controversial {self.topic} opinions?",
                f"I'm a {self.topic} expert - AMA"
            ]
        }

    def _x_strategy(self) -> Dict[str, Any]:
        """Generate X (Twitter) strategy."""
        return {
            "platform": "X (Twitter)",
            "content_approach": {
                "thread_structure": [
                    "Hook tweet (controversial or intriguing statement)",
                    "Context/setup (2-3 tweets)",
                    "Main content (5-7 tweets with key points)",
                    "Conclusion with CTA",
                    "Total: 8-12 tweets optimal"
                ],
                "single_tweet_tips": [
                    "Lead with value in first 7 words",
                    "Use line breaks for readability",
                    "1-2 relevant hashtags max",
                    "Include visual when possible",
                    "Ask question to drive engagement"
                ],
                "hook_formulas": [
                    "I made [mistake] with [topic]. Cost me [result]. Here's what I learned:",
                    "[Number] [topic] tips I wish I knew [timeframe] ago:",
                    "Everyone gets [topic] wrong. Here's the truth:",
                    "Thread: How to [achieve result] using [topic]"
                ]
            },
            "publishing_strategy": {
                "frequency": "3-5 tweets/threads per day",
                "best_times": ["8-10 AM EST", "12-1 PM EST", "5-6 PM EST"],
                "content_mix": "40% educational, 30% engagement, 20% personal, 10% promotional"
            },
            "growth_tactics": [
                "Reply to large accounts in your niche",
                "Quote tweet with added value",
                "Use Twitter Spaces for community building",
                "Collaborate on threads with other creators",
                "Analyze top tweets monthly - double down on what works"
            ],
            "engagement_tactics": [
                "Reply to first 10 comments personally",
                "Like and retweet relevant content",
                "Use polls to drive interaction",
                "Quote tweet your own threads for visibility",
                "Pin your best-performing thread"
            ],
            "content_ideas": [
                f"Thread: 10 {self.topic} mistakes keeping you stuck",
                f"Daily {self.topic} tips (build consistency)",
                f"Hot take on {self.topic} trends",
                f"{self.topic} resources thread (mega-thread)"
            ]
        }

    def _youtube_strategy(self) -> Dict[str, Any]:
        """Generate YouTube strategy."""
        return {
            "platform": "YouTube",
            "content_approach": {
                "video_structure": [
                    "Hook (first 8 seconds - critical)",
                    "Intro with channel branding (5-10 sec)",
                    "Preview of what's coming",
                    "Main content with clear sections",
                    "Recap and CTA",
                    "End screen with next video suggestion"
                ],
                "optimal_lengths": {
                    "Tutorials": "15-25 minutes",
                    "Reviews": "10-15 minutes",
                    "Quick tips": "5-8 minutes",
                    "Deep dives": "30-60 minutes"
                },
                "production_tips": [
                    "Invest in good audio (more important than video)",
                    "Use B-roll to maintain visual interest",
                    "Add captions/subtitles",
                    "Chapter markers for longer videos",
                    "Consistent branding and intro/outro"
                ]
            },
            "seo_optimization": {
                "title": "Front-load keywords, add intrigue (50-60 chars)",
                "thumbnail": "High contrast, large text, emotional expression",
                "description": "First 2 lines matter most, include timestamps",
                "tags": "Mix broad and specific, 15-20 tags",
                "cards_end_screens": "Direct to related content"
            },
            "publishing_strategy": {
                "frequency": "Weekly minimum (2-3x week optimal)",
                "best_days": ["Tuesday", "Thursday", "Saturday"],
                "best_times": ["2-4 PM EST (after school)", "7-9 PM EST (evening)"],
                "consistency": "Same day/time builds habit with viewers"
            },
            "growth_tactics": [
                "Collaborate with similar-sized channels",
                "Create series/playlists for binge-watching",
                "Shorts for discovery (60 sec max)",
                "Engage in comments section",
                "Optimize older videos (evergreen content)"
            ],
            "content_ideas": [
                f"{self.topic} tutorial series (10 episodes)",
                f"I tried {self.topic} for 30 days - results",
                f"Top 10 {self.topic} tools reviewed",
                f"{self.topic} mistakes to avoid"
            ]
        }

    def _blog_strategy(self) -> Dict[str, Any]:
        """Generate blog SEO strategy."""
        return {
            "platform": "Blog (SEO-focused)",
            "content_approach": {
                "optimal_length": "2000-3000 words (varies by competition)",
                "structure": [
                    "Meta title and description (SEO optimized)",
                    "Engaging introduction with hook",
                    "Table of contents for long articles",
                    "H2/H3 subheadings with keywords",
                    "Conclusion with clear CTA",
                    "Author bio and social proof"
                ],
                "on_page_seo": [
                    "Target keyword in first paragraph",
                    "Use keyword in 2-3 H2 headings naturally",
                    "Include LSI keywords throughout",
                    "Optimize images (alt text, file names, compression)",
                    "Internal link to 3-5 related articles",
                    "External link to 2-3 authoritative sources"
                ]
            },
            "technical_seo": {
                "page_speed": "< 3 seconds load time",
                "mobile_optimization": "Mobile-first design mandatory",
                "schema_markup": "Article schema, FAQ schema",
                "url_structure": "Short, descriptive, keyword-included",
                "internal_linking": "Build topic clusters"
            },
            "publishing_strategy": {
                "frequency": "2-4 articles per week",
                "timing": "Morning (8-10 AM) for best indexing",
                "update_schedule": "Refresh top articles every 6 months"
            },
            "promotion_tactics": [
                "Share on social media (with custom graphics)",
                "Email to newsletter subscribers",
                "Submit to content aggregators",
                "Reach out for backlinks (skyscraper technique)",
                "Repurpose into other formats (video, podcast, infographic)"
            ],
            "content_ideas": [
                f"The complete {self.topic} guide ({datetime.now().year})",
                f"Best {self.topic} tools compared",
                f"{self.topic} for beginners: step-by-step",
                f"Common {self.topic} mistakes and how to fix them"
            ]
        }

    def _podcast_strategy(self) -> Dict[str, Any]:
        """Generate podcast strategy."""
        return {
            "platform": "Podcasts",
            "content_approach": {
                "episode_structure": [
                    "Intro music/branding (15-30 sec)",
                    "Host introduction",
                    "Episode preview/hook",
                    "Main content (segmented into clear sections)",
                    "Recap of key points",
                    "CTA (subscribe, review, visit website)",
                    "Outro music"
                ],
                "optimal_length": "30-45 minutes (sweet spot)",
                "recording_tips": [
                    "Use quality microphone and recording software",
                    "Record in quiet environment",
                    "Use pop filter",
                    "Edit out long pauses and filler words",
                    "Add intro/outro music for branding"
                ]
            },
            "content_formats": [
                {"format": "Solo commentary", "description": f"Your insights on {self.topic}"},
                {"format": "Interview", "description": f"Expert guests discussing {self.topic}"},
                {"format": "Co-hosted", "description": "Discussion with co-host"},
                {"format": "Storytelling", "description": f"Case studies about {self.topic}"},
                {"format": "Q&A", "description": "Listener questions answered"}
            ],
            "publishing_strategy": {
                "frequency": "Weekly (minimum for retention)",
                "best_days": ["Monday", "Wednesday", "Friday"],
                "release_time": "5-6 AM EST (for morning commuters)",
                "consistency": "Same day, same time every week"
            },
            "distribution": {
                "platforms": [
                    "Apple Podcasts (primary)",
                    "Spotify",
                    "Google Podcasts",
                    "Stitcher",
                    "Pocket Casts"
                ],
                "promotion": [
                    "Create audiograms for social media",
                    "Transcribe episodes for SEO blog posts",
                    "Guest cross-promotion",
                    "Email newsletter with episode highlights",
                    "Submit to podcast directories"
                ]
            },
            "growth_tactics": [
                "Ask for reviews/ratings at end of each episode",
                "Appear as guest on other podcasts",
                "Create bonus content for email subscribers",
                "Run listener contests/giveaways",
                "Build community (Discord, Facebook group)"
            ],
            "content_ideas": [
                f"{self.topic} expert interview series",
                f"Weekly {self.topic} news and analysis",
                f"Deep dive case studies on {self.topic}",
                f"Listener Q&A episodes"
            ]
        }

    def _generic_strategy(self, platform: str, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Generate generic strategy for uncategorized platforms."""
        return {
            "platform": platform,
            "profile": profile,
            "content_approach": {
                "optimal_length": profile.get("optimal_length", "Varies"),
                "best_formats": profile.get("best_formats", ["General content"]),
                "audience": profile.get("audience", "Platform users")
            },
            "general_tips": [
                "Research platform-specific best practices",
                "Analyze top performers in your niche",
                "Test different content types",
                "Engage authentically with community",
                "Track metrics and iterate"
            ]
        }

    def _generate_cross_platform_strategy(self, platforms: List[str]) -> Dict[str, Any]:
        """Generate strategy for coordinating across platforms."""
        return {
            "content_repurposing": {
                "core_asset": "Long-form blog article or YouTube video",
                "derivatives": [
                    "LinkedIn carousel (key points)",
                    "X thread (summarized insights)",
                    "Instagram posts (quotes/stats)",
                    "Medium article (personal angle)",
                    "Newsletter (expanded analysis)",
                    "Podcast episode (discuss topic)",
                    "Reddit post (community discussion)"
                ],
                "workflow": "Create once, distribute everywhere (COPE strategy)"
            },
            "cross_promotion": {
                "strategy": "Each platform points to others",
                "examples": [
                    "Blog → Social media teasers",
                    "YouTube → Blog post with transcript",
                    "Podcast → X thread with highlights",
                    "Newsletter → All platforms for deep dives"
                ]
            },
            "platform_priorities": self._prioritize_platforms(platforms)
        }

    def _prioritize_platforms(self, platforms: List[str]) -> List[Dict[str, str]]:
        """Prioritize platforms based on effort vs. reach."""
        priorities = {
            "Blog": {"priority": "High", "reason": "SEO brings long-term traffic"},
            "YouTube": {"priority": "High", "reason": "High engagement, searchable"},
            "LinkedIn": {"priority": "Medium-High", "reason": "Professional audience, good reach"},
            "X": {"priority": "Medium", "reason": "Good for real-time, requires consistency"},
            "Medium": {"priority": "Medium", "reason": "Built-in audience, monetization"},
            "Substack": {"priority": "Medium-High", "reason": "Direct audience, recurring revenue"},
            "Reddit": {"priority": "Low-Medium", "reason": "High effort, community-dependent"},
            "Podcasts": {"priority": "Medium", "reason": "Loyal audience, high production effort"}
        }

        return [
            {
                "platform": p,
                "priority": priorities.get(p, {}).get("priority", "Medium"),
                "reason": priorities.get(p, {}).get("reason", "Standard platform")
            }
            for p in platforms
        ]

    def _generate_content_calendar(self, platforms: List[str]) -> Dict[str, Any]:
        """Generate a sample weekly content calendar."""
        return {
            "Monday": {
                "primary": "Publish long-form blog article",
                "secondary": ["Share on LinkedIn", "Email newsletter"],
                "time_investment": "4-6 hours"
            },
            "Tuesday": {
                "primary": "X thread from blog insights",
                "secondary": ["Engage with comments on Monday's content"],
                "time_investment": "1-2 hours"
            },
            "Wednesday": {
                "primary": "LinkedIn carousel or post",
                "secondary": ["Reddit discussion (if relevant community)"],
                "time_investment": "2-3 hours"
            },
            "Thursday": {
                "primary": "Record podcast episode or YouTube video",
                "secondary": ["Respond to comments across platforms"],
                "time_investment": "3-5 hours"
            },
            "Friday": {
                "primary": "Publish podcast/YouTube",
                "secondary": ["Promote across social channels", "Plan next week's content"],
                "time_investment": "2-3 hours"
            },
            "Weekend": {
                "primary": "Research and draft next week's content",
                "secondary": ["Engage with community", "Analyze week's performance"],
                "time_investment": "3-4 hours"
            },
            "total_weekly_hours": "15-25 hours"
        }

    def _generate_promotion_workflow(self, platforms: List[str]) -> List[Dict[str, str]]:
        """Generate step-by-step promotion workflow."""
        return [
            {
                "step": "1. Create core content",
                "action": "Write blog article or record video",
                "duration": "4-6 hours"
            },
            {
                "step": "2. Optimize for distribution",
                "action": "Create graphics, pull quotes, write social copy",
                "duration": "1-2 hours"
            },
            {
                "step": "3. Publish primary platform",
                "action": "Release on main platform (blog, YouTube)",
                "duration": "30 minutes"
            },
            {
                "step": "4. Cross-post adaptations",
                "action": "Share adapted versions on other platforms",
                "duration": "1-2 hours"
            },
            {
                "step": "5. Engage first 24 hours",
                "action": "Respond to all comments, participate in discussions",
                "duration": "2-3 hours spread throughout day"
            },
            {
                "step": "6. Boost top performers",
                "action": "Analyze metrics, boost high-performing content",
                "duration": "1 hour (48 hours after publishing)"
            },
            {
                "step": "7. Repurpose insights",
                "action": "Turn into future content ideas or update existing",
                "duration": "Ongoing"
            }
        ]


def generate_platform_insights(
    topic: str,
    platforms: List[str]
) -> Dict[str, Any]:
    """
    Convenience function to generate platform insights.

    Args:
        topic: The topic being researched
        platforms: List of platforms to analyze

    Returns:
        Platform-specific strategies and recommendations
    """
    insights = PlatformInsights(topic)
    return insights.generate_platform_strategy(platforms)
