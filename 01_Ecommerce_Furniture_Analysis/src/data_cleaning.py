"""Clean the raw furniture product-listing dataset.

Run from any working directory:
    python src/data_cleaning.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_DIR / "data" / "raw" / "ecommerce_furniture_dataset_2024.csv"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "cleaned_furniture_data.csv"

REQUIRED_COLUMNS = {"productTitle", "originalPrice", "price", "sold", "tagText"}


def parse_currency(series: pd.Series) -> pd.Series:
    """Convert currency-like strings such as '$1,294.04' to numeric values."""
    cleaned = (
        series.astype("string")
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce")


def parse_units_sold(series: pd.Series) -> pd.Series:
    """Convert unit-count strings (including comma separators and '+') to numbers."""
    cleaned = (
        series.astype("string")
        .str.replace("+", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce")


def main() -> None:
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw dataset not found: {RAW_FILE}")

    raw = pd.read_csv(RAW_FILE, encoding="utf-8-sig")
    raw.columns = raw.columns.str.strip()

    missing_columns = REQUIRED_COLUMNS.difference(raw.columns)
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing_columns)}")

    data = raw.copy()
    data["productTitle"] = data["productTitle"].astype("string").str.strip()
    data["price"] = parse_currency(data["price"])
    data["originalPrice"] = parse_currency(data["originalPrice"])
    data["sold"] = parse_units_sold(data["sold"])
    data["tagText"] = data["tagText"].astype("string").str.strip()

    # A row without a product title, current price, or units-sold value cannot
    # support the core listing analysis. Original price remains nullable.
    data = data.dropna(subset=["productTitle", "price", "sold"]).copy()
    data = data[(data["price"] >= 0) & (data["sold"] >= 0)].copy()

    data["shipping_group"] = np.select(
        [
            data["tagText"].eq("Free shipping"),
            data["tagText"].str.startswith("+Shipping:", na=False),
        ],
        ["Free shipping", "Paid shipping"],
        default="Missing or other",
    )

    eligible_discount = (
        data["originalPrice"].notna()
        & data["price"].notna()
        & data["originalPrice"].gt(0)
        & data["price"].gt(0)
    )
    data["discount_percentage"] = np.nan
    data.loc[eligible_discount, "discount_percentage"] = (
        (data.loc[eligible_discount, "originalPrice"] - data.loc[eligible_discount, "price"])
        / data.loc[eligible_discount, "originalPrice"]
        * 100
    )
    # Do not present price increases as discounts.
    data.loc[data["discount_percentage"] < 0, "discount_percentage"] = np.nan

    data["estimated_listed_value"] = data["price"] * data["sold"]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT_FILE, index=False)

    print("Cleaning completed successfully.")
    print(f"Input rows: {len(raw):,}")
    print(f"Output rows: {len(data):,}")
    print(f"Distinct product titles: {data['productTitle'].nunique():,}")
    print(f"Reported units sold: {data['sold'].sum():,.0f}")
    print(f"Rows with discount data: {data['discount_percentage'].notna().sum():,}")
    print(f"Saved cleaned data to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
