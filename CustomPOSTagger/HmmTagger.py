import io
from nltk.tag import hmm
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

print len(training_set)
print len(test_set)

# Train
trainer = hmm.HiddenMarkovModelTrainer()
train_data = training_set
tagger = trainer.train_supervised(train_data)

# Test
# print tagger.tag('open a start up'.encode('utf-8').decode('utf-8').split())
# print tagger.tag('OUT nahi KARDO ISSE BAHUT HOGAYA aaj Salman'.encode('utf-8').decode('utf-8').split())

# Accuracy
gold_sentences = test_set
print tagger.evaluate(gold_sentences)
