''' Remove neutral sentences'''

import json
text_file = open("hindiTransliteratedData.txt", "r")
hindiData = text_file.readlines()
f = open("hindiTransliteratedData_new.txt", "w")

text_file = open("predictedPOS.txt", "r")
predictedPOS = text_file.readlines()
f1 = open("predictedPOS_new.txt", "w")

f2 = open("tagged_text_new.txt", "w")

def readData(file_name):
	global data
	with open(file_name) as json_data:
		data = json.load(json_data)

def changeData():
	cnt = 0
	l = []	
	for tweet in data:
		print cnt
		if tweet['sentiment'] != 0:
			l.append(tweet)
			f.write(hindiData[cnt])
			f1.write(predictedPOS[cnt])
			f2.write(tweet['lang_tagged_text'].encode('utf-8'))
			f2.write("\n")
		cnt+=1
	json.dump(l, open('changedData.json','w'), indent=4)
	print cnt
	print len(l)
	
file_name = 'train_data.json'
readData(file_name)
changeData()
