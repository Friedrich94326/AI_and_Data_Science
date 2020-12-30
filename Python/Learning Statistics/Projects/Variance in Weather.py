import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data


print(london_data.head())
# check how many rows in the data frame
print(len(london_data)) 

temp = london_data['TemperatureC']
print(type(temp))
average_temp = np.average(temp)
print("Average temperature in Londoon in 2015 is %.2f degrees Celsius." % average_temp)

temperature_var = np.var(temp)
print("Variance of temperature in London in 2015 is %.2f square of degrees Celsius." %temperature_var)

temperature_standard_deviation = np.std(temp)
print("Standard deviation of temperature in London in 2015 is %.2f degrees Celsius." %temperature_standard_deviation)

# Filtering by month
print(london_data.head())
# take columns "month" and "TemperatureC" into account

# filter by the "month" column
June = london_data.loc[ london_data["month"] == 6 ] ["TemperatureC"]
#print(June)
#print(type(June))
avg_temp_June = np.mean(June)
print("Average temperature in London in June 2015 is %.2f degrees Celsius" %avg_temp_June)
std_temp_June = np.std(June)
print("STD of temperature in London in June 2015 is %.2f degrees Celsius" %std_temp_June)


July = london_data.loc[ london_data["month"] == 7] ["TemperatureC"]
avg_temp_July = np.mean(July)
print("Average temperature in London in July 2015 is %.2f degrees Celsius" %avg_temp_July)
std_temp_July = np.std(July)
print("STD of temperature in London in July 2015 is %.2f degrees Celsius" %std_temp_July)


# quickly see the mean and standard deviation of every month
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")



