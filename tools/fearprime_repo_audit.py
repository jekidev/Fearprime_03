#!/usr/bin/env python3
"""FearPrime repository QA audit.

Standard-library checks for:
- internal Markdown link integrity,
- release-version consistency,
- CSV readability/header integrity,
- orphan Markdown diagnostics,
- duplicate PMID/DOI diagnostics across study cards.

Errors can block CI with --strict. Warnings are reported but do not fail.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

EXCLUDED_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache"}
EXTERNAL_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "spotify:",
    "doi:",
)
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
ROOT_README_VERSION_RE = re.compile(
    r"Aktuel framework-version:\s*v?([0-9]+(?:\.[0-9]+)+)", re.IGNORECASE
)
REPO_MAP_VERSION_RE = re.compile(
    r"^Version\s+v?([0-9]+(?:\.[0-9]+)+)", re.IGNORECASE | re.MULTILINE
)
CHANGELOG_RELEASE_RE = re.compile(
    r"^##\s+v([0-9]+(?:\.[0-9]+)+)\b", re.IGNORECASE | re.MULTILINE
)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
PMID_RE = re.compile(r"\bPMID\s*[:#]?\s*(\d{6,9})\b", re.IGNORECASE)


@dataclass(frozen=True)
class Finding:
    level: str
    code: str
    path: str
    message: str


def iter_files(root: Path, suffix: str | None = None):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if suffix is not None and path.suffix.lower() != suffix:
            continue
        yield path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    # Markdown optional titles are outside the path; simple project links do not
    # use spaces in paths, so split conservatively on whitespace.
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split()[0]
    return unquote(target)


def resolve_local_target(root: Path, source: Path, raw_target: str) -> Path | None:
    target = normalize_link_target(raw_target)
    if not target or target.startswith("#") or target.lower().startswith(EXTERNAL_PREFIXES):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    if target.startswith("/"):
        return root / target.lstrip("/")
    return source.parent / target


def markdown_link_audit(root: Path):
    findings: list[Finding] = []
    inbound: dict[Path, int] = defaultdict(int)

    for source in iter_files(root, ".md"):
        text = read_text(source)
        for raw_target in LINK_RE.findall(text):
            resolved = resolve_local_target(root, source, raw_target)
            if resolved is None:
                continue
            resolved = resolved.resolve()
            if resolved.exists():
                try:
                    rel = resolved.relative_to(root.resolve())
                except ValueError:
                    continue
                if resolved.suffix.lower() == ".md":
                    inbound[rel] += 1
                continue
            findings.append(
                Finding(
                    "ERROR",
                    "BROKEN_LINK",
                    str(source.relative_to(root)),
                    f"Missing target: {normalize_link_target(raw_target)}",
                )
            )

    exempt_names = {"README.md", "CHANGELOG.md", "REPO_MAP.md", "DANSK_ORDBOG.md"}
    for path in iter_files(root, ".md"):
        rel = path.relative_to(root)
        if path.name in exempt_names or "ARCHIVE" in rel.parts:
            continue
        if inbound.get(rel, 0) == 0:
            findings.append(
                Finding(
                    "WARN",
                    "ORPHAN_MD",
                    str(rel),
                    "No inbound Markdown link found.",
                )
            )
    return findings


def version_audit(root: Path):
    findings: list[Finding] = []
    version_path = root / "VERSION"
    readme_path = root / "README.md"
    map_path = root / "REPO_MAP.md"
    changelog_path = root / "CHANGELOG.md"

    required = [version_path, readme_path, map_path, changelog_path]
    missing = [p for p in required if not p.exists()]
    for path in missing:
        findings.append(
            Finding("ERROR", "VERSION_FILE_MISSING", str(path.relative_to(root)), "Required release file missing.")
        )
    if missing:
        return findings

    version = read_text(version_path).strip().lstrip("v")
    sources = {
        "README.md": ROOT_README_VERSION_RE.search(read_text(readme_path)),
        "REPO_MAP.md": REPO_MAP_VERSION_RE.search(read_text(map_path)),
        "CHANGELOG.md": CHANGELOG_RELEASE_RE.search(read_text(changelog_path)),
    }
    for name, match in sources.items():
        if not match:
            findings.append(
                Finding("ERROR", "VERSION_NOT_FOUND", name, "Could not parse release version.")
            )
            continue
        found = match.group(1)
        if found != version:
            findings.append(
                Finding(
                    "ERROR",
                    "VERSION_MISMATCH",
                    name,
                    f"Found {found}; VERSION is {version}.",
                )
            )
    return findings


def csv_audit(root: Path):
    findings: list[Finding] = []
    data_dir = root / "data"
    if not data_dir.exists():
        return [Finding("ERROR", "DATA_DIR_MISSING", "data", "data/ directory missing.")]

    for path in iter_files(data_dir, ".csv"):
        rel = str(path.relative_to(root))
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.reader(handle, strict=True)
                header = next(reader, None)
                if not header:
                    findings.append(Finding("ERROR", "CSV_EMPTY", rel, "CSV has no header row."))
                    continue
                normalized = [cell.strip() for cell in header]
                if any(not cell for cell in normalized):
                    findings.append(Finding("ERROR", "CSV_EMPTY_HEADER", rel, "CSV contains an empty header."))
                if len(set(normalized)) != len(normalized):
                    findings.append(Finding("ERROR", "CSV_DUP_HEADER", rel, "CSV contains duplicate headers."))
                for row in reader:
                    if len(row) != len(header):
                        findings.append(
                            Finding(
                                "ERROR",
                                "CSV_ROW_WIDTH",
                                rel,
                                f"Record ending at line {reader.line_num} has {len(row)} fields; expected {len(header)}.",
                            )
                        )
        except (OSError, UnicodeError, csv.Error) as exc:
            findings.append(Finding("ERROR", "CSV_PARSE", rel, f"CSV parse failed: {exc}"))
    return findings


def duplicate_identifier_audit(root: Path):
    findings: list[Finding] = []
    studies = root / "07_STUDIES"
    if not studies.exists():
        return findings

    locations: dict[str, set[str]] = defaultdict(set)
    excluded_names = {"README.md", "STUDY_LEDGER.md", "SOURCE_REGISTER.md"}

    for path in iter_files(studies, ".md"):
        if path.name in excluded_names or "ARCHIVE" in path.parts:
            continue
        rel = str(path.relative_to(root))
        text = read_text(path)
        for doi in DOI_RE.findall(text):
            locations[f"DOI:{doi.rstrip('.,;').lower()}"].add(rel)
        for pmid in PMID_RE.findall(text):
            locations[f"PMID:{pmid}"].add(rel)

    for identifier, paths in sorted(locations.items()):
        if len(paths) > 1:
            findings.append(
                Finding(
                    "WARN",
                    "DUPLICATE_ID",
                    ", ".join(sorted(paths)),
                    f"{identifier} appears in multiple study-card files; verify alias/reanalysis/duplicate status.",
                )
            )
    return findings


def run_audit(root: Path):
    findings: list[Finding] = []
    findings.extend(markdown_link_audit(root))
    findings.extend(version_audit(root))
    findings.extend(csv_audit(root))
    findings.extend(duplicate_identifier_audit(root))
    return findings


def print_report(findings: list[Finding]):
    errors = [f for f in findings if f.level == "ERROR"]
    warnings = [f for f in findings if f.level == "WARN"]

    print("FearPrime repository QA")
    print(f"errors={len(errors)} warnings={len(warnings)}")
    for finding in findings:
        print(f"[{finding.level}] {finding.code} :: {finding.path} :: {finding.message}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Audit FearPrime repository integrity.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root (default: current directory)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when ERROR findings are present.",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    findings = run_audit(root)
    print_report(findings)

    if args.strict and any(f.level == "ERROR" for f in findings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
