"""
Problem Description:
For this project, you will create a deep learning regression model that predicts the likelihood 
that a student applying to graduate school will be accepted based on various application factors
(such as test scores).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow	import keras
from tensorflow.keras.callbacks import EarlyStopping

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.metrics import r2_score

from Design_models import *
from keras.models import load_model

""" Step 1: Prepare data """
df = pd.read_csv('admissions_data.csv')
df.head()

""" Step 2: Split the data into features and labels """
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X.head
y.head

""" Step 3: Preprocess data """

# Optional: K-Fold cross validation

# Split the data into training and test data
trainX, testX, trainy, testy = \
    train_test_split(X, y, test_size = .25, random_state = 45) # test set range between 0.20 and 0.35

# Normalise our data
scaler = StandardScaler()
trainX = scaler.fit_transform(trainX) # turned into a numpy array
testX = scaler.transform(testX)

# Review our data
print(trainX.shape) # (375, 8)
print('trainX: \r\n', trainX[:5, :])

print(testX.shape) # (125, 8)
print('testX: \r\n', testX[:5, :])


""" Step 4: Create a deep network for regression """



n_inputs = trainX.shape[1]

my_model = design_linear_model_2(trainX)



""" Step 6: Train and evaluate our model """

# Set an early stopping callback
callback = EarlyStopping(monitor = 'val_loss', mode = 'min', verbose = 1, patience = 20)

# Train the model
print('[INFO] Fitting model...')
history = my_model.fit(trainX, trainy, validation_split = .25, epochs = 400, batch_size = 32, verbose = 1)
print('[INFO] Evaluating model...')

# Evaluate the model
loss = my_model.evaluate(testX, testy, verbose = 0)

fig, axes = plt.subplots(2, 1, figsize = (8, 6)) # figsize = (width, height)

# Plot loss during training
axes[0].set_title('Loss: Mean-Squared Error')
axes[0].plot(history.history['loss'], label = 'training')
axes[0].plot(history.history['val_loss'], label = 'validation')
axes[0].legend()


# Plot the error during training
axes[1].set_title('Error: Mean-Absolute Error')
axes[1].plot(history.history['mae'], label = 'training')
axes[1].plot(history.history['val_mae'], label = 'validation')
axes[1].legend()

fig.tight_layout()
plt.show()



""" Step 7: Save or load the trained model """


# Save the model we just trained earlier
my_model.save("my_linear_model")

# Load the pre-trained model
reconstructed_model = load_model("my_linear_model")

reconstructed_model.summary()



""" Step 8: Predicting by the model manually """

manual_features = testX[:5, :]
manual_preds = my_model(manual_features)
manual_expects = testy[:5]


# Datatype check
manual_preds = manual_preds.numpy()
# print(type(manual_preds)) # eager tensor converted to numpy array
manual_preds = manual_preds.reshape(5)
# print(manual_preds.shape)

manual_expects = manual_expects.to_numpy()
# print(type(manual_expects)) # pandas series converted to numpy array
manual_expects = manual_expects.reshape(5)
# print(manual_expects.shape)
      
# print('Predictions:')
# print(manual_preds)
# print('\r\n\r\nActual:')
# print(manual_expects)

# Integrate to a dataframe for comparison
print('Comparing between actual and prediction data...\r\n')
compare_df = pd.DataFrame({'Prediction': manual_preds, 'Actual': manual_expects, 'Error': abs(manual_expects - manual_preds)})
print(compare_df)
