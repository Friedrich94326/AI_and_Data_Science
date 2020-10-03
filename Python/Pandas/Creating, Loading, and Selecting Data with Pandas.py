import codecademylib
import pandas as pd


# Create a DataFrame

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ["t-shirt", "t-shirt", "skirt", "skirt"],
  'Color': ["blue", "green", "red", "black"]
})

print(df1)


# add data using lists

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=[
    #add column names here
    'Store ID', 'Location', 'Number of Employees'
  ])

print(df2)

# Comma Separated Variables (CSV)

df = pd.read_csv('sample.csv')  # Read the CSV 'sample.csv' into a variable called df
print(df)



df = pd.read_csv('imdb.csv') 
print(df.head())   # .head() gives the first 5 rows of a DataFrame
print(df.info())  # df.info() gives some statistics for each column

# Select a single column
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df.clinic_north
print(type(clinic_north))
print(type(df))



# Selecting Multiple Columns from a DataFrame
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north_south = df[ ['clinic_north', 'clinic_south'] ]
print(type(clinic_north_south))

# Selecting a row
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march = df.iloc[2]  # When we select a single row, the result is a Series

# Selecting multiple rows
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

april_may_june = df.iloc[3:6]  # from row 3 to row 6 (not inclusive)
print(april_may_june)

# Select Rows with Logic
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

january = df[df.month == 'January'] 
"""
  select a subset of a DataFrame by using logical statements:
  df[df.MyColumnName == desired_column_value]
"""
print(january)

# combine multiple logical statements, as long as each statement is in parentheses
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march_april = df[(df.month == 'March') | (df.month == 'April')]



df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

january_february_march = df[df.month.isin( [ 'January', 'February', 'March'] )]
print(january_february_march)


# Setting indices
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

df2 = df.loc[[1, 3, 5]]

print(df2)
df3 = df2.reset_index(inplace = True, drop = True)
print(df3)


# Review
orders = pd.read_csv('shoefly.csv')
print(orders.head(5))

emails = orders.email

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

comfy_shoes = orders[ (orders.shoe_type == 'clogs') | (orders.shoe_type == 'boots') |(orders.shoe_type == 'ballet flats') ]

