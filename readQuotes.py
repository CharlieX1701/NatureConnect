''''
The purpose of this program is to read in a file containing inspirational
quotes, clean the data, and then randomly select a quote from this file
and print it for the user.

'''

import random 

#read in quotes data, clean it, write out to file
def readQuotes():
    
    filename = 'quotes.csv'

    infile = open(filename, 'r')
    data = infile.read()
    infile.close()

    data = data.replace(',', ': ')
    data = data.replace('"', '')
    data = data.split(',')

    outFile = 'allQuotes.txt'
    outVar = open(outFile, 'w')

    for i in data:
        outVar.write(str(i))

    outVar.close()

    
readQuotes()

