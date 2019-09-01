# Jesus Manuel Tovar
# Theory of Operating Systems
# Saturday, August 31st, 2019

import sys
import re
import string

# open input file
inputFile = open(sys.argv[1], "r")

# open output file, if not present, make
outputFile = open(sys.argv[2], "w+")

# make dictionary
dictionary = {}

# read through inputFile
for line in inputFile:

    # remove newline and remove punctuation
    line = line.strip()
    line = re.sub(r'[^\w\s]', '', line)

    # splits to individual words
    wordsInLine = re.split(' ', line)

    for word in wordsInLine:
        # every word in the line to lowercase
        word = word.lower()

        # if word exists in dictionary, ++. if not, add set counter at 1

        # sort dictionary

        # write dictionary to file

        # close input and output files

        print(word)
