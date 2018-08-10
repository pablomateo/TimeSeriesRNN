import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
import string


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []
    
    seriesLength = len(series)
    for element in range(seriesLength - window_size):
        X.append(series[element: element + window_size])
        y.append(series[element + window_size])

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    # Create model
    model = Sequential()
    # Add LSTM - Trying 5 units
    model.add(LSTM(5, input_shape=(window_size, 1)))
    # Add Dense Layer
    model.add(Dense(1))
    # Create Custom Optimizer (Based in RMSProp)
        # Learning Rate = 0.001 (Try 0.0001, 0.01, 0.1)
        # Other parameters Default as recommended in the documentation
            # https://keras.io/optimizers/
    # Done in RNN_project.ipynb
        # myOptimizer = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)
        # Compile Model
        # model.compile(loss='mean_squared_error', optimizer=myOptimizer)
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    
    # import string
    #string.ascii_lowercase
        #The lowercase letters 'abcdefghijklmnopqrstuvwxyz'.
        # ''.join(punctuation) = !,.:;?
    punctuationStr = ''.join(punctuation)
    acceptedStr = string.ascii_lowercase + punctuationStr
        # Out: 'abcdefghijklmnopqrstuvwxyz!,.:;?'
    
    # Use lowercased text!
    for alfanumSym in text.lower():
        # Check if accepted or not
        if not alfanumSym in acceptedStr:
            # Replace with ' ' if not accepted
            text = text.replace(alfanumSym, ' ')
    

    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    # From window_size to len(text) jumping by step_size
    for pos in range(window_size, len(text), step_size):
        # Append corresponding values
    	inputs.append(text[pos - window_size : pos])
    	outputs.append(text[pos])

    return inputs,outputs


# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    # Create model
    model = Sequential()
    # Add LSTM - trying 200 hidden units
    model.add(LSTM(200, input_shape=(window_size, num_chars)))
    # Using Softmax for correct output
    model.add(Dense(num_chars, activation='softmax'))
    # Compile Model
        # Using Optimizer RMSProp - Default values
        # Using categorical_crossentropy as reccommended
    # Done in RNN_project.ipynb
    # model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    return model
