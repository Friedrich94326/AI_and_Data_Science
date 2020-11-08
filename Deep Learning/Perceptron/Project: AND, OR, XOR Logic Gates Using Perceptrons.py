
""" Perceptrons can’t solve problems that aren’t linearly separable.
However, if you combine multiple perceptrons together, you now have a neural net that can solve these problems!
"""

import codecademylib3_seaborn
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product


""" Creating and visualizing AND Data """

data = [[0, 0], [1, 0], [0, 1], [1, 1]]
labels = [0, 0, 0, 1]

plt.scatter([point[0] for point in data], [point[1] for point in data], c = labels)
#plt.show()
plt.clf()

""" Building the Perceptron for AND gate """
labels_AND = [0, 0, 0, 1]
classifier = Perceptron(max_iter = 40) # by default: max_iter = 1000
classifier.fit(data, labels_AND)

print(classifier.score(data, labels_AND))
# accu = 1.0.  It shows that AND gate is linearly separable!

plt.scatter([point[0] for point in data], [point[1] for point in data], c = labels_AND)



""" Visualising the perceptron for AND gate with a heat map """

""" Given a list of points, this method returns the distance those points are from the decision boundary. The closer the number is to 0, the closer that point is to the decision boundary. """
print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]]) )  # distance [-1.  3.  1.]

print(classifier.decision_function([[0, 0.1], [0, 0.2]]) )  # distance [-0.8  -0.6]

x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
point_grid = list(product(x_values, y_values))

distances = classifier.decision_function(point_grid)
abs_distances = [abs(distance) for distance in distances]

distances_matrix = np.reshape(abs_distances, (len(x_values), len(y_values)))

heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)
plt.colorbar(heatmap) # will put a legend on the heat map
plt.title('Perceptron for AND gate')
plt.show()
plt.clf()



""" Building the Perceptron for XOR gate """
labels_XOR = [0, 1, 1, 0]
classifier = Perceptron(max_iter = 40) # by default: max_iter = 1000
classifier.fit(data, labels_XOR)

print(classifier.score(data, labels_XOR))
# accu = 0.5. It shows that XOR gate is not linearly separable

plt.scatter([point[0] for point in data], [point[1] for point in data], c = labels_XOR)




""" Visualising the perceptron for XOR gate with a heat map """

print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]]) )  # distance [-1.  3.  1.]

print(classifier.decision_function([[0, 0.1], [0, 0.2]]) )  # distance [-0.8  -0.6]

x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
point_grid = list(product(x_values, y_values))

distances = classifier.decision_function(point_grid)
abs_distances = [abs(distance) for distance in distances]

distances_matrix = np.reshape(abs_distances, (len(x_values), len(y_values)))

heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)
plt.colorbar(heatmap) # will put a legend on the heat map
plt.title('Perceptron for XOR gate')
plt.show()
plt.clf()

""" Building the Perceptron for OR gate """
labels_OR = [0, 1, 1, 1]
classifier = Perceptron(max_iter = 40) # by default: max_iter = 1000
classifier.fit(data, labels_OR)

print(classifier.score(data, labels_OR))
# accu = 1.0. It shows that OR gate is linearly separable

plt.scatter([point[0] for point in data], [point[1] for point in data], c = labels_OR)


""" Visualising the perceptron for AND gate with a heat map """
print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]]) )  # distance [-1.  3.  1.]

print(classifier.decision_function([[0, 0.1], [0, 0.2]]) )  # distance [-0.8  -0.6]

x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
point_grid = list(product(x_values, y_values))

distances = classifier.decision_function(point_grid)
abs_distances = [abs(distance) for distance in distances]

distances_matrix = np.reshape(abs_distances, (len(x_values), len(y_values)))

heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)
plt.colorbar(heatmap) # will put a legend on the heat map
plt.title('Perceptron for OR gate')
plt.show()
plt.clf()


"""
This is incredibly similar to logic gates. AND gates and OR gates can’t produce the output of XOR gates, 
but when you combine a few ANDs and ORs, you can make an XOR!
"""
