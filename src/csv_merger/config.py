"""Central place for paths and default settings."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_DIR = PROJECT_ROOT / "data" / "input"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"
OUTPUT_FILE = OUTPUT_DIR / "combined_dataset.csv"

# Optional: list file names (one per line) to force an exact merge order.
ORDER_FILE = PROJECT_ROOT / "config" / "merge_order.txt"

# Encodings tried in order when reading each CSV.
ENCODINGS = ("utf-8-sig", "utf-8", "latin-1")

# Name of the extra column that records which file each row came from.
SOURCE_COLUMN = "source_file"
