#!/usr/bin/env python3
"""Public-repo guard: fails CI when something private lands in this PUBLIC repo.

Zero dependencies. Checks every tracked file (git ls-files):

  private-file   working notes that belong in a private place: reports,
                 prompts, backlogs, status/handoff notes, a long CLAUDE.md
                 (a short pointer is fine), local env files, keys.
  secret         something that looks like a key or token.
  email          a personal email address (noreply/example addresses pass).

    python3 <this file>            # exit 1 on any finding

A finding means: move the file to the private repo or the Claude project,
or take the value out. Never silence the check for a real private file.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())

PRIVATE_PATHS = [
    r"(^|/)docs/reports/",
    r"(^|/)docs/prompts/",
    r"(^|/)handoff/",
    r"(^|/)scratchpad/",
    r"(^|/)(BACKLOG|STATUS|WORKFLOW|DISTRIBUTION|STATS|NOTES|TODO)(\.[a-z]+)?\.md$",
    r"(^|/)\.env$",
    r"(^|/)\.env\.(?!example$)[^/]+$",
    r"(^|/)\.dev\.vars$",
    r"(^|/)dart_defines\.json$",
    r"\.(pem|key|p12|keystore|jks|mobileprovision)$",
    r"(^|/)\.claude/",
]

# A CLAUDE.md / AGENTS.md may stay only as a short pointer to the private notes.
NOTES_FILES = re.compile(r"(^|/)(CLAUDE|AGENTS)\.md$")
NOTES_MAX_BYTES = 3000

SECRETS = [
    r"AKIA[0-9A-Z]{16}",
    r"sk-ant-[A-Za-z0-9_-]{10,}",
    r"sk-[A-Za-z0-9]{32,}",
    r"gh[pousr]_[A-Za-z0-9]{30,}",
    r"github_pat_[A-Za-z0-9_]{20,}",
    r"xox[abprs]-[A-Za-z0-9-]{10,}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    r"[?&]key=[A-Za-z0-9]{20,}",
    r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][A-Za-z0-9_\-./+]{20,}['\"]",
]

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
EMAIL_OK = re.compile(
    r"(noreply|no-reply|users\.noreply\.github\.com|@example\.(com|org|net)|@anthropic\.com"
    r"|@[a-z0-9-]+\.(test|invalid|local)$|@[0-9.]+x\.)",
    re.I,
)

BINARY = re.compile(r"\.(png|jpe?g|webp|gif|ico|woff2?|ttf|otf|mp3|wav|pbf|gz|zip|pdf)$", re.I)
SKIP = re.compile(r"(^|/)(package-lock\.json|pubspec\.lock|.*\.lock)$|(^|/)public_guard\.py$")


def main() -> int:
    files = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
    findings: list[str] = []
    for f in files:
        if any(re.search(p, f) for p in PRIVATE_PATHS):
            findings.append(f"private-file: {f}")
            continue
        path = ROOT / f
        if not path.is_file():
            continue
        if NOTES_FILES.search(f) and path.stat().st_size > NOTES_MAX_BYTES:
            findings.append(
                f"private-file: {f} is {path.stat().st_size} bytes: keep project notes private, "
                f"leave a pointer of under {NOTES_MAX_BYTES} bytes here"
            )
        if BINARY.search(f) or SKIP.search(f):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            for p in SECRETS:
                if re.search(p, line):
                    findings.append(f"secret: {f}:{n}")
                    break
            for m in EMAIL.finditer(line):
                if not EMAIL_OK.search(m.group(0)):
                    findings.append(f"email: {f}:{n}: {m.group(0)}")
    for x in findings:
        print(f"::error::{x}")
    print(f"public guard: {len(files)} files, {len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
