from pickle import load
from numpy import array
import numpy as np
import tensorflow as tf
from tensorflow.contrib.keras import layers
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.vis_utils import plot_model
from keras.models import Model
from keras.layers import Input, Dense, Flatten, Dropout, Embedding, Reshape
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.merge import concatenate
from keras.layers.recurrent import LSTM
from keras import backend as K

visible = Input(shape=(100,1))

hidden1 = LSTM(100, return_sequences = True)(visible)
hidden2 = LSTM(100)(hidden1)
hidden2 = Reshape((100, 1))(hidden2)

conv1 = Conv1D(filters=32, kernel_size=4, activation='relu')(hidden2)
drop1 = Dropout(0.5)(conv1)
pool1 = MaxPooling1D(pool_size=2)(drop1)
flat1 = Flatten()(pool1)

conv2 = Conv1D(filters=32, kernel_size=4, activation='relu')(hidden2)
drop2 = Dropout(0.5)(conv2)
pool2 = MaxPooling1D(pool_size=2)(drop2)
flat2 = Flatten()(pool2)

conv3 = Conv1D(filters=32, kernel_size=4, activation='relu')(hidden2)
drop3 = Dropout(0.5)(conv3)
pool3 = MaxPooling1D(pool_size=2)(drop3)
flat3 = Flatten()(pool3)

merge = concatenate([flat1, flat2, flat3])

output = Dense(1)(merge)
model = Model(inputs = visible, outputs = output)

model.summary()
plot_model(model, '3_model_1.png' ,show_shapes=True, show_layer_names=True)
