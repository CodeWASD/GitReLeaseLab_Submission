import argparse
import hashlib
import json
import sys
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify a release archive using a SHA256SUMS file."
    )

    parser.add_argument(
        "--archive",
        required=True,
        type=Path,
        help="Path to the release archive.",
    )

    parser.add_argument(
        "--checksum",
        required=True,
        type=Path,
        help="Path to the SHA256SUMS.txt file.",
    )

    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path where the JSON verification result will be saved.",
    )

    return parser.parse_args()


def calculate_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def read_expected_hash(
    checksum_path: Path,
    archive_name: str,
) -> tuple[str | None, str | None]:

    if not checksum_path.is_file():
        return None, "Checksum file does not exist."

    try:
        lines = checksum_path.read_text(
            encoding="utf-8-sig"
        ).splitlines()
    except OSError as error:
        return None, f"Cannot read checksum file: {error}"

    for line in lines:
        line = line.strip()

        if not line:
            continue

        parts = line.split(maxsplit=1)

        if len(parts) != 2:
            continue

        expected_hash, listed_file = parts

        listed_file = listed_file.lstrip("*").strip()
        listed_name = listed_file.replace("\\", "/").rsplit("/", 1)[-1]

        if listed_name != archive_name:
            continue

        expected_hash = expected_hash.lower()

        is_valid_sha256 = (
            len(expected_hash) == 64
            and all(
                character in "0123456789abcdef"
                for character in expected_hash
            )
        )

        if not is_valid_sha256:
            return None, "Checksum entry is not a valid SHA256 value."

        return expected_hash, None

    return None, "Archive entry was not found in checksum file."


def save_result(output_path: Path, result: dict) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    arguments = parse_arguments()

    archive_path = arguments.archive
    checksum_path = arguments.checksum
    output_path = arguments.output

    expected_hash, checksum_error = read_expected_hash(
        checksum_path,
        archive_path.name,
    )

    actual_hash = None
    archive_error = None

    if archive_path.is_file():
        try:
            actual_hash = calculate_sha256(archive_path)
        except OSError as error:
            archive_error = f"Cannot read archive: {error}"
    else:
        archive_error = "Archive file does not exist."

    if expected_hash is None or actual_hash is None:
        status = "MISSING"
        exit_code = 2
        reason = archive_error or checksum_error
    elif actual_hash == expected_hash:
        status = "PASS"
        exit_code = 0
        reason = "Actual hash matches expected hash."
    else:
        status = "FAIL"
        exit_code = 1
        reason = "Actual hash does not match expected hash."

    result = {
        "file": archive_path.name,
        "algorithm": "SHA256",
        "expected_hash": expected_hash,
        "actual_hash": actual_hash,
        "status": status,
        "reason": reason,
    }

    save_result(output_path, result)

    print(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nResult saved to: {output_path}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())