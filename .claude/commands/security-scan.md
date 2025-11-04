---
description: Perform local security scanning and dispatch the security audit workflow.
---

## Local Scan
1. Install tooling (first run): `pip install safety==3.2.4` and `brew install gitleaks` (or `go install github.com/zricethezav/gitleaks/v8@latest`).
2. Detect secrets: `gitleaks detect --verbose --redact`
3. Dependency audit (if `requirements*.txt` exists):
   ```bash
   for f in $(ls **/requirements*.txt 2>/dev/null); do
       safety check --full-report --file "$f"
   done
   ```
4. Document results in the commit template.

## Trigger Remote Audit
```bash
gh workflow run security-audit.yml --ref $(git branch --show-current)
gh run watch --workflow "Security Audit (Claude)"
```

## Completion
- Ensure both local and remote scans are clean before pushing or merging.

