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
        # 'word.position=%s' % str(i),
        'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word[:3]=' + word[:3],
        'word[:2]=' + word[:2],
        'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        #'word.isdigit=%s' % word.isdigit(),
        'word.contains#=%s' % str('#' in word),
        'word.contains@=%s' % str('@' in word)
    ]
    if i > 0:
        word1 = doc[i-1][0]
        features.extend([
            '-1:word.lower=' + word1.lower(),
            '-1:word[-3:]=' + word1[-3:],
            '-1:word[-2:]=' + word1[-2:],
            '-1:word[:3]=' + word1[:3],
            '-1:word[:2]=' + word1[:2],
            '-1:word.istitle=%s' % word1.istitle(),
            '-1:word.isupper=%s' % word1.isupper(),
            #'-1:word.isdigit=%s' % word1.isdigit(),
	    '-1:word.contains#=%s' % str('#' in word),
	    '-1:word.contains@=%s' % str('@' in word)
        ])
    else:
        features.append('BOS')
    if i < len(doc)-1:
        word1 = doc[i+1][0]
        features.extend([
            '+1:word.lower=' + word1.lower(),
            '+1:word[-3:]=' + word1[-3:],
            '+1:word[-2:]=' + word1[-2:],
            '+1:word[:3]=' + word1[:3],
            '+1:word[:2]=' + word1[:2],
            '+1:word.istitle=%s' % word1.istitle(),
            '+1:word.isupper=%s' % word1.isupper(),
            #'+1:word.isdigit=%s' % word1.isdigit(),
            '+1:word.contains#=%s' % str('#' in word),
            '+1:word.contains@=%s' % str('@' in word)
        ])
    else:
        features.append('EOS')
    if i > 1:
    	word1 = doc[i-2][0]
        features.extend([
            '-2:word.lower=' + word1.lower(),
            '-2:word[-3:]=' + word1[-3:],
            '-2:word[-2:]=' + word1[-2:],
            '-2:word[:3]=' + word1[:3],
            '-2:word[:2]=' + word1[:2],
            '-2:word.istitle=%s' % word1.istitle(),
            '-2:word.isupper=%s' % word1.isupper(),
            #'-2:word.isdigit=%s' % word1.isdigit(),
            '-2:word.contains#=%s' % str('#' in word),
            '-2:word.contains@=%s' % str('@' in word)
        ])
    if i < len(doc)-2:
        word1 = doc[i+2][0]
        features.extend([
            '+2:word.lower=' + word1.lower(),
            '+2:word[-3:]=' + word1[-3:],
            '+2:word[-2:]=' + word1[-2:],
            '+2:word[:3]=' + word1[:3],
            '+2:word[:2]=' + word1[:2],
            '+2:word.istitle=%s' % word1.istitle(),
            '+2:word.isupper=%s' % word1.isupper(),
            #'+2:word.isdigit=%s' % word1.isdigit(),
            '+2:word.contains#=%s' % str('#' in word),
            '+2:word.contains@=%s' % str('@' in word)
        ])
    if i > 2:
    	word1 = doc[i-3][0]
        features.extend([
            '-3:word.lower=' + word1.lower(),
            '-3:word[-3:]=' + word1[-3:],
            '-3:word[-2:]=' + word1[-2:],
            '-3:word[:3]=' + word1[:3],
            '-3:word[:2]=' + word1[:2],
            '-3:word.istitle=%s' % word1.istitle(),
            '-3:word.isupper=%s' % word1.isupper(),
            '-3:word.isdigit=%s' % word1.isdigit(),
            '-3:word.contains#=%s' % str('#' in word),
            '-3:word.contains@=%s' % str('@' in word)
        ])
    if i < len(doc)-3:
        word1 = doc[i+3][0]
        features.extend([
            '+3:word.lower=' + word1.lower(),
            '+3:word[-3:]=' + word1[-3:],
            '+3:word[-2:]=' + word1[-2:],
            '+3:word[:3]=' + word1[:3],
            '+3:word[:2]=' + word1[:2],
            '+3:word.istitle=%s' % word1.istitle(),
            '+3:word.isupper=%s' % word1.isupper(),
            '+3:word.isdigit=%s' % word1.isdigit(),
            '+3:word.contains#=%s' % str('#' in word),
            '+3:word.contains@=%s' % str('@' in word)
        ])
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

X = [extract_features(doc) for doc in data]
y = [get_labels(doc) for doc in data]
print X[:1]
l_corpus = len(X)
Recall = []
print 'Abhishek'
for i in range(1):
	X_train = X[:(l_corpus*i)/5] + X[(l_corpus*(i+1))/5 : ]
	y_train = y[:(l_corpus*i)/5] + y[(l_corpus*(i+1))/5 : ]
	X_test = X[(l_corpus*i)/5 : (l_corpus*(i+1))/5]
	y_test = y[(l_corpus*i)/5 : (l_corpus*(i+1))/5]

	# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
	trainer = pycrfsuite.Trainer(verbose=True)
	for xseq, yseq in zip(X_train, y_train):
	    trainer.append(xseq, yseq)
	trainer.set_params({
	    'c1': 0.1, # 0.1
	    'c2': 0.01,  # 0.01
	    'max_iterations': 1000,
	    'feature.possible_transitions': True
	})
	
	trainer.train('crf.model')
	
	tagger = pycrfsuite.Tagger()
	tagger.open('crf.model')
	y_pred = [tagger.tag(xseq) for xseq in X_test]
	
	labels = {"A": 0, "N": 1}
	
	predictions = np.array([labels[tag] for row in y_pred for tag in row])
	truths = np.array([labels[tag] for row in y_test for tag in row])
	
	# print predictions
	# print truths
	test_sentences = data[(l_corpus*i)/5 : (l_corpus*(i+1))/5]
	print test_sentences
	print y_pred
	out_data = open('out_data.txt', 'w')
	cnt1 = 0
	for sentence in test_sentences:
		cnt2 = 0
		for word, tag in sentence:
			out_data.write(str(word)+' '+str(tag)+' '+str(y_pred[cnt1][cnt2]))
			out_data.write('\n')
			cnt2+=1
		out_data.write('\n')
		cnt1+=1
	
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
