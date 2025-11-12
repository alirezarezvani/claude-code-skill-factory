"""
CLAUDE.md File Analyzer

Analyzes existing CLAUDE.md files to identify structure, sections, and quality issues.
Provides detailed analysis reports with quality scores and actionable recommendations.
"""

from typing import Dict, List, Any, Tuple
import re


class CLAUDEMDAnalyzer:
    """Analyzes CLAUDE.md files for structure, completeness, and quality."""

    # Standard sections that should be present in most CLAUDE.md files
    RECOMMENDED_SECTIONS = [
        "Quick Navigation",
        "Core Principles",
        "Tech Stack",
        "Workflow Instructions",
        "Quality Checklist",
        "File Organization",
        "Common Commands",
        "References"
    ]

    # Optional but valuable sections
    OPTIONAL_SECTIONS = [
        "Testing Requirements",
        "Error Handling Patterns",
        "Documentation Standards",
        "Performance Guidelines",
        "Security Checklist",
        "Deployment Process",
        "Troubleshooting"
    ]

    def __init__(self, content: str):
        """
        Initialize analyzer with CLAUDE.md file content.

        Args:
            content: Full text content of CLAUDE.md file
        """
        self.content = content
        self.lines = content.split('\n')
        self.line_count = len(self.lines)
        self.char_count = len(content)
        self.sections = []
        self.subsections = []

    def analyze_file(self) -> Dict[str, Any]:
        """
        Perform comprehensive analysis of CLAUDE.md file.

        Returns:
            Dictionary containing full analysis results
        """
        return {
            "file_metrics": self._get_file_metrics(),
            "sections_found": self.detect_sections(),
            "missing_sections": self._identify_missing_sections(),
            "structure_analysis": self._analyze_structure(),
            "issues": self._detect_issues(),
            "quality_score": self.calculate_quality_score(),
            "recommendations": self.generate_recommendations()
        }

    def _get_file_metrics(self) -> Dict[str, int]:
        """Calculate basic file metrics."""
        return {
            "char_count": self.char_count,
            "line_count": self.line_count,
            "word_count": len(self.content.split()),
            "heading_count": len([line for line in self.lines if line.startswith('#')]),
            "code_block_count": self.content.count('```') // 2
        }

    def detect_sections(self) -> List[str]:
        """
        Detect all sections (headings) in the file.

        Returns:
            List of section titles found
        """
        sections = []
        subsections = []

        for line in self.lines:
            # Match markdown headings (## or ###)
            if line.startswith('## '):
                section_title = line[3:].strip()
                sections.append(section_title)
            elif line.startswith('### '):
                subsection_title = line[4:].strip()
                subsections.append(subsection_title)

        self.sections = sections
        self.subsections = subsections
        return sections

    def _identify_missing_sections(self) -> List[str]:
        """
        Identify recommended sections that are missing.

        Returns:
            List of missing section names
        """
        if not self.sections:
            self.detect_sections()

        missing = []
        for recommended in self.RECOMMENDED_SECTIONS:
            # Check if section exists (case-insensitive, partial match)
            if not any(recommended.lower() in section.lower() for section in self.sections):
                missing.append(recommended)

        return missing

    def _analyze_structure(self) -> Dict[str, Any]:
        """
        Analyze the structural quality of the file.

        Returns:
            Dictionary with structure analysis
        """
        has_title = self.content.startswith('# ')
        has_navigation = any('navigation' in s.lower() for s in self.sections)
        has_code_examples = '```' in self.content
        has_links = '[' in self.content and '](' in self.content

        # Check for modular architecture mentions
        mentions_modular = any(
            keyword in self.content.lower()
            for keyword in ['backend/CLAUDE.md', 'frontend/CLAUDE.md', 'subdirectory', 'context-specific']
        )

        return {
            "has_main_title": has_title,
            "has_navigation_section": has_navigation,
            "has_code_examples": has_code_examples,
            "has_links": has_links,
            "mentions_modular_architecture": mentions_modular,
            "section_count": len(self.sections),
            "subsection_count": len(self.subsections),
            "hierarchy_depth": self._calculate_hierarchy_depth()
        }

    def _calculate_hierarchy_depth(self) -> int:
        """Calculate maximum heading depth."""
        max_depth = 1  # Assumes at least # title
        for line in self.lines:
            if line.startswith('#'):
                depth = len(line) - len(line.lstrip('#'))
                max_depth = max(max_depth, depth)
        return max_depth

    def _detect_issues(self) -> List[Dict[str, str]]:
        """
        Detect potential issues with the file.

        Returns:
            List of issue dictionaries with type, severity, and message
        """
        issues = []

        # Check file length
        if self.line_count > 400:
            issues.append({
                "type": "length_critical",
                "severity": "high",
                "message": f"File is too long ({self.line_count} lines). Recommended: split into modular files."
            })
        elif self.line_count > 300:
            issues.append({
                "type": "length_warning",
                "severity": "medium",
                "message": f"File exceeds recommended 300 lines ({self.line_count} lines). Consider splitting."
            })

        # Check if file is too short
        if self.line_count < 30:
            issues.append({
                "type": "too_short",
                "severity": "medium",
                "message": f"File is very short ({self.line_count} lines). May need more guidance."
            })

        # Check for missing critical sections
        critical_sections = ["Core Principles", "Tech Stack", "Workflow"]
        missing_critical = [
            s for s in critical_sections
            if not any(s.lower() in section.lower() for section in self.sections)
        ]

        if missing_critical:
            issues.append({
                "type": "missing_critical_sections",
                "severity": "high",
                "message": f"Missing critical sections: {', '.join(missing_critical)}"
            })

        # Check for placeholder text
        placeholders = ['TODO', 'TBD', 'FIXME', '[Insert', '[Add']
        for placeholder in placeholders:
            if placeholder in self.content:
                issues.append({
                    "type": "placeholder_text",
                    "severity": "medium",
                    "message": f"Contains placeholder text: '{placeholder}'"
                })
                break

        # Check for empty sections
        empty_section_pattern = r'##\s+[^\n]+\n\s*\n\s*##'
        if re.search(empty_section_pattern, self.content):
            issues.append({
                "type": "empty_sections",
                "severity": "low",
                "message": "Some sections appear to be empty"
            })

        return issues

    def calculate_quality_score(self) -> int:
        """
        Calculate overall quality score (0-100).

        Scoring breakdown:
        - Length appropriateness: 25 points
        - Section completeness: 25 points
        - Formatting quality: 20 points
        - Content specificity: 15 points
        - Modular organization: 15 points

        Returns:
            Quality score between 0 and 100
        """
        score = 0

        # Length appropriateness (25 points)
        if 50 <= self.line_count <= 300:
            score += 25
        elif 30 <= self.line_count < 50 or 300 < self.line_count <= 400:
            score += 15
        elif self.line_count > 400:
            score += 5
        else:
            score += 10

        # Section completeness (25 points)
        if not self.sections:
            self.detect_sections()

        found_count = len([
            s for s in self.RECOMMENDED_SECTIONS
            if any(s.lower() in section.lower() for section in self.sections)
        ])
        section_score = (found_count / len(self.RECOMMENDED_SECTIONS)) * 25
        score += int(section_score)

        # Formatting quality (20 points)
        formatting_score = 0
        if self.content.startswith('# '):
            formatting_score += 5
        if '```' in self.content:
            formatting_score += 5
        if '[' in self.content and '](' in self.content:
            formatting_score += 5
        if any('navigation' in s.lower() for s in self.sections):
            formatting_score += 5
        score += formatting_score

        # Content specificity (15 points)
        # Check for specific tech mentions (not generic)
        tech_keywords = [
            'typescript', 'python', 'react', 'vue', 'angular', 'node',
            'fastapi', 'django', 'postgresql', 'mongodb', 'docker'
        ]
        content_lower = self.content.lower()
        tech_mentions = sum(1 for keyword in tech_keywords if keyword in content_lower)

        if tech_mentions >= 3:
            score += 15
        elif tech_mentions >= 2:
            score += 10
        elif tech_mentions >= 1:
            score += 5

        # Modular organization (15 points)
        modular_keywords = [
            'backend/CLAUDE.md', 'frontend/CLAUDE.md', 'context-specific',
            'subdirectory', 'modular'
        ]
        modular_mentions = sum(1 for keyword in modular_keywords if keyword.lower() in content_lower)

        if modular_mentions >= 2:
            score += 15
        elif modular_mentions >= 1:
            score += 10

        return min(score, 100)

    def generate_recommendations(self) -> List[str]:
        """
        Generate actionable recommendations for improvement.

        Returns:
            List of recommendation strings
        """
        recommendations = []

        # Analyze first to ensure data is available
        if not self.sections:
            self.detect_sections()

        missing = self._identify_missing_sections()
        issues = self._detect_issues()

        # Critical issues first
        for issue in issues:
            if issue['severity'] == 'high':
                if issue['type'] == 'length_critical':
                    recommendations.append(
                        "CRITICAL: Split into modular files - create backend/CLAUDE.md, "
                        "frontend/CLAUDE.md, etc."
                    )
                elif issue['type'] == 'missing_critical_sections':
                    recommendations.append(f"CRITICAL: {issue['message']}")

        # Length recommendations
        if self.line_count > 300:
            recommendations.append(
                "Reduce root CLAUDE.md to <150 lines - move detailed guides to context-specific files"
            )
        elif self.line_count < 30:
            recommendations.append(
                "Expand with essential sections: Core Principles, Tech Stack, Workflow Instructions"
            )

        # Missing sections
        if missing:
            high_priority = ["Core Principles", "Tech Stack", "Workflow Instructions"]
            missing_high_priority = [s for s in missing if s in high_priority]

            if missing_high_priority:
                recommendations.append(
                    f"Add essential sections: {', '.join(missing_high_priority)}"
                )

            missing_optional = [s for s in missing if s not in high_priority]
            if len(missing_optional) <= 3:
                recommendations.append(
                    f"Consider adding: {', '.join(missing_optional)}"
                )

        # Structure recommendations
        structure = self._analyze_structure()
        if not structure['has_navigation_section'] and self.line_count > 100:
            recommendations.append(
                "Add Quick Navigation section with links to context-specific guides"
            )

        if not structure['has_code_examples']:
            recommendations.append(
                "Include code examples for complex patterns to improve clarity"
            )

        # Modular architecture
        if self.line_count > 200 and not structure['mentions_modular_architecture']:
            recommendations.append(
                "Consider implementing modular architecture - separate files for major components"
            )

        # Quality improvements
        quality_score = self.calculate_quality_score()
        if quality_score < 60:
            recommendations.append(
                f"Overall quality score is {quality_score}/100 - prioritize critical improvements"
            )

        return recommendations[:8]  # Limit to top 8 recommendations
