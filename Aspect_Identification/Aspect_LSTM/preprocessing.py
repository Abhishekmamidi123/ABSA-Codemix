import json
import string
from nltk.corpus import stopwords
exclude = set(string.punctuation)
english_stopwords = set(stopwords.words('english'))
english_stopwords.add('')
hindi_stopwords = set([u'hai', u'ki', u'ho', u'ko', u'ke', u'ka', u'h', u'se', u'bhi', u'hi', u'aap', u'u', u'k', u'ye', u'aur', u'p', u'tha', u'kya', u'kar', u'ji', u'd', u'ek', u'koi', u'nhi', u'mein', u'ne', u'pe', u'na', u'toh', u'kuch', u'ab', u'jo', u'httpURL', u'sab', u'par', u'hain', u'rt', u'b', u'2', u'tu', u'mai', u'hum', u'thi', u'main', u'apne', u'ni', u'kr', u'yaar', u'im', u'ha', u'wo', u'aa', u'v', u'hu', u'de', u'ap', u'amp', u'3', u'ur', u'r', u'ya', u'n', u'its', u'4', u'1', u'hua', u'1st', u'gya', u'yeh', u'le', u'apni'])
stop_words = hindi_stopwords|english_stopwords

print stop_words
print len(stop_words)

filename = '../../refinedData/final_codemix_data.json'
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
print data

words = []
counts = []
for sentence in data:
	for word in sentence:
		if word not in words:
			words.append(word)
			counts.append(0)
		if word in words:
			index = words.index(word)
			counts[index]+=1
print len(words)
print len(counts)
		
