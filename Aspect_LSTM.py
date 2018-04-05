import io
import json
import pycrfsuite
import numpy as np
from random import shuffle
from xml.etree import cElementTree as ET
np.set_printoptions(threshold=np.nan)
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, LSTM, Conv1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence


filename = '../refinedData/final_codemix_data.json'
open_file = open(filename, 'r')


