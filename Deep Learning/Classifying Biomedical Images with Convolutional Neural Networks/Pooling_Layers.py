""" Pooling: Layers that pool local information to reduce the dimensionality of intermediate convolutional outputs.
Beyond helping reduce the size of hidden layers (and reducing overfitting), max pooling layers have another useful property: 
they provide some amount of translational invariance. In other words, even if we move around objects in the input image, the output will be the same.  """


import tensorflow as tf

model = tf.keras.Sequential()

model.add(tf.keras.Input(shape = (256, 256, 1)))

model.add(tf.keras.layers.Conv2D(2, 5, strides = 3, padding = "valid", activation = "relu"))

#Add first max pooling layer
model.add(tf.keras.layers.MaxPooling2D(pool_size = (5, 5), strides = (5, 5)))

model.add(tf.keras.layers.Conv2D(4, 3, strides = 1, padding = "valid", activation = "relu"))

#Add the second max pooling layer
model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2), strides = (2, 2)))

model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(2, activation = "softmax"))

#Print model information:
model.summary() 

