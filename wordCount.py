import sys
import re
import os
import collections

""" File management """
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output text file>")
    exit()

textFile = sys.argv[1]
outputFile = sys.argv[2]

if not os.path.exists(textFile):
    print("text file %s doesn't exist! Exiting..." % textFile)
    exit()

""" code """
words = {}

with open(textFile, "r") as textFile:
    for line in textFile:
        line = line.strip()
        word = re.findall(r'\w+', line)

        for var in word:
            var = re.sub('[^a-zA-Z]+', '', var).lower()

            if var in words:
                words[var] += 1
            else:
                words[var] = 1
textFile.close()

with open(outputFile, "w+") as outputFile:
        for i in sorted(words):
            outputFile.write("%s %d\n" % (str(i), int(words[i])))
outputFile.close()
