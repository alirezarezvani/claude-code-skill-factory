"""
Codex CLI Execution Helpers

Python wrappers for Codex CLI commands with intelligent features:
- Always uses `codex exec` (never plain `codex` - critical for Claude Code)
- Intelligent model selection (gpt-5 vs gpt-5-codex)
- Sandbox mode helpers (read-only, workspace-write, danger-full-access)
- Session management (start, resume, list)
- Error handling and user notifications
"""

import subprocess
import json
from typing import Dict, Optional, List, Tuple
from dataclasses import dataclass
from enum import Enum


class CodexModel(Enum):
    """Codex model types."""
    GPT5 = "gpt-5"  # General high reasoning
    GPT5_CODEX = "gpt-5-codex"  # Code editing specialized


class SandboxMode(Enum):
    """Codex sandbox modes."""
    READ_ONLY = "read-only"  # Safe analysis (default)
    WORKSPACE_WRITE = "workspace-write"  # File modifications
    DANGER_FULL_ACCESS = "danger-full-access"  # Network access


class ReasoningEffort(Enum):
    """Model reasoning effort levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"  # Default


@dataclass
class CodexResult:
    """Result from Codex CLI execution."""
    success: bool
    stdout: str
    stderr: str
    return_code: int
    command: str
    session_id: Optional[str] = None
    model_used: Optional[str] = None


class CodexExecutor:
    """
    Python wrappers for Codex CLI commands.

    **CRITICAL**: Always uses `codex exec` not plain `codex`.
    Plain `codex` fails in Claude Code (non-terminal environment).
    """

    def __init__(self, working_dir: Optional[str] = None):
        """
        Initialize Codex executor.

        Args:
            working_dir: Optional working directory for Codex commands
        """
        self.working_dir = working_dir

    def exec_analysis(
        self,
        prompt: str,
        model: CodexModel = CodexModel.GPT5,
        reasoning: ReasoningEffort = ReasoningEffort.HIGH,
        enable_search: bool = False
    ) -> CodexResult:
        """
        Execute read-only analysis task.

        Args:
            prompt: Task description
            model: Codex model to use (default: GPT5)
            reasoning: Reasoning effort (default: HIGH)
            enable_search: Enable web search (default: False)

        Returns:
            CodexResult with execution details
        """
        return self._exec_command(
            prompt=prompt,
            model=model,
            sandbox=SandboxMode.READ_ONLY,
            reasoning=reasoning,
            enable_search=enable_search
        )

    def exec_edit(
        self,
        prompt: str,
        model: CodexModel = CodexModel.GPT5_CODEX,
        reasoning: ReasoningEffort = ReasoningEffort.HIGH,
        full_auto: bool = True
    ) -> CodexResult:
        """
        Execute code editing task.

        Args:
            prompt: Task description
            model: Codex model to use (default: GPT5_CODEX - specialized for coding)
            reasoning: Reasoning effort (default: HIGH)
            full_auto: Run in full-auto mode (default: True)

        Returns:
            CodexResult with execution details
        """
        return self._exec_command(
            prompt=prompt,
            model=model,
            sandbox=SandboxMode.WORKSPACE_WRITE,
            reasoning=reasoning,
            full_auto=full_auto
        )

    def exec_with_search(
        self,
        prompt: str,
        model: CodexModel = CodexModel.GPT5,
        sandbox: SandboxMode = SandboxMode.READ_ONLY,
        reasoning: ReasoningEffort = ReasoningEffort.HIGH
    ) -> CodexResult:
        """
        Execute task with web search enabled.

        Args:
            prompt: Task description
            model: Codex model to use (default: GPT5)
            sandbox: Sandbox mode (default: READ_ONLY)
            reasoning: Reasoning effort (default: HIGH)

        Returns:
            CodexResult with execution details
        """
        return self._exec_command(
            prompt=prompt,
            model=model,
            sandbox=sandbox,
            reasoning=reasoning,
            enable_search=True
        )

    def resume_session(self, session_id: Optional[str] = None) -> CodexResult:
        """
        Resume Codex session.

        Args:
            session_id: Optional session ID (uses --last if not provided)

        Returns:
            CodexResult with execution details
        """
        if session_id:
            # Resume specific session
            cmd = ["codex", "exec", "resume", session_id]
        else:
            # Resume last session
            cmd = ["codex", "exec", "resume", "--last"]

        return self._run_command(cmd, command_type="resume")

    def list_sessions(self) -> List[Dict[str, str]]:
        """
        List recent Codex sessions.

        Returns:
            List of session dictionaries (id, description, timestamp)
        """
        # Note: codex CLI doesn't have a direct list command
        # This would need to be implemented based on Codex CLI session storage
        # For now, return empty list
        return []

    def _exec_command(
        self,
        prompt: str,
        model: CodexModel,
        sandbox: SandboxMode,
        reasoning: ReasoningEffort,
        enable_search: bool = False,
        full_auto: bool = False
    ) -> CodexResult:
        """
        Execute Codex CLI command.

        **CRITICAL**: Always uses `codex exec` not plain `codex`.

        Args:
            prompt: Task description
            model: Codex model
            sandbox: Sandbox mode
            reasoning: Reasoning effort
            enable_search: Enable web search
            full_auto: Full auto mode

        Returns:
            CodexResult with execution details
        """
        # Build command - ALWAYS use `codex exec`
        cmd = [
            "codex",
            "exec",
            "-m", model.value,
            "-s", sandbox.value,
            "-c", f"model_reasoning_effort={reasoning.value}"
        ]

        # Add optional flags
        if enable_search:
            cmd.append("--search")

        if full_auto:
            cmd.append("--full-auto")

        # Always skip git repo check for smoother execution
        cmd.append("--skip-git-repo-check")

        # Add working directory if specified
        if self.working_dir:
            cmd.extend(["-C", self.working_dir])

        # Add prompt
        cmd.append(prompt)

        return self._run_command(cmd, command_type="exec", model=model.value)

    def _run_command(
        self,
        cmd: List[str],
        command_type: str,
        model: Optional[str] = None
    ) -> CodexResult:
        """
        Run Codex CLI command.

        Args:
            cmd: Command list
            command_type: Type of command (exec, resume)
            model: Optional model name for metadata

        Returns:
            CodexResult with execution details
        """
        # Convert command to string for display
        cmd_str = " ".join(cmd)

        print(f"🚀 Executing Codex CLI command:")
        print(f"   {cmd_str}")
        print()

        try:
            # Execute command
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            success = result.returncode == 0

            if success:
                print("✅ Codex execution successful")
            else:
                print(f"❌ Codex execution failed (exit code {result.returncode})")

            return CodexResult(
                success=success,
                stdout=result.stdout,
                stderr=result.stderr,
                return_code=result.returncode,
                command=cmd_str,
                model_used=model
            )

        except subprocess.TimeoutExpired:
            error_msg = "Codex command timed out after 5 minutes"
            print(f"❌ {error_msg}")

            return CodexResult(
                success=False,
                stdout="",
                stderr=error_msg,
                return_code=-1,
                command=cmd_str,
                model_used=model
            )

        except FileNotFoundError:
            error_msg = """
