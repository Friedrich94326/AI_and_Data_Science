from cars import training_points, training_labels, testing_points, testing_labels
from sklearn.tree import DecisionTreeClassifier

print(training_points[:5])
print(training_labels[:5])

classifier = DecisionTreeClassifier()

# import training data and corresponding labels
classifier.fit(training_points, training_labels)

# test the decision tree
predictions = classifier.predict(testing_points)
print("accuracy: %.3f " %classifier.score(testing_points, testing_labels))



# Prune the tree: Shrink the depth to avoid overfitting

classifier = DecisionTreeClassifier(random_state = 0)
classifier.fit(training_points, training_labels)
#print(classifier.score(testing_points, testing_labels))

# find the depth of the tree and its accuracy
print("depth of the tree: %d" %classifier.tree_.max_depth)
print("accuracy: %.3f%%" % (100* classifier.score(testing_points, testing_labels)) ) # 97.688%

# prune the tree by setting the depth to 11 instead
classifier = DecisionTreeClassifier(random_state = 0, max_depth = 11)
classifier.fit(training_points, training_labels)

print("accuracy: %.3f%%" % (100* classifier.score(testing_points, testing_labels)) ) # 98.266%


# Review
"""
Good decision trees have pure leaves. A leaf is pure if all of the data points in that class have the same label.
Decision trees are created using a greedy algorithm that prioritizes finding the feature that results in the largest information gain when splitting the data using that feature.
Creating an optimal decision tree is difficult. The greedy algorithm doesn’t always find the globally optimal tree.
Decision trees often suffer from overfitting. Making the tree small by pruning helps to generalize the tree so it is more accurate on data in the real world.

"""
