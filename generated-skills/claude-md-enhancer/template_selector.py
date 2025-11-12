"""
CLAUDE.md Template Selector

Selects appropriate CLAUDE.md templates based on project context.
Provides intelligent template selection, customization, and recommendations.
"""

from typing import Dict, List, Any, Optional


class TemplateSelector:
    """Selects and customizes CLAUDE.md templates based on project context."""

    # Template definitions by project type
    PROJECT_TEMPLATES = {
        "web_app": {
            "focus": "Frontend components, UI/UX, state management",
            "sections": [
                "Quick Navigation", "Core Principles", "Component Standards",
                "State Management", "Styling Guidelines", "Testing Requirements",
                "Performance Optimization", "Accessibility"
            ],
            "tech_hints": ["react", "vue", "angular", "svelte"]
        },
        "api": {
            "focus": "Backend services, REST/GraphQL, database operations",
            "sections": [
                "Quick Navigation", "Core Principles", "API Design",
                "Database Guidelines", "Error Handling", "Testing Requirements",
                "Security Practices", "Documentation Standards"
            ],
            "tech_hints": ["node", "python", "go", "java", "fastapi", "express"]
        },
        "fullstack": {
            "focus": "Integrated frontend + backend, end-to-end workflows",
            "sections": [
                "Quick Navigation", "Core Principles", "Frontend Guidelines",
                "Backend Guidelines", "Database Operations", "API Integration",
                "Testing Strategy", "Deployment Process"
            ],
            "tech_hints": ["next.js", "django", "rails", "laravel"]
        },
        "cli": {
            "focus": "Command-line interface, user interaction, scripting",
            "sections": [
                "Quick Navigation", "Core Principles", "Command Structure",
                "Argument Parsing", "Error Handling", "Testing Requirements",
                "Documentation Standards", "Distribution"
            ],
            "tech_hints": ["click", "commander", "cobra", "clap"]
        },
        "library": {
            "focus": "Reusable package, API design, versioning",
            "sections": [
                "Quick Navigation", "Core Principles", "Public API Design",
                "Versioning Strategy", "Testing Requirements", "Documentation Standards",
                "Breaking Changes", "Release Process"
            ],
            "tech_hints": ["npm", "pypi", "crates.io", "maven"]
        },
        "mobile": {
            "focus": "Mobile UI, platform-specific code, performance",
            "sections": [
                "Quick Navigation", "Core Principles", "Platform Guidelines",
                "Navigation Patterns", "State Management", "Performance Optimization",
                "Testing Requirements", "Release Process"
            ],
            "tech_hints": ["react-native", "flutter", "ios", "android"]
        },
        "desktop": {
            "focus": "Desktop application, native integration, distribution",
            "sections": [
                "Quick Navigation", "Core Principles", "Window Management",
                "Native Integration", "State Management", "Testing Requirements",
                "Build Process", "Distribution"
            ],
            "tech_hints": ["electron", "tauri", "qt", "gtk"]
        }
    }

    # Team size templates
    TEAM_SIZE_TEMPLATES = {
        "solo": {
            "target_lines": 75,
            "complexity": "minimal",
            "focus": "Efficiency, personal workflow",
            "detail_level": "concise"
        },
        "small": {
            "target_lines": 125,
            "complexity": "core",
            "focus": "Core guidelines, collaboration basics",
            "detail_level": "moderate"
        },
        "medium": {
            "target_lines": 200,
            "complexity": "detailed",
            "focus": "Team coordination, process standardization",
            "detail_level": "comprehensive"
        },
        "large": {
            "target_lines": 275,
            "complexity": "comprehensive",
            "focus": "Enterprise standards, governance",
            "detail_level": "extensive"
        }
    }

    # Development phase templates
    PHASE_TEMPLATES = {
        "prototype": {
            "priority": ["Quick start", "Flexibility", "Rapid iteration"],
            "skip_sections": ["Security Practices", "Performance Optimization"]
        },
        "mvp": {
            "priority": ["Core features", "Testing basics", "Documentation"],
            "skip_sections": []
        },
        "production": {
            "priority": ["Quality", "Security", "Performance", "Monitoring"],
            "skip_sections": []
        },
        "enterprise": {
            "priority": ["Compliance", "Security", "Scalability", "Governance"],
            "skip_sections": []
        }
    }

    def __init__(self, project_context: Dict[str, Any]):
        """
        Initialize template selector with project context.

        Args:
            project_context: Dictionary containing project type, tech_stack, team_size, etc.
        """
        self.project_type = project_context.get('type', 'web_app')
        self.tech_stack = project_context.get('tech_stack', [])
        self.team_size = project_context.get('team_size', 'small')
        self.phase = project_context.get('phase', 'mvp')
        self.workflows = project_context.get('workflows', [])
        self.modular = project_context.get('modular', False)

    def select_template(self) -> Dict[str, Any]:
        """
        Select the most appropriate template based on project context.

        Returns:
            Template configuration dictionary
        """
        # Get base template for project type
        project_template = self.PROJECT_TEMPLATES.get(
            self.project_type,
            self.PROJECT_TEMPLATES['web_app']
        )

        # Get team size configuration
        team_config = self.TEAM_SIZE_TEMPLATES.get(
            self.team_size,
            self.TEAM_SIZE_TEMPLATES['small']
        )

        # Get phase configuration
        phase_config = self.PHASE_TEMPLATES.get(
            self.phase,
            self.PHASE_TEMPLATES['mvp']
        )

        # Combine into final template
        return {
            "project_type": self.project_type,
            "team_size": self.team_size,
            "phase": self.phase,
            "target_lines": team_config['target_lines'],
            "complexity": team_config['complexity'],
            "sections": self._select_sections(
                project_template['sections'],
                phase_config
            ),
            "focus": project_template['focus'],
            "detail_level": team_config['detail_level'],
            "tech_customization": self._get_tech_customization(),
            "modular_recommended": self.recommend_modular_structure()
        }

    def _select_sections(self, base_sections: List[str], phase_config: Dict[str, Any]) -> List[str]:
        """
        Select sections based on phase and priorities.

        Args:
            base_sections: List of base section names
            phase_config: Phase configuration dictionary

        Returns:
            Filtered list of sections
        """
        skip_sections = phase_config.get('skip_sections', [])
        return [section for section in base_sections if section not in skip_sections]

    def _get_tech_customization(self) -> Dict[str, Any]:
        """
        Get tech stack-specific customizations.

        Returns:
            Tech customization configuration
        """
        customizations = {
            "languages": [],
            "frameworks": [],
            "tools": [],
            "specific_guidelines": []
        }

        # Detect languages
        lang_map = {
            'typescript': 'TypeScript',
            'javascript': 'JavaScript',
            'python': 'Python',
            'go': 'Go',
            'rust': 'Rust',
            'java': 'Java',
            'kotlin': 'Kotlin',
            'ruby': 'Ruby',
            'php': 'PHP'
        }

        for tech in self.tech_stack:
            tech_lower = tech.lower()
            if tech_lower in lang_map:
                customizations['languages'].append(lang_map[tech_lower])

        # Detect frameworks
        framework_map = {
            'react': 'React',
            'vue': 'Vue',
            'angular': 'Angular',
            'svelte': 'Svelte',
            'next.js': 'Next.js',
            'django': 'Django',
            'fastapi': 'FastAPI',
            'flask': 'Flask',
            'express': 'Express',
            'gin': 'Gin',
            'echo': 'Echo',
            'spring': 'Spring Boot',
            'rails': 'Rails'
        }

        for tech in self.tech_stack:
            tech_lower = tech.lower()
            if tech_lower in framework_map:
                customizations['frameworks'].append(framework_map[tech_lower])

        # Detect tools
        tool_map = {
            'docker': 'Docker',
            'kubernetes': 'Kubernetes',
            'postgresql': 'PostgreSQL',
            'mongodb': 'MongoDB',
            'redis': 'Redis',
            'git': 'Git',
            'github': 'GitHub',
            'gitlab': 'GitLab'
        }

        for tech in self.tech_stack:
            tech_lower = tech.lower()
            if tech_lower in tool_map:
                customizations['tools'].append(tool_map[tech_lower])

        # Add specific guidelines based on tech stack
        if 'typescript' in [t.lower() for t in self.tech_stack]:
            customizations['specific_guidelines'].append(
                "Use TypeScript strict mode throughout the project"
            )

        if 'react' in [t.lower() for t in self.tech_stack]:
            customizations['specific_guidelines'].append(
                "Prefer functional components with hooks over class components"
            )

        if 'python' in [t.lower() for t in self.tech_stack]:
            customizations['specific_guidelines'].append(
                "Use type hints for all function signatures (Python 3.10+)"
            )

        if 'docker' in [t.lower() for t in self.tech_stack]:
            customizations['specific_guidelines'].append(
                "Use multi-stage Dockerfiles for optimized image size"
            )

        return customizations

    def recommend_modular_structure(self) -> bool:
        """
        Determine if modular CLAUDE.md structure is recommended.

        Returns:
            True if modular structure recommended, False otherwise
        """
        # Recommend modular structure for:
        # 1. Full-stack projects
        # 2. Large teams
        # 3. Production/enterprise phase
        # 4. Projects with 3+ major tech stack components

        if self.project_type == 'fullstack':
            return True

        if self.team_size in ['medium', 'large']:
            return True

        if self.phase in ['production', 'enterprise']:
            return True

        if len(self.tech_stack) >= 3:
            return True

        # User explicitly requested modular
        if self.modular:
            return True

        return False

    def customize_template(self, template: Dict[str, Any]) -> str:
        """
        Generate customized CLAUDE.md content based on template.

        Args:
            template: Template configuration dictionary

        Returns:
            Customized CLAUDE.md content as string
        """
        lines = []

        # Add title
        lines.append("# CLAUDE.md")
        lines.append("")
        lines.append(f"This file provides guidance for Claude Code when working with this {self.project_type} project.")
        lines.append("")

        # Add modular navigation if recommended
        if template.get('modular_recommended'):
            lines.append("## Quick Navigation")
            lines.append("")
            lines.extend(self._generate_navigation_links())
            lines.append("")

        # Add core principles
        lines.append("## Core Principles")
        lines.append("")
        lines.extend(self._generate_core_principles(template))
        lines.append("")

        # Add tech stack section
        if self.tech_stack:
            lines.append("## Tech Stack")
            lines.append("")
            lines.extend(self._generate_tech_stack_section(template))
            lines.append("")

        # Add workflow section if workflows specified
        if self.workflows:
            lines.append("## Workflow Instructions")
            lines.append("")
            lines.extend(self._generate_workflow_section())
            lines.append("")

        # Add additional sections based on template
        for section in template['sections']:
            if section not in ["Quick Navigation", "Core Principles", "Tech Stack", "Workflow Instructions"]:
                lines.append(f"## {section}")
                lines.append("")
                lines.append(f"[Add {section.lower()} guidelines specific to your project]")
                lines.append("")

        return '\n'.join(lines)

    def _generate_navigation_links(self) -> List[str]:
        """Generate navigation links for modular structure."""
        links = []

        if self.project_type == 'fullstack':
            links.append("- [Backend Guidelines](backend/CLAUDE.md)")
            links.append("- [Frontend Guidelines](frontend/CLAUDE.md)")
            links.append("- [Database Operations](database/CLAUDE.md)")

        if 'cicd' in self.workflows:
            links.append("- [CI/CD Workflows](.github/CLAUDE.md)")

        if not links:
            links.append("- [Context-specific guides will be linked here]")

        return links

    def _generate_core_principles(self, template: Dict[str, Any]) -> List[str]:
        """Generate core principles based on template."""
        principles = []

        # Add workflow-specific principles
        if 'tdd' in self.workflows:
            principles.append("1. **Test-Driven Development**: Write tests before implementation")

        # Add tech-specific principles
        tech_custom = template.get('tech_customization', {})
        for i, guideline in enumerate(tech_custom.get('specific_guidelines', [])[:3], start=len(principles)+1):
            principles.append(f"{i}. **{guideline.split(':')[0] if ':' in guideline else 'Guideline'}**: {guideline}")

        # Add generic principles if needed
        if len(principles) < 3:
            generic = [
                "**Code Quality**: Maintain high code quality with clear, readable implementations",
                "**Documentation**: Keep documentation in sync with code changes",
                "**Error Handling**: Implement comprehensive error handling from the start"
            ]
            for i, principle in enumerate(generic[:3-len(principles)], start=len(principles)+1):
                principles.append(f"{i}. {principle}")

        return principles

    def _generate_tech_stack_section(self, template: Dict[str, Any]) -> List[str]:
        """Generate tech stack section."""
        lines = []
        tech_custom = template.get('tech_customization', {})

        if tech_custom.get('languages'):
            lines.append(f"- **Languages**: {', '.join(tech_custom['languages'])}")

        if tech_custom.get('frameworks'):
            lines.append(f"- **Frameworks**: {', '.join(tech_custom['frameworks'])}")

        if tech_custom.get('tools'):
            lines.append(f"- **Tools**: {', '.join(tech_custom['tools'])}")

        if not lines:
            lines.append("- [Add your tech stack details here]")

        return lines

    def _generate_workflow_section(self) -> List[str]:
        """Generate workflow section based on specified workflows."""
        lines = []

        workflow_descriptions = {
            'tdd': "1. **Test-Driven Development**: Write tests first, then implement features to pass tests",
            'cicd': "2. **CI/CD**: All changes go through automated testing and deployment pipelines",
            'documentation_first': "3. **Documentation First**: Document APIs and interfaces before implementation",
            'agile': "4. **Agile Process**: Work in sprints with regular retrospectives and planning"
        }

        for i, workflow in enumerate(self.workflows, start=1):
            if workflow in workflow_descriptions:
                lines.append(workflow_descriptions[workflow])
            else:
                lines.append(f"{i}. **{workflow.replace('_', ' ').title()}**: [Add workflow description]")

        return lines

    def determine_complexity(self) -> str:
        """
        Determine appropriate complexity level for the template.

        Returns:
            Complexity level: 'minimal', 'core', 'detailed', or 'comprehensive'
        """
        team_config = self.TEAM_SIZE_TEMPLATES.get(self.team_size, self.TEAM_SIZE_TEMPLATES['small'])
        return team_config['complexity']
