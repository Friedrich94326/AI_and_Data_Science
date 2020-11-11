""" Configuring Convolutional Layer-Filters """

import tensorflow as tf

model = tf.keras.Sequential()
model.add(tf.keras.Input(shape = (256, 256, 1)))

#Adds a Conv2D layer with 8 filters, each size 3x3:
print("\n\nModel with 8 filters of size 3x3:")
model.add(tf.keras.layers.Conv2D(8, 3, activation = "relu"))

#Modify change the number of filters to 16
#print("\n\nModel with 16 filters of size 3x3:")
#model.add(tf.keras.layers.Conv2D(16, 3, activation = "relu"))

#Modify the Conv2D layer to have filters of size 7x7
#print("\n\nModel with 16 filters of size 7x7:")
#model.add(tf.keras.layers.Conv2D(16, 7, activation = "relu"))

model.summary()


""" Configuring a Convolutional Layer- Stride and Padding """



