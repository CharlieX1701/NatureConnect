'''
this file is testing the opening and reading of national parks data file
'''


def readHikes():

    filename = 'AllTrailsOriginal.csv'

    infile = open(filename, 'r')
    data = infile.read()
    infile.close()

    data = data.replace(',', '\t')
    #data = data.replace('\n', '\t')
    data = data.split(',')
    
    print(data)

    outFile = 'testHikes.txt'
    outVar = open(outFile, 'w')

    for i in data:
        outVar.write(str(i))

    outVar.close()

readHikes()

