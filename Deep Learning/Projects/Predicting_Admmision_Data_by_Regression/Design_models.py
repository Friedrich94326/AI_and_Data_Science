from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import layers
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

# Approach 1: design a network model using Sequential()
def design_linear_model(features):
    
    model = Sequential(name = 'regression_net_v1')
    
    input = layers.InputLayer(input_shape = (features.shape[1], ))
    model.add(input)
    
    hidden_1 = layers.Dense(128, activation = 'relu')
    model.add(hidden_1)
    
    output = layers.Dense(1)
    model.add(output)
    
    opt = Adam(learning_rate = 1e-3)
    model.compile(loss = 'mse', metrics = ['mae'], optimizer = opt)
    
    model.summary()
    
    return model


from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense


# Approach 2: design a network model using Model()
def design_linear_model_2(features):
    
    inputs = Input(shape = (features.shape[1], ))
    x = Dense(128, activation = 'relu')(inputs)
    output = Dense(1, activation = 'relu')(x)
    
    model = Model(inputs = inputs, outputs = output, name = 'regression_net_v2')
    opt = Adam(learning_rate = 1e-3)
    model.compile(loss = 'mse',
                  metrics = ['mae'],
                  optimizer = opt) # 'accuracy' is not needed for regression problem
    
    model.summary()
    
    return model


