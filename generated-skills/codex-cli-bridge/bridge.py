#!/usr/bin/env python3
"""
Codex CLI Bridge - Main Orchestrator

Coordinates all components to generate AGENTS.md from Claude Code projects.

Usage:
    python bridge.py                    # Generate AGENTS.md for current directory
    python bridge.py --project /path    # Generate for specific project
    python bridge.py --validate         # Validate environment only
"""

import sys
import argparse
from pathlib import Path
from typing import Optional

from safety_mechanism import SafetyMechanism
from project_analyzer import ProjectAnalyzer
from agents_md_generator import AgentsMdGenerator


class CodexCliBridge:
    """
    Main orchestrator for Codex CLI Bridge skill.

    Coordinates:
    1. Safety validation (Codex CLI + CLAUDE.md checks)
    2. Project analysis (parse CLAUDE.md, skills, agents)
    3. AGENTS.md generation (template-based, reference approach)
    """

    def __init__(self, project_root: str, auto_init: bool = True):
        """
        Initialize bridge.

        Args:
            project_root: Path to project root directory
            auto_init: Auto-run /init if CLAUDE.md missing (default: True)
        """
        self.project_root = Path(project_root).resolve()
        self.auto_init = auto_init

        # Components
        self.safety = SafetyMechanism(str(self.project_root))
        self.analyzer: Optional[ProjectAnalyzer] = None
        self.generator: Optional[AgentsMdGenerator] = None

    def run(self) -> bool:
        """
        Execute complete AGENTS.md generation workflow.

        Returns:
            True if successful, False otherwise
        """
        print("=" * 64)
        print("CODEX CLI BRIDGE - AGENTS.MD GENERATOR")
        print("=" * 64)
        print()

        # Step 1: Safety validation
        print("STEP 1: Environment Validation")
        print("-" * 64)
        success, message = self.safety.validate_all(auto_init=self.auto_init)

        if not success:
            print()
            print("=" * 64)
            print("❌ VALIDATION FAILED")
            print("=" * 64)
            print(f"\nError: {message}")
            print("\nPlease fix the issues above and try again.")
            return False

        print()

        # Step 2: Project analysis
        print("STEP 2: Project Analysis")
        print("-" * 64)
        self.analyzer = ProjectAnalyzer(str(self.project_root))
        analysis = self.analyzer.analyze()
        print()

        # Step 3: AGENTS.md generation
        print("STEP 3: AGENTS.md Generation")
        print("-" * 64)
        self.generator = AgentsMdGenerator(str(self.project_root))

        # Convert analysis dict values to objects
        from project_analyzer import ProjectMetadata, ProjectStructure

        # Reconstruct metadata and structure from dicts
        metadata_dict = analysis["metadata"]
        structure_dict = analysis["structure"]

        metadata = ProjectMetadata(**metadata_dict)
        structure = ProjectStructure(**structure_dict)

        agents_md_content = self.generator.generate(
            metadata=metadata,
            structure=structure,
            skills=analysis["parsed_data"]["skills"],
            agents=analysis["parsed_data"]["agents"],
            claude_md_sections=analysis["parsed_data"]["claude_md_sections"],
            mcp_servers=analysis["parsed_data"].get("mcp_servers", [])
        )
        print()

        # Step 4: Write AGENTS.md
        print("STEP 4: Writing AGENTS.md")
        print("-" * 64)
        agents_md_path = self.project_root / "AGENTS.md"

        try:
            with open(agents_md_path, "w", encoding="utf-8") as f:
                f.write(agents_md_content)

            print(f"   ✅ Written to: {agents_md_path}")
            print()

            # Show summary
            print("=" * 64)
            print("✅ SUCCESS - AGENTS.MD GENERATED")
            print("=" * 64)
            print()
            print(f"📄 Output: {agents_md_path}")
            print(f"📊 Skills documented: {len(analysis['parsed_data']['skills'])}")
            print(f"🤖 Agents documented: {len(analysis['parsed_data']['agents'])}")
            print()
            print("Next steps:")
            print("  1. Review AGENTS.md")
            print("  2. Test with Codex CLI")
            print("  3. Share with team (works in both Claude Code and Codex CLI)")
            print()

            return True

        except Exception as e:
            print(f"   ❌ Failed to write AGENTS.md: {e}")
            print()
            print("=" * 64)
            print("❌ GENERATION FAILED")
            print("=" * 64)
            return False

    def validate_only(self) -> bool:
        """
        Run validation checks only (no generation).

        Returns:
            True if validation passed, False otherwise
        """
        print("=" * 64)
        print("CODEX CLI BRIDGE - VALIDATION ONLY")
        print("=" * 64)
        print()

        success, message = self.safety.validate_all(auto_init=self.auto_init)

        print()
        print("=" * 64)
        if success:
            print("✅ VALIDATION PASSED")
            print("=" * 64)
            print()
            print("Environment is ready for AGENTS.md generation.")
            print()
            print("Run without --validate to generate AGENTS.md:")
            print(f"  python bridge.py --project {self.project_root}")
        else:
            print("❌ VALIDATION FAILED")
            print("=" * 64)
            print(f"\nError: {message}")

        print()
        return success

    def get_status(self) -> dict:
        """
        Get current status report.

        Returns:
            Status dictionary
        """
        return self.safety.get_status_report()


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Codex CLI Bridge - Generate AGENTS.md from CLAUDE.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate AGENTS.md for current directory
  python bridge.py

  # Generate for specific project
  python bridge.py --project /path/to/project

  # Validate environment only (no generation)
  python bridge.py --validate

  # Don't auto-run /init if CLAUDE.md missing
  python bridge.py --no-auto-init

  # Show status report
  python bridge.py --status
        """
    )

    parser.add_argument(
        "--project",
        default=".",
        help="Project root directory (default: current directory)"
    )

    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate environment only (don't generate AGENTS.md)"
    )

    parser.add_argument(
        "--no-auto-init",
        action="store_true",
        help="Don't auto-run /init if CLAUDE.md missing"
    )

    parser.add_argument(
        "--status",
        action="store_true",
        help="Show status report only"
    )

    args = parser.parse_args()

    # Create bridge
    bridge = CodexCliBridge(
        project_root=args.project,
        auto_init=not args.no_auto_init
    )

    # Execute requested action
    if args.status:
        status = bridge.get_status()
        print("=" * 64)
        print("STATUS REPORT")
        print("=" * 64)
        for key, value in status.items():
            print(f"{key}: {value}")
        print("=" * 64)
        sys.exit(0)

    elif args.validate:
        success = bridge.validate_only()
        sys.exit(0 if success else 1)

    else:
        # Full generation
        success = bridge.run()
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
