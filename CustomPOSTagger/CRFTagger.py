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
print len(data)
# Divide data into train and test sets
eightyPercent = count*0.9
training_set = data[0:int(eightyPercent)]
test_set = data[int(eightyPercent):]

# Train
ct = CRFTagger()
train_data = training_set
ct.train(train_data, 'model.crf.tagger')

# Accuracy
gold_sentences = test_set
print ct.evaluate(gold_sentences)

print "Give a sentence..."
# Test
test_sent = raw_input()
test_sent = test_sent.encode('utf-8').decode('utf-8').split(' ')
# print test_sent
print ct.tag_sents([test_sent])
