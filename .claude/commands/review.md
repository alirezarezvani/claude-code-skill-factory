---
description: Run the full review gate locally and trigger CI visibility.
---

## Local Checks
1. Execute the git review helper: `/git/rv`
2. Fix any issues reported by yamllint, check-jsonschema, markdown-link-check, or safety.
3. Update the commit template’s Testing section with the commands executed.

## Remote Visibility
1. Trigger Commit & Branch Guard: `/ci-guard`
2. Trigger CI Quality Gate:
   ```bash
   gh workflow run ci-quality-gate.yml --ref $(git branch --show-current)
   gh run watch --workflow "CI Quality Gate"
   ```

## Tips
- Run `/review` before every push to keep the main branch green.
- If workflows fail, fix the root cause and rerun `/review` to confirm.

