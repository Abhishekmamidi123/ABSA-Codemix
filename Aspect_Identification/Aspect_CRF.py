import io
import json
import pycrfsuite
import numpy as np
from random import shuffle
from nltk.tag import CRFTagger
from xml.etree import cElementTree as ET
np.set_printoptions(threshold=np.nan)
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

filename = '../refinedData/final_codemix_data.json'
open_file = open(filename, 'r')

def word2features(doc, i):
    word = doc[i][0]
    features = [
        'bias',
        'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit()
    ]
    if i > 0:
        word1 = doc[i-1][0]
        features.extend([
            '-1:word.lower=' + word1.lower(),
            '-1:word.istitle=%s' % word1.istitle(),
            '-1:word.isupper=%s' % word1.isupper(),
            '-1:word.isdigit=%s' % word1.isdigit()
        ])
    else:
        features.append('BOS')
    if i < len(doc)-1:
        word1 = doc[i+1][0]
        features.extend([
            '+1:word.lower=' + word1.lower(),
            '+1:word.istitle=%s' % word1.istitle(),
            '+1:word.isupper=%s' % word1.isupper(),
            '+1:word.isdigit=%s' % word1.isdigit()
        ])
    else:
        features.append('EOS')
    return features

def extract_features(doc):
    return [word2features(doc, i) for i in range(len(doc))]

def get_labels(doc):
    return [label for (token, label) in doc]
    
# Main function
c=1
data_read = json.load(open_file)
data = []
for tweet in data_read:
	print c
	aspects = tweet['aspects']
	text = tweet['text'].split(' ')
	print text
	tags = ['N']*len(text)
	print tags
	for aspect in aspects:
		print aspect
		for asp in aspect.split(' '):
			print asp
			cnt = 0
			for i in range(len(text)):
				text[i] = text[i].strip('.').strip(',').strip('!')
			index = text.index(asp)
			tags[index] = 'A'
	print tags
	count = 0
	l = []
	for i in range(len(text)):
		l.append((text[i], tags[i]))
	data.append(l)
	c+=1
print data

