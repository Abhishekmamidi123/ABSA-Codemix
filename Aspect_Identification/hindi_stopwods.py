import json
import string
from nltk.corpus import stopwords 
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

stop.add('')
def clean(doc):
	# print doc
	stop_free = " ".join([i for i in doc if i.lower() not in stop])
	punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
	return punc_free
data = [clean(doc).split() for doc in data]

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

words_and_counts = zip(counts, words)
words_and_counts.sort()
words_and_counts = words_and_counts[::-1]
print words_and_counts[:200]




# Stop words - Top 200 words sorted based on count.
# [(658, u'hai'), (439, u'ki'), (337, u'bhai'), (330, u'ho'), (312, u'ko'), (297, u'ke'), (293, u'ka'), (263, u'h'), (261, u'se'), (218, u'bhi'), (193, u'salman'), (191, u'hi'), (187, u'someUSER'), (186, u'aap'), (179, u'u'), (176, u'nahi'), (167, u'k'), (157, u'ye'), (149, u'aur'), (140, u'p'), (135, u'tha'), (134, u'guddu'), (132, u'kya'), (129, u'kar'), (126, u'ji'), (121, u'love'), (116, u'd'), (111, u'india'), (108, u'ek'), (107, u'koi'), (104, u'nhi'), (99, u'movie'), (94, u'day'), (92, u'modi'), (91, u'tomorrow'), (91, u'sir'), (89, u'mein'), (89, u'Salman'), (87, u'good'), (85, u'ne'), (85, u'best'), (84, u'pe'), (83, u'na'), (80, u'toh'), (80, u'time'), (80, u'kuch'), (80, u'ab'), (78, u'jo'), (77, u'httpURL'), (75, u'like'), (73, u'sab'), (72, u'par'), (72, u'may'), (70, u'hain'), (70, u'delhi'), (69, u'liye'), (67, u'rt'), (67, u'film'), (64, u'desh'), (63, u'gaya'), (62, u'khan'), (61, u'b'), (60, u'one'), (60, u'hota'), (60, u'bjp'), (58, u'2'), (57, u'hit'), (56, u'tu'), (56, u'mai'), (56, u'hum'), (56, u'aaj'), (53, u'thi'), (53, u'main'), (53, u'kejriwal'), (52, u'rahe'), (52, u'new'), (51, u'raha'), (51, u'game'), (51, u'din'), (50, u'apne'), (49, u'night'), (49, u'ni'), (49, u'great'), (48, u'school'), (48, u'diya'), (47, u'see'), (47, u'dont'), (47, u'cant'), (47, u'bhaijaan'), (47, u'Bhai'), (46, u'kr'), (46, u'kiya'), (46, u'bahut'), (45, u'yaar'), (45, u'mere'), (45, u'match'), (45, u'life'), (45, u'im'), (45, u'ha'), (45, u'aapsweep'), (44, u'gurmeetramrahim'), (44, u'go'), (43, u'wo'), (43, u'hoga'), (43, u'going'), (43, u'baat'), (43, u'aa'), (42, u'party'), (42, u'bajrangi'), (41, u'v'), (41, u'mera'), (41, u'hu'), (41, u'de'), (41, u'ap'), (41, u'amp'), (41, u'3'), (40, u'world'), (40, u'ur'), (40, u'karo'), (40, u'free'), (38, u'sallu'), (38, u'r'), (38, u'log'), (38, u'indvspak'), (38, u'first'), (37, u'ya'), (37, u'wale'), (37, u'papa'), (37, u'hogi'), (37, u'beefban'), (37, u'bar'), (36, u'nice'), (36, u'man'), (36, u'karte'), (36, u'jai'), (36, u'fan'), (36, u'dil'), (35, u'wait'), (35, u'super'), (35, u'song'), (35, u'sirf'), (35, u'show'), (35, u'people'), (35, u'n'), (35, u'maa'), (35, u'jaan'), (35, u'its'), (35, u'get'), (35, u'baar'), (34, u'vote'), (34, u'sath'), (34, u'last'), (34, u'4'), (34, u'1'), (33, u'hua'), (33, u'garbage'), (33, u'1st'), (32, u'meri'), (32, u'gya'), (32, u'bin'), (32, u'better'), (32, u'anna'), (32, u'aisa'), (31, u'yeh'), (31, u'year'), (31, u'well'), (31, u'wala'), (31, u'post'), (31, u'pakistan'), (31, u'know'), (31, u'kabhi'), (31, u'indvssa'), (31, u'days'), (30, u'sahi'), (30, u'naam'), (30, u'lol'), (30, u'kam'), (30, u'agar'), (30, u'Modi'), (29, u'us'), (29, u'sakta'), (29, u'railbudget2015'), (29, u'karna'), (29, u'har'), (29, u'happy'), (28, u'thursday'), (28, u'think'), (28, u'tak'), (28, u'saturday'), (28, u'pm'), (28, u'news'), (28, u'nai'), (28, u'mat'), (28, u'le'), (28, u'karne'), (28, u'hoti'), (28, u'friday'), (28, u'apni'), (28, u'always'), (27, u'page')]


