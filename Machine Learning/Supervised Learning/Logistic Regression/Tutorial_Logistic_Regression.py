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

def sigmoid(z):
  denominator = 1 + np.exp(-z)
  return 1 / denominator

probabilities = sigmoid(calculated_log_odds)
print(probabilities)


# Log-Loss Function

from exam import passed_exam, probabilities, probabilities_2

# Function to calculate log-loss
def log_loss(probabilities, actual_class):
  return np.sum(-(1/actual_class.shape[0])*(actual_class*np.log(probabilities) + (1-actual_class)*np.log(1-probabilities)))

# Print passed_exam here
print(passed_exam)
print(probabilities)

# Combine passed_exam, probabilities, probabilities_2

for i in range(len(passed_exam)):
  print(passed_exam[i], probabilities[i], probabilities_2[i])


# Calculate and print loss_1 here
loss_1 = log_loss(probabilities, passed_exam)
print(loss_1)

# Calculate and print loss_2 here
loss_2 = log_loss(probabilities_2, passed_exam)
print(loss_2)


# Classification Thresholding
from exam import hours_studied, calculated_coefficients, intercept

def log_odds(features, coefficients,intercept):
  return np.dot(features,coefficients) + intercept

def sigmoid(z):
    denominator = 1 + np.exp(-z)
    return 1/denominator

# Create predict_class() function here

def predict_class(features, coefficients, intercept, threshold):
  calculated_log_odds = log_odds(features, coefficients,intercept)
  probabilities = sigmoid(calculated_log_odds)
  #if np.any( probabilities >= threshold ):
  #  return 1
  #elif np.any( probabilities < threshold ):
  #  return 0
  
  # HINT
  return np.where( probabilities >= threshold, 1, 0)

# Make final classifications on Codecademy University data here

final_results = predict_class(hours_studied, calculated_coefficients, intercept, threshold = .5)
print(final_results)


