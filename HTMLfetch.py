from urllib.request import *
import re
import requests
import time
import tkinter as tk
from Gifhandler import *
import os
import subprocess
import sys

#Loadwindow
root = tk.Tk()
root.withdraw()

###########################################
#Definitions

def quitcommand():
    try:
        os._exit(0)
    except:
        quit()

def waitfunc(delay):
    _waitwindow=tk.Toplevel()
    _waitwindow.withdraw()
    starttime=time.time()
    stoptime=starttime
    while stoptime-starttime<delay:
        _waitwindow.update()
        stoptime=time.time()
    _waitwindow.destroy()

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
    mainanimation=Gifhandler(top,topcanvas,'gifs/jumping.gif',50,100,130)
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


###########################################
#Tk window

#Main window
top=tk.Toplevel()

#Fixing picture canvas (will load later)
topcanvas=tk.Canvas(top,width=250,height=250,background='gold')
topcanvas.pack()

#Makes it not rezisable
top.resizable(width=False, height=False)

#Icon
top.iconbitmap('gifs/zergyicon.ico')

#Setting color
top.configure(background='gold')

#Title
top.title('Waiting...')

#Open gif
mainanimation=Gifhandler(top,topcanvas,'gifs/Waiting1.gif',100,50,130)
mainanimation.animate()

#Loadingtext
loadstring=tk.StringVar()
loadtext = tk.Label(master=top,textvariable=loadstring)
loadtext.configure(background='gold')
loadtext.config(font=("Georgia", 26))
loadtext.pack()

#Smaller size of font
loadtext.config(font=("Georgia", 16))

loadstring.set('Starting')

#Quit button
font=('Georgia',12)
quitbutton = tk.Button(top, text="Quit",font=font, command=quitcommand,bg='red')
quitbutton.pack()


###########################################
#Checks connection

#Gets URL
f=open('data/url.txt','r')
_lines=f.readlines()
url=_lines[0].replace('\n','')
f.close()


#Tries to find url
try:
    response = urlopen(url)
except:
    loadstring.set('Error. Bad url?\n Quitting program')
    waitfunc(5)
    quit()

#Changes label
loadstring.set('Response recieved')
waitfunc(0.5)


###########################################
#Loads information and saving

#Decodes response (might be unnecessary?)
htmlbytes = response.read()
html=htmlbytes.decode('utf-8')

f=open('data/html.txt','w')
for x in list(html):
    try:
        f.write(x)
    except:
        pass
f.close()


loadstring.set('Saved HTML as txt')
waitfunc(0.1)

#Settings
try:
    Settings=[]
    f=open('data/Settings.txt','r')
    _lines=f.readlines()
    Settings.append([i.replace('\n','') for i in _lines])
    Settings=Settings[0] #Because list in list
    f.close()
    loadstring.set('Loaded settings')
    waitfunc(0.1)
except:
    Settings=[['']*9]
    Settings=Settings[0]
    

###########################################
#Loads information and saving

refresh=Settings[1]
if refresh == '':
    refresh=5
else:
    refresh=int(refresh)

#Counters
done=0
itt=0

#Notfoundstring
notfound=' Google form has \nnot been found'

loadstring.set('Update time is \n' + str(refresh) + ' seconds')

#Timer for gif change
timer=time.time()
gifcount=0
skipgifs=0


#Looking for url loop
while done==0:
    itt=itt+1
    waitfunc(refresh)
    response = urlopen(url)
    htmlbytes = response.read()
    html=htmlbytes.decode('utf-8')
    searchstring=re.findall(r'&quot;https:\\(.+?)&quot;',html)
    if searchstring is None or searchstring=='':
        loadstring.set('ERROR')
        
    foundstring=None
    for x in searchstring:
        if 'goo.gl' in x:
            foundstring=x
        elif 'docs.google.com' in x:
            foundstring=x
        else:
            pass

    if foundstring==None:
        loadstring.set('Itteration ' + str(itt)+'\n'+notfound)
    else:
        loadstring.set('Google form found!!!')
        skipgifs=1

    ##GIFS
    
    timenow=time.time()
    
    if int(timenow)-int(timer)>60 and gifcount==0 and skipgifs==0:
        runchasegif()
        gifcount=1

    elif int(timenow)-int(timer)>120 and gifcount==1 and skipgifs==0:
        runannoyinggif()
        gifcount=2

    elif int(timenow)-int(timer)>180 and gifcount==2 and skipgifs==0:
        runmorechasegif()
        gifcount=3

    elif int(timenow)-int(timer)>240 and gifcount==3 and skipgifs==0:
        runjumpinggif()
        gifcount=4

    elif int(timenow)-int(timer)>300 and gifcount==4 and skipgifs==0:
        runboomgif()
        gifcount=5

    elif int(timenow)-int(timer)>360 and gifcount==5 and skipgifs==0:
        runcutegif()
        gifcount=6

    elif int(timenow)-int(timer)>420 and gifcount==6 and skipgifs==0:
        runwaitgif()
        timer=time.time()
        gifcount=0
    

    
    if foundstring is not None:
        found=0
        for x in searchstring:
            if ('goo.gl' in x) and ('forms' in x) and (r'\\' in x) and found==0:
                foundstring=x
                found=1
            elif ('docs.google.com' in x) and ('forms' in x) and (r'\\' in x) and found==0:
                foundstring=x
                found=1

        loadstring.set('Fixing URL')
        urlfixed=foundstring.replace('\\','')
        urlfixed='https:'+urlfixed
        r = requests.get(urlfixed)
        realurl=r.url
        done=1


urlfixed=foundstring.replace('\\','')
urlfixed='https:'+urlfixed


#Gets full url
r = requests.get(urlfixed)

#Writes to txt
f=open('data/urlfixed.txt','w')
f.write(r.url)
f.close()

loadstring.set('Done!')

try:
    subprocess.Popen(['Autofiller.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)
except:
    os.system('Autofiller.py')

os._exit(0)

