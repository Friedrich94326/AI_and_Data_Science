""" Cross-Entropy: a score that summarizes the average difference between the actual and predicted probability distributions for all classes.  """

from sklearn.metrics import log_loss

#the first class is set to probability 1, all others are 0; this example belongs to class #1
ex_1_true = [1, 0, 0] 
#the second class is set to probability 1, all others are 0; this example belongs to class #2
ex_2_true = [0, 1, 0] 
#the third class is set to probability 1, all others are 0; this example belongs to class #3
ex_3_true = [0, 0, 1] 

#the highest probability is given to class #1
ex_1_predicted = [0.7, 0.2, 0.1] 
#the highest probability is given to class #2
ex_2_predicted = [0.1, 0.8, 0.1] 
#the highest probability is given to class #3
ex_3_predicted = [0.2, 0.2, 0.6] 

#the highest probability given to class #3, true labels is class #1
ex_1_predicted_bad = [0.1, 0.1, 0.7]
#the highest probability given to class #1, true labels is class #2
ex_2_predicted_bad = [0.8, 0.1, 0.1] 
#the highest probability given to class #1, true labels is class #3
ex_3_predicted_bad = [0.6, 0.2, 0.2] 

true_labels = [ex_1_true, ex_2_true, ex_3_true]
predicted_labels = [ex_1_predicted, ex_2_predicted, ex_3_predicted]
predicted_labels_bad = [ex_1_predicted_bad, ex_2_predicted_bad, ex_3_predicted_bad]

ll = log_loss(true_labels, predicted_labels)
print('Average Log Loss (good prediction): %.3f' % ll) # 0.364

ll = log_loss(true_labels, predicted_labels_bad)
print('Average Log Loss (bad prediction): %.3f' % ll) # 2.036

ll = log_loss(true_labels, true_labels)
print('(TODO)Average Log Loss (true prediction): %.3f' % ll) # 0.000


""" Loading and Analyzing Data """

import pandas as pd
from collections import Counter

#your code here
train_data = pd.read_csv('air_quality_train.csv')
test_data = pd.read_csv('air_quality_test.csv')

#print columns and their respective types
print(train_data.info())

#print the class distribution
print(Counter(train_data['Air_Quality']))

#extract the features from the training data
x_train = train_data[ ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI'] ]

#extract the label column from the training data
y_train = train_data["Air_Quality"]

#extract the features from the test data
x_test = test_data[['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI']]

#extract the label column from the test data
y_test = test_data["Air_Quality"]

""" Preparing the Data """

from sklearn.preprocessing import LabelEncoder
import tensorflow




