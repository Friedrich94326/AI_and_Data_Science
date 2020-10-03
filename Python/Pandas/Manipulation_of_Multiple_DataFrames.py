import codecademylib
import pandas as pd


orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

customers = pd.read_csv('customers.csv')

print(orders)
print(products)
print(customers)

# Inner Merging Multiple DataFrames
sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

# merging DataFrames one by one
men_women = pd.read_csv('men_women_sales.csv')
all_data = sales.merge(targets).merge(men_women)
print(all_data)
results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]


