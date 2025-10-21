"""
User Intent Analyzer
Analyzes search queries and content to determine user intent and optimize content strategy.
"""

from typing import Dict, List, Any, Tuple
import re


class IntentAnalyzer:
    """Analyzes user intent from search queries and content engagement patterns."""

    # Intent signal keywords
    INTENT_PATTERNS = {
        "informational": [
            r"\bhow to\b", r"\bwhat is\b", r"\bwhy\b", r"\bguide\b",
            r"\btutorial\b", r"\blearn\b", r"\bexplain\b", r"\bdefinition\b",
            r"\bsteps\b", r"\bprocess\b", r"\bunderstand\b", r"\bwhat are\b"
        ],
        "commercial": [
            r"\bbest\b", r"\btop\b", r"\breview\b", r"\bcompare\b",
            r"\bcomparison\b", r"\bvs\b", r"\balternative\b", r"\boption\b",
            r"\bchoose\b", r"\bselect\b", r"\bfind\b", r"\brecommend\b"
        ],
        "transactional": [
            r"\bbuy\b", r"\bpurchase\b", r"\bprice\b", r"\bcost\b",
            r"\bdeal\b", r"\bdiscount\b", r"\bcoupon\b", r"\border\b",
            r"\bshop\b", r"\bfor sale\b", r"\bsubscribe\b", r"\bsign up\b"
        ],
        "navigational": [
            r"\blogin\b", r"\bofficial\b", r"\bwebsite\b", r"\bplatform\b",
            r"\bapp\b", r"\btool\b", r"\bdashboard\b", r"\baccount\b"
        ],
        "problem_solving": [
            r"\bfix\b", r"\bsolve\b", r"\btroubleshoot\b", r"\berror\b",
            r"\bissue\b", r"\bproblem\b", r"\bnot working\b", r"\bhelp\b",
            r"\bsolution\b", r"\bresolve\b"
        ]
    }

    # Content depth signals
    DEPTH_SIGNALS = {
        "beginner": [
            r"\bbeginner\b", r"\bstart\b", r"\bintro\b", r"\bbasic\b",
            r"\b101\b", r"\bfirst time\b", r"\bfor beginners\b"
        ],
        "intermediate": [
            r"\bimprove\b", r"\boptimize\b", r"\btips\b", r"\btricks\b",
            r"\bbetter\b", r"\benhance\b", r"\badvance\b"
        ],
        "advanced": [
            r"\badvanced\b", r"\bexpert\b", r"\bpro\b", r"\bmaster\b",
            r"\bdeep dive\b", r"\bin-depth\b", r"\bcomplete\b"
        ]
    }

    def __init__(self, topic: str, queries: List[str] = None):
        """
        Initialize the intent analyzer.

        Args:
            topic: Main topic being analyzed
            queries: List of related search queries
        """
        self.topic = topic
        self.queries = queries or []

    def analyze_intent(self) -> Dict[str, Any]:
        """
        Perform comprehensive user intent analysis.

        Returns:
            Complete intent analysis report
        """
        return {
            "primary_intent": self._determine_primary_intent(),
            "intent_breakdown": self._calculate_intent_distribution(),
            "user_journey_stage": self._identify_journey_stage(),
            "content_depth_needed": self._determine_content_depth(),
            "top_questions": self._extract_top_questions(),
            "search_patterns": self._analyze_search_patterns(),
            "content_recommendations": self._generate_content_recommendations()
        }

    def _determine_primary_intent(self) -> Dict[str, Any]:
        """Determine the primary user intent for the topic."""
        # Analyze topic and queries for intent signals
        intent_scores = {
            "informational": 0,
            "commercial": 0,
            "transactional": 0,
            "navigational": 0,
            "problem_solving": 0
        }

        # Score based on topic and sample queries
        all_text = f"{self.topic} " + " ".join(self.queries)
        all_text_lower = all_text.lower()

        for intent_type, patterns in self.INTENT_PATTERNS.items():
            for pattern in patterns:
                matches = len(re.findall(pattern, all_text_lower, re.IGNORECASE))
                intent_scores[intent_type] += matches

        # Determine primary intent
        primary = max(intent_scores.items(), key=lambda x: x[1])

        return {
            "intent": primary[0],
            "confidence": self._calculate_confidence(primary[1], sum(intent_scores.values())),
            "description": self._get_intent_description(primary[0])
        }

    def _calculate_intent_distribution(self) -> Dict[str, float]:
        """Calculate percentage breakdown of different intent types."""
        # Sample distribution based on topic analysis
        # In production, this would analyze actual search data
        return {
            "informational": 65.0,
            "commercial": 20.0,
            "transactional": 8.0,
            "navigational": 5.0,
            "problem_solving": 2.0
        }

    def _identify_journey_stage(self) -> Dict[str, Any]:
        """Identify which stage of the buyer/learner journey users are in."""
        # Analyze intent to map to journey stage
        intent = self._determine_primary_intent()

        stage_mapping = {
            "informational": "Awareness",
            "commercial": "Consideration",
            "transactional": "Decision",
            "navigational": "Decision",
            "problem_solving": "Retention/Support"
        }

        stage = stage_mapping.get(intent["intent"], "Awareness")

        return {
            "stage": stage,
            "characteristics": self._get_stage_characteristics(stage),
            "content_focus": self._get_stage_content_focus(stage)
        }

    def _determine_content_depth(self) -> Dict[str, Any]:
        """Determine required content depth and complexity."""
        depth_scores = {
            "beginner": 0,
            "intermediate": 0,
            "advanced": 0
        }

        all_text = f"{self.topic} " + " ".join(self.queries)
        all_text_lower = all_text.lower()

        for depth_level, patterns in self.DEPTH_SIGNALS.items():
            for pattern in patterns:
                matches = len(re.findall(pattern, all_text_lower, re.IGNORECASE))
                depth_scores[depth_level] += matches

        # If no specific signals, default to comprehensive approach
        if sum(depth_scores.values()) == 0:
            return {
                "recommended_depth": "Beginner to Intermediate",
                "approach": "Start with basics, progress to intermediate concepts",
                "audience_level": "Mixed - cater to multiple skill levels"
            }

        primary_depth = max(depth_scores.items(), key=lambda x: x[1])[0]

        return {
            "recommended_depth": primary_depth.capitalize(),
            "approach": self._get_depth_approach(primary_depth),
            "audience_level": self._get_audience_description(primary_depth)
        }

    def _extract_top_questions(self) -> List[Dict[str, Any]]:
        """Extract top questions users are asking about the topic."""
        # Common question patterns for any topic
        return [
            {
                "question": f"What is {self.topic}?",
                "intent": "informational",
                "search_volume": "High",
                "difficulty": "Easy"
            },
            {
                "question": f"How to get started with {self.topic}?",
                "intent": "informational",
                "search_volume": "High",
                "difficulty": "Easy"
            },
            {
                "question": f"What are the benefits of {self.topic}?",
                "intent": "informational",
                "search_volume": "Medium",
                "difficulty": "Easy"
            },
            {
                "question": f"Best {self.topic} tools/resources?",
                "intent": "commercial",
                "search_volume": "High",
                "difficulty": "Medium"
            },
            {
                "question": f"How much does {self.topic} cost?",
                "intent": "transactional",
                "search_volume": "Medium",
                "difficulty": "Medium"
            },
            {
                "question": f"Common {self.topic} mistakes to avoid?",
                "intent": "informational",
                "search_volume": "Medium",
                "difficulty": "Easy"
            },
            {
                "question": f"Is {self.topic} worth it?",
                "intent": "commercial",
                "search_volume": "Medium",
                "difficulty": "Easy"
            },
            {
                "question": f"How long does it take to learn {self.topic}?",
                "intent": "informational",
                "search_volume": "Low",
                "difficulty": "Easy"
            }
        ]

    def _analyze_search_patterns(self) -> Dict[str, Any]:
        """Analyze patterns in how users search for this topic."""
        return {
            "query_patterns": {
                "how_to_queries": f"how to {self.topic}, how to learn {self.topic}, how to use {self.topic}",
                "what_queries": f"what is {self.topic}, what are {self.topic} benefits",
                "best_queries": f"best {self.topic} tools, best way to learn {self.topic}",
                "comparison_queries": f"{self.topic} vs alternatives, {self.topic} comparison"
            },
            "common_modifiers": [
                "best",
                "free",
                "tutorial",
                "guide",
                "2025",
                "for beginners",
                "tips",
                "tools"
            ],
            "long_tail_opportunities": [
                f"{self.topic} for small business",
                f"{self.topic} case study",
                f"{self.topic} implementation guide",
                f"{self.topic} best practices 2025"
            ],
            "question_keywords": [
                "how",
                "what",
                "why",
                "when",
                "where",
                "which"
            ]
        }

    def _generate_content_recommendations(self) -> List[Dict[str, Any]]:
        """Generate specific content recommendations based on intent analysis."""
        intent = self._determine_primary_intent()

        recommendations = []

        if intent["intent"] == "informational":
            recommendations.extend([
                {
                    "content_type": "Ultimate Guide",
                    "format": "Long-form article (3000+ words)",
                    "focus": f"Comprehensive {self.topic} guide from basics to advanced",
                    "priority": "High"
                },
                {
                    "content_type": "How-to Tutorial",
                    "format": "Step-by-step guide with visuals",
                    "focus": f"Getting started with {self.topic}",
                    "priority": "High"
                },
                {
                    "content_type": "Explainer Video",
                    "format": "YouTube (10-15 min)",
                    "focus": f"What is {self.topic} and why it matters",
                    "priority": "Medium"
                }
            ])

        if intent["intent"] == "commercial":
            recommendations.extend([
                {
                    "content_type": "Comparison Article",
                    "format": "In-depth comparison (2000+ words)",
                    "focus": f"Best {self.topic} tools/services comparison",
                    "priority": "High"
                },
                {
                    "content_type": "Review Roundup",
                    "format": "Listicle with pros/cons",
                    "focus": f"Top 10 {self.topic} solutions reviewed",
                    "priority": "High"
                }
            ])

        # Universal recommendations
        recommendations.extend([
            {
                "content_type": "FAQ Page",
                "format": "Structured Q&A",
                "focus": f"Common {self.topic} questions answered",
                "priority": "Medium"
            },
            {
                "content_type": "Case Study",
                "format": "Story-driven article (1500+ words)",
                "focus": f"Real-world {self.topic} success story",
                "priority": "Medium"
            }
        ])

        return recommendations

    def _calculate_confidence(self, score: int, total: int) -> str:
        """Calculate confidence level for intent classification."""
        if total == 0:
            return "Low"

        percentage = (score / total) * 100

        if percentage >= 60:
            return "High"
        elif percentage >= 40:
            return "Medium"
        else:
            return "Low"

    def _get_intent_description(self, intent: str) -> str:
        """Get description for intent type."""
        descriptions = {
            "informational": "Users want to learn and understand the topic",
            "commercial": "Users are researching options before making a decision",
            "transactional": "Users are ready to take action or make a purchase",
            "navigational": "Users are looking for a specific resource or platform",
            "problem_solving": "Users need help fixing an issue or problem"
        }
        return descriptions.get(intent, "Unknown intent type")

    def _get_stage_characteristics(self, stage: str) -> List[str]:
        """Get characteristics of journey stage."""
        characteristics = {
            "Awareness": [
                "Just discovering the topic",
                "Researching to understand basics",
                "Looking for educational content",
                "High-level information needs"
            ],
            "Consideration": [
                "Evaluating different options",
                "Comparing features and benefits",
                "Looking for proof and validation",
                "Detailed information needs"
            ],
            "Decision": [
                "Ready to commit",
                "Looking for final validation",
                "Pricing and implementation details",
                "Specific, actionable information"
            ],
            "Retention/Support": [
                "Already using the solution",
                "Encountering problems",
                "Looking for optimization",
                "Troubleshooting guidance needed"
            ]
        }
        return characteristics.get(stage, [])

    def _get_stage_content_focus(self, stage: str) -> str:
        """Get recommended content focus for stage."""
        focus = {
            "Awareness": "Educational, broad, foundational content",
            "Consideration": "Comparison, reviews, detailed feature analysis",
            "Decision": "Implementation guides, pricing, case studies",
            "Retention/Support": "Troubleshooting, optimization, advanced tips"
        }
        return focus.get(stage, "Educational content")

    def _get_depth_approach(self, depth: str) -> str:
        """Get recommended approach for content depth."""
        approaches = {
            "beginner": "Start from scratch, explain all terms, provide context",
            "intermediate": "Build on existing knowledge, focus on practical application",
            "advanced": "Dive deep into complex topics, assume prior knowledge"
        }
        return approaches.get(depth, "Comprehensive coverage")

    def _get_audience_description(self, depth: str) -> str:
        """Get audience description for depth level."""
        descriptions = {
            "beginner": "New to the topic, needs foundational knowledge",
            "intermediate": "Has basic understanding, wants to improve",
            "advanced": "Experienced, seeking expert-level insights"
        }
        return descriptions.get(depth, "Mixed skill levels")


def analyze_user_intent(
    topic: str,
    related_queries: List[str] = None
) -> Dict[str, Any]:
    """
    Convenience function to analyze user intent for a topic.

    Args:
        topic: The topic to analyze
        related_queries: List of related search queries

    Returns:
        Complete intent analysis
    """
    analyzer = IntentAnalyzer(topic, related_queries)
    return analyzer.analyze_intent()
