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

#encode the labels into integers
le = LabelEncoder()
y_train = le.fit_transform(y_train.astype(str))
y_test = le.transform(y_test.astype(str))

print("integer-encoded labels:")
print("the first 5 y_train's:")
print(y_train[0:5])
print("the first 5 y_test's:")
print(y_test[0:5])


#print the integer mappings
integer_mapping = {l: i for i, l in enumerate(le.classes_)}
print("The integer mapping:\n", integer_mapping)

#convert the integer encoded labels into binary vectors
y_train = tensorflow.keras.utils.to_categorical(y_train, dtype = 'int64')
y_test = tensorflow.keras.utils.to_categorical(y_test, dtype = 'int64')

print("one-hot-encoded labels:")
print("the first 5 y_train's:")
print(y_train[0:5])
print("the first 5 y_test's:")
print(y_test[0:5])


""" Designing a Deep Learning Model for Classification """

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import IutLayer
from tensorflow.keras.layers import Dense

#design the model
model = Sequential()

#add the input layer
model.add(InputLayer(input_shape = (x_train.shape[1], )))

#add a hidden layer
model.add(Dense(10, activation = 'relu'))

#add an output layer
model.add(Dense(y_train.shape[1], activation = 'softmax'))


""" Setting Up the Optimiser """

#compile the model
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])


""" Train and Evaluate the Model """

#train and evaluate the model
model.fit(x_train, y_train, epochs = 20, batch_size = 4, verbose = 1)
res_mse, res_accu = model.evaluate(x_test, y_test, verbose = 1)

print("MSE test: ", res_mse) # MSE test: 0.4955960214138031
print("ACCU test: ", res_accu) # ACCU test: 0.8285509347915649


""" Additional Evaluation Statistics """

import numpy as np
from sklearn.metrics import classification_report

#get additional statistics
y_estimate = model.predict(x_test)
print("one-hot encoded y_estimate")
print(y_estimate[0:5])

#convert one-hot encoded labels into the index of the class the sample belongs to
print("after conversion y_estimate")
y_estimate = np.argmax(y_estimate, axis = 1)
print(y_estimate[0:5])

y_true = np.argmax(y_test, axis = 1)

#F1-score
print(classification_report(y_true, y_estimate))





















