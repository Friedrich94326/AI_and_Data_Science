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

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import layers

import matplotlib.pyplot as plt
import numpy




""" Preprocessing Image Data """
#Construct an ImageDataGenerator object:
DIRECTORY_TRAIN = "drive/My Drive/Deep Learning Projects/Covid-19 and Pneumonia Classification/Covid19-dataset/train"
DIRECTORY_TEST = "drive/My Drive/Deep Learning Projects/Covid-19 and Pneumonia Classification/Covid19-dataset/test"
CLASS_MODE = "categorical"
COLOR_MODE = "grayscale"
TARGET_SIZE = (256, 256)
BATCH_SIZE = 32

training_data_generator = ImageDataGenerator(
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
validation_split = 0.2 
)

print("\nLoading training data...")


training_iterator = training_data_generator.flow_from_directory(DIRECTORY_TRAIN, class_mode = 'categorical', color_mode = 'grayscale', target_size = TARGET_SIZE, batch_size = BATCH_SIZE, subset = 'training') # set as training data

training_iterator.next()

print("\nLoading validation data...")

validation_iterator = training_data_generator.flow_from_directory(DIRECTORY_TRAIN, class_mode = 'categorical', color_mode = 'grayscale', target_size = TARGET_SIZE, batch_size = BATCH_SIZE, subset = 'validation') # set as validation data

validation_iterator.next()

#Print its attributes:
print(training_data_generator.__dict__)



""" Contruct a Neural Network Model """


print("\nBuilding model...")

def design_model(training_data):
    # sequential model
    model = Sequential(name = 'Covid19_and_Pneumonia_Classifier')
    # add input layer with grayscale image shape
    model.add(tf.keras.Input(shape = (256, 256, 1), name = 'input_layer'))
    # convolutional hidden layers with relu functions
    # maxpooling layers and dropout layers as well
    model.add(layers.Conv2D(5, 5, strides = 3, activation = "relu", name = 'conv_layer_1')) 
    model.add(layers.MaxPooling2D(
        pool_size = (2, 2), strides = (2,2), name = 'max_pooling_layer_1'))
    model.add(layers.Dropout(0.1, name = 'dropout_layer_1'))
    model.add(layers.Conv2D(3, 3, strides = 1, activation = "relu", name = 'conv_layer_2')) 
    model.add(layers.MaxPooling2D(
        pool_size = (2, 2), strides = (2, 2), name = 'max_pooling_layer_2'))
    model.add(layers.Dropout(0.2, name = 'dropout_layer_2'))

    # experimenting with extra layesr
    #model.add(tf.keras.layers.Conv2D(3, 3, strides=1, activation="relu"))
    #model.add(tf.keras.layers.Conv2D(1, 1, strides=1, activation="relu"))
    #model.add(tf.keras.layers.Dropout(0.1))

    model.add(layers.Flatten(name = 'flatten_layer'))
    # output layer with softmax activation function
    model.add(layers.Dense(3, activation = "softmax", name = 'output_layer'))
    # compile model with Adam optimizer
    # loss function is categorical crossentropy
    # metrics are categorical accuracy and AUC
    print("\nCompiling model...")
    model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = .001), loss = tf.keras.losses.CategoricalCrossentropy(), metrics = [tf.keras.metrics.CategoricalAccuracy(), tf.keras.metrics.AUC()],)
    # summarize model
    model.summary()
    return model
 
 
 
 
""" Train and Evaluate the Model """

#Build a model from Model function
model = design_model(training_iterator)

# early stopping implementation
es = EarlyStopping(monitor = 'val_auc', mode = 'max', verbose = 1, patience = 20)

print("\nTraining model...")
# fit the model with 30 ephochs and early stopping
history = model.fit(
        training_iterator,
        steps_per_epoch = training_iterator.samples/ BATCH_SIZE,
        epochs = 30,
        validation_data = validation_iterator,
        validation_steps = validation_iterator.samples/ BATCH_SIZE,
        callbacks = [es]
)


print(validation_iterator.samples)
print(training_iterator.samples)




""" Visualisation the Training Process of the Neural Network Model """

# plotting categorical and validation accuracy over epochs
fig = plt.figure()
fig.subplots_adjust(wspace = 0.1, hspace = 1)
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(history.history['categorical_accuracy'])
ax1.plot(history.history['val_categorical_accuracy'])
ax1.set_title('model accuracy')
ax1.set_xlabel('epoch')
ax1.set_ylabel('accuracy')
ax1.legend(['train', 'validation'], loc = 'upper left')

# plotting auc and validation auc over epochs
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(history.history['categorical_accuracy'])
ax2.plot(history.history['val_categorical_accuracy'])
ax2.set_title('model auc')
ax2.set_xlabel('epoch')
ax2.set_ylabel('auc')
ax2.legend(['train', 'validation'], loc = 'upper left')

plt.show()



test_steps_per_epoch = numpy.math.ceil(validation_iterator.samples / validation_iterator.batch_size)
predictions = model.predict(validation_iterator, steps = test_steps_per_epoch)
predicted_classes = numpy.argmax(predictions, axis = 1)
true_classes = validation_iterator.classes
class_labels = list(validation_iterator.class_indices.keys())
report = classification_report(true_classes, predicted_classes, target_names = class_labels)
print(report)   

cm = confusion_matrix(true_classes, predicted_classes)
print(cm)



