"""Command-line entry point."""
import argparse
import logging
from pathlib import Path

from . import config
from .merger import merge_csv_files
from .ordering import get_ordered_files


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Combine many CSV files into a single CSV.")
    p.add_argument("-i", "--input-dir", type=Path, default=config.INPUT_DIR)
    p.add_argument("-o", "--output", type=Path, default=config.OUTPUT_FILE)
    p.add_argument("--order-file", type=Path, default=config.ORDER_FILE)
    p.add_argument("--no-source-column", action="store_true",
                   help="Do not add the 'source_file' column.")
    return p.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
    args = parse_args()

    files = get_ordered_files(args.input_dir, args.order_file)
    logging.info("Merging %d files in this order:", len(files))
    for i, f in enumerate(files, 1):
        logging.info("  %2d. %s", i, f.name)

    source_col = None if args.no_source_column else config.SOURCE_COLUMN
    combined = merge_csv_files(files, config.ENCODINGS, source_col)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(args.output, index=False, encoding="utf-8-sig")
    logging.info("Done: %d rows x %d columns -> %s", *combined.shape, args.output)
