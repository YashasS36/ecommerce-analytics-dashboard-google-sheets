import pandas as pd

customers = pd.read_csv("../Data/Customers.csv")
orders = pd.read_csv("../Data/Orders.csv")
order_items = pd.read_csv("../Data/Order_Items.csv")
products = pd.read_csv("../Data/Products.csv")

print("Customers:", customers.shape)
print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
print("Products:", products.shape)