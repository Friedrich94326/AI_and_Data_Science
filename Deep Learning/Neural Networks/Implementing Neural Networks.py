
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


