# Gini Impurity
from collections import Counter

labels = ["unacc", "unacc", "acc", "acc", "good", "good"]
#labels = ["unacc","unacc","unacc", "good", "vgood", "vgood"]
#labels = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc"]

impurity = 1
label_counts = Counter(labels)
print(label_counts)

for label in label_counts:
  probability_of_label = label_counts[label] / len(labels)
  impurity -=  probability_of_label ** 2

print(impurity)

# Information Gain
unsplit_labels = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc", "good", "good", "good", "good", "vgood", "vgood", "vgood"]

split_labels_1 = [
  ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc", "good", "good", "vgood"], 
  [ "good", "good"], 
  ["vgood", "vgood"]
]

split_labels_2 = [
  ["unacc", "unacc", "unacc", "unacc","unacc", "unacc", "good", "good", "good", "good"], 
  ["vgood", "vgood", "vgood"]
]

def gini(dataset):
  impurity = 1
  label_counts = Counter(dataset)
  for label in label_counts:
    prob_of_label = label_counts[label] / len(dataset)
    impurity -= prob_of_label ** 2
  return impurity

# calculuating the info gain of splitting laebls 1

info_gain = gini(unsplit_labels)
for subset in split_labels_1:
  info_gain -= gini(subset)

print("the information gain of splitting data 1 is %.4f" %info_gain)


# calculuating the info gain of splitting laebls 2

info_gain = gini(unsplit_labels)
for subset in split_labels_2:
  info_gain -= gini(subset)

print("the information gain of splitting data 2 is %.4f" %info_gain)

# The higher the information gain the better!!!



# Weighted Information Gain
car_data = [['med', 'low', '3', '4', 'med', 'med'], ['med', 'vhigh', '4', 'more', 'small', 'high'], \
        ['high', 'med', '3', '2', 'med', 'low'], ['med', 'low', '4', '4', 'med', 'low'],\
        ['med', 'low', '5more', '2', 'big', 'med'], ['med', 'med', '2', 'more', 'big', 'high'], \
        ['med', 'med', '2', 'more', 'med', 'med'], ['vhigh', 'vhigh', '2', '2', 'med', 'low'], \
        ['high', 'med', '4', '2', 'big', 'low'], ['low', 'low', '2', '4', 'big', 'med']]

car_labels = ['acc', 'acc', 'unacc', 'unacc', 'unacc', 'vgood', 'acc', 'unacc', 'unacc', 'good']

def split(dataset, labels, column):
    data_subsets = []
    label_subsets = []
    counts = list(set([data[column] for data in dataset]))
    counts.sort()
    for k in counts:
        new_data_subset = []
        new_label_subset = []
        for i in range(len(dataset)):
            if dataset[i][column] == k:
                new_data_subset.append(dataset[i])
                new_label_subset.append(labels[i])
        data_subsets.append(new_data_subset)
        label_subsets.append(new_label_subset)
    return data_subsets, label_subsets

def gini(dataset):
  impurity = 1
  label_counts = Counter(dataset)
  for label in label_counts:
    prob_of_label = label_counts[label] / len(dataset)
    impurity -= prob_of_label ** 2
  return impurity

def information_gain(starting_labels, split_labels):
  info_gain = gini(starting_labels)
  for subset in split_labels:
    # Multiply gini(subset) by the correct percentage below
    info_gain -= gini(subset) * (len(subset) / len(starting_labels))
  return info_gain

# split the data based on the third index (That feature was the number of people the car could hold)
# when we called split, we used 3 as the split index
split_data, split_labels = split(car_data, car_labels, 3)
print(split_data)
print("length of spliting data: %d" %len(split_data))
print(split_data[0])
print(split_data[1])

print("splitting labels:")
print(split_labels)

print("before splitting data:")
print(information_gain(car_labels, car_labels))
# -2.169999999999999

print("after splitting data:")
print(information_gain(car_labels, split_labels))
# 0.30666666666666675


# Loop through all of the features of our data to find the best one to split on
for idx in range(len(car_data[0])):
  split_data, split_labels = split(car_data, car_labels, idx)
  print("split data on feature %d" %idx)
  print(information_gain(car_labels, split_labels))
  print("\n")

