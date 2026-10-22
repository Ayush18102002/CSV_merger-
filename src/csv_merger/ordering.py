"""Decide the order in which CSV files are merged."""
import re
from pathlib import Path


def natural_key(path: Path) -> list:
    """Sort key so 'file2.csv' comes before 'file10.csv'."""
    parts = re.split(r"(\d+)", path.name.lower())
    return [int(p) if p.isdigit() else p for p in parts]


def read_order_file(order_file: Path) -> list[str]:
    """Read file names from merge_order.txt (ignores blank lines and # comments)."""
    lines = order_file.read_text(encoding="utf-8").splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")]


def get_ordered_files(input_dir: Path, order_file: Path) -> list[Path]:
    """
    Return CSV files in merge order.

    1. If config/merge_order.txt has entries, that exact order is used.
    2. Otherwise files are sorted naturally by name (01_, 02_, ... or file1, file2, ...).
    """
    if order_file.exists():
        names = read_order_file(order_file)
        if names:
            files = [input_dir / name for name in names]
            missing = [f.name for f in files if not f.exists()]
            if missing:
                raise FileNotFoundError(f"Listed in merge_order.txt but not found: {missing}")
            return files

    files = sorted(input_dir.glob("*.csv"), key=natural_key)
    if not files:
        raise FileNotFoundError(f"No .csv files found in {input_dir}")
    return files
