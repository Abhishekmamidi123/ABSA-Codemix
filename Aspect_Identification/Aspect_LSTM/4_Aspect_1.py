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

def load_data():
	with open('X_data.pkl', 'r') as file:
		X = load(file)
	with open('y_data.txt', 'r') as file:
		y = eval(file.readline())
	return X, y

def create_model():
	visible = Input(shape=(100,1))
	hidden1 = LSTM(200, return_sequences = True)(visible)
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
	plot_model(model, '3_model_1.png' ,show_shapes=True, show_layer_names=True)
	return model

def concat_X(X):
	X_c = []
	for i in range(len(X)):
		X_c.append(' '.join(X[i]))
	return X_c

def preprocess_data_and_save(X_data, y_data, encoded_docs, vector_length, X_c):
	dont_train = [190, 476, 511, 518, 567, 571, 579, 797, 801, 1222, 1389, 2058, 2532]
	dividing_point = int(len(X_c)*0.8)
	X_train = []
	# X_train = np.array([])
	y_train = []
	count = 0
	print dividing_point
	for i in range(dividing_point):
		print i
		if i not in dont_train:
			vector = encoded_docs[i]
			vector = np.reshape(vector, (1, vector.shape[0]))
			for j in range(len(X_data[i])):
				word_vector = np.zeros(vector_length)
				word = X_data[i][j]
				try:
					index = word_index[X_data[i][j]]
					word_vector[index] = 1
				except:
					if y_data[i][j] == 1:
						count+=1
				word_vector = np.reshape(word_vector, (1, word_vector.shape[0]))
				#if X_train.shape[0] == 0:
				if len(X_train) == 0:
					X_train.append(np.append(word_vector, vector))
					#X_train = np.append(word_vector, vector)
					#X_train = np.reshape(X_train, (1, X_train.shape[0]))
					#print X_train.shape
				else:
					X_train.append(np.append(word_vector, vector))
					#s = np.append(word_vector, vector)
					#print s
					#s = np.reshape(s, (1, s.shape[0]))
					#X_train = np.concatenate((X_train, s))
					#print X_train.shape
					print len(X_train)
				y_train.append(y_data[i][j])
	X_train = np.array(X_train)
	print X_train.shape
	np.save('X_train_model1.npy', X_train)
	np.save('y_train_model1.npy', np.array(y_train))
	
	X_test = np.array([])
	y_test = []
	count = 0
	for i in range(dividing_point, len(X_c)):
		break
		print i
		if i not in dont_train:
			vector = encoded_docs[i]
			vector = np.reshape(vector, (1, vector.shape[0]))
			for j in range(len(X_data[i])):
				word_vector = np.zeros(vector_length)
				word = X_data[i][j]
				try:
					index = word_index[X_data[i][j]]
					word_vector[index] = 1
				except:
					if y_data[i][j] == 1:
						count+=1
				word_vector = np.reshape(word_vector, (1, word_vector.shape[0]))
				if X_test.shape[0] == 0:
					X_test = np.append(word_vector, vector)
					X_test = np.reshape(X_test, (1, X_test.shape[0]))
					print X_test.shape
				else:
					s = np.append(word_vector, vector)
					s = np.reshape(s, (1, s.shape[0]))
					X_test = np.concatenate((X_test, s))
					print X_test.shape
				y_test.append(y_data[i][j])
	print X_test.shape
	np.save('X_test_model1.npy', X_test)
	np.save('y_test_model1.npy', np.array(y_test))

X_data,y_data = load_data()
model = create_model()
X_c = concat_X(X_data)

t = Tokenizer()
t.fit_on_texts(X_c)
word_index = t.word_index
encoded_docs = t.texts_to_matrix(X_c, mode='count')
vector_length = len(encoded_docs[20])

preprocess_data_and_save(X_data, y_data, encoded_docs, vector_length, X_c)
