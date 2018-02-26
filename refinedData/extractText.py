import json
f = open('codemixTextData.txt','w')

def readData(file_name):
	global data
	with open(file_name) as json_data:
		data = json.load(json_data)
		print len(data)		

def extractTaggedText():
	for tweet in data:
		text = tweet['text']			
		f.write(text)
		f.write('\n')

file_name = 'changedData.json'
readData(file_name)
extractTaggedText()
