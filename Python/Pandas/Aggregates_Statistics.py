import codecademylib
import pandas as pd
import numpy as np


orders = pd.read_csv('orders.csv')
print(orders.head(10))
most_expensive = max(orders.price)
num_colors = orders.shoe_color.nunique()  # the number of different colors of shoes we are selling


# Calculating Aggregate Functions

orders = pd.read_csv('orders.csv')
pricey_shoes = orders.groupby('shoe_type').price.max()
# the most expensive shoe for each shoe_type
print(pricey_shoes)
print(type(pricey_shoes))



pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
#print(pricey_shoes.head(10))
print(type(pricey_shoes))


#  calculate the 25th percentile for shoe price for each shoe_color
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
print(cheap_shoes)

# group by more than one column by passing a list of column names into the groupby method
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
print(shoe_counts)
print(type(shoe_counts))

# Create a pivot table
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
shoe_counts_pivot = shoe_counts.pivot(
    columns = 'shoe_color',
    index = 'shoe_type',
    values = 'id'  
).reset_index()  # a pivot table is a dataframe, providing a great way to compare data across two dimensions
print(shoe_counts_pivot)




# the following is a review
user_visits = pd.read_csv('page_visits.csv')

print(user_visits.head())

# calculate how many visits came from each of the different sources
click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source)

click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()
clikc_source_by_month_pivot = click_source_by_month.pivot(
    columns = 'month',
    index = 'utm_source',
    values = 'id').reset_index()












