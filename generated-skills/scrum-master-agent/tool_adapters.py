"""
Tool-specific adapters for Linear, Jira, GitHub Projects, and Azure DevOps.
Handles unique field mappings and data structures for each platform.
"""

from typing import Dict, List, Any, Optional


class ToolAdapter:
    """Base adapter class for tool-specific transformations."""

    def __init__(self, raw_data: Dict[str, Any]):
        """
        Initialize adapter with raw tool data.

        Args:
            raw_data: Data exported from specific tool
        """
        self.raw_data = raw_data
        self.tool_name = self._detect_tool()

    def _detect_tool(self) -> str:
        """Detect which tool the data came from."""
        # Check for tool-specific field patterns
        if 'identifier' in str(self.raw_data) and 'team' in str(self.raw_data):
            return 'linear'
        elif 'key' in str(self.raw_data) and 'fields' in str(self.raw_data):
            return 'jira'
        elif 'node_id' in str(self.raw_data) or 'repository' in str(self.raw_data):
            return 'github'
        elif 'workItemId' in str(self.raw_data) or 'System.WorkItemType' in str(self.raw_data):
            return 'azure'
        else:
            return 'unknown'

    def transform(self) -> Dict[str, Any]:
        """
        Transform tool-specific data to normalized format.

        Returns:
            Normalized sprint data
        """
        if self.tool_name == 'linear':
            return LinearAdapter(self.raw_data).transform()
        elif self.tool_name == 'jira':
            return JiraAdapter(self.raw_data).transform()
        elif self.tool_name == 'github':
            return GitHubAdapter(self.raw_data).transform()
        elif self.tool_name == 'azure':
            return AzureDevOpsAdapter(self.raw_data).transform()
        else:
            return self.raw_data


