---
name: Release Checklist
about: Manual checklist for publishing a tagged release
title: "Release: vX.Y.Z"
labels: [release]
assignees: ''
---

## Pre-release
- [ ] Confirm `main` is green (all required checks passing)
- [ ] Review `CHANGELOG.md` entries match upcoming version
- [ ] Ensure `.claude/commands/git/*` prompts and docs are up to date
- [ ] Verify `/review` and `/security-scan` run clean locally

## Versioning
- [ ] Decide semantic version bump: `major` / `minor` / `patch`
- [ ] Update version references (README, docs, packages)
- [ ] Commit version bump using `chore(release): vX.Y.Z`

## Release Orchestrator Workflow
- [ ] Trigger `release-orchestrator` (via `/run-release` command or Actions tab)
- [ ] Review generated release notes artifact
- [ ] Approve `release` environment gate and verify annotated tag push

## Post-release
- [ ] Publish GitHub Release (convert draft to published)
- [ ] Announce in project channels (status update, docs)
- [ ] Create follow-up issues for leftovers (if any)

