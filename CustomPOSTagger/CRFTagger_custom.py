from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
np.set_printoptions(threshold=np.nan)
from xml.etree import cElementTree as ET
from nltk.tag import CRFTagger
from random import shuffle
import pycrfsuite
import io

def word2features(doc, i):
    word = doc[i][0]
    # postag = doc[i][1]

    # Common features for all words
    features = [
        'bias',
        'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit(),
        # 'postag=' + postag
    ]

    # Features for words that are not
    # at the beginning of a document
    if i > 0:
        word1 = doc[i-1][0]
        #postag1 = doc[i-1][1]
        features.extend([
            '-1:word.lower=' + word1.lower(),
            '-1:word.istitle=%s' % word1.istitle(),
            '-1:word.isupper=%s' % word1.isupper(),
            '-1:word.isdigit=%s' % word1.isdigit()
    #        '-1:postag=' + postag1
        ])
    else:
        # Indicate that it is the 'beginning of a document'
        features.append('BOS')

    # Features for words that are not
    # at the end of a document
    if i < len(doc)-1:
        word1 = doc[i+1][0]
        #postag1 = doc[i+1][1]
        features.extend([
            '+1:word.lower=' + word1.lower(),
            '+1:word.istitle=%s' % word1.istitle(),
            '+1:word.isupper=%s' % word1.isupper(),
            '+1:word.isdigit=%s' % word1.isdigit()
#            '+1:postag=' + postag1
        ])
    else:
        # Indicate that it is the 'end of a document'
        features.append('EOS')

    return features
    
def extract_features(doc):
    return [word2features(doc, i) for i in range(len(doc))]

def get_labels(doc):
    return [postag for (token, postag) in doc]

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
#print data

# eightyPercent = count*0.9
# training_set = data[0:int(eightyPercent)]
# test_set = data[int(eightyPercent):]

X = [extract_features(doc) for doc in data]
y = [get_labels(doc) for doc in data]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print len(X), len(X_train), len(X_test)

trainer = pycrfsuite.Trainer(verbose=False)

# Submit training data to the trainer
for xseq, yseq in zip(X_train, y_train):
    trainer.append(xseq, yseq)
    
trainer.set_params({
    'c1': 0.1,
    'c2': 0.01,  
    'max_iterations': 200,
    'feature.possible_transitions': True
})
trainer.train('crf.model')

tagger = pycrfsuite.Tagger()
tagger.open('crf.model')
#y_pred = [tagger.tag(xseq) for xseq in X_test]
for i in X_test:
	print tagger.tag(i)
print "-=------------------"
print type(i)
print tagger.tag(u"mera bharat mahan")

i = 12
#for x, y in zip(y_pred[i], [x[1].split("=")[1] for x in X_test[i]]):
    #print("%s (%s)" % (y, x))

# Create a mapping of labels to indices
labels = {"G_PRT": 0, "G_X": 1, "E": 2, "PSP": 3, "DT": 4, "G_N": 5, "U": 6, "CC": 7, "G_V": 8, "G_J": 9, "@": 10, "G_SYM": 11, "G_R": 12, "$": 13, "G_PRP": 14, "#": 15, "~": 16, "null": 17}

# labels = {"N": 1, "I": 0}

# Convert the sequences of tags into a 1-dimensional array
predictions = np.array([labels[tag] for row in y_pred for tag in row])
truths = np.array([labels[tag] for row in y_test for tag in row])
print predictions
print truths
if np.array_equal(predictions,truths):
	print "L"
else:
	print "K"

test_sent = raw_input()
test_sent = test_sent.encode('utf-8').decode('utf-8').split(' ')
# print test_sent
print ct.tag_sents([test_sent])

# Print out the classification report
# print(classification_report(truths, predictions, target_names=["G_PRT", "G_X", "E", "PSP", "DT", "G_N", "U", "CC", "G_V", "G_J", "@", "G_SYM", "G_R", "$", "G_PRP", "#", "~", "null"]))
