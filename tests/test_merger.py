import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from csv_merger.merger import merge_csv_files
from csv_merger.ordering import get_ordered_files


def test_order_and_single_output(tmp_path):
    for name, val in {"file10.csv": "3", "file2.csv": "2", "file1.csv": "1"}.items():
        (tmp_path / name).write_text(f"id,val\n{val},x\n")
    files = get_ordered_files(tmp_path, tmp_path / "none.txt")
    assert [f.name for f in files] == ["file1.csv", "file2.csv", "file10.csv"]
    df = merge_csv_files(files, ("utf-8",), "source_file")
    assert list(df["id"]) == ["1", "2", "3"]
