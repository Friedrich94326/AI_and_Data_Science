""" A perceptron is an artificial neuron that can make a simple decision, having 3 main components- Inputs, Weights, and Output """


# Represeting a perception (a class takes two inputs and a pre-defined weight)
class Perceptron:
  def __init__(self, num_inputs = 2, weights = [1, 1]):
    self.num_inputs = num_inputs
    self.weights = weights
    
  def weighted_sum(self, inputs): # weighted sum method
    weighted_sum = 0
    for i in range(self.num_inputs):
      # complete this loop
      weighted_sum += inputs[i] * self.weights[i]
    return weighted_sum
  
  def activation(self, weighted_sum): # .activation() method is set to Sign Activation Function
    if weighted_sum >= 0:
      return 1
    else:
      return -1
    
  def training(self, training_set): # Training Error
    for inputs in training_set:
      prediction = self.activation(self.weighted_sum(inputs))
      actual = training_set[inputs]
      error = actual - prediction
      



# Step 1: Weighted Sum
  
cool_perceptron = Perceptron()

print(cool_perceptron.weighted_sum([24, 55])) #  the weighted sum for the inputs [24, 55]

# Step 2: Activation Function: Special functions that transform the weighted sum into a desired and constrained output

print(cool_perceptron.activation(52))


# Training the Perceptron
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import random

def generate_training_set(num_points):
	x_coordinates = [random.randint(0, 50) for i in range(num_points)]
	y_coordinates = [random.randint(0, 50) for i in range(num_points)]
	training_set = dict()
	for x, y in zip(x_coordinates, y_coordinates):
		if x <= 45-y:
			training_set[(x,y)] = 1
		elif x > 45-y:
			training_set[(x,y)] = -1
	return training_set

training_set = generate_training_set(30)

x_plus = []
y_plus = []
x_minus = []
y_minus = []

for data in training_set:
	if training_set[data] == 1:
		x_plus.append(data[0])
		y_plus.append(data[1])
	elif training_set[data] == -1:
		x_minus.append(data[0])
		y_minus.append(data[1])
    
fig = plt.figure()
ax = plt.axes(xlim=(-25, 75), ylim=(-25, 75))

plt.scatter(x_plus, y_plus, marker = '+', c = 'green', s = 128, linewidth = 2)
plt.scatter(x_minus, y_minus, marker = '_', c = 'red', s = 128, linewidth = 2)

plt.title("Training Set")

plt.show()



