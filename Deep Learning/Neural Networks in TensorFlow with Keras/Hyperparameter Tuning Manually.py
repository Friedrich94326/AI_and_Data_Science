""" Using a Validation Set for Hyperparameter Tuning """
from model import design_model, features_train, labels_train 

model = design_model(features_train, learning_rate = 0.01)
#your code here
model.fit(features_train, labels_train, epochs = 40, batch_size = 8, verbose = 1, validation_split = 0.33)


""" Manual tuning: Learning Rate """
import matplotlib.pyplot as plt

def fit_model(f_train, l_train, learning_rate, num_epochs, bs):
    #build the model
    model = design_model(f_train, learning_rate)
    #train the model on the training data
    history = model.fit(f_train, l_train, epochs = num_epochs, batch_size = bs, verbose = 0, validation_split = 0.2)
    # plot learning curves
    plt.plot(history.history['loss'], label = 'train')
    plt.plot(history.history['val_loss'], label = 'validation')
    plt.title('lrate=' + str(learning_rate))
    plt.legend(loc = "upper right")


#make a list of learning rates to try out
#learning_rates = [1, 1E-2, 1E-7]
learning_rates = [1E-3, 1E-4, 1E-7]

#fixed number of epochs
num_epochs = 100
#fixed number of batches
batch_size = 10 

for i in range(len(learning_rates)):
  plot_no = 420 + (i+1)
  plt.subplot(plot_no)
  fit_model(features_train, labels_train, learning_rates[i], num_epochs, batch_size)

plt.tight_layout()
plt.show()
plt.savefig('static/images/my_plot.png')
print("See the plot on the right with learning rates", learning_rates)
import app #don't worry about this. This is to show you the plot in the browser.


""" Manual tuning: Batch Size """

""" Batch GD/ SGD/ Mini-batch GD: An advantage of using batches is for GPU computation that can parallelize neural network computations. """


def fit_model(f_train, l_train, learning_rate, num_epochs, batch_size, ax):
    model = design_model(features_train, learning_rate)
    #train the model on the training data
    history = model.fit(features_train, labels_train, epochs = num_epochs, batch_size = batch_size, verbose = 0, validation_split = 0.3)
    # plot learning curves
    ax.plot(history.history['mae'], label = 'train')
    ax.plot(history.history['val_mae'], label = 'validation')
    ax.set_title('batch = ' + str(batch_size), fontdict = {'fontsize': 8, 'fontweight': 'medium'})
    ax.set_xlabel('# epochs')
    ax.set_ylabel('mae')
    ax.legend()

#fixed learning rate 
#learning_rate = 0.01 
learning_rate = 0.1

#fixed number of epochs
num_epochs = 100
#we choose a number of batch sizes to try out
#batches = [2, 10, 16]
batches = [4, 32, 64] 
print("Learning rate fixed to:", learning_rate)

#plotting code
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex='col', sharey='row',
                        gridspec_kw = {'hspace': 0.7, 'wspace': 0.4}) #preparing axes for plotting
axes = [ax1, ax2, ax3]

#iterate through all the batch values
for i in range(len(batches)):
  fit_model(features_train, labels_train, learning_rate, num_epochs, batches[i], axes[i])

plt.savefig('static/images/my_plot.png')
print("See the plot on the right with batch sizes", batches)
import app #don't worry about this. This is to show you the plot in the browser.


""" Manual Tuning: Epochs and Early Stopping """

"""  Too many epochs can lead to overfitting, and too few to underfitting. 
One trick is to use early stopping: when the training performance reaches the plateau or starts degrading, the learning stops. """

from tensorflow.keras.callbacks import EarlyStopping

def fit_model(f_train, l_train, learning_rate, num_epochs):
    #build the model: to see the specs go to model.pyl we increased the number of hidden neurons
    #in order to introduce some overfitting
    model = design_model(features_train, learning_rate) 
    #train the model on the training data
    # An EarlyStopping callback monitors the validation loss (val_loss), seeks minimal loss, that is verbose, and has patience equal to 20
    es = EarlyStopping(monitor = 'val_loss', mode = 'min', verbose = 1, patience = 20)
    history = model.fit(features_train, labels_train, epochs=num_epochs, batch_size= 16, verbose=0, validation_split = 0.2, callbacks = [es])
    return history
    

