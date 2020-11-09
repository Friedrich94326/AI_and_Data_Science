""" The World Health Organization (WHO)’s Global Health Observatory (GHO) data repository tracks life expectancy 
for countries worldwideby following health status and many other related factors. This dataset covers a variety 
of indicators for all countries from 2000 to 2015 including:
  1. immunization factors
  2. mortality factors
  3. economic factors
  4. social factors
  5. other health-related factors 
In this project, I will design, train, and evaluate a neural network model performing the task of regressionto predict 
the life expectancy of countries using this dataset.  
"""


import pandas as pd

dataset = pd.read_csv('life_expectancy.csv')

print(dataset.head())
print(dataset.columns)
# observe the summary statistics of the data
print(dataset.describe())

# Drop the 'Country' column to learn a general pattern for all the countries
dataset = dataset.drop(['Country'], axis = 1)
print(dataset.head())
print(dataset.columns)

# labels: the last column of data
labels = dataset.iloc[:, -1]

# features: the remaining columns of data
features = dataset.iloc[:, ]