# [(658, u'hai'), (439, u'ki'), (330, u'ho'), (312, u'ko'), (297, u'ke'), (293, u'ka'), (263, u'h'), (261, u'se'), (218, u'bhi'), (191, u'hi'), (186, u'aap'), (179, u'u'), (167, u'k'), (157, u'ye'), (149, u'aur'), (140, u'p'), (135, u'tha'), (132, u'kya'), (129, u'kar'), (126, u'ji'), (116, u'd'), (108, u'ek'), (107, u'koi'), (104, u'nhi'), (89, u'mein'), (85, u'ne'), (84, u'pe'), (83, u'na'), (80, u'toh'), (80, u'kuch'), (80, u'ab'), (78, u'jo'), (77, u'httpURL'), (73, u'sab'), (72, u'par'), (70, u'hain'), (67, u'rt'), (61, u'b'), (58, u'2'), (56, u'tu'), (56, u'mai'), (56, u'hum'), (53, u'thi'), (53, u'main'), (50, u'apne'), (49, u'ni'), (46, u'kr'), (45, u'yaar'), (45, u'im'), (45, u'ha'), (43, u'wo'), (43, u'aa'), (41, u'v'), (41, u'hu'), (41, u'de'), (41, u'ap'), (41, u'amp'), (41, u'3'), (40, u'ur'), (38, u'r'), (37, u'ya'), (35, u'n'), (35, u'its'), (34, u'4'), (34, u'1'), (33, u'hua'), (33, u'1st'), (32, u'gya'), (31, u'yeh'), (28, u'le'), (28, u'apni')]

# Stop words
# [u'hai', u'ki', u'ho', u'ko', u'ke', u'ka', u'h', u'se', u'bhi', u'hi', u'aap', u'u', u'k', u'ye', u'aur', u'p', u'tha', u'kya', u'kar', u'ji', u'd', u'ek', u'koi', u'nhi', u'mein', u'ne', u'pe', u'na', u'toh', u'kuch', u'ab', u'jo', u'httpURL', u'sab', u'par', u'hain', u'rt', u'b', u'2', u'tu', u'mai', u'hum', u'thi', u'main', u'apne', u'ni', u'kr', u'yaar', u'im', u'ha', u'wo', u'aa', u'v', u'hu', u'de', u'ap', u'amp', u'3', u'ur', u'r', u'ya', u'n', u'its', u'4', u'1', u'hua', u'1st', u'gya', u'yeh', u'le', u'apni']

# set([u'all', u'just', u'being', u'over', u'both', u'through', u'yourselves', u'its', u'before', u'o', u'hadn', u'herself', u'll', u'had', u'should', u'to', u'only', u'won', u'under', u'ours', u'has', u'do', u'them', u'his', u'very', u'they', u'not', u'during', u'now', u'him', u'nor', u'd', u'did', u'didn', u'this', u'she', u'each', u'further', u'where', u'few', u'because', u'doing', u'some', u'hasn', u'are', u'our', u'ourselves', u'out', u'what', u'for', u'while', u're', u'does', u'above', u'between', u'mustn', u't', u'be', u'we', u'who', u'were', u'here', u'shouldn', u'hers', u'by', u'on', u'about', u'couldn', u'of', u'against', u's', u'isn', u'or', u'own', u'into', u'yourself', u'down', u'mightn', u'wasn', u'your', u'from', u'her', u'their', u'aren', u'there', u'been', u'whom', u'too', u'wouldn', u'themselves', u'weren', u'was', u'until', u'more', u'himself', u'that', u'but', u'don', u'with', u'than', u'those', u'he', u'me', u'myself', u'ma', u'these', u'up', u'will', u'below', u'ain', u'can', u'theirs', u'my', u'and', u've', u'then', u'is', u'am', u'it', u'doesn', u'an', u'as', u'itself', u'at', u'have', u'in', u'any', u'if', u'again', u'no', u'when', u'same', u'how', u'other', u'which', u'you', u'shan', u'needn', u'haven', u'after', u'most', u'such', u'why', u'a', u'off', u'i', u'm', u'yours', u'so', u'y', u'the', u'having', u'once'])
