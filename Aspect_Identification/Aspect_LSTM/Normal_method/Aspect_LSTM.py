import io
import json
import pycrfsuite
import numpy as np
from random import shuffle
from xml.etree import cElementTree as ET
np.set_printoptions(threshold=np.nan)
from keras.models import Sequential
from keras.layers import Dense, LSTM, Conv1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.utils import plot_model

# X - converted into numbers. 0 if not present in the corpus
X_filename = 'X_data_numbers.txt'
with open(X_filename, 'r') as file:
	X = eval(file.readline())

tag_num = {'N':0, 'A':1}
y_filename = 'y_data.txt'
with open(y_filename, 'r') as file:
	y = eval(file.readline())

np.random.seed(7)
number_of_words = 6001
max_length_of_input = 60

# (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=number_of_words)
X_train = X[:2536]
y_train = y[:2536]
X_test = X[2536:]
y_test = y[2536:]

X_train = sequence.pad_sequences(X_train, max_length_of_input)
X_test = sequence.pad_sequences(X_test, max_length_of_input)
y_train = sequence.pad_sequences(y_train, max_length_of_input)
y_test = sequence.pad_sequences(y_test, max_length_of_input)
print y_test

embedding_vector_length = 32
model = Sequential()
model.add(Embedding(number_of_words, embedding_vector_length, input_length = max_length_of_input))
# Uncomment the below line if you want to use Dropout
# model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dense(max_length_of_input, activation = 'softmax'))
model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['accuracy'])
print model.summary()
plot_model(model, to_file='model_LSTM.png', show_shapes=True, show_layer_names=True)

model.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))
score_train, accuracy_train = model.evaluate(X_train, y_train)
print score_train, accuracy_train
score_test, accuracy_test = model.evaluate(X_test, y_test)
print score_test, accuracy_test

model.save('model_LSTM.h5')

predictions = model.predict_classes(X_test)
print predictions[:100]
#for i in range(len(predictions)):
	# print type(predictions[i])
#	predictions[i][predictions[i]<0.4] = 0
#print predictions[:100]
#for i in range(100):
#	print y_test[i], predictions[i]

print score_train, accuracy_train
print score_test, accuracy_test
# truths = y_test
# aspects_matched = 0
# count_aspects = 0
# for i in range(len(predictions)):
# 	if predictions[i] == truths[i] and predictions[i] == 0:
#		aspects_matched += 1
#	if truths[i] == 0:
#		count_aspects += 1
#print aspects_matched
#print count_aspects
#print aspects_matched/float(count_aspects)
