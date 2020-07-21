'''
This is the main program to the hiking app. This program will import
the Hike.py and readQuotes.py libraries in order to decide which hike(s)
and quote are displayed to the user at the end of user input.

'''

import Hike, readQuotes, random

#function for user to search for specific hike
def searchHike():

    infile = open('allHikes.txt', 'r')

    userHike = str(input("What hike are you searching for?: "))

    for hikes in infile:
        refHike = Hike.makeHike(hikes)
        if userHike == refHike.name:
            print()
            print(refHike.name, "located in: ", refHike.park)
            print("The hike is: ", refHike.length,"meters with a difficulty rating of", refHike.diff)
            print("This hike is a ", refHike.route, "trail")
            print("Features include: ", refHike.f1, ",", refHike.f2, ",",  refHike.f3)

            
#function for user to search for hikes in their park
def findHikes():

    infile = open('allHikes.txt', 'r')

    findPark = str(input("Which National Park are you in?: "))
    findLength = float(input("How many miles do you want to hike?: "))

    upperLength = (findLength + 0.75) * 1609.34
    lowerLength = (findLength - 0.75) * 1609.34
    
    hikeStack = list()

    print("\nHere are the hikes in your park: \n")

    for hikes in infile:
        refHike = Hike.makeHike(hikes)
        if findPark == refHike.park:
            if (refHike.length <= upperLength) and (refHike.length >= lowerLength):
                hikeStack.append(hikes)
    
    for i in range(len(hikeStack)):
        print(hikeStack.pop())

    infile.close()


#function to generate random quote 
def findQuote():

    infile = open('allQuotes.txt', 'r')
       
    quotes = infile.readlines()
    qList = []
    
    for i in range(0, len(quotes)-1):
        q = quotes[i]
        qList.append(q)

    print("Mental health is just as important as physical health.")
    print("To help clear your mind on your hike, here is your quote of the day: \n")    
    
    newQ = random.choice(qList)
    print(newQ)
    print("Have a great hike and enjoy the nature!")
       
    infile.close()    

#searchHike()
#findQuote()
