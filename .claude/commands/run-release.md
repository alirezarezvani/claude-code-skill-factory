---
description: Orchestrate a tagged release using the release workflow.
argument-hint: <version> [target]
---

## Pre-flight
- Complete the Release Checklist issue.
- Ensure `/review` and `/security-scan` are green on the target branch.

## Trigger Workflow
```
/run-release vX.Y.Z [target]
```

- `vX.Y.Z`: Required semantic version tag (include the `v`).
- `target`: Optional branch/commit (defaults to `main`).

### Command
```bash
gh workflow run release-orchestrator.yml \
  --ref ${target:-main} \
  -f version=${version} \
  -f target=${target:-main}
```

## After Triggering
1. Wait for the `Release Orchestrator` workflow to reach the environment approval step.
2. Approve the `release` environment to publish the annotated tag and draft release.
3. Review and publish the draft release on GitHub.

