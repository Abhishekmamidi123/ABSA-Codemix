import io
import json
import pickle
import gensim
from gensim import corpora
import pycrfsuite
import numpy as np
from random import shuffle
from xml.etree import cElementTree as ET
np.set_printoptions(threshold=np.nan)

def run_LDA(data):
	dictionary = corpora.Dictionary(data)
	doc_term_matrix = [dictionary.doc2bow(doc) for doc in data]
	Lda = gensim.models.ldamodel.LdaModel
	ldamodel = Lda(doc_term_matrix, num_topics=6, id2word = dictionary, passes=50)
	filehandler = open('0_ldamodel.obj', 'w')
	pickle.dump(ldamodel, filehandler)
	filehandler = open('0_dictionary.obj', 'w')
	pickle.dump(dictionary, filehandler)
	
with open('X_data.pkl', 'r') as file:
	X = pickle.load(file)

tag_num = {'N':0, 'A':1}
with open('y_data.txt', 'r') as file:
	y = eval(file.readline())

filehandler = open('0_ldamodel.obj', 'r')
ldamodel = pickle.load(filehandler)
filehandler = open('0_dictionary.obj', 'r')
dictionary = pickle.load(filehandler)

# run_LDA(X)

threshold = 0.5
count = 0
X_LDA_words = []
for sent in X:
	print '\n'
	if count == 30:
		break
	topics = ldamodel[dictionary.doc2bow(sent)]
	print sent
	print y[count]
	#print topics
	topic_ids = []
	for topic in topics:
		if topic[1] > threshold:
			topic_ids.append(topic)
	print topic_ids
	x_lda = []
	for topic in topic_ids:
		words = ldamodel.show_topic(topic[0], topn = 500)
		words = [word[0] for word in words]
		for word in sent:
			if word in words:
				x_lda.append(word)
	X_LDA_words.append(x_lda)
	count+=1
print X_LDA_words

#print X[200]
#topics = ldamodel[dictionary.doc2bow(X[200])]
#print topics
#print ldamodel.print_topics()
