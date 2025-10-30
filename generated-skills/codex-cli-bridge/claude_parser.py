"""
Claude Code Project Parser

Parses CLAUDE.md and extracts project structure information:
- CLAUDE.md sections (overview, workflows, quality gates)
- Skills directories (.claude/skills/, ~/.claude/skills/)
- Agents directories (.claude/agents/)
- Documentation folder structure
- MCP server configuration

Returns file paths only - no content duplication (reference-based approach)
"""

import os
import re
import yaml
from typing import Dict, List, Optional, Any
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class SkillInfo:
    """Information about a Claude Code skill."""
    name: str
    description: str
    location: str  # Relative path from project root
    skill_md_path: str
    python_files: List[str] = field(default_factory=list)
    has_python: bool = False
    is_functional: bool = False  # Has Python scripts vs prompt-only

    def __post_init__(self):
        """Determine if skill is functional (has Python) or prompt-only."""
        self.is_functional = len(self.python_files) > 0


@dataclass
class AgentInfo:
    """Information about a Claude Code agent."""
    name: str
    description: str
    location: str  # Relative path from project root
    tools: List[str] = field(default_factory=list)
    field: Optional[str] = None
    color: Optional[str] = None
    expertise: Optional[str] = None
    model: Optional[str] = None


@dataclass
class MCPServerInfo:
    """Information about an MCP server."""
    name: str
    command: str
    description: Optional[str] = None


@dataclass
class ClaudeMdSection:
    """Parsed section from CLAUDE.md."""
    title: str
    content: str
    level: int  # Heading level (1-6)


