""" The World Health Organization (WHO)’s Global Health Observatory (GHO) data repository tracks life expectancy 
for countries worldwideby following health status and many other related factors. This dataset covers a variety 
of indicators for all countries from 2000 to 2015 including:
  1. immunization factors
  2. mortality factors
  3. economic factors
  4. social factors
  5. other health-related factors 
In this project, I will design, train, and evaluate a neural network model performing the task of regressionto predict 
the life expectancy of countries using this dataset.  
"""


import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


""" Data Loading and Observing """
dataset = pd.read_csv('life_expectancy.csv')

print(dataset.head())
print(dataset.columns)
# observe the summary statistics of the data
print(dataset.describe())

# Drop the 'Country' column to learn a general pattern for all the countries
dataset = dataset.drop(['Country'], axis = 1)
print(dataset.head())
print(dataset.columns)

""" Data Preprocessing """
# convert categorical columns into numerical ones
dataset = pd.get_dummies(dataset)

# labels: the last column of data
labels = dataset.iloc[:, -1]

# features: the remaining columns of data
features = dataset.iloc[:, 0:-1]

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 100)

# normalise the numerical features
numerical_features = features.select_dtypes(include = ['float64', 'int64'])
numerical_columns = numerical_features.columns
ct = ColumnTransformer([('standardize', StandardScaler(), numerical_columns)], remainder = 'passthrough')

features_train_scaled = ct.fit_transform(features_train)
features_test_scaled = ct.fit_transform(features_test)


""" Building the Model """
num_features = features.shape[1]
my_model = Sequential()

# create an input layer and add it to the model
input = InputLayer(input_shape = (num_features, ))
my_model.add(input)

# create a hidden layer and add it to the model
my_model.add(Dense(64, activation = 'relu'))

# create an output layer and add it to the model
my_model.add(Dense(1)) # for regression prediction

print(my_model.summary())

""" Intialising the Optimiser and Compiling the Model """
opt_adam = Adam(learning_rate = 0.01)
my_model.compile(loss = 'mse',  metrics = ['mae'], optimizer = opt_adam)


""" Train and Evaluate the model """
my_model.fit(features_train_scaled, labels_train, epochs = 40, batch_size = 1, verbose = 1)

res_mse, res_mae = my_model.evaluate(feautres_test_scaled, labels_test, verbose = 0)

print("MSE test: ", res_mse)
print("MAE test: ", res_mae)
