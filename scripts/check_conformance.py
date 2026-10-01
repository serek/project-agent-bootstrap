#!/usr/bin/env python3
"""Offline conformance checks for the project-bootstrap package."""

from __future__ import annotations

import re
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "project-bootstrap"
SKILL_FILE = SKILL_DIR / "SKILL.md"
EXAMPLE_FILES = (
    ROOT / "examples" / "lean-example.md",
    ROOT / "examples" / "standard-example.md",
    ROOT / "examples" / "web-portal-example.md",
    ROOT / "examples" / "python-service-example.md",
)
REQUIRED_ASSETS = {
    "AGENTS.md.template",
    "Claude.md.template",
    "TESTING.md.template",
    "WORKFLOW.md.template",
    "LINEAR-DESCRIPTION.md.template",
    "EVIDENCE.md.template",
    "CYRUS-LINEAR.md.template",
    "PRD-README.md.template",
    "ADR-README.md.template",
    "CONTEXT.md.template",
}
REQUIRED_REFERENCES = {"LINEAR-OPERATING-MODEL.md"}
SECTION_HEADING = re.compile(r"^## (\d+)\. ", re.MULTILINE)
LOCAL_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\{\{[^{}]+\}\}")
NONPORTABLE_DEFAULTS = (
    (re.compile(r"\bTEAMHOS(?:-[A-Z0-9]+)?\b", re.IGNORECASE), "TEAMHOS project identifier"),
    (re.compile(r"\bHOS-[0-9]+\b", re.IGNORECASE), "HOS project identifier"),
    (re.compile(r"\bPythia\s+(?:reviewer|review|gate|approval|required)\b", re.IGNORECASE), "Pythia-specific review default"),
    (re.compile(r"\bOracle\s+(?:reviewer|review|gate|approval|required)\b", re.IGNORECASE), "Oracle-specific review default"),
    (re.compile(r"\bReady for Dev\b", re.IGNORECASE), "project-specific status default"),
)


def frontmatter_fields(markdown: str) -> dict[str, str]:
    if not markdown.startswith("---\n"):
        raise ValueError("missing YAML frontmatter opener")
    _, frontmatter, _ = markdown.split("---", 2)
    fields: dict[str, str] = {}
    for line in frontmatter.strip().splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    return fields


def check_frontmatter(markdown: str, expected_name: str) -> None:
    fields = frontmatter_fields(markdown)
    if fields.get("name") != expected_name:
        raise ValueError("frontmatter name does not match the skill directory")
    if not fields.get("description"):
        raise ValueError("frontmatter description is empty")


def check_template_sections(markdown: str) -> None:
    sections = [int(value) for value in SECTION_HEADING.findall(markdown)]
    if sections != list(range(1, 18)):
        raise ValueError("task template must have each numbered section 1 through 17 once, in order")


def check_complete_examples(paths: tuple[Path, ...], root: Path = ROOT) -> None:
    for path in paths:
        content = path.read_text(encoding="utf-8")
        if PLACEHOLDER.search(content):
            raise ValueError(f"unresolved template placeholder in {path.relative_to(root)}")
        table_rows = [line for line in content.splitlines() if line.startswith("|")]
        action_rows = [line for line in table_rows if re.search(r"\|\s*(Reuse|Amend|Create|Omit)\s*\|", line)]
        if not action_rows:
            raise ValueError(f"responsibility map missing a reuse/amend/create/omit action in {path.name}")
        fixture_dir = path.parent / path.stem.removesuffix("-example")
        if not fixture_dir.is_dir():
            raise ValueError(f"missing synthetic output directory for {path.name}")
        fixture_root = fixture_dir.resolve()
        for row in action_rows:
            cells = [cell.strip().strip("`") for cell in row.strip("|").split("|")]
            output = cells[0]
            action = cells[1]
            if action in {"Amend", "Create"}:
                prefix = f"examples/{fixture_dir.name}/"
                if not output.startswith(prefix):
                    raise ValueError(f"{action} row must name a fixture output under {prefix}: {output}")
                fixture_output = root / output
                try:
                    fixture_output.resolve().relative_to(fixture_root)
                except ValueError as error:
                    raise ValueError(f"{action} output escapes its fixture directory: {output}") from error
                if not fixture_output.is_file():
                    raise ValueError(f"missing adapted output named by responsibility map: {output}")
                if PLACEHOLDER.search(fixture_output.read_text(encoding="utf-8")):
                    raise ValueError(f"unresolved template placeholder in adapted output: {output}")


