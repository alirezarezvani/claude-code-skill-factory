"""
Hook Installer - Automated hook installation to Claude Code settings.json

Provides safe installation, uninstallation, and listing of hooks with:
- Atomic file operations (backup, modify, restore)
- JSON validation before/after changes
- Support for user-level (~/.claude/settings.json) and project-level (.claude/settings.json)
- Automatic backup creation with timestamps
- Rollback on failure

macOS/Linux only (Windows not supported in this version)
"""

import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import tempfile
import os


class HookInstaller:
    """Handles hook installation to Claude Code settings.json"""

    def __init__(self):
        self.user_settings_path = Path.home() / '.claude' / 'settings.json'
        self.project_settings_path = Path('.claude') / 'settings.json'

    def get_settings_path(self, level: str = 'user') -> Path:
        """
        Get settings.json path for specified level.

        Args:
            level: 'user' for ~/.claude/settings.json or 'project' for .claude/settings.json

        Returns:
            Path to settings.json

        Raises:
            ValueError: If level is invalid
        """
        if level == 'user':
            return self.user_settings_path
        elif level == 'project':
            return self.project_settings_path
        else:
            raise ValueError(f"Invalid level '{level}'. Must be 'user' or 'project'")

    def backup_settings(self, settings_path: Path) -> Optional[Path]:
        """
        Create timestamped backup of settings.json.

        Args:
            settings_path: Path to settings.json

        Returns:
            Path to backup file, or None if file doesn't exist

        Example:
            settings.json → settings.json.backup.20251106_143025
        """
        if not settings_path.exists():
            return None

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = settings_path.with_suffix(f'.json.backup.{timestamp}')

        shutil.copy2(settings_path, backup_path)
        print(f"✅ Backup created: {backup_path}")

        # Keep only last 5 backups
        self._cleanup_old_backups(settings_path)

        return backup_path

    def _cleanup_old_backups(self, settings_path: Path, keep: int = 5):
        """Keep only the most recent N backups."""
        backup_pattern = f"{settings_path.name}.backup.*"
        backups = sorted(settings_path.parent.glob(backup_pattern), key=lambda p: p.stat().st_mtime, reverse=True)

        # Remove old backups beyond keep limit
        for old_backup in backups[keep:]:
            old_backup.unlink()
            print(f"🗑️  Removed old backup: {old_backup.name}")

    def restore_settings(self, backup_path: Path) -> bool:
        """
        Restore settings.json from backup.

        Args:
            backup_path: Path to backup file

        Returns:
            True if successful, False otherwise
        """
        if not backup_path.exists():
            print(f"❌ Backup not found: {backup_path}")
            return False

        # Determine original settings path
        settings_path = backup_path.parent / 'settings.json'

        try:
            shutil.copy2(backup_path, settings_path)
            print(f"✅ Restored from backup: {backup_path}")
            return True
        except Exception as e:
            print(f"❌ Restore failed: {e}")
            return False

    def load_settings(self, settings_path: Path) -> Tuple[Dict, bool]:
        """
        Load settings.json safely.

        Args:
            settings_path: Path to settings.json

        Returns:
            Tuple of (settings_dict, file_existed)
            If file doesn't exist, returns empty dict with hooks structure

        Raises:
            json.JSONDecodeError: If JSON is malformed
        """
        if not settings_path.exists():
            # Create minimal settings structure
            return {'hooks': {}}, False

        try:
            with open(settings_path, 'r', encoding='utf-8') as f:
                settings = json.load(f)

            # Ensure hooks key exists
            if 'hooks' not in settings:
                settings['hooks'] = {}

            return settings, True

        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Malformed JSON in {settings_path}: {e.msg}",
                e.doc,
                e.pos
            )

    def save_settings(self, settings_path: Path, settings: Dict) -> bool:
        """
        Save settings.json atomically (write to temp, then rename).

        Args:
            settings_path: Path to settings.json
            settings: Settings dictionary to save

        Returns:
            True if successful, False otherwise
        """
        try:
            # Ensure parent directory exists
            settings_path.parent.mkdir(parents=True, exist_ok=True)

            # Write to temporary file first (atomic operation)
            with tempfile.NamedTemporaryFile(
                mode='w',
                encoding='utf-8',
                dir=settings_path.parent,
                delete=False,
                suffix='.tmp'
            ) as tmp_file:
                json.dump(settings, tmp_file, indent=2, ensure_ascii=False)
                tmp_file.write('\n')  # Add trailing newline
                tmp_path = Path(tmp_file.name)

            # Validate JSON before replacing
            with open(tmp_path, 'r', encoding='utf-8') as f:
                json.load(f)  # Will raise if invalid

            # Atomic rename (replaces existing file)
            tmp_path.replace(settings_path)
            print(f"✅ Settings saved: {settings_path}")
            return True

        except Exception as e:
            print(f"❌ Save failed: {e}")
            # Clean up temp file if it exists
            if 'tmp_path' in locals() and tmp_path.exists():
                tmp_path.unlink()
            return False

    def load_hook_config(self, hook_path: Path) -> Tuple[Dict, str]:
        """
        Load hook.json and determine event type.

        Args:
            hook_path: Path to hook folder containing hook.json

        Returns:
            Tuple of (hook_config, event_type)

        Raises:
            FileNotFoundError: If hook.json not found
            ValueError: If event type cannot be determined
        """
        hook_json = hook_path / 'hook.json'

        if not hook_json.exists():
            raise FileNotFoundError(f"hook.json not found in {hook_path}")

        with open(hook_json, 'r', encoding='utf-8') as f:
            hook_config = json.load(f)

        # Determine event type (top-level key in hook.json)
        event_types = ['PostToolUse', 'PreToolUse', 'SessionStart', 'Stop', 'PrePush', 'UserPromptSubmit', 'SubagentStop']
        event_type = None

        for et in event_types:
            if et in hook_config:
                event_type = et
                break

        if not event_type:
            raise ValueError(f"Could not determine event type from hook.json. Expected one of: {event_types}")

        return hook_config, event_type

    def install_hook(self, hook_path: str, level: str = 'user', hook_name: Optional[str] = None) -> bool:
        """
        Install hook to settings.json.

        Args:
            hook_path: Path to hook folder (contains hook.json)
            level: 'user' for ~/.claude or 'project' for .claude
            hook_name: Optional custom name (default: folder name)

        Returns:
            True if successful, False otherwise

        Process:
            1. Load hook.json and determine event type
            2. Backup existing settings.json
            3. Load current settings
            4. Merge hook into appropriate event type array
            5. Save atomically with validation
            6. Rollback on failure
        """
        hook_path = Path(hook_path)
        if not hook_path.exists():
            print(f"❌ Hook path not found: {hook_path}")
            return False

        if hook_name is None:
            hook_name = hook_path.name

        settings_path = self.get_settings_path(level)

        print(f"\n📦 Installing hook: {hook_name}")
        print(f"📍 Location: {settings_path}")

        backup_path = None

        try:
            # 1. Load hook configuration
            hook_config, event_type = self.load_hook_config(hook_path)
            print(f"🎯 Event type: {event_type}")

            # 2. Backup existing settings
            if settings_path.exists():
                backup_path = self.backup_settings(settings_path)

            # 3. Load current settings
            settings, file_existed = self.load_settings(settings_path)

            # 4. Merge hook into settings
            # Ensure event type array exists in hooks
            if event_type not in settings['hooks']:
                settings['hooks'][event_type] = []

            # Get hook entry for this event type
            hook_entry = hook_config[event_type]

            # Check for duplicate (by matcher/command similarity)
            if self._is_duplicate_hook(settings['hooks'][event_type], hook_entry):
                print(f"⚠️  Similar hook already exists for {event_type}")
                response = input("Replace existing hook? (y/n): ").strip().lower()
                if response != 'y':
                    print("❌ Installation cancelled")
                    return False

                # Remove old version before adding new
                settings['hooks'][event_type] = [
                    h for h in settings['hooks'][event_type]
                    if not self._is_matching_hook(h, hook_entry)
                ]

            # Add hook(s) to event type array
            if isinstance(hook_entry, list):
                settings['hooks'][event_type].extend(hook_entry)
            else:
                settings['hooks'][event_type].append(hook_entry)

            # 5. Save settings atomically
            if not self.save_settings(settings_path, settings):
                raise Exception("Failed to save settings")

            print(f"✅ Hook installed successfully!")
            print(f"📝 Hook name: {hook_name}")
            print(f"🎯 Event type: {event_type}")
            print(f"📍 Location: {level} ({settings_path})")

            return True

        except Exception as e:
            print(f"\n❌ Installation failed: {e}")

            # Rollback from backup if available
            if backup_path and backup_path.exists():
                print("🔄 Rolling back from backup...")
                self.restore_settings(backup_path)

            return False

    def _is_duplicate_hook(self, existing_hooks: List[Dict], new_hook: Dict) -> bool:
        """Check if hook already exists (by matcher/command similarity)."""
        if isinstance(new_hook, list):
            new_hook = new_hook[0] if new_hook else {}

        for hook in existing_hooks:
            if self._is_matching_hook(hook, new_hook):
                return True
        return False

    def _is_matching_hook(self, hook1: Dict, hook2: Dict) -> bool:
        """Check if two hooks are similar enough to be duplicates."""
        # Compare matchers
        matcher1 = hook1.get('matcher', {})
        matcher2 = hook2.get('matcher', {})

        if matcher1 == matcher2:
            # Same matcher - check if commands are similar
            hooks1 = hook1.get('hooks', [])
            hooks2 = hook2.get('hooks', [])

            if hooks1 and hooks2:
                cmd1 = hooks1[0].get('command', '').strip()[:50]  # First 50 chars
                cmd2 = hooks2[0].get('command', '').strip()[:50]

                if cmd1 == cmd2:
                    return True

        return False

    def uninstall_hook(self, hook_name: str, level: str = 'user', event_type: Optional[str] = None) -> bool:
        """
        Uninstall hook from settings.json.

        Args:
            hook_name: Name of hook to remove
            level: 'user' or 'project'
            event_type: Optional - event type to search (faster if known)

        Returns:
            True if successful, False otherwise

        Note: Removes hook by matching against hook name or command content
        """
        settings_path = self.get_settings_path(level)

        if not settings_path.exists():
            print(f"❌ Settings file not found: {settings_path}")
            return False

        print(f"\n🗑️  Uninstalling hook: {hook_name}")
        print(f"📍 Location: {settings_path}")

        backup_path = None

        try:
            # 1. Backup settings
            backup_path = self.backup_settings(settings_path)

            # 2. Load settings
            settings, _ = self.load_settings(settings_path)

            # 3. Find and remove hook
            removed = False
            event_types_to_check = [event_type] if event_type else settings['hooks'].keys()

            for et in event_types_to_check:
                if et not in settings['hooks']:
                    continue

                original_count = len(settings['hooks'][et])

                # Remove hooks matching the name
                settings['hooks'][et] = [
                    h for h in settings['hooks'][et]
                    if not self._hook_matches_name(h, hook_name)
                ]

                removed_count = original_count - len(settings['hooks'][et])
                if removed_count > 0:
                    print(f"✅ Removed {removed_count} hook(s) from {et}")
                    removed = True

            if not removed:
                print(f"⚠️  Hook '{hook_name}' not found")
                return False

            # 4. Save settings
            if not self.save_settings(settings_path, settings):
                raise Exception("Failed to save settings")

            print(f"✅ Hook uninstalled successfully!")
            return True

        except Exception as e:
            print(f"\n❌ Uninstallation failed: {e}")

            # Rollback
            if backup_path and backup_path.exists():
                print("🔄 Rolling back from backup...")
                self.restore_settings(backup_path)

            return False

    def _hook_matches_name(self, hook: Dict, name: str) -> bool:
        """Check if hook matches the given name."""
        # Check if name appears in command
        for h in hook.get('hooks', []):
            command = h.get('command', '')
            if name.lower() in command.lower():
                return True

        return False

    def list_installed_hooks(self, level: str = 'user') -> List[Dict]:
        """
        List all installed hooks.

        Args:
            level: 'user' or 'project'

        Returns:
            List of hook info dictionaries with keys:
                - event_type: str
                - matcher: dict
                - command: str (first 100 chars)
                - timeout: int
        """
        settings_path = self.get_settings_path(level)

        if not settings_path.exists():
            return []

        try:
            settings, _ = self.load_settings(settings_path)
            hooks_info = []

            for event_type, hooks in settings.get('hooks', {}).items():
                for hook in hooks:
                    matcher = hook.get('matcher', {})
                    hook_commands = hook.get('hooks', [])

                    if hook_commands:
                        first_hook = hook_commands[0]
                        command = first_hook.get('command', '')[:100]
                        timeout = first_hook.get('timeout', 60)

                        hooks_info.append({
                            'event_type': event_type,
                            'matcher': matcher,
                            'command': command,
                            'timeout': timeout
                        })

            return hooks_info

        except Exception as e:
            print(f"❌ Failed to list hooks: {e}")
            return []


