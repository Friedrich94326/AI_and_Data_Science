"""  In this project, we're gonna build a neural network to classify deep-space galaxies.  """

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.model_selection import train_test_split
from utils import load_galaxy_data

import app

""" Loading Data """
input_data, labels = load_galaxy_data()

print("dimesion of input_data:", input_data.shape)
# (1400, 128, 128, 3)
print("dimension of labels:", labels.shape)
# (1400, 4)

features_train, features_validation, labels_train, labels_validation = train_test_split(input_data, labels, test_size = 0.20, shuffle = True, random_state = 222, stratify = labels)

""" Preprocessing the Input Data """

#Create an img generator and normalise the pixels
data_generator = ImageDataGenerator(rescale = 1.0/255)

training_iterator = data_generator.flow(features_train, labels_train, batch_size = 5)
validation_iterator = data_generator.flow(features_validation, labels_validation, batch_size = 5)

""" Build a model starting with the input shape and output layer """
model = tf.keras.Sequential()

#Input layer
model.add(tf.keras.Input(shape = (128, 128, 3)))

#Convolutional layer: 8 filters, each 3x3 with strides of 2
model.add(tf.keras.layers.Conv2D(8, 3, strides = 2, activation = "relu"))

#Pooling layer: pool_size = (2, 2), strides = 2
model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2), strides = (2, 2)))

#Convolutional layer: 8 filters, each 3x3 with strides of 2
model.add(tf.keras.layers.Conv2D(8, 3, strides = 2, activation = "relu"))

#Pooling layer: pool_size = (2, 2), strides = 2
model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2), strides = (2, 2)))

#Flatten layer
model.add(tf.keras.layers.Flatten())

#Hidden dense layer with 16 hidden units
model.add(tf.keras.layers.Dense(16, activation = "relu"))

#Output layer: 4 classes outputed
model.add(tf.keras.layers.Dense(4, activation = "softmax"))

""" Compile the model """
model.compile(
  optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001),
  loss = tf.keras.losses.CategoricalCrossentropy(),
  metrics = [tf.keras.metrics.CategoricalAccuracy(), tf.keras.metrics.AUC()]
)

""" Print model information: 7,164 parameters """
model.summary()


""" Train and evaluate the model """
BATCH_SIZE = 5

model.fit(
  training_iterator,
  steps_per_epoch = len(training_iterator) / BATCH_SIZE,
  epochs = 12,
  validation_data = validation_iterator,
  validation_steps = len(validation_iterator) / BATCH_SIZE,
  verbose = 1
)



""" Visualise how my CNN processes images """

from visualize import visualize_activations

visualize_activations(model, validation_iterator)

