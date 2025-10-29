"""
Slash Command Validator
Validates generated slash command files for proper format.
Enforces official Anthropic patterns and best practices.
"""

import re
import os
from typing import Dict, List, Any


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

    def validate_bash_permissions(self, allowed_tools: str) -> Dict[str, Any]:
        """
        Validate bash permissions are specific (not wildcards).

        Official rule from Anthropic: NEVER use 'Bash' alone - always specify commands.

        Args:
            allowed_tools: The allowed-tools string from YAML

        Returns:
            Dict with validation results including errors and warnings
        """
        if not allowed_tools:
            return {'valid': True, 'errors': [], 'warnings': []}

        errors = []
        warnings = []

        # Check for wildcard Bash (CRITICAL ERROR - not allowed)
        # Must check if 'Bash' appears without parentheses
        if re.search(r'\bBash\b(?!\()', allowed_tools):
            errors.append("❌ CRITICAL: Wildcard 'Bash' not allowed per official patterns. Must specify exact commands: Bash(git status:*)")

        # Extract bash commands
        bash_commands = re.findall(r'Bash\(([^)]+)\)', allowed_tools)

        # Validate each command against whitelist
        valid_commands = [
            'git', 'find', 'tree', 'ls', 'grep', 'wc', 'du',
            'head', 'tail', 'cat', 'awk', 'sed', 'sort', 'uniq', 'touch'
        ]

        for cmd in bash_commands:
            base_cmd = cmd.split(':')[0].strip()
            if base_cmd not in valid_commands:
                warnings.append(f"⚠️ Command '{base_cmd}' not in official patterns. Verify necessity.")

        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }

    def validate_command_name(self, name: str) -> Dict[str, Any]:
        """
        Validate command name follows kebab-case convention.

        Official rules from Anthropic docs:
        - Must be kebab-case (lowercase with hyphens)
        - Length: 2-4 words
        - Characters: [a-z0-9-] only
        - Must start and end with letter/number

        Args:
            name: Command name to validate

        Returns:
            Dict with validation results
        """
        errors = []

        # Check format (kebab-case with 2-4 words)
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+){1,3}$', name):
            errors.append(f"❌ Command name '{name}' must be kebab-case with 2-4 words (e.g., 'code-review')")

        # Check length
        word_count = len(name.split('-'))
        if word_count < 2:
            errors.append(f"❌ Command name too short: needs at least 2 words (e.g., 'api-build')")
        elif word_count > 4:
            errors.append(f"❌ Command name too long: maximum 4 words, found {word_count}")

        # Check invalid characters
        if re.search(r'[^a-z0-9-]', name):
            errors.append(f"❌ Command name contains invalid characters. Use only [a-z0-9-]")

        # Check for underscores (common mistake)
        if '_' in name:
            suggested = name.replace('_', '-')
            errors.append(f"❌ Use hyphens not underscores. Try: '{suggested}'")

        # Check for camelCase or PascalCase
        if re.search(r'[A-Z]', name):
            errors.append(f"❌ Command name must be lowercase only. No CamelCase or PascalCase.")

        return {
            'valid': len(errors) == 0,
            'errors': errors
        }

    def validate_arguments_usage(self, command_content: str) -> Dict[str, Any]:
        """
        Validate uses $ARGUMENTS (not $1, $2, $3).

        Official pattern from Anthropic: All examples use $ARGUMENTS.

        Args:
            command_content: Full command file content

        Returns:
            Dict with validation results
        """
        warnings = []
        errors = []

        # Check for positional arguments (CRITICAL - wrong pattern)
        positional_matches = re.findall(r'\$[0-9]+', command_content)
        if positional_matches:
            errors.append(f"❌ Found positional arguments: {positional_matches}. Official pattern uses $ARGUMENTS")

        # Check for $ARGUMENTS without argument-hint
        if '$ARGUMENTS' in command_content and 'argument-hint:' not in command_content:
            warnings.append("⚠️ Uses $ARGUMENTS but missing 'argument-hint' in YAML frontmatter")

        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }

    def validate_comprehensive(self, command_name: str, command_content: str, allowed_tools: str) -> Dict[str, Any]:
        """
        Run all validations comprehensively.

        Args:
            command_name: Name of the command
            command_content: Full command file content
            allowed_tools: The allowed-tools string

        Returns:
            Comprehensive validation results
        """
        all_errors = []
        all_warnings = []

        # Validate command name
        name_result = self.validate_command_name(command_name)
        if not name_result['valid']:
            all_errors.extend(name_result['errors'])

        # Validate bash permissions
        bash_result = self.validate_bash_permissions(allowed_tools)
        if not bash_result['valid']:
            all_errors.extend(bash_result['errors'])
        all_warnings.extend(bash_result['warnings'])

        # Validate arguments usage
        args_result = self.validate_arguments_usage(command_content)
        if not args_result['valid']:
            all_errors.extend(args_result['errors'])
        all_warnings.extend(args_result['warnings'])

        # Run standard validation
        standard_result = self.validate(command_content)
        if not standard_result['valid']:
            all_errors.extend(standard_result['issues'])

        return {
            'valid': len(all_errors) == 0,
            'errors': all_errors,
            'warnings': all_warnings,
            'summary': f"{'✅ VALID' if len(all_errors) == 0 else '❌ INVALID'} - {len(all_errors)} errors, {len(all_warnings)} warnings"
        }
