# make a K-Nearest Neighbors classifier that is trained to predict whether a patient has breast cancer

import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt

breast_cancer_data = load_breast_cancer()
print(type(breast_cancer_data))
# <class 'sklearn.utils.Bunch'>
print(breast_cancer_data.data[0]) # datapoinnts in our dataset
print(breast_cancer_data.feature_names) # corresponding labels 

# What are we trying to classify?
print(breast_cancer_data.target)
print(breast_cancer_data.target_names) # ['malignant' 'benign']


# Splitting the data into Training and Validation Sets
training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = .2, random_state = 100)
# random_state ensures that every time you run your code, the data is split in the same way

print(training_data)
print(training_labels)

# Train our classifier
classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(training_data, training_labels)
print("Validation accuracy = %.3f" %classifier.score(validation_data, validation_labels))


# Choosing different k's
accuracy_dict = {}
k_list = range(1, 101)
for k in k_list:
  classifier = KNeighborsClassifier(n_neighbors = k)
  classifier.fit(training_data, training_labels)
  accuracy_dict[k] = classifier.score(validation_data, validation_labels)
  print("Validation accuracy = %.3f" %classifier.score(validation_data, validation_labels))

k_for_AccuracyMax = max(accuracy_dict, key = accuracy_dict.get) 
print("When k = %d, we have the best validation accuracy ever!" %k_for_AccuracyMax)


# Graphing the results
accuracies = [accuracy_dict[k] for k in k_list]
plt.plot(k_list, accuracies, color = 'blue')
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.show()


#  try changing the random_state parameter when making the training set and validation set
