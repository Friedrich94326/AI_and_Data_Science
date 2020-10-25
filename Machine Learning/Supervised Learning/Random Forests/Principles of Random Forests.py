"""
A random forest is an ensemble machine learning technique — a random forest contains many decision trees that 
all work together to classify new points. When a random forest is asked to classify a new point, the random forest
gives that point to each of the decision trees. Each of those trees reports their classification and the random forest returns
the most popular classification. 
"""

"""
Random forests create different trees using a process known as bagging. 
Every time a decision tree is made, it is created using a different subset of the points in the training set.
"""

## Bagging- Those data points are chosen at random with replacement

from tree import build_tree, print_tree, car_data, car_labels
import random
random.seed(4)

tree = build_tree(car_data, car_labels)
#print_tree(tree)
#plot_tree(tree)


# indices contains 1000 random numbers between 0 and 1000
indices = []
for i in range(1000):
  indices.append(random.randint(0, 999))


data_subset = []
labels_subset = []

for index in indices:
  data_subset.append(car_data[index])
  labels_subset.append(car_labels[index])

subset_tree = build_tree(data_subset, labels_subset)
print(subset_tree)
print_tree(tree)




def find_best_split(dataset, labels):
    best_gain = 0
    best_feature = 0
    # to pick 3 features without replacement
    features = np.random.choice(len(dataset[0]), 3, replace = False)

    for feature in features:
        data_subsets, label_subsets = split(dataset, labels, feature)
        gain = information_gain(labels, label_subsets)
        if gain > best_gain:
            best_gain, best_feature = gain, feature
    return best_gain, best_feature
  
indices = [random.randint(0, 999) for i in range(1000)]

data_subset = [car_data[index] for index in indices]
labels_subset = [car_labels[index] for index in indices]

print("information gain and best feature to split on:")
print(find_best_split(data_subset, labels_subset))


## Plant a random forest

# The features are the price of the car, the cost of maintenance, the number of doors, the number of people the car can hold, the size of the trunk, and the safety rating
unlabeled_point = ['high', 'vhigh', '3', 'more', 'med', 'med']



# make 20 trees and record the prediction of each one
predictions = []
count = 0

for i in range(20):
  # making a decision tree
  indices = [random.randint(0, 999) for i in range(1000)]
  data_subset = [car_data[index] for index in indices]
  labels_subset = [car_labels[index] for index in indices]
  subset_tree = build_tree(data_subset, labels_subset)
  
  predictions.append( classify(unlabeled_point, subset_tree) )
  print("The unlabeled point is classified as '%s' by the %d-th subset tree." %(predictions[i], i) )
  count += 1

print("Review of the 20 predictions:")
print(predictions)

# find the most common one among the 20 predictions
final_prediction = max(predictions, key = predictions.count)
print("the final prediction is '%s'!" %final_prediction)



## Calculate the accuracy of both a single decision tree and a random forest

from tree import training_data, training_labels, testing_data, testing_labels, make_random_forest, make_single_tree, classify
import numpy as np
import random
np.random.seed(1)
random.seed(1)

tree = make_single_tree(training_data, training_labels)
forest = make_random_forest(40, training_data, training_labels) # 40 stands for the num of trees

single_tree_correct = 0
forest_correct = 0

for i in range(len(testing_data)):
  prediction = classify(testing_data[i], tree)
  if prediction == testing_labels[i]:
    single_tree_correct += 1

  predictions = []
  for forest_tree in forest:
    predictions.append( classify(testing_data[i], forest_tree) )
    
  forest_prediction = max(predictions, key = predictions.count)
  if forest_prediction == testing_labels[i]:
    forest_correct += 1

# the accuracy of a single tree
print(single_tree_correct / len(testing_data)) # 0.8815

# the accuracy of a random forest
print(forest_correct / len(testing_data)) # 0.9220

