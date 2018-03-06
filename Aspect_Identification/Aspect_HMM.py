import io
import json
import numpy as np
from nltk.tag import hmm
from random import shuffle
from xml.etree import cElementTree as ET
from sklearn.metrics import classification_report

c=1
filename = '../refinedData/final_codemix_data.json'
open_file = open(filename, 'r')
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

shuffle(data)

# Divide data into train and test sets
eightyPercent = c*0.9
training_set = data[0:int(eightyPercent)]
test_set = data[int(eightyPercent):]

print len(training_set)
print len(test_set)
print test_set[:5]
# Train
trainer = hmm.HiddenMarkovModelTrainer()
train_data = training_set
tagger = trainer.train_supervised(train_data)


y_pred = []
for sent in test_set:
	tag_sent = []
	for word in sent:
		tag_sent.append(word[0])
	tags =  tagger.tag(tag_sent)
	for word in tags:
		y_pred.append(word[1])

predictions = np.array([tag for row in y_pred for tag in row])
truths = np.array([item[1] for row in test_set for item in row])

print(classification_report(truths, predictions, target_names=["A", "N"]))

# Accuracy
# gold_sentences = test_set
# print tagger.evaluate(gold_sentences)

# print tagger.tag(['I', 'love', 'India'])
