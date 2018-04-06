import json
import string
import validators
from nltk.corpus import stopwords
exclude = set(string.punctuation)
english_stopwords = set(stopwords.words('english'))
english_stopwords.add('')
hindi_stopwords = set([u'hai', u'ki', u'ho', u'ko', u'ke', u'ka', u'h', u'se', u'bhi', u'hi', u'aap', u'u', u'k', u'ye', u'aur', u'p', u'tha', u'kya', u'kar', u'ji', u'd', u'ek', u'koi', u'nhi', u'mein', u'ne', u'pe', u'na', u'toh', u'kuch', u'ab', u'jo', u'httpURL', u'sab', u'par', u'hain', u'rt', u'b', u'2', u'tu', u'mai', u'hum', u'thi', u'main', u'apne', u'ni', u'kr', u'yaar', u'im', u'ha', u'wo', u'aa', u'v', u'hu', u'de', u'ap', u'amp', u'3', u'ur', u'r', u'ya', u'n', u'its', u'4', u'1', u'hua', u'1st', u'gya', u'yeh', u'le', u'apni'])
stop_words = hindi_stopwords|english_stopwords

# print stop_words
# print len(stop_words)

filename = '../../refinedData/final_codemix_data.json'
open_file = open(filename, 'r')
c=1
data_read = json.load(open_file)
data = []
y_tags = []
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
		if validators.url(text[i]) != True:
			l.append(text[i].lower())
	y_tags.append(tags)
	data.append(l)
print data
def clean(doc):
	# print doc
	stop_free = " ".join([i for i in doc if i.lower() not in stop_words])
	punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
	return punc_free
data = [clean(doc).split() for doc in data]

words = []
counts = []
for sentence in data:
	for word in sentence:
		if word not in words:
			if word not in stop_words:
				words.append(word)
				counts.append(1)
		else:
			index = words.index(word)
			counts[index]+=1
print len(words)
print len(counts)

words_and_counts = zip(counts, words)
words_and_counts.sort()
words_and_counts = words_and_counts[::-1]
# print words_and_counts
print len(words_and_counts)

words_with_num = []
for count in range(len(words_and_counts)):
	words_with_num.append((count+1, words_and_counts[count][1]))
# Top 6000 words
words_with_num = words_with_num[:6000]

dictionary = {}
words_to_num = {}
num_to_words = {}

for word in words_with_num:
	words_to_num[word[1]] = word[0]
	num_to_words[word[0]] = word[1]

dictionary['words_to_num'] = words_to_num
dictionary['num_to_words'] = num_to_words

# print data

# Representing Data in-terms of numbers
final_data_representation = []
for sentence in data:
	l = []
	for word in sentence:
		try:
			l.append(words_to_num[word])
		except:
			l.append(0)
	final_data_representation.append(l)
# print final_data_representation

with open('X_data.txt', 'w') as file:
	file.write(str(final_data_representation))

tag_num = {'A':0, 'N':1}

print y_tags
for i in range(len(y_tags)):
	for j in range(len(y_tags[i])):
		y_tags[i][j] = tag_num[y_tags[i][j]]
print y_tags

with open('y_data.txt', 'w') as file:
	file.write(str(y_tags))
