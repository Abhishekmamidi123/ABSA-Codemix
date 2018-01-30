import os
import lxml.etree as ET

def ExtractData(f, count):
    data = f.readlines()
    string = ""
    lang = ""
    tags = ""
    for word in data:
        if word == '\n':
            print string
            print lang
            print tags
            try:
                count = count + 1
                line = ET.SubElement(root, "senetnce")
                item1 = ET.SubElement(line, "id")
                item2 = ET.SubElement(line, "text")
                item3 = ET.SubElement(line, "language")
                item4 = ET.SubElement(line, "pos_tags")
                item1.text = str(count)
                item2.text = string
                item3.text = lang
                item4.text = tags
            except:
                root.remove(line)
                count = count - 1
                print "\n"
            string = " "
            lang = " "
            tags = " "
        else:
            splitWord = word.split("\t")
            # print splitWord
            string = string + splitWord[0] + " "
            lang = lang + splitWord[1] + " "
            tags = tags + splitWord[2].split("\n")[0] + " "
    return count

f_fb = open("Facebook.txt", 'r')
f_t = open("Twitter.txt", 'r')
f_wa = open("WhatsApp.txt", 'r')

root = ET.Element("root")

count = 0
count = ExtractData(f_fb, count)
count = ExtractData(f_t, count)
count = ExtractData(f_wa, count)
print count
tree = ET.ElementTree(root)
tree.write("Hi-En_data.xml", pretty_print=True)
