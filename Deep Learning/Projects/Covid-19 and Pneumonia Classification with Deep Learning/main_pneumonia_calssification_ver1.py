""" 
        Problem Description and Project Goal:

You are a researcher in a hospital lab and are given the task to develop a learning model that supports doctors
with diagnosing illnesses that affect patients’ lungs. At your disposal, you have a set X-ray lung scans with 
examples of patients who had either pneumonia, Covid-19, or no illness. Using the Keras module, you will create
a classification model that outputs a diagnosis based on a patient’s X-ray scan. You hope this model can help
doctors with the challenge of deciphering X-ray scans and open a dialogue between your research team and the
medical staff to create learning models that are as effective and interpretable as possible.
"""


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import layers

import matplotlib.pyplot as plt
import app


""" Preprocessing Image Data """

# Create a data generator and normalise pixels
data_generator = ImageDataGenerator(
#normalise image data
rescale = 1.0/255,

#Randomly increase or decrease the size of the image by up to 10%
zoom_range = 0.1, 

#Randomly rotate the image between -25,25 degrees
rotation_range = 25, 

#Shift the image along its width by up to +/- 5%
width_shift_range = 0.05, 

#Shift the image along its height by up to +/- 5%
height_shift_range = 0.05,

# set validation split
validation_split = 0.2)

# Load and iterate dataset: training & validation
DIRECTORY_TRAIN = 'augmented-data/train'
DIRECTORY_VALIDATION = 'augmented-data/test'
CLASS_MODE = 'categorical'
COLOR_MODE = 'grayscale'
TARGET_SIZE = (256, 256)
BATCH_SIZE = 32 #by default

print("\nLoading training data...")


training_iterator = training_data_generator.flow_from_directory(DIRECTORY_TRAIN, class_mode = CLASS_MODE, color_mode = COLOR_MODE, target_size = TARGET_SIZE, batch_size = BATCH_SIZE, subset = 'training') # set as training data

training_iterator.next()

print("\nLoading validation data...")

validation_iterator = training_data_generator.flow_from_directory(DIRECTORY_TRAIN, class_mode = CLASS_MODE, color_mode = COLOR_MODE,  target_size = TARGET_SIZE, batch_size = BATCH_SIZE, subset = 'validation') # set as validation data

validation_iterator.next()

#Print its attributes:
print(training_data_generator.__dict__)



""" Create a classification neural network model """
print("\nBuilding a neural network model...")
model = Sequential(name = 'Covid19_and_Pneumonia_Classifier')

#input layer
model.add(keras.Input(shape = (256, 256, 1), name = "input_layer"))

#convolutional layer: 8 filters, each 3x3 with strides of 2,
model.add(layers.Conv2D(8, 3, strides = 2, activation = 'relu', name = "convolution_layer"))

#pooling layer
model.add(layers.MaxPooling2D(pool_size = (2, 2), strides = 2, name = "pooling_layer"))

#another possible convolution layer

#another possible pooling layer after the conv2D layer

#flatten layer
model.add(layers.Flatten(name = "flatten_layer"))

#hidden dense layers
model.add(layers.Dense(16, activation = 'relu', name = "hidden_layer"))

#output layer: 3 classes outputed
model.add(layers.Dense(3, activation = "softmax", name = "output_layer"))



""" Compile the model """
OPTIMIZER = tf.keras.optimizers.Adam(learning_rate = 0.001)
LOSS_FUNCTION = tf.keras.losses.CategoricalCrossentropy()
METRICS = [tf.keras.metrics.CategoricalAccuracy(), tf.keras.metrics.AUC()]

model.compile(
  optimizer = OPTIMIZER,
  loss = LOSS_FUNCTION,
  metrics = METRICS
)


""" Print model information """
model.summary()



""" Fit the model with the training set """

BATCH_SIZE = 5

history = model.fit(
  training_iterator,
  steps_per_epoch = len(training_iterator) / BATCH_SIZE,
  epochs = 12,
  validation_data = validation_iterator,
  validation_steps = len(validation_iterator) / BATCH_SIZE,
  verbose = 1
)



""" Visualise training history """

# plot accuracy in the history of training & validation
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc = 'upper left')
plt.show()

# plot loss in the history of training & validation
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc = 'upper left')
plt.show()


#plt.savefig('static/images/my_plots.png')
#plt.show()