def main():
    """CLI interface for hook installer."""
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python installer.py install <hook_path> [user|project]")
        print("  python installer.py uninstall <hook_name> [user|project]")
        print("  python installer.py list [user|project]")
        sys.exit(1)

    command = sys.argv[1]
    installer = HookInstaller()

    if command == 'install':
        if len(sys.argv) < 3:
            print("Error: hook_path required")
            sys.exit(1)

        hook_path = sys.argv[2]
        level = sys.argv[3] if len(sys.argv) > 3 else 'user'

        success = installer.install_hook(hook_path, level)
        sys.exit(0 if success else 1)

    elif command == 'uninstall':
        if len(sys.argv) < 3:
            print("Error: hook_name required")
            sys.exit(1)

        hook_name = sys.argv[2]
        level = sys.argv[3] if len(sys.argv) > 3 else 'user'

        success = installer.uninstall_hook(hook_name, level)
        sys.exit(0 if success else 1)

    elif command == 'list':
        level = sys.argv[2] if len(sys.argv) > 2 else 'user'

        hooks = installer.list_installed_hooks(level)

        if not hooks:
            print(f"No hooks installed at {level} level")
        else:
            print(f"\n📋 Installed hooks ({level} level):\n")
            for i, hook in enumerate(hooks, 1):
                print(f"{i}. {hook['event_type']}")
                print(f"   Matcher: {hook['matcher']}")
                print(f"   Command: {hook['command']}...")
                print(f"   Timeout: {hook['timeout']}s")
                print()

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == '__main__':
    main()
