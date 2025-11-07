#!/usr/bin/env python3
"""
Hook Factory - Main orchestrator for generating Claude Code hooks.

This is the main entry point for the hook-factory skill.
"""

import os
import sys
import json
from pathlib import Path
from typing import Optional

from generator import HookGenerator, HookRequirements, HookPackage, generate_hook_from_request
from validator import HookValidator, ValidationResult


class HookFactory:
    """Main orchestrator for hook generation."""

    def __init__(self, project_root: str = None):
        """
        Initialize Hook Factory.

        Args:
            project_root: Path to project root (defaults to current directory parent)
        """
        if project_root is None:
            # Default to parent of parent directory (assuming we're in generated-skills/hook-factory/)
            script_dir = Path(__file__).resolve().parent
            project_root = script_dir.parent.parent

        self.project_root = Path(project_root)
        self.output_base = self.project_root / 'generated-hooks'
        self.generator = HookGenerator()
        self.validator = HookValidator()

        # Ensure output directory exists
        self.output_base.mkdir(exist_ok=True)

    def create_hook_from_request(self, request: str) -> Optional[dict]:
        """
        Create a hook from natural language request.

        Args:
            request: Natural language description of desired hook

        Returns:
            Dictionary with status and file paths, or None if failed
        """
        print(f"🏭 Hook Factory: Processing request...")
        print(f"   Request: {request}\n")

        # Generate hook package
        package = generate_hook_from_request(request)

        if not package:
            print("❌ Could not determine hook type from request.")
            print("\n💡 Supported hook types:")
            print("   - Auto-format code (keywords: format, prettier, black, rustfmt)")
            print("   - Git auto-add (keywords: git add, auto-add, stage)")
            print("   - Run tests (keywords: test, pytest, jest)")
            print("   - Load context (keywords: load, context, session start)")
            return None

        return self._process_package(package)

    def create_hook_from_template(self, template_name: str, language: str = 'python',
                                    hook_name: str = '', **options) -> Optional[dict]:
        """
        Create a hook from explicit template and language.

        Args:
            template_name: Template key from templates.json
            language: Programming language
            hook_name: Custom hook name (optional)
            **options: Additional options

        Returns:
            Dictionary with status and file paths, or None if failed
        """
        print(f"🏭 Hook Factory: Creating hook from template...")
        print(f"   Template: {template_name}")
        print(f"   Language: {language}\n")

        # Create requirements
        requirements = HookRequirements(
            template_name=template_name,
            language=language,
            hook_name=hook_name,
            additional_options=options
        )

        try:
            # Generate hook
            package = self.generator.generate_hook(requirements)
            return self._process_package(package)

        except ValueError as e:
            print(f"❌ Error: {str(e)}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            return None

    def _process_package(self, package: HookPackage) -> dict:
        """
        Process and validate a generated hook package.

        Args:
            package: Generated HookPackage

        Returns:
            Dictionary with status and file paths
        """
        # Validate hook
        print("🔍 Validating hook configuration...")
        validation = self.validator.validate_hook(package.hook_config)

        if not validation.is_valid:
            print("❌ Hook validation failed:\n")
            for error in validation.errors:
                print(f"   [ERROR] {error.message}")
                if error.fix_suggestion:
                    print(f"           Fix: {error.fix_suggestion}")
            return None

        if validation.warnings:
            print("⚠️  Warnings detected:")
            for warning in validation.warnings:
                print(f"   [WARN] {warning.message}")
                if warning.fix_suggestion:
                    print(f"          Fix: {warning.fix_suggestion}")
            print()

        if not validation.is_safe:
            print("🚫 Hook contains potentially unsafe operations!")
            print("   Review the hook carefully before installing.")
            print()

        # Save files
        print("💾 Saving hook files...")
        result = self._save_package(package)

        # Display success
        print("\n✅ Hook generated successfully!\n")
        print(f"📁 Hook Name: {package.hook_name}")
        print(f"📂 Location: {result['output_dir']}")
        print(f"\n📄 Files created:")
        for file_type, path in result['files'].items():
            print(f"   - {file_type}: {path}")

        print("\n📋 Next Steps:")
        print(f"   1. Review the generated files in: {result['output_dir']}")
        print(f"   2. Read the README.md for installation instructions")
        print(f"   3. Copy hook.json configuration to your Claude Code settings")
        print(f"\n💡 To install manually:")
        print(f"   Open .claude/settings.json and add the hook configuration")

        return result

    def _save_package(self, package: HookPackage) -> dict:
        """
        Save hook package to disk.

        Args:
            package: HookPackage to save

        Returns:
            Dictionary with file paths
        """
        # Validate hook_name for path traversal
        hook_name = self._sanitize_hook_name(package.hook_name)

        # Create output directory
        output_dir = self.output_base / hook_name

        # Validate path is within output_base (prevent path traversal)
        try:
            output_dir = output_dir.resolve()
            output_base_resolved = self.output_base.resolve()
            if not str(output_dir).startswith(str(output_base_resolved)):
                raise ValueError(f"Invalid hook name: path traversal detected in '{package.hook_name}'")
        except (ValueError, OSError) as e:
            raise ValueError(f"Invalid hook name: {str(e)}")

        output_dir.mkdir(parents=True, exist_ok=True)

        files = {}

        # Save hook.json
        hook_json_path = output_dir / 'hook.json'
        with open(hook_json_path, 'w') as f:
            f.write(package.hook_json)
        files['hook.json'] = str(hook_json_path)

        # Save README.md
        readme_path = output_dir / 'README.md'
        with open(readme_path, 'w') as f:
            f.write(package.readme_md)
        files['README.md'] = str(readme_path)

        return {
            'output_dir': str(output_dir),
            'hook_name': package.hook_name,
            'files': files
        }

    def _sanitize_hook_name(self, hook_name: str) -> str:
        """
        Sanitize hook name to prevent path traversal attacks.

        Args:
            hook_name: Raw hook name from user input

        Returns:
            Sanitized hook name safe for filesystem

        Raises:
            ValueError: If hook name contains invalid characters
        """
        import re

        # Check for path traversal attempts
        if '..' in hook_name:
            raise ValueError(f"Invalid hook name: '..' not allowed in '{hook_name}'")

        # Check for absolute paths
        if hook_name.startswith('/') or (len(hook_name) > 1 and hook_name[1] == ':'):
            raise ValueError(f"Invalid hook name: absolute paths not allowed in '{hook_name}'")

        # Only allow alphanumeric, hyphens, underscores
        if not re.match(r'^[a-zA-Z0-9_-]+$', hook_name):
            raise ValueError(f"Invalid hook name: only alphanumeric, hyphens, and underscores allowed in '{hook_name}'")

        return hook_name

    def list_templates(self) -> None:
        """List all available templates."""
        print("📚 Available Hook Templates:\n")

        templates = self.generator.list_templates()

        for template in templates:
            print(f"🔹 {template['key']}")
            print(f"   Name: {template['name']}")
            print(f"   Description: {template['description']}")
            print(f"   Event Type: {template['event_type']}")
            print(f"   Complexity: {template['complexity']}")
            if template['use_cases']:
                print(f"   Use Cases:")
                for use_case in template['use_cases']:
                    print(f"      - {use_case}")
            print()


def interactive_mode(factory: HookFactory) -> int:
    """
    Interactive mode with guided 7-question flow.

    Args:
        factory: HookFactory instance

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    print("\n" + "=" * 70)
    print("🎯 Hook Factory - Interactive Mode")
    print("=" * 70)
    print("\nThis wizard will guide you through creating a custom hook.")
    print("You can press Ctrl+C at any time to cancel.\n")

    try:
        # Q1: Event Type
        event_type = _ask_event_type()

        # Q2: Programming Language
        language = _ask_language(event_type)

        # Q3: Tool Matcher
        matcher = _ask_matcher(event_type)

        # Q4: Command to Run
        command = _ask_command(event_type, language)

        # Q5: Timeout
        timeout = _ask_timeout(event_type)

        # Q6: Installation Level
        level = _ask_installation_level()

        # Q7: Auto-Install
        auto_install = _ask_auto_install()

        # Summary
        print("\n" + "=" * 70)
        print("📋 Hook Configuration Summary")
        print("=" * 70)
        print(f"  Event Type: {event_type}")
        print(f"  Language: {language}")
        print(f"  Matcher: {matcher}")
        print(f"  Command: {command[:60]}..." if len(command) > 60 else f"  Command: {command}")
        print(f"  Timeout: {timeout}s")
        print(f"  Level: {level}")
        print(f"  Auto-Install: {'Yes' if auto_install else 'No'}")
        print("=" * 70)

        confirm = input("\n✅ Generate this hook? (y/n): ").strip().lower()
        if confirm != 'y':
            print("❌ Hook generation cancelled.")
            return 1

        # Generate hook name from event and language
        hook_name = f"{event_type.lower().replace('tooluse', 'tool_use')}-{language.lower()}"

        # Create HookRequirements
        requirements = HookRequirements(
            template_name=_get_template_for_event(event_type),
            language=language,
            hook_name=hook_name,
            additional_options={
                'matcher': matcher,
                'command': command,
                'timeout': timeout
            }
        )

        # Generate hook
        try:
            package = factory.generator.generate_hook(requirements)
            result = factory._process_package(package)

            if not result:
                print("❌ Hook generation failed.")
                return 1

            # Auto-install if requested
            if auto_install:
                print("\n🔧 Installing hook...")
                try:
                    from installer import HookInstaller
                    installer = HookInstaller()
                    hook_path = result['output_dir']

                    success = installer.install_hook(hook_path, level=level)
                    if success:
                        print("✅ Hook installed successfully!")
                        print(f"📍 Location: {level} level")
                        print("\nℹ️  Restart Claude Code to activate the hook")
                    else:
                        print("⚠️  Hook generation succeeded but installation failed.")
                        print(f"   You can manually install from: {hook_path}")

                except ImportError:
                    print("⚠️  installer.py not found - skipping auto-install")
                    print(f"   You can manually install from: {result['output_dir']}")
                except Exception as e:
                    print(f"⚠️  Auto-install failed: {e}")
                    print(f"   You can manually install from: {result['output_dir']}")

            return 0

        except Exception as e:
            print(f"❌ Error generating hook: {e}")
            return 1

    except KeyboardInterrupt:
        print("\n\n❌ Hook generation cancelled by user.")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return 1


def _ask_event_type() -> str:
    """Ask user for event type."""
    print("\n" + "-" * 70)
    print("❓ Q1: Event Type")
    print("-" * 70)
    print("\nWhat event should trigger this hook?\n")
    print("  1. PostToolUse - After using a tool (Edit, Write, Bash)")
    print("  2. SubagentStop - When an agent completes")
    print("  3. SessionStart - At session startup")
    print("  4. PreToolUse - Before using a tool (validation)")
    print("  5. UserPromptSubmit - Before processing user prompt")
    print("  6. Stop - At session end (cleanup)")
    print("  7. PrePush - Before git push (validation)")

    event_map = {
        '1': 'PostToolUse',
        '2': 'SubagentStop',
        '3': 'SessionStart',
        '4': 'PreToolUse',
        '5': 'UserPromptSubmit',
        '6': 'Stop',
        '7': 'PrePush'
    }

    while True:
        choice = input("\nYour choice (1-7): ").strip()
        if choice in event_map:
            return event_map[choice]
        print("❌ Invalid choice. Please enter a number between 1 and 7.")


def _ask_language(event_type: str) -> str:
    """Ask user for programming language with smart defaults."""
    print("\n" + "-" * 70)
    print("❓ Q2: Programming Language")
    print("-" * 70)
    print("\nWhat programming language? (for formatting/testing templates)\n")
    print("  1. Python")
    print("  2. JavaScript")
    print("  3. TypeScript")
    print("  4. Rust")
    print("  5. Go")
    print("  6. N/A (not language-specific)")

    # Smart default
    default = '1' if event_type in ['PostToolUse', 'SubagentStop'] else '6'
    default_name = {
        '1': 'Python', '2': 'JavaScript', '3': 'TypeScript',
        '4': 'Rust', '5': 'Go', '6': 'N/A'
    }[default]

    print(f"\n💡 Suggested: {default_name}")

    language_map = {
        '1': 'python',
        '2': 'javascript',
        '3': 'typescript',
        '4': 'rust',
        '5': 'go',
        '6': 'generic'
    }

    while True:
        choice = input(f"\nYour choice (1-6, default={default}): ").strip() or default
        if choice in language_map:
            return language_map[choice]
        print("❌ Invalid choice. Please enter a number between 1 and 6.")


def _ask_matcher(event_type: str) -> str:
    """Ask user for tool matcher."""
    print("\n" + "-" * 70)
    print("❓ Q3: Tool Matcher")
    print("-" * 70)
    print("\nWhat tools should trigger this hook?\n")
    print("Examples:")
    print('  "Edit,Write" - Trigger on Edit or Write')
    print('  "Bash" - Trigger on Bash only')
    print('  "*.py" - Trigger on Python files')
    print('  "*" - Trigger on all tools (not recommended for PreToolUse)')

    # Smart defaults
    if event_type == 'PostToolUse':
        default = "Edit,Write"
    elif event_type == 'PreToolUse':
        default = "Write,Edit"
    elif event_type == 'SubagentStop':
        default = "*"
    else:
        default = "{}"  # Empty matcher

    print(f"\n💡 Suggested: {default}")

    while True:
        answer = input(f"\nYour answer (default={default}): ").strip() or default

        # Validation
        if event_type == 'PreToolUse' and answer == '*':
            print("⚠️  Warning: PreToolUse with '*' matcher is not recommended (too broad)")
            confirm = input("   Continue anyway? (y/n): ").strip().lower()
            if confirm != 'y':
                continue

        return answer


def _ask_command(event_type: str, language: str) -> str:
    """Ask user for command to run."""
    print("\n" + "-" * 70)
    print("❓ Q4: Command to Run")
    print("-" * 70)
    print("\nWhat command should the hook execute?\n")
    print("Examples:")
    print('  "black {file_path}" (Python formatting)')
    print('  "git add {file_path}" (Git auto-add)')
    print('  "pytest tests/" (Run tests)')
    print('  "echo Session started" (Simple notification)')

    # Smart defaults based on event + language
    defaults = {
        ('PostToolUse', 'python'): 'black {file_path}',
        ('PostToolUse', 'javascript'): 'prettier --write {file_path}',
        ('PostToolUse', 'typescript'): 'prettier --write {file_path}',
        ('SubagentStop', 'python'): 'pytest tests/',
        ('SessionStart', 'generic'): 'echo "🚀 Session started at $(date)"',
        ('Stop', 'generic'): 'echo "👋 Session ended at $(date)"',
        ('PrePush', 'python'): 'pytest tests/ && echo "✅ Tests passed"'
    }

    default = defaults.get((event_type, language), 'echo "Hook triggered"')
    print(f"\n💡 Suggested: {default}")

    while True:
        answer = input(f"\nYour command (default={default}): ").strip() or default

        # Basic validation
        if not answer:
            print("❌ Command cannot be empty.")
            continue

        # Warn about dangerous commands
        dangerous = ['rm -rf', 'dd if=', '> /dev/', 'chmod -R 777']
        if any(d in answer for d in dangerous):
            print("⚠️  Warning: This command may be dangerous!")
            confirm = input("   Continue anyway? (y/n): ").strip().lower()
            if confirm != 'y':
                continue

        return answer


def _ask_timeout(event_type: str) -> int:
    """Ask user for timeout with smart defaults."""
    print("\n" + "-" * 70)
    print("❓ Q5: Timeout")
    print("-" * 70)
    print("\nMaximum execution time?\n")
    print("  1. 5s (quick validation)")
    print("  2. 10s (formatting)")
    print("  3. 30s (testing, notifications)")
    print("  4. 60s (comprehensive tests)")
    print("  5. 120s (slow tests, security scans)")

    # Smart defaults based on event type
    defaults = {
        'PreToolUse': '1',      # 5s - blocking
        'UserPromptSubmit': '1', # 5s - blocking
        'PostToolUse': '2',      # 10s - formatting
        'SessionStart': '3',     # 30s - setup
        'SubagentStop': '4',     # 60s - tests
        'Stop': '3',             # 30s - cleanup
        'PrePush': '5'           # 120s - comprehensive
    }

    default = defaults.get(event_type, '3')
    timeout_map = {'1': 5, '2': 10, '3': 30, '4': 60, '5': 120}

    print(f"\n💡 Suggested: {timeout_map[default]}s (choice {default})")

    while True:
        choice = input(f"\nYour choice (1-5, default={default}): ").strip() or default
        if choice in timeout_map:
            return timeout_map[choice]
        print("❌ Invalid choice. Please enter a number between 1 and 5.")


def _ask_installation_level() -> str:
    """Ask user for installation level."""
    print("\n" + "-" * 70)
    print("❓ Q6: Installation Level")
    print("-" * 70)
    print("\nWhere should this hook be installed?\n")
    print("  1. User (~/.claude/settings.json) - All projects")
    print("  2. Project (.claude/settings.json) - This project only")

    print("\n💡 Suggested: User (safer, applies to all projects)")

    level_map = {'1': 'user', '2': 'project'}

    while True:
        choice = input("\nYour choice (1-2, default=1): ").strip() or '1'
        if choice in level_map:
            return level_map[choice]
        print("❌ Invalid choice. Please enter 1 or 2.")


def _ask_auto_install() -> bool:
    """Ask user if auto-install is desired."""
    print("\n" + "-" * 70)
    print("❓ Q7: Auto-Install")
    print("-" * 70)
    print("\nInstall the hook automatically after generation?")
    print("(You can also install manually later)\n")

    while True:
        choice = input("Auto-install? (y/n, default=n): ").strip().lower() or 'n'
        if choice in ['y', 'n', 'yes', 'no']:
            return choice in ['y', 'yes']
        print("❌ Invalid choice. Please enter 'y' or 'n'.")


def _get_template_for_event(event_type: str) -> str:
    """Get appropriate template name for event type."""
    template_map = {
        'PostToolUse': 'post_tool_use_format',
        'SubagentStop': 'subagent_stop_test_runner',
        'SessionStart': 'session_start_load_context',
        'PreToolUse': 'pre_tool_use_validation',
        'UserPromptSubmit': 'user_prompt_submit_preprocessor',
        'Stop': 'stop_session_cleanup',
        'PrePush': 'pre_push_validation'
    }
    return template_map.get(event_type, 'post_tool_use_format')


def main():
    """Main entry point for CLI usage."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Hook Factory - Generate Claude Code hooks from templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (guided 7-question flow)
  python hook_factory.py -i

  # Generate from natural language
  python hook_factory.py -r "auto-format Python files after editing"
  python hook_factory.py -r "run tests when agent completes"
  python hook_factory.py -r "git add files automatically"

  # Generate from template
  python hook_factory.py -t post_tool_use_format -l python
  python hook_factory.py -t subagent_stop_test_runner -l javascript

  # List available templates
  python hook_factory.py --list
        """
    )

    parser.add_argument('-r', '--request',
                        help='Natural language request for hook')
    parser.add_argument('-t', '--template',
                        help='Template name to use')
    parser.add_argument('-l', '--language',
                        default='python',
                        help='Programming language (default: python)')
    parser.add_argument('-n', '--name',
                        help='Custom hook name')
    parser.add_argument('--list',
                        action='store_true',
                        help='List available templates')
    parser.add_argument('-i', '--interactive',
                        action='store_true',
                        help='Interactive mode with guided questions')
    parser.add_argument('--project-root',
                        help='Project root directory (default: auto-detect)')

    args = parser.parse_args()

    factory = HookFactory(project_root=args.project_root)

    # Interactive mode
    if args.interactive:
        return interactive_mode(factory)

    # List templates
    if args.list:
        factory.list_templates()
        return 0

    # Generate from request
    if args.request:
        result = factory.create_hook_from_request(args.request)
        return 0 if result else 1

    # Generate from template
    if args.template:
        result = factory.create_hook_from_template(
            template_name=args.template,
            language=args.language,
            hook_name=args.name or ''
        )
        return 0 if result else 1

    # No action specified
    parser.print_help()
    return 1


if __name__ == '__main__':
    sys.exit(main())
