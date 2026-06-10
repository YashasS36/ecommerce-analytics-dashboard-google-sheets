import pandas as pd

customers = pd.read_csv("../Data/Customers.csv")

print(customers.columns)
print(customers.head())