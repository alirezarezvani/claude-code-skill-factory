"""
Slash Command Validator
Validates generated slash command files for proper format.
"""

import re
from typing import Dict, List


class CommandValidator:
    """Validate slash command .md files."""

    def validate(self, command_content: str) -> Dict[str, any]:
        """
        Validate complete command file content.

        Args:
            command_content: Full .md file content

        Returns:
            Dict with validation results
        """
        issues = []

        # Check YAML frontmatter
        yaml_valid, yaml_issues = self._check_yaml_frontmatter(command_content)
        if not yaml_valid:
            issues.extend(yaml_issues)

        # Check argument syntax
        args_valid, args_issues = self._check_arguments(command_content)
        if not args_valid:
            issues.extend(args_issues)

        # Check allowed-tools format
        tools_valid, tools_issues = self._check_allowed_tools(command_content)
        if not tools_valid:
            issues.extend(tools_issues)

        return {
            'valid': len(issues) == 0,
            'issues': issues
        }

    def _check_yaml_frontmatter(self, content: str) -> tuple:
        """Check YAML frontmatter is present and valid."""
        issues = []

        # Check starts with ---
        if not content.strip().startswith('---'):
            issues.append("Missing YAML frontmatter opening (---)")
            return False, issues

        # Extract frontmatter
        parts = content.split('---')
        if len(parts) < 3:
            issues.append("YAML frontmatter not properly closed")
            return False, issues

        frontmatter = parts[1]

        # Check required fields
        if 'description:' not in frontmatter:
            issues.append("Missing required 'description' field in YAML")

        return len(issues) == 0, issues

    def _check_arguments(self, content: str) -> tuple:
        """
        Check argument usage is correct.

        Commands should use $ARGUMENTS (not $1, $2, $3).
        """
        issues = []

        # Check for positional arguments (not allowed)
        if re.search(r'\$[0-9]', content):
            issues.append("Found positional arguments ($1, $2, etc.). Use $ARGUMENTS instead.")

        # If uses $ARGUMENTS, should have argument-hint
        if '$ARGUMENTS' in content:
            if 'argument-hint:' not in content:
                issues.append("Command uses $ARGUMENTS but missing 'argument-hint' in YAML")

        return len(issues) == 0, issues

    def _check_allowed_tools(self, content: str) -> tuple:
        """Check allowed-tools format is correct."""
        issues = []

        # Extract frontmatter
        if '---' not in content:
            return True, []  # Already caught in YAML check

        parts = content.split('---')
        if len(parts) < 2:
            return True, []

        frontmatter = parts[1]

        # If has allowed-tools, validate format
        if 'allowed-tools:' in frontmatter:
            # Extract the tools line
            for line in frontmatter.split('\n'):
                if 'allowed-tools:' in line:
                    tools_part = line.split('allowed-tools:')[1].strip()

                    # Valid tools
                    valid_tools = ['Read', 'Write', 'Edit', 'Bash', 'Grep', 'Glob', 'Task', 'TodoWrite', 'Skill', 'SlashCommand']

                    # Check comma-separated
                    if ',' in tools_part or any(tool in tools_part for tool in valid_tools):
                        # Format looks okay
                        pass
                    else:
                        issues.append("allowed-tools should be comma-separated list")

        return len(issues) == 0, issues

    def validate_folder_structure(self, folder_path: str) -> Dict[str, Any]:
        """
        Validate command folder organization.

        Args:
            folder_path: Path to generated command folder

        Returns:
            Validation results
        """
        issues = []

        if not os.path.exists(folder_path):
            issues.append(f"Folder not found: {folder_path}")
            return {'valid': False, 'issues': issues}

        # Check .md files are in root (not in subfolders)
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    # Should be in root of folder
                    if root != folder_path:
                        issues.append(f".md file in subfolder (should be in root): {file}")

        # Check folders are properly separated
        subfolders = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

        # Valid folder names
        valid_folders = ['standards', 'examples', 'scripts']

        for folder in subfolders:
            if folder not in valid_folders:
                issues.append(f"Unexpected folder: {folder} (valid: {valid_folders})")

        return {
            'valid': len(issues) == 0,
            'issues': issues
        }
