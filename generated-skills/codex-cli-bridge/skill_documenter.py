"""
Skill Documenter for Codex CLI Bridge

Documents Claude Code skills for Codex CLI users:
- Determines most relevant usage method per skill type
- Functional skills: Execute Python scripts directly
- Prompt-based skills: Reference in Codex prompts
- Generates bash examples and prompt templates
- Reference-based: Links to existing files, no duplication
"""

from typing import List, Optional
from pathlib import Path

from claude_parser import SkillInfo


class SkillDocumenter:
    """
    Document Claude Skills for Codex CLI users.

    Determines the most relevant usage method for each skill type:
    - Functional skills (has Python): Show bash execution examples
    - Prompt-based skills (no Python): Show prompt reference examples
    """

    def document_functional_skill(self, skill: SkillInfo) -> str:
        """
        Document a functional skill (has Python scripts).

        Args:
            skill: SkillInfo with python_files

        Returns:
            Formatted documentation string
        """
        content = []

        # Title
        content.append(f"#### {skill.name}")
        content.append("")

        # Description
        if skill.description:
            # Truncate if too long
            description = skill.description
            if len(description) > 150:
                description = description[:147] + "..."
            content.append(f"**Description**: {description}")
            content.append("")

        # Location
        content.append(f"**Location**: `{skill.location}/`")
        content.append(f"**Documentation**: [{skill.location}/SKILL.md]({skill.skill_md_path})")
        content.append("")

        # Python scripts
        if skill.python_files:
            content.append("**Python Scripts**:")
            for py_file in skill.python_files:
                py_name = Path(py_file).name
                content.append(f"- [{py_name}]({py_file})")
            content.append("")

        # Usage with Codex CLI
        content.append("**Using with Codex CLI**:")
        content.append("")
        content.append("```bash")
        content.append(f"# Execute Python scripts directly")
        content.append(f"cd {skill.location}")

        if skill.python_files:
            # Show first Python file as example
            first_py = Path(skill.python_files[0]).name
            content.append(f"python {first_py} --help  # See usage options")
        else:
            content.append("python script.py --help")

        content.append("")
        content.append("# Or reference in Codex prompt for guidance")
        content.append(f'codex exec -m gpt-5 -s read-only \\')
        content.append(f'  "Using the {skill.name} skill documentation at')
        content.append(f'  {skill.skill_md_path}, help me with [task]"')
        content.append("```")

        return "\n".join(content)

    def document_prompt_skill(self, skill: SkillInfo) -> str:
        """
        Document a prompt-based skill (no Python scripts).

        Args:
            skill: SkillInfo without python_files

        Returns:
            Formatted documentation string
        """
        content = []

        # Title
        content.append(f"#### {skill.name}")
        content.append("")

        # Description
        if skill.description:
            # Truncate if too long
            description = skill.description
            if len(description) > 150:
                description = description[:147] + "..."
            content.append(f"**Description**: {description}")
            content.append("")

        # Location
        content.append(f"**Location**: `{skill.location}/`")
        content.append(f"**Documentation**: [{skill.location}/SKILL.md]({skill.skill_md_path})")
        content.append("")

        # Usage with Codex CLI
        content.append("**Using with Codex CLI**:")
        content.append("")
        content.append("```bash")
        content.append(f"# Reference skill documentation in prompt")
        content.append(f'codex exec -m gpt-5 -s read-only \\')
        content.append(f'  --skip-git-repo-check \\')
        content.append(f'  "Using the {skill.name} skill documentation')
        content.append(f'  at {skill.skill_md_path},')
        content.append(f'  apply these guidelines to [your task]"')
        content.append("```")

        return "\n".join(content)

    def generate_bash_examples(self, skill: SkillInfo) -> List[str]:
        """
        Generate bash command examples for skill.

        Args:
            skill: SkillInfo

        Returns:
            List of bash command strings
        """
        examples = []

        if skill.is_functional and skill.python_files:
            # Functional skill: execute Python
            for py_file in skill.python_files:
                py_name = Path(py_file).name
                cmd = f"cd {skill.location} && python {py_name} --help"
                examples.append(cmd)
        else:
            # Prompt-based: reference in codex
            cmd = (
                f'codex exec -m gpt-5 -s read-only '
                f'"Using {skill.skill_md_path}, [task]"'
            )
            examples.append(cmd)

        return examples

    def generate_prompt_templates(self, skill: SkillInfo) -> List[str]:
        """
        Generate Codex prompt templates referencing skill.

        Args:
            skill: SkillInfo

        Returns:
            List of prompt template strings
        """
        templates = []

        # Template 1: Basic reference
        template1 = (
            f"Using the {skill.name} skill documentation at "
            f"{skill.skill_md_path}, help me with [task description]"
        )
        templates.append(template1)

        # Template 2: Detailed guidance
        template2 = (
            f"I need to [task]. Please reference the {skill.name} skill "
            f"at {skill.skill_md_path} for guidelines and best practices. "
            f"Provide step-by-step instructions."
        )
        templates.append(template2)

        # Template 3: Code generation (if functional)
        if skill.is_functional:
            template3 = (
                f"Generate code similar to the {skill.name} skill's approach. "
                f"Reference the implementation at {skill.location}/ for patterns "
                f"and best practices."
            )
            templates.append(template3)

        return templates

    def create_capability_reference(self, skills: List[SkillInfo]) -> str:
        """
        Create comprehensive capability reference for all skills.

        Args:
            skills: List of SkillInfo objects

        Returns:
            Formatted capability reference string
        """
        content = []

        content.append("# Capabilities Reference")
        content.append("")
        content.append(f"Total Skills: {len(skills)}")
        content.append("")

        # Categorize
        functional = [s for s in skills if s.is_functional]
        prompt_based = [s for s in skills if not s.is_functional]

        content.append(f"## Functional Skills ({len(functional)})")
        content.append("")
        content.append("Execute Python scripts directly:")
        content.append("")

        for skill in functional:
            content.append(f"### {skill.name}")
            content.append(f"Location: `{skill.location}/`")
            content.append(f"Scripts: {len(skill.python_files)}")
            content.append("")

        content.append(f"## Prompt-Based Skills ({len(prompt_based)})")
        content.append("")
        content.append("Reference in Codex prompts:")
        content.append("")

        for skill in prompt_based:
            content.append(f"### {skill.name}")
            content.append(f"Location: `{skill.location}/`")
            content.append("")

        return "\n".join(content)


