import io
from nltk.tag import CRFTagger
from xml.etree import cElementTree as ET
from random import shuffle

root = ET.fromstring(io.open('Hi-En_data.xml',encoding='utf-8').read())
count = 0
data = []
for page in list(root):
    l = []
    text = page.find('text').text.decode('utf8')
    language = page.find('language').text.decode('utf8')
    pos = page.find('pos_tags').text.decode('utf8')
    splitText = text.split(" ")[1:-1]
    posText = pos.split(" ")[1:-1]
    for i in range(len(splitText)):
        l.append((splitText[i], posText[i]))
    data.append(l)
    count = count + 1
shuffle(data)
print data

uniqueTags = []
for sentence in data:
	for word in sentence:
		if word[1] not in uniqueTags:
			uniqueTags.append(word[1])
print uniqueTags
