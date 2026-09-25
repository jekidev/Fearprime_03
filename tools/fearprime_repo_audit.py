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

    required = [version_path, readme_path, map_path]
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
    }
    if changelog_path.exists():
        sources["CHANGELOG.md"] = CHANGELOG_RELEASE_RE.search(read_text(changelog_path))
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


def yaml_audit(root: Path):
    findings: list[Finding] = []
    try:
        import yaml
    except ImportError:
        return [
            Finding(
                "ERROR",
                "YAML_VALIDATOR_UNAVAILABLE",
                "data",
                "Install PyYAML to validate YAML syntax.",
            )
        ]

    for path in [*iter_files(root, ".yaml"), *iter_files(root, ".yml")]:
        rel = str(path.relative_to(root))
        try:
            with path.open("r", encoding="utf-8") as handle:
                yaml.safe_load(handle)
        except (OSError, UnicodeError, yaml.YAMLError) as exc:
            findings.append(Finding("ERROR", "YAML_PARSE", rel, f"YAML parse failed: {exc}"))
    return findings


def data_reference_audit(root: Path):
    findings: list[Finding] = []
    data_dir = root / "data"
    studies_path = data_dir / "studies.csv"
    if not studies_path.exists():
        return [Finding("ERROR", "STUDY_DATA_MISSING", "data/studies.csv", "Canonical study index missing.")]

    try:
        with studies_path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, strict=True)
            if not reader.fieldnames or not {"study_id", "study_card_path"} <= set(reader.fieldnames):
                return [Finding("ERROR", "STUDY_DATA_SCHEMA", "data/studies.csv", "Required columns study_id and study_card_path are missing.")]
            studies = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        return [Finding("ERROR", "STUDY_DATA_PARSE", "data/studies.csv", f"Could not read study index: {exc}")]

    study_ids: set[str] = set()
    card_paths: set[str] = set()
    for row in studies:
        study_id = (row.get("study_id") or "").strip()
        card_path = (row.get("study_card_path") or "").strip()
        if not study_id:
            findings.append(Finding("ERROR", "STUDY_ID_EMPTY", "data/studies.csv", "Study row has no study_id."))
            continue
        if study_id in study_ids:
            findings.append(Finding("ERROR", "STUDY_ID_DUPLICATE", "data/studies.csv", f"Duplicate study_id: {study_id}"))
        study_ids.add(study_id)
        if card_path:
            card_paths.add(card_path)
            target = (root / card_path).resolve()
            try:
                target.relative_to(root.resolve())
            except ValueError:
                target = None
            if target is None or not target.is_file():
                findings.append(Finding("ERROR", "STUDY_CARD_MISSING", "data/studies.csv", f"{study_id} points to missing or out-of-repository card: {card_path}"))
        else:
            findings.append(Finding("WARN", "STUDY_CARD_UNSET", "data/studies.csv", f"{study_id} has no study_card_path."))

    for filename, id_field in (("effects.csv", "effect_id"), ("risk_of_bias.csv", None)):
        path = data_dir / filename
        if not path.exists():
            continue
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle, strict=True)
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            findings.append(Finding("ERROR", "DATA_REFERENCE_PARSE", str(path.relative_to(root)), f"Could not read references: {exc}"))
            continue
        seen: set[str] = set()
        for row in rows:
            study_id = (row.get("study_id") or "").strip()
            if study_id and study_id not in study_ids:
                findings.append(Finding("ERROR", "STUDY_REFERENCE_MISSING", str(path.relative_to(root)), f"Unknown study_id: {study_id}"))
            if id_field:
                value = (row.get(id_field) or "").strip()
                if value and value in seen:
                    findings.append(Finding("ERROR", "EFFECT_ID_DUPLICATE", str(path.relative_to(root)), f"Duplicate {id_field}: {value}"))
                if value:
                    seen.add(value)

    overlap_path = data_dir / "participant_overlap.csv"
    if overlap_path.exists():
        try:
            with overlap_path.open("r", encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle, strict=True):
                    card_path = (row.get("study_card_path") or "").strip()
                    if card_path and not (root / card_path).is_file():
                        findings.append(Finding("ERROR", "OVERLAP_CARD_MISSING", str(overlap_path.relative_to(root)), f"Missing participant-overlap card: {card_path}"))
        except (OSError, UnicodeError, csv.Error) as exc:
            findings.append(Finding("ERROR", "OVERLAP_DATA_PARSE", str(overlap_path.relative_to(root)), f"Could not read overlap register: {exc}"))

    duplicate_registry = data_dir / "duplicate_reference_registry.csv"
    if duplicate_registry.exists():
        try:
            with duplicate_registry.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle, strict=True)
                required = {"identifier", "path_a", "path_b", "review_status"}
                if not reader.fieldnames or not required <= set(reader.fieldnames):
                    findings.append(Finding("ERROR", "DUPLICATE_REGISTRY_SCHEMA", str(duplicate_registry.relative_to(root)), "Required duplicate registry columns are missing."))
                else:
                    for row in reader:
                        for field in ("path_a", "path_b"):
                            card_path = (row.get(field) or "").strip()
                            if not card_path or not (root / card_path).is_file():
                                findings.append(Finding("ERROR", "DUPLICATE_REGISTRY_CARD_MISSING", str(duplicate_registry.relative_to(root)), f"Missing card in {field}: {card_path}"))
        except (OSError, UnicodeError, csv.Error) as exc:
            findings.append(Finding("ERROR", "DUPLICATE_REGISTRY_PARSE", str(duplicate_registry.relative_to(root)), f"Could not read duplicate registry: {exc}"))

    verified_dir = root / "07_STUDIES" / "VERIFIED"
    if verified_dir.exists():
        verified_cards = {
            str(path.relative_to(root))
            for path in verified_dir.glob("*.md")
            if path.name != "README.md"
        }
        unindexed = sorted(verified_cards - card_paths)
        if unindexed:
            findings.append(
                Finding(
                    "WARN",
                    "STUDY_DATA_SEED_COVERAGE",
                    "data/studies.csv",
                    f"{len(unindexed)} verified study cards are not mirrored in the seed CSV; this is a coverage warning, not a claim that the cards are invalid.",
                )
            )
    return findings


