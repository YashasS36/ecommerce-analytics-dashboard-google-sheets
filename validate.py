import pandas as pd

# Read CSV files
customers = pd.read_csv("../Data/Customers.csv")
orders = pd.read_csv("../Data/Orders.csv")
order_items = pd.read_csv("../Data/Order_Items.csv")
products = pd.read_csv("../Data/Products.csv")

print("\n===== DATA VALIDATION REPORT =====\n")

# Check for missing values
print("Missing Values:")

print("\nCustomers:")
print(customers.isnull().sum())

print("\nOrders:")
print(orders.isnull().sum())

print("\nOrder Items:")
print(order_items.isnull().sum())

print("\nProducts:")
print(products.isnull().sum())

# Check duplicate IDs
print("\nDuplicate Records:")

print("Customer_ID duplicates:",
      customers["Customer_ID"].duplicated().sum())

print("Order_ID duplicates:",
      orders["Order_ID"].duplicated().sum())

print("Order_Item_ID duplicates:",
      order_items["Order_Item_ID"].duplicated().sum())

print("Product_ID duplicates:",
      products["Product_ID"].duplicated().sum())

# Check invalid prices
invalid_prices = products[products["Price"] <= 0]

print("\nInvalid Prices Found:", len(invalid_prices))

# Check invalid quantities
invalid_qty = order_items[order_items["Quantity"] <= 0]

print("Invalid Quantities Found:", len(invalid_qty))

print("\n===== VALIDATION COMPLETED =====")