#########################################################################################################
# This code file is to merge all the smaller files of the transliterated data into the Devnagari script # 
#########################################################################################################

import os
from string import ascii_lowercase

data_file = open('hindiData.txt','a') #file into which all the data is being merged
source = '/home/vagdevi/Documents/Honors/ABSA/ABSA_Amitavasir_data/codemix_HI_version' #location of folder containing data files
for root, dirs, filenames in os.walk(source):
	for char1 in ascii_lowercase:
		try:
			file_series = 'x'+char1 
			for char2 in ascii_lowercase:
				try:
					file_name = file_series + char2 + '.txt'
					print file_name
					fullpath=os.path.join(source,file_name)
					f = open(fullpath,'r')
					for line in f:
						data_file.write(line)
				except:
					pass	
		except:	
			pass			



















'''for root, dirs, filenames in os.walk(source):
    for f in filenames:
        print f
	fullpath=os.path.join(source,f)
	r=open(fullpath,'r')
	for i in r:
		actual_file.write(i)
	actual_file.write("-----------------------------------------------------------------------")	
		
'''
