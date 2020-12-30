""" Two hyperparameters in a convolutional layer: Stride & Padding """
import tensorflow as tf

print("Model with 16 filters:")

model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(256, 256, 1)))

#Adds a Conv2D layer with 16 filters, each size 7x7, and uses a stride of 2 with valid padding:
model.add(tf.keras.layers.Conv2D(16, 7,
strides = 1,
padding = "same",
activation = "relu"))
model.summary()
