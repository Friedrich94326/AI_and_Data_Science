import codecademylib
from matplotlib import pyplot as plt
import numpy as np


# Bar Chart

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]
x_values = range(len(sales))
plt.bar(x_values, sales)
plt.show()



drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]
plt.bar(range(len(drinks)), sales)
#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks, rotation = 30)  
ax.set_title('Drinks Sold in MatplotSip')
plt.show()

# Side-by-side Bars


drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#Paste the x_values code here
x_values = range(len(drinks))

# Sales 1 (blue bars)
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = .8 # Width of each bar
store1_x = [t*element + w*n for element in range(d)]

# Sales 2 (red bars)
n = 2  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = .8 # Width of each bar
store2_x = [t*element + w*n for element in range(d)]

# plot bar charts separately
ax = plt.subplot()
plt.bar(store1_x, sales1)
plt.bar(store2_x, sales2)

# display the result
plt.show()
plt.close('all')

# Stacked Bars
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
  
plt.bar(range(len(drinks)), sales1)
plt.bar(range(len(drinks)), sales2, bottom=sales1)
plt.legend(["Location 1", "Location 2"])

plt.show()




# Error Bars

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

plt.bar(range(len(drinks)), ounces_of_milk, yerr = error, capsize = 5)
plt.show()


# Fill Between- to create a shaded error region

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

y_lower = [ i - 0.1 * i for i in revenue] # lower bound of the expected revenue 
y_upper = [ i + 0.1 * i for i in revenue] # upper bound of the expected revenue 

plt.fill_between(months, y_lower, y_upper, alpha = .2) # the saded error
plt.plot(months, revenue)
plt.show()


# Pie Chart- display elements of a data set as proportions of a whole

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs)
plt.axis('equal')
plt.show()



# Pie Chart Labeling
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, autopct = '%.1f%%')
plt.axis('equal')
plt.legend(payment_method_names, loc = 0)
plt.show()



# Histogram
from script import sales_times

#create the histogram here
plt.hist(sales_times, bins=20) # sales_times has been loaded in as a list

plt.show()

# Multiple Histograms
from script import sales_times1
from script import sales_times2

plt.hist(sales_times1, bins = 20, alpha = .4, normed = True)
plt.hist(sales_times2, bins = 20, alpha = .4, nored = True)
# Normalize both the histograms so that we can compare the patterns between them despite the differences in sample size

plt.show()


