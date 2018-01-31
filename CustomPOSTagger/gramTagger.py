import io
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
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

# Divide data into train and test sets
eightyPercent = count*0.9
training_set = data[0:int(eightyPercent)]
test_set = data[int(eightyPercent):]

# Train
train_data = training_set
tag1 = DefaultTagger('NN')
tag2 = UnigramTagger(train_data, backoff = tag1)
tag3 = BigramTagger(train_data, backoff = tag2)
tag4 = TrigramTagger(train_data, backoff = tag3)

# Accuracy
# print tag4.tag('open a start up'.encode('utf-8').decode('utf-8').split())
# print tag4.tag('OUT nahi KARDO ISSE BAHUT HOGAYA aaj Salman'.encode('utf-8').decode('utf-8').split())
gold_sentences = test_set
print tag4.evaluate(gold_sentences)