Codex CLI not found!

Please ensure:
1. Codex CLI is installed
2. Codex is in your PATH
3. Try: which codex

Installation:
  Visit: https://github.com/openai/codex
"""
            print(f"❌ {error_msg}")

            return CodexResult(
                success=False,
                stdout="",
                stderr=error_msg,
                return_code=-1,
                command=cmd_str,
                model_used=model
            )

        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            print(f"❌ {error_msg}")

            return CodexResult(
                success=False,
                stdout="",
                stderr=error_msg,
                return_code=-1,
                command=cmd_str,
                model_used=model
            )

    def generate_command_string(
        self,
        prompt: str,
        model: CodexModel,
        sandbox: SandboxMode,
        reasoning: ReasoningEffort = ReasoningEffort.HIGH,
        enable_search: bool = False,
        full_auto: bool = False
    ) -> str:
        """
        Generate Codex CLI command string (for documentation).

        Args:
            prompt: Task description
            model: Codex model
            sandbox: Sandbox mode
            reasoning: Reasoning effort
            enable_search: Enable web search
            full_auto: Full auto mode

        Returns:
            Command string
        """
        cmd = f"codex exec -m {model.value} -s {sandbox.value} \\\n"
        cmd += f"  -c model_reasoning_effort={reasoning.value} \\\n"

        if enable_search:
            cmd += "  --search \\\n"

        if full_auto:
            cmd += "  --full-auto \\\n"

        cmd += "  --skip-git-repo-check \\\n"

        if self.working_dir:
            cmd += f"  -C {self.working_dir} \\\n"

        cmd += f'  "{prompt}"'

        return cmd


def main():
    """Demo usage of CodexExecutor."""
    import argparse

    parser = argparse.ArgumentParser(description="Codex CLI Execution Helper")
    parser.add_argument(
        "action",
        choices=["analysis", "edit", "search", "resume"],
        help="Action to perform"
    )
    parser.add_argument(
        "--prompt",
        help="Task prompt (required for analysis, edit, search)"
    )
    parser.add_argument(
        "--model",
        choices=["gpt-5", "gpt-5-codex"],
        default="gpt-5",
        help="Codex model to use"
    )
    parser.add_argument(
        "--working-dir",
        help="Working directory"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show command without executing"
    )

    args = parser.parse_args()

    executor = CodexExecutor(working_dir=args.working_dir)

    # Map string to enum
    model_map = {
        "gpt-5": CodexModel.GPT5,
        "gpt-5-codex": CodexModel.GPT5_CODEX
    }
    model = model_map[args.model]

    if args.action in ["analysis", "edit", "search"] and not args.prompt:
        print("❌ --prompt is required for this action")
        return

    if args.dry_run:
        if args.action == "analysis":
            cmd = executor.generate_command_string(
                prompt=args.prompt,
                model=model,
                sandbox=SandboxMode.READ_ONLY,
                reasoning=ReasoningEffort.HIGH
            )
        elif args.action == "edit":
            cmd = executor.generate_command_string(
                prompt=args.prompt,
                model=CodexModel.GPT5_CODEX,
                sandbox=SandboxMode.WORKSPACE_WRITE,
                reasoning=ReasoningEffort.HIGH,
                full_auto=True
            )
        elif args.action == "search":
            cmd = executor.generate_command_string(
                prompt=args.prompt,
                model=model,
                sandbox=SandboxMode.READ_ONLY,
                reasoning=ReasoningEffort.HIGH,
                enable_search=True
            )
        else:  # resume
            cmd = "codex exec resume --last"

        print("Generated command:")
        print(cmd)
        return

    # Execute action
    if args.action == "analysis":
        result = executor.exec_analysis(prompt=args.prompt, model=model)
    elif args.action == "edit":
        result = executor.exec_edit(prompt=args.prompt, model=model)
    elif args.action == "search":
        result = executor.exec_with_search(prompt=args.prompt, model=model)
    elif args.action == "resume":
        result = executor.resume_session()

    # Display result
    print("\n" + "=" * 64)
    print("RESULT")
    print("=" * 64)
    print(f"Success: {result.success}")
    print(f"Return Code: {result.return_code}")
    print(f"Model: {result.model_used}")
    print(f"Command: {result.command}")

    if result.stdout:
        print("\nStdout:")
        print(result.stdout)

    if result.stderr:
        print("\nStderr:")
        print(result.stderr)


if __name__ == "__main__":
    main()