#using the early stopping in fit_model
learning_rate = 0.1
num_epochs = 500
history = fit_model(features_train, labels_train, learning_rate, num_epochs)

#plotting
fig, axs = plt.subplots(1, 2, gridspec_kw={'hspace': 1, 'wspace': 0.5}) 
(ax1, ax2) = axs
ax1.plot(history.history['loss'], label='train')
ax1.plot(history.history['val_loss'], label='validation')
ax1.set_title('lrate=' + str(learning_rate))
ax1.legend(loc="upper right")
ax1.set_xlabel("# of epochs")
ax1.set_ylabel("loss (mse)")

ax2.plot(history.history['mae'], label='train')
ax2.plot(history.history['val_mae'], label='validation')
ax2.set_title('lrate=' + str(learning_rate))
ax2.legend(loc="upper right")
ax2.set_xlabel("# of epochs")
ax2.set_ylabel("MAE")

print("Final training MAE:", history.history['mae'][-1])
print("Final validation MAE:", history.history['val_mae'][-1])

plt.savefig('static/images/my_plot.png')
import app #don't worry about this. This is to show you the plot in the browser.


""" Manual Tuning: Changing the Model """
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers

def more_complex_model(X, learning_rate):
    model = Sequential(name="my_first_model")
    input = tf.keras.Input(shape=(X.shape[1],))
    model.add(input)
    #model.add(layers.Dense(64, activation='relu'))
    # simplify the hidden units from 64 to 8
    model.add(layers.Dense(8, activation='relu'))
    model.add(layers.Dense(1))
    opt = tf.keras.optimizers.Adam(learning_rate = learning_rate)
    model.compile(loss='mse', metrics=['mae'], optimizer=opt)
    return model

def one_layer_model(X, learning_rate):
    model = Sequential(name="my_first_model")
    input = tf.keras.Input(shape=(X.shape[1],))
    model.add(input)
    model.add(layers.Dense(1))
    opt = tf.keras.optimizers.Adam(learning_rate = learning_rate)
    model.compile(loss='mse', metrics=['mae'], optimizer=opt)
    return model

def fit_model(model, f_train, l_train, learning_rate, num_epochs):
    #train the model on the training data
    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience = 20)
    history = model.fit(features_train, labels_train, epochs=num_epochs, batch_size= 2, verbose=0, validation_split = 0.2, callbacks = [es])
    return history

def plot(history):
    # plot learning curves
    fig, axs = plt.subplots(1, 2, gridspec_kw={'hspace': 1, 'wspace': 0.8}) 
    (ax1, ax2) = axs
    ax1.plot(history.history['loss'], label='train')
    ax1.plot(history.history['val_loss'], label='validation')
    ax1.set_title('lrate=' + str(learning_rate))
    ax1.legend(loc="upper right")
    ax1.set_xlabel("# of epochs")
    ax1.set_ylabel("loss (mse)")

    ax2.plot(history.history['mae'], label='train')
    ax2.plot(history.history['val_mae'], label='validation')
    ax2.set_title('lrate=' + str(learning_rate))
    ax2.legend(loc="upper right")
    ax2.set_xlabel("# of epochs")
    ax2.set_ylabel("MAE")
    print("Final training MAE:", history.history['mae'][-1])
    print("Final validation MAE:", history.history['val_mae'][-1])

learning_rate = 0.1
num_epochs = 200

#fit the more simple model
print("Results of a one layer model:")
history1 = fit_model(one_layer_model(features_train, learning_rate), features_train, labels_train, learning_rate, num_epochs)
plot(history1)
plt.savefig('static/images/my_plot1.png')

#fit the more complex model
print("Results of a model with hidden layers:")
history2 = fit_model(more_complex_model(features_train, learning_rate), features_train, labels_train, learning_rate, num_epochs)
plot(history2)
plt.savefig('static/images/my_plot2.png')

import app #don't worry about this. This is to show you the plot in the browser.


