import pandas as pd
import os

# Load datasets
order_items = pd.read_csv("../Data/order_items.csv")
products = pd.read_csv("../Data/products.csv")

# Merge Order Items with Products
transformed = pd.merge(
    order_items,
    products,
    on="Product_ID",
    how="left"
)

# Calculate Revenue
transformed["Revenue"] = (
    transformed["Quantity"] * transformed["Price"]
)

# Create Outputs folder if it doesn't exist
os.makedirs("../Outputs", exist_ok=True)

# Save transformed dataset
transformed.to_csv(
    "../Outputs/Transformed_Ecommerce.csv",
    index=False
)

# Display results
print("\n===== TRANSFORMATION COMPLETED =====")
print(f"\nTotal Rows: {len(transformed)}")

print("\nColumns:")
print(list(transformed.columns))

print("\nPreview:")
print(transformed.head())

print("\nTransformed file saved successfully!")
print("Location: ../Outputs/Transformed_Ecommerce.csv")