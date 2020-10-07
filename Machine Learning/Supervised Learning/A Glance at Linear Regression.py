x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0
y_predicted1 = [m1 * x_i + b1 for x_i in x]
total_loss1 = 0
for i in range(len(x)):
  total_loss1 += ( y_predicted1[i] - y[i]  ) **2
print("total_loss1 = %d" %(total_loss1))

#y = 0.5x + 1
m2 = 0.5
b2 = 1
y_predicted2 = [m2 * x_i + b2 for x_i in x]
total_loss2 = 0
for i in range(len(x)):
  total_loss2 += ( y_predicted2[i] - y[i]  ) **2
print("total_loss2 = %d" %(total_loss2))

if total_loss1 < total_loss2:
  better_fit = 1
elif total_loss1 > total_loss2:
  better_fit = 2
else:
  better_fit = "even!"
  
  
  
# Gradient Descent for Intercept b

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

# Gradient Descent for Slope m

def get_gradient_at_m(x, y, b, m):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += x_val * (y_val - ((m * x_val) + b))
    m_gradient = -2/N * diff
    return m_gradient
    
 

def step_gradient(x, y, b_current, m_current):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (0.01 * b_gradient)   # learning rate is set to 0.01
    m = m_current - (0.01 * m_gradient)
    return [b, m]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0

# new intercept and slope guesses
b, m = step_gradient(months, revenue, b, m)
print(b, m)





 