def personal_data_audit(root: Path):
    findings: list[Finding] = []
    cpr_pattern = re.compile(r"(?<!\d)\d{6}-\d{4}(?!\d)")
    text_suffixes = {".md", ".csv", ".yaml", ".yml", ".json", ".txt"}
    for path in iter_files(root):
        if path.suffix.lower() not in text_suffixes:
            continue
        try:
            text = read_text(path)
        except (OSError, UnicodeError):
            continue
        if cpr_pattern.search(text):
            findings.append(
                Finding(
                    "WARN",
                    "POSSIBLE_DANISH_CPR",
                    str(path.relative_to(root)),
                    "A CPR-formatted number was found; manually verify and remove private data if present.",
                )
            )
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

    registry_path = root / "data" / "duplicate_reference_registry.csv"
    documented: set[tuple[str, str, str]] = set()
    if registry_path.exists():
        try:
            with registry_path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle, strict=True)
                required = {"identifier", "path_a", "path_b", "review_status"}
                if reader.fieldnames and required <= set(reader.fieldnames):
                    for row in reader:
                        if (row.get("review_status") or "").strip().lower() != "verified":
                            continue
                        identifier = (row.get("identifier") or "").strip().lower()
                        path_a = (row.get("path_a") or "").strip()
                        path_b = (row.get("path_b") or "").strip()
                        if identifier and path_a and path_b:
                            documented.add((identifier, *sorted((path_a, path_b))))
                else:
                    findings.append(Finding("ERROR", "DUPLICATE_REGISTRY_SCHEMA", str(registry_path.relative_to(root)), "Required duplicate registry columns are missing."))
        except (OSError, UnicodeError, csv.Error) as exc:
            findings.append(Finding("ERROR", "DUPLICATE_REGISTRY_PARSE", str(registry_path.relative_to(root)), f"Could not read duplicate registry: {exc}"))

    for identifier, paths_set in sorted(locations.items()):
        if len(paths_set) <= 1:
            continue
        paths = sorted(paths_set)
        unreviewed_pairs = [
            (path_a, path_b)
            for index, path_a in enumerate(paths)
            for path_b in paths[index + 1 :]
            if (identifier.lower(), path_a, path_b) not in documented
        ]
        if not unreviewed_pairs:
            findings.append(
                Finding(
                    "INFO",
                    "DUPLICATE_ID_DOCUMENTED",
                    ", ".join(paths),
                    f"{identifier} repeats only in pairs documented in duplicate_reference_registry.csv.",
                )
            )
        else:
            findings.append(
                Finding(
                    "WARN",
                    "DUPLICATE_ID",
                    ", ".join(path for pair in unreviewed_pairs for path in pair),
                    f"{identifier} appears in multiple study-card files; undocumented card pairs require review.",
                )
            )
    return findings

def run_audit(root: Path):
    findings: list[Finding] = []
    findings.extend(markdown_link_audit(root))
    findings.extend(version_audit(root))
    findings.extend(csv_audit(root))
    findings.extend(yaml_audit(root))
    findings.extend(data_reference_audit(root))
    findings.extend(personal_data_audit(root))
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
