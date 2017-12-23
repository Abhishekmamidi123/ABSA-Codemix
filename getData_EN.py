##################################################################
# This code file gets the raw tweets written in the English text # 
##################################################################

import json

f = open('englishData.txt','w')


def readData(file_name):
	global data
	with open(file_name) as json_data:
		data = json.load(json_data)
		

def extractTaggedText():
	for tweet in data:
		try:
			
			text=""
			tweet_word_list = tweet['lang_tagged_text'].split()
			for index in range(len(tweet_word_list)):
				actual_word = tweet_word_list[index][:-3]
				text = text + actual_word
				if index < len(tweet_word_list)-1:
					text = text + " "			
			f.write(text)
			f.write('\n')
		except:
			f.write("")

file_name = 'train_codemixed.json'
readData(file_name)
extractTaggedText()


