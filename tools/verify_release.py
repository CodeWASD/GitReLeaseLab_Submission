import hashlib
import json
import sys
from pathlib import Path


from pathlib import Path

ARCHIVE_PATH = Path(
    r"C:\Users\11\Desktop\file\GitReLeaseLab_Submission\GitReleaseLab\release\GitReleaseLab_v0.1.0.zip"
)

CHECKSUM_PATH = Path(
    r"C:\Users\11\Desktop\file\GitReLeaseLab_Submission\GitReleaseLab\release\SHA256SUMS"
)

RESULT_PATH = Path(
    r"C:\Users\11\Desktop\file\GitReLeaseLab_Submission\GitReleaseLab\evidence\verification_result.json"
)

def calculate_sha256(file_path: Path) -> str:
    """Calculate the SHA256 hash without loading the whole file into memory."""
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def read_expected_hash(checksum_path: Path, archive_name: str) -> str | None:
    """Read the expected hash for archive_name from a SHA256SUMS file."""
    if not checksum_path.is_file():
        return None

    for line in checksum_path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line:
            continue

        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            continue

        expected_hash, listed_name = parts
        listed_name = listed_name.lstrip("*").strip()

        if listed_name == archive_name:
            expected_hash = expected_hash.lower()
            if len(expected_hash) == 64 and all(
                character in "0123456789abcdef" for character in expected_hash
            ):
                return expected_hash

    return None



def main() -> int:
    archive_path = ARCHIVE_PATH
    checksum_path = CHECKSUM_PATH
    result_path = RESULT_PATH

    expected_hash = read_expected_hash(
        checksum_path,
        archive_path.name
    )

    actual_hash = (
        calculate_sha256(archive_path)
        if archive_path.is_file()
        else None
    )

    if expected_hash is None or actual_hash is None:
        status = "MISSING"
        exit_code = 2
    elif actual_hash == expected_hash:
        status = "PASS"
        exit_code = 0
    else:
        status = "FAIL"
        exit_code = 1

    result = {
        "file": "GitReleaseLab_v0.1.0.zip",
        "algorithm": "SHA256",
        "expected_hash": expected_hash,
        "actual_hash": actual_hash,
        "status": status,
    }

    json_output = json.dumps(result, indent=2)
    result_path.write_text(json_output + "\n", encoding="utf-8")
    print(json_output)
    print(f"\nResult saved to: {result_path.name}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
