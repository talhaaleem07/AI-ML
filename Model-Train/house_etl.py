"""
ETL pipeline for the Pakistan house price dataset.

    Extract   -> read the raw CSV (everything as text, so nothing is guessed wrongly)
    Transform -> clean numbers, standardise text, fix bad values, remove duplicates,
                 fill gaps, add two useful features
    Load      -> write a clean CSV and a SQLite table

Usage:
    python house_etl.py                      # CSV next to the script, results in ./output
    python house_etl.py --input raw.csv --output-dir clean_data
"""

import argparse
import logging
import sqlite3
from datetime import date
from pathlib import Path

import pandas as pd

# --------------------------------------------------------------------------- #
# Configuration: every "business rule" lives here so it is easy to change
# --------------------------------------------------------------------------- #
CURRENT_YEAR = date.today().year

VALID_RANGES = {                         # values outside these become missing
    "Area_SqFt": (100, 30_000),
    "Year_Built": (1900, CURRENT_YEAR),
    "Price_PKR": (500_000, 1_000_000_000),   # removes 5,000,000,000 / 9,999,999,999 placeholders
}

NUMERIC_TEXT_COLS = list(VALID_RANGES)                    # messy text -> numbers
COUNT_COLS = ["Bedrooms", "Bathrooms", "Floors", "Garage"]
YES_NO_COLS = ["Furnished", "Corner_Property", "Park_Facing"]
TEXT_COLS = ["City", "Location", "Condition", "Property_Type"]

ACRONYMS = {"Dha": "DHA", "Pechs": "PECHS", "Pwd": "PWD"}   # fixed after Title Case

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("etl")


# --------------------------------------------------------------------------- #
# EXTRACT
# --------------------------------------------------------------------------- #
def extract(path: Path) -> pd.DataFrame:
    """Read the raw file. dtype=str keeps values like '9159 sqft' or '1,996' intact."""
    df = pd.read_csv(path, dtype=str)
    log.info(f"[Extract]   {len(df):,} rows, {df.shape[1]} columns read from {path.name}")
    return df


# --------------------------------------------------------------------------- #
# TRANSFORM  (one small function per job)
# --------------------------------------------------------------------------- #
def parse_number(series: pd.Series) -> pd.Series:
    """'1,996' -> 1996, '9159 sqft' -> 9159, ' 82700000 ' -> 82700000, '-' -> NaN."""
    text = series.astype("string").str.replace(",", "", regex=False)
    return pd.to_numeric(text.str.extract(r"(-?\d+(?:\.\d+)?)")[0], errors="coerce")


def clean_text(series: pd.Series) -> pd.Series:
    """Trim, collapse repeated spaces, and use consistent Title Case."""
    text = series.astype("string").str.strip().str.replace(r"\s+", " ", regex=True)
    text = text.str.lower().str.split().str.join(" ")
    text = text.map(lambda s: s if pd.isna(s) else s.title().replace("'S", "'s"), na_action="ignore")
    for wrong, right in ACRONYMS.items():
        text = text.str.replace(rf"\b{wrong}\b", right, regex=True)
    return text


def to_flag(series: pd.Series) -> pd.Series:
    """'Yes'/'yes'/'YES' -> 1, 'no' -> 0, anything else -> missing."""
    return series.astype("string").str.strip().str.lower().map({"yes": 1, "no": 0}).astype("Int8")


