import json
file_name = 'changedData.json'
f = open('final_codemix_data.json','w')
golden_file = open('golden_set_aspects.txt', 'r')

golden_aspects = golden_file.readlines()

with open(file_name) as json_data:
	data = json.load(json_data)

final_data = []
for i in range(len(golden_aspects)):
	if golden_aspects[i]!='\n' and ('=' not in golden_aspects[i]):
		l = golden_aspects[i].split('|')
		l[-1] = l[-1][:len(l[-1])-1]
		data[i]['aspects'] = l
		final_data.append(data[i])

json.dump(final_data, f, indent=4)
print "Total number of tweets: " + str(len(final_data))
