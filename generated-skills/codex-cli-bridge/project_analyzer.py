"""
Project Analyzer for Codex CLI Bridge

Analyzes Claude Code project structure:
- Auto-detect project root and type
- Discover all Claude Code assets (skills, agents, commands)
- Generate project metadata
- Build reference map
- Categorize skills by type
"""

import os
import json
from typing import Dict, List, Optional, Any
from pathlib import Path
from dataclasses import dataclass, field, asdict

from claude_parser import ClaudeProjectParser, SkillInfo, AgentInfo


@dataclass
class ProjectMetadata:
    """Complete project metadata."""
    name: str
    root: str
    type: str  # GREENFIELD_NEW, ENTERPRISE_REFACTOR, LEGACY_MODERNIZATION
    description: str
    has_claude_md: bool
    has_agents_md: bool
    skill_count: int
    agent_count: int
    documentation_exists: bool


@dataclass
class ProjectStructure:
    """Project folder structure."""
    folders: List[str] = field(default_factory=list)
    key_files: List[str] = field(default_factory=list)
    documentation_files: List[str] = field(default_factory=list)


class ProjectAnalyzer:
    """
    Comprehensive project analysis.

    Combines parsing with analysis to build complete project understanding.
    """

    def __init__(self, project_root: str):
        """
        Initialize analyzer.

        Args:
            project_root: Path to project root directory
        """
        self.project_root = Path(project_root).resolve()
        self.parser = ClaudeProjectParser(str(self.project_root))

        # Analysis results
        self.metadata: Optional[ProjectMetadata] = None
        self.structure: Optional[ProjectStructure] = None
        self.parsed_data: Optional[Dict] = None

    def analyze(self) -> Dict[str, Any]:
        """
        Perform complete project analysis.

        Returns:
            Dictionary with all analysis results
        """
        print("🔍 Analyzing project structure...")

        # Parse project
        self.parsed_data = self.parser.parse_all()

        # Generate metadata
        self.metadata = self._generate_metadata()

        # Analyze structure
        self.structure = self._analyze_structure()

        # Categorize skills
        functional_skills = [s for s in self.parsed_data["skills"] if s.is_functional]
        prompt_skills = [s for s in self.parsed_data["skills"] if not s.is_functional]

        print(f"   📊 Project: {self.metadata.name}")
        print(f"   📁 Type: {self.metadata.type}")
        print(f"   📦 Skills: {self.metadata.skill_count} ({len(functional_skills)} functional, {len(prompt_skills)} prompt-only)")
        print(f"   🤖 Agents: {self.metadata.agent_count}")
        print()

        return {
            "metadata": asdict(self.metadata),
            "structure": asdict(self.structure),
            "parsed_data": self.parsed_data,
            "functional_skills": functional_skills,
            "prompt_skills": prompt_skills
        }

    def _generate_metadata(self) -> ProjectMetadata:
        """Generate project metadata."""
        # Get project name
        name = self.project_root.name

        # Detect project type from CLAUDE.md or default
        project_type = self._detect_project_type()

        # Get description
        description = self.parser.get_overview_section() or f"{name} project"
        if len(description) > 200:
            description = description[:197] + "..."

        # Check for files
        has_claude_md = (self.project_root / "CLAUDE.md").exists()
        has_agents_md = (self.project_root / "AGENTS.md").exists()
        documentation_exists = (self.project_root / "documentation").exists()

        return ProjectMetadata(
            name=name,
            root=str(self.project_root),
            type=project_type,
            description=description,
            has_claude_md=has_claude_md,
            has_agents_md=has_agents_md,
            skill_count=len(self.parsed_data["skills"]),
            agent_count=len(self.parsed_data["agents"]),
            documentation_exists=documentation_exists
        )

    def _detect_project_type(self) -> str:
        """
        Detect project type from CLAUDE.md or structure.

        Returns:
            GREENFIELD_NEW, ENTERPRISE_REFACTOR, or LEGACY_MODERNIZATION
        """
        # Check CLAUDE.md for type mentions
        if self.parsed_data.get("claude_md_sections"):
            for section in self.parsed_data["claude_md_sections"]:
                content = section.content.lower()
                if "greenfield_new" in content or "greenfield new" in content:
                    return "GREENFIELD_NEW"
                elif "enterprise_refactor" in content or "enterprise refactor" in content:
                    return "ENTERPRISE_REFACTOR"
                elif "legacy_modernization" in content or "legacy modernization" in content:
                    return "LEGACY_MODERNIZATION"

        # Default
        return "GREENFIELD_NEW"

    def _analyze_structure(self) -> ProjectStructure:
        """Analyze project folder structure."""
        folders = []
        key_files = []
        documentation_files = []

        # Key folders to check
        important_folders = [
            ".claude/skills",
            ".claude/agents",
            ".claude/commands",
            "documentation",
            "generated-skills",
            "claude-skills-examples",
            "src",
            "lib",
            "tests"
        ]

        for folder in important_folders:
            folder_path = self.project_root / folder
            if folder_path.exists():
                folders.append(folder)

        # Key files to check
        important_files = [
            "CLAUDE.md",
            "AGENTS.md",
            "README.md",
            "CHANGELOG.md",
            "package.json",
            "requirements.txt",
            "pyproject.toml",
            ".gitignore"
        ]

        for file in important_files:
            file_path = self.project_root / file
            if file_path.exists():
                key_files.append(file)

        # Documentation files
        docs_dir = self.project_root / "documentation"
        if docs_dir.exists():
            for doc_file in docs_dir.rglob("*.md"):
                rel_path = doc_file.relative_to(self.project_root)
                documentation_files.append(str(rel_path))

        return ProjectStructure(
            folders=folders,
            key_files=key_files,
            documentation_files=documentation_files
        )

    def get_skill_by_name(self, name: str) -> Optional[SkillInfo]:
        """
        Find skill by name.

        Args:
            name: Skill name

        Returns:
            SkillInfo or None
        """
        if not self.parsed_data:
            return None

        for skill in self.parsed_data["skills"]:
            if skill.name == name:
                return skill
        return None

    def get_agent_by_name(self, name: str) -> Optional[AgentInfo]:
        """
        Find agent by name.

        Args:
            name: Agent name

        Returns:
            AgentInfo or None
        """
        if not self.parsed_data:
            return None

        for agent in self.parsed_data["agents"]:
            if agent.name == name:
                return agent
        return None

    def generate_summary_report(self) -> str:
        """
        Generate human-readable summary report.

        Returns:
            Formatted summary string
        """
        if not self.metadata or not self.structure:
            return "No analysis performed yet. Run analyze() first."

        report = f"""
╔══════════════════════════════════════════════════════════════╗
║                   PROJECT ANALYSIS SUMMARY                   ║
╚══════════════════════════════════════════════════════════════╝

📁 Project Information
  Name:        {self.metadata.name}
  Type:        {self.metadata.type}
  Root:        {self.metadata.root}
  Description: {self.metadata.description}

📄 Key Files
  CLAUDE.md:       {'✅ Yes' if self.metadata.has_claude_md else '❌ No'}
  AGENTS.md:       {'✅ Yes' if self.metadata.has_agents_md else '❌ No'}
  Documentation:   {'✅ Yes' if self.metadata.documentation_exists else '❌ No'}

📊 Statistics
  Skills:      {self.metadata.skill_count}
  Agents:      {self.metadata.agent_count}
  Folders:     {len(self.structure.folders)}
  Key Files:   {len(self.structure.key_files)}
  Doc Files:   {len(self.structure.documentation_files)}

📁 Project Structure
"""

        # Add folders
        if self.structure.folders:
            report += "\n  Folders:\n"
            for folder in sorted(self.structure.folders):
                report += f"    ✓ {folder}\n"

        # Add key files
        if self.structure.key_files:
            report += "\n  Key Files:\n"
            for file in sorted(self.structure.key_files):
                report += f"    ✓ {file}\n"

        report += "\n" + "=" * 64 + "\n"

        return report


