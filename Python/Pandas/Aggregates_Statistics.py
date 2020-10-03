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


