import pandas as pd
import os

# Load datasets
customers = pd.read_csv("../Data/customers.csv")
orders = pd.read_csv("../Data/orders.csv")
transformed = pd.read_csv("../Outputs/Transformed_Ecommerce.csv")

# Merge Orders with Customers
fact_table = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="left"
)

# Merge with Transformed Ecommerce Data
fact_table = pd.merge(
    fact_table,
    transformed,
    on="Order_ID",
    how="left"
)

# Save Fact Table
os.makedirs("../Outputs", exist_ok=True)

fact_table.to_csv(
    "../Outputs/Fact_Ecommerce.csv",
    index=False
)

print("\n===== FACT TABLE CREATED =====")
print(f"\nTotal Rows: {len(fact_table)}")

print("\nColumns:")
print(list(fact_table.columns))

print("\nPreview:")
print(fact_table.head())

print("\nFact table saved successfully!")
print("Location: ../Outputs/Fact_Ecommerce.csv")