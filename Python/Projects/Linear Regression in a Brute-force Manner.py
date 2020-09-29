# Part I: Calculating error

def get_y(m, b, x):  # vertical distance of a single point to a line
  return m*x + b
  
def calculate_error(m, b, point): # calculate the regression error of a single point
   x_point, y_point = point
   error = abs(get_y(m, b, x_point) - y_point) 
   return error
   
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]




# Part 2: Try a bunch of slopes and intercepts!

diff_m = 0.1
m_min = -10
m_max = 10
possible_ms = [ m_min + i *diff_m for i in range(int((m_max - m_min) / diff_m)) ]


b_min = -20
b_max = 20
diff_b = 0.1
possible_bs = [b_min + i * diff_b for i in range(int((b_max - b_min) / diff_b))]

smallest_error = float("inf")
best_m = 0
best_b = 0


Part 3: What does our model predict?

regression_data = [(m, b, calculate_all_error(m, b, datapoints))  for (m, b) in zip(possible_ms, possible_bs)]
total_errors = [total_error for (m, b, total_error) in regression_data]
for m in possible_ms:
    for b in possible_bs:
        total_error = calculate_all_error(m, b, datapoints)
        print("m = %.1f, b = %.1f, total error = %.1f" %(m, b, total_error))
        

for m in possible_ms:
    for b in possible_bs:
        total_error = calculate_all_error(m, b, datapoints)
        if (total_error == min(total_errors) ):
            smallest_error = total_error
            best_m = m
            best_b = b
            print("m = %.1f, b = %.1f, total error = %.1f" %(m, b, total_error))
            
