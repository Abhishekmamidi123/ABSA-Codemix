from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction import FeatureHasher
from sklearn.svm import SVC
import nltk
import numpy as np

data = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]

pos_window = [
    {
        'word-2': 'the',
        'pos-2': 'DT',
        'word-1': 'cat',
        'pos-1': 'NN',
        'word+1': 'on',
        'pos+1': 'PP',
    },
    {
        'word-2': 'Abhi',
        'pos-2': 'NN',
        'word-1': 'is',
        'pos-1': 'IND',
        'word+1': 'good',
        'pos+1': 'ADJ',
    },
]

def word2features(doc, i):
    word = doc[i]
    print word
    features = {
        'word': word.lower(),
        'word.isupper': word.isupper(),
        'word.istitle': word.istitle(),
    }
    return features
	
vec = DictVectorizer()
feature_vector = []
for doc in data:
    doc = doc.split(' ')
    print doc
    for i in range(len(doc)):
        feature_vector.append(word2features(doc, i))

print feature_vector
pos_vectorized = vec.fit_transform(feature_vector)
print len(pos_vectorized.toarray())
print pos_vectorized.toarray()
print vec.get_feature_names()

X = np.array(pos_vectorized.toarray())
print X[2:4].shape
print X[5:8].shape

Y = np.concatenate((X[2:4],X[5:8]))
print Y.shape

labels = ['N', 'N', 'N', 'N', 'A', 'N', 'N', 'N', 'N', 'N', 'A', 'N', 'N', 'A', 'N', 'N', 'N', 'N', 'N', 'A']
print len(labels)

model = SVC().fit(np.array(pos_vectorized.toarray()), labels)
print model



tests = [[ 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.], [ 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.]]
print(model.predict(tests))
