# Import packages
import numpy as np
import pandas as pd
from scipy import stats
from Matplotlib import pyplot as plt

# Read in housing data
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

"""
print("Brooklyn Price:")
print(brooklyn_price)
print("Manhattan Price:")
print(manhattan_price)
print("Queens Price:")
print(queens_price)
"""

# Add mean calculations below 
brooklyn_mean = np.average(brooklyn_price)
manhattan_mean = np.average(manhattan_price)
queens_mean = np.average(queens_price)




# Add median calculations below
brooklyn_median = np.median(brooklyn_price)
manhattan_median = np.median(manhattan_price)
queens_median = np.median(queens_price)


# Add mode calculations below

brooklyn_mode = stats.mode(brooklyn_price)
manhattan_mode = stats.mode(manhattan_price)
queens_mode = stats.mode(queens_price)






##############################################
##############################################
##############################################







# Don't look below here
# Mean
try:
    print("The mean price in Brooklyn is " + str(round(brooklyn_mean, 2)))
except NameError:
    print("The mean price in Brooklyn is not yet defined.")
try:
    print("The mean price in Manhattan is " + str(round(manhattan_mean, 2)))
except NameError:
    print("The mean in Manhattan is not yet defined.")
try:
    print("The mean price in Queens is " + str(round(queens_mean, 2)))
except NameError:
    print("The mean price in Queens is not yet defined.")
    
    
# Median
try:
    print("The median price in Brooklyn is " + str(brooklyn_median))
except NameError:
    print("The median price in Brooklyn is not yet defined.")
try:
    print("The median price in Manhattan is " + str(manhattan_median))
except NameError:
    print("The median price in Manhattan is not yet defined.")
try:
    print("The median price in Queens is " + str(queens_median))
except NameError:
    print("The median price in Queens is not yet defined.")
    
    
#Mode
try:
    print("The mode price in Brooklyn is " + str(brooklyn_mode[0][0]) + " and it appears " + str(brooklyn_mode[1][0]) + " times out of " + str(len(brooklyn_price)))
except NameError:
    print("The mode price in Brooklyn is not yet defined.")
try:
    print("The mode price in Manhattan is " + str(manhattan_mode[0][0]) + " and it appears " + str(manhattan_mode[1][0]) + " times out of " + str(len(manhattan_price)))
except NameError:
    print("The mode price in Manhattan is not yet defined.")
try:
    print("The mode price in Queens is " + str(queens_mode[0][0]) + " and it appears " + str(queens_mode[1][0]) + " times out of " + str(len(queens_price)))
except NameError:
    print("The mode price in Queens is not yet defined.")



# Sketch histograms for each dataset

# Histogram of Brooklyn price
plt.hist(brooklyn_price, range = (min(brooklyn_price), 20000), bins = 1000, edgecolor = 'black')
plt.title("Cost of one-bedroom apartments in Brooklyn")
plt.xlabel("cost")
plt.ylabel("count")
plt.axvline(brooklyn_mean, ymin = 0, ymax =  max(brooklyn_price), color = 'r', linestyle = 'solid', linewidth = 3, label = "Mean")
plt.axvline(brooklyn_median, ymin = 0, ymax =  max(brooklyn_price), color = 'y', linestyle = 'dotted', linewidth = 3, label = "Median")
plt.axvline(brooklyn_mode[0][0], ymin = 0, ymax =  max(brooklyn_price), color = 'g', linestyle = 'dashed', linewidth = 3, label = "Mode")
plt.legend()
plt.show()


# Histogram of Manhattan price
plt.hist(manhattan_price, range = (min(manhattan_price), 20000), bins = 1000, edgecolor = 'black')
plt.title("Cost of one-bedroom apartments in Manhattan")
plt.xlabel("cost")
plt.ylabel("count")
plt.axvline(manhattan_mean, ymin = 0, ymax =  max(manhattan_price), color = 'r', linestyle = 'solid', linewidth = 3, label = "Mean")
plt.axvline(manhattan_median, ymin = 0, ymax =  max(manhattan_price), color = 'y', linestyle = 'dotted', linewidth = 3, label = "Median")
plt.axvline(manhattan_mode[0][0], ymin = 0, ymax =  max(manhattan_price), color = 'g', linestyle = 'dashed', linewidth = 3, label = "Mode")
plt.legend()
plt.show()


