"""
Context detection module for environment-aware output formatting.
Detects Claude AI Desktop vs Claude Code CLI to optimize output format.
"""

import os
import sys
from typing import Dict, Literal


class ContextDetector:
    """Detect execution environment and optimize output accordingly."""

    def __init__(self):
        """Initialize context detector."""
        self.environment = self._detect_environment()
        self.terminal_width = self._get_terminal_width()

    def _detect_environment(self) -> Literal['claude_desktop', 'claude_code', 'api', 'unknown']:
        """
        Detect which Claude environment is running.

        Returns:
            Environment type: claude_desktop, claude_code, api, or unknown
        """
        # Check for Claude Code CLI indicators
        if os.environ.get('CLAUDE_CODE'):
            return 'claude_code'

        # Check for terminal/TTY (likely CLI)
        if sys.stdout.isatty():
            return 'claude_code'

        # Check for Claude Desktop indicators
        if os.environ.get('CLAUDE_DESKTOP'):
            return 'claude_desktop'

        # Check if running in API context (no terminal, no desktop env)
        if not sys.stdout.isatty() and not os.environ.get('TERM'):
            return 'api'

        # Default to Claude Desktop (most common for interactive use)
        return 'claude_desktop'

    def _get_terminal_width(self) -> int:
        """
        Get terminal width for ASCII chart rendering.

        Returns:
            Terminal width in characters (default: 80)
        """
        try:
            import shutil
            width, _ = shutil.get_terminal_size((80, 20))
            return width
        except Exception:
            return 80

    def get_output_preferences(self) -> Dict[str, any]:
        """
        Get output format preferences based on environment.

        Returns:
            Dictionary with formatting preferences
        """
        if self.environment == 'claude_desktop':
            return {
                'environment': 'claude_desktop',
                'use_markdown_tables': True,
                'use_ascii_charts': False,
                'use_emojis': True,
                'use_colors': False,  # Markdown doesn't support ANSI colors
                'max_table_width': None,  # No limit for Claude Desktop
                'prefer_detail_level': 'high'  # Claude Desktop has good rendering
            }

        elif self.environment == 'claude_code':
            return {
                'environment': 'claude_code',
                'use_markdown_tables': True,  # Markdown works in CLI
                'use_ascii_charts': True,  # Better for terminal
                'use_emojis': False,  # Can cause rendering issues
                'use_colors': True,  # Terminal supports ANSI colors
                'max_table_width': self.terminal_width - 4,
                'prefer_detail_level': 'medium'  # Keep CLI output concise
            }

        elif self.environment == 'api':
            return {
                'environment': 'api',
                'use_markdown_tables': True,
                'use_ascii_charts': False,
                'use_emojis': False,
                'use_colors': False,
                'max_table_width': 100,
                'prefer_detail_level': 'high'
            }

        else:
            return {
                'environment': 'unknown',
                'use_markdown_tables': True,
                'use_ascii_charts': False,
                'use_emojis': False,
                'use_colors': False,
                'max_table_width': 100,
                'prefer_detail_level': 'medium'
            }

    def supports_interactive_prompts(self) -> bool:
        """
        Check if environment supports interactive prompts.

        Returns:
            True if interactive prompts are supported
        """
        return self.environment in ['claude_code'] and sys.stdout.isatty()

    def get_chart_preferences(self) -> Dict[str, any]:
        """
        Get chart rendering preferences.

        Returns:
            Dictionary with chart configuration
        """
        if self.environment == 'claude_desktop':
            return {
                'type': 'markdown_table',
                'width': None,
                'height': None,
                'use_sparklines': False
            }

        elif self.environment == 'claude_code':
            return {
                'type': 'ascii',
                'width': min(self.terminal_width - 10, 70),
                'height': 10,
                'use_sparklines': True  # Compact trend visualization
            }

        else:
            return {
                'type': 'markdown_table',
                'width': 100,
                'height': None,
                'use_sparklines': False
            }

    def should_paginate(self, content_length: int, threshold: int = 1000) -> bool:
        """
        Determine if content should be paginated.

        Args:
            content_length: Length of content in tokens/characters
            threshold: Pagination threshold

        Returns:
            True if content should be paginated
        """
        # Only paginate in CLI for very long outputs
        if self.environment == 'claude_code' and content_length > threshold:
            return True

        return False

    def get_token_budget(self, report_type: str) -> int:
        """
        Get token budget for different report types.

        Args:
            report_type: Type of report (standup, planning, review, retrospective)

        Returns:
            Recommended token budget
        """
        budgets = {
            'standup': {
                'claude_desktop': 100,
                'claude_code': 80,
                'api': 100
            },
            'planning': {
                'claude_desktop': 500,
                'claude_code': 400,
                'api': 500
            },
            'review': {
                'claude_desktop': 1000,
                'claude_code': 800,
                'api': 1000
            },
            'retrospective': {
                'claude_desktop': 500,
                'claude_code': 400,
                'api': 500
            }
        }

        report_budgets = budgets.get(report_type, {'claude_desktop': 500, 'claude_code': 400, 'api': 500})
        return report_budgets.get(self.environment, 500)

    def format_priority_indicator(self, priority: str) -> str:
        """
        Format priority indicator based on environment.

        Args:
            priority: Priority level (P0, P1, P2, P3)

        Returns:
            Formatted priority string
        """
        prefs = self.get_output_preferences()

        if prefs['use_colors'] and prefs['environment'] == 'claude_code':
            # ANSI color codes for terminal
            color_map = {
                'P0': '\033[91m',  # Red
                'P1': '\033[93m',  # Yellow
                'P2': '\033[94m',  # Blue
                'P3': '\033[90m'   # Gray
            }
            reset = '\033[0m'
            color = color_map.get(priority, '')
            return f"{color}[{priority}]{reset}"

        elif prefs['use_emojis']:
            # Emojis for Claude Desktop
            emoji_map = {
                'P0': '🔴',
                'P1': '🟡',
                'P2': '🔵',
                'P3': '⚪'
            }
            emoji = emoji_map.get(priority, '')
            return f"{emoji} [{priority}]"

        else:
            # Plain text
            return f"[{priority}]"

    def get_summary_config(self) -> Dict[str, int]:
        """
        Get configuration for summary-first output.

        Returns:
            Dictionary with line limits for different sections
        """
        if self.environment == 'claude_desktop':
            return {
                'summary_lines': 10,
                'detail_lines': 50,
                'offer_full_report': True
            }

        elif self.environment == 'claude_code':
            return {
                'summary_lines': 8,
                'detail_lines': 30,
                'offer_full_report': True
            }

        else:
            return {
                'summary_lines': 10,
                'detail_lines': 50,
                'offer_full_report': False
            }
