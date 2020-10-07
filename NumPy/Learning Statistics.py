# construct and manipulate single-variable datasets


# import the desired package
import numpy as np

# NumPy arrays look like Python lists
test_1 = np.array([92, 94, 88, 91, 87])


# create an array from a CSV
test_2 = np.genfromtxt('test_2.csv', delimiter = ',')


# Element-wise Operations with NumPy Arrays

# The student’s grades on the third test are stored in the array test_3
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

# Give each student two extra points
test_3_fixed = test_3 + 2

# Arrays can also be added to or subtracted from each other in NumPy, assuming the arrays have the same number of elements
total_grade = test_1 + test_2 + test_3_fixed
final_grade = total_grade / 3
print(final_grade)


# Two-Dimensional Arrays
coin_toss = np.array([1, 0, 0, 1, 0])
coin_toss_again = np.array([[1, 0, 0, 1, 0], [0, 0, 1, 1, 1]])
#  the [] for the outer lists have to be attached


# same as normal python
jeremy_test_2 = test_2[-2]

# select from array[1] to array[2]
manual_adwoa_test_1 = test_1[1:3]

# Selecting Elements from a 2-D Array
tanya_test_3 = student_scores[2,0]
cody_test_scores = student_scores[:,-1]



# element-wise logical operations wihout using a for loop
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
cold = porridge[ porridge < 60]
hot = porridge [porridge > 80]
# & for 'and', | for 'or'
just_right = porridge[ ( porridge > 60 )  & ( porridge < 80)]
print(cold)
print(hot)
print(just_right)

# A Review
temperatures = np.genfromtxt('temperature_data.csv', delimiter = ',')
print(temperatures)

temperatures_fixed = temperatures + 3.0
monday_temperatures = temperatures_fixed[0,:]

thursday_friday_morning = temperatures_fixed[-2: , 1]
temperature_extremes = temperatures_fixed[ (temperatures_fixed < 50) | (temperatures_fixed > 60)]





