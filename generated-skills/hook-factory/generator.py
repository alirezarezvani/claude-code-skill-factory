"""
Hook Generator - Template substitution and hook creation for Claude Code hooks.

Generates production-ready hook configurations from templates.
"""

import json
import os
import re
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class HookRequirements:
    """User requirements for hook generation."""
    template_name: str
    language: str = "python"
    hook_name: str = ""
    description: str = ""
    tool: str = ""
    file_patterns: List[str] = None
    additional_options: Dict = None

    def __post_init__(self):
        if self.file_patterns is None:
            self.file_patterns = []
        if self.additional_options is None:
            self.additional_options = {}


@dataclass
class HookPackage:
    """Generated hook package with all files."""
    hook_config: Dict
    hook_json: str
    readme_md: str
    output_dir: str
    hook_name: str


class HookGenerator:
    """Generates Claude Code hooks from templates."""

    def __init__(self, templates_path: str = None):
        """
        Initialize hook generator.

        Args:
            templates_path: Path to templates.json file
        """
        if templates_path is None:
            # Default to templates.json in same directory
            script_dir = os.path.dirname(os.path.abspath(__file__))
            templates_path = os.path.join(script_dir, 'templates.json')

        self.templates_path = templates_path
        self.templates = self._load_templates()

    def _load_templates(self) -> Dict:
        """Load hook templates from JSON file."""
        try:
            with open(self.templates_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Templates file not found: {self.templates_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in templates file: {str(e)}")

    def list_templates(self) -> List[Dict]:
        """List available templates with metadata."""
        template_list = []

        for key, template in self.templates.items():
            metadata = template.get('metadata', {})
            template_list.append({
                'key': key,
                'name': metadata.get('name', key),
                'description': metadata.get('description', ''),
                'use_cases': metadata.get('use_cases', []),
                'complexity': metadata.get('complexity', 'unknown'),
                'event_type': metadata.get('event_type', 'unknown')
            })

        return template_list

    def generate_hook(self, requirements: HookRequirements) -> HookPackage:
        """
        Generate a complete hook package from requirements.

        Args:
            requirements: HookRequirements object

        Returns:
            HookPackage with generated files

        Raises:
            ValueError: If template not found or requirements invalid
        """
        # Validate template exists
        if requirements.template_name not in self.templates:
            raise ValueError(f"Template not found: {requirements.template_name}")

        template = self.templates[requirements.template_name]

        # Generate hook name if not provided
        if not requirements.hook_name:
            requirements.hook_name = self._generate_hook_name(
                template['metadata']['name'],
                requirements.language
            )

        # Perform template substitution
        hook_config = self._substitute_template(template, requirements)

        # Get event type from template metadata
        event_type = template['metadata'].get('event_type', 'PostToolUse')

        # Wrap hook config with event type for installer compatibility
        wrapped_config = {
            event_type: [hook_config]
        }

        # Add metadata at root level (for reference, not used by installer)
        wrapped_config['_metadata'] = {
            'generated_by': 'hook-factory',
            'generated_at': datetime.utcnow().isoformat() + 'Z',
            'template': requirements.template_name,
            'language': requirements.language,
            'hook_name': requirements.hook_name,
            'event_type': event_type
        }

        # Generate JSON string
        hook_json = json.dumps(wrapped_config, indent=2)

        # Generate README
        readme_md = self._generate_readme(template, requirements, hook_config)

        # Determine output directory
        output_dir = os.path.join('generated-hooks', requirements.hook_name)

        return HookPackage(
            hook_config=hook_config,  # Raw format for validation
            hook_json=hook_json,  # Wrapped format saved to file
            readme_md=readme_md,
            output_dir=output_dir,
            hook_name=requirements.hook_name
        )

    def _substitute_template(self, template: Dict, requirements: HookRequirements) -> Dict:
        """
        Substitute template variables with actual values.

        Args:
            template: Template dictionary
            requirements: User requirements

        Returns:
            Substituted hook configuration
        """
        template_config = template['template']
        variables = template.get('variables', {})

        # Start with template structure
        hook_config = {
            'matcher': template_config.get('matcher', {}),
            'hooks': []
        }

        # Process each hook in template
        for hook in template_config.get('hooks', []):
            command = hook.get('command', '')

            # Substitute variables
            command = self._substitute_variables(command, variables, requirements)

            hook_config['hooks'].append({
                'type': hook.get('type', 'command'),
                'command': command,
                'timeout': hook.get('timeout', 60)
            })

        return hook_config

    def _substitute_variables(self, command: str, variables: Dict, requirements: HookRequirements) -> str:
        """
        Substitute template variables in command string.

        Args:
            command: Command template string
            variables: Variable definitions
            requirements: User requirements

        Returns:
            Substituted command string
        """
        # Find all {{VARIABLE}} placeholders
        placeholders = re.findall(r'\{\{(\w+)\}\}', command)

        for placeholder in placeholders:
            if placeholder not in variables:
                continue

            var_def = variables[placeholder]

            # Get value based on variable type
            if 'options' in var_def:
                # Language-specific option
                value = self._get_language_option(var_def, requirements.language)
            elif 'patterns' in var_def:
                # Language-specific pattern
                value = self._get_language_pattern(var_def, requirements.language)
            else:
                # Default value or from requirements
                value = var_def.get('default', '')

            # Replace placeholder
            command = command.replace(f'{{{{{placeholder}}}}}', str(value))

        return command

    def _get_language_option(self, var_def: Dict, language: str) -> str:
        """Get language-specific option value."""
        options = var_def.get('options', {})

        if language in options:
            value = options[language]
            # If value is a list, convert to JSON array string
            if isinstance(value, list):
                return json.dumps(value)
            return value

        # Fallback to default
        return var_def.get('default', '')

    def _get_language_pattern(self, var_def: Dict, language: str) -> str:
        """Get language-specific pattern."""
        patterns = var_def.get('patterns', {})

        if language in patterns:
            return patterns[language]

        # Fallback to first pattern
        if patterns:
            return list(patterns.values())[0]

        return ''

    def _generate_hook_name(self, template_name: str, language: str) -> str:
        """
        Generate a hook name from template and language.

        Args:
            template_name: Template name
            language: Programming language

        Returns:
            Hook name in kebab-case (sanitized for filesystem safety)
        """
        # Convert to lowercase and replace spaces with hyphens
        name = template_name.lower().replace(' ', '-')

        # Remove special characters (only keep alphanumeric and hyphens)
        name = re.sub(r'[^a-z0-9-]', '', name)

        # Add language if not already in name
        if language and language not in name:
            name = f"{name}-{language}"

        # Ensure no path traversal sequences
        name = name.replace('..', '').strip('/')

        # Validate final name is safe
        if not re.match(r'^[a-z0-9-]+$', name):
            raise ValueError(f"Generated hook name '{name}' contains invalid characters")

        return name

    def _generate_readme(self, template: Dict, requirements: HookRequirements, hook_config: Dict) -> str:
        """
        Generate README.md for the hook.

        Args:
            template: Template dictionary
            requirements: User requirements
            hook_config: Generated hook configuration

        Returns:
            README markdown content
        """
        metadata = template.get('metadata', {})

        readme = f"""# {requirements.hook_name}

## Overview
{metadata.get('description', 'Claude Code hook')}

**Event Type:** `{metadata.get('event_type', 'Unknown')}`
**Complexity:** {metadata.get('complexity', 'Unknown')}
**Language:** {requirements.language}

## How It Works
{metadata.get('timing', 'Triggers based on configured event type.')}

{self._generate_workflow_description(hook_config)}

## Use Cases
"""

        for use_case in metadata.get('use_cases', []):
            readme += f"- {use_case}\n"

        readme += f"""

## Prerequisites
{self._generate_prerequisites(requirements.language, hook_config)}

## Installation

### Manual Installation

1. Open your Claude Code settings file:
   - **Project-level:** `.claude/settings.json`
   - **User-level:** `~/.claude/settings.json`

2. Add this hook configuration to the `hooks` array:

```json
{{
  "hooks": {{
    "{metadata.get('event_type', 'PostToolUse')}": [
      {json.dumps(hook_config, indent=6)}
    ]
  }}
}}
```

3. Save the file and restart Claude Code.

### Automated Installation (Future)
Installation script coming soon.

## Configuration

### Customize Behavior
You can modify the hook by editing `hook.json`:

{self._generate_customization_guide(template, requirements)}

## Safety Notes
{metadata.get('safety_notes', 'This hook uses safe practices.')}

**Safety Features:**
- ✅ Tool detection prevents errors if dependencies missing
- ✅ Silent failure mode (`|| exit 0`) never interrupts workflow
- ✅ Appropriate timeout settings
- ✅ No destructive operations

## Troubleshooting

### Hook Not Triggering
1. Check that the event type matches your use case
2. Verify file patterns in matcher (if applicable)
3. Check Claude Code logs: `~/.claude/logs/`

### Command Errors
1. Verify required tools are installed
2. Test command manually in terminal
3. Check timeout settings

## Advanced

### Combining with Other Hooks
You can combine this hook with others by adding them to the same event type array.

### Custom Modifications
{self._generate_advanced_tips(requirements.language)}

---
**Generated by hook-factory** | {datetime.utcnow().strftime('%Y-%m-%d')}
**Template:** {requirements.template_name}
**Version:** 1.0
"""

        return readme

    def _generate_workflow_description(self, hook_config: Dict) -> str:
        """Generate workflow description from hook config."""
        steps = [
            "1. Claude Code detects the configured event",
            "2. Hook matcher checks if conditions are met",
            "3. Hook command executes with safety wrappers",
            "4. Result is processed (silent failure on errors)"
        ]

        return "\n".join(steps)

    def _generate_prerequisites(self, language: str, hook_config: Dict) -> str:
        """Generate prerequisites list."""
        prereqs = []

        # Language-specific tools
        tool_map = {
            'python': ['Python 3.6+', 'black (pip install black)'],
            'javascript': ['Node.js 14+', 'prettier (npm install -g prettier)'],
            'typescript': ['Node.js 14+', 'prettier (npm install -g prettier)'],
            'rust': ['Rust 1.50+', 'rustfmt (included with Rust)'],
            'go': ['Go 1.16+', 'gofmt (included with Go)']
        }

        if language in tool_map:
            prereqs.extend(tool_map[language])
        else:
            prereqs.append(f"{language} development environment")

        # Git prerequisite if needed
        command_str = json.dumps(hook_config)
        if 'git' in command_str.lower():
            prereqs.append('Git')

        return "\n".join(f"- {p}" for p in prereqs)

    def _generate_customization_guide(self, template: Dict, requirements: HookRequirements) -> str:
        """Generate customization guide."""
        variables = template.get('variables', {})

        if not variables:
            return "No customization options available."

        guide = "**Available Customizations:**\n\n"

        for var_name, var_def in variables.items():
            guide += f"**{var_name}:** {var_def.get('description', 'No description')}\n"

            if 'options' in var_def:
                guide += "- Options: " + ", ".join(var_def['options'].keys()) + "\n"

            guide += "\n"

        return guide

    def _generate_advanced_tips(self, language: str) -> str:
        """Generate advanced tips section."""
        tips = {
            'python': "- Combine with `isort` for import sorting\n- Add `mypy` for type checking\n- Configure black in `pyproject.toml`",
            'javascript': "- Add ESLint integration\n- Configure prettier in `.prettierrc`\n- Combine with git pre-commit hooks",
            'typescript': "- Add TSLint/ESLint integration\n- Configure prettier in `.prettierrc`\n- Enable strict mode type checking",
            'rust': "- Combine with `cargo clippy` for linting\n- Use `cargo fmt --check` in CI\n- Configure in `rustfmt.toml`",
            'go': "- Combine with `golint` or `staticcheck`\n- Use `gofmt -s` for simplification\n- Add `go vet` for static analysis"
        }

        return tips.get(language, "- Customize command parameters\n- Add conditional logic\n- Combine with other tools")


def generate_hook_from_request(request: str) -> Optional[HookPackage]:
    """
    Generate hook from natural language request (simple keyword matching).

    Args:
        request: Natural language request

    Returns:
        HookPackage or None if no match
    """
    generator = HookGenerator()

    # Simple keyword matching
    request_lower = request.lower()

    # Detect template
    template_name = None
    if any(kw in request_lower for kw in ['format', 'prettier', 'black', 'rustfmt']):
        template_name = 'post_tool_use_format'
    elif any(kw in request_lower for kw in ['git add', 'auto-add', 'stage', 'git stage']):
        template_name = 'post_tool_use_git_add'
    elif any(kw in request_lower for kw in ['test', 'pytest', 'jest', 'run tests']):
        template_name = 'subagent_stop_test_runner'
    elif any(kw in request_lower for kw in ['load', 'context', 'session start', 'startup']):
        template_name = 'session_start_context_loader'

    if not template_name:
        return None

    # Detect language
    language = 'python'  # default
    if any(kw in request_lower for kw in ['python', 'py', '.py']):
        language = 'python'
    elif any(kw in request_lower for kw in ['javascript', 'js', '.js']):
        language = 'javascript'
    elif any(kw in request_lower for kw in ['typescript', 'ts', '.ts']):
        language = 'typescript'
    elif any(kw in request_lower for kw in ['rust', 'rs', '.rs']):
        language = 'rust'
    elif any(kw in request_lower for kw in ['go', 'golang', '.go']):
        language = 'go'

    # Create requirements
    requirements = HookRequirements(
        template_name=template_name,
        language=language
    )

    # Generate hook
    return generator.generate_hook(requirements)


if __name__ == '__main__':
    # Example usage
    import sys

    if len(sys.argv) < 2:
        print("Usage: python generator.py <template_name> <language>")
        print("\nAvailable templates:")
        gen = HookGenerator()
        for template in gen.list_templates():
            print(f"  - {template['key']}: {template['name']}")
        sys.exit(1)

    template_name = sys.argv[1]
    language = sys.argv[2] if len(sys.argv) > 2 else 'python'

    gen = HookGenerator()
    requirements = HookRequirements(
        template_name=template_name,
        language=language
    )

    package = gen.generate_hook(requirements)

    print(f"Generated hook: {package.hook_name}")
    print(f"Output directory: {package.output_dir}")
    print("\n--- hook.json ---")
    print(package.hook_json)
