import codecademylib
import pandas as pd


# Adding a column
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

# add a new column that is the same for all rows in the DataFrame
df['Is taxed?'] = 'Yes'

# add a new column by performing a function on the existing columns
df['Margin'] = df['Price'] - df['Cost to Manufacture']

# the column that we want to add is related to existing columns, but requires a calculation more complex than multiplication or addition.
df['Lowercase Name'] = df.Name.apply(lower)

# Applying a Lambda to a column
# a lambda function mylambda that returns the first and last letters of a string
mylambda = lambda string: string[0] + string[-1]

print(mylambda('Unbreakable Will'))

mylambda = lambda age: 'Welcome to BattleCity!' if age >= 13 else 'You must be over 13'

df = pd.read_csv('employees.csv')

#  get_last_name which takes a string with someone’s first and last name
get_last_name = lambda String: String.split( )[-1]
df['last_name'] = df.name.apply(get_last_name)


df = pd.read_csv('employees.csv')
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)



# Renaming Columns
df = pd.read_csv('imdb.csv')
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']

# rename individual columns by using the .rename method
df.rename( columns = {
  'name': 'movie_title'},
  inplace = True    # Using inplace=True lets us edit the original DataFrame
)

print(orders.head(5))

orders['shoe_source'] = orders.shoe_material.apply(lambda x: 'animal' if x == 'leather' else 'vegan')
print(orders.head(5))

Salutation_by_gender = lambda row: 'Dear Mr. ' + row.last_name if gender == 'male' else 'Dear Ms. ' + row.last_name

orders['salutation'] = orders.apply(Salutation_by_gender, axis = 1)
print(orders.head(5))



