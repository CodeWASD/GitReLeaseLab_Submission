from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = PROJECT_ROOT / "VERSION"


def get_version() -> str:
    """Read and return the current project version."""
    return VERSION_FILE.read_text(encoding="utf-8").strip()


def main() -> None:
    version = get_version()
    print(f"GitReleaseLab version: {version}")


if __name__ == "__main__":
    main()