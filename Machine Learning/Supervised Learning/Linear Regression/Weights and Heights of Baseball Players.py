import codecademylib3_seaborn
from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")



X = df["height"]
y = df["weight"]

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

#Your step_gradient function here
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
  
#Your gradient_descent function here:
def gradient_descent(x, y, learning_rate, num_iterations):
  # initial guesses
  [b, m] = [0, 0]
  for i in range(num_iterations):
    b, m = step_gradient(b, m, x, y, learning_rate)
  return [b, m]

learning_rate = 0.0001
num_iterations = 1000

b, m = gradient_descent(X, y, learning_rate, num_iterations)
y_predictions = [m*x + b for x in X]


# visualisation of regression
plt.plot(X, y, 'o')
plt.plot(X, y_predictions, color = 'red')
plt.xlabel('weight (kg)')
plt.ylabel('height (cm)')
plt.title('Baseball Players')

plt.show()
