#!/usr/bin/env python3
"""Validate the small, reviewable university knowledge catalog."""

import json
from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).parents[1]
KNOWLEDGE = ROOT / "plugins/hu-core/knowledge"
REQUIRED = {"id", "title", "kind", "scope", "owner", "status", "last_reviewed", "review_due", "overridable", "source"}
COMPARED = REQUIRED
STATUSES = {"approved", "draft", "superseded"}
OVERRIDABLE = {"true", "false"}


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError("frontmatter must be closed with ---")
    end = lines.index("---", 1)
    values = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        if not separator or not key.strip() or not value.strip():
            raise ValueError(f"invalid frontmatter line: {line}")
        values[key.strip()] = value.strip()
    return values


def as_text(value) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    return str(value).strip()


errors = []
warnings = []
catalog_path = KNOWLEDGE / "index.json"
try:
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as error:
    errors.append(f"{catalog_path}: {error}")
    catalog = []

catalog_ids = set()
catalog_paths = set()
documents = {}
for entry in catalog:
    entry_id = entry.get("id", "<unknown>")
    missing = REQUIRED - entry.keys()
    if missing:
        errors.append(f"{entry_id}: missing {', '.join(sorted(missing))}")
    if entry.get("id") in catalog_ids:
        errors.append(f"{entry_id}: duplicate catalog id")
    catalog_ids.add(entry.get("id"))
    if as_text(entry.get("status")) not in STATUSES:
        errors.append(f"{entry_id}: status must be one of {', '.join(sorted(STATUSES))}")
    if as_text(entry.get("overridable")) not in OVERRIDABLE:
        errors.append(f"{entry_id}: overridable must be true or false")
    relative = entry.get("path", "")
    if relative in catalog_paths:
        errors.append(f"{entry_id}: duplicate catalog path {relative}")
    catalog_paths.add(relative)
    path = KNOWLEDGE / relative
    if not path.is_file():
        errors.append(f"{entry_id}: missing document {path}")
    else:
        documents[path.resolve()] = entry

today = date.today()
for document in sorted(KNOWLEDGE.glob("**/*.md")):
    if document.name == "README.md":
        continue
    entry = documents.get(document.resolve())
    if entry is None:
        errors.append(f"{document}: document is not registered in index.json")
    try:
        values = frontmatter(document)
    except ValueError as error:
        errors.append(f"{document}: {error}")
        continue
    missing = REQUIRED - values.keys()
    if missing:
        errors.append(f"{document}: missing {', '.join(sorted(missing))}")
    if values.get("scope") != "university":
        errors.append(f"{document}: university catalog documents must have scope: university")
    if values.get("status") not in STATUSES:
        errors.append(f"{document}: status must be one of {', '.join(sorted(STATUSES))}")
    if values.get("overridable") not in OVERRIDABLE:
        errors.append(f"{document}: overridable must be true or false")
    try:
        date.fromisoformat(values.get("last_reviewed", ""))
        review_due = date.fromisoformat(values.get("review_due", ""))
    except ValueError:
        errors.append(f"{document}: review dates must use YYYY-MM-DD")
    else:
        if review_due < today:
            warnings.append(f"{document}: review_due {review_due} has passed")
    if entry is not None:
        for key in sorted(COMPARED):
            catalog_value = as_text(entry.get(key, ""))
            document_value = as_text(values.get(key, ""))
            if catalog_value != document_value:
                errors.append(
                    f"{document}: {key} differs from index.json "
                    f"(catalog: {catalog_value!r}, document: {document_value!r})"
                )

if warnings:
    print("\n".join(f"warning: {warning}" for warning in warnings), file=sys.stderr)

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)

print("Knowledge validation passed")
