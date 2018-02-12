import re
import csv
import glob, os, io
import string
import nltk
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords



####Combine Multiple Files Together
#read_files = glob.glob("*.txt")

#with open("result.txt", "wb") as outfile:
#    for f in read_files:
#        with open(f, "rb") as infile:
#            outfile.write(infile.read())
#



#For multiple files, use "result.txt" instead of "South_Park.txt"
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("South_Park.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext2.txt','a')
        appendFile.write(" "+r)
        appendFile.close()



##Word Frequency
frequency = {}
document_text = open('filteredtext2.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)


for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

#List
l =[]

#dictionary
d = {}

##Write to dictionary
print(type(l))
print(type(d))

for words in frequency_list:
    #print words, frequency[words]
    d.update({words:frequency[words]})


print(d)


##Write to CSV
w = csv.writer(open("South_Park_Words.csv", "w"))
w.writerow(["Word", "Frequency"])
for key, val in d.items():
    w.writerow([key, val])