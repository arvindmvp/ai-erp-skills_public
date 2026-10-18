#!/usr/bin/env python3
"""Validate the repository's Agent Skills files using the Python standard library."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,64}$")
REQUIRED_SECTIONS = [
    "Purpose",
    "When to use / when not to use",
    "Inputs needed",
    "Step-by-step instructions",
    "D365 data and ERP MCP tools used (if any)",
    "Output format",
    "Guardrails",
    "Example prompts",
    "Limitations",
]
ALLOWED_CATEGORIES = {"supply-chain", "finance", "consultant-toolkit"}
ALLOWED_STATUSES = {"draft", "tested", "stable"}


def field_value(frontmatter, field, indentation=""):
    pattern = re.compile(
        rf"^{re.escape(indentation)}{re.escape(field)}:\s*(.*?)\s*$",
        re.MULTILINE,
    )
    match = pattern.search(frontmatter)
    return match.group(1).strip("\"'") if match else None


def validate_skill(path):
    errors = []
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    if len(lines) >= 500:
        errors.append(f"{path.relative_to(ROOT)}: must be under 500 lines")

    if not content.startswith("---\n"):
        return [f"{path.relative_to(ROOT)}: missing YAML frontmatter"]

    parts = content.split("\n---\n", 1)
    if len(parts) != 2:
        return [f"{path.relative_to(ROOT)}: frontmatter must end with ---"]
    frontmatter = parts[0][4:]
    body = parts[1]

    name = field_value(frontmatter, "name")
    description = field_value(frontmatter, "description")
    license_name = field_value(frontmatter, "license")
    category = field_value(frontmatter, "category", "  ")
    status = field_value(frontmatter, "status", "  ")

    if not name or not NAME_PATTERN.fullmatch(name):
        errors.append(f"{path.relative_to(ROOT)}: name must be lowercase letters, digits, or hyphens (max 64)")
    elif name != path.parent.name:
        errors.append(f"{path.relative_to(ROOT)}: name must match folder '{path.parent.name}'")

    if not description:
        errors.append(f"{path.relative_to(ROOT)}: missing description")
    elif len(description) > 1024:
        errors.append(f"{path.relative_to(ROOT)}: description exceeds 1024 characters")
    elif not re.search(r"\b(when|whenever|if)\b", description, re.IGNORECASE):
        errors.append(f"{path.relative_to(ROOT)}: description must state when to use the skill")

    if license_name != "MIT":
        errors.append(f"{path.relative_to(ROOT)}: license must be MIT")
    if category not in ALLOWED_CATEGORIES:
        errors.append(f"{path.relative_to(ROOT)}: metadata.category is missing or invalid")
    elif len(path.relative_to(SKILLS_ROOT).parts) != 3 or category != path.relative_to(SKILLS_ROOT).parts[0]:
        errors.append(f"{path.relative_to(ROOT)}: metadata.category must match its skills category folder")
    if status not in ALLOWED_STATUSES:
        errors.append(f"{path.relative_to(ROOT)}: metadata.status must be draft, tested, or stable")

    for key in ("author", "version", "d365-module", "blog-post", "tested-in"):
        if not field_value(frontmatter, key, "  "):
            errors.append(f"{path.relative_to(ROOT)}: missing metadata.{key}")

    headings = re.findall(r"^## (.+?)\s*$", body, re.MULTILINE)
    section_positions = []
    for section in REQUIRED_SECTIONS:
        if section not in headings:
            errors.append(f"{path.relative_to(ROOT)}: missing section '{section}'")
        else:
            section_positions.append(headings.index(section))
    if len(section_positions) == len(REQUIRED_SECTIONS) and section_positions != sorted(section_positions):
        errors.append(f"{path.relative_to(ROOT)}: required sections are out of order")

    guardrails = re.search(r"^## Guardrails\s*$([\s\S]*?)(?=^## |\Z)", body, re.MULTILINE)
    if guardrails:
        guardrail_text = guardrails.group(1).lower()
        if "read-only" not in guardrail_text or "explicit human approval" not in guardrail_text:
            errors.append(f"{path.relative_to(ROOT)}: guardrails must specify read-only behavior and explicit human approval")

    return errors


def main():
    skill_files = sorted(SKILLS_ROOT.glob("*/*/SKILL.md"))
    if not skill_files:
        print("No skills found under skills/<category>/<skill-name>/SKILL.md", file=sys.stderr)
        return 1

    errors = []
    for skill_file in skill_files:
        errors.extend(validate_skill(skill_file))

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(skill_files)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