class LinearAdapter:
    """Adapter for Linear project management tool."""

    def __init__(self, data: Dict[str, Any]):
        """Initialize with Linear export data."""
        self.data = data

    def transform(self) -> Dict[str, Any]:
        """Transform Linear data to normalized format."""
        # Linear export structure
        issues = self.data.get('issues', [])
        project = self.data.get('project', {})

        return {
            'tool': 'linear',
            'sprint_name': project.get('name', 'Linear Sprint'),
            'start_date': project.get('startDate'),
            'end_date': project.get('targetDate'),
            'team_capacity': self._calculate_capacity(issues),
            'stories': [self._transform_issue(issue) for issue in issues]
        }

    def _transform_issue(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Transform Linear issue to normalized story."""
        return {
            'id': issue.get('identifier', issue.get('id', 'UNKNOWN')),
            'title': issue.get('title', 'Untitled'),
            'points': issue.get('estimate', 0),
            'status': self._map_status(issue.get('state', {}).get('name', 'Todo')),
            'assignee': issue.get('assignee', {}).get('name', 'Unassigned'),
            'priority': self._map_priority(issue.get('priority', 0)),
            'blocked': issue.get('blockedByCount', 0) > 0,
            'created_date': issue.get('createdAt'),
            'labels': [label.get('name', '') for label in issue.get('labels', [])],
            'dependencies': [dep.get('identifier') for dep in issue.get('relations', [])]
        }

    def _map_status(self, linear_status: str) -> str:
        """Map Linear status to normalized status."""
        status_map = {
            'triage': 'Todo',
            'backlog': 'Todo',
            'todo': 'Todo',
            'in progress': 'In Progress',
            'in review': 'In Review',
            'done': 'Done',
            'canceled': 'Done',
            'duplicate': 'Done'
        }
        return status_map.get(linear_status.lower(), linear_status)

    def _map_priority(self, linear_priority: int) -> str:
        """Map Linear priority (0-4) to normalized priority."""
        # Linear: 0=No priority, 1=Urgent, 2=High, 3=Medium, 4=Low
        priority_map = {
            0: 'Medium',
            1: 'High',
            2: 'High',
            3: 'Medium',
            4: 'Low'
        }
        return priority_map.get(linear_priority, 'Medium')

    def _calculate_capacity(self, issues: List[Dict[str, Any]]) -> int:
        """Calculate total capacity based on estimated points."""
        return sum(issue.get('estimate', 0) for issue in issues)


class JiraAdapter:
    """Adapter for Jira project management tool."""

    def __init__(self, data: Dict[str, Any]):
        """Initialize with Jira export data."""
        self.data = data

    def transform(self) -> Dict[str, Any]:
        """Transform Jira data to normalized format."""
        # Jira REST API structure
        issues = self.data.get('issues', [])
        sprint = self._extract_sprint_info(issues)

        return {
            'tool': 'jira',
            'sprint_name': sprint.get('name', 'Jira Sprint'),
            'start_date': sprint.get('startDate'),
            'end_date': sprint.get('endDate'),
            'team_capacity': sprint.get('goal', 0),
            'stories': [self._transform_issue(issue) for issue in issues]
        }

    def _transform_issue(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Transform Jira issue to normalized story."""
        fields = issue.get('fields', {})

        return {
            'id': issue.get('key', 'UNKNOWN'),
            'title': fields.get('summary', 'Untitled'),
            'points': fields.get('customfield_10016', fields.get('storyPoints', 0)),  # Story points custom field
            'status': fields.get('status', {}).get('name', 'Todo'),
            'assignee': fields.get('assignee', {}).get('displayName', 'Unassigned'),
            'priority': fields.get('priority', {}).get('name', 'Medium'),
            'blocked': len(fields.get('issuelinks', [])) > 0 and any(
                link.get('type', {}).get('name') == 'Blocks' for link in fields.get('issuelinks', [])
            ),
            'created_date': fields.get('created'),
            'labels': fields.get('labels', []),
            'dependencies': [
                link.get('inwardIssue', {}).get('key', '')
                for link in fields.get('issuelinks', [])
                if 'inwardIssue' in link
            ]
        }

    def _extract_sprint_info(self, issues: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract sprint information from issues."""
        # Try to get sprint from first issue
        if issues:
            fields = issues[0].get('fields', {})
            sprint_field = fields.get('customfield_10020', [])  # Sprint custom field
            if sprint_field:
                sprint = sprint_field[0] if isinstance(sprint_field, list) else sprint_field
                return {
                    'name': sprint.get('name', 'Sprint'),
                    'startDate': sprint.get('startDate'),
                    'endDate': sprint.get('endDate'),
                    'goal': sprint.get('goal', 0)
                }

        return {'name': 'Sprint', 'startDate': None, 'endDate': None, 'goal': 0}


class GitHubAdapter:
    """Adapter for GitHub Projects."""

    def __init__(self, data: Dict[str, Any]):
        """Initialize with GitHub Projects export data."""
        self.data = data

    def transform(self) -> Dict[str, Any]:
        """Transform GitHub Projects data to normalized format."""
        # GitHub GraphQL structure
        project = self.data.get('project', {})
        items = self.data.get('items', self.data.get('issues', []))

        return {
            'tool': 'github',
            'sprint_name': project.get('title', 'GitHub Sprint'),
            'start_date': None,  # GitHub Projects doesn't have built-in sprint dates
            'end_date': None,
            'team_capacity': 0,
            'stories': [self._transform_item(item) for item in items]
        }

    def _transform_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Transform GitHub issue/PR to normalized story."""
        return {
            'id': item.get('number', item.get('node_id', 'UNKNOWN')),
            'title': item.get('title', 'Untitled'),
            'points': self._extract_points(item),
            'status': self._map_status(item.get('state', 'open')),
            'assignee': self._extract_assignee(item),
            'priority': self._extract_priority(item),
            'blocked': 'blocked' in [label.lower() for label in item.get('labels', [])],
            'created_date': item.get('created_at'),
            'labels': item.get('labels', []),
            'dependencies': []  # GitHub doesn't have native dependency tracking
        }

    def _extract_points(self, item: Dict[str, Any]) -> int:
        """Extract story points from labels or custom fields."""
        # Look for labels like "points: 5" or "5 points"
        labels = item.get('labels', [])
        for label in labels:
            label_lower = str(label).lower()
            if 'point' in label_lower:
                # Extract number from label
                words = label_lower.split()
                for word in words:
                    try:
                        return int(word)
                    except ValueError:
                        continue
        return 0

    def _extract_assignee(self, item: Dict[str, Any]) -> str:
        """Extract assignee name."""
        assignees = item.get('assignees', [])
        if assignees:
            return assignees[0].get('login', 'Unassigned')
        return 'Unassigned'

    def _extract_priority(self, item: Dict[str, Any]) -> str:
        """Extract priority from labels."""
        labels = [str(label).lower() for label in item.get('labels', [])]
        if any('high' in label or 'urgent' in label or 'critical' in label for label in labels):
            return 'High'
        elif any('low' in label for label in labels):
            return 'Low'
        return 'Medium'

    def _map_status(self, github_state: str) -> str:
        """Map GitHub state to normalized status."""
        status_map = {
            'open': 'In Progress',
            'closed': 'Done',
            'draft': 'Todo'
        }
        return status_map.get(github_state.lower(), github_state)


class AzureDevOpsAdapter:
    """Adapter for Azure DevOps."""

    def __init__(self, data: Dict[str, Any]):
        """Initialize with Azure DevOps export data."""
        self.data = data

    def transform(self) -> Dict[str, Any]:
        """Transform Azure DevOps data to normalized format."""
        # Azure DevOps Work Item Query structure
        work_items = self.data.get('workItems', self.data.get('value', []))

        return {
            'tool': 'azure',
            'sprint_name': self._extract_sprint_name(work_items),
            'start_date': None,
            'end_date': None,
            'team_capacity': 0,
            'stories': [self._transform_work_item(item) for item in work_items]
        }

    def _transform_work_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Transform Azure DevOps work item to normalized story."""
        fields = item.get('fields', {})

        return {
            'id': item.get('id', 'UNKNOWN'),
            'title': fields.get('System.Title', 'Untitled'),
            'points': fields.get('Microsoft.VSTS.Scheduling.StoryPoints', 0),
            'status': fields.get('System.State', 'New'),
            'assignee': fields.get('System.AssignedTo', {}).get('displayName', 'Unassigned'),
            'priority': str(fields.get('Microsoft.VSTS.Common.Priority', 2)),  # 1=High, 2=Medium, 3=Low
            'blocked': fields.get('Microsoft.VSTS.CMMI.Blocked', 'No') == 'Yes',
            'created_date': fields.get('System.CreatedDate'),
            'labels': fields.get('System.Tags', '').split(';'),
            'dependencies': []  # Would need separate query for work item relations
        }

    def _extract_sprint_name(self, work_items: List[Dict[str, Any]]) -> str:
        """Extract sprint name from work items."""
        if work_items:
            fields = work_items[0].get('fields', {})
            iteration_path = fields.get('System.IterationPath', 'Sprint')
            # Extract last part of iteration path (e.g., "Project\\Sprint 45" -> "Sprint 45")
            return iteration_path.split('\\')[-1]
        return 'Azure DevOps Sprint'
