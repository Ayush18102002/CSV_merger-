"""Run:  python main.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from csv_merger.cli import main

if __name__ == "__main__":
    main()
