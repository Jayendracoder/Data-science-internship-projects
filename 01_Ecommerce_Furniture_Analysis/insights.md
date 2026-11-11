# Verified Findings — E-commerce Furniture Listing Analysis

The findings below are based on the supplied `ecommerce_furniture_dataset_2024.csv` file (2,000 rows).

## Dataset profile

- The file contains 2,000 product-listing rows and 5 fields.
- There are 1,793 distinct product titles, so some titles appear in more than one row.
- The supplied `sold` values sum to 46,987 reported units. This is a listing-level total, not verified transaction revenue or order count.

## Product demand

- The highest single listing-level `sold` value is 10,000 units, for the portable round folding chair listing.
- Other high-volume listings include a foldable adjustable reading stand (3,000 units in each of two rows) and a shoe rack listing (2,000 units).
- Repeated product titles exist. Analyses that aggregate by title should sum the reported units and clearly state that this combines rows with the same title.

## Pricing and discounts

- Current listed prices range from $0.99 to $2,876.38.
- The median current listed price is approximately $114.08.
- Original price is missing for 1,513 rows, so discount analysis cannot cover the full dataset.
- 487 rows have both a positive original price and positive current price. Of these, 466 have a lower current price than original price; 21 have equal values.
- The mean percentage reduction among those 466 discounted rows is approximately 49.34%. This is a simple unweighted row-level average, not a realized customer savings or margin estimate.

## Shipping labels

- 1,880 rows (94.0%) are labelled `Free shipping`.
- 117 rows contain a paid-shipping label.
- 3 rows have a blank or other shipping label.
- Paid shipping appears as many different dollar amounts; treating each amount as a separate category would make a chart difficult to interpret. Grouping into Free shipping / Paid shipping / Missing or other is more useful.

## Interpretation limits

The dataset does not include order dates, customer details, product categories, cost, profit, or transaction-level sales. Do not infer seasonality, customer behaviour, category-level performance, profit margins, or actual revenue from these fields alone.
