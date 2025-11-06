"""
Notification channel integration for Slack and Microsoft Teams.
Supports webhook-based messaging with optional/disabled by default.
"""

import json
import os
from typing import Dict, Any, Optional, List
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


class NotificationConfig:
    """Configuration manager for notification channels."""

    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize notification configuration.

        Args:
            config_file: Optional path to config YAML file
        """
        self.enabled = False
        self.channel = None
        self.slack_webhook = None
        self.teams_webhook = None

        # Try to load from config file
        if config_file and os.path.exists(config_file):
            self._load_from_file(config_file)
        else:
            # Try to load from environment variables
            self._load_from_env()

    def _load_from_file(self, config_file: str) -> None:
        """Load configuration from YAML file."""
        try:
            import yaml
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                notifications = config.get('notifications', {})
                self.enabled = notifications.get('enabled', False)
                self.channel = notifications.get('channel', 'slack')
                self.slack_webhook = notifications.get('slack_webhook')
                self.teams_webhook = notifications.get('teams_webhook')
        except ImportError:
            # yaml not available, try JSON
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    notifications = config.get('notifications', {})
                    self.enabled = notifications.get('enabled', False)
                    self.channel = notifications.get('channel', 'slack')
                    self.slack_webhook = notifications.get('slack_webhook')
                    self.teams_webhook = notifications.get('teams_webhook')
            except json.JSONDecodeError:
                pass

    def _load_from_env(self) -> None:
        """Load configuration from environment variables."""
        self.enabled = os.getenv('NOTIFY_ENABLED', 'false').lower() == 'true'
        self.channel = os.getenv('NOTIFY_CHANNEL', 'slack').lower()
        self.slack_webhook = os.getenv('SLACK_WEBHOOK_URL')
        self.teams_webhook = os.getenv('TEAMS_WEBHOOK_URL')

    def is_enabled(self) -> bool:
        """Check if notifications are enabled."""
        return self.enabled

    def get_channel(self) -> Optional[str]:
        """Get configured notification channel."""
        return self.channel if self.enabled else None

    def get_webhook_url(self) -> Optional[str]:
        """Get webhook URL for configured channel."""
        if not self.enabled:
            return None

        if self.channel == 'slack':
            return self.slack_webhook
        elif self.channel == 'teams':
            return self.teams_webhook
        return None


class SlackNotifier:
    """Slack webhook integration."""

    def __init__(self, webhook_url: str):
        """
        Initialize Slack notifier.

        Args:
            webhook_url: Slack webhook URL
        """
        self.webhook_url = webhook_url

    def send_notification(self, summary: Dict[str, Any]) -> bool:
        """
        Send notification to Slack.

        Args:
            summary: Sprint summary data

        Returns:
            True if successful, False otherwise
        """
        try:
            message = self._format_slack_message(summary)
            payload = json.dumps(message).encode('utf-8')

            request = Request(
                self.webhook_url,
                data=payload,
                headers={'Content-Type': 'application/json'}
            )

            with urlopen(request, timeout=10) as response:
                return response.status == 200

        except (URLError, HTTPError, Exception) as e:
            print(f"Slack notification failed: {e}")
            return False

    def _format_slack_message(self, summary: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format summary as Slack message (token-efficient).

        Target: 50-100 tokens max

        Args:
            summary: Sprint summary data

        Returns:
            Slack message payload
        """
        sprint_name = summary.get('sprint_name', 'Sprint')
        velocity = summary.get('velocity', {})
        health = summary.get('sprint_health', {})
        risks = summary.get('risks', [])

        # Build concise summary
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"🚀 {sprint_name} Update"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Velocity:* {velocity.get('current', 0)}/{velocity.get('committed', 0)} pts"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Health:* {health.get('health_score', 0)}/100"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Completion:* {int(velocity.get('completion_rate', 0) * 100)}%"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Status:* {health.get('rating', 'Unknown')}"
                    }
                ]
            }
        ]

        # Add risks if they exist (conditional)
        if risks:
            risk_text = "\n".join([f"• {risk}" for risk in risks[:3]])  # Top 3 risks only
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*⚠️ Risks:*\n{risk_text}"
                }
            })

        return {"blocks": blocks}


