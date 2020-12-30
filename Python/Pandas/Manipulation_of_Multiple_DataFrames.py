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

sales_vs_targets = pd.merge(sales, targets)  # combine tables based on the columns that were the same between two tables
print(sales_vs_targets)



crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

# merging DataFrames one by one
men_women = pd.read_csv('men_women_sales.csv')
all_data = sales.merge(targets).merge(men_women)
print(all_data)
results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]



# Merging on Specific Columns
orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(orders, products.rename(columns = {'id': 'product_id'})) # use rename to merge two DataFrames whose columns don’t match
print(orders_products)

orders_products = pd.merge(
  orders,
  products,
  left_on = 'customer_id',
  right_on = 'id',
  suffixes = ['_orders', '_products']
)
print(orders_products)



# Mismatched Merge
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
print(products, orders)
merged_df = pd.merge(orders, products)
print(merged_df)
# when we merge two DataFrames whose rows don’t match perfectly, we lose the unmatched rows.



# Outer Merges (Outer Joins)
store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

# combine the data from both companies without losing the customers who are missing from one of the tables
# any missing values are filled in with None or nan
store_a_b_outer = pd.merge(store_a, store_b, how = 'outer')
print(store_a_b_outer)


# Left and Right Merges

# Store A wants to find out what products they carry that Store B does not carry
store_a_b_left = pd.merge(store_a, store_b, how = 'left')
print(store_a_b_left)


# Store B wants to find out what products they carry that Store A does not carry
store_b_a_left = pd.merge(store_b, store_a, how = 'left')
print(store_b_a_left)


# Concatenate DataFrames

"""
  to reconstruct a single DataFrame from multiple smaller DataFrames
  This method only works if all of the columns are the same in all of the DataFrames.
"""

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

menu = pd.concat([bakery, ice_cream]).reset_index()
print(menu)




visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])
print(visits, checkouts)


v_to_c = pd.merge(visits, checkouts)
v_to_c['time'] = v_to_c.checkout_time - \
                 v_to_c.visit_time
print(v_to_c)                 
print(v_to_c.time.mean())

