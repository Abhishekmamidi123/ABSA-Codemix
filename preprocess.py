import json

f = open('data/tagged_text.txt','w')


def readData(file_name):
	global data
	with open(file_name) as json_data:
		data = json.load(json_data)

def extractTaggedText():
	for tweet in data:
		f.write(tweet['lang_tagged_text'].encode('utf-8'))
		f.write('\n')

file_name = 'data/train_data.json'
readData(file_name)
extractTaggedText()
