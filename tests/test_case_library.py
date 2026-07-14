import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from case_library import parse_case, render_case, slugify, validate_record, write_case


class CaseLibraryTests(unittest.TestCase):
    def load_fixture(self, name: str) -> dict[str, object]:
        path = ROOT / "tests" / "fixtures" / name
        return json.loads(path.read_text(encoding="utf-8"))

    def test_slugify_normalizes_ascii_and_keeps_chinese(self) -> None:
        self.assertEqual(slugify("Founder 定位 Sprint"), "founder-定位-sprint")

    def test_valid_record_has_no_issues(self) -> None:
        self.assertEqual(validate_record(self.load_fixture("valid-case.json")), [])

    def test_invalid_record_reports_actionable_fields(self) -> None:
        fields = {issue.field for issue in validate_record(self.load_fixture("invalid-case.json"))}
        self.assertTrue({"id", "name", "permission", "target_customer", "tags", "recorded_at", "updated_at"} <= fields)

    def test_render_and_parse_preserve_required_values(self) -> None:
        record = self.load_fixture("valid-case.json")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "case.md"
            path.write_text(render_case(record), encoding="utf-8")
            parsed = parse_case(path)
        for field in ("id", "name", "source", "permission", "target_customer", "promise", "tags"):
            self.assertEqual(parsed[field], record[field])

    def test_write_case_refuses_duplicate_id(self) -> None:
        record = self.load_fixture("valid-case.json")
        with tempfile.TemporaryDirectory() as directory:
            cases_dir = Path(directory)
            write_case(record, cases_dir)
            with self.assertRaisesRegex(ValueError, "already exists"):
                write_case(record, cases_dir)

    def test_rebuild_index_lists_case_with_searchable_fields(self) -> None:
        from case_library import rebuild_index

        record = self.load_fixture("valid-case.json")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases_dir = root / "cases"
            index_path = root / "case-index.md"
            write_case(record, cases_dir)
            content = rebuild_index(cases_dir, index_path)
            self.assertEqual(index_path.read_text(encoding="utf-8"), content)
        self.assertIn("founder-positioning-sprint", content)
        self.assertIn("知识型创始人", content)
        self.assertIn("咨询", content)

    def test_rebuild_index_is_sorted_by_case_id(self) -> None:
        from case_library import rebuild_index

        first = self.load_fixture("valid-case.json")
        second = dict(first, id="another-case", name="另一个案例")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases_dir = root / "cases"
            write_case(first, cases_dir)
            write_case(second, cases_dir)
            content = rebuild_index(cases_dir, root / "index.md")
        self.assertLess(content.index("another-case"), content.index("founder-positioning-sprint"))


if __name__ == "__main__":
    unittest.main()
