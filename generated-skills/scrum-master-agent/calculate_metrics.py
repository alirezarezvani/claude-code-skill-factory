"""
Sprint metrics calculation module.
Calculates all 6 metrics: velocity, burndown, capacity, priority, health, retrospective.
"""

from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from statistics import mean, stdev


class MetricsCalculator:
    """Calculate comprehensive sprint metrics."""

    def __init__(self, sprint_data: Dict[str, Any], historical_data: Optional[List[Dict[str, Any]]] = None):
        """
        Initialize with sprint data and optional historical data.

        Args:
            sprint_data: Current sprint data
            historical_data: List of previous sprint data for trend analysis
        """
        self.sprint_data = sprint_data
        self.historical_data = historical_data or []
        self.stories = sprint_data.get('stories', [])
        self.metrics = {}

    def safe_divide(self, numerator: float, denominator: float, default: float = 0.0) -> float:
        """Safely divide two numbers, returning default if denominator is zero."""
        if denominator == 0:
            return default
        return numerator / denominator

    def calculate_velocity(self) -> Dict[str, Any]:
        """
        Calculate velocity metrics.

        Returns:
            Dictionary with current velocity, historical average, and trend
        """
        # Current sprint velocity (completed points)
        completed_points = sum(
            story['points'] for story in self.stories
            if story['status'] == 'Done'
        )

        # Committed points
        committed_points = sum(story['points'] for story in self.stories)

        # Historical velocity
        historical_velocities = [
            sum(story['points'] for story in sprint.get('stories', []) if story['status'] == 'Done')
            for sprint in self.historical_data
        ]

        avg_velocity = mean(historical_velocities) if historical_velocities else committed_points
        velocity_trend = self._calculate_trend(historical_velocities) if len(historical_velocities) >= 3 else 'stable'

        return {
            'current': completed_points,
            'committed': committed_points,
            'completion_rate': self.safe_divide(completed_points, committed_points),
            'historical_avg': round(avg_velocity, 1),
            'trend': velocity_trend,
            'forecast_next_sprint': round(avg_velocity * 1.05 if velocity_trend == 'improving' else avg_velocity, 1)
        }

    def calculate_burndown(self) -> Dict[str, Any]:
        """
        Calculate burndown metrics and predictive completion.

        Returns:
            Dictionary with burndown data, ideal line, and predictions
        """
        # Calculate days elapsed
        start_date = self._parse_date(self.sprint_data.get('start_date'))
        end_date = self._parse_date(self.sprint_data.get('end_date'))
        today = datetime.now()

        if not start_date or not end_date:
            return {
                'error': 'Missing start_date or end_date',
                'actual_burndown': [],
                'ideal_burndown': []
            }

        total_days = (end_date - start_date).days
        days_elapsed = min((today - start_date).days, total_days)

        # Calculate actual burndown (this would ideally come from daily snapshots)
        committed_points = sum(story['points'] for story in self.stories)
        remaining_points = sum(
            story['points'] for story in self.stories
            if story['status'] != 'Done'
        )

        # Ideal burndown line
        ideal_burndown = [
            committed_points - (committed_points * (day / total_days))
            for day in range(total_days + 1)
        ]

        # Predict completion date (linear regression)
        if days_elapsed > 0:
            daily_velocity = (committed_points - remaining_points) / days_elapsed
            days_to_completion = remaining_points / daily_velocity if daily_velocity > 0 else total_days
            predicted_completion = start_date + timedelta(days=days_elapsed + days_to_completion)
        else:
            predicted_completion = end_date

        return {
            'committed_points': committed_points,
            'remaining_points': remaining_points,
            'completed_points': committed_points - remaining_points,
            'days_elapsed': days_elapsed,
            'total_days': total_days,
            'ideal_remaining': ideal_burndown[days_elapsed] if days_elapsed <= total_days else 0,
            'actual_remaining': remaining_points,
            'predicted_completion': predicted_completion.strftime('%Y-%m-%d'),
            'on_track': remaining_points <= ideal_burndown[days_elapsed] if days_elapsed <= total_days else False
        }

    def calculate_capacity(self, team_data: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Calculate team capacity metrics.

        Args:
            team_data: Optional team member data with availability

        Returns:
            Dictionary with capacity metrics
        """
        if not team_data:
            # Use sprint-level capacity if team data not provided
            total_capacity = self.sprint_data.get('team_capacity', 0)
            return {
                'total_capacity': total_capacity,
                'committed_points': sum(story['points'] for story in self.stories),
                'allocation_rate': self.safe_divide(
                    sum(story['points'] for story in self.stories),
                    total_capacity
                ),
                'buffer': total_capacity - sum(story['points'] for story in self.stories)
            }

        # Calculate from team member data
        total_capacity = sum(member['capacity'] for member in team_data)
        committed_points = sum(story['points'] for story in self.stories)

        # Calculate per-member allocation
        member_allocations = []
        for member in team_data:
            member_stories = [
                story for story in self.stories
                if story['assignee'] == member['name']
            ]
            member_points = sum(story['points'] for story in member_stories)
            member_allocations.append({
                'name': member['name'],
                'capacity': member['capacity'],
                'allocated': member_points,
                'utilization': self.safe_divide(member_points, member['capacity'])
            })

        return {
            'total_capacity': total_capacity,
            'committed_points': committed_points,
            'allocation_rate': self.safe_divide(committed_points, total_capacity),
            'buffer': total_capacity - committed_points,
            'buffer_percentage': self.safe_divide(total_capacity - committed_points, total_capacity),
            'team_members': len(team_data),
            'member_allocations': member_allocations,
            'overallocated_members': [
                m['name'] for m in member_allocations if m['utilization'] > 1.0
            ]
        }

    def calculate_priority_scores(self) -> List[Dict[str, Any]]:
        """
        Calculate priority scores for all stories.

        Formula: priority_score = (value * 2 + (10 - effort) + (10 - risk)) / 4

        Returns:
            List of stories with calculated priority scores
        """
        scored_stories = []

        for story in self.stories:
            # Skip completed stories
            if story['status'] == 'Done':
                continue

            # Value (0-10): High=10, Medium=5, Low=2
            value_map = {'High': 10, 'Medium': 5, 'Low': 2}
            value = value_map.get(story['priority'], 5)

            # Effort (0-10): Normalized from story points (inverse - lower is better)
            effort = min(story['points'], 10)

            # Risk (0-10): Based on blockers, dependencies, complexity
            risk = 0
            if story['blocked']:
                risk += 5
            if len(story.get('dependencies', [])) > 0:
                risk += 2
            if story['points'] > 8:  # Large stories are riskier
                risk += 3
            risk = min(risk, 10)

            # Calculate priority score
            priority_score = (value * 2 + (10 - effort) + (10 - risk)) / 4

            scored_stories.append({
                'id': story['id'],
                'title': story['title'],
                'points': story['points'],
                'status': story['status'],
                'priority_score': round(priority_score, 2),
                'value': value,
                'effort': effort,
                'risk': risk,
                'recommendation': self._get_priority_recommendation(priority_score)
            })

        # Sort by priority score (descending)
        scored_stories.sort(key=lambda x: x['priority_score'], reverse=True)

        return scored_stories

    def calculate_sprint_health(self) -> Dict[str, Any]:
        """
        Calculate overall sprint health score (0-100).

        Weights:
        - Velocity: 40%
        - Burndown: 30%
        - Blocked Items: 20%
        - Team Morale: 10% (optional)

        Returns:
            Dictionary with health score and breakdown
        """
        # 1. Velocity component (40%)
        velocity_metrics = self.calculate_velocity()
        velocity_score = velocity_metrics['completion_rate'] * 40

        # 2. Burndown component (30%)
        burndown_metrics = self.calculate_burndown()
        if 'error' not in burndown_metrics:
            # Compare actual vs ideal remaining
            ideal = burndown_metrics.get('ideal_remaining', 0)
            actual = burndown_metrics.get('actual_remaining', 0)
            if ideal > 0:
                burndown_score = min(1.0, ideal / actual) * 30 if actual > 0 else 30
            else:
                burndown_score = 30  # Sprint is complete
        else:
            burndown_score = 15  # Default to 50% if can't calculate

        # 3. Blocked items component (20%)
        blocked_count = sum(1 for story in self.stories if story['blocked'])
        total_stories = len([s for s in self.stories if s['status'] != 'Done'])
        blocked_rate = self.safe_divide(blocked_count, max(total_stories, 1))
        blocked_score = (1 - blocked_rate) * 20

        # 4. Team morale component (10%) - default to neutral
        morale_score = 10  # Would be set from optional input

        # Total health score
        health_score = velocity_score + burndown_score + blocked_score + morale_score

        # Determine health rating
        if health_score >= 90:
            rating = 'Excellent'
        elif health_score >= 70:
            rating = 'Good'
        elif health_score >= 50:
            rating = 'Fair'
        else:
            rating = 'At Risk'

        return {
            'health_score': round(health_score, 1),
            'rating': rating,
            'breakdown': {
                'velocity': round(velocity_score, 1),
                'burndown': round(burndown_score, 1),
                'blocked_items': round(blocked_score, 1),
                'team_morale': round(morale_score, 1)
            },
            'blocked_count': blocked_count,
            'total_stories': total_stories + blocked_count,
            'velocity_completion_rate': round(velocity_metrics['completion_rate'] * 100, 1)
        }

    def calculate_retrospective_metrics(self) -> Dict[str, Any]:
        """
        Calculate retrospective analysis metrics.

        Returns:
            Dictionary with retrospective insights
        """
        velocity_metrics = self.calculate_velocity()

        # Blocked item analysis
        blocked_stories = [story for story in self.stories if story['blocked']]
        blocked_count = len(blocked_stories)
        blocked_points = sum(story['points'] for story in blocked_stories)

        # Cycle time analysis (would be more accurate with historical status changes)
        completed_stories = [story for story in self.stories if story['status'] == 'Done']
        avg_cycle_time = self._estimate_cycle_time(completed_stories)

        # Success metrics
        committed_points = velocity_metrics['committed']
        completed_points = velocity_metrics['current']
        completion_rate = velocity_metrics['completion_rate']

        # Generate insights
        what_went_well = []
        what_needs_improvement = []

        if completion_rate >= 0.9:
            what_went_well.append(f"{int(completion_rate * 100)}% velocity achievement")
        else:
            what_needs_improvement.append(f"Only {int(completion_rate * 100)}% velocity - missed {committed_points - completed_points} points")

        if blocked_count == 0:
            what_went_well.append("Zero blocked stories")
        else:
            what_needs_improvement.append(f"{blocked_count} stories blocked ({blocked_points} points)")

        if avg_cycle_time < 5:
            what_went_well.append(f"Fast cycle time (avg {avg_cycle_time} days)")
        elif avg_cycle_time > 7:
            what_needs_improvement.append(f"Slow cycle time (avg {avg_cycle_time} days)")

        return {
            'committed_points': committed_points,
            'completed_points': completed_points,
            'completion_rate': round(completion_rate, 2),
            'blocked_count': blocked_count,
            'blocked_points': blocked_points,
            'avg_cycle_time': round(avg_cycle_time, 1),
            'completed_story_count': len(completed_stories),
            'what_went_well': what_went_well,
            'what_needs_improvement': what_needs_improvement,
            'action_items': self._generate_action_items(what_needs_improvement)
        }

    def _calculate_trend(self, values: List[float]) -> str:
        """Calculate trend from historical values."""
        if len(values) < 3:
            return 'stable'

        # Simple linear regression slope
        n = len(values)
        x = list(range(n))
        x_mean = mean(x)
        y_mean = mean(values)

        numerator = sum((x[i] - x_mean) * (values[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

        if denominator == 0:
            return 'stable'

        slope = numerator / denominator

        if slope > 1:
            return 'improving'
        elif slope < -1:
            return 'declining'
        else:
            return 'stable'

    def _parse_date(self, date_str: Optional[str]) -> Optional[datetime]:
        """Parse date string to datetime object."""
        if not date_str:
            return None

        try:
            return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        except (ValueError, AttributeError):
            try:
                return datetime.strptime(date_str, '%Y-%m-%d')
            except (ValueError, TypeError):
                return None

    def _estimate_cycle_time(self, completed_stories: List[Dict[str, Any]]) -> float:
        """Estimate average cycle time for completed stories."""
        if not completed_stories:
            return 5.0  # Default estimate

        # This is a simplified estimate - would be more accurate with actual status change history
        # For now, use a heuristic based on story size
        total_days = sum(story['points'] * 0.8 for story in completed_stories)  # Rough estimate
        return self.safe_divide(total_days, len(completed_stories), 5.0)

    def _get_priority_recommendation(self, priority_score: float) -> str:
        """Get recommendation level based on priority score."""
        if priority_score >= 8:
            return 'P0 - Critical'
        elif priority_score >= 6:
            return 'P1 - High'
        elif priority_score >= 4:
            return 'P2 - Medium'
        else:
            return 'P3 - Low'

    def _generate_action_items(self, improvements: List[str]) -> List[Dict[str, str]]:
        """Generate action items from improvement areas."""
        action_items = []

        for improvement in improvements:
            if 'blocked' in improvement.lower():
                action_items.append({
                    'priority': 'P0',
                    'action': 'Establish blocker resolution protocol',
                    'owner': 'Scrum Master',
                    'due_date': 'Next sprint start'
                })
            elif 'velocity' in improvement.lower():
                action_items.append({
                    'priority': 'P1',
                    'action': 'Review sprint planning accuracy',
                    'owner': 'Team',
                    'due_date': 'Next sprint planning'
                })
            elif 'cycle time' in improvement.lower():
                action_items.append({
                    'priority': 'P1',
                    'action': 'Reduce code review delays',
                    'owner': 'Engineering Manager',
                    'due_date': 'Within 1 week'
                })

        return action_items

    def calculate_all_metrics(self) -> Dict[str, Any]:
        """
        Calculate all metrics at once.

        Returns:
            Dictionary with all metric categories
        """
        return {
            'velocity': self.calculate_velocity(),
            'burndown': self.calculate_burndown(),
            'capacity': self.calculate_capacity(self.sprint_data.get('team')),
            'priority_scores': self.calculate_priority_scores(),
            'sprint_health': self.calculate_sprint_health(),
            'retrospective': self.calculate_retrospective_metrics()
        }
