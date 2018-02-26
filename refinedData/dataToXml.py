import os
import lxml.etree as ET
import json

def loadData(fileName):
    with open("changedData.json") as f:
        return json.load(f)

def loadAspects(fileName):
    with open(fileName) as f:
        return f.readlines()

def txtToXml(data, aspectsData):
    count = 0
    for dic in data:
        print "========================================================"
        text = dic['text']
        print text
        print aspectsData[count][:-1]
        aspects = aspectsData[count].split('|')
        print aspects
        if len(aspects)!=0:
            aspects[-1] = aspects[-1][:len(aspects[-1])-1]
        print aspects
        indexStart = 0
        for aspect in aspects:
            index = text.find(aspect[:-1], indexStart)
            print text[indexStart : index]
            # print (text, aspect)
            # print index
            if index != -1:
                # print "Entered"
                # print indexStart
                # print index, index+len(aspect)
                print text[index:index+len(aspect)]
                indexStart = index + len(aspect)+1
            # print indexStart
        print text[indexStart:]
        # print aspect
        count+=1
        print "========================================================"
        if count == 15:
            break
    return 0

fileName = 'changedData.json'
aspectsFileName = 'golden_set_aspects.txt'
data = loadData(fileName)
aspectsData = loadAspects(aspectsFileName)
cnt = txtToXml(data, aspectsData)
