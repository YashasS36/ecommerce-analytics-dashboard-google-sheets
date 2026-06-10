import pandas as pd
import os

# Load fact table
df = pd.read_csv("../Outputs/Fact_Ecommerce.csv")

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Reference date (analysis date)
snapshot_date = df["Order_Date"].max()

# RFM calculation
rfm = df.groupby("Customer_ID").agg(
    Recency=("Order_Date", lambda x: (snapshot_date - x.max()).days),
    Frequency=("Order_ID", "nunique"),
    Monetary=("Revenue", "sum")
).reset_index()

# Save output
os.makedirs("../Outputs", exist_ok=True)

rfm.to_csv("../Outputs/RFM_Table.csv", index=False)

print("\n===== RFM TABLE CREATED =====")
print(rfm.head())