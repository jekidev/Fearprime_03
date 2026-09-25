import tempfile
import unittest
from pathlib import Path

from tools.fearprime_repo_audit import (
    csv_audit,
    data_reference_audit,
    duplicate_identifier_audit,
    personal_data_audit,
    yaml_audit,
    markdown_link_audit,
    version_audit,
)


class RepoAuditTests(unittest.TestCase):
    def make_minimal_repo(self, root: Path):
        (root / "data").mkdir()
        (root / "VERSION").write_text("0.30\n", encoding="utf-8")
        (root / "README.md").write_text(
            "# Test\n\n**Aktuel framework-version: v0.30 · 2026-09-20**\n\n"
            "[Doc](docs/OK.md)\n",
            encoding="utf-8",
        )
        (root / "REPO_MAP.md").write_text(
            "# Map\n\nVersion 0.30 · 2026-09-20\n", encoding="utf-8"
        )
        (root / "CHANGELOG.md").write_text(
            "# Changelog\n\n## Unreleased\n\n## v0.30 — test\n", encoding="utf-8"
        )
        (root / "docs").mkdir()
        (root / "docs" / "OK.md").write_text("# OK\n", encoding="utf-8")
        (root / "data" / "ok.csv").write_text("a,b\n1,2\n", encoding="utf-8")

    def test_clean_minimal_repo_has_no_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_minimal_repo(root)
            findings = (
                markdown_link_audit(root)
                + version_audit(root)
                + csv_audit(root)
            )
            errors = [f for f in findings if f.level == "ERROR"]
            self.assertEqual(errors, [])

    def test_version_sources_work_without_optional_changelog(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_minimal_repo(root)
            (root / "CHANGELOG.md").unlink()
            self.assertEqual(version_audit(root), [])
            (root / "VERSION").unlink()
            self.assertTrue(any(f.code == "VERSION_FILE_MISSING" for f in version_audit(root)))

    def test_broken_link_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_minimal_repo(root)
            (root / "README.md").write_text(
                "# Test\n\n**Aktuel framework-version: v0.30 · 2026-09-20**\n"
                "[Missing](docs/NOPE.md)\n",
                encoding="utf-8",
            )
            findings = markdown_link_audit(root)
            self.assertTrue(any(f.code == "BROKEN_LINK" for f in findings))

    def test_version_mismatch_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_minimal_repo(root)
            (root / "REPO_MAP.md").write_text(
                "# Map\n\nVersion 0.29 · test\n", encoding="utf-8"
            )
            findings = version_audit(root)
            self.assertTrue(any(f.code == "VERSION_MISMATCH" for f in findings))

    def test_duplicate_csv_headers_are_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_minimal_repo(root)
            (root / "data" / "bad.csv").write_text("a,a\n1,2\n", encoding="utf-8")
            findings = csv_audit(root)
            self.assertTrue(any(f.code == "CSV_DUP_HEADER" for f in findings))

    def test_missing_or_extra_fields_are_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_minimal_repo(root)
            (root / "data" / "bad.csv").write_text(
                "a,b\n1\n1,2,3\n", encoding="utf-8"
            )
            findings = csv_audit(root)
            self.assertEqual(sum(f.code == "CSV_ROW_WIDTH" for f in findings), 2)

    def test_quoted_multiline_field_and_empty_cell_are_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_minimal_repo(root)
            (root / "data" / "valid.csv").write_text(
                'a,b\n"first, line\nsecond line",\n', encoding="utf-8"
            )
            self.assertEqual(csv_audit(root), [])

    def test_yaml_syntax_is_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data").mkdir()
            (root / "data" / "valid.yaml").write_text("key: value\n", encoding="utf-8")
            self.assertEqual(yaml_audit(root), [])
            (root / "data" / "invalid.yaml").write_text("key: [unterminated\n", encoding="utf-8")
            self.assertTrue(any(f.code == "YAML_PARSE" for f in yaml_audit(root)))

    def test_study_paths_and_cross_file_ids_are_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data").mkdir()
            (root / "07_STUDIES" / "VERIFIED").mkdir(parents=True)
            card = root / "07_STUDIES" / "VERIFIED" / "study.md"
            card.write_text("# Study\n", encoding="utf-8")
            (root / "data" / "studies.csv").write_text(
                "study_id,study_card_path\nS1,07_STUDIES/VERIFIED/study.md\n",
                encoding="utf-8",
            )
            (root / "data" / "effects.csv").write_text(
                "effect_id,study_id\nE1,S1\n", encoding="utf-8"
            )
            (root / "data" / "risk_of_bias.csv").write_text(
                "study_id,overall\nS1,LOW\n", encoding="utf-8"
            )
            self.assertFalse(any(f.level == "ERROR" for f in data_reference_audit(root)))
            (root / "data" / "effects.csv").write_text(
                "effect_id,study_id\nE1,UNKNOWN\n", encoding="utf-8"
            )
            self.assertTrue(any(f.code == "STUDY_REFERENCE_MISSING" for f in data_reference_audit(root)))

    def test_documented_duplicate_reference_is_triaged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cards = root / "07_STUDIES" / "VERIFIED"
            cards.mkdir(parents=True)
            a = cards / "a.md"
            b = cards / "b.md"
            a.write_text("DOI: 10.1234/example", encoding="utf-8")
            b.write_text("DOI: 10.1234/example", encoding="utf-8")
            data = root / "data"
            data.mkdir()
            (data / "duplicate_reference_registry.csv").write_text(
                "identifier,path_a,path_b,review_status\n"
                "DOI:10.1234/example,07_STUDIES/VERIFIED/a.md,"
                "07_STUDIES/VERIFIED/b.md,verified\n",
                encoding="utf-8",
            )
            findings = duplicate_identifier_audit(root)
            self.assertTrue(any(f.code == "DUPLICATE_ID_DOCUMENTED" for f in findings))
            self.assertFalse(any(f.code == "DUPLICATE_ID" for f in findings))

    def test_cpr_pattern_is_flagged_for_manual_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "notes.md").write_text("Personnummer: 010190-1234", encoding="utf-8")
            self.assertTrue(any(f.code == "POSSIBLE_DANISH_CPR" for f in personal_data_audit(root)))

    def test_unclosed_quoted_field_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_minimal_repo(root)
            (root / "data" / "bad.csv").write_text(
                'a,b\n1,"unclosed\n', encoding="utf-8"
            )
            self.assertTrue(any(f.code == "CSV_PARSE" for f in csv_audit(root)))


if __name__ == "__main__":
    unittest.main()