class TeamsNotifier:
    """Microsoft Teams webhook integration."""

    def __init__(self, webhook_url: str):
        """
        Initialize Teams notifier.

        Args:
            webhook_url: Teams webhook URL
        """
        self.webhook_url = webhook_url

    def send_notification(self, summary: Dict[str, Any]) -> bool:
        """
        Send notification to Microsoft Teams.

        Args:
            summary: Sprint summary data

        Returns:
            True if successful, False otherwise
        """
        try:
            message = self._format_teams_message(summary)
            payload = json.dumps(message).encode('utf-8')

            request = Request(
                self.webhook_url,
                data=payload,
                headers={'Content-Type': 'application/json'}
            )

            with urlopen(request, timeout=10) as response:
                return response.status == 200

        except (URLError, HTTPError, Exception) as e:
            print(f"Teams notification failed: {e}")
            return False

    def _format_teams_message(self, summary: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format summary as Teams Adaptive Card (token-efficient).

        Target: 50-100 tokens max

        Args:
            summary: Sprint summary data

        Returns:
            Teams message payload
        """
        sprint_name = summary.get('sprint_name', 'Sprint')
        velocity = summary.get('velocity', {})
        health = summary.get('sprint_health', {})
        risks = summary.get('risks', [])

        # Build Adaptive Card
        card = {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": {
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "type": "AdaptiveCard",
                        "version": "1.2",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": f"🚀 {sprint_name} Update",
                                "weight": "bolder",
                                "size": "large"
                            },
                            {
                                "type": "FactSet",
                                "facts": [
                                    {
                                        "title": "Velocity:",
                                        "value": f"{velocity.get('current', 0)}/{velocity.get('committed', 0)} pts"
                                    },
                                    {
                                        "title": "Health:",
                                        "value": f"{health.get('health_score', 0)}/100"
                                    },
                                    {
                                        "title": "Completion:",
                                        "value": f"{int(velocity.get('completion_rate', 0) * 100)}%"
                                    },
                                    {
                                        "title": "Status:",
                                        "value": health.get('rating', 'Unknown')
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }

        # Add risks if they exist (conditional)
        if risks:
            risk_items = [{"type": "TextBlock", "text": f"• {risk}", "wrap": True} for risk in risks[:3]]
            card["attachments"][0]["content"]["body"].append({
                "type": "TextBlock",
                "text": "⚠️ Risks:",
                "weight": "bolder",
                "spacing": "medium"
            })
            card["attachments"][0]["content"]["body"].extend(risk_items)

        return card


class NotificationManager:
    """High-level notification manager."""

    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize notification manager.

        Args:
            config_file: Optional path to config YAML file
        """
        self.config = NotificationConfig(config_file)
        self.notifier = None

        if self.config.is_enabled():
            webhook_url = self.config.get_webhook_url()
            if webhook_url:
                channel = self.config.get_channel()
                if channel == 'slack':
                    self.notifier = SlackNotifier(webhook_url)
                elif channel == 'teams':
                    self.notifier = TeamsNotifier(webhook_url)

    def send_sprint_summary(self, metrics: Dict[str, Any]) -> bool:
        """
        Send sprint summary notification.

        Args:
            metrics: Sprint metrics dictionary

        Returns:
            True if successful, False if disabled or failed
        """
        if not self.config.is_enabled() or not self.notifier:
            return False

        # Extract token-efficient summary
        summary = self._create_summary(metrics)

        return self.notifier.send_notification(summary)

    def _create_summary(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create concise summary from metrics (token-efficient).

        Args:
            metrics: Full sprint metrics

        Returns:
            Concise summary dict
        """
        velocity = metrics.get('velocity', {})
        health = metrics.get('sprint_health', {})
        priority_scores = metrics.get('priority_scores', [])

        # Identify risks (top 3 only)
        risks = []

        # Velocity risk
        if velocity.get('completion_rate', 1.0) < 0.75:
            risks.append(f"Low velocity ({int(velocity.get('completion_rate', 0) * 100)}%)")

        # Health risk
        if health.get('health_score', 100) < 60:
            risks.append(f"Health at risk ({health.get('health_score', 0)}/100)")

        # Blocked items risk
        blocked_count = len([s for s in priority_scores if s.get('blocked', False)])
        if blocked_count > 0:
            risks.append(f"{blocked_count} blocked stories")

        return {
            'sprint_name': metrics.get('sprint_name', 'Sprint'),
            'velocity': velocity,
            'sprint_health': health,
            'risks': risks[:3]  # Top 3 only
        }