def main():
    """Demo usage of SkillDocumenter."""
    import argparse
    from claude_parser import ClaudeProjectParser

    parser = argparse.ArgumentParser(description="Document skills for Codex CLI")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root directory (default: current directory)"
    )
    parser.add_argument(
        "--skill-name",
        help="Document specific skill by name"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all skills"
    )

    args = parser.parse_args()

    # Parse project
    claude_parser = ClaudeProjectParser(args.project_root)
    data = claude_parser.parse_all()

    documenter = SkillDocumenter()

    if args.list:
        # List all skills
        print(f"\n📦 Found {len(data['skills'])} skills:\n")
        for skill in data['skills']:
            skill_type = "Functional" if skill.is_functional else "Prompt-based"
            print(f"  {skill.name} ({skill_type})")
            print(f"    Location: {skill.location}")
            if skill.python_files:
                print(f"    Python files: {len(skill.python_files)}")
            print()

    elif args.skill_name:
        # Document specific skill
        skill = next((s for s in data['skills'] if s.name == args.skill_name), None)
        if not skill:
            print(f"❌ Skill '{args.skill_name}' not found")
            return

        if skill.is_functional:
            doc = documenter.document_functional_skill(skill)
        else:
            doc = documenter.document_prompt_skill(skill)

        print("\n" + doc + "\n")

    else:
        # Show capability reference
        reference = documenter.create_capability_reference(data['skills'])
        print(reference)


if __name__ == "__main__":
    main()
