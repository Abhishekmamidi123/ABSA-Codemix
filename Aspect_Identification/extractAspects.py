import os
import nltk
from nltk.tag import pos_tag

text_file = open("../data/Hi.txt", "r")
hindiData = text_file.readlines()
print 'Completed reading Hindi Transliterated data.'
print 'Reading tweets to find POS tags'
path='../data/En.txt'
with open(path) as f:
	lineCount=0
	for line in f:
		splittedLine = line.split(' ')
		hindiLine = hindiData[lineCount].split(' ')
		wordIndex=0
		for taggedWord in splittedLine:
			l = len(taggedWord)
			word = taggedWord[:l-3]
			language = taggedWord[l-2:]
			if language == 'EN':
				# 
				tag = nltk.pos_tag([word])
				pos = tag[0][1]
				print word, pos
			elif language == 'HI':
				# NN NNP
				print '*******************'
				print hindiLine[wordIndex]
				os.chdir("HindiPOS")
				f = open('my_input.txt', 'w')
				#f = open('my_output.txt', 'w')
				f.write(hindiLine[wordIndex])
				f.close()
				os.system('make tag')
				os.system('ls')
				f = open("my_output.txt", "r").readlines()
				print f[0].split('\t')[2]
				print f
				os.chdir('..')
				print hindiLine[wordIndex]
			wordIndex+=1
		lineCount+=1
print 'done'
