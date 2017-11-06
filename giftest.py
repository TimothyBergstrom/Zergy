import tkinter as tk
from Gifhandler import *

#Main window
top=tk.Tk()

#Icon
top.iconbitmap('gifs/zergyicon.ico')

#Setting color
top.configure(background='gold')

#Title
top.title('Zergy')

#Fixing picture canvas (will load later)
topcanvas=tk.Canvas(top,width=250,height=250,background='gold')
topcanvas.pack()

#Open gif
mainanimation=Gifhandler(top,topcanvas,'gifs/zergysmall.gif',40)

def runwaitgif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/zergysmall.gif',40)
    mainanimation.animate()

def runbuggif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/bug.gif',30)
    mainanimation.animate_noloop()

def runtraingif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/train.gif',100)
    mainanimation.animate()

def rungotitgif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/gotit.gif',30,200,130)
    mainanimation.animate_noloop()
    
def runboomgif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/boom.gif',40,200,130)
    mainanimation.animate()

def runburrowgif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/burrow.gif',30,100,130)
    mainanimation.animate()

def runmorechasegif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/morechase.gif',30,100,130)
    mainanimation.animate()

def runjumpinggif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/jumping.gif',40,100,130)
    mainanimation.animate()

def runannoyinggif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/annoying.gif',30,-45,130)
    mainanimation.animate()

def runcutegif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/cute.gif',30,140,150)
    mainanimation.animate()

def runchasegif():
    global topcanvas, mainanimation
    mainanimation.stop_animation()
    mainanimation=Gifhandler(top,topcanvas,'gifs/chase.gif',30,50,130)
    mainanimation.animate()

gifname=input('gif: ')
vars()['run'+gifname+'gif']()

top.mainloop()
