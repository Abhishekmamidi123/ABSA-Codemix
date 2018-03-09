import json

filename = '../final_codemix_data.json'
open_file = open(filename, 'r')

data_read = json.load(open_file)
print data_read

c=0
data = []
for tweet in data_read:
	aspects = tweet['aspects']
	text = tweet['text'].split(' ')
	tags = ["N"]*len(text)
	for aspect in aspects:
		for asp in aspect.split(' '):
			cnt = 0
			for i in range(len(text)):
				text[i] = text[i].strip('.').strip(',').strip('!')
			index = text.index(asp)
			tags[index] = "A"
	count = 0
	l = []
	for i in range(len(text)):
		l.append((text[i], tags[i]))
	data.append(l)
	c+=1


print data
print len(data) # 3169

# 1900
# 633
# 633

train = open('train.txt', 'w')
valid = open('valid.txt', 'w')
test = open('test.txt', 'w')

total_sentences = len(data)
count = 0
for sentence in data:
	if count < total_sentences*0.6:
		for word,tag in sentence:
			train.write(word+'\t'+tag)
			train.write('\n')
		train.write('\n')
	elif count >= total_sentences*0.6 and count <= total_sentences*0.8:
		for word,tag in sentence:
			valid.write(word+'\t'+tag)
			valid.write('\n')
		valid.write('\n')
	else:
		for word,tag in sentence:
			test.write(word+'\t'+tag)
			test.write('\n')
		test.write('\n')
	count+=1
