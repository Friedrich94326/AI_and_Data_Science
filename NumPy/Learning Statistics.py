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





# Mean in NumPy
store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18,  9,  2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])


store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)

print("The average sales for store one is %.1f." %store_one_avg)
print("The average sales for store two is %.1f." %store_two_avg)
#print("The average sales for store two is " + str(store_two_avg))
print("The average sales for store one is %.1f." %store_three_avg)

# select stores of which average sales are greater than 7 bottles per week
best_seller = store_two



# use np.mean to calculate the percent of array elements that have a certain property

"""
explanation:
The logical statement survey_array > 8 evaluates which survey answers were greater than 8,
and assigns them a value of 1. np.mean adds all of the 1s up and divides them by the length
of survey_array. The resulting output tells us that 20% of responders purchased more than 8 
pounds of produce.
"""
class_year = np.array([1967, 1949, 2004, 1997, 1953,\
                       1950, 1958, 1974, 1987, 2006,\ 
                       2013, 1978, 1951, 1998, 1996,\
                       1952, 2005, 2007, 2003, 1955,\
                       1963, 1978, 2001, 2012, 2014,\
                       1948, 1970, 2011, 1962, 1966,\
                       1978, 1988, 2006, 1971, 1994,\
                       1978, 1977, 1960, 2008, 1965,\
                       1990, 2011, 1962, 1995, 2004,\
                       1991, 1952, 2013, 1983, 1955,\
                       1957, 1947, 1994, 1978, 1957,\
                       2016, 1969, 1996, 1958, 1994,\
                       1958, 2008, 1988, 1977, 1991,\
                       1997, 2009, 1976, 1999, 1975,\
                       1949, 1985, 2001, 1952, 1953,\
                       1949, 2015, 2006, 1996, 2015,\
                       2009, 1949, 2004, 2010, 2011,\
                       2001, 1998, 1967, 1994, 1966,\
                       1994, 1986, 1963, 1954, 1963,\
                       1987, 1992, 2008, 1979, 1987])

millennials = np.mean(class_year > 2005)
print("There are %.2f  percent of class years which are after 2005." %(millennials *100))


# Calculating the Mean of 2D Arrays
"""
we’ve provided data about a trial for a new allergy medication, AllerGeeThatSucks! Five participants were asked to rate how drowsy the medication made them once a day for three days on a scale of one (least drowsy) to ten (most drowsy)
"""

allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])



total_mean = np.mean(allergy_trials)

# the average level of drowsiness across each day of the experiment
trial_mean = np.mean(allergy_trials, axis = 1)

# the average level of drowsiness across for each individual patient 
patient_mean = np.mean(allergy_trials, axis = 0)

print("Total mean: %.2f" %total_mean)
print("Trial mean: %.2f" %trial_mean)
print("Patient mean: %.2f" %patient_mean)


# Outliers- Values that don’t fit within the majority of a dataset
temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88,\
                  87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93,\
                  90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90,\
                  99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87,\
                  87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

sorted_temps = np.sort(temps) # temps sorted in an increasing manner
print(sorted_temps)


# Median and Sorting
large_set = np.genfromtxt('household_income.csv', delimiter=',')

large_set_median = np.median(large_set)
print(large_set_median)


time_spent = np.genfromtxt('file.csv', delimiter=',')

print(time_spent)


minutes_mean = np.mean(time_spent)
print("Minutes_mean: %.2f" %minutes_mean)

minutes_median = np.median(time_spent)
print("Minutes_median: %.2f" %minutes_median)
best_measure = minutes_median

# Percentiles
patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])
thirtieth_percentile = np.percentile(patrons, 30)
seventieth_percentile = np.percentile(patrons, 70)
print("30th percentile: %.1f" %thirtieth_percentile)
print("70th percentile: %.1f" %seventieth_percentile)

# Interquartile range
movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])
first_quarter = np.percentile(movies_watched, 25)
third_quarter = np.percentile(movies_watched, 75)
interquartile_range = third_quarter - first_quarter 

print("1st quartile: %.1f" %first_quarter)
print("3rd quartile: %.1f" %third_quarter)
print("interquartile range: %.1f" %interquartile_range)

# Standard Deviation
pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_avg = np.mean(pumpkin)
acorn_squash_avg = np.mean(acorn_squash)

pumpkin_std = np.std(pumpkin)
acorn_squash_std = np.std(acorn_squash)




# convert numpy float to python float
#pumpkin_std = pumpkin_std.item()
#acorn_squash_std = acorn_squash_std.item()

winner = ""


if pumpkin_std > acorn_squash_std:
  winner += "pumpkin"
elif pumpkin_std < acorn_squash_std:
  winner += "acorn_squash"
else:
  winner += "even!"

print("The winner is " + winner + "!")




# Review
rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])


rain_mean = np.mean(rainfall)
rain_median = np.median(rainfall)
first_quarter = np.percentile(rainfall, 25)
third_quarter = np.percentile(rainfall, 75)
interquartile_range = third_quarter - first_quarter
rain_std = np.std(rainfall)



print("rain mean: %.2f" %rain_mean)
print("rain median: %.2f" %rain_median)
print("1st quartile: %.2f" %first_quarter)
print("3rd quartile: %.2f" %third_quarter)
print("interquartile range: %.2f" %interquartile_range)
print("rain std: %.2f" %rain_std)

