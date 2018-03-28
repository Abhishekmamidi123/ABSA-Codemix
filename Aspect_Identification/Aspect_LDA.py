import io
import json
import pickle
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
hindi_stop_words = [u'hai', u'ki', u'ho', u'ko', u'ke', u'ka', u'h', u'se', u'bhi', u'hi', u'aap', u'u', u'k', u'ye', u'aur', u'p', u'tha', u'kya', u'kar', u'ji', u'd', u'ek', u'koi', u'nhi', u'mein', u'ne', u'pe', u'na', u'toh', u'kuch', u'ab', u'jo', u'httpURL', u'sab', u'par', u'hain', u'rt', u'b', u'2', u'tu', u'mai', u'hum', u'thi', u'main', u'apne', u'ni', u'kr', u'yaar', u'im', u'ha', u'wo', u'aa', u'v', u'hu', u'de', u'ap', u'amp', u'3', u'ur', u'r', u'ya', u'n', u'its', u'4', u'1', u'hua', u'1st', u'gya', u'yeh', u'le', u'apni']

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
# print data

new_data = []
for sentence in data:
	sent = []
	for word in sentence:
		if word not in hindi_stop_words:
			sent.append(word)
	new_data.append(sent)
data = new_data

dictionary = corpora.Dictionary(data)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in data]
# print doc_term_matrix

Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=6, id2word = dictionary, passes=50)
filehandler = open('ldamodel.obj', 'w')
pickle.dump(ldamodel, filehandler)
# print ldamodel[]

# print(ldamodel.print_topics(num_topics=3, num_words=3))
# print(ldamodel.print_topics(num_topics=4, num_words=4))
# print(ldamodel.print_topics(num_topics=5, num_words=5))
print(ldamodel.print_topics(num_topics=6, num_words=6))

print data[200]
test_sent = data[200]
# stop_free = " ".join([i for i in test_sent if i.lower() not in stop])
# test_sent = ''.join(ch for ch in stop_free if ch not in exclude)
print test_sent
test_doc = data[200]
print ldamodel[dictionary.doc2bow(test_sent)]