def fill_with_median(df: pd.DataFrame, col: str, group_by: list[str] | None = None) -> None:
    """Fill gaps with the median of the same group (falls back to the overall median)."""
    overall = df[col].median()
    if group_by:
        df[col] = df[col].fillna(df.groupby(group_by)[col].transform("median"))
    df[col] = df[col].fillna(overall)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    rows_in = len(df)

    # 1. Numbers stored as messy text -> real numbers
    for col in NUMERIC_TEXT_COLS + COUNT_COLS:
        df[col] = parse_number(df[col])

    # 2. Impossible values -> missing (0 sqft, year 3000, 9,999,999,999 PKR ...)
    for col, (low, high) in VALID_RANGES.items():
        invalid = df[col].notna() & ~df[col].between(low, high)
        if invalid.any():
            log.info(f"[Transform] {invalid.sum():>4} invalid {col} values set to missing")
        df.loc[invalid, col] = pd.NA

    # 3. Text columns and Yes/No columns
    for col in TEXT_COLS:
        df[col] = clean_text(df[col])
    for col in YES_NO_COLS:
        df[col] = to_flag(df[col])

    # 4. Remove duplicates (after cleaning, so ' Lahore' and 'lahore' count as equal)
    before = len(df)
    df = df.drop_duplicates().drop_duplicates(subset="ID", keep="first")
    log.info(f"[Transform] {before - len(df):>4} duplicate rows removed")

    # 5. Price is the value we want to predict, so rows without it are useless
    before = len(df)
    df = df.dropna(subset=["Price_PKR"])
    log.info(f"[Transform] {before - len(df):>4} rows dropped (no valid price)")

    # 6. Recover missing City from Location (each location belongs to one city)
    city_of_location = df.dropna(subset=["City"]).groupby("Location")["City"].agg(lambda s: s.mode()[0])
    missing_city = df["City"].isna()
    df.loc[missing_city, "City"] = df.loc[missing_city, "Location"].map(city_of_location)
    log.info(f"[Transform] {missing_city.sum() - df['City'].isna().sum():>4} missing cities recovered from Location")

    # 7. New features (calculated from real values only, before any filling)
    df["Price_Per_SqFt"] = (df["Price_PKR"] / df["Area_SqFt"]).round(2)
    df["Property_Age"] = CURRENT_YEAR - df["Year_Built"]

    # 8. Fill remaining gaps in numeric columns with medians
    fill_with_median(df, "Area_SqFt", group_by=["City", "Property_Type"])
    for col in ["Year_Built", *COUNT_COLS]:
        fill_with_median(df, col)

    # 9. Final tidy types
    df = df.dropna(subset=["City"])  # only rows whose city could not be recovered
    int_cols = ["ID", "Area_SqFt", "Year_Built", "Price_PKR", *COUNT_COLS]
    df[int_cols] = df[int_cols].round().astype("int64")
    df["Property_Age"] = df["Property_Age"].astype("Int64")
    df = df.sort_values("ID").reset_index(drop=True)

    log.info(f"[Transform] {rows_in:,} rows in -> {len(df):,} rows out")
    return df


# --------------------------------------------------------------------------- #
# VALIDATE  (fail loudly if the output is not what we expect)
# --------------------------------------------------------------------------- #
def validate(df: pd.DataFrame) -> None:
    assert df["ID"].is_unique, "Duplicate IDs found"
    assert df["Price_PKR"].between(*VALID_RANGES["Price_PKR"]).all(), "Price out of range"
    assert df["Area_SqFt"].between(*VALID_RANGES["Area_SqFt"]).all(), "Area out of range"
    assert df[["City", "Location", "Condition", "Property_Type"]].notna().all().all(), "Missing text values"
    log.info("[Validate] all checks passed")


# --------------------------------------------------------------------------- #
# LOAD
# --------------------------------------------------------------------------- #
def load(df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "houses_clean.csv"
    df.to_csv(csv_path, index=False)

    db_path = output_dir / "houses.db"
    with sqlite3.connect(db_path) as conn:
        df.to_sql("houses", conn, if_exists="replace", index=False)

    log.info(f"[Load]      {csv_path}")
    log.info(f"[Load]      {db_path} (table: houses)")


# --------------------------------------------------------------------------- #
# MAIN
# --------------------------------------------------------------------------- #
def main() -> None:
    parser = argparse.ArgumentParser(description="ETL for the Pakistan house price dataset")
    here = Path(__file__).resolve().parent   # folder that contains this script
    parser.add_argument("--input", type=Path,
                        default=here / "pakistan house prediction dataset.csv")
    parser.add_argument("--output-dir", type=Path, default=here / "output")
    args = parser.parse_args()

    raw = extract(args.input)
    clean = transform(raw)
    validate(clean)
    load(clean, args.output_dir)

    print("\nSample of the cleaned data:")
    print(clean.head().to_string(index=False))


if __name__ == "__main__":
    main()