# The number of people the car could hold (feature 3) produces the most information gain.


# Recursive Tree Building
def find_best_split(dataset, labels):
    best_gain = 0
    best_feature = 0
    for feature in range(len(dataset[0])):
        data_subsets, label_subsets = split(dataset, labels, feature)
        gain = information_gain(labels, label_subsets)
        if gain > best_gain:
            best_gain, best_feature = gain, feature
    return best_feature, best_gain


best_feature, best_gain = find_best_split(car_data, car_labels)
print("best feature: %d" %best_feature)
print("best_gain %.4f" %best_gain)


# recursive case: split the data into subsets using the best feature, and recursively call the build_tree() on those subsets to create subtrees

def build_tree(data, labels):
  print(data)
  best_feature, best_gain = find_best_split(data, labels)
  print("best feature: %d\n" %best_feature)
  
  if best_gain == 0:
    return Counter(labels)
  else:
    pass
  
  data_subsets, label_subsets = split(data, labels, best_feature)
  branches = []
  for i in range(len(data_subsets)):
    branches.append(build_tree(data_subsets[i], label_subsets[i]))

  return branches

tree = build_tree(car_data, car_labels)
print_tree(tree)

"""
Result presented as below:
Splitting
--> Branch 0:
  Counter({'unacc': 4})
--> Branch 1:
  Splitting
  --> Branch 0:
    Counter({'good': 1})
  --> Branch 1:
    Counter({'acc': 1})
  --> Branch 2:
    Counter({'unacc': 1})
--> Branch 2:
  Splitting
  --> Branch 0:
    Counter({'vgood': 1})
  --> Branch 1:
    Counter({'acc': 1})
  --> Branch 2:
    Counter({'acc': 1})
"""

# Classifying New Data

import operator

test_point = ['vhigh', 'low', '3', '4', 'med', 'med']

print_tree(tree)

def classify(datapoint, tree):
  # check if tree is a Leaf
  if isinstance(tree, Leaf): 
    return max(tree.labels.items(), key=operator.itemgetter(1))[0]
  # if tree is not a leaf
  else:
    pass

  # tree.feature contains the index of the feature that we’re splitting on
  value = datapoint[tree.feature]

  for branch in tree.branches:
    if value == branch.value:
      return value
    else:
      return classify(datapoint, branch)

print("The test point is classified as %s" %classify(test_point, tree)) # unacc


