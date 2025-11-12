"""
CLAUDE.md Initialization Workflow

Handles the complete workflow for initializing CLAUDE.md in a new project:
1. Explore repository to understand codebase
2. Detect project type, tech stack, and structure
3. Ask user for confirmation
4. Create initial CLAUDE.md file
5. Enhance with best practices

This workflow is interactive and conversational - user must confirm each step.

CRITICAL VALIDATION RULE:
"Always validate your output against official native examples before declaring complete."

Before finalizing CLAUDE.md generation:
- Compare output against `/update-claude-md` slash command format
- Verify all native format sections are present (Overview, Project Structure,
  File Structure, Setup & Installation, Architecture, etc.)
- Cross-check against reference examples in examples/ folder
"""

from typing import Dict, List, Any, Optional
from pathlib import Path
import json


class InitializationWorkflow:
    """Manages the interactive initialization workflow for CLAUDE.md creation."""

    def __init__(self, project_path: str = "."):
        """
        Initialize workflow with project path.

        Args:
            project_path: Path to project directory (default: current directory)
        """
        self.project_path = Path(project_path)
        self.discoveries = {}
        self.user_confirmations = {}

    def check_claude_md_exists(self) -> bool:
        """
        Check if CLAUDE.md already exists in project.

        Returns:
            True if CLAUDE.md exists, False otherwise
        """
        claude_md_path = self.project_path / "CLAUDE.md"
        return claude_md_path.exists()

    def generate_exploration_prompt(self) -> str:
        """
        Generate prompt to guide Claude to explore the repository.

        Returns:
            Exploration prompt string for Claude to execute
        """
        return """I'll explore this repository to understand the codebase before creating a CLAUDE.md file.

Let me examine:
1. Project structure and key directories
2. Technology stack (package.json, requirements.txt, go.mod, etc.)
3. Existing documentation (README.md, docs/)
4. Development workflows (GitHub Actions, scripts/, Makefile)
5. Testing setup
6. Build configuration

Exploring repository now..."""

    def analyze_discoveries(self, exploration_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze repository exploration results to determine project context.

        Args:
            exploration_results: Results from repository exploration

        Returns:
            Analyzed project context
        """
        context = {
            "project_type": self._detect_project_type(exploration_results),
            "tech_stack": self._detect_tech_stack(exploration_results),
            "team_size": self._estimate_team_size(exploration_results),
            "phase": self._detect_development_phase(exploration_results),
            "workflows": self._detect_workflows(exploration_results),
            "structure": self._analyze_structure(exploration_results),
            "modular_recommended": self._should_use_modular(exploration_results)
        }

        self.discoveries = context
        return context

    def _detect_project_type(self, results: Dict[str, Any]) -> str:
        """Detect project type from exploration results."""
        # Check for common project type indicators
        files = results.get('files', [])
        directories = results.get('directories', [])

        # Full-stack indicators
        if ('frontend' in directories or 'client' in directories) and \
           ('backend' in directories or 'server' in directories or 'api' in directories):
            return "fullstack"

        # Frontend indicators
        if any(f in files for f in ['package.json']) and \
           any(d in directories for d in ['src/components', 'components', 'pages']):
            return "web_app"

        # Backend API indicators
        if any(f in files for f in ['requirements.txt', 'go.mod', 'Cargo.toml']):
            if any(d in directories for d in ['api', 'routes', 'controllers']):
                return "api"

        # CLI indicators
        if any(d in directories for d in ['cmd', 'cli', 'bin']):
            return "cli"

        # Library indicators
        if any(f in files for f in ['setup.py', 'pyproject.toml', 'Cargo.toml']) and \
           'examples' in directories:
            return "library"

        # Mobile indicators
        if any(f in files for f in ['app.json', 'ios', 'android']):
            return "mobile"

        # Default to web app
        return "web_app"

    def _detect_tech_stack(self, results: Dict[str, Any]) -> List[str]:
        """Detect technologies used in the project."""
        tech_stack = []
        files = results.get('files', [])
        content = results.get('file_contents', {})

        # JavaScript/TypeScript
        if 'package.json' in files:
            pkg_json = content.get('package.json', {})
            dependencies = pkg_json.get('dependencies', {})

            if 'typescript' in dependencies or any('typescript' in f for f in files):
                tech_stack.append('typescript')
            else:
                tech_stack.append('javascript')

            # Frameworks
            if 'react' in dependencies:
                tech_stack.append('react')
            if 'vue' in dependencies:
                tech_stack.append('vue')
            if 'angular' in dependencies or '@angular/core' in dependencies:
                tech_stack.append('angular')
            if 'next' in dependencies:
                tech_stack.append('next.js')
            if 'express' in dependencies:
                tech_stack.append('express')

        # Python
        if any(f in files for f in ['requirements.txt', 'pyproject.toml', 'setup.py']):
            tech_stack.append('python')

            req_content = content.get('requirements.txt', '')
            if 'fastapi' in req_content.lower():
                tech_stack.append('fastapi')
            elif 'django' in req_content.lower():
                tech_stack.append('django')
            elif 'flask' in req_content.lower():
                tech_stack.append('flask')

        # Go
        if 'go.mod' in files:
            tech_stack.append('go')
            go_mod = content.get('go.mod', '')
            if 'gin-gonic/gin' in go_mod:
                tech_stack.append('gin')
            if 'echo' in go_mod:
                tech_stack.append('echo')

        # Databases
        if any('postgres' in f.lower() for f in files):
            tech_stack.append('postgresql')
        if any('mongo' in f.lower() for f in files):
            tech_stack.append('mongodb')
        if any('redis' in f.lower() for f in files):
            tech_stack.append('redis')

        # Infrastructure
        if 'Dockerfile' in files or 'docker-compose.yml' in files:
            tech_stack.append('docker')
        if any('k8s' in d for d in results.get('directories', [])) or \
           any('kubernetes' in f.lower() for f in files):
            tech_stack.append('kubernetes')

        return tech_stack

    def _estimate_team_size(self, results: Dict[str, Any]) -> str:
        """Estimate team size based on project complexity."""
        directories = results.get('directories', [])
        files = results.get('files', [])

        # Indicators of team size
        complexity_score = 0

        # File count indicator
        if len(files) > 100:
            complexity_score += 2
        elif len(files) > 50:
            complexity_score += 1

        # Directory structure
        if len(directories) > 20:
            complexity_score += 2
        elif len(directories) > 10:
            complexity_score += 1

        # CI/CD presence (indicates larger team)
        if any('.github/workflows' in str(d) for d in directories):
            complexity_score += 1

        # Documentation (larger teams document more)
        if 'docs' in directories or any('documentation' in d for d in directories):
            complexity_score += 1

        # Determine team size
        if complexity_score >= 5:
            return "large"
        elif complexity_score >= 3:
            return "medium"
        elif complexity_score >= 1:
            return "small"
        else:
            return "solo"

    def _detect_development_phase(self, results: Dict[str, Any]) -> str:
        """Detect development phase based on project maturity."""
        files = results.get('files', [])
        directories = results.get('directories', [])

        # Production indicators
        production_indicators = [
            'Dockerfile' in files,
            'docker-compose.yml' in files,
            any('.github/workflows' in str(d) for d in directories),
            'CHANGELOG.md' in files,
            any('deploy' in f.lower() for f in files)
        ]

        if sum(production_indicators) >= 3:
            return "production"
        elif sum(production_indicators) >= 2:
            return "mvp"
        else:
            return "prototype"

    def _detect_workflows(self, results: Dict[str, Any]) -> List[str]:
        """Detect development workflows in use."""
        workflows = []
        files = results.get('files', [])
        directories = results.get('directories', [])

        # TDD indicators
        if any('test' in d for d in directories) or \
           any('test' in f for f in files):
            workflows.append('tdd')

        # CI/CD indicators
        if any('.github/workflows' in str(d) for d in directories) or \
           '.gitlab-ci.yml' in files or \
           'Jenkinsfile' in files:
            workflows.append('cicd')

        # Documentation-first indicators
        if 'docs' in directories or \
           any('documentation' in d for d in directories):
            workflows.append('documentation_first')

        return workflows

    def _analyze_structure(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze project structure."""
        directories = results.get('directories', [])

        return {
            "has_frontend": any(d in directories for d in ['frontend', 'client', 'src/components']),
            "has_backend": any(d in directories for d in ['backend', 'server', 'api']),
            "has_database": any(d in directories for d in ['database', 'db', 'migrations']),
            "has_tests": any('test' in d for d in directories),
            "has_docs": 'docs' in directories or any('documentation' in d for d in directories),
            "has_ci": any('.github' in str(d) for d in directories)
        }

    def _should_use_modular(self, results: Dict[str, Any]) -> bool:
        """Determine if modular CLAUDE.md structure is recommended."""
        structure = self._analyze_structure(results)

        # Recommend modular if:
        # - Has separate frontend and backend
        # - Large number of directories (>15)
        # - Medium/large team size

        return (
            (structure['has_frontend'] and structure['has_backend']) or
            len(results.get('directories', [])) > 15 or
            self._estimate_team_size(results) in ['medium', 'large']
        )

    def generate_confirmation_prompt(self, context: Dict[str, Any]) -> str:
        """
        Generate confirmation prompt to show user the discoveries.

        Args:
            context: Analyzed project context

        Returns:
            Confirmation prompt string
        """
        tech_stack_str = ", ".join(context['tech_stack'][:5])
        if len(context['tech_stack']) > 5:
            tech_stack_str += f" (+{len(context['tech_stack']) - 5} more)"

        prompt = f"""Based on my exploration, here's what I discovered:

**Project Type**: {context['project_type'].replace('_', ' ').title()}
**Tech Stack**: {tech_stack_str}
**Team Size**: {context['team_size'].title()} ({self._get_team_size_range(context['team_size'])})
**Development Phase**: {context['phase'].title()}
**Workflows**: {', '.join(context['workflows']) if context['workflows'] else 'Standard development'}

**Recommended Structure**:
{"Modular architecture (separate CLAUDE.md files for major components)" if context['modular_recommended'] else "Single CLAUDE.md file (appropriate for project size)"}

Would you like me to create a CLAUDE.md file based on these discoveries?

I can:
1. Generate a customized CLAUDE.md tailored to your tech stack
2. Include appropriate sections for your team size and phase
3. {"Create modular files (backend/CLAUDE.md, frontend/CLAUDE.md, etc.)" if context['modular_recommended'] else "Focus on essential guidelines"}

Please confirm to proceed, or let me know if you'd like to adjust any of these settings."""

        return prompt

    def _get_team_size_range(self, team_size: str) -> str:
        """Get human-readable team size range."""
        ranges = {
            "solo": "1 developer",
            "small": "2-9 developers",
            "medium": "10-49 developers",
            "large": "50+ developers"
        }
        return ranges.get(team_size, "Unknown")

    def generate_initialization_summary(self, created_files: List[str]) -> str:
        """
        Generate summary of initialization process.

        Args:
            created_files: List of files created during initialization

        Returns:
            Summary string
        """
        summary = f"""✅ CLAUDE.md Initialization Complete!

**Created Files** ({len(created_files)}):
"""
        for file in created_files:
            summary += f"- {file}\n"

        summary += """
**Next Steps**:
1. Review the generated CLAUDE.md file
2. Customize for your specific needs
3. Add team-specific conventions
4. Update as your project evolves

Your project is now set up for efficient AI-assisted development with Claude Code!
"""
        return summary

    def get_workflow_steps(self) -> List[Dict[str, str]]:
        """
        Get the complete workflow steps for initialization.

        Returns:
            List of workflow steps with descriptions
        """
        return [
            {
                "step": 1,
                "name": "Check for existing CLAUDE.md",
                "description": "Verify if CLAUDE.md already exists in project",
                "action": "check_claude_md_exists"
            },
            {
                "step": 2,
                "name": "Explore repository",
                "description": "Analyze project structure, tech stack, and workflows using Claude Code's built-in explore capability",
                "action": "generate_exploration_prompt"
            },
            {
                "step": 3,
                "name": "Analyze discoveries",
                "description": "Detect project type, tech stack, team size, and recommend structure",
                "action": "analyze_discoveries"
            },
            {
                "step": 4,
                "name": "Request user confirmation",
                "description": "Show discoveries and ask user to confirm CLAUDE.md creation",
                "action": "generate_confirmation_prompt"
            },
            {
                "step": 5,
                "name": "Create CLAUDE.md file(s)",
                "description": "Generate customized CLAUDE.md based on confirmed context",
                "action": "create_files"
            },
            {
                "step": 6,
                "name": "Enhance with best practices",
                "description": "Apply additional enhancements and validate quality",
                "action": "enhance_files"
            },
            {
                "step": 7,
                "name": "Provide summary",
                "description": "Show what was created and next steps",
                "action": "generate_initialization_summary"
            }
        ]
