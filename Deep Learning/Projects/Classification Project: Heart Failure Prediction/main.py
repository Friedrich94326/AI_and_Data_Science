""" In this project, you will use a dataset from Kaggle to predict the survival of patients with heart failure 
from serum creatinine and ejection fraction, and other factors such as age, anemia, diabetes, and so on. """

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from sklearn.metrics import classification_report
from tensorflow.keras.utils import to_categorical
import numpy as np

""" Loading and Exploring the Data """
#load the data using `pandas.read_csv()`
data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

#print all the columns and their types
print(data.info())

#print the class distribution
print('Classes and number of values in the dataset', Counter(data['DEATH_EVENT']))

#split the dataframe into features and labels
y = data["DEATH_EVENT"]
x = data[['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time']]

""" Data preprocessing """

#convert the categorical features to one-hot encodings
x  = pd.get_dummies(x)


#to split the data into training features, test features, training labels and test labels
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

#set up a scaler
ct = ColumnTransformer([("numeric", StandardScaler(), ['age', 'creatinine_phosphokinase', 'ejection_fraction','platelets', 'serum_creatinine', 'serum_sodium', 'time'])])

#train the scaler on the training data
X_train = ct.fit_transform(X_train)

#scale the test data using the trained scaler
X_test = ct.transform(X_test)


""" Preparing Labels for Classification """
#initialise LabelEncoder
le = LabelEncoder()

# fit the encoder to the training labels and at the same time convert the labels and then encode the test labels
Y_train = le.fit_transform(Y_train.astype(str))
Y_test = le.transform(Y_test.astype(str))

#transform the training and test labels into a binary vector respectively
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)

""" Designing the Model """
model = Sequential()

#create an input layer and add it to the model
input = InputLayer(input_shape=(X_train.shape[1],))
model.add(input)

#add a hidden layer to the model
model.add(Dense(12, activation='relu'))

#add an output layer to the model with a `softmax` activation function with the number of units corresponding to the number of classes in the dataset
model.add(Dense(2, activation='softmax'))

#set up an optimiser and compile the model
model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])


""" Training and Evaluating the Model """
model.fit(X_train, Y_train, epochs = 100, batch_size = 16, verbose = 1)

loss, acc = model.evaluate(X_test, Y_test, verbose = 0)
print("Loss", loss, "Acc: ", acc)


""" Generating a Classification Report """
#get the predictions for the test data
y_estimate = model.predict(X_test, verbose = 0)

#select the index of the true class for each label encoding in `y_estimate` and 'y_true'
y_estimate = np.argmax(y_estimate, axis = 1)
y_true = np.argmax(Y_test, axis = 1)

#Task 26: print additional metrics
print(classification_report(y_true, y_estimate))
 


