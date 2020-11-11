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


""" Configuring Convolutional Layers- Stride and Padding """

print("Model with 16 filters:")

model_2 = tf.keras.Sequential()
model_2.add(tf.keras.Input(shape = (256, 256, 1)))

#Adds a Conv2D layer with 16 filters, each size 7x7, and uses a stride of 2 with valid padding:
model_2.add(tf.keras.layers.Conv2D(16, 7,
strides = 2,
padding = "same",
activation = "relu"))
model.summary()

""" Adding a Single Convolutional Layer to the Sequential Model """


#Add a Conv2D layer, with 2 filters of size 5x5, strides of 3, valid padding
model.add(tf.keras.layers.Conv2D(
  filters = 2,
  kernel_size = 5,
  strides = 3,
  padding = "valid",
  activation = "relu"
 ))

""" Stack Multiple Layers """
#Add another Conv2D layer, with 4 filters of size 3x3, strides of 1, valid padding
model.add(tf.keras.layers.Conv2D(
  filters = 4,
  kernel_size = 3,
  strides = 1,
  padding = "valid",
  activation = "relu"
 ))


model.add(tf.keras.layers.Flatten())

# #Remove these two dense layers:
#model.add(tf.keras.layers.Dense(100, activation="relu"))
#model.add(tf.keras.layers.Dense(50, activation="relu"))

model.add(tf.keras.layers.Dense(2, activation = "softmax"))

#Print model information:
model.summary()




