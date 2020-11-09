""" Neural Network Model- tensorflow.keras.Sequential: A sequential model, as the name suggests, allows us to create models layer-by-layer in a step-by-step fashion. """

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers


def design_model(features):
  model = Sequential(name = "My First Neural Network")
  return model

dataset = pd.read_csv('insurance.csv') #load the dataset
features = dataset.iloc[:,0:6] #choose first 7 columns as features
labels = dataset.iloc[:,-1] #choose the final column for prediction

features = pd.get_dummies(features) #one-hot encoding for categorical variables
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42) #split the data into training and test data
 
#standardize
ct = ColumnTransformer([('standardize', StandardScaler(), ['age', 'bmi', 'children'])], remainder='passthrough')
features_train = ct.fit_transform(features_train)
features_test = ct.transform(features_test)

#invoke the function for our model design
model = design_model(features_train)

#print the layers
print(model.layers)


""" Neural Network Model- Layers: Layers are the building blocks of neural networks and can contain 1 or more neurons. 
Each layer is associated with parameters: weights, and bias, that are tuned during the learning. """
import tensorflow as tf
from tensorflow.keras import layers

layer = layers.Dense(3) #3 is the number we chose

print(layer.weights) #we get empty weight and bias arrays because tensorflow doesn't know what the shape is of the input to this layer

# 5000 samples, 21 features as in our dataset
input = tf.ones((5000, 21)) 
# a fully-connected layer with 10 neurons
layer = layers.Dense(10) 
# calculate the outputs
output = layer(input) 
# print the weights
print(layer.weights)

""" Neural Network Model: Input Layer """

def design_model(features):
  model = Sequential(name = "my_first_model")

  #get the number of features/dimensions in the data
  num_features = features.shape[1]

  #without hard-coding
  input = layers.InputLayer(input_shape = (num_features, ))

  #add this input layer to the model
  model.add(input)

  return model


dataset = pd.read_csv('insurance.csv') #load the dataset
features = dataset.iloc[:,0:6] #choose first 7 columns as features
labels = dataset.iloc[:,-1] #choose the final column for prediction

features = pd.get_dummies(features) #one-hot encoding for categorical variables
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42) #split the data into training and test data
 
#standardize
ct = ColumnTransformer([('standardize', StandardScaler(), ['age', 'bmi', 'children'])], remainder='passthrough')
features_train = ct.fit_transform(features_train)
features_test = ct.transform(features_test)

#invoke the function for our model design
model = design_model(features_train)

#print a useful summary of a model instance
print(model.summary())



