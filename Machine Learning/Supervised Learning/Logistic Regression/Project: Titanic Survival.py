# In this project you will create a Logistic Regression model that predicts which passengers survived the sinking of the Titanic, based on features like age and class.

# Training data is provided by Kaggle at: https://www.kaggle.com/c/titanic

import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')
print(passengers.head())

# Update sex column to numerical
passengers["Sex"].replace({"male": "0", "female": "1"}, inplace = True)

print(passengers.head())
print(passengers["Age"].values)

# Fill the nan values in the age column
passengers["Age"].fillna(value = passengers["Age"].mean(), inplace=True)


# Create a first class column
def DivideClass(x):
  ReturnNum = 0
  if x == 1:
    ReturnNum = 1
  else:
    pass
  return ReturnNum

passengers["FirstClass"] = passengers['Pclass'].apply(DivideClass)
#print(passengers.FirstClass.values)

# Create a second class column
passengers["SecondClass"] = passengers['Pclass'].apply(lambda x: 2 if x == 2 else 0)

print(passengers)

# Select the desired features
features = passengers[ ["Sex", "Age", "FirstClass", "SecondClass"] ] 
survival = passengers["Survived"]

# Perform train, test, split
features_train, features_test, labels_train, labels_test = train_test_split(features, survival, train_size = 0.8, test_size = 0.2, random_state = 100)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
scaler.fit_transform(features_train)
scaler.transform(features_test)

# Create and train the model
regressor = LogisticRegression()
regressor.fit(features_train, labels_train)

# Score the model on the train data
print("Training score: %.3f" %regressor.score(features_train, labels_train))

# Score the model on the test data
print("Testing score: %.3f" %regressor.score(features_test, labels_test))


# Analyze the coefficients
#print("Feature coefficients: Sex, Age, FirstClass, SecondClass")
#print(regressor.coef_)
# print each feature with its respectice coefficient value
print(list(zip(['Sex','Age','FirstClass','SecondClass'],regressor.coef_[0])))

# 'Sex'is most important in predicting survival on the sinking of the Titanic
# 'FirstClass' is the secondly important feature



# Sample passenger features
Jack = np.array([0.0, 20.0, 0.0, 0.0])
Rose = np.array([1.0, 17.0, 1.0, 0.0])
Me = np.array([0.0, 26.0, 0.0, 1.0])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, Me])


# Scale the sample passenger features
print("normalised features:")
print(scaler.transform(sample_passengers))

# Make survival predictions!
print("Survival classifications of sample passengers:")
print(regressor.predict(sample_passengers))
print("[prob of perishing, prob of surviving]")
print(regressor.predict_proba(sample_passengers) )

# Result:
# Jack: perish, survive, perish
# Jack: [0.88529354 0.11470646] Rose: [0.06246447 0.93753553] Me: [0.83230187 0.16769813]

