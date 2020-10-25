# By using this census data with a random forest, we will try to predict whether or not a person makes more than $50,000.
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

#  every string has an extra space at the start, which makes our data a little hard to catch
income_data = pd.read_csv("income.csv", header = 0, delimiter = ", ")

print(income_data.head())
# see the first row in its entirety
print(income_data.iloc[0])

# label
labels = income_data[ ["income"] ]


# Random forests can’t use columns that contain Strings — they have to be continuous values like integers or floats. So we make every "Male" a 0 and every "Female" a 1.
income_data["sex-int"] = income_data["sex"].apply(lambda row: 0 if row == "Male" else 1)

# since the majority of data comes from United-States, make it 0 and other 1 
print(income_data["native-country"].value_counts())
income_data["country-int"] = income_data["native-country"].apply(lambda row: 0 if row == "United-States" else 1)

# data
data = income_data[ ["age", "capital-gain", "capital-loss", "hours-per-week", "sex-int", "country-int"]]

train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)


forest = RandomForestClassifier(random_state = 1)
forest.fit(train_data, train_labels)

# shows the relevance of a column from the training data
print(forest.feature_importances_)

accuracy = forest.score(test_data, test_labels)
print("accuracy = %.4f" %accuracy) # without both: 0.8223, with "sex_int": .8273, with "country-int": .8225

visualize_classifier(forest, train_data, train_labels)





