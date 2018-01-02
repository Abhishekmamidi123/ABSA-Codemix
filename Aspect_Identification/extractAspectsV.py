import os
import nltk
from nltk.tag import pos_tag

text_file = open("../data/hindiTransliteratedData.txt", "r")
# text_file = open("../data/Hi.txt", "r")
hindiData = text_file.readlines()

f1 = open('viterbi/tagfile.txt', 'w')

path='../data/tagged_text.txt'
# path='../data/En.txt'
with open(path) as f:
	lineCount=0
	for line in f:
		splittedLine = line.split(' ')
		size = len(splittedLine)
		# lastWord = splittedLine[size-1]
		# splittedLine[size-1] = lastWord[:len(lastWord)-1]
		print splittedLine
		hindiLine = hindiData[lineCount].split(' ')
		print hindiLine
		wordIndex=0
		for taggedWord in splittedLine:
			print wordIndex, size
			print taggedWord
			l = len(taggedWord)
			word = taggedWord[:l-3]
			language = taggedWord[l-2:]
			if language == 'HI':
				# NN NNP
				print '*******************'
				print len(hindiLine)
				print hindiLine[wordIndex]
				f1.write(hindiLine[wordIndex])
				f1.write("\n")
			elif wordIndex == size-2 and language != 'HI':
				print "vaggggggggggggggggggggggggggg"
				f1.write("\n")
			wordIndex+=1
		lineCount+=1
print 'done'
f1.close()
f.close()
os.chdir("viterbi")
os.system('ls')
out = os.popen('python viterbi.py').read()
open("tags.txt", "w").write(out)
print out
print out.split('\n')
os.chdir('..')
print '\n'

outFile = open("predictedPOS.txt", 'w')
tags = open("viterbi/tags.txt", "r").readlines()
tagCount = 0
with open(path) as f:
	lineCount=0
	for line in f:
		posSent = ''
		splittedLine = line.split(' ')
		size = len(splittedLine)
		# lastWord = splittedLine[size-1]
		# splittedLine[size-1] = lastWord[:len(lastWord)-1]
		print splittedLine
		hindiLine = hindiData[lineCount].split(' ')
		wordIndex=0
		for taggedWord in splittedLine:
			# print taggedWord
			l = len(taggedWord)
			word = taggedWord[:l-3]
			language = taggedWord[l-2:]
			if language == 'EN':
			 	tag = nltk.pos_tag([word])
				pos = tag[0][1]
				# print word, pos
				posSent = posSent + str(pos) + ' '
			elif language == 'HI':
				# NN NNP
				tag = tags[tagCount]
				pos = tag[3:len(tag)-3]
				tagCount+=1
				posSent = posSent + str(pos) + ' '
			else:
				posSent = posSent + 'PUNC' + ' '
			wordIndex+=1
		print "POS Sentence:"
		print posSent
		outFile.write(posSent)
		outFile.write("\n")
		tagCount+=1
		lineCount+=1
