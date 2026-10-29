import json
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).parent / "data"


def load_data(filename: str) -> list[dict[str, Any]]:
    """Load records from a JSON file."""
    file_path = DATA_DIR / filename

    if not file_path.exists():
        return []

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_data(filename: str, records: list[dict[str, Any]]) -> None:
    """Save records to a JSON file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    file_path = DATA_DIR / filename

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4, ensure_ascii=False)