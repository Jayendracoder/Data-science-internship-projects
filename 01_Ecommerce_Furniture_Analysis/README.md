# E-commerce Furniture Listing Analysis

A reproducible analysis of a 2024 e-commerce furniture product-listing dataset. The project focuses on product pricing, listed units sold, discount availability, and shipping-label patterns.

## Business objective

Understand which listed products have the highest reported unit sales, how current prices are distributed, and what the available original-price and shipping fields can tell us.

## Dataset

**File:** `data/raw/ecommerce_furniture_dataset_2024.csv`

The source CSV contains 2,000 rows and five columns:

| Column | Description |
|---|---|
| `productTitle` | Product listing title |
| `originalPrice` | Original/list price when supplied; often blank |
| `price` | Current listed price, stored as text with currency symbols |
| `sold` | Reported units sold; stored as text |
| `tagText` | Shipping label or shipping charge text |

The dataset does **not** contain order dates, customer IDs, product categories, customer regions, profit, or transaction-level revenue. Accordingly, this project does not claim monthly trends, customer behaviour, category performance, or actual profit/revenue.

## Verified dataset snapshot

- 2,000 listing rows
- 1,793 distinct product titles
- 46,987 reported units sold in total (sum of the supplied `sold` field)
- 1,880 rows labelled `Free shipping`
- 117 rows with a paid-shipping label
- 3 rows with a blank or other shipping label
- 487 rows have both a usable original price and current price; 466 show a lower current price than original price

These are descriptive figures from the supplied file. The `sold` field is treated as a reported listing-level count, not as transaction-level order data.

## Project workflow

1. Load and inspect the raw CSV.
2. Standardize column names and clean currency and unit-count fields.
3. Preserve missing original prices as missing values.
4. Add transparent derived fields, including discount percentage where both prices are valid.
5. Export a cleaned CSV for analysis and Tableau.
6. Explore price distribution, units sold, top listings, discount availability, and shipping-label groups.
7. Record findings with their limitations.

## Repository structure

```text
01_Ecommerce_Furniture_Analysis/
├── data/
│   ├── raw/
│   │   └── ecommerce_furniture_dataset_2024.csv
│   └── processed/
├── notebooks/
│   └── ecommerce_furniture_analysis.ipynb
├── reports/
│   └── figures/
├── src/
│   ├── data_cleaning.py
│   ├── eda.py
│   └── model.py
├── tableau/
│   └── dashboard_link.txt
├── README.md
├── insights.md
└── requirements.txt
```

## Run locally

From this project directory:

```bash
python -m pip install -r requirements.txt
python src/data_cleaning.py
python src/eda.py
```

The cleaning script writes `data/processed/cleaned_furniture_data.csv`. The EDA script saves chart images under `reports/figures/`.

To work interactively, open `notebooks/ecommerce_furniture_analysis.ipynb` in Jupyter Notebook or VS Code.

## Tools

Python, pandas, NumPy, Matplotlib, and Jupyter.

## Modelling decision

No predictive model is claimed in this project. The available file is a cross-sectional product-listing snapshot without dates, customer/order records, or a clearly defined independent prediction target. A machine-learning model would not be justified without additional suitable data.

## Tableau

Use the processed CSV as the Tableau data source. The dashboard should use only supported fields: listed price, reported units sold, product title, discount percentage where available, and shipping group. Add the published dashboard URL to `tableau/dashboard_link.txt` after the dashboard is actually published.
