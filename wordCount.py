# Jesus Manuel Tovar
# Theory of Operating Systems
# Saturday, August 31st, 2019

import sys
import re

# open input file
inputFile = open(sys.argv[1], "r")

# open output file, if not present, make
outputFile = open(sys.argv[2], "w+")

# make dictionary
dictionary = {}

# read through inputFile
for line in inputFile:

    # remove newline and remove punctuation
    line = re.sub(r'[^\w\s]', ' ', line)
    line = line.strip()

    # splits to individual words
    wordsInLine = re.split(' ', line)

    for word in wordsInLine:

        # to detect if a newline filtered through
        if word == "":
            continue

        # every word in the line to lowercase
        word = word.lower()

        # if word exists in dictionary, ++. if not, add set counter at 1
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

# write dictionary to file by sorted keys
for key in sorted(dictionary.keys()):
    outputFile.write(key + " " + str(dictionary[key])+'\n')

# close input and output files
outputFile.close()