class ClaudeProjectParser:
    """
    Parse Claude Code project structure.

    Extracts metadata from CLAUDE.md, skills, agents, and documentation.
    Returns file paths only - no content duplication.
    """

    def __init__(self, project_root: str):
        """
        Initialize parser.

        Args:
            project_root: Path to project root directory
        """
        self.project_root = Path(project_root).resolve()
        self.claude_md_path = self.project_root / "CLAUDE.md"

        # Parsed data
        self.claude_md_content: Optional[str] = None
        self.claude_md_sections: List[ClaudeMdSection] = []
        self.skills: List[SkillInfo] = []
        self.agents: List[AgentInfo] = []
        self.mcp_servers: List[MCPServerInfo] = []

    def parse_all(self) -> Dict[str, Any]:
        """
        Parse all project components.

        Returns:
            Dictionary with all parsed data
        """
        print("📖 Parsing Claude Code project...")

        # Parse CLAUDE.md
        self.parse_claude_md()

        # Scan skills
        self.scan_skills()

        # Scan agents
        self.scan_agents()

        # Parse MCP servers (would need to read Claude settings)
        # For now, return empty list
        self.mcp_servers = []

        print(f"   ✅ Found {len(self.skills)} skills")
        print(f"   ✅ Found {len(self.agents)} agents")
        print(f"   ✅ Found {len(self.claude_md_sections)} CLAUDE.md sections")
        print()

        return {
            "claude_md_path": str(self.claude_md_path),
            "claude_md_sections": self.claude_md_sections,
            "skills": self.skills,
            "agents": self.agents,
            "mcp_servers": self.mcp_servers,
            "project_root": str(self.project_root)
        }

    def parse_claude_md(self) -> None:
        """Parse CLAUDE.md and extract sections."""
        if not self.claude_md_path.exists():
            raise FileNotFoundError(f"CLAUDE.md not found at {self.claude_md_path}")

        with open(self.claude_md_path, "r", encoding="utf-8") as f:
            self.claude_md_content = f.read()

        # Extract sections by headings
        self.claude_md_sections = self._extract_sections(self.claude_md_content)

    def _extract_sections(self, content: str) -> List[ClaudeMdSection]:
        """
        Extract sections from Markdown content.

        Args:
            content: Markdown content

        Returns:
            List of ClaudeMdSection objects
        """
        sections = []

        # Split by headings (# - ######)
        heading_pattern = r'^(#{1,6})\s+(.+?)$'
        lines = content.split('\n')

        current_section = None
        current_content = []

        for line in lines:
            match = re.match(heading_pattern, line)
            if match:
                # Save previous section
                if current_section:
                    sections.append(ClaudeMdSection(
                        title=current_section["title"],
                        content='\n'.join(current_content).strip(),
                        level=current_section["level"]
                    ))

                # Start new section
                level = len(match.group(1))
                title = match.group(2).strip()
                current_section = {"title": title, "level": level}
                current_content = []
            else:
                if current_section:
                    current_content.append(line)

        # Save last section
        if current_section:
            sections.append(ClaudeMdSection(
                title=current_section["title"],
                content='\n'.join(current_content).strip(),
                level=current_section["level"]
            ))

        return sections

    def scan_skills(self) -> None:
        """Scan skill directories and extract metadata."""
        skills_dirs = [
            self.project_root / ".claude" / "skills",
            Path.home() / ".claude" / "skills",
            self.project_root / "generated-skills",
            self.project_root / "claude-skills-examples"
        ]

        for skills_dir in skills_dirs:
            if not skills_dir.exists():
                continue

            # Scan each directory in skills folder
            for skill_path in skills_dir.iterdir():
                if not skill_path.is_dir():
                    continue

                # Look for SKILL.md
                skill_md = skill_path / "SKILL.md"
                if not skill_md.exists():
                    # Try lowercase
                    skill_md = skill_path / "skill.md"
                    if not skill_md.exists():
                        continue

                # Parse skill
                skill_info = self._parse_skill(skill_path, skill_md)
                if skill_info:
                    self.skills.append(skill_info)

    def _parse_skill(self, skill_path: Path, skill_md: Path) -> Optional[SkillInfo]:
        """
        Parse a single skill.

        Args:
            skill_path: Path to skill directory
            skill_md: Path to SKILL.md file

        Returns:
            SkillInfo object or None if parsing fails
        """
        try:
            with open(skill_md, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract YAML frontmatter
            yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not yaml_match:
                return None

            frontmatter = yaml.safe_load(yaml_match.group(1))
            name = frontmatter.get("name", skill_path.name)
            description = frontmatter.get("description", "")

            # Find Python files
            python_files = []
            for py_file in skill_path.glob("*.py"):
                # Get relative path from project root
                try:
                    rel_path = py_file.relative_to(self.project_root)
                    python_files.append(str(rel_path))
                except ValueError:
                    # File is outside project root (e.g., ~/.claude/skills)
                    python_files.append(str(py_file))

            # Get relative location
            try:
                location = str(skill_path.relative_to(self.project_root))
            except ValueError:
                location = str(skill_path)

            # Get relative SKILL.md path
            try:
                skill_md_rel = str(skill_md.relative_to(self.project_root))
            except ValueError:
                skill_md_rel = str(skill_md)

            return SkillInfo(
                name=name,
                description=description,
                location=location,
                skill_md_path=skill_md_rel,
                python_files=python_files,
                has_python=len(python_files) > 0
            )

        except Exception as e:
            print(f"   ⚠️  Failed to parse skill at {skill_path}: {e}")
            return None

    def scan_agents(self) -> None:
        """Scan agent directories and extract metadata."""
        agents_dirs = [
            self.project_root / ".claude" / "agents",
            Path.home() / ".claude" / "agents"
        ]

        for agents_dir in agents_dirs:
            if not agents_dir.exists():
                continue

            # Scan each .md file in agents folder
            for agent_file in agents_dir.glob("*.md"):
                agent_info = self._parse_agent(agent_file)
                if agent_info:
                    self.agents.append(agent_info)

    def _parse_agent(self, agent_file: Path) -> Optional[AgentInfo]:
        """
        Parse a single agent file.

        Args:
            agent_file: Path to agent .md file

        Returns:
            AgentInfo object or None if parsing fails
        """
        try:
            with open(agent_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract YAML frontmatter
            yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not yaml_match:
                return None

            frontmatter = yaml.safe_load(yaml_match.group(1))
            name = frontmatter.get("name", agent_file.stem)
            description = frontmatter.get("description", "")
            tools = frontmatter.get("tools", [])
            field = frontmatter.get("field")
            color = frontmatter.get("color")
            expertise = frontmatter.get("expertise")
            model = frontmatter.get("model")

            # Get relative location
            try:
                location = str(agent_file.relative_to(self.project_root))
            except ValueError:
                location = str(agent_file)

            return AgentInfo(
                name=name,
                description=description,
                location=location,
                tools=tools,
                field=field,
                color=color,
                expertise=expertise,
                model=model
            )

        except Exception as e:
            print(f"   ⚠️  Failed to parse agent at {agent_file}: {e}")
            return None

    def get_section(self, title_pattern: str) -> Optional[ClaudeMdSection]:
        """
        Get first section matching title pattern.

        Args:
            title_pattern: Regex pattern to match section title

        Returns:
            ClaudeMdSection or None if not found
        """
        for section in self.claude_md_sections:
            if re.search(title_pattern, section.title, re.IGNORECASE):
                return section
        return None

    def get_sections_by_level(self, level: int) -> List[ClaudeMdSection]:
        """
        Get all sections at a specific heading level.

        Args:
            level: Heading level (1-6)

        Returns:
            List of ClaudeMdSection objects
        """
        return [s for s in self.claude_md_sections if s.level == level]

    def get_overview_section(self) -> Optional[str]:
        """Get project overview/purpose section content."""
        patterns = [
            r"repository\s+purpose",
            r"project\s+overview",
            r"purpose",
            r"about"
        ]

        for pattern in patterns:
            section = self.get_section(pattern)
            if section:
                return section.content

        return None


def main():
    """Demo usage of ClaudeProjectParser."""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Parse Claude Code project")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root directory (default: current directory)"
    )
    parser.add_argument(
        "--output",
        choices=["summary", "json", "skills", "agents"],
        default="summary",
        help="Output format"
    )

    args = parser.parse_args()

    # Parse project
    claude_parser = ClaudeProjectParser(args.project_root)
    data = claude_parser.parse_all()

    if args.output == "summary":
        print("=" * 60)
        print("📊 Parse Summary")
        print("=" * 60)
        print(f"Project Root: {data['project_root']}")
        print(f"CLAUDE.md: {data['claude_md_path']}")
        print(f"Skills: {len(data['skills'])}")
        print(f"Agents: {len(data['agents'])}")
        print(f"MCP Servers: {len(data['mcp_servers'])}")
        print(f"Sections: {len(data['claude_md_sections'])}")
        print("=" * 60)

    elif args.output == "skills":
        print("📦 Skills:")
        for skill in data['skills']:
            print(f"\n  {skill.name}")
            print(f"    Description: {skill.description[:60]}...")
            print(f"    Location: {skill.location}")
            print(f"    Type: {'Functional' if skill.is_functional else 'Prompt-only'}")
            if skill.python_files:
                print(f"    Python files: {len(skill.python_files)}")

    elif args.output == "agents":
        print("🤖 Agents:")
        for agent in data['agents']:
            print(f"\n  {agent.name}")
            print(f"    Description: {agent.description[:60]}...")
            print(f"    Location: {agent.location}")
            if agent.tools:
                print(f"    Tools: {', '.join(agent.tools)}")

    elif args.output == "json":
        # Convert dataclasses to dicts for JSON serialization
        output = {
            "project_root": data["project_root"],
            "claude_md_path": data["claude_md_path"],
            "skills": [
                {
                    "name": s.name,
                    "description": s.description,
                    "location": s.location,
                    "skill_md_path": s.skill_md_path,
                    "python_files": s.python_files,
                    "is_functional": s.is_functional
                }
                for s in data["skills"]
            ],
            "agents": [
                {
                    "name": a.name,
                    "description": a.description,
                    "location": a.location,
                    "tools": a.tools
                }
                for a in data["agents"]
            ],
            "sections": [
                {
                    "title": s.title,
                    "level": s.level,
                    "content_length": len(s.content)
                }
                for s in data["claude_md_sections"]
            ]
        }
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
