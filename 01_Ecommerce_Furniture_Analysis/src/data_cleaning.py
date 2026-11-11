"""Clean the furniture dataset with explicit, reproducible transformations.

Run from any working directory:
    python 01_Ecommerce_Furniture_Analysis/src/data_cleaning.py
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_DIR / "data" / "raw" / "ecommerce_furniture_dataset_2024.csv"
DEFAULT_OUTPUT = PROJECT_DIR / "data" / "processed" / "cleaned_furniture_data.csv"


def parse_numeric(series: pd.Series) -> pd.Series:
    """Convert currency/count strings to numeric values without failing on bad rows."""
    cleaned = (
        series.astype("string")
        .str.replace(r"[$,]", "", regex=True)
        .str.replace(r"\+$", "", regex=True)
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce")


def clean_dataset(input_path: Path, output_path: Path) -> pd.DataFrame:
    if not input_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {input_path}. Add the source CSV to data/raw/ "
            "or pass --input with its location."
        )

    raw = pd.read_csv(input_path)
    if raw.empty:
        raise ValueError("The input dataset contains no rows.")

    data = raw.copy()
    required = {"price", "sold"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    data["price"] = parse_numeric(data["price"])
    data["sold"] = parse_numeric(data["sold"])

    if "originalPrice" in data.columns:
        data["originalPrice"] = parse_numeric(data["originalPrice"])
        valid_original = data["originalPrice"].gt(0)
        data["discount_percentage"] = (
            (data["originalPrice"] - data["price"]) / data["originalPrice"] * 100
        ).where(valid_original)
    else:
        data["discount_percentage"] = pd.NA

    # Retain optional descriptive fields; remove only rows unusable for core analysis.
    before = len(data)
    data = data.dropna(subset=["price", "sold"]).copy()
    data = data[(data["price"] >= 0) & (data["sold"] >= 0)].copy()
    removed = before - len(data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Input rows: {len(raw):,}")
    print(f"Output rows: {len(data):,}")
    print(f"Rows removed (invalid price/sold): {removed:,}")
    print(f"Saved cleaned data to: {output_path}")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    clean_dataset(args.input, args.output)


if __name__ == "__main__":
    main()
