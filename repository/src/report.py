import json

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_CATEGORY = "general"


def build_report(data: dict[str, Any]) -> dict[str, Any]:
    """Build a simple report from the supplied data."""

    return {
        "project": data["project"],
        "status": data["status"],
        "category": data.get("category", DEFAULT_CATEGORY),
        "summary": f"{data['project']} is {data['status']}",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def save_report(
    data: dict[str, Any],
    output_path: str = "temp/report.json",
) -> dict[str, Any]:
    """Build and save a report as JSON."""

    report = build_report(data)

    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)

    destination.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )

    return report