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

        # 4.5. Validate event-specific rules (if event type can be determined)
        # Event type is the top-level key in the hook config
        for event_type in ['PreToolUse', 'PostToolUse', 'SessionStart', 'Stop', 'PrePush', 'UserPromptSubmit', 'SubagentStop']:
            if event_type in str(hook_config) or (hook_config.get('_metadata', {}).get('event_type') == event_type):
                issues.extend(self._validate_event_specific_rules(event_type, hook_config))
                break

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

            # Check for hardcoded secrets (enhanced check)
            if self._has_potential_secrets(command):
                issues.append(ValidationIssue(
                    severity='warning',
                    message=f'Hook {idx} may contain hardcoded secrets',
                    fix_suggestion='Use environment variables for sensitive data'
                ))

            # Check Unix/macOS/Linux command syntax and compatibility
            unix_issues = self._validate_unix_commands(command)
            for issue in unix_issues:
                # Prepend hook index to message for context
                issue.message = f'Hook {idx}: {issue.message}'
                issues.append(issue)

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

    def _validate_event_specific_rules(self, event_type: str, hook_config: Dict) -> List[ValidationIssue]:
        """
        Validate event-specific rules for different hook types.

        Rules:
        - PreToolUse: Must have tool matcher, cannot be *, timeout <10s
        - SessionStart: Cannot depend on file paths, read-only, timeout <30s
        - PrePush: Should use git, timeout 60-120s appropriate
        - Stop: Cleanup operations only, timeout <60s
        - UserPromptSubmit: Cannot modify files, timeout <5s
        """
        issues = []
        matcher = hook_config.get('matcher', {})
        hooks = hook_config.get('hooks', [])

        # PreToolUse validation
        if event_type == 'PreToolUse':
            # Must have tool_names matcher
            if 'tool_names' not in matcher:
                issues.append(ValidationIssue(
                    severity='error',
                    message='PreToolUse hook must have tool_names matcher',
                    fix_suggestion='Add "tool_names": ["Write", "Edit"] to matcher'
                ))
            elif matcher.get('tool_names') == ['*'] or matcher.get('tool_names') == '*':
                issues.append(ValidationIssue(
                    severity='warning',
                    message='PreToolUse with "*" matcher may block all tool operations',
                    fix_suggestion='Use specific tool names for better control'
                ))

            # Timeout should be quick (blocking event)
            for hook in hooks:
                timeout = hook.get('timeout', 60)
                if timeout > 10:
                    issues.append(ValidationIssue(
                        severity='warning',
                        message=f'PreToolUse hook timeout ({timeout}s) is high for blocking event',
                        fix_suggestion='PreToolUse hooks block tool execution - keep timeout <10s'
                    ))

        # SessionStart validation
        elif event_type == 'SessionStart':
            # Check for file path dependencies (files not loaded yet)
            for hook in hooks:
                command = hook.get('command', '')
                if 'CLAUDE_TOOL_FILE_PATH' in command or '$FILE' in command:
                    issues.append(ValidationIssue(
                        severity='error',
                        message='SessionStart hook cannot depend on file paths',
                        fix_suggestion='File paths not available at session start - use project-level checks only'
                    ))

                # Check for write operations (should be read-only)
                if re.search(r'\b(Write|Edit|write|echo\s+>|cat\s+>)', command):
                    issues.append(ValidationIssue(
                        severity='warning',
                        message='SessionStart should be read-only (display context, not modify)',
                        fix_suggestion='Use read operations only (cat, echo, git status)'
                    ))

                # Timeout check
                timeout = hook.get('timeout', 60)
                if timeout > 30:
                    issues.append(ValidationIssue(
                        severity='warning',
                        message=f'SessionStart hook timeout ({timeout}s) is too long',
                        fix_suggestion='SessionStart should be fast (<30s) for quick startup'
                    ))

        # PrePush validation
        elif event_type == 'PrePush':
            # Should involve git operations
            has_git = False
            for hook in hooks:
                command = hook.get('command', '')
                if re.search(r'\bgit\b', command, re.IGNORECASE):
                    has_git = True

            if not has_git:
                issues.append(ValidationIssue(
                    severity='info',
                    message='PrePush hook does not seem to use git commands',
                    fix_suggestion='Consider adding git-related validation (git status, git diff, etc.)'
                ))

            # Check timeout is reasonable for tests
            for hook in hooks:
                timeout = hook.get('timeout', 60)
                if timeout < 30:
                    issues.append(ValidationIssue(
                        severity='info',
                        message=f'PrePush hook timeout ({timeout}s) may be too short for tests',
                        fix_suggestion='Tests may need 60-120s - consider increasing timeout'
                    ))

        # Stop event validation
        elif event_type == 'Stop':
            # Check for non-cleanup operations
            for hook in hooks:
                command = hook.get('command', '')

                # Should not have long-running operations
                if re.search(r'\b(npm\s+install|pip\s+install|build|compile)\b', command):
                    issues.append(ValidationIssue(
                        severity='warning',
                        message='Stop hook should not run long operations (install, build)',
                        fix_suggestion='Stop is for cleanup only - save state, remove temp files'
                    ))

                # Timeout check
                timeout = hook.get('timeout', 60)
                if timeout > 60:
                    issues.append(ValidationIssue(
                        severity='warning',
                        message=f'Stop hook timeout ({timeout}s) is high',
                        fix_suggestion='Stop hooks should complete quickly (<60s)'
                    ))

        # UserPromptSubmit validation
        elif event_type == 'UserPromptSubmit':
            # Should not modify files (read-only event)
            for hook in hooks:
                command = hook.get('command', '')

                if re.search(r'\b(Write|Edit|>|>>|tee)\b', command):
                    issues.append(ValidationIssue(
                        severity='error',
                        message='UserPromptSubmit hook cannot modify files',
                        fix_suggestion='This event is for prompt preprocessing only - no file modifications'
                    ))

                # Timeout must be very fast (blocks user input)
                timeout = hook.get('timeout', 60)
                if timeout > 5:
                    issues.append(ValidationIssue(
                        severity='error',
                        message=f'UserPromptSubmit hook timeout ({timeout}s) too high - blocks user',
                        fix_suggestion='UserPromptSubmit must complete in <5s - it blocks prompt processing'
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
        """
        Check for potential hardcoded secrets with comprehensive pattern detection.

        Detects:
        - Environment variable secrets ($AWS_SECRET, $API_KEY, etc.)
        - AWS keys (AKIA..., AWS secret keys)
        - Private keys (RSA, SSH)
        - JWT tokens
        - API tokens (Stripe, GitHub, etc.)
        - Generic credential patterns
        """
        secret_patterns = [
            # Basic assignment patterns
            r'password\s*=\s*["\'][^"\']+["\']',
            r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']',
            r'secret\s*=\s*["\'][^"\']+["\']',
            r'bearer\s*=\s*["\'][^"\']+["\']',

            # Environment variable patterns (unquoted secrets in env vars)
            r'\$\{?(?:AWS|GITHUB|SLACK|STRIPE|API)[_A-Z]*(?:KEY|SECRET|TOKEN)[_A-Z]*\}?\s*=\s*["\'][^"\']+["\']',

            # AWS Access Key ID (starts with AKIA)
            r'AKIA[0-9A-Z]{16}',

            # AWS Secret Access Key (40 characters base64)
            r'(?:aws_secret_access_key|AWS_SECRET_ACCESS_KEY)\s*=\s*["\']?[A-Za-z0-9/+=]{40}["\']?',

            # Generic AWS-style keys
            r'[A-Za-z0-9/+=]{40}',  # 40-char base64 strings (common for secrets)

            # Private keys
            r'-----BEGIN\s+(?:RSA\s+)?PRIVATE\s+KEY-----',
            r'-----BEGIN\s+OPENSSH\s+PRIVATE\s+KEY-----',
            r'-----BEGIN\s+EC\s+PRIVATE\s+KEY-----',

            # JWT tokens (eyJ... pattern)
            r'eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*',

            # Stripe API keys
            r'sk_live_[A-Za-z0-9]{24,}',
            r'sk_test_[A-Za-z0-9]{24,}',
            r'rk_live_[A-Za-z0-9]{24,}',

            # GitHub tokens
            r'gh[ps]_[A-Za-z0-9]{36,}',
            r'github_pat_[A-Za-z0-9]{22}_[A-Za-z0-9]{59}',

            # Generic high-entropy strings (likely secrets)
            r'["\'][A-Za-z0-9+/=]{32,}["\']',  # Long random strings in quotes

            # Connection strings with credentials
            r'://[^:]+:[^@]+@',  # protocol://user:pass@host

            # API endpoints with tokens in URL
            r'[?&](?:api_key|token|access_token|auth)=[A-Za-z0-9_-]{16,}',
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

    def _validate_unix_commands(self, command: str) -> List[ValidationIssue]:
        """
        Validate Unix/macOS/Linux command syntax and availability.

        Checks:
        - Bash syntax (quotes, redirects, pipes)
        - Common Unix commands availability
        - Path formats (Unix-style)
        - Potentially dangerous operations
        """
        issues = []

        # Check for unclosed quotes
        single_quotes = command.count("'")
        double_quotes = command.count('"')
        if single_quotes % 2 != 0:
            issues.append(ValidationIssue(
                severity='error',
                message='Unclosed single quote in command',
                fix_suggestion="Check for mismatched single quotes (')"
            ))
        if double_quotes % 2 != 0:
            issues.append(ValidationIssue(
                severity='error',
                message='Unclosed double quote in command',
                fix_suggestion='Check for mismatched double quotes (")'
            ))

        # Check for common bash syntax errors
        if re.search(r'>\s*>', command) or re.search(r'<\s*<', command):
            issues.append(ValidationIssue(
                severity='warning',
                message='Possible redirect syntax error (>> or <<)',
                fix_suggestion='Check redirect operators: > for write, >> for append, < for input'
            ))

        # Check for unescaped special characters in paths
        if re.search(r'[^\\]\s+[^-]', command) and '  ' not in command:
            # Has spaces without backslash escape (potential issue)
            if '/Users/' in command or '/home/' in command or '/path/' in command:
                issues.append(ValidationIssue(
                    severity='info',
                    message='Path with spaces may need escaping or quotes',
                    fix_suggestion='Use "path with spaces" or path\\ with\\ spaces'
                ))

        # Check for Windows-style paths (incorrect for macOS/Linux)
        if re.search(r'[A-Z]:\\', command):
            issues.append(ValidationIssue(
                severity='error',
                message='Windows-style path detected (C:\\) - incompatible with macOS/Linux',
                fix_suggestion='Use Unix-style paths: /path/to/file'
            ))

        # Check for common Unix commands and suggest alternatives if missing
        common_commands = {
            'find': 'Use for file searching',
            'grep': 'Use for text searching',
            'awk': 'Use for text processing',
            'sed': 'Use for text transformation',
            'cat': 'Use for file reading',
            'ls': 'Use for listing files',
            'mkdir': 'Use for directory creation',
            'rm': 'Use for file removal (be careful!)',
            'cp': 'Use for file copying',
            'mv': 'Use for moving/renaming',
        }

        # Extract commands used
        used_commands = re.findall(r'\b(\w+)\b', command)
        for cmd in used_commands:
            if cmd in ['rm', 'rmdir'] and '-rf' in command:
                issues.append(ValidationIssue(
                    severity='warning',
                    message=f'Potentially destructive command: {cmd} -rf',
                    fix_suggestion='Ensure this is intentional and safe'
                ))

        # Check for sudo usage (requires password)
        if re.search(r'\bsudo\b', command):
            issues.append(ValidationIssue(
                severity='warning',
                message='sudo requires password - may not work in hooks',
                fix_suggestion='Avoid sudo in hooks - run commands with appropriate permissions'
            ))

        # Check for interactive commands (won't work in hooks)
        interactive_commands = ['vi', 'vim', 'emacs', 'nano', 'less', 'more', 'top', 'htop']
        for cmd in interactive_commands:
            if re.search(rf'\b{cmd}\b', command):
                issues.append(ValidationIssue(
                    severity='error',
                    message=f'Interactive command "{cmd}" cannot run in hooks',
                    fix_suggestion='Hooks run non-interactively - use non-interactive alternatives'
                ))

        # Check for missing shebang in multi-line scripts
        if command.count('\n') > 3 and not command.strip().startswith('#!'):
            issues.append(ValidationIssue(
                severity='info',
                message='Multi-line script missing shebang (#!/bin/bash)',
                fix_suggestion='Add #!/bin/bash at the start for clarity'
            ))

        # Check for unquoted variables (potential issues)
        if re.search(r'\$[A-Za-z_][A-Za-z0-9_]*[^"]', command):
            # Has $VAR not followed by quote (might need quoting)
            issues.append(ValidationIssue(
                severity='info',
                message='Unquoted variable expansion may cause issues with spaces',
                fix_suggestion='Consider quoting variables: "$VAR" instead of $VAR'
            ))

        return issues


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
