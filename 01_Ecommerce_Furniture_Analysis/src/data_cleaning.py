import pandas as pd
import numpy as np

# Load raw dataset
df = pd.read_csv("../data/raw/ecommerce_furniture_dataset_2024.csv")

# Make a copy
data = df.copy()

# Drop columns with too many missing values (if any)
if 'originalPrice' in data.columns:
    data.drop(columns=['originalPrice'], inplace=True)

# Clean price column
data['price'] = (
    data['price']
    .astype(str)
    .str.replace('$', '', regex=False)
    .astype(float)
)

# Clean sold column
data['sold'] = (
    data['sold']
    .astype(str)
    .str.replace('+', '', regex=False)
    .astype(int)
)

# Handle missing values
data.dropna(inplace=True)

# Feature Engineering: Discount Percentage
if 'originalPrice' in df.columns:
    data['discount_percentage'] = (
        (df['originalPrice'] - data['price']) / df['originalPrice']
    ) * 100
else:
    data['discount_percentage'] = 0

# Save cleaned data
output_path = "../data/processed/cleaned_furniture_data.csv"
data.to_csv(output_path, index=False)

print("✅ Cleaned dataset saved successfully!")

