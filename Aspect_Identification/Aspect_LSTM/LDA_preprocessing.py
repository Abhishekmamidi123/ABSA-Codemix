import io
import json
import pickle
import pycrfsuite
import numpy as np
from random import shuffle
from xml.etree import cElementTree as ET
np.set_printoptions(threshold=np.nan)

with open('X_data.pkl', 'r') as file:
	X = pickle.load(file)

tag_num = {'N':0, 'A':1}
with open('y_data.txt', 'r') as file:
	y = eval(file.readline())

filehandler = open('ldamodel.obj', 'r')
ldamodel = pickle.load(filehandler)


