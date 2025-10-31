"""
Hook Validator - JSON validation and safety checks for Claude Code hooks.

Validates:
1. JSON syntax and structure
2. Required fields present
3. Safety patterns (tool detection, silent failure)
4. No destructive operations
5. Valid glob patterns
6. Event type appropriateness
"""

import json
import re
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class ValidationIssue:
    """Represents a validation issue."""
    severity: str  # 'error', 'warning', 'info'
    message: str
    fix_suggestion: str = ""


@dataclass
class ValidationResult:
    """Result of hook validation."""
    is_valid: bool
    is_safe: bool
    issues: List[ValidationIssue]

    @property
    def errors(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == 'error']

    @property
    def warnings(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == 'warning']


class HookValidator:
    """Validates Claude Code hooks for correctness and safety."""

    # Destructive command patterns
    DESTRUCTIVE_PATTERNS = [
        (r'rm\s+-rf', 'rm -rf'),
        (r'git\s+push\s+--force', 'git push --force'),
        (r'DROP\s+TABLE', 'DROP TABLE'),
        (r'chmod\s+777', 'chmod 777'),
        (r'sudo\s+rm', 'sudo rm'),
        (r'\|\s*dd\s+', 'dd command'),
        (r'>>\s*/dev/', 'writing to /dev/'),
        (r'mkfs\s+', 'mkfs command'),
    ]

    # Common external tools that need detection
    EXTERNAL_TOOLS = [
        'black', 'prettier', 'rustfmt', 'gofmt', 'autopep8',
        'pytest', 'jest', 'cargo', 'npm', 'go',
        'git', 'docker', 'kubectl', 'terraform',
        'eslint', 'pylint', 'semgrep', 'bandit'
    ]

    # Event types and their timing requirements
    EVENT_TIMING = {
        'SessionStart': {'max_time': 10, 'can_block': False},
        'SessionEnd': {'max_time': 10, 'can_block': False},
        'PreToolUse': {'max_time': 5, 'can_block': True},
        'PostToolUse': {'max_time': 5, 'can_block': False},
        'UserPromptSubmit': {'max_time': 5, 'can_block': True},
        'Stop': {'max_time': 30, 'can_block': True},
        'SubagentStop': {'max_time': 120, 'can_block': True},
        'Notification': {'max_time': 5, 'can_block': False},
        'PreCompact': {'max_time': 10, 'can_block': False},
    }

    def validate_hook(self, hook_config: Dict) -> ValidationResult:
        """
        Validate a hook configuration.

        Args:
            hook_config: Dictionary containing hook configuration

        Returns:
            ValidationResult with validation status and issues
        """
        issues = []

        # 1. Validate JSON structure
        issues.extend(self._validate_structure(hook_config))

        # 2. Validate safety patterns
        issues.extend(self._validate_safety(hook_config))

        # 3. Validate matchers
        issues.extend(self._validate_matchers(hook_config))

        # 4. Validate event appropriateness
        issues.extend(self._validate_event_type(hook_config))

        # 5. Validate timeouts
        issues.extend(self._validate_timeouts(hook_config))

        # Determine overall validity
        has_errors = any(i.severity == 'error' for i in issues)
        has_safety_issues = any(
            i.severity == 'error' and 'destructive' in i.message.lower()
            for i in issues
        )

        return ValidationResult(
            is_valid=not has_errors,
            is_safe=not has_safety_issues,
            issues=issues
        )

    def validate_json(self, json_str: str) -> Tuple[bool, Dict, str]:
        """
        Validate JSON syntax.

        Returns:
            (is_valid, parsed_dict, error_message)
        """
        try:
            parsed = json.loads(json_str)
            return True, parsed, ""
        except json.JSONDecodeError as e:
            return False, {}, f"Invalid JSON: {str(e)}"

    def _validate_structure(self, hook_config: Dict) -> List[ValidationIssue]:
        """Validate hook configuration structure."""
        issues = []

        # Check for matcher field
        if 'matcher' not in hook_config:
            issues.append(ValidationIssue(
                severity='error',
                message='Missing required field: matcher',
                fix_suggestion='Add "matcher": {} for hooks that apply to all events'
            ))

        # Check for hooks array
        if 'hooks' not in hook_config:
            issues.append(ValidationIssue(
                severity='error',
                message='Missing required field: hooks',
                fix_suggestion='Add "hooks": [] array with hook commands'
            ))
        elif not isinstance(hook_config['hooks'], list):
            issues.append(ValidationIssue(
                severity='error',
                message='Field "hooks" must be an array',
                fix_suggestion='Change "hooks" to be a JSON array'
            ))
        else:
            # Validate each hook
            for idx, hook in enumerate(hook_config['hooks']):
                if not isinstance(hook, dict):
                    issues.append(ValidationIssue(
                        severity='error',
                        message=f'Hook {idx} must be an object',
                        fix_suggestion='Each hook must be a JSON object with "type" and "command"'
                    ))
                    continue

                if 'type' not in hook:
                    issues.append(ValidationIssue(
                        severity='error',
                        message=f'Hook {idx} missing required field: type',
                        fix_suggestion='Add "type": "command"'
                    ))

                if 'command' not in hook:
                    issues.append(ValidationIssue(
                        severity='error',
                        message=f'Hook {idx} missing required field: command',
                        fix_suggestion='Add "command": "your bash/python command"'
                    ))

        return issues

    def _validate_safety(self, hook_config: Dict) -> List[ValidationIssue]:
        """Validate safety patterns in hook commands."""
        issues = []

        if 'hooks' not in hook_config or not isinstance(hook_config['hooks'], list):
            return issues

        for idx, hook in enumerate(hook_config['hooks']):
            if 'command' not in hook:
                continue

            command = hook['command']

            # Check for destructive operations
            for pattern, name in self.DESTRUCTIVE_PATTERNS:
                if re.search(pattern, command, re.IGNORECASE):
                    issues.append(ValidationIssue(
                        severity='error',
                        message=f'Hook {idx} contains destructive operation: {name}',
                        fix_suggestion='Remove destructive command or add explicit user confirmation'
                    ))

            # Check for external tool usage without detection
            used_tools = self._extract_used_tools(command)
            for tool in used_tools:
                if not self._has_tool_detection(command, tool):
                    issues.append(ValidationIssue(
                        severity='warning',
                        message=f'Hook {idx} uses "{tool}" without tool detection',
                        fix_suggestion=f'Add: if ! command -v {tool} &> /dev/null; then exit 0; fi'
                    ))

            # Check for silent failure pattern
            if not self._has_silent_failure(command):
                issues.append(ValidationIssue(
                    severity='warning',
                    message=f'Hook {idx} may fail loudly',
                    fix_suggestion='Append "|| exit 0" to commands for silent failure'
                ))

            # Check for hardcoded secrets (basic check)
            if self._has_potential_secrets(command):
                issues.append(ValidationIssue(
                    severity='warning',
                    message=f'Hook {idx} may contain hardcoded secrets',
                    fix_suggestion='Use environment variables for sensitive data'
                ))

        return issues

    def _validate_matchers(self, hook_config: Dict) -> List[ValidationIssue]:
        """Validate matcher patterns."""
        issues = []

        matcher = hook_config.get('matcher', {})

        # Validate tool_names if present
        if 'tool_names' in matcher:
            tool_names = matcher['tool_names']
            if not isinstance(tool_names, list):
                issues.append(ValidationIssue(
                    severity='error',
                    message='matcher.tool_names must be an array',
                    fix_suggestion='Change to: "tool_names": ["Write", "Edit"]'
                ))
            else:
                valid_tools = [
                    'Read', 'Write', 'Edit', 'Bash', 'Grep', 'Glob',
                    'Task', 'WebFetch', 'WebSearch', 'Skill', 'SlashCommand'
                ]
                for tool in tool_names:
                    if tool not in valid_tools and not tool.startswith('mcp__'):
                        issues.append(ValidationIssue(
                            severity='warning',
                            message=f'Unknown tool name in matcher: {tool}',
                            fix_suggestion=f'Valid tools: {", ".join(valid_tools)}'
                        ))

        # Validate glob patterns if present
        if 'paths' in matcher:
            paths = matcher.get('paths', [])
            if not isinstance(paths, list):
                issues.append(ValidationIssue(
                    severity='error',
                    message='matcher.paths must be an array',
                    fix_suggestion='Change to: "paths": ["**/*.py"]'
                ))
            else:
                for pattern in paths:
                    if not self._is_valid_glob(pattern):
                        issues.append(ValidationIssue(
                            severity='warning',
                            message=f'Potentially invalid glob pattern: {pattern}',
                            fix_suggestion='Use patterns like **/*.py, src/**/*.js'
                        ))

        return issues

    def _validate_event_type(self, hook_config: Dict) -> List[ValidationIssue]:
        """Validate event type appropriateness (requires metadata)."""
        issues = []

        # This requires metadata to be present, which may not always be the case
        # We'll add this as an optional check
        if '_metadata' in hook_config:
            metadata = hook_config['_metadata']
            event_type = metadata.get('event_type')

            if event_type and event_type in self.EVENT_TIMING:
                timing = self.EVENT_TIMING[event_type]

                # Check timeout appropriateness
                for hook in hook_config.get('hooks', []):
                    timeout = hook.get('timeout', 60)
                    if timeout > timing['max_time']:
                        issues.append(ValidationIssue(
                            severity='warning',
                            message=f'{event_type} hook timeout ({timeout}s) exceeds recommended max ({timing["max_time"]}s)',
                            fix_suggestion=f'Consider using a different event type for long operations'
                        ))

        return issues

    def _validate_timeouts(self, hook_config: Dict) -> List[ValidationIssue]:
        """Validate timeout settings."""
        issues = []

        for idx, hook in enumerate(hook_config.get('hooks', [])):
            timeout = hook.get('timeout', 60)

            if timeout < 1:
                issues.append(ValidationIssue(
                    severity='error',
                    message=f'Hook {idx} timeout too low: {timeout}s',
                    fix_suggestion='Timeout must be at least 1 second'
                ))
            elif timeout > 600:
                issues.append(ValidationIssue(
                    severity='warning',
                    message=f'Hook {idx} timeout very high: {timeout}s',
                    fix_suggestion='Consider if this operation really needs >10 minutes'
                ))

        return issues

    def _extract_used_tools(self, command: str) -> List[str]:
        """Extract external tools used in command."""
        used_tools = []

        for tool in self.EXTERNAL_TOOLS:
            # Look for tool name as standalone word
            if re.search(rf'\b{tool}\b', command):
                used_tools.append(tool)

        return used_tools

    def _has_tool_detection(self, command: str, tool: str) -> bool:
        """Check if command has tool detection for given tool."""
        # Look for: command -v {tool} or which {tool}
        detection_patterns = [
            rf'command\s+-v\s+{tool}',
            rf'which\s+{tool}',
            rf'type\s+{tool}',
        ]

        return any(re.search(pattern, command) for pattern in detection_patterns)

    def _has_silent_failure(self, command: str) -> bool:
        """Check if command has silent failure pattern."""
        # Look for: || exit 0 or || true or 2>/dev/null
        silent_patterns = [
            r'\|\|\s*exit\s+0',
            r'\|\|\s*true',
            r'2>/dev/null',
            r'2>&1\s*>/dev/null',
        ]

        return any(re.search(pattern, command) for pattern in silent_patterns)

    def _has_potential_secrets(self, command: str) -> bool:
        """Check for potential hardcoded secrets."""
        secret_patterns = [
            r'password\s*=\s*["\'][^"\']+["\']',
            r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']',
            r'secret\s*=\s*["\'][^"\']+["\']',
        ]

        return any(re.search(pattern, command, re.IGNORECASE) for pattern in secret_patterns)

    def _is_valid_glob(self, pattern: str) -> bool:
        """Basic validation of glob pattern."""
        # Check for common mistakes
        if pattern.endswith('*') and not pattern.endswith('**'):
            # Might be missing file extension
            return False

        # Pattern should contain at least one *
        if '*' not in pattern:
            return False

        return True


