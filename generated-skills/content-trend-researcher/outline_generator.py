"""
Article Outline Generator
Creates comprehensive, SEO-optimized article outlines based on trend and intent analysis.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime


class OutlineGenerator:
    """Generates data-driven article outlines for content creation."""

    # Content frameworks
    FRAMEWORKS = {
        "how_to": ["Introduction", "Prerequisites", "Step-by-step Instructions", "Common Mistakes", "Conclusion"],
        "guide": ["Overview", "Background", "Main Content Sections", "Best Practices", "Resources", "Conclusion"],
        "listicle": ["Introduction", "List Items (with explanations)", "Summary", "Next Steps"],
        "comparison": ["Introduction", "Comparison Criteria", "Option Comparisons", "Recommendation", "Conclusion"],
        "case_study": ["Challenge", "Solution", "Implementation", "Results", "Key Takeaways"],
        "ultimate_guide": ["Introduction", "Fundamentals", "Intermediate Topics", "Advanced Topics", "Tools & Resources", "Conclusion"]
    }

    def __init__(
        self,
        topic: str,
        trend_data: Dict[str, Any],
        intent_data: Dict[str, Any],
        target_audience: str = "General",
        content_type: str = "article"
    ):
        """
        Initialize the outline generator.

        Args:
            topic: Main topic for the article
            trend_data: Trend analysis data
            intent_data: User intent analysis data
            target_audience: Target audience description
            content_type: Type of content (article, blog, newsletter, etc.)
        """
        self.topic = topic
        self.trend_data = trend_data
        self.intent_data = intent_data
        self.target_audience = target_audience
        self.content_type = content_type

    def generate_outlines(self, num_outlines: int = 1) -> List[Dict[str, Any]]:
        """
        Generate multiple article outlines.

        Args:
            num_outlines: Number of different outlines to generate

        Returns:
            List of article outlines
        """
        outlines = []

        # Generate different types of outlines based on intent
        primary_intent = self.intent_data.get("primary_intent", {}).get("intent", "informational")

        outline_types = self._select_outline_types(primary_intent, num_outlines)

        for i, outline_type in enumerate(outline_types):
            outline = self._generate_single_outline(outline_type, i + 1)
            outlines.append(outline)

        return outlines

    def _select_outline_types(self, intent: str, count: int) -> List[str]:
        """Select outline types based on intent."""
        type_mapping = {
            "informational": ["ultimate_guide", "how_to", "guide"],
            "commercial": ["comparison", "listicle", "guide"],
            "transactional": ["comparison", "guide", "listicle"],
            "problem_solving": ["how_to", "guide", "case_study"]
        }

        types = type_mapping.get(intent, ["guide", "how_to", "listicle"])
        return types[:count]

    def _generate_single_outline(self, outline_type: str, variant: int) -> Dict[str, Any]:
        """Generate a single article outline."""
        title = self._generate_title(outline_type, variant)
        subtitle = self._generate_subtitle(outline_type)
        word_count = self._recommend_word_count(outline_type)
        structure = self._build_structure(outline_type)
        seo_data = self._generate_seo_data()

        return {
            "outline_type": outline_type,
            "title": title,
            "subtitle": subtitle,
            "meta_description": self._generate_meta_description(title),
            "target_word_count": word_count,
            "estimated_reading_time": self._calculate_reading_time(word_count),
            "structure": structure,
            "seo_keywords": seo_data["keywords"],
            "internal_linking_opportunities": seo_data["internal_links"],
            "external_sources": seo_data["external_sources"],
            "multimedia_suggestions": self._generate_multimedia_suggestions(outline_type),
            "cta": self._generate_cta(outline_type),
            "social_media_hooks": self._generate_social_hooks(title),
            "email_newsletter_angle": self._generate_email_angle(title)
        }

    def _generate_title(self, outline_type: str, variant: int) -> str:
        """Generate SEO-optimized title based on outline type."""
        title_templates = {
            "ultimate_guide": [
                f"The Complete {self.topic} Guide for {datetime.now().year}",
                f"{self.topic}: The Ultimate Beginner to Expert Guide",
                f"Master {self.topic}: Everything You Need to Know"
            ],
            "how_to": [
                f"How to Master {self.topic} in 30 Days (Step-by-Step)",
                f"The Complete Guide to {self.topic}: From Zero to Hero",
                f"How to {self.topic}: A Practical Beginner's Guide"
            ],
            "guide": [
                f"The {self.topic} Playbook: Strategies That Actually Work",
                f"{self.topic} for Beginners: Your Complete Starter Guide",
                f"Understanding {self.topic}: A Comprehensive Guide"
            ],
            "listicle": [
                f"15 {self.topic} Tips That Will Transform Your Results",
                f"10 Game-Changing {self.topic} Strategies for {datetime.now().year}",
                f"7 {self.topic} Secrets the Experts Don't Tell You"
            ],
            "comparison": [
                f"{self.topic}: Which Option is Right for You? (Complete Comparison)",
                f"Best {self.topic} Tools Compared: Features, Pricing & More",
                f"{self.topic} Showdown: Top 5 Solutions Reviewed"
            ],
            "case_study": [
                f"How We Used {self.topic} to Achieve [Impressive Result]",
                f"{self.topic} Case Study: 6-Month Results & Lessons Learned",
                f"Real Results: Our {self.topic} Journey from Start to Success"
            ]
        }

        templates = title_templates.get(outline_type, [f"Your Guide to {self.topic}"])
        return templates[(variant - 1) % len(templates)]

    def _generate_subtitle(self, outline_type: str) -> str:
        """Generate engaging subtitle."""
        subtitles = {
            "ultimate_guide": f"A comprehensive, data-driven guide to mastering {self.topic} with proven strategies and expert insights",
            "how_to": f"Learn {self.topic} step-by-step with this practical, beginner-friendly tutorial",
            "guide": f"Discover everything you need to know about {self.topic} to get started today",
            "listicle": f"Actionable tips and proven strategies to level up your {self.topic} game",
            "comparison": f"Make informed decisions with our in-depth {self.topic} comparison",
            "case_study": f"Real-world insights and measurable results from our {self.topic} implementation"
        }
        return subtitles.get(outline_type, f"Your comprehensive resource for {self.topic}")

    def _recommend_word_count(self, outline_type: str) -> str:
        """Recommend word count based on outline type."""
        word_counts = {
            "ultimate_guide": "3500-5000",
            "how_to": "1800-2500",
            "guide": "2000-3000",
            "listicle": "1500-2000",
            "comparison": "2500-3500",
            "case_study": "2000-2800"
        }
        return word_counts.get(outline_type, "2000-2500")

    def _calculate_reading_time(self, word_count: str) -> str:
        """Calculate estimated reading time."""
        # Average reading speed: 200-250 words per minute
        avg_words = sum(map(int, word_count.split('-'))) / 2
        minutes = int(avg_words / 225)
        return f"{minutes} min read"

    def _build_structure(self, outline_type: str) -> List[Dict[str, Any]]:
        """Build detailed article structure."""
        if outline_type == "ultimate_guide":
            return self._build_ultimate_guide_structure()
        elif outline_type == "how_to":
            return self._build_how_to_structure()
        elif outline_type == "guide":
            return self._build_guide_structure()
        elif outline_type == "listicle":
            return self._build_listicle_structure()
        elif outline_type == "comparison":
            return self._build_comparison_structure()
        elif outline_type == "case_study":
            return self._build_case_study_structure()
        else:
            return self._build_guide_structure()

    def _build_ultimate_guide_structure(self) -> List[Dict[str, Any]]:
        """Build structure for ultimate guide."""
        return [
            {
                "heading": "Introduction",
                "heading_level": "H2",
                "subheadings": [
                    {"text": f"What is {self.topic}?", "level": "H3"},
                    {"text": f"Why {self.topic} matters in {datetime.now().year}", "level": "H3"},
                    {"text": "Who this guide is for", "level": "H3"}
                ],
                "key_points": [
                    "Hook with compelling stat or story",
                    f"Define {self.topic} in simple terms",
                    "Explain relevance and benefits",
                    "Set expectations for what readers will learn"
                ],
                "word_count": "300-400"
            },
            {
                "heading": f"{self.topic} Fundamentals",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Core concepts explained", "level": "H3"},
                    {"text": "Common terminology", "level": "H3"},
                    {"text": "Essential prerequisites", "level": "H3"}
                ],
                "key_points": [
                    "Cover foundational concepts",
                    "Explain key terms and definitions",
                    "List what readers need to get started",
                    "Include beginner-friendly examples"
                ],
                "word_count": "600-800"
            },
            {
                "heading": f"Getting Started with {self.topic}",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Step 1: Initial setup", "level": "H3"},
                    {"text": "Step 2: First implementation", "level": "H3"},
                    {"text": "Step 3: Best practices", "level": "H3"}
                ],
                "key_points": [
                    "Provide step-by-step instructions",
                    "Include screenshots or visuals",
                    "Highlight common beginner mistakes",
                    "Offer troubleshooting tips"
                ],
                "word_count": "700-900"
            },
            {
                "heading": f"Intermediate {self.topic} Strategies",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Optimization techniques", "level": "H3"},
                    {"text": "Advanced tools and resources", "level": "H3"},
                    {"text": "Measuring success", "level": "H3"}
                ],
                "key_points": [
                    "Build on fundamentals",
                    "Introduce optimization strategies",
                    "Recommend tools and resources",
                    "Explain success metrics"
                ],
                "word_count": "700-900"
            },
            {
                "heading": f"Advanced {self.topic} Tactics",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Expert-level techniques", "level": "H3"},
                    {"text": "Scaling strategies", "level": "H3"},
                    {"text": "Automation opportunities", "level": "H3"}
                ],
                "key_points": [
                    "Dive into advanced concepts",
                    "Share expert insights",
                    "Discuss scaling challenges",
                    "Explore automation options"
                ],
                "word_count": "600-800"
            },
            {
                "heading": "Common Challenges and Solutions",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Challenge #1 and how to overcome it", "level": "H3"},
                    {"text": "Challenge #2 and how to overcome it", "level": "H3"},
                    {"text": "Challenge #3 and how to overcome it", "level": "H3"}
                ],
                "key_points": [
                    "Address common pain points",
                    "Provide actionable solutions",
                    "Include real examples",
                    "Link to additional resources"
                ],
                "word_count": "400-600"
            },
            {
                "heading": "Conclusion",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "Summarize key takeaways",
                    "Encourage next steps",
                    "Provide additional resources",
                    "Include clear call-to-action"
                ],
                "word_count": "200-300"
            }
        ]

    def _build_how_to_structure(self) -> List[Dict[str, Any]]:
        """Build structure for how-to guide."""
        return [
            {
                "heading": "Introduction",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    f"Promise: What readers will achieve with {self.topic}",
                    "Time/difficulty estimate",
                    "Brief overview of the process"
                ],
                "word_count": "200-300"
            },
            {
                "heading": "What You'll Need",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "List required tools/resources",
                    "Prerequisites and knowledge needed",
                    "Time investment required"
                ],
                "word_count": "150-200"
            },
            {
                "heading": f"Step-by-Step: How to {self.topic}",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Step 1: [First action]", "level": "H3"},
                    {"text": "Step 2: [Second action]", "level": "H3"},
                    {"text": "Step 3: [Third action]", "level": "H3"},
                    {"text": "Step 4: [Fourth action]", "level": "H3"},
                    {"text": "Step 5: [Final action]", "level": "H3"}
                ],
                "key_points": [
                    "Clear, numbered steps",
                    "Include visuals for each step",
                    "Provide context for why each step matters",
                    "Add tips and warnings"
                ],
                "word_count": "1000-1400"
            },
            {
                "heading": "Common Mistakes to Avoid",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "List 3-5 common pitfalls",
                    "Explain how to avoid each",
                    "Share real examples if possible"
                ],
                "word_count": "300-400"
            },
            {
                "heading": "Next Steps",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "Recap what was accomplished",
                    "Suggest advanced topics to explore",
                    "Provide additional resources",
                    "Include call-to-action"
                ],
                "word_count": "200-250"
            }
        ]

    def _build_guide_structure(self) -> List[Dict[str, Any]]:
        """Build structure for general guide."""
        return [
            {
                "heading": "Introduction",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [f"Overview of {self.topic}", "What readers will learn"],
                "word_count": "200-300"
            },
            {
                "heading": f"Understanding {self.topic}",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Key concepts", "level": "H3"},
                    {"text": "Why it matters", "level": "H3"}
                ],
                "key_points": ["Define core concepts", "Explain relevance"],
                "word_count": "400-600"
            },
            {
                "heading": f"How to Implement {self.topic}",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Getting started", "level": "H3"},
                    {"text": "Best practices", "level": "H3"}
                ],
                "key_points": ["Practical implementation steps", "Proven strategies"],
                "word_count": "700-900"
            },
            {
                "heading": "Tools and Resources",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": ["Recommended tools", "Additional learning resources"],
                "word_count": "300-400"
            },
            {
                "heading": "Conclusion",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": ["Key takeaways", "Next steps"],
                "word_count": "200-300"
            }
        ]

    def _build_listicle_structure(self) -> List[Dict[str, Any]]:
        """Build structure for listicle."""
        num_items = 10

        structure = [
            {
                "heading": "Introduction",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    f"Why these {self.topic} tips matter",
                    "Promise of value from the list"
                ],
                "word_count": "150-200"
            }
        ]

        # Add list items
        for i in range(1, num_items + 1):
            structure.append({
                "heading": f"#{i}: [Specific Tip/Strategy]",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "Explain the tip",
                    "Why it works",
                    "How to implement it",
                    "Example or case study"
                ],
                "word_count": "120-150"
            })

        structure.append({
            "heading": "Wrapping Up",
            "heading_level": "H2",
            "subheadings": [],
            "key_points": [
                "Quick recap of top tips",
                "Encourage implementation",
                "Call-to-action"
            ],
            "word_count": "150-200"
        })

        return structure

    def _build_comparison_structure(self) -> List[Dict[str, Any]]:
        """Build structure for comparison article."""
        return [
            {
                "heading": "Introduction",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    f"Why choosing the right {self.topic} matters",
                    "What we'll compare",
                    "Who this comparison is for"
                ],
                "word_count": "200-300"
            },
            {
                "heading": "Comparison Criteria",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "Features",
                    "Pricing",
                    "Ease of use",
                    "Support & documentation",
                    "Performance"
                ],
                "word_count": "300-400"
            },
            {
                "heading": "Option 1: [Name]",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Pros", "level": "H3"},
                    {"text": "Cons", "level": "H3"},
                    {"text": "Best for", "level": "H3"}
                ],
                "key_points": ["Detailed analysis against criteria"],
                "word_count": "400-500"
            },
            {
                "heading": "Option 2: [Name]",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Pros", "level": "H3"},
                    {"text": "Cons", "level": "H3"},
                    {"text": "Best for", "level": "H3"}
                ],
                "key_points": ["Detailed analysis against criteria"],
                "word_count": "400-500"
            },
            {
                "heading": "Option 3: [Name]",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Pros", "level": "H3"},
                    {"text": "Cons", "level": "H3"},
                    {"text": "Best for", "level": "H3"}
                ],
                "key_points": ["Detailed analysis against criteria"],
                "word_count": "400-500"
            },
            {
                "heading": "Side-by-Side Comparison",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "Comparison table",
                    "Visual comparison if possible"
                ],
                "word_count": "200-300"
            },
            {
                "heading": "Our Recommendation",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "Best overall option",
                    "Best for specific use cases",
                    "Final verdict"
                ],
                "word_count": "300-400"
            }
        ]

    def _build_case_study_structure(self) -> List[Dict[str, Any]]:
        """Build structure for case study."""
        return [
            {
                "heading": "Executive Summary",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "Quick overview of challenge, solution, results",
                    "Key metrics achieved"
                ],
                "word_count": "150-200"
            },
            {
                "heading": "The Challenge",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Background context", "level": "H3"},
                    {"text": "The problem", "level": "H3"},
                    {"text": "Why it mattered", "level": "H3"}
                ],
                "key_points": [
                    "Describe situation before implementation",
                    "Specific pain points",
                    "Business impact of the problem"
                ],
                "word_count": "400-500"
            },
            {
                "heading": "The Solution",
                "heading_level": "H2",
                "subheadings": [
                    {"text": f"Why we chose {self.topic}", "level": "H3"},
                    {"text": "Implementation process", "level": "H3"},
                    {"text": "Timeline", "level": "H3"}
                ],
                "key_points": [
                    "Decision-making process",
                    "Implementation details",
                    "Challenges during rollout",
                    "How we overcame obstacles"
                ],
                "word_count": "600-800"
            },
            {
                "heading": "The Results",
                "heading_level": "H2",
                "subheadings": [
                    {"text": "Quantitative results", "level": "H3"},
                    {"text": "Qualitative impact", "level": "H3"}
                ],
                "key_points": [
                    "Specific metrics and improvements",
                    "ROI calculation",
                    "Unexpected benefits",
                    "Visual charts/graphs of results"
                ],
                "word_count": "500-600"
            },
            {
                "heading": "Key Takeaways",
                "heading_level": "H2",
                "subheadings": [],
                "key_points": [
                    "Lessons learned",
                    "What we'd do differently",
                    "Recommendations for others",
                    "Next steps"
                ],
                "word_count": "300-400"
            }
        ]

    def _generate_seo_data(self) -> Dict[str, Any]:
        """Generate SEO-related data."""
        return {
            "keywords": [
                self.topic,
                f"{self.topic} guide",
                f"{self.topic} tutorial",
                f"learn {self.topic}",
                f"{self.topic} tips",
                f"best {self.topic}",
                f"{self.topic} {datetime.now().year}"
            ],
            "internal_links": [
                f"Link to: {self.topic} basics article",
                f"Link to: {self.topic} tools comparison",
                f"Link to: Related topic article",
                f"Link to: Case study or example"
            ],
            "external_sources": [
                "Industry reports and statistics",
                "Expert quotes and interviews",
                "Research papers or studies",
                "Official documentation"
            ]
        }

    def _generate_meta_description(self, title: str) -> str:
        """Generate SEO meta description."""
        return f"Discover everything about {self.topic} in this comprehensive guide. Learn proven strategies, expert tips, and actionable insights to get started today."[:160]

    def _generate_multimedia_suggestions(self, outline_type: str) -> List[Dict[str, str]]:
        """Generate multimedia content suggestions."""
        suggestions = [
            {
                "type": "Featured image",
                "description": f"Eye-catching header image related to {self.topic}",
                "placement": "Top of article"
            },
            {
                "type": "Infographic",
                "description": f"Visual summary of key {self.topic} statistics or process",
                "placement": "Middle of article"
            },
            {
                "type": "Screenshots/diagrams",
                "description": "Step-by-step visual guides",
                "placement": "Throughout tutorial sections"
            },
            {
                "type": "Video embed",
                "description": f"Short explainer video about {self.topic}",
                "placement": "Introduction or conclusion"
            }
        ]

        if outline_type == "comparison":
            suggestions.append({
                "type": "Comparison table",
                "description": "Side-by-side feature comparison",
                "placement": "Comparison section"
            })

        if outline_type == "case_study":
            suggestions.append({
                "type": "Charts/graphs",
                "description": "Visual representation of results and metrics",
                "placement": "Results section"
            })

        return suggestions

    def _generate_cta(self, outline_type: str) -> Dict[str, str]:
        """Generate call-to-action recommendation."""
        ctas = {
            "ultimate_guide": {
                "type": "Resource download",
                "text": f"Download our free {self.topic} checklist",
                "placement": "End of article and sidebar"
            },
            "how_to": {
                "type": "Next step action",
                "text": f"Ready to implement? Start with our {self.topic} template",
                "placement": "Conclusion"
            },
            "guide": {
                "type": "Newsletter signup",
                "text": f"Get weekly {self.topic} tips delivered to your inbox",
                "placement": "After introduction and conclusion"
            },
            "listicle": {
                "type": "Social share",
                "text": "Found this helpful? Share it with your network",
                "placement": "After each major tip"
            },
            "comparison": {
                "type": "Tool recommendation",
                "text": "Try our recommended solution with a free trial",
                "placement": "After recommendation section"
            },
            "case_study": {
                "type": "Consultation",
                "text": "Want similar results? Book a free consultation",
                "placement": "After results section"
            }
        }

        return ctas.get(outline_type, {
            "type": "General CTA",
            "text": f"Learn more about {self.topic}",
            "placement": "End of article"
        })

    def _generate_social_hooks(self, title: str) -> List[str]:
        """Generate social media hooks for promotion."""
        return [
            f"Just published: {title} 📚",
            f"Everything you need to know about {self.topic} in one place 👇",
            f"Spent 3 months researching {self.topic}. Here's what I learned:",
            f"The {self.topic} guide I wish I had when I started 🎯"
        ]

    def _generate_email_angle(self, title: str) -> Dict[str, str]:
        """Generate email newsletter angle."""
        return {
            "subject_line": f"New guide: {title[:50]}...",
            "preview_text": f"Your complete resource for mastering {self.topic}",
            "email_intro": f"I'm excited to share our comprehensive guide to {self.topic}. Whether you're just getting started or looking to level up, this guide has you covered."
        }


def generate_article_outlines(
    topic: str,
    trend_data: Dict[str, Any],
    intent_data: Dict[str, Any],
    num_outlines: int = 1,
    target_audience: str = "General"
) -> List[Dict[str, Any]]:
    """
    Convenience function to generate article outlines.

    Args:
        topic: Topic for the articles
        trend_data: Trend analysis data
        intent_data: Intent analysis data
        num_outlines: Number of outlines to generate
        target_audience: Target audience description

    Returns:
        List of article outlines
    """
    generator = OutlineGenerator(topic, trend_data, intent_data, target_audience)
    return generator.generate_outlines(num_outlines)
