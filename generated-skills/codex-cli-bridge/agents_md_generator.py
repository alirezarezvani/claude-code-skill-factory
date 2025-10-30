"""
AGENTS.md Generator for Codex CLI Bridge

Generates comprehensive AGENTS.md from Claude Code project structure:
- Template-based generation with file path references
- Documents skills with most relevant usage method
- Translates workflows (slash commands → Codex equivalents)
- Includes MCP integration
- Creates command reference table
- Reference-based: No file duplication, only links to existing files
"""

import os
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime

from claude_parser import SkillInfo, AgentInfo, ClaudeMdSection
from project_analyzer import ProjectMetadata, ProjectStructure
from skill_documenter import SkillDocumenter


class AgentsMdGenerator:
    """
    Generate AGENTS.md from Claude Code project.

    Uses template-based approach with file path references.
    No content duplication - only links to existing files.
    """

    def __init__(self, project_root: str):
        """
        Initialize generator.

        Args:
            project_root: Path to project root directory
        """
        self.project_root = Path(project_root).resolve()
        self.skill_documenter = SkillDocumenter()

    def generate(
        self,
        metadata: ProjectMetadata,
        structure: ProjectStructure,
        skills: List[SkillInfo],
        agents: List[AgentInfo],
        claude_md_sections: List[ClaudeMdSection],
        mcp_servers: List[Dict] = None
    ) -> str:
        """
        Generate complete AGENTS.md content.

        Args:
            metadata: Project metadata
            structure: Project structure
            skills: List of skills
            agents: List of agents
            claude_md_sections: CLAUDE.md sections
            mcp_servers: Optional MCP server info

        Returns:
            Complete AGENTS.md content as string
        """
        print("📝 Generating AGENTS.md...")

        mcp_servers = mcp_servers or []

        # Build AGENTS.md content
        content = []

        # Header
        content.append(self._generate_header(metadata))

        # Quick Reference
        content.append(self._generate_quick_reference(metadata, skills, agents))

        # Project Overview
        content.append(self._generate_project_overview(metadata, claude_md_sections))

        # Available Skills
        if skills:
            content.append(self._generate_skills_section(skills))

        # Project Structure
        content.append(self._generate_structure_section(metadata, structure))

        # Workflow Patterns
        content.append(self._generate_workflow_patterns())

        # MCP Integration
        if mcp_servers:
            content.append(self._generate_mcp_section(mcp_servers))

        # Command Reference
        content.append(self._generate_command_reference())

        # Common Operations
        content.append(self._generate_common_operations())

        # Best Practices
        content.append(self._generate_best_practices())

        # Footer
        content.append(self._generate_footer(metadata))

        print("   ✅ AGENTS.md generated successfully")

        return "\n\n".join(content)

    def _generate_header(self, metadata: ProjectMetadata) -> str:
        """Generate AGENTS.md header."""
        return f"""# AGENTS.md

**Project**: {metadata.name}
**Purpose**: {metadata.description}
**Type**: {metadata.type}
**Codex CLI Compatibility**: Full support with reference-based architecture

---"""

    def _generate_quick_reference(
        self,
        metadata: ProjectMetadata,
        skills: List[SkillInfo],
        agents: List[AgentInfo]
    ) -> str:
        """Generate quick reference section."""
        functional_skills = [s for s in skills if s.is_functional]
        prompt_skills = [s for s in skills if not s.is_functional]

        return f"""## Quick Reference

This project is a **Claude Code project** that can be used with **Codex CLI**.

**Project Statistics**:
- **Skills**: {len(skills)} total ({len(functional_skills)} functional, {len(prompt_skills)} prompt-based)
- **Agents**: {len(agents)} total
- **Documentation**: {"✅ Yes" if metadata.documentation_exists else "❌ No"}

**For Codex CLI Users**:
- Skills are documented below with Codex CLI usage examples
- Use `codex exec` commands (never plain `codex`)
- Python scripts can be executed directly
- All file references are relative to project root

---"""

    def _generate_project_overview(
        self,
        metadata: ProjectMetadata,
        claude_md_sections: List[ClaudeMdSection]
    ) -> str:
        """Generate project overview from CLAUDE.md."""
        # Find overview section
        overview = None
        for section in claude_md_sections:
            title_lower = section.title.lower()
            if any(keyword in title_lower for keyword in ["purpose", "overview", "about"]):
                overview = section.content
                break

        if not overview:
            overview = metadata.description

        # Limit length
        if len(overview) > 500:
            overview = overview[:497] + "..."

        return f"""## Project Overview

{overview}

**Project Type**: {metadata.type}
**Root Directory**: `{metadata.name}/`

---"""

    def _generate_skills_section(self, skills: List[SkillInfo]) -> str:
        """Generate available skills section."""
        functional_skills = [s for s in skills if s.is_functional]
        prompt_skills = [s for s in skills if not s.is_functional]

        content = ["## Available Skills"]
        content.append("")
        content.append(f"This project includes **{len(skills)} skills** that can be used with Codex CLI.")
        content.append("")

        if functional_skills:
            content.append(f"### Functional Skills ({len(functional_skills)})")
            content.append("")
            content.append("These skills have Python scripts that can be executed directly:")
            content.append("")

            for skill in functional_skills:
                content.append(self.skill_documenter.document_functional_skill(skill))
                content.append("")

        if prompt_skills:
            content.append(f"### Prompt-Based Skills ({len(prompt_skills)})")
            content.append("")
            content.append("These skills provide guidance through documentation:")
            content.append("")

            for skill in prompt_skills:
                content.append(self.skill_documenter.document_prompt_skill(skill))
                content.append("")

        content.append("---")

        return "\n".join(content)

    def _generate_structure_section(
        self,
        metadata: ProjectMetadata,
        structure: ProjectStructure
    ) -> str:
        """Generate project structure section."""
        content = ["## Project Structure"]
        content.append("")
        content.append("```")
        content.append(f"{metadata.name}/")

        # Add key files
        for file in sorted(structure.key_files):
            content.append(f"├── {file}")

        # Add folders
        for folder in sorted(structure.folders):
            content.append(f"├── {folder}/")

        content.append("```")
        content.append("")
        content.append("**Key Components**:")

        # Describe key components
        if "CLAUDE.md" in structure.key_files:
            content.append("- `CLAUDE.md` - Claude Code configuration (source of truth)")

        if "AGENTS.md" in structure.key_files:
            content.append("- `AGENTS.md` - This file (Codex CLI bridge documentation)")

        if ".claude/skills" in structure.folders:
            content.append("- `.claude/skills/` - Project-specific Claude skills")

        if ".claude/agents" in structure.folders:
            content.append("- `.claude/agents/` - Custom Claude Code agents")

        if "documentation" in structure.folders:
            content.append("- `documentation/` - Project documentation")

        if "generated-skills" in structure.folders:
            content.append("- `generated-skills/` - Production-ready skills")

        content.append("")
        content.append("---")

        return "\n".join(content)

    def _generate_workflow_patterns(self) -> str:
        """Generate workflow patterns (slash commands → Codex equivalents)."""
        return """## Workflow Patterns

Common Claude Code workflows and their Codex CLI equivalents:

### Generate New Skill

**Claude Code**:
```
User: "Create a skill for data visualization"
→ Skills Factory auto-activates
→ Generates complete skill package
```

**Codex CLI Equivalent**:
```bash
codex exec -m gpt-5 -s workspace-write --full-auto \\
  --skip-git-repo-check \\
  "Using the Skills Factory Prompt template, generate a
  data visualization skill with Python scripts for chart
  generation, interactive dashboards, and export functionality"
```

---

### Code Review

**Claude Code**: `/code-review`

**Codex CLI**:
```bash
codex exec -m gpt-5 -s read-only \\
  --skip-git-repo-check \\
  "Review this codebase for:
  - Code quality issues
  - Security vulnerabilities
  - Performance bottlenecks
  - Best practices violations
  Provide detailed report with file references"
```

---

### Run Tests

**Claude Code**: `/test`

**Codex CLI**:
```bash
codex exec -m gpt-5-codex -s workspace-write \\
  --skip-git-repo-check \\
  "Run all tests in this project and analyze any failures.
  Provide detailed failure reports with suggested fixes."
```

---

### Documentation Generation

**Claude Code**: `/docs-generate` or rr-tech-writer agent

**Codex CLI**:
```bash
codex exec -m gpt-5 -s workspace-write --full-auto \\
  --skip-git-repo-check \\
  "Generate comprehensive documentation for this project:
  - Update README.md with current features
  - Create API documentation
  - Update CHANGELOG.md with recent changes"
```

---

### Architecture Design

**Claude Code**: `/architect` or rr-architect agent

**Codex CLI**:
```bash
codex exec -m gpt-5 -s read-only \\
  -c model_reasoning_effort=high \\
  --skip-git-repo-check \\
  "Analyze current architecture and propose:
  - System architecture diagram
  - Technology stack recommendations
  - Scalability improvements
  - Performance optimization strategies"
```

---"""

    def _generate_mcp_section(self, mcp_servers: List[Dict]) -> str:
        """Generate MCP integration section."""
        content = ["## MCP Integration"]
        content.append("")
        content.append("Both Claude Code and Codex CLI support Model Context Protocol (MCP) servers.")
        content.append("")

        if mcp_servers:
            content.append("**Configured MCP Servers**:")
            content.append("")

            for server in mcp_servers:
                name = server.get("name", "Unknown")
                command = server.get("command", "")
                description = server.get("description", "")

                content.append(f"### {name}")
                if description:
                    content.append(f"**Description**: {description}")
                content.append(f"**Command**: `{command}`")
                content.append("")

            content.append("**Using with Codex CLI**:")
            content.append("```bash")
            content.append("# List MCP servers")
            content.append("codex mcp list")
            content.append("")
            content.append("# Use in session")
            content.append('codex exec --config experimental_use_rmcp_client=true \\')
            content.append('  "Your task using MCP servers"')
            content.append("```")
        else:
            content.append("**No MCP servers configured.**")
            content.append("")
            content.append("To add MCP servers, configure them in Claude Code settings.")

        content.append("")
        content.append("---")

        return "\n".join(content)

    def _generate_command_reference(self) -> str:
        """Generate command reference table."""
        return """## Command Reference

| Operation | Claude Code | Codex CLI |
|-----------|-------------|-----------|
| Start session | `claude` | `codex` or `codex exec` |
| Resume session | `/resume-work` | `codex exec resume --last` |
| Code review | `/code-review` | `codex exec "review code"` |
| Run tests | `/test` | `codex exec "run tests"` |
| Generate docs | `/docs-generate` | `codex exec "generate docs"` |
| Plan feature | `/create-plan` | `codex exec -m gpt-5 "plan feature"` |
| Architecture | `/architect` | `codex exec -m gpt-5 -c model_reasoning_effort=high "design architecture"` |
| Build feature | `/implement` | `codex exec -m gpt-5-codex -s workspace-write "implement feature"` |

---"""

    def _generate_common_operations(self) -> str:
        """Generate common operations section."""
        return """## Common Operations

### Execute Skill Python Script

**For functional skills with Python files**:

```bash
# Navigate to skill directory
cd generated-skills/skill-name/

# Run Python script
python script_name.py --arg value

# Example: AWS architecture designer
cd generated-skills/aws-solution-architect/
python architecture_designer.py --requirements requirements.json
```

---

### Reference Skill in Codex Prompt

**For prompt-based skills or complex workflows**:

```bash
codex exec -m gpt-5 -s read-only \\
  "Using the skill documentation at path/to/SKILL.md,
  perform the following task: [your task description]"
```

---

### Combine Multiple Skills

```bash
codex exec -m gpt-5 -s workspace-write \\
  "Referencing the following skills:
  - Skill 1 at path/to/skill1/SKILL.md
  - Skill 2 at path/to/skill2/SKILL.md

  Perform this complex task: [task description]"
```

---

### Resume Previous Session

```bash
# Resume last session
codex exec resume --last

# Or choose from history
codex exec resume
# (opens interactive picker)
```

---"""

    def _generate_best_practices(self) -> str:
        """Generate best practices section."""
        return """## Best Practices for Codex CLI Users

### 1. Always Use `codex exec`

❌ **WRONG**: `codex -m gpt-5 "task"`
✅ **CORRECT**: `codex exec -m gpt-5 "task"`

**Why**: Claude Code runs in a non-terminal environment. Plain `codex` commands fail with "stdout is not a terminal" error.

---

### 2. Choose Correct Model

**gpt-5** (General reasoning):
- Architecture design
- Code analysis
- Documentation
- Planning

**gpt-5-codex** (Code editing):
- Refactoring
- Bug fixes
- Feature implementation
- Test generation

Example:
```bash
# Analysis: use gpt-5
codex exec -m gpt-5 -s read-only "analyze security"

# Editing: use gpt-5-codex
codex exec -m gpt-5-codex -s workspace-write "refactor code"
```

---

### 3. Choose Correct Sandbox Mode

**read-only** (Safe, default):
- Code review
- Analysis
- Documentation reading

**workspace-write** (File modifications):
- Code editing
- Documentation generation
- Test creation

**danger-full-access** (Network, rarely needed):
- Web scraping
- API calls
- External data fetching

---

### 4. Reference Skills Properly

**Functional skills** (has Python):
```bash
# Execute directly
cd skill-directory/
python script.py
```

**Prompt skills** (documentation only):
```bash
# Reference in prompt
codex exec "Using SKILL.md at path/to/skill, do task"
```

---

### 5. Use High Reasoning for Complex Tasks

```bash
codex exec -m gpt-5 \\
  -c model_reasoning_effort=high \\
  -s read-only \\
  "Complex architecture analysis task"
```

---"""

    def _generate_footer(self, metadata: ProjectMetadata) -> str:
        """Generate footer with metadata."""
        timestamp = datetime.now().strftime("%Y-%m-%d")

        return f"""## References

- **CLAUDE.md**: Project configuration for Claude Code
- **Skills Documentation**: See individual SKILL.md files in skill directories
- **Codex CLI Docs**: https://github.com/openai/codex
- **Claude Code Docs**: https://docs.claude.com/claude-code

---

**Last Updated**: {timestamp}
**Generated By**: codex-cli-bridge skill
**Project Type**: {metadata.type}
**Maintained For**: Cross-tool team collaboration (Claude Code ↔ Codex CLI)
**Sync Strategy**: One-way sync (CLAUDE.md → AGENTS.md)

---

*This AGENTS.md is auto-generated from CLAUDE.md and project structure.*
*To update, modify CLAUDE.md and run: `/sync-agents-md` or regenerate with codex-cli-bridge skill.*"""


def main():
    """Demo usage of AgentsMdGenerator."""
    import argparse
    from project_analyzer import ProjectAnalyzer

    parser = argparse.ArgumentParser(description="Generate AGENTS.md")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root directory (default: current directory)"
    )
    parser.add_argument(
        "--output",
        default="AGENTS.md",
        help="Output file path (default: AGENTS.md)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print to stdout instead of writing file"
    )

    args = parser.parse_args()

    # Analyze project
    analyzer = ProjectAnalyzer(args.project_root)
    analysis = analyzer.analyze()

    # Generate AGENTS.md
    generator = AgentsMdGenerator(args.project_root)
    agents_md = generator.generate(
        metadata=analysis["metadata"],
        structure=analysis["structure"],
        skills=analysis["parsed_data"]["skills"],
        agents=analysis["parsed_data"]["agents"],
        claude_md_sections=analysis["parsed_data"]["claude_md_sections"],
        mcp_servers=analysis["parsed_data"].get("mcp_servers", [])
    )

    if args.dry_run:
        print(agents_md)
    else:
        output_path = Path(args.project_root) / args.output
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(agents_md)

        print(f"✅ AGENTS.md written to: {output_path}")


if __name__ == "__main__":
    main()
