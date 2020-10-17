"""
An SVM uses support vectors to define a decision boundary. Classifications are made by comparing unlabeled points to that decision boundary.
Support vectors are the points of each class closest to the decision boundary.
"""

# Optimal Decision Boundaries
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from graph import ax, x_1, y_1, x_2, y_2

#Top graph intercept and slope
intercept_one = 98
slope_one = -20

x_vals = np.array(ax.get_xlim())
y_vals = intercept_one + slope_one * x_vals
plt.plot(x_vals, y_vals, '-')

#Bottom graph
ax = plt.subplot(2, 1, 2)
plt.title('Good Decision Boundary')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.scatter(x_1, y_1, color = "b")
plt.scatter(x_2, y_2, color = "r")

#Bottom graph intercept and slope
intercept_two = 8
slope_two = -.5

x_vals = np.array(ax.get_xlim())
y_vals = intercept_two + slope_two * x_vals
plt.plot(x_vals, y_vals, '-')

plt.tight_layout()
plt.show()



# Using Sklearn library
from sklearn.svm import SVC
from graph import points, labels

classifier = SVC(kernel = 'linear')
classifier.fit(points, labels)
print(classifier.predict([ [3, 4], [6, 7] ]))

# the effect of outliers on the boundary
import codecademylib3_seaborn
import matplotlib.pyplot as plt
from graph import points, labels, draw_points, draw_margin

# adding an outlier (labelled as a blue point) to the training set 
points.append([3, 3])
labels.append(0)

points.extend([ [4.3, 1.5], [7.2, 5.1], [9.0, 6.1] ])
labels.extend([0, 0, 1 ])

# The C parameter controls how much error is allowed.
# A large C allows for little error and creates a hard margin. A small C allows for more error and creates a soft margin.
classifier = SVC(kernel='linear', C =.24)
classifier.fit(points, labels)

draw_points(points, labels)
draw_margin(classifier)

plt.show()


# Kernels: Linearly Separable & Non-linearly Separable Dataset
# A kernel transforms the data into a higher dimension so it can be linearly separable.

from graph import points, labels
from sklearn.model_selection import train_test_split

training_data, validation_data, training_labels, validation_labels = train_test_split(points, labels, train_size = 0.8, test_size = 0.2, random_state = 100)


#classifier = SVC(kernel = 'linear')
classifier = SVC(kernel = 'poly', degree = 2)
classifier.fit(training_data, training_labels)

Avg_Accu = classifier.score(validation_data, validation_labels)
print("average accuracy of the model is around %.f%%" %(Avg_Accu* 100) )
# 43% for linear kernel: not linearly separable
# 100% for quadratic kernel


# Polynomial Kernel

from sklearn.datasets import make_circles

#Makes concentric circles
points, labels = make_circles(n_samples=300, factor=.2, noise=.05, random_state = 1)

#Makes training set and validation set.
training_data, validation_data, training_labels, validation_labels = train_test_split(points, labels, train_size = 0.8, test_size = 0.2, random_state = 100)

classifier = SVC(kernel = "linear", random_state = 1)
classifier.fit(training_data, training_labels)
print(classifier.score(validation_data, validation_labels))

print(training_data[0])

new_training = []
new_validation = []


for point in training_data:
  new_training_pt = [ 2 ** (1/2) * point[0] * point[1], point[0] ** 2, point[1] ** 2 ]
  new_training.append(new_training_pt)


for point in validation_data:
  new_validation_pt = [ 2 ** (1/2) * point[0] * point[1], point[0] ** 2, point[1] ** 2 ]
  new_validation.append(new_validation_pt)

# Retrain the model 'classifier' with new training data
classifier.fit(new_training, training_labels)

# validation process
New_Validation_Score = classifier.score(new_validation, validation_labels)
print(New_Validation_Score)




# Radial Basis Function Kernel

training_data, validation_data, training_labels, validation_labels = train_test_split(points, labels, train_size = 0.8, test_size = 0.2, random_state = 100)


classifier = SVC(kernel = 'rbf', gamma = 1)
# A higher gamma, say 100, will put more importance on the training data and could result in overfitting.
# Conversely, a lower gamma like 0.01 makes the points in the training data less relevant and can result in underfitting.
classifier.fit(training_data, training_labels)
#print("when gamma = 1, classifier's accuracy %.3f" % classifier.score(validation_data, validation_labels) )

for gamma in range(1, 11):
  classifier = SVC(kernel = 'rbf', gamma = gamma)
  classifier.fit(training_data, training_labels)
  print("when gamma = %d, classifier's accuracy is %.3f" %(gamma, classifier.score(validation_data, validation_labels) ) )

classifier = SVC(kernel = 'rbf', gamma = .1)
classifier.fit(training_data, training_labels)
print("when gamma = 0.1, classifier's accuracy is %.3f" %classifier.score(validation_data, validation_labels) )



