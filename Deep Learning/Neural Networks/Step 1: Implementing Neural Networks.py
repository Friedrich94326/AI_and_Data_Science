
""" Loading the data """

import pandas as pd

#load the dataset
dataset = pd.read_csv('insurance.csv') 
#choose first 7 columns as features
features = dataset.iloc[:,0:6] 
#choose the final column for prediction
labels = dataset.iloc[:,-1] 

#print the number of features in the dataset
print("Number of features: ", features.shape[1]) 
#print the number of samples in the dataset
print("Number of samples: ", features.shape[0]) 
#see useful summary statistics for numeric features
print(features.describe()) 

# number of samples of the 'labels' series
print(labels.shape)
# summary statistics of the 'labels' series
print(labels.describe())

""" Data preprocessing: one-hot encoding and standardization """

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer

# one-hot encoding for categorical variables
features = pd.get_dummies(features) 
# split the data into training and test data
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42) 
 
# normalize the numeric columns using ColumnTransformer
ct = ColumnTransformer([('normalize', Normalizer(), ['age', 'bmi', 'children'])], remainder='passthrough')
# fit the normalizer to the training data and convert from numpy arrays to pandas frame
features_train_norm = ct.fit_transform(features_train) 
# applied the trained normalizer on the test data and convert from numpy arrays to pandas frame
features_test_norm = ct.transform(features_test) 

# ColumnTransformer returns numpy arrays. Convert the features to dataframes
features_train_norm = pd.DataFrame(features_train_norm, columns = features_train.columns)
features_test_norm = pd.DataFrame(features_test_norm, columns = features_test.columns)

# -----> your code here below
my_ct = ColumnTransformer([('scale', StandardScaler(), ['age', 'bmi', 'children'])], remainder = 'passthrough')

features_train_scale = my_ct.fit_transform(features_train)
features_test_scale = my_ct.transform(features_test)
print(type(features_train_scale))

# Transform the features_train_scale NumPy array back to a DataFrame
features_train_scale = pd.DataFrame(features_train_scale,columns = features_train.columns)

# Transform the features_test_scale NumPy array back to DataFrame
features_test_scale = pd.DataFrame(features_test_scale,columns = features_test.columns)

# Print the statistics summary
print(features_train_scale.describe())
print(features_test_scale.describe())




