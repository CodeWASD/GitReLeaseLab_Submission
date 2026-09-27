import json

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def build_report(data: dict[str, Any]) -> dict[str, Any]:

    report = {
        "project": data["project"],
        "status": data["status"],
    }

    if "category" in data:
        report["category"] = data["category"]

    report["summary"] = f"{data['project']} is {data['status']}"
    report["generated_at"] = datetime.now(timezone.utc).isoformat()

    return report


def save_report(
    data: dict[str, Any],
    output_path: str = "temp/report.json",
) -> dict[str, Any]:

    report = build_report(data)

    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)

    destination.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )

    return report