'''
The purpose of this program is to use OOP to create hikes. The program will read in a file
containing data from AllTrails on every hike in the National Park system. This library
will be imported into the main program where the user will be asked for hike parameters.

'''

#create class for hike objects
class Hike:

    def __init__(self, name, park, state, length, diff, route, f1, f2, f3):
        self.name = name
        self.park = park
        self.state = state
        self.length = float(length)
        self.diff = int(diff)
        self.route = route
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3

    def getName(self):
        return self.name

    def getPark(self):
        return self.park

    def getState(self):
        return self.state

    def getLength(self):
        return self.length

    def getDiff(self):
        return self.diff

    def getRoute(self):
        return self.route

    def getFeatures(self):
        return f1, f2, f3

#create hike objects
def makeHike(infoStr):
    name, park, state, length, diff, route, f1, f2, f3 = infoStr.split("\t")
    return Hike(name, park, state, length, diff, route, f1, f2, f3)


#read in hikes data, clean it, write out to file
def hikesFile():

    filename = 'AllTrailsOriginal.csv'

    infile = open(filename, 'r')
    data = infile.read()
    infile.close()

    data = data.replace(',', '\t')
    data = data.split(',')
    

    outFile = 'allHikes.txt'
    outVar = open(outFile, 'w')

    for i in data:
        outVar.write(str(i))

    outVar.close()

    
hikesFile()   
#makeHike()

