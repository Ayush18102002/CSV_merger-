# CSV Merger

Combine 20+ CSV files into **one single CSV** (one continuous sheet, rows one after another).

## Folder structure
```
csv_merger/
├── main.py                  # run this
├── requirements.txt
├── config/
│   └── merge_order.txt      # optional: exact file order
├── data/
│   ├── input/               # put all your CSV files here
│   └── output/              # combined_dataset.csv is created here
├── src/csv_merger/
│   ├── config.py            # paths & settings
│   ├── ordering.py          # decides file order
│   ├── merger.py            # merge logic
│   └── cli.py               # command line
└── tests/test_merger.py
```

## Usage
```bash
pip install -r requirements.txt
# 1. copy your CSVs into data/input/
python main.py
```

## Order of files
- **Option A (automatic):** name files `01_a.csv`, `02_b.csv` ... or `file1.csv`, `file2.csv` ... (natural sort, so file2 comes before file10).
- **Option B (manual):** list file names in `config/merge_order.txt`, one per line.

## Options
```bash
python main.py -i my_folder -o result.csv --no-source-column
```
A `source_file` column is added by default so you can trace each row back to its original file.
