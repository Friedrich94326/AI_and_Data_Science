# Set total equal to the sum
total = 0
ages = [29, 49, 42, 43]
for age in ages:
  total += age


# Set mean_value equal to the mean
mean_value = total / len(ages)
# The following code prints the total and mean
print("The sum total is equal to: " + str(total))
print("The mean value is equal to: " + str(mean_value))



# NumPy Average

# Import packages
import numpy as np
import pandas as pd

# Read author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Set author ages to a NumPy array
author_ages = greatest_books['Ages']


# Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)

print("The average age of the 100 greatest authors, according to a survey by Le Monde, is: " + str(average_age))



# Statistics with Matplotlib

# Import packages
import codecademylib

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
author_ages = greatest_books['Ages']

# Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)

print("The average age of the 100 greatest authors, according to Le Monde is: " + str(average_age))

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Novel Authors at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.legend()

plt.show()




# Median NumPy
# Read in author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save author ages to author_ages
author_ages = greatest_books['Ages']

# Use numpy to calculate the median age of the top 100 authors
median_age = np.median(author_ages)

print("The median age of the 100 greatest authors, according to a survey by Le Monde is: " + str(median_age))

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Novel Authors at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.axvline(median_age, color='y', linestyle='solid', linewidth=2, label="Median")
plt.legend()

plt.show()


# Mode
"""
The most frequently occurring observation in the dataset.
A dataset can have multiple modes if there is more than one value with the same maximum frequency.
"""

from scipy import stats

# Use numpy to calculate the mode age of the top 100 authors
mode_age = stats.mode(author_ages)

print("The mode age and its frequency of authors from Le Monde's 100 greatest books is: " + str(mode_age[0][0]) + " and " + str(mode_age[1][0]))

for i in range(1): # mode and its counted are contained 
  for j in [0]: # in this case we have only one mode
    print("mode_age[%d][%d] = %d \r\n" %(i, j, mode_age[i][j]))
    

    
# Calculate the average and median value of the author_ages array
average_age = np.average(author_ages)
median_age = np.median(author_ages)
mode_age = 38

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Author Ages at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=3, label="Mean")
plt.axvline(median_age, color='y', linestyle='dotted', linewidth=3, label="Median")
plt.axvline(mode_age, color='orange', linestyle='dashed', linewidth=3, label="Mode")
plt.legend()

plt.show()


