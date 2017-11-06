###########################################
#IMPORTING

#Imports OS
import os

#Needed for sleep
import time

#GUI
import tkinter as tk

#Import filename
from tkinter import filedialog

#Import filename
from tkinter import messagebox

#Import py file (needs __init__.py)
from Gifhandler import *

#Tabs
from tkinter import ttk

#To run shit in background
import subprocess

#Startup
import winshell

#To close
import sys

###########################################
#CHOOSING FOLDERS

#Finds folder location
cwd = os.getcwd()

#saves root cwd
rootcwd=cwd

#Goes to script folder
os.chdir(cwd)

#Checks datafolder
if not os.path.isdir(cwd+'/'+'data'):
    os.mkdir(cwd+'/'+'data')


###########################################
#Loading

#Main window
top=tk.Tk()

#Hide
top.withdraw()

#Loadwindow
loadwindow = tk.Toplevel(top)

#Icon
loadwindow.iconbitmap('gifs/zergyicon.ico')

#Setting color
loadwindow.configure(background='gold')

#Title
loadwindow.title('LOADING')

#Fixing picture canvas
loadcanvas=tk.Canvas(loadwindow,width=250,height=250,background='gold')
loadcanvas.pack()

#Open gif
loadanimation=Gifhandler(loadwindow,loadcanvas,'gifs/running.gif',40)
loadanimation.animate()

#Loadingtext
loadstring=tk.StringVar()
loadtext = tk.Label(master=loadwindow,textvariable=loadstring)
loadtext.configure(background='gold')
loadtext.config(font=("Georgia", 26))
loadtext.pack()

loadstring.set('Loading: \nDefinitions')


###########################################
#Definitions

#Wait function, that makes tkinter still run, #MASTAAAPIECE
def waitfunc(delay):
    _waitwindow=tk.Toplevel()
    _waitwindow.withdraw()
    _starttime=time.time()
    _stoptime=_starttime
    while (int(_stoptime)-int(_starttime))<delay:
        _waitwindow.update()
        _stoptime=time.time()
    _waitwindow.destroy()

