import unittest
from datetime import datetime

from src.app import get_version
from src.report import build_report


class TestApplication(unittest.TestCase):
    def test_development_version(self) -> None:
        """Check that the development version is correct."""
        self.assertEqual(get_version(), "0.1.0-dev")

    def test_basic_report(self) -> None:
        """Check the basic report fields and values."""
        data = {
            "project": "GitReleaseLab",
            "status": "development",
        }

        report = build_report(data)

        self.assertEqual(report["project"], "GitReleaseLab")
        self.assertEqual(report["status"], "development")
        self.assertEqual(
            report["summary"],
            "GitReleaseLab is development",
        )

    def test_report_contains_valid_timestamp(self) -> None:
        """Check that the report contains a valid timezone-aware timestamp."""
        data = {
            "project": "GitReleaseLab",
            "status": "development",
        }

        report = build_report(data)

        self.assertIn("generated_at", report)

        timestamp = datetime.fromisoformat(report["generated_at"])

        self.assertIsNotNone(timestamp.tzinfo)


if __name__ == "__main__":
    unittest.main()