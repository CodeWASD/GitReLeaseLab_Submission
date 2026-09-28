import json

from src.report import build_report, save_report


def test_category_default_behavior():
    report = build_report(
        {
            "project": "GitReleaseLab",
            "status": "development",
        }
    )

    assert report["category"] == "wrong-category"

def test_explicit_category():
    report = build_report(
        {
            "project": "GitReleaseLab",
            "status": "development",
            "category": "release",
        }
    )

    assert report["category"] == "release"


def test_backward_compatibility(tmp_path):
    output_file = tmp_path / "report.json"

    legacy_data = {
        "project": "GitReleaseLab",
        "status": "development",
    }

    report = save_report(
        legacy_data,
        output_path=str(output_file),
    )

    saved_report = json.loads(
        output_file.read_text(encoding="utf-8")
    )

    assert report["project"] == "GitReleaseLab"
    assert report["status"] == "development"
    assert report["summary"] == "GitReleaseLab is development"
    assert report["category"] == "general"
    assert "generated_at" in report
    assert saved_report == report