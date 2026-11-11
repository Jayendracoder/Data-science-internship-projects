"""Exploratory analysis for the cleaned furniture listing dataset.

Run after src/data_cleaning.py:
    python src/eda.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "processed" / "cleaned_furniture_data.csv"
FIGURE_DIR = PROJECT_DIR / "reports" / "figures"


def save_price_distribution(data: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(data["price"].dropna(), bins=40, edgecolor="white")
    ax.set(title="Distribution of Current Listed Prices", xlabel="Price", ylabel="Number of listings")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "price_distribution.png", dpi=160)
    plt.close(fig)


def save_top_products(data: pd.DataFrame) -> None:
    top = (
        data.groupby("productTitle", as_index=False)["sold"]
        .sum()
        .sort_values("sold", ascending=False)
        .head(10)
        .sort_values("sold")
    )
    labels = top["productTitle"].str.slice(0, 58)
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.barh(labels, top["sold"])
    ax.set(title="Top 10 Product Listings by Reported Units Sold", xlabel="Reported units sold", ylabel="")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "top_10_products_by_units_sold.png", dpi=160)
    plt.close(fig)


def save_shipping_mix(data: pd.DataFrame) -> None:
    counts = data["shipping_group"].value_counts().reindex(
        ["Free shipping", "Paid shipping", "Missing or other"], fill_value=0
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(counts.index, counts.values)
    ax.set(title="Shipping Label Mix", xlabel="Shipping group", ylabel="Number of listings")
    ax.tick_params(axis="x", rotation=12)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "shipping_label_mix.png", dpi=160)
    plt.close(fig)


def save_discount_distribution(data: pd.DataFrame) -> None:
    discounts = data["discount_percentage"].dropna()
    if discounts.empty:
        print("No valid discount records; skipping discount chart.")
        return
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(discounts, bins=30, edgecolor="white")
    ax.set(title="Discount Percentage Distribution (Eligible Listings)", xlabel="Discount (%)", ylabel="Number of listings")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "discount_distribution.png", dpi=160)
    plt.close(fig)


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned data not found: {DATA_FILE}. Run python src/data_cleaning.py first."
        )

    data = pd.read_csv(DATA_FILE)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    print("Dataset shape:", data.shape)
    print("Distinct product titles:", data["productTitle"].nunique())
    print("Reported units sold:", f"{data['sold'].sum():,.0f}")
    print("Median listed price:", f"{data['price'].median():,.2f}")
    print("\nShipping groups:")
    print(data["shipping_group"].value_counts(dropna=False))
    print("\nTop 10 products by reported units sold:")
    print(
        data.groupby("productTitle")["sold"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .to_string()
    )

    save_price_distribution(data)
    save_top_products(data)
    save_shipping_mix(data)
    save_discount_distribution(data)
    print(f"Charts saved to: {FIGURE_DIR}")


if __name__ == "__main__":
    main()
