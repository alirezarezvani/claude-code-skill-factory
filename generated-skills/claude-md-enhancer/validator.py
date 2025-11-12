"""
CLAUDE.md Best Practices Validator

Validates CLAUDE.md files against Anthropic guidelines and community best practices.
Provides detailed validation reports with pass/fail status and improvement suggestions.
"""

from typing import Dict, List, Any, Tuple
import re


class BestPracticesValidator:
    """Validates CLAUDE.md files against best practices and guidelines."""

    # Maximum recommended line count
    MAX_RECOMMENDED_LINES = 300
    WARNING_THRESHOLD_LINES = 200

    # Minimum content requirements
    MIN_LINES = 20
    MIN_SECTIONS = 3

    # Required sections for a complete CLAUDE.md
    REQUIRED_SECTIONS = [
        "Core Principles",
        "Workflow"
    ]

    # Anti-patterns to detect
    ANTI_PATTERNS = [
        {
            "name": "hardcoded_secrets",
            "patterns": [
                r'api[_-]?key\s*=\s*["\'][a-zA-Z0-9]{20,}["\']',
                r'password\s*=\s*["\'][^"\']+["\']',
                r'secret\s*=\s*["\'][^"\']+["\']',
                r'token\s*=\s*["\'][a-zA-Z0-9]{20,}["\']'
            ],
            "message": "Potential hardcoded secrets detected (API keys, passwords, tokens)"
        },
        {
            "name": "generic_content",
            "patterns": [
                r'\[TODO\]',
                r'\[TBD\]',
                r'\[PLACEHOLDER\]',
                r'\[Insert.*?\]',
                r'\[Add.*?\]'
            ],
            "message": "Generic placeholder content found - replace with specific guidance"
        },
        {
            "name": "duplicate_sections",
            "patterns": [],
            "message": "Duplicate section headings detected"
        },
        {
            "name": "broken_links",
            "patterns": [
                r'\[.*?\]\(\)',
                r'\[.*?\]\(#\)',
                r'\[.*?\]\(undefined\)'
            ],
            "message": "Broken or empty markdown links detected"
        }
    ]

    def __init__(self, content: str, project_context: Dict[str, Any] = None):
        """
        Initialize validator with CLAUDE.md content.

        Args:
            content: Full text content of CLAUDE.md file
            project_context: Optional project context for advanced validation
        """
        self.content = content
        self.lines = content.split('\n')
        self.line_count = len(self.lines)
        self.project_context = project_context or {}

    def validate_all(self) -> Dict[str, Any]:
        """
        Run all validation checks.

        Returns:
            Comprehensive validation report
        """
        return {
            "valid": self._is_valid_overall(),
            "validation_results": {
                "length": self.validate_length(),
                "structure": self.validate_structure(),
                "formatting": self.validate_formatting(),
                "completeness": self.validate_completeness(),
                "anti_patterns": self._check_anti_patterns()
            },
            "errors": self._collect_errors(),
            "warnings": self._collect_warnings(),
            "pass_count": self._count_passes(),
            "fail_count": self._count_failures()
        }

    def validate_length(self) -> Dict[str, Any]:
        """
        Validate file length against best practices.

        Returns:
            Validation result for length check
        """
        status = "pass"
        message = f"File length is appropriate ({self.line_count} lines)"
        severity = "info"

        if self.line_count > self.MAX_RECOMMENDED_LINES:
            status = "fail"
            message = f"File exceeds maximum recommended length ({self.line_count} > {self.MAX_RECOMMENDED_LINES} lines)"
            severity = "high"
        elif self.line_count > self.WARNING_THRESHOLD_LINES:
            status = "warning"
            message = f"File is approaching maximum length ({self.line_count} lines, recommended < {self.WARNING_THRESHOLD_LINES})"
            severity = "medium"
        elif self.line_count < self.MIN_LINES:
            status = "fail"
            message = f"File is too short ({self.line_count} lines, minimum {self.MIN_LINES})"
            severity = "high"

        return {
            "check": "file_length",
            "status": status,
            "message": message,
            "severity": severity,
            "actual_value": self.line_count,
            "expected_range": f"{self.MIN_LINES}-{self.MAX_RECOMMENDED_LINES} lines"
        }

    def validate_structure(self) -> Dict[str, Any]:
        """
        Validate file structure and organization.

        Returns:
            Validation result for structure check
        """
        sections = self._extract_sections()
        errors = []
        warnings = []

        # Check for main title
        if not self.content.strip().startswith('# '):
            errors.append("Missing main title (# CLAUDE.md)")

        # Check for minimum sections
        if len(sections) < self.MIN_SECTIONS:
            errors.append(f"Too few sections ({len(sections)}, minimum {self.MIN_SECTIONS})")

        # Check for required sections
        for required in self.REQUIRED_SECTIONS:
            if not any(required.lower() in section.lower() for section in sections):
                errors.append(f"Missing required section: '{required}'")

        # Check for duplicate sections
        section_counts = {}
        for section in sections:
            section_lower = section.lower()
            section_counts[section_lower] = section_counts.get(section_lower, 0) + 1

        duplicates = [s for s, count in section_counts.items() if count > 1]
        if duplicates:
            warnings.append(f"Duplicate sections found: {', '.join(duplicates)}")

        # Determine overall status
        status = "pass"
        if errors:
            status = "fail"
        elif warnings:
            status = "warning"

        return {
            "check": "file_structure",
            "status": status,
            "message": "Structure validation complete",
            "severity": "high" if errors else "medium" if warnings else "info",
            "errors": errors,
            "warnings": warnings,
            "sections_found": len(sections)
        }

    def validate_formatting(self) -> Dict[str, Any]:
        """
        Validate markdown formatting quality.

        Returns:
            Validation result for formatting check
        """
        errors = []
        warnings = []

        # Check for balanced code blocks
        code_block_count = self.content.count('```')
        if code_block_count % 2 != 0:
            errors.append("Unbalanced code blocks (unclosed ``` markers)")

        # Check for proper heading hierarchy
        heading_levels = []
        for line in self.lines:
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                heading_levels.append(level)

        if heading_levels and heading_levels[0] != 1:
            errors.append("First heading should be level 1 (# Title)")

        # Check for heading level skipping (e.g., # → ###)
        for i in range(len(heading_levels) - 1):
            if heading_levels[i+1] - heading_levels[i] > 1:
                warnings.append(f"Heading level skips detected (h{heading_levels[i]} → h{heading_levels[i+1]})")
                break

        # Check for consistent list formatting
        if '- ' in self.content and '* ' in self.content:
            warnings.append("Mixed list markers (- and *) - prefer consistent style")

        # Check for trailing whitespace (sample check)
        lines_with_trailing_ws = sum(1 for line in self.lines if line.endswith(' ') and line.strip())
        if lines_with_trailing_ws > 5:
            warnings.append(f"Multiple lines with trailing whitespace ({lines_with_trailing_ws})")

        status = "pass"
        if errors:
            status = "fail"
        elif warnings:
            status = "warning"

        return {
            "check": "markdown_formatting",
            "status": status,
            "message": "Formatting validation complete",
            "severity": "medium" if errors else "low",
            "errors": errors,
            "warnings": warnings
        }

    def validate_completeness(self) -> Dict[str, Any]:
        """
        Validate content completeness and quality.

        Returns:
            Validation result for completeness check
        """
        errors = []
        warnings = []

        # Check for essential content types
        has_code_examples = '```' in self.content
        has_links = '[' in self.content and '](' in self.content
        has_lists = any(line.strip().startswith(('-', '*', '1.')) for line in self.lines)

        if not has_code_examples:
            warnings.append("No code examples found - consider adding examples for clarity")

        if not has_links:
            warnings.append("No links found - consider linking to external documentation")

        if not has_lists:
            warnings.append("No lists found - consider using lists for better readability")

        # Check for tech stack mention
        tech_keywords = [
            'typescript', 'javascript', 'python', 'react', 'vue', 'angular',
            'node', 'django', 'fastapi', 'go', 'rust', 'java'
        ]
        content_lower = self.content.lower()
        tech_mentioned = any(keyword in content_lower for keyword in tech_keywords)

        if not tech_mentioned:
            warnings.append("No specific technologies mentioned - add tech stack reference")

        # Check for workflow mentions
        workflow_keywords = ['test', 'commit', 'deploy', 'review', 'documentation']
        workflow_mentioned = sum(1 for keyword in workflow_keywords if keyword in content_lower)

        if workflow_mentioned < 2:
            warnings.append("Limited workflow guidance - consider adding development workflow instructions")

        # Check for empty sections
        empty_section_pattern = r'##\s+[^\n]+\n\s*\n\s*##'
        if re.search(empty_section_pattern, self.content):
            errors.append("Empty sections detected - remove or populate with content")

        status = "pass"
        if errors:
            status = "fail"
        elif len(warnings) >= 3:
            status = "warning"

        return {
            "check": "content_completeness",
            "status": status,
            "message": "Completeness validation complete",
            "severity": "medium",
            "errors": errors,
            "warnings": warnings,
            "has_code_examples": has_code_examples,
            "has_links": has_links,
            "has_lists": has_lists,
            "tech_stack_mentioned": tech_mentioned
        }

    def _check_anti_patterns(self) -> Dict[str, Any]:
        """
        Check for anti-patterns and bad practices.

        Returns:
            Validation result for anti-pattern detection
        """
        detected = []

        for anti_pattern in self.ANTI_PATTERNS:
            if anti_pattern['name'] == 'duplicate_sections':
                # Handle duplicate sections separately
                sections = self._extract_sections()
                section_counts = {}
                for section in sections:
                    section_lower = section.lower()
                    section_counts[section_lower] = section_counts.get(section_lower, 0) + 1

                if any(count > 1 for count in section_counts.values()):
                    detected.append({
                        "pattern": anti_pattern['name'],
                        "message": anti_pattern['message']
                    })
            else:
                # Check regex patterns
                for pattern in anti_pattern['patterns']:
                    if re.search(pattern, self.content, re.IGNORECASE):
                        detected.append({
                            "pattern": anti_pattern['name'],
                            "message": anti_pattern['message']
                        })
                        break  # Only report each anti-pattern once

        status = "pass" if not detected else "fail"
        severity = "high" if any(p['pattern'] == 'hardcoded_secrets' for p in detected) else "medium"

        return {
            "check": "anti_patterns",
            "status": status,
            "message": f"{len(detected)} anti-pattern(s) detected" if detected else "No anti-patterns detected",
            "severity": severity,
            "detected_patterns": detected
        }

    def _extract_sections(self) -> List[str]:
        """Extract all section headings from content."""
        sections = []
        for line in self.lines:
            if line.startswith('## '):
                sections.append(line[3:].strip())
        return sections

    def _is_valid_overall(self) -> bool:
        """Determine if file passes overall validation."""
        length_result = self.validate_length()
        structure_result = self.validate_structure()

        # File is valid if length and structure pass (formatting and completeness can have warnings)
        return (
            length_result['status'] != 'fail' and
            structure_result['status'] != 'fail'
        )

    def _collect_errors(self) -> List[str]:
        """Collect all errors from validation checks."""
        errors = []
        all_results = [
            self.validate_length(),
            self.validate_structure(),
            self.validate_formatting(),
            self.validate_completeness(),
            self._check_anti_patterns()
        ]

        for result in all_results:
            if result['status'] == 'fail':
                if 'errors' in result:
                    errors.extend(result['errors'])
                else:
                    errors.append(result['message'])

        return errors

    def _collect_warnings(self) -> List[str]:
        """Collect all warnings from validation checks."""
        warnings = []
        all_results = [
            self.validate_length(),
            self.validate_structure(),
            self.validate_formatting(),
            self.validate_completeness()
        ]

        for result in all_results:
            if 'warnings' in result:
                warnings.extend(result['warnings'])
            elif result['status'] == 'warning':
                warnings.append(result['message'])

        return warnings

    def _count_passes(self) -> int:
        """Count number of passed checks."""
        all_results = [
            self.validate_length(),
            self.validate_structure(),
            self.validate_formatting(),
            self.validate_completeness(),
            self._check_anti_patterns()
        ]
        return sum(1 for result in all_results if result['status'] == 'pass')

    def _count_failures(self) -> int:
        """Count number of failed checks."""
        all_results = [
            self.validate_length(),
            self.validate_structure(),
            self.validate_formatting(),
            self.validate_completeness(),
            self._check_anti_patterns()
        ]
        return sum(1 for result in all_results if result['status'] == 'fail')
