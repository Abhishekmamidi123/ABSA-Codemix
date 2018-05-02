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

visible1 = Input(shape=(100,1))
visible2 = Input(shape=(100,1))
visible3 = Input(shape=(100,1))

hidden1 = LSTM(100, return_sequences = True)(visible1)
hidden2 = LSTM(100)(hidden1)

hidden3 = LSTM(100, return_sequences = True)(visible2)
hidden4 = LSTM(100)(hidden3)

hidden5 = LSTM(100, return_sequences = True)(visible3)
hidden6 = LSTM(100)(hidden5)

merge = concatenate([hidden2, hidden4, hidden6])
print type(merge.shape[1])
merge = Reshape((300, 1))(merge)
conv1 = Conv1D(filters=32, kernel_size=4, activation='relu')(merge)
drop1 = Dropout(0.5)(conv1)
pool1 = MaxPooling1D(pool_size=2)(drop1)
flat1 = Flatten()(pool1)

conv2 = Conv1D(filters=32, kernel_size=4, activation='relu')(merge)
drop2 = Dropout(0.5)(conv2)
pool2 = MaxPooling1D(pool_size=2)(drop2)
flat2 = Flatten()(pool2)

conv3 = Conv1D(filters=32, kernel_size=4, activation='relu')(merge)
drop3 = Dropout(0.5)(conv3)
pool3 = MaxPooling1D(pool_size=2)(drop3)
flat3 = Flatten()(pool3)

merge = concatenate([flat1, flat2, flat3])

output = Dense(2048)(merge)
output = Dense(1)(output)
model = Model(inputs = [visible1, visible2, visible3], outputs = output)

model.summary()
plot_model(model, '3_model_2.png' ,show_shapes=True, show_layer_names=True)
