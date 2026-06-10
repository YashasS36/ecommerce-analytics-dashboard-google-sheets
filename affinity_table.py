import pandas as pd
import os

# Load fact table
df = pd.read_csv("../Outputs/Fact_Ecommerce.csv")

# Keep only required columns
basket = df[["Order_ID", "Product_Name"]]

# Group products by order
basket = basket.groupby("Order_ID")["Product_Name"].apply(list)

pairs = []

# Generate product pairs
for products in basket:
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            pairs.append((products[i], products[j]))

# Create DataFrame
affinity = pd.DataFrame(pairs, columns=["Product_A", "Product_B"])

# Count occurrences
affinity_table = affinity.value_counts().reset_index(name="Count")

# Save output
os.makedirs("../Outputs", exist_ok=True)

affinity_table.to_csv("../Outputs/Affinity_Table.csv", index=False)

print("\n===== AFFINITY TABLE CREATED =====")
print(affinity_table.head())