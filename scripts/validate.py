#!/usr/bin/env python3
"""Structural checks for the judge skill packages. Standard library only.

Checks, for every skills/<lang>/<skill>/ folder:
- SKILL.md exists and starts with YAML frontmatter holding `name` and `description`;
- `name` matches the folder name and uses lowercase letters, digits and hyphens;
- the description stays within 1,024 characters;
- light editions (judge-flash) stay under 8,000 characters in total;
- every references/... path or relative Markdown link points to an existing file;
- agents/openai.yaml, if present, names the matching skill in its default prompt;
- English and Arabic editions ship the same set of files.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
FLASH_LIMIT = 8000
DESCRIPTION_LIMIT = 1024
errors: list[str] = []


def fail(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def check_skill(folder: Path) -> None:
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        fail(folder, "missing SKILL.md")
        return
    text = skill_md.read_text(encoding="utf-8")
    meta = frontmatter(text)
    name, description = meta.get("name", ""), meta.get("description", "")
    if not name or not description:
        fail(skill_md, "frontmatter needs both `name` and `description`")
    if name != folder.name:
        fail(skill_md, f"name `{name}` does not match folder `{folder.name}`")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name or "x"):
        fail(skill_md, f"name `{name}` must be lowercase letters, digits and hyphens")
    if len(description) > DESCRIPTION_LIMIT:
        fail(skill_md, f"description is {len(description)} chars (limit {DESCRIPTION_LIMIT})")
    if folder.name.endswith("-flash") and len(text) >= FLASH_LIMIT:
        fail(skill_md, f"light edition is {len(text)} chars (must stay under {FLASH_LIMIT})")

    referenced = set(re.findall(r"(?<![\w/])(references/[\w.-]+\.md)", text))
    referenced |= {
        link for link in re.findall(r"\]\(([^)#\s]+)\)", text) if "://" not in link
    }
    for ref in sorted(referenced):
        if not (folder / ref).is_file():
            fail(skill_md, f"links to missing file `{ref}`")

    yaml = folder / "agents" / "openai.yaml"
    if yaml.is_file():
        content = yaml.read_text(encoding="utf-8")
        if f"${name} " not in content:
            fail(yaml, f"default prompt should invoke `${name}`")
        for asset in re.findall(r"icon_(?:small|large):\s*(\S+)", content):
            if not (folder / asset).is_file():
                fail(yaml, f"icon `{asset}` not found")

    print(f"ok  {folder.relative_to(ROOT)}  ({len(text):,} chars)")


def files_of(folder: Path) -> set[str]:
    return {str(p.relative_to(folder)) for p in folder.rglob("*") if p.is_file()}


def main() -> int:
    langs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for lang in langs:
        for folder in sorted(p for p in lang.iterdir() if p.is_dir()):
            check_skill(folder)
    en, ar = SKILLS / "en", SKILLS / "ar"
    if en.is_dir() and ar.is_dir():
        for folder in sorted(p for p in en.iterdir() if p.is_dir()):
            twin = ar / folder.name
            if not twin.is_dir():
                fail(folder, "no Arabic counterpart")
            elif files_of(folder) != files_of(twin):
                fail(folder, f"file set differs from {twin.relative_to(ROOT)}")
    for doc in ("README.md", "CHANGELOG.md", "LICENSE"):
        if not (ROOT / doc).is_file():
            errors.append(f"missing {doc}")
    if errors:
        print("\n".join(f"FAIL {e}" for e in errors))
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
