"""
CLAUDE.md Content Generator

Generates new CLAUDE.md files or enhances existing ones based on templates and analysis.
Supports modular architecture with context-specific files.
"""

from typing import Dict, List, Any, Optional
from template_selector import TemplateSelector
import re


class ContentGenerator:
    """Generates and enhances CLAUDE.md files based on project context."""

    def __init__(self, project_context: Dict[str, Any]):
        """
        Initialize content generator with project context.

        Args:
            project_context: Dictionary containing project type, tech_stack, team_size, etc.
        """
        self.project_context = project_context
        self.template_selector = TemplateSelector(project_context)

    def generate_root_file(self) -> str:
        """
        Generate root CLAUDE.md file (navigation hub).

        Returns:
            Complete CLAUDE.md content as string
        """
        template = self.template_selector.select_template()

        # Use template selector's customization
        if template.get('modular_recommended'):
            return self._generate_modular_root(template)
        else:
            return self._generate_standalone_file(template)

    def _generate_modular_root(self, template: Dict[str, Any]) -> str:
        """Generate root file for modular architecture (navigation hub)."""
        lines = []

        # Title
        lines.append("# CLAUDE.md")
        lines.append("")
        lines.append(f"This file provides top-level guidance for Claude Code when working with this {self.project_context.get('type', 'project')}.")
        lines.append("")

        # Quick Navigation
        lines.append("## Quick Navigation")
        lines.append("")
        lines.extend(self._generate_navigation_section(template))
        lines.append("")

        # Core Principles (concise, 5-7 principles)
        lines.append("## Core Principles")
        lines.append("")
        principles = self._generate_core_principles(template, max_count=5)
        lines.extend(principles)
        lines.append("")

        # Tech Stack (summary only)
        if self.project_context.get('tech_stack'):
            lines.append("## Tech Stack")
            lines.append("")
            lines.extend(self._generate_tech_stack_summary())
            lines.append("")

        # Key Commands/Shortcuts
        lines.append("## Quick Reference")
        lines.append("")
        lines.extend(self._generate_quick_reference())
        lines.append("")

        # Footer
        lines.append("---")
        lines.append("")
        lines.append("For detailed guidelines, see context-specific CLAUDE.md files in subdirectories.")

        return '\n'.join(lines)

    def _generate_standalone_file(self, template: Dict[str, Any]) -> str:
        """Generate standalone CLAUDE.md file (all-in-one)."""
        return self.template_selector.customize_template(template)

    def generate_context_file(self, context: str) -> str:
        """
        Generate context-specific CLAUDE.md file (e.g., backend, frontend).

        Args:
            context: Context name ('backend', 'frontend', 'database', etc.)

        Returns:
            Context-specific CLAUDE.md content
        """
        generators = {
            'backend': self._generate_backend_file,
            'frontend': self._generate_frontend_file,
            'database': self._generate_database_file,
            'docs': self._generate_docs_file,
            '.github': self._generate_github_file
        }

        generator = generators.get(context, self._generate_generic_context_file)
        return generator()

    def _generate_backend_file(self) -> str:
        """Generate backend-specific CLAUDE.md."""
        lines = []
        lines.append("# Backend Development Guidelines")
        lines.append("")
        lines.append("This file provides guidance for backend development in this project.")
        lines.append("")

        # API Design
        lines.append("## API Design")
        lines.append("")
        lines.append("- Use RESTful conventions for API endpoints")
        lines.append("- Implement proper HTTP status codes (200, 201, 400, 404, 500)")
        lines.append("- Version APIs when breaking changes are needed (/api/v1/, /api/v2/)")
        lines.append("- Document all endpoints with OpenAPI/Swagger")
        lines.append("")

        # Database Guidelines
        lines.append("## Database Operations")
        lines.append("")
        lines.append("- Use migrations for all schema changes")
        lines.append("- Implement proper indexes for query performance")
        lines.append("- Use transactions for multi-step operations")
        lines.append("- Avoid N+1 queries - use joins or batch loading")
        lines.append("")

        # Error Handling
        lines.append("## Error Handling")
        lines.append("")
        lines.append("- Implement global error handling middleware")
        lines.append("- Log errors with context (request ID, user ID, timestamp)")
        lines.append("- Return consistent error response format")
        lines.append("- Never expose stack traces to clients in production")
        lines.append("")

        # Testing
        lines.append("## Testing Requirements")
        lines.append("")
        lines.append("- Write unit tests for business logic")
        lines.append("- Write integration tests for API endpoints")
        lines.append("- Mock external services in tests")
        lines.append("- Aim for 80%+ code coverage")
        lines.append("")

        return '\n'.join(lines)

    def _generate_frontend_file(self) -> str:
        """Generate frontend-specific CLAUDE.md."""
        lines = []
        lines.append("# Frontend Development Guidelines")
        lines.append("")
        lines.append("This file provides guidance for frontend development in this project.")
        lines.append("")

        # Component Standards
        lines.append("## Component Standards")
        lines.append("")
        tech_stack = [t.lower() for t in self.project_context.get('tech_stack', [])]

        if 'react' in tech_stack:
            lines.append("- Prefer functional components with hooks over class components")
            lines.append("- Use TypeScript for type safety")
            lines.append("- Keep components small and focused (< 200 lines)")
            lines.append("- Extract reusable logic into custom hooks")
        elif 'vue' in tech_stack:
            lines.append("- Use Composition API for complex components")
            lines.append("- Keep components small and focused (< 200 lines)")
            lines.append("- Use TypeScript with Vue 3")
            lines.append("- Extract reusable logic into composables")
        else:
            lines.append("- Keep components small and focused")
            lines.append("- Extract reusable logic into utilities")
            lines.append("- Use TypeScript for type safety")
        lines.append("")

        # State Management
        lines.append("## State Management")
        lines.append("")
        lines.append("- Keep component state local when possible")
        lines.append("- Use global state only for truly shared data")
        lines.append("- Avoid prop drilling - use context/store for deep state")
        lines.append("- Document state shape and update patterns")
        lines.append("")

        # Styling
        lines.append("## Styling Guidelines")
        lines.append("")
        lines.append("- Use consistent naming conventions (BEM, CSS Modules, etc.)")
        lines.append("- Avoid inline styles except for dynamic values")
        lines.append("- Use design tokens for colors, spacing, typography")
        lines.append("- Ensure responsive design for all breakpoints")
        lines.append("")

        # Performance
        lines.append("## Performance Optimization")
        lines.append("")
        lines.append("- Lazy load routes and heavy components")
        lines.append("- Optimize images (use WebP, lazy loading)")
        lines.append("- Minimize bundle size - code split where possible")
        lines.append("- Use memoization for expensive calculations")
        lines.append("")

        return '\n'.join(lines)

    def _generate_database_file(self) -> str:
        """Generate database-specific CLAUDE.md."""
        lines = []
        lines.append("# Database Guidelines")
        lines.append("")
        lines.append("This file provides guidance for database operations and migrations.")
        lines.append("")

        # Schema Design
        lines.append("## Schema Design")
        lines.append("")
        lines.append("- Use meaningful table and column names")
        lines.append("- Always include created_at and updated_at timestamps")
        lines.append("- Use proper foreign key constraints")
        lines.append("- Add indexes for frequently queried columns")
        lines.append("")

        # Migrations
        lines.append("## Migration Guidelines")
        lines.append("")
        lines.append("- Never edit existing migrations - create new ones")
        lines.append("- Test migrations on copy of production data")
        lines.append("- Include both up and down migrations")
        lines.append("- Document breaking changes in migration comments")
        lines.append("")

        # Query Optimization
        lines.append("## Query Optimization")
        lines.append("")
        lines.append("- Use EXPLAIN to analyze slow queries")
        lines.append("- Avoid SELECT * - specify needed columns")
        lines.append("- Use appropriate JOIN types")
        lines.append("- Limit result sets with pagination")
        lines.append("")

        return '\n'.join(lines)

    def _generate_docs_file(self) -> str:
        """Generate documentation-specific CLAUDE.md."""
        lines = []
        lines.append("# Documentation Guidelines")
        lines.append("")
        lines.append("This file provides guidance for project documentation.")
        lines.append("")

        lines.append("## Documentation Standards")
        lines.append("")
        lines.append("- Keep README.md updated with setup instructions")
        lines.append("- Document all public APIs with examples")
        lines.append("- Include architecture diagrams for complex systems")
        lines.append("- Maintain changelog with semantic versioning")
        lines.append("")

        return '\n'.join(lines)

    def _generate_github_file(self) -> str:
        """Generate .github-specific CLAUDE.md for CI/CD."""
        lines = []
        lines.append("# CI/CD Workflows")
        lines.append("")
        lines.append("This file provides guidance for GitHub Actions and CI/CD processes.")
        lines.append("")

        lines.append("## Workflow Guidelines")
        lines.append("")
        lines.append("- Run linting and tests on all pull requests")
        lines.append("- Automate deployments to staging on main branch")
        lines.append("- Require manual approval for production deployments")
        lines.append("- Cache dependencies to speed up builds")
        lines.append("")

        return '\n'.join(lines)

    def _generate_generic_context_file(self) -> str:
        """Generate generic context-specific file."""
        return "# Context-Specific Guidelines\n\n[Add guidelines specific to this context]\n"

    def generate_section(self, section_name: str) -> str:
        """
        Generate a specific section for CLAUDE.md.

        Args:
            section_name: Name of section to generate

        Returns:
            Section content as string
        """
        generators = {
            'Core Principles': self._generate_core_principles_section,
            'Tech Stack': self._generate_tech_stack_section,
            'Workflow Instructions': self._generate_workflow_section,
            'Testing Requirements': self._generate_testing_section,
            'Error Handling': self._generate_error_handling_section,
            'Documentation Standards': self._generate_documentation_section
        }

        generator = generators.get(section_name, self._generate_generic_section)
        return generator(section_name)

    def _generate_core_principles_section(self, section_name: str) -> str:
        """Generate Core Principles section."""
        template = self.template_selector.select_template()
        lines = [f"## {section_name}", ""]
        lines.extend(self._generate_core_principles(template, max_count=7))
        return '\n'.join(lines)

    def _generate_tech_stack_section(self, section_name: str) -> str:
        """Generate Tech Stack section."""
        lines = [f"## {section_name}", ""]
        lines.extend(self._generate_tech_stack_summary())
        return '\n'.join(lines)

    def _generate_workflow_section(self, section_name: str) -> str:
        """Generate Workflow Instructions section."""
        lines = [f"## {section_name}", ""]

        workflows = self.project_context.get('workflows', [])
        if workflows:
            for i, workflow in enumerate(workflows, 1):
                workflow_title = workflow.replace('_', ' ').title()
                lines.append(f"{i}. **{workflow_title}**: [Add {workflow} workflow description]")
        else:
            lines.append("[Add workflow instructions specific to your project]")

        return '\n'.join(lines)

    def _generate_testing_section(self, section_name: str) -> str:
        """Generate Testing Requirements section."""
        lines = [f"## {section_name}", ""]
        lines.append("- Write tests before or alongside feature implementation")
        lines.append("- Maintain minimum 80% code coverage")
        lines.append("- Include unit, integration, and e2e tests")
        lines.append("- Mock external dependencies in tests")
        return '\n'.join(lines)

    def _generate_error_handling_section(self, section_name: str) -> str:
        """Generate Error Handling section."""
        lines = [f"## {section_name}", ""]
        lines.append("- Implement comprehensive error handling from the start")
        lines.append("- Log errors with context (user ID, request ID, timestamp)")
        lines.append("- Provide helpful error messages to users")
        lines.append("- Never expose sensitive information in error messages")
        return '\n'.join(lines)

    def _generate_documentation_section(self, section_name: str) -> str:
        """Generate Documentation Standards section."""
        lines = [f"## {section_name}", ""]
        lines.append("- Keep documentation in sync with code")
        lines.append("- Document all public APIs and interfaces")
        lines.append("- Include code examples in documentation")
        lines.append("- Update README.md with setup and usage instructions")
        return '\n'.join(lines)

    def _generate_generic_section(self, section_name: str) -> str:
        """Generate generic section placeholder."""
        return f"## {section_name}\n\n[Add {section_name.lower()} guidelines specific to your project]\n"

    def merge_with_existing(self, existing_content: str, new_sections: List[str]) -> str:
        """
        Merge new sections with existing CLAUDE.md content.

        Args:
            existing_content: Current CLAUDE.md content
            new_sections: List of new sections to add

        Returns:
            Merged content as string
        """
        lines = existing_content.split('\n')
        existing_sections = self._extract_existing_sections(existing_content)

        # Add new sections that don't already exist
        for new_section in new_sections:
            section_name = new_section.split('\n')[0].replace('## ', '')
            if section_name not in existing_sections:
                lines.append("")
                lines.append(new_section)

        return '\n'.join(lines)

    def _extract_existing_sections(self, content: str) -> List[str]:
        """Extract section names from existing content."""
        sections = []
        for line in content.split('\n'):
            if line.startswith('## '):
                sections.append(line[3:].strip())
        return sections

    def _generate_navigation_section(self, template: Dict[str, Any]) -> List[str]:
        """Generate navigation section for modular architecture."""
        project_type = self.project_context.get('type')
        links = []

        if project_type == 'fullstack':
            links.append("- [Backend Guidelines](backend/CLAUDE.md)")
            links.append("- [Frontend Guidelines](frontend/CLAUDE.md)")
            links.append("- [Database Operations](database/CLAUDE.md)")

        if 'cicd' in self.project_context.get('workflows', []):
            links.append("- [CI/CD Workflows](.github/CLAUDE.md)")

        if not links:
            links.append("- [Add links to context-specific CLAUDE.md files]")

        return links

    def _generate_core_principles(self, template: Dict[str, Any], max_count: int = 7) -> List[str]:
        """Generate core principles list."""
        principles = []
        workflows = self.project_context.get('workflows', [])

        # Add workflow-based principles
        if 'tdd' in workflows:
            principles.append("1. **Test-Driven Development**: Write tests before implementation")

        # Add tech-specific principles
        tech_custom = template.get('tech_customization', {})
        for guideline in tech_custom.get('specific_guidelines', [])[:3]:
            principle_num = len(principles) + 1
            principles.append(f"{principle_num}. **{guideline.split(':')[0] if ':' in guideline else 'Guideline'}**: {guideline}")

        # Add generic essential principles
        generic = [
            "**Code Quality**: Maintain high code quality with clear, readable implementations",
            "**Documentation**: Keep documentation in sync with code changes",
            "**Error Handling**: Implement comprehensive error handling from the start",
            "**Performance**: Consider performance implications in implementation decisions",
            "**Security**: Follow security best practices and avoid common vulnerabilities"
        ]

        for principle in generic:
            if len(principles) >= max_count:
                break
            principle_num = len(principles) + 1
            principles.append(f"{principle_num}. {principle}")

        return principles

    def _generate_tech_stack_summary(self) -> List[str]:
        """Generate tech stack summary."""
        lines = []
        template = self.template_selector.select_template()
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

    def _generate_quick_reference(self) -> List[str]:
        """Generate quick reference commands."""
        lines = []
        lines.append("```bash")
        lines.append("# Common development commands")
        lines.append("npm test          # Run tests")
        lines.append("npm run lint      # Run linter")
        lines.append("npm run build     # Build for production")
        lines.append("```")
        return lines
