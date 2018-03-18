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
import gensim
from gensim import corpora
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)

filename = '../refinedData/final_codemix_data.json'
open_file = open(filename, 'r')

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
		# l.append((text[i], tags[i]))
		l.append(text[i])
	data.append(l)
	c+=1
# print data
stop.add('')
def clean(doc):
	# print doc
	stop_free = " ".join([i for i in doc if i.lower() not in stop])
	punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
	return punc_free
data = [clean(doc).split() for doc in data]     
print data

dictionary = corpora.Dictionary(data)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in data]
print doc_term_matrix

Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=3, num_words=3))
print(ldamodel.print_topics(num_topics=4, num_words=4))
print(ldamodel.print_topics(num_topics=5, num_words=5))
print(ldamodel.print_topics(num_topics=30, num_words=30))