"""
Splitting on Estimated Saftey
--> Branch high:
  Splitting on Person Capacity
  --> Branch 2:
    Counter({'unacc': 174})
  --> Branch 4:
    Splitting on Buying Price
    --> Branch high:
      Splitting on Price of maintenance
      --> Branch high:
        Counter({'acc': 11})
      --> Branch low:
        Counter({'acc': 12})
      --> Branch med:
        Counter({'acc': 11})
      --> Branch vhigh:
        Counter({'unacc': 12})
    --> Branch low:
      Splitting on Price of maintenance
      --> Branch high:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 4})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'acc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'vgood': 1})
          --> Branch 5more:
            Counter({'vgood': 1})
        --> Branch small:
          Counter({'acc': 3})
      --> Branch low:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 3})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'good': 1})
          --> Branch 3:
            Counter({'good': 1})
          --> Branch 4:
            Counter({'vgood': 1})
          --> Branch 5more:
            Counter({'vgood': 1})
        --> Branch small:
          Counter({'good': 2})
      --> Branch med:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 3})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'good': 1})
          --> Branch 3:
            Counter({'good': 1})
          --> Branch 4:
            Counter({'vgood': 1})
          --> Branch 5more:
            Counter({'vgood': 1})
        --> Branch small:
          Counter({'good': 4})
      --> Branch vhigh:
        Counter({'acc': 9})
    --> Branch med:
      Splitting on Price of maintenance
      --> Branch high:
        Counter({'acc': 12})
      --> Branch low:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 4})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'good': 1})
          --> Branch 3:
            Counter({'good': 1})
          --> Branch 4:
            Counter({'vgood': 1})
          --> Branch 5more:
            Counter({'vgood': 1})
        --> Branch small:
          Counter({'good': 4})
      --> Branch med:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 3})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'acc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'vgood': 1})
          --> Branch 5more:
            Counter({'vgood': 1})
        --> Branch small:
          Counter({'acc': 4})
      --> Branch vhigh:
        Counter({'acc': 11})
    --> Branch vhigh:
      Splitting on Price of maintenance
      --> Branch high:
        Counter({'unacc': 11})
      --> Branch low:
        Counter({'acc': 12})
      --> Branch med:
        Counter({'acc': 12})
      --> Branch vhigh:
        Counter({'unacc': 10})
  --> Branch more:
    Splitting on Buying Price
    --> Branch high:
      Splitting on Price of maintenance
      --> Branch high:
        Splitting on Number of doors
        --> Branch 2:
          Splitting on Size of luggage boot
          --> Branch big:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch small:
            Counter({'unacc': 1})
        --> Branch 3:
          Counter({'acc': 3})
        --> Branch 4:
          Counter({'acc': 3})
        --> Branch 5more:
          Counter({'acc': 3})
      --> Branch low:
        Splitting on Number of doors
        --> Branch 2:
          Splitting on Size of luggage boot
          --> Branch big:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch small:
            Counter({'unacc': 1})
        --> Branch 3:
          Counter({'acc': 3})
        --> Branch 4:
          Counter({'acc': 3})
        --> Branch 5more:
          Counter({'acc': 3})
      --> Branch med:
        Splitting on Number of doors
        --> Branch 2:
          Splitting on Size of luggage boot
          --> Branch big:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch small:
            Counter({'unacc': 1})
        --> Branch 3:
          Counter({'acc': 3})
        --> Branch 4:
          Counter({'acc': 3})
        --> Branch 5more:
          Counter({'acc': 3})
      --> Branch vhigh:
        Counter({'unacc': 12})
    --> Branch low:
      Splitting on Price of maintenance
      --> Branch high:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 4})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'acc': 1})
          --> Branch 3:
            Counter({'vgood': 1})
          --> Branch 4:
            Counter({'vgood': 1})
          --> Branch 5more:
            Counter({'vgood': 1})
        --> Branch small:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
      --> Branch low:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 3})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'good': 1})
          --> Branch 4:
            Counter({'vgood': 1})
          --> Branch 5more:
            Counter({'vgood': 1})
        --> Branch small:
          Counter({'good': 3})
      --> Branch med:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 4})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'good': 1})
          --> Branch 4:
            Counter({'vgood': 1})
          --> Branch 5more:
            Counter({'vgood': 1})
        --> Branch small:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'good': 1})
          --> Branch 4:
            Counter({'good': 1})
          --> Branch 5more:
            Counter({'good': 1})
      --> Branch vhigh:
        Splitting on Number of doors
        --> Branch 2:
          Splitting on Size of luggage boot
          --> Branch big:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch small:
            Counter({'unacc': 1})
        --> Branch 3:
          Counter({'acc': 2})
        --> Branch 4:
          Counter({'acc': 3})
        --> Branch 5more:
          Counter({'acc': 2})
    --> Branch med:
      Splitting on Price of maintenance
      --> Branch high:
        Splitting on Number of doors
        --> Branch 2:
          Splitting on Size of luggage boot
          --> Branch big:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch small:
            Counter({'unacc': 1})
        --> Branch 3:
          Counter({'acc': 2})
        --> Branch 4:
          Counter({'acc': 2})
        --> Branch 5more:
          Counter({'acc': 2})
      --> Branch low:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 4})
        --> Branch med:
          Counter({'vgood': 3})
        --> Branch small:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'good': 1})
          --> Branch 5more:
            Counter({'good': 1})
      --> Branch med:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'vgood': 4})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'acc': 1})
          --> Branch 3:
            Counter({'vgood': 1})
          --> Branch 4:
            Counter({'vgood': 1})
          --> Branch 5more:
            Counter({'vgood': 1})
        --> Branch small:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
      --> Branch vhigh:
        Splitting on Number of doors
        --> Branch 2:
          Splitting on Size of luggage boot
          --> Branch big:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch small:
            Counter({'unacc': 1})
        --> Branch 3:
          Counter({'acc': 2})
        --> Branch 4:
          Counter({'acc': 2})
        --> Branch 5more:
          Counter({'acc': 3})
    --> Branch vhigh:
      Splitting on Price of maintenance
      --> Branch high:
        Counter({'unacc': 12})
      --> Branch low:
        Splitting on Number of doors
        --> Branch 2:
          Splitting on Size of luggage boot
          --> Branch big:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch small:
            Counter({'unacc': 1})
        --> Branch 3:
          Counter({'acc': 3})
        --> Branch 4:
          Counter({'acc': 3})
        --> Branch 5more:
          Counter({'acc': 1})
      --> Branch med:
        Splitting on Number of doors
        --> Branch 2:
          Splitting on Size of luggage boot
          --> Branch big:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch small:
            Counter({'unacc': 1})
        --> Branch 3:
          Counter({'acc': 3})
        --> Branch 4:
          Counter({'acc': 3})
        --> Branch 5more:
          Counter({'acc': 3})
      --> Branch vhigh:
        Counter({'unacc': 12})
--> Branch low:
  Counter({'unacc': 524})
--> Branch med:
  Splitting on Person Capacity
  --> Branch 2:
    Counter({'unacc': 171})
  --> Branch 4:
    Splitting on Buying Price
    --> Branch high:
      Splitting on Size of luggage boot
      --> Branch big:
        Splitting on Price of maintenance
        --> Branch high:
          Counter({'acc': 4})
        --> Branch low:
          Counter({'acc': 4})
        --> Branch med:
          Counter({'acc': 1})
        --> Branch vhigh:
          Counter({'unacc': 4})
      --> Branch med:
        Splitting on Number of doors
        --> Branch 2:
          Counter({'unacc': 4})
        --> Branch 3:
          Counter({'unacc': 3})
        --> Branch 4:
          Splitting on Price of maintenance
          --> Branch high:
            Counter({'acc': 1})
          --> Branch low:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch vhigh:
            Counter({'unacc': 1})
        --> Branch 5more:
          Splitting on Price of maintenance
          --> Branch high:
            Counter({'acc': 1})
          --> Branch low:
            Counter({'acc': 1})
          --> Branch vhigh:
            Counter({'unacc': 1})
      --> Branch small:
        Counter({'unacc': 13})
    --> Branch low:
      Splitting on Price of maintenance
      --> Branch high:
        Counter({'acc': 11})
      --> Branch low:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'good': 4})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'good': 1})
          --> Branch 5more:
            Counter({'good': 1})
        --> Branch small:
          Counter({'acc': 2})
      --> Branch med:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'good': 3})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'good': 1})
        --> Branch small:
          Counter({'acc': 4})
      --> Branch vhigh:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'acc': 4})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'unacc': 1})
          --> Branch 4:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch small:
          Counter({'unacc': 4})
    --> Branch med:
      Splitting on Price of maintenance
      --> Branch high:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'acc': 2})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'unacc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch small:
          Counter({'unacc': 3})
      --> Branch low:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'good': 3})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'acc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'good': 1})
          --> Branch 5more:
            Counter({'good': 1})
        --> Branch small:
          Counter({'acc': 4})
      --> Branch med:
        Counter({'acc': 11})
      --> Branch vhigh:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'acc': 4})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'unacc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch small:
          Counter({'unacc': 4})
    --> Branch vhigh:
      Splitting on Price of maintenance
      --> Branch high:
        Counter({'unacc': 12})
      --> Branch low:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'acc': 3})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'unacc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch small:
          Counter({'unacc': 3})
      --> Branch med:
        Splitting on Size of luggage boot
        --> Branch big:
          Counter({'acc': 4})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'unacc': 1})
          --> Branch 4:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch small:
          Counter({'unacc': 4})
      --> Branch vhigh:
        Counter({'unacc': 11})
  --> Branch more:
    Splitting on Size of luggage boot
    --> Branch big:
      Splitting on Buying Price
      --> Branch high:
        Splitting on Price of maintenance
        --> Branch high:
          Counter({'acc': 4})
        --> Branch low:
          Counter({'acc': 4})
        --> Branch med:
          Counter({'acc': 4})
        --> Branch vhigh:
          Counter({'unacc': 3})
      --> Branch low:
        Splitting on Price of maintenance
        --> Branch high:
          Counter({'acc': 4})
        --> Branch low:
          Counter({'good': 2})
        --> Branch med:
          Counter({'good': 4})
        --> Branch vhigh:
          Counter({'acc': 4})
      --> Branch med:
        Splitting on Price of maintenance
        --> Branch high:
          Counter({'acc': 4})
        --> Branch low:
          Counter({'good': 3})
        --> Branch med:
          Counter({'acc': 4})
        --> Branch vhigh:
          Counter({'acc': 4})
      --> Branch vhigh:
        Splitting on Price of maintenance
        --> Branch high:
          Counter({'unacc': 3})
        --> Branch low:
          Counter({'acc': 3})
        --> Branch med:
          Counter({'acc': 4})
        --> Branch vhigh:
          Counter({'unacc': 4})
    --> Branch med:
      Splitting on Price of maintenance
      --> Branch high:
        Splitting on Buying Price
        --> Branch high:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch low:
          Counter({'acc': 2})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'acc': 1})
        --> Branch vhigh:
          Counter({'unacc': 4})
      --> Branch low:
        Splitting on Buying Price
        --> Branch high:
          Counter({'acc': 1})
        --> Branch low:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'acc': 1})
          --> Branch 3:
            Counter({'good': 1})
          --> Branch 5more:
            Counter({'good': 1})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'acc': 1})
          --> Branch 3:
            Counter({'good': 1})
          --> Branch 4:
            Counter({'good': 1})
          --> Branch 5more:
            Counter({'good': 1})
        --> Branch vhigh:
          Counter({'acc': 3})
      --> Branch med:
        Splitting on Buying Price
        --> Branch high:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch low:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'acc': 1})
          --> Branch 3:
            Counter({'good': 1})
          --> Branch 4:
            Counter({'good': 1})
          --> Branch 5more:
            Counter({'good': 1})
        --> Branch med:
          Counter({'acc': 4})
        --> Branch vhigh:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
      --> Branch vhigh:
        Splitting on Buying Price
        --> Branch high:
          Counter({'unacc': 3})
        --> Branch low:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch vhigh:
          Counter({'unacc': 4})
    --> Branch small:
      Splitting on Buying Price
      --> Branch high:
        Counter({'unacc': 15})
      --> Branch low:
        Splitting on Number of doors
        --> Branch 2:
          Counter({'unacc': 4})
        --> Branch 3:
          Splitting on Price of maintenance
          --> Branch high:
            Counter({'acc': 1})
          --> Branch low:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch vhigh:
            Counter({'unacc': 1})
        --> Branch 4:
          Splitting on Price of maintenance
          --> Branch high:
            Counter({'acc': 1})
          --> Branch low:
            Counter({'acc': 1})
          --> Branch med:
            Counter({'acc': 1})
          --> Branch vhigh:
            Counter({'unacc': 1})
        --> Branch 5more:
          Splitting on Price of maintenance
          --> Branch med:
            Counter({'acc': 1})
          --> Branch vhigh:
            Counter({'unacc': 1})
      --> Branch med:
        Splitting on Price of maintenance
        --> Branch high:
          Counter({'unacc': 4})
        --> Branch low:
          Counter({'acc': 2})
        --> Branch med:
          Splitting on Number of doors
          --> Branch 2:
            Counter({'unacc': 1})
          --> Branch 3:
            Counter({'acc': 1})
          --> Branch 4:
            Counter({'acc': 1})
          --> Branch 5more:
            Counter({'acc': 1})
        --> Branch vhigh:
          Counter({'unacc': 4})
      --> Branch vhigh:
        Counter({'unacc': 12})
""" 