def check_local_links(
    root: Path,
    markdown_paths: tuple[Path, ...],
    *,
    enforce_within_root: bool = False,
) -> None:
    for markdown_path in markdown_paths:
        content = markdown_path.read_text(encoding="utf-8")
        for target in LOCAL_LINK.findall(content):
            target = target.strip()
            if target.startswith(("https://", "http://", "mailto:")) or "{{" in target:
                continue
            target_path, separator, fragment = target.partition("#")
            resolved = (markdown_path.parent / target_path).resolve() if target_path else markdown_path
            if enforce_within_root:
                try:
                    resolved.relative_to(root.resolve())
                except ValueError as error:
                    raise ValueError(
                        f"local link escapes {root.name} in {markdown_path.relative_to(root)}: {target}"
                    ) from error
            if not resolved.exists():
                raise ValueError(f"broken local link in {markdown_path.relative_to(root)}: {target}")
            if separator and fragment and resolved.suffix.lower() in {".md", ".markdown"}:
                headings = markdown_heading_slugs(resolved.read_text(encoding="utf-8"))
                if unquote(fragment).lower() not in headings:
                    raise ValueError(f"broken local heading link in {markdown_path.relative_to(root)}: {target}")


def markdown_heading_slugs(markdown: str) -> set[str]:
    slugs: set[str] = set()
    used: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", markdown, re.MULTILINE):
        text = re.sub(r"`([^`]*)`", r"\1", heading)
        base = re.sub(r"[^\w\- ]", "", text.lower()).strip().replace(" ", "-")
        ordinal = used.get(base, 0)
        used[base] = ordinal + 1
        slugs.add(base if ordinal == 0 else f"{base}-{ordinal}")
    return slugs


def check_linear_guide_is_portable(path: Path) -> None:
    guide = path.read_text(encoding="utf-8")
    required = (
        "Initiative", "Project", "Milestone", "Issue", "CEO / product",
        "CTO / technical leadership", "Engineering", "Readiness", "Delegation",
        "Human acceptance", "configured state", "before relying", "explicit authorization",
    )
    missing = [term for term in required if term.lower() not in guide.lower()]
    if missing:
        raise ValueError("Linear guide lacks required operating concepts: " + ", ".join(missing))


def check_portable_project_tokens(paths: tuple[Path, ...]) -> None:
    for path in paths:
        content = path.read_text(encoding="utf-8")
        for pattern, description in NONPORTABLE_DEFAULTS:
            if pattern.search(content):
                raise ValueError(f"{description} found in {path.name}")


