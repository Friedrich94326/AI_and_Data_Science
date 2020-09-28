# double the nums
nums = [4, 8, 15, 16, 23, 42]
wrong_double_nums = 2*nums   #wrong_double_nums = [4, 8, 15, 16, 23, 42, 4, 8, 15, 16, 23, 42]
double_nums = [2*num for num in nums]

# squaring the nums
nums = range(11)
squares = [num**2 for num in nums]

# add ten to each element in a list
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num + 10 for num in nums]

# divide by two 
nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [ num / 2 for num in nums]

# odd or even
nums = [4, 8, 15, 16, 23, 42]
parity = [ num % 2 for num in nums ]

# Hello, ***!
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + name for name in names]

# pick the first character in a name
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]

# length of each name in a list of names
names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]

# flip the value of each boolean
booleans = [True, False, True]
opposite = [not boolean for boolean in booleans]

# string comparison
names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name == "Jerry" for name in names]

# number comparison
nums = [5, -10, 40, 20, 0]
greater_than_two = [ num > 2 for num in nums]

# access multiple items in those sub-lists
nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [item1 * item2 for (item1, item2) in nested_lists]

# compare the first item to the second
nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [item1 > item2 for (item1, item2) in nested_lists]

# list contains the first element in each sublist of a nested list
nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [item1 for (item1, item2) in nested_lists]

# add with zip()
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

nested_ab = zip(a, b)
sums = [item1 + item2 for (item1, item2) in nested_ab]
print(sums)

# divide with zip()
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

quotients = [b_i / a_i for (a_i, b_i) in zip(a, b)]

# "capital, country" by list comprehension
capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]

locations = [ capital + ", " + country for (capital, country) in zip(capitals, countries) ]
print(locations)

# "Name: name, Age: age"
names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]

users = ["Name: " + name + ", Age: " + str(age) for (name, age) in zip(names, ages)]

# greater than with zip()
a = [30, 42, 10]
b = [15, 16, 17]

greater_than = [a_i > b_i for (a_i, b_i) in zip(a, b)]

