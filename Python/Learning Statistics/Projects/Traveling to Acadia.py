"""
Imagine you work at a travel agency and want to inform your customers 
of the best time to visit one of your favorite vacation locations, Acadia, Maine. 
In this project, you will use flower bloom data, and flight information to
recommend the best time of year for someone to make a trip to Maine.
"""

# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms

plt.figure(1)
plt.subplot(2, 1, 1)
#plt.subplots_adjust(hspace = 1)

plt.hist(flights, bins = 12, color = '#1B88E5', range = (0, 365), edgecolor = 'black')
plt.title("Frequency of Occurrence of Flights")
plt.xlabel('day of the year')
plt.ylabel('number of flights')


plt.subplot(2, 1, 2)
plt.hist(in_bloom, bins = 12, color = '#FF4F4C', range = (0, 365), edgecolor = 'black')
plt.title("Frequency of Blooming Flowers")
plt.xlabel('day of the year')
plt.ylabel('number of in-bloom flowers')



plt.right_layout() # prevents the labels from overlapping with the graphs
plt.show()
plt.close('all')