def main():
    """Demo usage of ProjectAnalyzer."""
    import argparse

    parser = argparse.ArgumentParser(description="Analyze Claude Code project")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root directory (default: current directory)"
    )
    parser.add_argument(
        "--output",
        choices=["summary", "json", "report"],
        default="summary",
        help="Output format"
    )

    args = parser.parse_args()

    # Analyze project
    analyzer = ProjectAnalyzer(args.project_root)
    analysis = analyzer.analyze()

    if args.output == "summary":
        print("=" * 64)
        print("ANALYSIS COMPLETE")
        print("=" * 64)
        print(f"Project: {analysis['metadata']['name']}")
        print(f"Skills: {analysis['metadata']['skill_count']}")
        print(f"Agents: {analysis['metadata']['agent_count']}")
        print(f"Functional skills: {len(analysis['functional_skills'])}")
        print(f"Prompt skills: {len(analysis['prompt_skills'])}")

    elif args.output == "report":
        print(analyzer.generate_summary_report())

    elif args.output == "json":
        # Convert dataclasses to dicts for JSON
        output = {
            "metadata": analysis["metadata"],
            "structure": analysis["structure"],
            "skills": [
                {
                    "name": s.name,
                    "description": s.description,
                    "location": s.location,
                    "is_functional": s.is_functional
                }
                for s in analysis["parsed_data"]["skills"]
            ],
            "agents": [
                {
                    "name": a.name,
                    "description": a.description,
                    "location": a.location
                }
                for a in analysis["parsed_data"]["agents"]
            ]
        }
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
