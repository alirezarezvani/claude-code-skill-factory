"""
Context-aware output formatting module.
Generates token-efficient, environment-optimized reports.
"""

from typing import Dict, List, Any, Optional
from detect_context import ContextDetector


class OutputFormatter:
    """Format sprint metrics into context-aware reports."""

    def __init__(self, context_detector: Optional[ContextDetector] = None):
        """
        Initialize formatter with context detector.

        Args:
            context_detector: Optional ContextDetector instance
        """
        self.detector = context_detector or ContextDetector()
        self.prefs = self.detector.get_output_preferences()
        self.notification_manager = None

        # Initialize notification manager if configured
        try:
            from notify_channels import NotificationManager
            self.notification_manager = NotificationManager()
        except (ImportError, Exception):
            # Notifications not configured or module not available
            pass

    def format_standup_summary(self, metrics: Dict[str, Any], send_notification: bool = False) -> str:
        """
        Format ultra-lightweight daily standup summary.

        Target: 50-100 tokens

        Args:
            metrics: Sprint metrics dictionary
            send_notification: Whether to send notification to configured channel

        Returns:
            Formatted standup report
        """
        velocity = metrics.get('velocity', {})
        burndown = metrics.get('burndown', {})
        health = metrics.get('sprint_health', {})

        # Count stories by status
        priority_scores = metrics.get('priority_scores', [])
        in_progress = len([s for s in priority_scores if s['status'] == 'In Progress'])
        blocked = len([s for s in priority_scores if s.get('blocked', False)])

        # Build summary
        sprint_name = metrics.get('sprint_name', 'Sprint')
        emoji_prefix = "🚀 " if self.prefs['use_emojis'] else ""

        lines = [
            f"{emoji_prefix}{sprint_name} - Day {burndown.get('days_elapsed', 0)}/{burndown.get('total_days', 10)}",
            "",
            f"✅ Completed: {velocity.get('current', 0)} pts" if self.prefs['use_emojis'] else f"Completed: {velocity.get('current', 0)} pts",
            f"🔄 In Progress: {in_progress} stories" if self.prefs['use_emojis'] else f"In Progress: {in_progress} stories"
        ]

        # Only show blockers if they exist (conditional)
        if blocked > 0:
            lines.append(f"⚠️  Blocked: {blocked} stories" if self.prefs['use_emojis'] else f"ALERT - Blocked: {blocked} stories")

        # Add velocity status
        on_track = "On track" if burndown.get('on_track', False) else "Behind schedule"
        lines.append(f"\nVelocity: {on_track}")

        # Send notification if requested
        if send_notification and self.notification_manager:
            notification_sent = self.notification_manager.send_sprint_summary(metrics)
            if notification_sent:
                lines.append("")
                lines.append("✅ Notification sent" if self.prefs['use_emojis'] else "[Notification sent]")

        return "\n".join(lines)

    def format_planning_summary(self, metrics: Dict[str, Any], send_notification: bool = False) -> str:
        """
        Format sprint planning summary with priority recommendations.

        Target: 200-500 tokens

        Args:
            metrics: Sprint metrics dictionary
            send_notification: Whether to send notification to configured channel

        Returns:
            Formatted planning report
        """
        capacity = metrics.get('capacity', {})
        priority_scores = metrics.get('priority_scores', [])

        # Header
        emoji_prefix = "📊 " if self.prefs['use_emojis'] else ""
        sprint_name = metrics.get('sprint_name', 'Sprint')

        lines = [
            f"{emoji_prefix}{sprint_name} Planning Summary",
            "",
            f"Capacity: {capacity.get('total_capacity', 0)} pts | " +
            f"Committed: {capacity.get('committed_points', 0)} pts | " +
            f"Buffer: {capacity.get('buffer', 0)} pts",
            ""
        ]

        # High priority stories (top 5)
        high_priority = [s for s in priority_scores if s['recommendation'].startswith('P0') or s['recommendation'].startswith('P1')][:5]

        if high_priority:
            lines.append("High Priority Stories:")
            for story in high_priority:
                priority_indicator = self.detector.format_priority_indicator(story['recommendation'].split(' ')[0])
                lines.append(f"  {priority_indicator} {story['id']}: {story['title']} ({story['points']} pts)")

        lines.append("")

        # Recommendations
        recommendations = self._generate_planning_recommendations(metrics)
        if recommendations:
            lines.append("Recommendations:")
            for rec in recommendations:
                lines.append(f"  {rec}")

        # Send notification if requested
        if send_notification and self.notification_manager:
            notification_sent = self.notification_manager.send_sprint_summary(metrics)
            if notification_sent:
                lines.append("")
                lines.append("✅ Notification sent" if self.prefs['use_emojis'] else "[Notification sent]")

        return "\n".join(lines)

    def format_sprint_review(self, metrics: Dict[str, Any], send_notification: bool = False) -> str:
        """
        Format comprehensive sprint review report.

        Target: 500-1000 tokens

        Args:
            metrics: Sprint metrics dictionary
            send_notification: Whether to send notification to configured channel

        Returns:
            Formatted review report
        """
        velocity = metrics.get('velocity', {})
        burndown = metrics.get('burndown', {})
        health = metrics.get('sprint_health', {})

        # Header
        emoji_prefix = "📈 " if self.prefs['use_emojis'] else ""
        sprint_name = metrics.get('sprint_name', 'Sprint')

        lines = [
            f"{emoji_prefix}{sprint_name} Review",
            "",
            "## Velocity Metrics"
        ]

        # Velocity table
        if self.prefs['use_markdown_tables']:
            lines.extend([
                "",
                "| Metric | Value |",
                "|--------|-------|",
                f"| Committed Points | {velocity.get('committed', 0)} |",
                f"| Completed Points | {velocity.get('current', 0)} |",
                f"| Completion Rate | {int(velocity.get('completion_rate', 0) * 100)}% |",
                f"| Historical Avg | {velocity.get('historical_avg', 0)} |",
                f"| Trend | {velocity.get('trend', 'stable').title()} |",
                ""
            ])
        else:
            lines.extend([
                f"  Committed: {velocity.get('committed', 0)} pts",
                f"  Completed: {velocity.get('current', 0)} pts",
                f"  Rate: {int(velocity.get('completion_rate', 0) * 100)}%",
                f"  Trend: {velocity.get('trend', 'stable').title()}",
                ""
            ])

        # Burndown analysis
        lines.append("## Burndown Analysis")
        lines.append("")

        if self.prefs['use_ascii_charts']:
            # ASCII chart for CLI
            chart = self._create_ascii_burndown_chart(burndown)
            lines.extend(chart)
        else:
            # Markdown table for Claude Desktop
            lines.extend([
                "| Metric | Value |",
                "|--------|-------|",
                f"| Days Elapsed | {burndown.get('days_elapsed', 0)}/{burndown.get('total_days', 0)} |",
                f"| Remaining Points | {burndown.get('remaining_points', 0)} |",
                f"| Predicted Completion | {burndown.get('predicted_completion', 'N/A')} |",
                f"| On Track | {'Yes' if burndown.get('on_track', False) else 'No'} |",
                ""
            ])

        # Sprint health
        lines.append("## Sprint Health Score")
        lines.append("")
        lines.append(f"**Overall: {health.get('health_score', 0)}/100 - {health.get('rating', 'Unknown')}**")
        lines.append("")

        breakdown = health.get('breakdown', {})
        lines.extend([
            f"- Velocity: {breakdown.get('velocity', 0)}/40",
            f"- Burndown: {breakdown.get('burndown', 0)}/30",
            f"- Blocked Items: {breakdown.get('blocked_items', 0)}/20",
            f"- Team Morale: {breakdown.get('team_morale', 0)}/10",
            ""
        ])

        # Risk alerts (conditional)
        risks = self._identify_risks(metrics)
        if risks:
            lines.append("## Risk Alerts")
            lines.append("")
            for risk in risks:
                risk_emoji = "⚠️ " if self.prefs['use_emojis'] else "ALERT: "
                lines.append(f"{risk_emoji}{risk}")
            lines.append("")

        # Send notification if requested
        if send_notification and self.notification_manager:
            notification_sent = self.notification_manager.send_sprint_summary(metrics)
            if notification_sent:
                lines.append("---")
                lines.append("")
                lines.append("✅ Notification sent to configured channel" if self.prefs['use_emojis'] else "[Notification sent to configured channel]")

        return "\n".join(lines)

    def format_retrospective(self, metrics: Dict[str, Any], send_notification: bool = False) -> str:
        """
        Format retrospective analysis report.

        Target: 300-500 tokens

        Args:
            metrics: Sprint metrics dictionary
            send_notification: Whether to send notification to configured channel

        Returns:
            Formatted retrospective report
        """
        retro = metrics.get('retrospective', {})

        # Header
        emoji_prefix = "🔍 " if self.prefs['use_emojis'] else ""
        sprint_name = metrics.get('sprint_name', 'Sprint')

        lines = [
            f"{emoji_prefix}{sprint_name} Retrospective",
            "",
            "## What Went Well"
        ]

        # What went well
        went_well = retro.get('what_went_well', [])
        if went_well:
            for item in went_well:
                check_emoji = "✅ " if self.prefs['use_emojis'] else "- "
                lines.append(f"{check_emoji}{item}")
        else:
            lines.append("- No significant highlights")

        lines.append("")
        lines.append("## What Needs Improvement")

        # What needs improvement
        needs_improvement = retro.get('what_needs_improvement', [])
        if needs_improvement:
            for item in needs_improvement:
                warning_emoji = "⚠️  " if self.prefs['use_emojis'] else "- "
                lines.append(f"{warning_emoji}{item}")
        else:
            lines.append("- No significant issues")

        lines.append("")
        lines.append("## Action Items")

        # Action items
        action_items = retro.get('action_items', [])
        if action_items:
            for item in action_items:
                priority_indicator = self.detector.format_priority_indicator(item.get('priority', 'P2'))
                lines.append(f"{priority_indicator} {item.get('action', 'Action')} (Owner: {item.get('owner', 'TBD')}, Due: {item.get('due_date', 'TBD')})")
        else:
            lines.append("- No action items")

        lines.append("")

        # Send notification if requested
        if send_notification and self.notification_manager:
            notification_sent = self.notification_manager.send_sprint_summary(metrics)
            if notification_sent:
                lines.append("---")
                lines.append("")
                lines.append("✅ Notification sent to configured channel" if self.prefs['use_emojis'] else "[Notification sent to configured channel]")

        return "\n".join(lines)

    def format_json_export(self, metrics: Dict[str, Any]) -> str:
        """
        Format metrics as JSON for tool integration.

        Args:
            metrics: Sprint metrics dictionary

        Returns:
            JSON string
        """
        import json

        export_data = {
            'sprint_name': metrics.get('sprint_name', 'Unknown'),
            'metrics': {
                'velocity': metrics.get('velocity', {}),
                'burndown': metrics.get('burndown', {}),
                'capacity': metrics.get('capacity', {}),
                'health_score': metrics.get('sprint_health', {})
            },
            'priority_scores': metrics.get('priority_scores', [])[:10],  # Top 10 only
            'retrospective': metrics.get('retrospective', {}),
            'risks': self._identify_risks(metrics)
        }

        return json.dumps(export_data, indent=2)

    def _create_ascii_burndown_chart(self, burndown: Dict[str, Any]) -> List[str]:
        """Create ASCII burndown chart for terminal."""
        chart_prefs = self.detector.get_chart_preferences()
        width = chart_prefs['width']
        height = chart_prefs['height']

        total_days = burndown.get('total_days', 10)
        committed_points = burndown.get('committed_points', 100)
        remaining_points = burndown.get('remaining_points', 50)
        days_elapsed = burndown.get('days_elapsed', 5)

        lines = ["```"]
        lines.append(f"Burndown Chart ({committed_points} pts)")
        lines.append("")

        # Simple ASCII representation
        ideal_remaining = committed_points - (committed_points * (days_elapsed / total_days))

        # Create bars
        max_points = committed_points
        ideal_bar_width = int((ideal_remaining / max_points) * (width - 20))
        actual_bar_width = int((remaining_points / max_points) * (width - 20))

        lines.append(f"Ideal:  {'=' * ideal_bar_width} {int(ideal_remaining)} pts")
        lines.append(f"Actual: {'=' * actual_bar_width} {remaining_points} pts")
        lines.append("")
        lines.append(f"Day {days_elapsed}/{total_days}")
        lines.append("```")

        return lines

    def _generate_planning_recommendations(self, metrics: Dict[str, Any]) -> List[str]:
        """Generate planning recommendations based on metrics."""
        recommendations = []

        capacity = metrics.get('capacity', {})
        priority_scores = metrics.get('priority_scores', [])
        health = metrics.get('sprint_health', {})

        # Check allocation
        allocation_rate = capacity.get('allocation_rate', 0)
        if allocation_rate > 1.0:
            recommendations.append(f"P0: Overallocated by {int((allocation_rate - 1.0) * 100)}% - reduce scope")
        elif allocation_rate < 0.7:
            recommendations.append(f"P2: Only {int(allocation_rate * 100)}% allocated - consider adding stories")

        # Check for large stories
        large_stories = [s for s in priority_scores if s['points'] > 8]
        if large_stories:
            recommendations.append(f"P1: {len(large_stories)} stories over 8 pts - consider splitting")

        # Check for blockers
        blocked = [s for s in priority_scores if s.get('blocked', False)]
        if blocked:
            recommendations.append(f"P0: {len(blocked)} blocked stories - resolve before sprint start")

        return recommendations[:5]  # Top 5 recommendations

    def _identify_risks(self, metrics: Dict[str, Any]) -> List[str]:
        """Identify sprint risks from metrics."""
        risks = []

        velocity = metrics.get('velocity', {})
        burndown = metrics.get('burndown', {})
        health = metrics.get('sprint_health', {})
        priority_scores = metrics.get('priority_scores', [])

        # Velocity risk
        if velocity.get('completion_rate', 1.0) < 0.75:
            risks.append(f"Low velocity - only {int(velocity.get('completion_rate', 0) * 100)}% complete")

        # Burndown risk
        if not burndown.get('on_track', True):
            predicted = burndown.get('predicted_completion', 'Unknown')
            risks.append(f"Behind schedule - predicted completion: {predicted}")

        # Health score risk
        if health.get('health_score', 100) < 60:
            risks.append(f"Sprint health at risk - score: {health.get('health_score', 0)}/100")

        # Blocked items risk
        blocked_count = health.get('blocked_count', 0)
        if blocked_count > 0:
            risks.append(f"{blocked_count} stories blocked")

        return risks
