"""
Backlog prioritization module.
Advanced priority scoring with effort/value/risk analysis.
"""

from typing import Dict, List, Any, Optional
from calculate_metrics import MetricsCalculator


class BacklogPrioritizer:
    """Prioritize backlog stories using multi-factor analysis."""

    def __init__(self, sprint_data: Dict[str, Any]):
        """
        Initialize with sprint/backlog data.

        Args:
            sprint_data: Sprint data with stories
        """
        self.sprint_data = sprint_data
        self.stories = sprint_data.get('stories', [])

    def prioritize_stories(
        self,
        value_weights: Optional[Dict[str, float]] = None,
        custom_value_fn: Optional[callable] = None
    ) -> List[Dict[str, Any]]:
        """
        Prioritize stories using configurable value function.

        Args:
            value_weights: Optional custom weights for priority factors
            custom_value_fn: Optional custom value calculation function

        Returns:
            Sorted list of stories with priority scores
        """
        # Default weights: value (50%), effort (30%), risk (20%)
        weights = value_weights or {
            'value': 0.5,
            'effort': 0.3,
            'risk': 0.2
        }

        prioritized = []

        for story in self.stories:
            # Skip completed stories
            if story['status'] == 'Done':
                continue

            # Calculate factors
            value_score = self._calculate_value_score(story)
            effort_score = self._calculate_effort_score(story)
            risk_score = self._calculate_risk_score(story)

            # Apply custom function if provided
            if custom_value_fn:
                priority_score = custom_value_fn(value_score, effort_score, risk_score, story)
            else:
                # Default weighted formula
                priority_score = (
                    value_score * weights['value'] +
                    effort_score * weights['effort'] +
                    risk_score * weights['risk']
                )

            prioritized.append({
                'id': story['id'],
                'title': story['title'],
                'points': story['points'],
                'status': story['status'],
                'assignee': story['assignee'],
                'priority_score': round(priority_score, 2),
                'value_score': value_score,
                'effort_score': effort_score,
                'risk_score': risk_score,
                'recommendation': self._get_recommendation(priority_score),
                'rationale': self._generate_rationale(value_score, effort_score, risk_score)
            })

        # Sort by priority score (descending)
        prioritized.sort(key=lambda x: x['priority_score'], reverse=True)

        return prioritized

    def _calculate_value_score(self, story: Dict[str, Any]) -> float:
        """
        Calculate business value score (0-10).

        Factors:
        - Priority label (High/Medium/Low)
        - Labels (customer-facing, revenue-impact, etc.)
        - Dependencies (stories others depend on have higher value)

        Args:
            story: Story dictionary

        Returns:
            Value score (0-10)
        """
        score = 5.0  # Base score

        # Priority mapping
        priority_map = {
            'High': 3.0,
            'Medium': 0.0,
            'Low': -3.0
        }
        score += priority_map.get(story['priority'], 0.0)

        # Labels boost
        high_value_labels = [
            'customer-facing', 'revenue-impact', 'security', 'compliance',
            'critical', 'urgent', 'milestone', 'mvp'
        ]

        labels = [label.lower() for label in story.get('labels', [])]
        for label in labels:
            if any(hvl in label for hvl in high_value_labels):
                score += 1.5

        # Dependencies boost (other stories depend on this)
        # This would require checking all stories for dependencies on this story
        # Simplified: assume stories with 0 dependencies have slightly lower value
        if len(story.get('dependencies', [])) == 0:
            score += 0.5

        return min(max(score, 0), 10)  # Clamp to 0-10

    def _calculate_effort_score(self, story: Dict[str, Any]) -> float:
        """
        Calculate effort score (0-10, higher is EASIER).

        Lower story points = higher effort score (inverse relationship)

        Args:
            story: Story dictionary

        Returns:
            Effort score (0-10)
        """
        points = story['points']

        # Map story points to effort score (inverse)
        # 1-2 points = 10 (very easy)
        # 3-5 points = 7-8 (moderate)
        # 8-13 points = 3-5 (hard)
        # 13+ points = 0-2 (very hard)

        if points <= 2:
            return 10
        elif points <= 5:
            return 8 - (points - 2) * 0.5
        elif points <= 8:
            return 6 - (points - 5) * 0.5
        elif points <= 13:
            return 4 - (points - 8) * 0.4
        else:
            return max(0, 2 - (points - 13) * 0.2)

    def _calculate_risk_score(self, story: Dict[str, Any]) -> float:
        """
        Calculate risk score (0-10, higher is LOWER RISK).

        Factors:
        - Blocked status (major risk)
        - Dependencies (moderate risk)
        - Large size (complexity risk)
        - Unassigned (ownership risk)

        Args:
            story: Story dictionary

        Returns:
            Risk score (0-10)
        """
        score = 10.0  # Start with low risk

        # Blocked is a major risk
        if story.get('blocked', False):
            score -= 5.0

        # Dependencies add risk
        dep_count = len(story.get('dependencies', []))
        score -= min(dep_count * 1.5, 3.0)

        # Large stories are risky (complexity)
        if story['points'] > 8:
            score -= 2.0
        elif story['points'] > 13:
            score -= 4.0

        # Unassigned stories have ownership risk
        if story['assignee'] in ['Unassigned', '', None]:
            score -= 1.5

        # Labels indicating risk
        risk_labels = ['spike', 'research', 'experimental', 'unknown', 'complex']
        labels = [label.lower() for label in story.get('labels', [])]
        for label in labels:
            if any(rl in label for rl in risk_labels):
                score -= 1.0

        return min(max(score, 0), 10)  # Clamp to 0-10

    def _get_recommendation(self, priority_score: float) -> str:
        """Get recommendation level from priority score."""
        if priority_score >= 8.0:
            return 'P0 - Critical'
        elif priority_score >= 6.5:
            return 'P1 - High'
        elif priority_score >= 5.0:
            return 'P2 - Medium'
        else:
            return 'P3 - Low'

    def _generate_rationale(self, value: float, effort: float, risk: float) -> str:
        """Generate human-readable rationale for priority."""
        reasons = []

        # Value reasoning
        if value >= 8:
            reasons.append("high business value")
        elif value <= 3:
            reasons.append("low business value")

        # Effort reasoning
        if effort >= 8:
            reasons.append("low effort")
        elif effort <= 3:
            reasons.append("high effort")

        # Risk reasoning
        if risk <= 3:
            reasons.append("high risk")
        elif risk >= 8:
            reasons.append("low risk")

        if not reasons:
            return "balanced priority"

        return ", ".join(reasons)

    def capacity_based_sprint_allocation(
        self,
        team_capacity: int,
        buffer_percentage: float = 0.15
    ) -> Dict[str, Any]:
        """
        Allocate stories to sprint based on capacity and priority.

        Args:
            team_capacity: Total team capacity in story points
            buffer_percentage: Buffer to leave (0.15 = 15%)

        Returns:
            Dictionary with allocated stories and metrics
        """
        prioritized = self.prioritize_stories()

        # Calculate target capacity (with buffer)
        target_capacity = int(team_capacity * (1 - buffer_percentage))

        # Allocate stories
        allocated = []
        allocated_points = 0

        for story in prioritized:
            if allocated_points + story['points'] <= target_capacity:
                allocated.append(story)
                allocated_points += story['points']
            else:
                # Check if we can squeeze it in
                if allocated_points + story['points'] <= team_capacity:
                    allocated.append({
                        **story,
                        'warning': 'Exceeds target capacity but within max capacity'
                    })
                    allocated_points += story['points']

        # Remaining stories
        remaining = [s for s in prioritized if s not in allocated]

        return {
            'allocated_stories': allocated,
            'allocated_points': allocated_points,
            'team_capacity': team_capacity,
            'target_capacity': target_capacity,
            'buffer': team_capacity - allocated_points,
            'utilization': allocated_points / team_capacity,
            'remaining_backlog': remaining[:10],  # Top 10 remaining
            'allocation_recommendation': self._get_allocation_recommendation(
                allocated_points, target_capacity, team_capacity
            )
        }

    def _get_allocation_recommendation(
        self,
        allocated: int,
        target: int,
        capacity: int
    ) -> str:
        """Generate allocation recommendation."""
        utilization = allocated / capacity

        if utilization < 0.7:
            return f"Low utilization ({int(utilization * 100)}%) - consider adding more stories"
        elif utilization <= 0.85:
            return f"Good allocation ({int(utilization * 100)}%) - healthy buffer maintained"
        elif utilization <= 1.0:
            return f"High utilization ({int(utilization * 100)}%) - minimal buffer, risky"
        else:
            return f"Overallocated ({int(utilization * 100)}%) - reduce scope immediately"

    def identify_quick_wins(self, threshold_score: float = 7.5) -> List[Dict[str, Any]]:
        """
        Identify quick win stories (high value, low effort, low risk).

        Args:
            threshold_score: Minimum priority score for quick wins

        Returns:
            List of quick win stories
        """
        prioritized = self.prioritize_stories()

        quick_wins = [
            story for story in prioritized
            if story['priority_score'] >= threshold_score
            and story['effort_score'] >= 7  # Low effort
            and story['risk_score'] >= 7  # Low risk
        ]

        return quick_wins

    def flag_high_risk_stories(self, risk_threshold: float = 4.0) -> List[Dict[str, Any]]:
        """
        Flag high-risk stories that need attention.

        Args:
            risk_threshold: Maximum risk score (lower = higher risk)

        Returns:
            List of high-risk stories with recommendations
        """
        prioritized = self.prioritize_stories()

        high_risk = [
            {
                **story,
                'risk_mitigation': self._suggest_risk_mitigation(story)
            }
            for story in prioritized
            if story['risk_score'] <= risk_threshold
        ]

        return high_risk

    def _suggest_risk_mitigation(self, story: Dict[str, Any]) -> List[str]:
        """Suggest risk mitigation strategies."""
        suggestions = []

        # Find original story to check blocked status and dependencies
        original_story = next((s for s in self.stories if s['id'] == story['id']), None)

        if original_story:
            if original_story.get('blocked', False):
                suggestions.append("Unblock this story before sprint start")

            if len(original_story.get('dependencies', [])) > 0:
                suggestions.append("Ensure dependencies are resolved first")

            if original_story['points'] > 8:
                suggestions.append("Consider splitting into smaller stories")

            if original_story['assignee'] in ['Unassigned', '', None]:
                suggestions.append("Assign owner before sprint planning")

        return suggestions or ["Review complexity and unknowns"]
