"""
Slash Command Generator
Generates Claude Code slash command .md files with proper YAML frontmatter.
"""

from typing import Dict, Any, List
import json
import os


class SlashCommandGenerator:
    """Generate custom slash commands for Claude Code."""

    def __init__(self):
        """Initialize generator with presets."""
        self.presets = self._load_presets()

    def _load_presets(self) -> Dict[str, Any]:
        """Load preset commands from presets.json."""
        presets_path = os.path.join(os.path.dirname(__file__), 'presets.json')
        with open(presets_path, 'r') as f:
            return json.load(f)

    def generate_from_preset(self, preset_name: str) -> Dict[str, Any]:
        """
        Generate command from preset.

        Args:
            preset_name: Name of preset (e.g., 'research-business')

        Returns:
            Dict with command_content and metadata
        """
        if preset_name not in self.presets:
            raise ValueError(f"Preset '{preset_name}' not found. Available: {list(self.presets.keys())}")

        preset = self.presets[preset_name]

        # Generate full command content
        command_content = self._create_command_file(
            description=preset['description'],
            argument_hint=preset.get('argument-hint'),
            allowed_tools=preset.get('allowed-tools'),
            model=preset.get('model'),
            command_body=preset['command_body']
        )

        return {
            'command_name': preset['name'],
            'command_content': command_content,
            'supporting_folders': preset.get('supporting_folders', [])
        }

    def generate_custom(self, answers: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate custom command from user answers.

        Args:
            answers: User responses to 5-7 questions

        Returns:
            Dict with command_content and metadata
        """
        # Determine command name from purpose (kebab-case)
        command_name = self._purpose_to_command_name(answers['purpose'])

        # Auto-determine if $ARGUMENTS needed
        needs_args = self._needs_arguments(answers['purpose'])

        # Create argument hint if needed
        argument_hint = self._create_argument_hint(answers) if needs_args else None

        # Generate command body
        command_body = self._create_command_body_from_answers(answers)

        # Generate full command content
        command_content = self._create_command_file(
            description=answers['purpose'],
            argument_hint=argument_hint,
            allowed_tools=answers.get('tools'),
            model=answers.get('model'),
            command_body=command_body
        )

        # Determine supporting folders
        supporting_folders = self._determine_folders(answers)

        return {
            'command_name': command_name,
            'command_content': command_content,
            'supporting_folders': supporting_folders
        }

    def _create_command_file(
        self,
        description: str,
        argument_hint: str = None,
        allowed_tools: str = None,
        model: str = None,
        command_body: str = None
    ) -> str:
        """
        Create complete command .md file content.

        Args:
            description: Command description
            argument_hint: Argument syntax hint
            allowed_tools: Tools the command can use
            model: Specific model to use
            command_body: Main command instructions

        Returns:
            Complete .md file content with YAML frontmatter
        """
        # Build YAML frontmatter
        frontmatter_lines = ['---']
        frontmatter_lines.append(f'description: {description}')

        if argument_hint:
            frontmatter_lines.append(f'argument-hint: {argument_hint}')

        if allowed_tools:
            frontmatter_lines.append(f'allowed-tools: {allowed_tools}')

        if model:
            frontmatter_lines.append(f'model: {model}')

        frontmatter_lines.append('disable-model-invocation: false')
        frontmatter_lines.append('---')

        # Combine frontmatter + body
        frontmatter = '\n'.join(frontmatter_lines)
        full_content = f"{frontmatter}\n\n{command_body}"

        return full_content

    def _purpose_to_command_name(self, purpose: str) -> str:
        """Convert purpose to kebab-case command name."""
        # Simple conversion: lowercase, replace spaces with hyphens
        name = purpose.lower()
        name = name.replace(' ', '-')
        # Remove special characters
        name = ''.join(c for c in name if c.isalnum() or c == '-')
        # Remove multiple hyphens
        while '--' in name:
            name = name.replace('--', '-')
        return name.strip('-')

    def _needs_arguments(self, purpose: str) -> bool:
        """
        Determine if command needs arguments based on purpose.

        Returns True if purpose suggests needing input parameters.
        """
        # Keywords that suggest arguments needed
        arg_indicators = [
            'for', 'analyze', 'research', 'generate', 'create',
            'build', 'translate', 'audit', 'review', 'process'
        ]

        purpose_lower = purpose.lower()
        return any(indicator in purpose_lower for indicator in arg_indicators)

    def _create_argument_hint(self, answers: Dict[str, Any]) -> str:
        """
        Create argument hint based on command purpose.

        Always uses $ARGUMENTS format (never $1, $2, $3).
        """
        # Generic hints based on common patterns
        purpose_lower = answers['purpose'].lower()

        if 'research' in purpose_lower:
            return '[topic] [scope]'
        elif 'translate' in purpose_lower:
            return '[text] [language]'
        elif 'audit' in purpose_lower or 'check' in purpose_lower:
            return '[path] [standard]'
        elif 'generate' in purpose_lower or 'create' in purpose_lower:
            return '[name] [type]'
        elif 'analyze' in purpose_lower:
            return '[target] [analysis-type]'
        else:
            return '[input] [options]'

    def _create_command_body_from_answers(self, answers: Dict[str, Any]) -> str:
        """Generate command body from user answers."""

        # Start with purpose
        body_lines = [f"Execute task: \"$ARGUMENTS\"\n"]

        # Add steps based on output type
        output_type = answers.get('output_type', 'analysis')

        if output_type == 'analysis':
            body_lines.append("1. **Analyze Input**:\n   - Gather relevant data\n   - Identify key patterns\n   - Extract insights\n\n")
            body_lines.append("2. **Generate Analysis**:\n   - Comprehensive findings\n   - Data-driven insights\n   - Recommendations\n\n")

        elif output_type == 'files':
            body_lines.append("1. **Plan Structure**:\n   - Determine file organization\n   - Design architecture\n\n")
            body_lines.append("2. **Generate Files**:\n   - Create necessary files\n   - Add proper formatting\n   - Include documentation\n\n")

        elif output_type == 'action':
            body_lines.append("1. **Execute Action**:\n   - Perform requested task\n   - Monitor progress\n   - Handle errors\n\n")

        else:  # report
            body_lines.append("1. **Gather Information**:\n   - Collect relevant data\n   - Analyze thoroughly\n\n")
            body_lines.append("2. **Generate Report**:\n   - Structured findings\n   - Recommendations\n   - Next steps\n\n")

        # Add agent launching if needed
        if answers.get('launches_agents'):
            agents = answers.get('agent_names', [])
            if agents:
                body_lines.append(f"3. **Launch Agents**:\n")
                for agent in agents:
                    body_lines.append(f"   - Launch {agent} for specialized task\n")
                body_lines.append("\n")

        # Add success criteria
        body_lines.append("**Success Criteria**:\n")
        body_lines.append(f"- {answers['purpose']} completed successfully\n")
        body_lines.append("- Quality standards met\n")
        body_lines.append("- Output validated and ready to use\n")

        return ''.join(body_lines)

    def _determine_folders(self, answers: Dict[str, Any]) -> List[str]:
        """Determine which supporting folders are needed."""
        folders = []

        # Add folders based on command characteristics
        if 'standard' in answers.get('purpose', '').lower() or 'compliance' in answers.get('purpose', '').lower():
            folders.append('standards')

        if 'example' in answers.get('purpose', '').lower() or answers.get('output_type') == 'files':
            folders.append('examples')

        if 'script' in answers.get('purpose', '').lower() or 'bash' in answers.get('tools', '').lower():
            folders.append('scripts')

        return folders