# Histogram of Queens price
plt.hist(queens_price, range = (min(queens_price), 20000), bins = 1000, edgecolor = 'black')
plt.title("Cost of one-bedroom apartments in Queens")
plt.xlabel("cost")
plt.ylabel("count")
plt.axvline(queens_mean, ymin = 0, ymax =  max(queens_price), color = 'r', linestyle = 'solid', linewidth = 3, label = "Mean")
plt.axvline(queens_median, ymin = 0, ymax =  max(queens_price), color = 'y', linestyle = 'dotted', linewidth = 3, label = "Median")
plt.axvline(queens_mode[0][0], ymin = 0, ymax =  max(queens_price), color = 'g', linestyle = 'dashed', linewidth = 3, label = "Mode")
plt.legend()
plt.show()



#  Collection of the 3 plots in a figure
figNewYork = plt.figure()
figNewYork.suptitle('Central Tendency for Housing Data in New York', x = 1.5, y = 6.2, fontsize = 30)
plt.subplots_adjust(left = 0, bottom = 0, right = 3, top = 6, wspace = 1, hspace = 0.1)


ax1 = plt.subplot(3, 1, 1)
ax1.hist(brooklyn_price, range = (0, 20000), bins = 1000, edgecolor = 'black')
ax1.set_title("Cost of one-bedroom apartments in Brooklyn")
ax1.set_xlabel("cost")
ax1.set_ylabel("count")
ax1.axvline(brooklyn_mean, ymin = 0, ymax =  max(brooklyn_price), color = 'r', linestyle = 'solid', linewidth = 3, label = "Mean")
ax1.axvline(brooklyn_median, ymin = 0, ymax =  max(brooklyn_price), color = 'y', linestyle = 'dotted', linewidth = 3, label = "Median")
ax1.axvline(brooklyn_mode[0][0], ymin = 0, ymax =  max(brooklyn_price), color = 'g', linestyle = 'dashed', linewidth = 3, label = "Mode")
ax1.legend()

ax2 = plt.subplot(3, 1, 2)
ax2.hist(manhattan_price, range = (0, 20000), bins = 1000, edgecolor = 'black')
ax2.set_title("Cost of one-bedroom apartments in Manhattan")
ax2.set_xlabel("cost")
ax2.set_ylabel("count")
ax2.axvline(manhattan_mean, ymin = 0, ymax =  max(manhattan_price), color = 'r', linestyle = 'solid', linewidth = 3, label = "Mean")
ax2.axvline(manhattan_median, ymin = 0, ymax =  max(manhattan_price), color = 'y', linestyle = 'dotted', linewidth = 3, label = "Median")
ax2.axvline(manhattan_mode[0][0], ymin = 0, ymax =  max(manhattan_price), color = 'g', linestyle = 'dashed', linewidth = 3, label = "Mode")
ax2.legend()


ax3 = plt.subplot(3, 1, 3)
ax3.hist(queens_price, range = (0, 20000), bins = 1000, edgecolor = 'black')
ax3.set_title("Cost of one-bedroom apartments in Queens")
ax3.set_xlabel("cost")
ax3.set_ylabel("count")
ax3.axvline(queens_mean, ymin = 0, ymax =  max(queens_price), color = 'r', linestyle = 'solid', linewidth = 3, label = "Mean")
ax3.axvline(queens_median, ymin = 0, ymax =  max(queens_price), color = 'y', linestyle = 'dotted', linewidth = 3, label = "Median")
ax3.axvline(queens_mode[0][0], ymin = 0, ymax =  max(queens_price), color = 'g', linestyle = 'dashed', linewidth = 3, label = "Mode")
ax3.legend()



#OutputPath = 'Outputs/'
#plt.imsave(OutputPath + 'Central_Tendency_for_Housing_Data_in_NY.png', figNewYork)

plt.clf()
