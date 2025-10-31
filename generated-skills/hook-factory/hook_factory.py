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


def main():
    """Main entry point for CLI usage."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Hook Factory - Generate Claude Code hooks from templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
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
    parser.add_argument('--project-root',
                        help='Project root directory (default: auto-detect)')

    args = parser.parse_args()

    factory = HookFactory(project_root=args.project_root)

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
