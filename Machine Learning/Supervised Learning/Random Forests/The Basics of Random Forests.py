# Random forests create different trees using a process known as bagging. \
Every time a decision tree is made, it is created using a different subset of the points in the training set.

# Bagging

rom tree import build_tree, print_tree, car_data, car_labels
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