def runzergy():
    global cwd
    url=E1T1.get()
    f=open('data/url.txt','w')
    f.write(url)
    f.close()

    #Close GUI
    #top.destroy()
    
    if 'Yes' in Settings[3]:
        startupfolder = winshell.startup()
        winshell.CreateShortcut(Path=(startupfolder+'/'+'Zergyshortcut.lnk'), Target=(cwd+'/'+'HTMLfetch.exe'))
    try:
        subprocess.Popen(['HTMLfetch.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)
    except:
        os.system('HTMLfetch.py')

def quitcommand():
    try:
        os._exit(0)
    except:
        quit()

def delete_startup():
    global cwd
    startupfolder = winshell.startup()
    os.remove(startupfolder+'/'+'Zergyshortcut.lnk')
    B2T4.config(text='Deleted',bg='deep sky blue')
    waitfunc(1)
    B2T4.config(text='Delete autostart',bg='red')

def traincommand():
    Question=E1T3.get()
    Answer=E2T3.get()
    f=open('data/Training.txt','a')
    f.write(Question+';'+Answer+'\n')
    f.close()
    B1T3.config(text='Learned!',bg='deep sky blue')
    waitfunc(1)
    B1T3.config(text='Train',bg='orange')

def opentrain():
    os.system('start '+r'data/Training.txt')

def writedetails():
    global E1T2,E2T2,E3T2,E4T2,E5T2,E6T2,E7T2,E8T2
    varlist=[E1T2,E2T2,E3T2,E4T2,E5T2,E6T2,E7T2,E8T2]
    Details=[]
    for i in range(0,8):
        _temp=varlist[i].get()
        Details.append(_temp)
    f=open('data/Details.txt','w')
    for i in Details:
        f.write(i+'\n')
    f.close()
    B1T2.config(text='Written!',bg='deep sky blue')
    waitfunc(1)
    B1T2.config(text='Write to file',bg='orange')

def writesettings():
    global font
    global O1T4_stringvar,S1T4, S2T4,O2T4_stringvar,O3T4_stringvar
    varlist=[O1T4_stringvar,S1T4,S2T4,O2T4_stringvar,O3T4_stringvar]
    Settings=[]
    for i in varlist:
        Settings.append(i.get())    
    f=open('data/Settings.txt','w')
    for i in Settings:
        f.write(str(i)+'\n')
    f.close()
    B1T4.config(text='Written!',font=font,bg='deep sky blue')
    waitfunc(1)
    B1T4.config(text='Write to file',font=font,bg='orange')

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
    mainanimation=Gifhandler(top,topcanvas,'gifs/train.gif',80)
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

def checktab():
    global ttkNote
    currenttab=ttkNote.index('current')
    if currenttab==0 or currenttab==1:
        runwaitgif()
    elif currenttab==2:
        runtraingif()
    elif currenttab==3:
        runbuggif()
    elif currenttab==4:
        rungotitgif()
    elif currenttab==5:
        runburrowgif()

###########################################
#GUI window

#Update
waitfunc(0.1)
loadstring.set('Loading: \nMain window')

#Icon
top.iconbitmap('gifs/zergyicon.ico')

#Setting color
top.configure(background='gold')

#Title
top.title('Zergy')

#Fixing picture canvas (will load later)
topcanvas=tk.Canvas(top,width=250,height=250,background='gold')
topcanvas.pack()

#Makes it not rezisable
top.resizable(width=False, height=False)


###########################################
#Create tabs

#Tabs
ttkNote=ttk.Notebook(top)
frame1=tk.Frame(ttkNote,bg='gold')
frame2=tk.Frame(ttkNote,bg='gold')
frame3=tk.Frame(ttkNote,bg='gold')
frame4=tk.Frame(ttkNote,bg='gold')
frame5=tk.Frame(ttkNote,bg='gold')
frame6=tk.Frame(ttkNote,bg='gold')
ttkNote.add(frame1,text='Start')
ttkNote.add(frame2,text='Details')
ttkNote.add(frame3,text='Training')
ttkNote.add(frame4,text='Settings')
ttkNote.add(frame5,text='Info')
ttkNote.add(frame6,text='      ') #Hidden

tab1=ttkNote.index('current')
ttkNote.pack()


###########################################
#Load default text

#Update
waitfunc(0.1)
loadstring.set('Loading: \nData')

#DONT FORGET DEFAULT TEXT IN ENTRIES!

#Details
try:
    Details=[]
    f=open('data/Details.txt','r')
    _lines=f.readlines()
    Details.append([i.replace('\n','') for i in _lines])
    Details=Details[0] #Because list in list
    f.close()
except:
    Details=[['']*9]
    Details=Details[0]


#Settings
try:
    Settings=[]
    f=open('data/Settings.txt','r')
    _lines=f.readlines()
    Settings.append([i.replace('\n','') for i in _lines])
    Settings=Settings[0] #Because list in list
    f.close()
except:
    Settings=['Manual: Fill',5,0,'No','No']

###########################################
#Entries

#Update
waitfunc(0.1)
loadstring.set('Loading: \nMain GUI')

font=('Georgia',12)
foreground='black'
background='gold'

#TAB1
E1T1 = tk.Entry(frame1)
L1T1 = tk.Label(frame1,text='URL:',font=font,fg=foreground,bg=background)
B1T1 = tk.Button(frame1, text="Start", command=runzergy,bg='orange')
B2T1 = tk.Button(frame1, text="Quit", command=quitcommand,bg='red')

#TAB2
for i in range(1,9):
    vars()['E'+str(i)+'T2']=tk.Entry(frame2)
    vars()['E'+str(i)+'T2'].insert(0,Details[i-1])

L1T2 = tk.Label(frame2,text='First Name:',font=font,fg=foreground,bg=background)
L2T2 = tk.Label(frame2,text='Surname:',font=font,fg=foreground,bg=background)
L3T2 = tk.Label(frame2,text='ZIP code:',font=font,fg=foreground,bg=background)
L4T2 = tk.Label(frame2,text='Adress:',font=font,fg=foreground,bg=background)
L5T2 = tk.Label(frame2,text='Mailing Adress:',font=font,fg=foreground,bg=background)
L6T2 = tk.Label(frame2,text='"Ovvenamn":',font=font,fg=foreground,bg=background)
L7T2 = tk.Label(frame2,text='Shipping:',font=font,fg=foreground,bg=background)
L8T2 = tk.Label(frame2,text='Amount:',font=font,fg=foreground,bg=background)

B1T2 = tk.Button(frame2, text="Write to file", font=font, command=writedetails,bg='orange')

#TAB3
E1T3 = tk.Entry(frame3)
E2T3 = tk.Entry(frame3)
L1T3 = tk.Label(frame3,text='Question:',font=font,fg=foreground,bg=background)
L2T3 = tk.Label(frame3,text='Answer:',font=font,fg=foreground,bg=background)

B1T3 = tk.Button(frame3, text="Train", command=traincommand,bg='orange')
B2T3 = tk.Button(frame3, text="Open file", font=font, command=opentrain,bg='deep sky blue')

#TAB4
O1T4_tuple = ("Manual: Open","Manual: Fill","Manual: Force", "Auto: Fill", "Auto: Force")
O1T4_stringvar=tk.StringVar(frame4)
O2T4_tuple = ("No","Yes")
O2T4_stringvar=tk.StringVar(frame4)
O3T4_tuple = ("No","Yes")
O3T4_stringvar=tk.StringVar(frame4)


O1T4 = tk.OptionMenu(frame4,O1T4_stringvar, *O1T4_tuple)
O1T4.config(bg=background,fg=foreground,font=font)
O1T4_stringvar.set(Settings[0])

O2T4 = tk.OptionMenu(frame4,O2T4_stringvar, *O2T4_tuple)
O2T4.config(bg=background,fg=foreground,font=font)
O2T4_stringvar.set(Settings[3])

O3T4 = tk.OptionMenu(frame4,O3T4_stringvar, *O3T4_tuple)
O3T4.config(bg=background,fg=foreground,font=font)
O3T4_stringvar.set(Settings[4])

S1T4 = tk.Scale(frame4,from_=0, to=30,orient='horizontal',font=font,fg=foreground,bg=background)
S2T4 = tk.Scale(frame4,from_=0, to=30,orient='horizontal',font=font,fg=foreground,bg=background)

S1T4.set(Settings[1])
S2T4.set(Settings[2])
    
L1T4 = tk.Label(frame4,text='Function:',font=font,fg=foreground,bg=background)
L2T4 = tk.Label(frame4,text='Refresh:',font=font,fg=foreground,bg=background)
L3T4 = tk.Label(frame4,text='Delay:',font=font,fg=foreground,bg=background)
L4T4 = tk.Label(frame4,text='Autoresume:',font=font,fg=foreground,bg=background)
L5T4 = tk.Label(frame4,text='Autotrain:',font=font,fg=foreground,bg=background)
B1T4 = tk.Button(frame4, text="Write to file", font=font, command=writesettings,bg='orange')
B2T4 = tk.Button(frame4, text="Delete autostart", font=('Georgia',9), command=delete_startup,bg='red')


#TAB5
infotext="\nHey!\nLet go of the bug!\n\n\n\nThis program has been written\nby Timothy Bergström and\nis used to autofill Googleforms"
L1T5 = tk.Label(frame5,text=infotext,font=font,fg=foreground,bg=background)

#TAB6 (Hidden)
infotext="\nDon't put a new \nbug in the program!!\n\n\n\nSigh..."
L1T6 = tk.Label(frame6,text=infotext,font=font,fg=foreground,bg=background)

#Packing Tab1
L1T1.pack()
E1T1.pack()

B1T1.pack()
B2T1.pack(side='bottom')

#Packing Tab2
for i in range(1,8):
    vars()['L'+str(i)+'T2'].grid(row=i,column=0)

for i in range(1,8):
    vars()['E'+str(i)+'T2'].grid(row=i,column=1)

B1T2.grid(row=9,column=1)

#Packing Tab3
L1T3.pack()
E1T3.pack()
L2T3.pack()
E2T3.pack()

B1T3.pack()
B2T3.pack(side='bottom')

#Packing Tab4
O1T4.grid(row=1,column=1)
S1T4.grid(row=2,column=1)
S2T4.grid(row=3,column=1)
O2T4.grid(row=4,column=1)
O3T4.grid(row=5,column=1)

L1T4.grid(row=1,column=0)
L2T4.grid(row=2,column=0)
L3T4.grid(row=3,column=0)
L4T4.grid(row=4,column=0)
L5T4.grid(row=5,column=0)

B1T4.grid(row=6,column=1)
B2T4.grid(row=6,column=0)

#Packing Tab5
L1T5.pack()

#Packing Tab6
L1T6.pack()


#Update
loadstring.set('Loading: \nFinished')
waitfunc(0.5)

#Reveal
top.deiconify()

#Open gif
mainanimation=Gifhandler(top,topcanvas,'gifs/zergysmall.gif',40)
mainanimation.animate()

#checktabs AWW YISSS, IT TOOK SO LONG TO FIND A SOLUTION
ttkNote.bind('<<NotebookTabChanged>>',lambda event: checktab())

#Destroy
loadanimation.stop_animation()
loadwindow.destroy()

#loop
top.mainloop()






