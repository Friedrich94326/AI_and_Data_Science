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
