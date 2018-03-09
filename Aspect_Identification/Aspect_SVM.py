import io
import json
import pycrfsuite
import numpy as np
from random import shuffle
from nltk.tag import CRFTagger
from xml.etree import cElementTree as ET
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction import FeatureHasher
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
np.set_printoptions(threshold=np.nan)

filename = '../refinedData/final_codemix_data.json'
open_file = open(filename, 'r')

def word2features(doc, i):
    word = doc[i][0]
    # print word
    features = {
        'bias': 'bias',
        #'word.lower': word.lower(),
        #'word[-3:]' : word[-3:],
        'word[-2:]' : word[-2:],
        #'word[:3]' : word[:3],
        'word[:2]' : word[:2],
        'word.isupper' : word.isupper(),
        'word.istitle' : word.istitle(),
        #'word.isdigit' : word.isdigit(),
        'word.contains#' : str('#' in word),
        'word.contains@' : str('@' in word)
    }
    if i > 0:
        word1 = doc[i-1][0]
        features.update({
            #'-1:word.lower' : word1.lower(),
            #'-1:word[-3:]' : word1[-3:],
            '-1:word[-2:]' : word1[-2:],
            #'-1:word[:3]' : word1[:3],
            '-1:word[:2]' : word1[:2],
            '-1:word.istitle' : word1.istitle(),
            '-1:word.isupper' : word1.isupper(),
            #'-1:word.isdigit' : word1.isdigit(),
	    '-1:word.contains#' : str('#' in word),
	    '-1:word.contains@' : str('@' in word)
        })
    else:
        features.update({'BOS': 'BOS'})
    if i < len(doc)-1:
        word1 = doc[i+1][0]
        features.update({
            #'+1:word.lower' : word1.lower(),
            #'+1:word[-3:]' : word1[-3:],
            '+1:word[-2:]' : word1[-2:],
            #'+1:word[:3]' : word1[:3],
            '+1:word[:2]' : word1[:2],
            '+1:word.istitle' : word1.istitle(),
            '+1:word.isupper' : word1.isupper(),
            #'+1:word.isdigit' : word1.isdigit(),
            '+1:word.contains#' : str('#' in word),
            '+1:word.contains@' : str('@' in word)
        })
    else:
        features.update({'EOS': 'EOS'})
    if i > 1:
    	word1 = doc[i-2][0]
        features.update({
            #'-2:word.lower' : word1.lower(),
            #'-2:word[-3:]' : word1[-3:],
            '-2:word[-2:]' : word1[-2:],
            #'-2:word[:3]' : word1[:3],
            '-2:word[:2]' : word1[:2],
            '-2:word.istitle' : word1.istitle(),
            '-2:word.isupper' : word1.isupper(),
            #'-2:word.isdigit' : word1.isdigit(),
            '-2:word.contains#' : str('#' in word),
            '-2:word.contains@' : str('@' in word)
        })
    if i < len(doc)-2:
        word1 = doc[i+2][0]
        features.update({
            #'+2:word.lower' : word1.lower(),
            #'+2:word[-3:]' : word1[-3:],
            '+2:word[-2:]' : word1[-2:],
            #'+2:word[:3]' : word1[:3],
            '+2:word[:2]' : word1[:2],
            '+2:word.istitle' : word1.istitle(),
            '+2:word.isupper' : word1.isupper(),
            #'+2:word.isdigit' : word1.isdigit(),
            '+2:word.contains#' : str('#' in word),
            '+2:word.contains@' : str('@' in word)
        })
    if i > 2:
    	word1 = doc[i-3][0]
        features.update({
            #'-3:word.lower' : word1.lower(),
            #'-3:word[-3:]' : word1[-3:],
            '-3:word[-2:]' : word1[-2:],
            #'-3:word[:3]' : word1[:3],
            '-3:word[:2]' : word1[:2],
            '-3:word.istitle' : word1.istitle(),
            '-3:word.isupper' : word1.isupper(),
            #'-3:word.isdigit' : word1.isdigit(),
            '-3:word.contains#' : str('#' in word),
            '-3:word.contains@' : str('@' in word)
        })
    if i < len(doc)-3:
        word1 = doc[i+3][0]
        features.update({
            #'+3:word.lower' : word1.lower(),
            #'+3:word[-3:]' : word1[-3:],
            '+3:word[-2:]' : word1[-2:],
            #'+3:word[:3]' : word1[:3],
            '+3:word[:2]' : word1[:2],
            '+3:word.istitle' : word1.istitle(),
            '+3:word.isupper' : word1.isupper(),
            #'+3:word.isdigit' : word1.isdigit(),
            '+3:word.contains#' : str('#' in word),
            '+3:word.contains@' : str('@' in word)
        })
    return features

# Main function
c=1
data_read = json.load(open_file)
data = []
for tweet in data_read:
	aspects = tweet['aspects']
	text = tweet['text'].split(' ')
	tags = ["N"]*len(text)
	for aspect in aspects:
		for asp in aspect.split(' '):
			cnt = 0
			for i in range(len(text)):
				text[i] = text[i].strip('.').strip(',').strip('!')
			index = text.index(asp)
			tags[index] = "A"
	count = 0
	l = []
	for i in range(len(text)):
		l.append((text[i], tags[i]))
	data.append(l)
	c+=1
#shuffle(data)

vec = DictVectorizer()
X = []
for doc in data:
    for i in range(len(doc)):
        X.append(word2features(doc, i))

y = []
for doc in data:
	for (token, label) in doc:
		y.append(label)
l_corpus = len(X)
del data_read
del data
print len(X)
print len(y)
Recall = []
print 'Abhi'
X_vectorized = vec.fit_transform(X)
del X
X = np.array(X_vectorized.toarray())
del X_vectorized
print X[2]

for i in range(5):
	X_train = np.concatenate((X[:(l_corpus*i)/5], X[(l_corpus*(i+1))/5 : ]))
	y_train = np.concatenate((y[:(l_corpus*i)/5], y[(l_corpus*(i+1))/5 : ]))
	X_test = X[(l_corpus*i)/5 : (l_corpus*(i+1))/5]
	y_test = y[(l_corpus*i)/5 : (l_corpus*(i+1))/5]
    
	clf = SVC()
	clf.verbose = True
	print 'started'
	model = clf.fit(X_train, y_train)
	print 'Fit completed'
	y_pred = model.predict(X_test)
	print 'prediction completed'
	print 'Hello'
	labels = {"A": 0, "N": 1}
	predictions = np.array([labels[tag] for row in y_pred for tag in row])
	truths = np.array([labels[tag] for row in y_test for tag in row])
	
	print predictions
	print truths
	
	aspects_matched = 0
	count_aspects = 0
	for i in range(len(predictions)):
		if predictions[i] == truths[i] and predictions[i] == 0:
			aspects_matched += 1
		if truths[i] == 0:
			count_aspects += 1
	print aspects_matched
	print count_aspects
	print aspects_matched/float(count_aspects)
	
	Recall.append(aspects_matched/float(count_aspects))

print Recall
print (Recall[0]+Recall[1]+Recall[2]+Recall[3]+Recall[4])/float(5)

# Print out the classification report
# print(classification_report(truths, predictions, target_names=["A", "N"]))
