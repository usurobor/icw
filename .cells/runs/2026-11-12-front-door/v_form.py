#!/usr/bin/env python3
"""V form predicates for the ICW front-door cell (added by ε, amendment 1).

Mechanical checks for AC1/AC6/AC7, so form is validated by predicate, not
judgment. Words are counted in prose only: fenced and indented code blocks,
table delimiter rows and link targets are excluded.

usage: v_form.py REPO
"""
import re
import sys
from pathlib import Path

README_MAX = 650          # whole README
FIRST_SCREEN_MAX = 150    # text before the first '## ' heading, title excluded
EXAMPLE_MAX = 500         # each examples/*.md
PRIOR_ART_FILE = "PRIOR-ART.md"


def prose(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    lines = [l for l in text.splitlines()
             if not l.startswith("    ") and not re.match(r"^\|[-:| ]+\|$", l)]
    text = "\n".join(lines)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    return text


def words(text):
    return len(re.findall(r"[A-Za-z0-9][\w'’-]*", prose(text)))


def first_screen(text):
    body = text.split("\n", 1)[1] if text.startswith("# ") else text
    return body.split("\n## ", 1)[0]


def main(repo):
    repo = Path(repo)
    readme = (repo / "README.md").read_text()
    checks = []
    n = words(readme)
    checks.append((f"README words {n} <= {README_MAX}", n <= README_MAX))
    n = words(first_screen(readme))
    checks.append((f"README first screen words {n} <= {FIRST_SCREEN_MAX}",
                   n <= FIRST_SCREEN_MAX))
    has_refs = bool(re.search(r"^##\s+References", readme, re.M))
    checks.append(("README has no reference list (credits live in "
                   f"{PRIOR_ART_FILE})", not has_refs))
    checks.append((f"{PRIOR_ART_FILE} exists and README links to it",
                   (repo / PRIOR_ART_FILE).exists() and PRIOR_ART_FILE in readme))
    for ex in sorted((repo / "examples").glob("*.md")):
        n = words(ex.read_text())
        checks.append((f"{ex.name} words {n} <= {EXAMPLE_MAX}", n <= EXAMPLE_MAX))
    for msg, ok in checks:
        print(("ok    " if ok else "FAIL  ") + msg)
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
