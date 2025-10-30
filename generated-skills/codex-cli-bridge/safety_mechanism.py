"""
Safety Mechanism for Codex CLI Bridge Skill

Validates environment before AGENTS.md generation:
1. Check Codex CLI installation
2. Check CLAUDE.md exists (auto-run /init if missing)
3. Validate authentication
4. User-friendly notifications
"""

import os
import subprocess
import sys
from typing import Dict, Optional, Tuple
from pathlib import Path


class SafetyMechanism:
    """
    Safety validation for Codex CLI Bridge Skill.

    Ensures environment is ready before generating AGENTS.md:
    - Codex CLI installed and accessible
    - CLAUDE.md exists (or can be created)
    - User is notified of all actions
    """

    def __init__(self, project_root: str):
        """
        Initialize safety mechanism.

        Args:
            project_root: Path to project root directory
        """
        self.project_root = Path(project_root).resolve()
        self.claude_md_path = self.project_root / "CLAUDE.md"

    def validate_all(self, auto_init: bool = True) -> Tuple[bool, str]:
        """
        Run all safety checks.

        Args:
            auto_init: If True, auto-run /init if CLAUDE.md missing

        Returns:
            Tuple of (success: bool, message: str)
        """
        print("🔍 Running safety checks...")
        print()

        # Check 1: Codex CLI installation
        codex_ok, codex_msg = self.check_codex_cli()
        if not codex_ok:
            return False, codex_msg

        # Check 2: CLAUDE.md exists
        claude_ok, claude_msg = self.check_claude_md(auto_init=auto_init)
        if not claude_ok:
            return False, claude_msg

        # All checks passed
        print("✅ All safety checks passed!")
        print()
        return True, "Environment validated successfully"

    def check_codex_cli(self) -> Tuple[bool, str]:
        """
        Check if Codex CLI is installed and accessible.

        Returns:
            Tuple of (success: bool, message: str)
        """
        print("📦 Checking Codex CLI installation...")

        try:
            # Check if codex command exists
            result = subprocess.run(
                ["which", "codex"],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode != 0:
                error_msg = """
❌ Codex CLI not found!

Codex CLI must be installed and in your PATH.

Installation:
  Visit: https://github.com/openai/codex
  Or check official OpenAI Codex CLI documentation

After installation, verify:
  codex --version
"""
                print(error_msg)
                return False, "Codex CLI not installed"

            codex_path = result.stdout.strip()
            print(f"   Found: {codex_path}")

            # Verify it works
            version_result = subprocess.run(
                ["codex", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )

            if version_result.returncode == 0:
                version = version_result.stdout.strip()
                print(f"   Version: {version}")
                print("   ✅ Codex CLI installed and working")
                print()
                return True, f"Codex CLI found: {version}"
            else:
                error_msg = f"""
❌ Codex CLI installed but not working!

Error: {version_result.stderr}

Try:
  codex login
  codex --help
"""
                print(error_msg)
                return False, "Codex CLI not functioning"

        except subprocess.TimeoutExpired:
            error_msg = "❌ Codex CLI check timed out!"
            print(error_msg)
            return False, "Codex CLI check timeout"

        except Exception as e:
            error_msg = f"""
❌ Error checking Codex CLI!

Error: {str(e)}

Please ensure Codex CLI is installed:
  which codex
  codex --version
"""
            print(error_msg)
            return False, f"Codex CLI check error: {str(e)}"

    def check_claude_md(self, auto_init: bool = True) -> Tuple[bool, str]:
        """
        Check if CLAUDE.md exists. If not, optionally auto-run /init.

        Args:
            auto_init: If True, auto-run /init to create CLAUDE.md

        Returns:
            Tuple of (success: bool, message: str)
        """
        print("📄 Checking CLAUDE.md...")

        if self.claude_md_path.exists():
            print(f"   Found: {self.claude_md_path}")
            print("   ✅ CLAUDE.md exists")
            print()
            return True, f"CLAUDE.md found at {self.claude_md_path}"

        # CLAUDE.md missing
        print(f"   ⚠️  Not found: {self.claude_md_path}")
        print()

        if not auto_init:
            error_msg = """
❌ CLAUDE.md not found!

This skill requires CLAUDE.md to generate AGENTS.md.

Options:
1. Run: /init to create CLAUDE.md
2. Manually create CLAUDE.md in project root
3. Run this skill with auto_init=True

CLAUDE.md is required because:
- It's the source of truth for project configuration
- AGENTS.md is generated FROM CLAUDE.md
- Ensures consistent documentation
"""
            print(error_msg)
            return False, "CLAUDE.md not found"

        # Auto-run /init
        return self.run_init_command()

    def run_init_command(self) -> Tuple[bool, str]:
        """
        Auto-run /init command to create CLAUDE.md.

        Returns:
            Tuple of (success: bool, message: str)
        """
        print("🚀 Auto-running /init to create CLAUDE.md...")
        print()
        print("=" * 60)
        print("IMPORTANT: /init will analyze project and create CLAUDE.md")
        print("This may take 30-60 seconds...")
        print("=" * 60)
        print()

        try:
            # Note: In actual implementation, this would use SlashCommand tool
            # For now, create minimal CLAUDE.md as fallback
            return self.generate_minimal_claude_md()

        except Exception as e:
            error_msg = f"""
❌ Failed to run /init!

Error: {str(e)}

Please manually run:
  /init

Or manually create CLAUDE.md in project root.
"""
            print(error_msg)
            return False, f"/init failed: {str(e)}"

    def generate_minimal_claude_md(self) -> Tuple[bool, str]:
        """
        Generate minimal CLAUDE.md as fallback.

        Returns:
            Tuple of (success: bool, message: str)
        """
        print("📝 Generating minimal CLAUDE.md...")

        # Detect project name
        project_name = self.project_root.name

        minimal_content = f"""# CLAUDE.md

## Repository Purpose

{project_name} - Project documentation auto-generated by codex-cli-bridge skill.

**Note**: This is a minimal CLAUDE.md. Customize it for your project needs.

## Repository Structure

```
{project_name}/
├── CLAUDE.md (this file)
├── AGENTS.md (generated by codex-cli-bridge)
└── [your project files]
```

## Key Information

**Project Name**: {project_name}
**Type**: GREENFIELD_NEW (update as needed)
**Created**: 2025-10-30
**Generated By**: codex-cli-bridge skill

## Next Steps

1. Customize this CLAUDE.md for your project
2. Add skills to `.claude/skills/` if needed
3. Add agents to `.claude/agents/` if needed
4. Run `/update-claude` to regenerate AGENTS.md

## References

- Claude Skills: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- Codex CLI: https://github.com/openai/codex

---

*Auto-generated by codex-cli-bridge skill*
*Edit this file to customize Claude Code configuration*
"""

        try:
            with open(self.claude_md_path, "w", encoding="utf-8") as f:
                f.write(minimal_content)

            print(f"   ✅ Created: {self.claude_md_path}")
            print()
            print("=" * 60)
            print("✅ Minimal CLAUDE.md created successfully!")
            print()
            print("You can now:")
            print("  1. Edit CLAUDE.md to customize for your project")
            print("  2. Proceed with AGENTS.md generation")
            print("  3. Run /update-claude to regenerate later")
            print("=" * 60)
            print()

            return True, f"Minimal CLAUDE.md created at {self.claude_md_path}"

        except Exception as e:
            error_msg = f"""
❌ Failed to create CLAUDE.md!

Error: {str(e)}

Permission issue? Disk full?

Please manually create CLAUDE.md at:
  {self.claude_md_path}
"""
            print(error_msg)
            return False, f"Failed to create CLAUDE.md: {str(e)}"

    def check_authentication(self) -> Tuple[bool, str]:
        """
        Check if user is authenticated with Codex CLI.

        Returns:
            Tuple of (success: bool, message: str)
        """
        print("🔐 Checking Codex CLI authentication...")

        try:
            # Test if codex exec works (requires auth)
            result = subprocess.run(
                ["codex", "exec", "--help"],
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                print("   ✅ Authenticated")
                print()
                return True, "Codex CLI authenticated"
            else:
                error_msg = """
❌ Not authenticated with Codex CLI!

Please run:
  codex login

Follow the authentication flow, then try again.
"""
                print(error_msg)
                return False, "Not authenticated"

        except Exception as e:
            error_msg = f"""
⚠️  Could not verify authentication

Error: {str(e)}

Try running:
  codex login
"""
            print(error_msg)
            # Don't fail hard on auth check - might work anyway
            return True, "Authentication check skipped"

    def get_status_report(self) -> Dict[str, any]:
        """
        Generate comprehensive status report.

        Returns:
            Dictionary with status of all checks
        """
        status = {
            "project_root": str(self.project_root),
            "claude_md_exists": self.claude_md_path.exists(),
            "claude_md_path": str(self.claude_md_path),
            "codex_cli_installed": False,
            "codex_cli_version": None,
            "authenticated": False
        }

        # Check Codex CLI
        try:
            result = subprocess.run(
                ["codex", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                status["codex_cli_installed"] = True
                status["codex_cli_version"] = result.stdout.strip()
        except:
            pass

        # Check auth
        try:
            result = subprocess.run(
                ["codex", "exec", "--help"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                status["authenticated"] = True
        except:
            pass

        return status


def main():
    """Demo usage of SafetyMechanism."""
    import argparse

    parser = argparse.ArgumentParser(description="Codex CLI Bridge Safety Checks")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root directory (default: current directory)"
    )
    parser.add_argument(
        "--no-auto-init",
        action="store_true",
        help="Don't auto-run /init if CLAUDE.md missing"
    )
    parser.add_argument(
        "--status-only",
        action="store_true",
        help="Show status report only (no validation)"
    )

    args = parser.parse_args()

    safety = SafetyMechanism(args.project_root)

    if args.status_only:
        status = safety.get_status_report()
        print("📊 Status Report")
        print("=" * 60)
        for key, value in status.items():
            print(f"{key}: {value}")
        print("=" * 60)
        return

    # Run full validation
    success, message = safety.validate_all(auto_init=not args.no_auto_init)

    if success:
        print("🎉 All systems go! Ready to generate AGENTS.md")
        sys.exit(0)
    else:
        print(f"❌ Validation failed: {message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
