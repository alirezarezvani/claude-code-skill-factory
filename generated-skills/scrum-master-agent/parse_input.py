"""
Multi-format input parser for Scrum Master Agent.
Handles JSON, CSV, YAML formats with automatic format detection.
"""

import json
import csv
import yaml
from typing import Dict, List, Any, Optional
from io import StringIO


class InputParser:
    """Parse sprint data from multiple formats."""

    def __init__(self, data: str, format_hint: Optional[str] = None):
        """
        Initialize parser with data string.

        Args:
            data: Raw input data as string
            format_hint: Optional format hint ('json', 'csv', 'yaml')
        """
        self.data = data
        self.format_hint = format_hint
        self.parsed_data = {}

    def detect_format(self) -> str:
        """
        Auto-detect input format based on content.

        Returns:
            Format type: 'json', 'csv', or 'yaml'
        """
        if self.format_hint:
            return self.format_hint

        stripped = self.data.strip()

        # JSON detection
        if stripped.startswith('{') or stripped.startswith('['):
            return 'json'

        # YAML detection (starts with key: or ---)
        if stripped.startswith('---') or ':' in stripped.split('\n')[0]:
            # Check if it's CSV (has commas in first line)
            if ',' in stripped.split('\n')[0]:
                return 'csv'
            return 'yaml'

        # CSV detection (default for comma-separated data)
        if ',' in stripped.split('\n')[0]:
            return 'csv'

        # Default to JSON
        return 'json'

    def parse(self) -> Dict[str, Any]:
        """
        Parse input data based on detected format.

        Returns:
            Normalized dictionary with sprint data
        """
        format_type = self.detect_format()

        if format_type == 'json':
            return self._parse_json()
        elif format_type == 'csv':
            return self._parse_csv()
        elif format_type == 'yaml':
            return self._parse_yaml()
        else:
            raise ValueError(f"Unsupported format: {format_type}")

    def _parse_json(self) -> Dict[str, Any]:
        """Parse JSON input."""
        try:
            data = json.loads(self.data)
            return self._normalize_structure(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {str(e)}")

    def _parse_csv(self) -> Dict[str, Any]:
        """Parse CSV input."""
        try:
            reader = csv.DictReader(StringIO(self.data))
            stories = [row for row in reader]

            # Build normalized structure
            return {
                'sprint_name': 'Sprint (from CSV)',
                'start_date': None,
                'end_date': None,
                'team_capacity': 0,
                'stories': self._normalize_stories(stories)
            }
        except Exception as e:
            raise ValueError(f"Invalid CSV: {str(e)}")

    def _parse_yaml(self) -> Dict[str, Any]:
        """Parse YAML input."""
        try:
            data = yaml.safe_load(self.data)
            return self._normalize_structure(data)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML: {str(e)}")

    def _normalize_structure(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize data structure to standard format.

        Args:
            data: Raw parsed data

        Returns:
            Normalized sprint data structure
        """
        normalized = {
            'tool': data.get('tool', 'unknown'),
            'sprint_name': data.get('sprint_name', data.get('sprint', {}).get('name', 'Unknown Sprint')),
            'start_date': data.get('start_date', data.get('sprint', {}).get('start_date')),
            'end_date': data.get('end_date', data.get('sprint', {}).get('end_date')),
            'team_capacity': data.get('team_capacity', data.get('sprint', {}).get('capacity', 0)),
            'stories': self._normalize_stories(data.get('stories', data.get('issues', [])))
        }

        # Extract team data if present
        if 'team' in data or ('sprint' in data and 'team' in data['sprint']):
            team_data = data.get('team', data.get('sprint', {}).get('team', []))
            normalized['team'] = self._normalize_team(team_data)

        return normalized

    def _normalize_stories(self, stories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Normalize story data to standard format.

        Args:
            stories: List of story dictionaries

        Returns:
            Normalized story list
        """
        normalized = []

        for story in stories:
            normalized_story = {
                'id': story.get('story_id', story.get('id', story.get('key', 'UNKNOWN'))),
                'title': story.get('title', story.get('summary', story.get('name', 'Untitled'))),
                'points': self._parse_points(story.get('points', story.get('story_points', story.get('estimate', 0)))),
                'status': self._normalize_status(story.get('status', 'Todo')),
                'assignee': story.get('assignee', story.get('assigned_to', 'Unassigned')),
                'priority': self._normalize_priority(story.get('priority', 'Medium')),
                'blocked': self._parse_boolean(story.get('blocked', story.get('is_blocked', False))),
                'created_date': story.get('created_date', story.get('created', None)),
                'labels': story.get('labels', story.get('tags', [])),
                'dependencies': story.get('dependencies', [])
            }

            normalized.append(normalized_story)

        return normalized

    def _normalize_team(self, team: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Normalize team member data.

        Args:
            team: List of team member dictionaries

        Returns:
            Normalized team list
        """
        normalized = []

        for member in team:
            normalized_member = {
                'name': member.get('name', 'Unknown'),
                'capacity': member.get('capacity', member.get('points', 40)),
                'availability': member.get('availability', member.get('available_days', 10))
            }
            normalized.append(normalized_member)

        return normalized

    def _parse_points(self, points: Any) -> int:
        """
        Parse story points to integer.

        Args:
            points: Story points (could be int, str, or T-shirt size)

        Returns:
            Normalized story points
        """
        if isinstance(points, int):
            return points

        if isinstance(points, str):
            # Handle T-shirt sizes
            size_map = {
                'xs': 1, 'extra small': 1,
                's': 2, 'small': 2,
                'm': 3, 'medium': 3,
                'l': 5, 'large': 5,
                'xl': 8, 'extra large': 8,
                'xxl': 13, 'extra extra large': 13
            }

            points_lower = points.lower().strip()
            if points_lower in size_map:
                return size_map[points_lower]

            # Try to parse as number
            try:
                return int(float(points))
            except (ValueError, TypeError):
                return 0

        return 0

    def _normalize_status(self, status: str) -> str:
        """
        Normalize status values to standard set.

        Args:
            status: Raw status string

        Returns:
            Normalized status: Todo, In Progress, In Review, or Done
        """
        status_map = {
            'todo': 'Todo',
            'to do': 'Todo',
            'backlog': 'Todo',
            'open': 'Todo',
            'new': 'Todo',
            'in progress': 'In Progress',
            'in_progress': 'In Progress',
            'started': 'In Progress',
            'active': 'In Progress',
            'in review': 'In Review',
            'in_review': 'In Review',
            'review': 'In Review',
            'code review': 'In Review',
            'done': 'Done',
            'closed': 'Done',
            'completed': 'Done',
            'resolved': 'Done',
            'finished': 'Done'
        }

        status_lower = status.lower().strip()
        return status_map.get(status_lower, status)

    def _normalize_priority(self, priority: str) -> str:
        """
        Normalize priority values.

        Args:
            priority: Raw priority string

        Returns:
            Normalized priority: High, Medium, or Low
        """
        priority_map = {
            'high': 'High',
            'highest': 'High',
            'critical': 'High',
            'urgent': 'High',
            'p0': 'High',
            'p1': 'High',
            'medium': 'Medium',
            'normal': 'Medium',
            'p2': 'Medium',
            'low': 'Low',
            'lowest': 'Low',
            'trivial': 'Low',
            'p3': 'Low'
        }

        priority_lower = priority.lower().strip()
        return priority_map.get(priority_lower, 'Medium')

    def _parse_boolean(self, value: Any) -> bool:
        """
        Parse boolean values from various formats.

        Args:
            value: Value to parse

        Returns:
            Boolean result
        """
        if isinstance(value, bool):
            return value

        if isinstance(value, str):
            return value.lower().strip() in ['true', 'yes', '1', 'y']

        return bool(value)
