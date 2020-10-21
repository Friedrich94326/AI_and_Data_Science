# In this project, we’ll use decision trees to try to predict the continent of flags based on several of these features.

import codecademylib3_seaborn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# Step 1: Investigate the Data

# We want row 0 to be used as the header, so include the parameter header = 0
flags = pd.read_csv("flags.csv", header = 0)

# Preview the features available to us
print(flags.columns)
print(flags.head())


# create a decision tree to classify what Landmass a country is on
labels_landmass = flags[["Landmass"]]
labels_language = flags[["Language"]]
labels_religion = flags[["Religion"]]


# Step 2: Creating Your Data and Labels

# let’s see if we can predict where a country is based only on the colors of its flag
#data = flags[["Red", "Green", "Blue", "Gold", "White", "Black", "Orange"]]

data = flags[["Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses", "Saltires", "Quarters", "Sunstars", "Crescent", "Triangle"]]

train_data, test_data, train_labels_religion, test_labels_religion = train_test_split(data, labels_religion, random_state = 1)

train_data, test_data, train_labels_landmass, test_labels_landmass = train_test_split(data, labels_landmass, random_state = 1)

train_data, test_data, train_labels_language, test_labels_language = train_test_split(data, labels_language, random_state = 1)


# Step 3: Make and Test the Model

tree = DecisionTreeClassifier(random_state = 1)
tree = tree.fit(train_data, train_labels_religion)
#plot_tree(tree)

tree = DecisionTreeClassifier(random_state = 1)
tree = tree.fit(train_data, train_labels_landmass)

tree = DecisionTreeClassifier(random_state = 1)
tree = tree.fit(train_data, train_labels_language)

accuracy = tree.score(test_data, test_labels_religion)
accuracy = tree.score(test_data, test_labels_landmass)
accuracy = tree.score(test_data, test_labels_language)

# Step 4: Tuning the Model- prune the tree to make it predict better!
N = 20
for i in range(1, N + 1):
  tree = DecisionTreeClassifier(max_depth = i, random_state = 1)
  tree = tree.fit(train_data, train_labels_religion)

  accuracy = tree.score(test_data, test_labels_religion)
  print("As max depth = %d, religion accuracy = %.3f%%" %(i, (100*accuracy)) )

for i in range(1, N + 1):
  tree = DecisionTreeClassifier(max_depth = i, random_state = 1)
  tree = tree.fit(train_data, train_labels_landmass)

  accuracy = tree.score(test_data, test_labels_landmass)
  print("As max depth = %d, landmass accuracy = %.3f%%" %(i, (100*accuracy)) )


for i in range(1, N + 1):
  tree = DecisionTreeClassifier(max_depth = i, random_state = 1)
  tree = tree.fit(train_data, train_labels_language)

  accuracy = tree.score(test_data, test_labels_language)
  print("As max depth = %d, language accuracy = %.3f%%" %(i, (100*accuracy)) )


# Graph the score of each tree versus different max depth
scores_religion = []
scores_landmass = []
scores_language = []

for i in range(1, N + 1):
  tree = DecisionTreeClassifier(max_depth = i, random_state = 1)
  tree = tree.fit(train_data, train_labels_religion)

  accuracy = tree.score(test_data, test_labels_religion)
  scores_religion.append(accuracy)
  
for i in range(1, N + 1):
  tree = DecisionTreeClassifier(max_depth = i, random_state = 1)
  tree = tree.fit(train_data, train_labels_landmass)

  accuracy = tree.score(test_data, test_labels_landmass)
  scores_landmass.append(accuracy)


for i in range(1, N + 1):
  tree = DecisionTreeClassifier(max_depth = i, random_state = 1)
  tree = tree.fit(train_data, train_labels_language)

  accuracy = tree.score(test_data, test_labels_language)
  scores_language.append(accuracy)

# It seems like the depth of the tree isn’t really having an impact on its performance. This might be a good indication that we’re not using enough features.

# using the variable ax for single a Axes
fig, ax = plt.subplots()
ax.plot(range(1, N + 1), scores_religion, color = "blue", label = "prediction of religion")
ax.plot(range(1, N + 1), scores_landmass, color = "red", label = "prediction of landmass")
ax.plot(range(1, N + 1), scores_language, color = "green", label = "prediction of language")
ax.set_title("Decision Tree for Finding a Flag")
ax.set_xlabel("max depth")
ax.set_ylabel("accuracy")
ax.set_xticks(range(1, N + 1))
ax.set_ylim(min(scores_language), max(scores_landmass) + 0.025)


plt.legend()
plt.show()

# Explore on Your Own
# N = 4 # reset the max depth of the tree


