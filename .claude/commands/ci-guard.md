---
description: Trigger the Commit & Branch Guard workflow on demand.
argument-hint: [ref]
---

## Purpose
Run `ci-commit-branch-guard.yml` manually to validate branch naming and Conventional Commit syntax.

## Usage

```
/ci-guard [ref]
```

- `ref` (optional): Branch or SHA to validate. Defaults to current branch.

## Steps
1. Ensure you are authenticated with GitHub CLI (`gh auth status`).
2. Determine the branch to validate (defaults to `git branch --show-current`).
3. Trigger the workflow:
   ```bash
   gh workflow run ci-commit-branch-guard.yml --ref ${ref:-$(git branch --show-current)}
   ```
4. Watch progress:
   ```bash
   gh run watch --workflow "Commit & Branch Guard"
   ```
5. Resolve any failures (branch rename or commit amend) before continuing.

