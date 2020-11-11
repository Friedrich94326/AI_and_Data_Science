import tensorflow as tf

model = tf.keras.Sequential()

#Add an input layer that will expect grayscale input images of size 256x256:
model.add(tf.keras.Input(shape = (256, 256, 1)))

#flatten the image into a single vector:
model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(100, activation = "relu"))
model.add(tf.keras.layers.Dense(50, activation = "relu"))
model.add(tf.keras.layers.Dense(2, activation = "softmax"))

#Print model information:
model.summary() 
