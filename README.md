# Data Science Internship Projects

A portfolio collection of applied analytics and data science case studies using Python, SQL, machine learning and visualization tools.

> **Portfolio honesty note:** This repository contains projects at different stages of completion. A project README describes its intended analysis; only mark a feature as implemented after its notebook/script/dashboard and outputs are present and verified.

## Featured projects
| Project | Focus | Status |
|---|---|---|
| [E-commerce Furniture Analysis](01_Ecommerce_Furniture_Analysis/) | Product pricing, sales volume and discount analysis | Cleaning script present; validate EDA, model and dashboard artifacts before claiming completion |
| [Netflix Data Analysis](03_Netflix_Data_Analysis/) | Content catalogue and release trends | Inspect notebook, source data and dashboard before publication |
| [Uber Trip Analysis](05_Uber_Trip_Analysis/) | Trip patterns and demand periods | Inspect analysis outputs and dashboard before publication |
| [EV Sales India Analysis](06_EV_Sales_India_Analysis/) | EV adoption and state/category trends | Inspect analysis outputs and dashboard before publication |

See the numbered project folders for the remaining case studies. The repository's project count is a collection size, not a claim that every project is production-complete.

## Tech stack
- Python: pandas, NumPy, Matplotlib, Seaborn, scikit-learn
- SQL: relational querying and analytical aggregation (where included)
- BI: Tableau dashboards (only where a working public link or packaged workbook is provided)

## Getting started
1. Clone this repository.
2. Open the project folder you want to run.
3. Read that project's README for its dataset, expected columns and steps.
4. Install only the dependencies listed for that project.
5. Run scripts from the documented command or notebook environment.

For the E-commerce Furniture cleaning script:
```bash
python -m pip install -r 01_Ecommerce_Furniture_Analysis/requirements.txt
python 01_Ecommerce_Furniture_Analysis/src/data_cleaning.py
```

The source dataset is not redistributed here unless explicitly included in the project folder. If absent, obtain it from its original source and place it at `01_Ecommerce_Furniture_Analysis/data/raw/ecommerce_furniture_dataset_2024.csv`.

## Reproducibility and quality standards
- Keep raw data unchanged; write derived files under `data/processed/`.
- Document dataset source, licence, date range, row count and column definitions.
- Explain missing-value handling and feature engineering.
- Use train/test separation and report appropriate metrics for any predictive model.
- Link only dashboards that are publicly accessible and contain no private data.
- Do not publish credentials, personal data or restricted datasets.

## Repository structure
Each project should ideally include:
```text
project_name/
├── data/
│   ├── raw/          # source files; large/private data excluded
│   └── processed/    # generated outputs
├── notebooks/        # exploration and modelling
├── src/              # reusable scripts
├── tableau/          # dashboard link or workbook
├── README.md         # objective, data, method, results and limitations
└── requirements.txt
```

## Author
Jayendra Karke · [GitHub](https://github.com/Jayendracoder)
