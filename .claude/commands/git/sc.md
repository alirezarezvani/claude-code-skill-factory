---
description: Run the security scan gate before pushing.
---

1. Ensure dependencies are installed (`pip install safety==3.2.4 gitleaks==8.18.4`).
2. Scan for committed secrets:
   ```bash
   gitleaks detect --verbose --redact
   ```
   - Resolve any findings before continuing.
3. Audit Python dependencies (if requirements files exist):
   ```bash
   for f in $(ls **/requirements*.txt 2>/dev/null); do
       safety check --full-report --file "$f"
   done
   ```
4. Record results in the commit template’s Testing section.
5. After a clean pass, trigger the remote security audit for visibility:
   ```bash
   gh workflow run security-audit.yml --ref $(git branch --show-current)
   ```