def validate_hook_file(file_path: str) -> ValidationResult:
    """
    Validate a hook JSON file.

    Args:
        file_path: Path to hook.json file

    Returns:
        ValidationResult
    """
    from pathlib import Path

    validator = HookValidator()

    try:
        # Validate file path for path traversal
        file_path_obj = Path(file_path).resolve()

        # Only allow reading from safe directories (generated-hooks, examples, etc.)
        # This prevents reading arbitrary system files
        safe_directories = [
            Path.cwd() / 'generated-hooks',
            Path.cwd() / 'examples',
            Path.cwd() / 'generated-skills' / 'hook-factory' / 'examples'
        ]

        # Check if file is within any safe directory
        is_safe = any(
            str(file_path_obj).startswith(str(safe_dir.resolve()))
            for safe_dir in safe_directories
        )

        if not is_safe:
            return ValidationResult(
                is_valid=False,
                is_safe=False,
                issues=[ValidationIssue(
                    severity='error',
                    message=f'Security: File path outside allowed directories: {file_path}',
                    fix_suggestion='Only validate files in generated-hooks/, examples/, or hook-factory/examples/'
                )]
            )

        with open(file_path_obj, 'r') as f:
            content = f.read()

        # Validate JSON syntax
        is_valid, hook_config, error = validator.validate_json(content)
        if not is_valid:
            return ValidationResult(
                is_valid=False,
                is_safe=False,
                issues=[ValidationIssue(
                    severity='error',
                    message=error,
                    fix_suggestion='Fix JSON syntax errors'
                )]
            )

        # Validate hook configuration
        return validator.validate_hook(hook_config)

    except FileNotFoundError:
        return ValidationResult(
            is_valid=False,
            is_safe=False,
            issues=[ValidationIssue(
                severity='error',
                message=f'File not found: {file_path}',
                fix_suggestion='Check file path'
            )]
        )
    except Exception as e:
        return ValidationResult(
            is_valid=False,
            is_safe=False,
            issues=[ValidationIssue(
                severity='error',
                message=f'Validation error: {str(e)}',
                fix_suggestion='Check hook configuration'
            )]
        )


if __name__ == '__main__':
    # Example usage
    import sys

    if len(sys.argv) < 2:
        print("Usage: python validator.py <hook.json>")
        sys.exit(1)

    result = validate_hook_file(sys.argv[1])

    print(f"Valid: {result.is_valid}")
    print(f"Safe: {result.is_safe}")
    print(f"\nIssues ({len(result.issues)}):")

    for issue in result.issues:
        print(f"  [{issue.severity.upper()}] {issue.message}")
        if issue.fix_suggestion:
            print(f"    Fix: {issue.fix_suggestion}")

    sys.exit(0 if result.is_valid else 1)
