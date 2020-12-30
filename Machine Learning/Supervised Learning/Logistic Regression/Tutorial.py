"""
Logistic Regression is a supervised machine learning algorithm that uses regression to predict the continuous probability, 
ranging from 0 to 1, of a data sample belonging to a specific category, or class. This act of deciding which of two classes
a data sample belongs to is called binary classification.

"""


# Intro

import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
from import hours_studied, passed_exam, math_courses_taken

# Scatter plot of exam passage vs number of hours studied
plt.scatter(hours_studied.ravel(), passed_exam, color='black', zorder=20)
plt.ylabel('passed/failed')
plt.xlabel('hours studied')

plt.show()


# Linear Regression Approach

from sklearn.linear_model import LinearRegression
from plotter import plot_data

# Create linear regression model
model = LinearRegression()
model.fit(hours_studied,passed_exam)

# Plug sample data into fitted model
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
probability = model.predict(sample_x).ravel()

# Function to plot exam data and linear regression curve
plot_data(model)

# Show the plot
plt.show()

# Define studious and slacker here
slacker = -0.15
studious = 1.1


# Logistic Regression

# Create logistic regression model
model = LogisticRegression()
model.fit(hours_studied,passed_exam)

# Plug sample data into fitted model
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
probability = model.predict_proba(sample_x)[:,1]

# Function to plot exam data and logistic regression curve
plot_data(model)

# Show the plot
plt.show()

# Lowest and highest probabilities
lowest = 0.0
highest = 1.0


# Log-Odds

from exam import hours_studied, calculated_coefficients, intercept

# Create your log_odds() function here
def log_odds(features, coefficients, intercept):
  return np.dot(features, coefficients) + intercept

# Calculate the log-odds for the Codecademy University data here
calculated_log_odds = log_odds(hours_studied, calculated_coefficients, intercept)
print(calculated_log_odds)



# Sigmoid Function
from exam import calculated_log_odds


