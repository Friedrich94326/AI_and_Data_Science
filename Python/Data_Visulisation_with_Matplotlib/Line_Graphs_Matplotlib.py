# Matplotlib is a Python library used to create charts and graphs

from matplotlib import pyplot as plt

# Basic Line Plot
days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12,10,14,22, 24]

plt.plot(days, money_spent)
plt.show() # display the result

# multiple line plots displayed on the same set of axes
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue) # revenue vs time
plt.plot(time, costs)
plt.show()

# Linestyles
# specify a different color for a line by using the keyword color with either an HTML color name or a HEX code
plt.plot(time, revenue, color = 'purple', linestyle = '--') # linestyle: dashed line, color = purple
plt.plot(time, costs, color = '#82edc9', marker = 's') #  HEX color #82edc9 and square ('s') markers
plt.show()


# Axis and Labels
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

plt.axis([0, 12, 2900, 3100])
# x-axis goes from 0 to 12, and the y-axis goes from 2900 to 3100
plt.show()


plt.xlabel('Time') # label the x-axis
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')

plt.show()


months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]


# a figure that has 1 row with 2 columns
plt.subplot(1, 2, 1)
plt.plot(months, temperature)

plt.subplot(1, 2, 2)
plt.plot(months, flights_to_hawaii, marker = '0')

plt.show()

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

"""
a figure having 2 rows of subplots:
  one subplot in the top row
  two subplots in the bottom row
"""

#x = [.96, .98, 1.00, 1.02, 1.04]
#y = x

# top plot
plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

# lower-left plot
plt.subplot(2, 2, 3)
plt.plot(x, parabola)

# lower-right plot
plt.subplot(2, 2, 4)
plt.plot(x, cubic)

# # Subplot Adjust: increase the spacing between horizontal subplots to 0.35 and the bottom margin to 0.2
plt.subplots_adjust(wspace = .35, bottom = .2)

# Display the result
plt.show()

# legend method takes a list with the labels to display


# label each line as we create it

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend here
legend_labels = ["Hyrule","Karariko", "Gerudo Valley"]
plt.legend(legend_labels)


plt.show()
