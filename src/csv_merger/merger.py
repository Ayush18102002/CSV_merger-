"""Core logic: read each CSV and stack them one after another."""
import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def read_csv_safely(path: Path, encodings: tuple[str, ...]) -> pd.DataFrame:
    """Read a CSV as text (keeps IDs/leading zeros intact), trying several encodings."""
    last_error = None
    for enc in encodings:
        try:
            return pd.read_csv(path, dtype=str, keep_default_na=False, encoding=enc)
        except UnicodeDecodeError as err:
            last_error = err
    raise ValueError(f"Could not decode {path.name}: {last_error}")


def merge_csv_files(
    files: list[Path],
    encodings: tuple[str, ...],
    source_column: str | None = None,
) -> pd.DataFrame:
    """
    Stack all files vertically, in the order given, into ONE DataFrame.

    - Columns are matched by name; if a file lacks a column it is left blank.
    - Row order is preserved: all rows of file 1, then file 2, and so on.
    """
    frames = []
    base_columns = None

    for path in files:
        df = read_csv_safely(path, encodings)

        if base_columns is None:
            base_columns = list(df.columns)
        elif set(df.columns) != set(base_columns):
            logger.warning("Column mismatch in %s (columns will be aligned by name)", path.name)

        if source_column:
            df[source_column] = path.name

        logger.info("Loaded %-35s rows=%d", path.name, len(df))
        frames.append(df)

    # sort=False keeps the original column order of the first file
    return pd.concat(frames, ignore_index=True, sort=False).fillna("")