class NegativeConformanceTests(unittest.TestCase):
    def test_frontmatter_rejects_wrong_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "name"):
            check_frontmatter("---\nname: other\ndescription: test\n---\n", "project-bootstrap")

    def test_template_rejects_missing_section(self) -> None:
        headings = "\n".join(f"## {number}. Section" for number in range(1, 17))
        with self.assertRaisesRegex(ValueError, "1 through 17"):
            check_template_sections(headings + "\nThis is optional.\n")

    def test_example_rejects_unresolved_placeholder(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "examples" / "lean").mkdir(parents=True)
            example = root / "examples" / "lean-example.md"
            example.write_text(
                "| Output | Action | Source | Reason |\n| --- | --- | --- | --- |\n"
                "| examples/lean/AGENTS.md | Amend | AGENTS.md | Keep boundary |\n"
                "| examples/lean/TESTING.md | Create | tests | gate |\n| WORKFLOW.md | Omit | none | small |\n"
                "| PRD.md | Reuse | PRD.md | keep |\n", encoding="utf-8"
            )
            (root / "examples" / "lean" / "AGENTS.md").write_text("adapted", encoding="utf-8")
            (root / "examples" / "lean" / "TESTING.md").write_text("{{GATE}}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "placeholder"):
                check_complete_examples((example,), root)

    def test_example_rejects_missing_mapped_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "examples" / "sample").mkdir(parents=True)
            example = root / "examples" / "sample-example.md"
            example.write_text(
                "| Output | Action | Source | Reason |\n| --- | --- | --- | --- |\n"
                "| examples/sample/AGENTS.md | Amend | AGENTS.md | Preserve boundary |\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "missing adapted output"):
                check_complete_examples((example,), root)

    def test_example_accepts_map_without_create(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fixture = root / "examples" / "sample"
            fixture.mkdir(parents=True)
            example = root / "examples" / "sample-example.md"
            example.write_text(
                "| Output | Action | Source | Reason |\n| --- | --- | --- | --- |\n"
                "| examples/sample/AGENTS.md | Amend | AGENTS.md | Preserve boundary |\n"
                "| TESTING.md | Reuse | Existing checks | Keep owner |\n",
                encoding="utf-8",
            )
            (fixture / "AGENTS.md").write_text("adapted", encoding="utf-8")
            check_complete_examples((example,), root)

    def test_local_link_checker_rejects_missing_target(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "README.md"
            source.write_text("[missing](absent.md)", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "broken local link"):
                check_local_links(root, (source,))

    def test_local_link_checker_rejects_missing_heading(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "README.md"
            source.write_text("# Existing heading\n\n[missing](#not-there)\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "broken local heading link"):
                check_local_links(root, (source,))

    def test_skill_local_link_checker_rejects_escape(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "skill"
            root.mkdir()
            source = root / "SKILL.md"
            source.write_text("[outside](../../outside.md)\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "escapes skill"):
                check_local_links(root, (source,), enforce_within_root=True)

    def test_portability_checker_rejects_project_default(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "SKILL.md"
            source.write_text("Use Pythia reviewer for this project's default review.\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Pythia-specific review default"):
                check_portable_project_tokens((source,))


def main() -> int:
    try:
        check_frontmatter(SKILL_FILE.read_text(encoding="utf-8"), SKILL_DIR.name)
        assets = {path.name for path in (SKILL_DIR / "assets").iterdir() if path.is_file()}
        missing_assets = sorted(REQUIRED_ASSETS - assets)
        if missing_assets:
            raise ValueError("missing assets: " + ", ".join(missing_assets))
        references = {path.name for path in (SKILL_DIR / "references").iterdir() if path.is_file()}
        missing_references = sorted(REQUIRED_REFERENCES - references)
        if missing_references:
            raise ValueError("missing references: " + ", ".join(missing_references))
        check_template_sections((SKILL_DIR / "assets" / "LINEAR-DESCRIPTION.md.template").read_text(encoding="utf-8"))
        check_complete_examples(EXAMPLE_FILES)
        check_linear_guide_is_portable(SKILL_DIR / "references" / "LINEAR-OPERATING-MODEL.md")
        portable_docs = (SKILL_FILE, *tuple((SKILL_DIR / "assets").iterdir()), *tuple((SKILL_DIR / "references").iterdir()))
        check_portable_project_tokens(portable_docs)
        skill_markdown = tuple(path for path in SKILL_DIR.rglob("*.md") if path.is_file())
        check_local_links(SKILL_DIR, skill_markdown, enforce_within_root=True)
        markdown_paths = tuple(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
        check_local_links(ROOT, markdown_paths)
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(NegativeConformanceTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        return 1
    print("Package conformance passed: metadata, assets, links and heading anchors, 17-section convention, portable Linear guide, examples, and negative cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
