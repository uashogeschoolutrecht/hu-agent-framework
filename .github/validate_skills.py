#!/usr/bin/env python3
"""Validate the simple, portable skill contract used by the marketplace."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).parents[1]
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED = {"name", "description", "owner", "last_reviewed"}
HIDDEN = {"\u202a", "\u202b", "\u202c", "\u202d", "\u202e", "\u2066", "\u2067", "\u2069", "\u200b", "\u200c", "\u200d", "\ufeff"}


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("frontmatter must start with ---")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("frontmatter is not closed") from error
    values = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        if not separator or not key.strip() or not value.strip():
            raise ValueError(f"invalid frontmatter line: {line}")
        values[key.strip()] = value.strip()
    return values


errors = []
for skill_file in ROOT.glob("plugins/*/skills/*/SKILL.md"):
    if any(character in skill_file.read_text(encoding="utf-8") for character in HIDDEN):
        errors.append(f"{skill_file}: hidden Unicode character found")
    try:
        values = frontmatter(skill_file)
    except ValueError as error:
        errors.append(f"{skill_file}: {error}")
        continue
    missing = REQUIRED - values.keys()
    if missing:
        errors.append(f"{skill_file}: missing {', '.join(sorted(missing))}")
    if values.get("name") != skill_file.parent.name or not NAME.fullmatch(values.get("name", "")):
        errors.append(f"{skill_file}: name must be kebab-case and match its directory")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)

print("Skill validation passed")
