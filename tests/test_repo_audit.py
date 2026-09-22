import tempfile
import unittest
from pathlib import Path

from tools.fearprime_repo_audit import (
    csv_audit,
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


if __name__ == "__main__":
    unittest.main()
