import pandas as pd
import os

# Load Fact Table
df = pd.read_csv("../Outputs/Fact_Ecommerce.csv")

# -------------------------
# KPIs
# -------------------------
total_revenue = df["Revenue"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()
aov = total_revenue / total_orders

# -------------------------
# Category Sales
# -------------------------
category_sales = df.groupby("Category")["Revenue"].sum().reset_index()

# -------------------------
# Top Products
# -------------------------
top_products = df.groupby("Product_Name")["Revenue"].sum().reset_index()
top_products = top_products.sort_values(by="Revenue", ascending=False)

# -------------------------
# Create Excel Report
# -------------------------
os.makedirs("../Outputs", exist_ok=True)

with pd.ExcelWriter("../Outputs/Ecommerce_Dashboard_Data.xlsx") as writer:
    
    df.to_excel(writer, sheet_name="Fact_Data", index=False)
    category_sales.to_excel(writer, sheet_name="Category_Sales", index=False)
    top_products.to_excel(writer, sheet_name="Top_Products", index=False)

    # KPI Sheet
    kpi = pd.DataFrame({
        "Metric": ["Total Revenue", "Total Orders", "Total Customers", "AOV"],
        "Value": [total_revenue, total_orders, total_customers, aov]
    })

    kpi.to_excel(writer, sheet_name="KPIs", index=False)

print("\n===== LOAD PROCESS COMPLETED =====")
print("\nKPIs:")
print(kpi)

print("\nExcel file created:")
print("Outputs/Ecommerce_Dashboard_Data.xlsx")