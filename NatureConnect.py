'''
This program will utilize the TKinter module to create a basic GUI
to simulate a mobile app called NatureConnect. This program will
import mainProgHikeProject in order to access the Hike and readQuote
libraries, which will be used to determine the hike information
given to the user.

'''

from tkinter import *
import mainProgHikeProject


#create functions for button commands
def specHike():
    mainProgHikeProject.searchHike()
    mainProgHikeProject.findQuote()

def parkHikes():
    mainProgHikeProject.findHikes()
    mainProgHikeProject.findQuote()
    

#format an app window using Tkinter   
window = Tk()

headline = Label(window, text = 'NatureConnect \n Connecting Users to the Perfect Hike'
                 , bg = '#47B346', fg = '#893E07', font = ('Helvetica', 24))
headline.place(x = 90, y = 100)

button1 = Button(window, text = 'I want to search for a specific hike',  fg = '#893E07', font = ('Helvetica', 14)
                 , command = specHike)
button1.place(x = 180, y = 200)

button2 = Button(window, text = 'I want to find hikes in my park',  fg = '#893E07', font = ('Helvetica', 14)
                 , command = parkHikes)
button2.place(x = 180, y = 250)

window.title('NatureConnect')
window.geometry("600x400+20+40")
window.configure(bg = '#47B346')
window.mainloop()
