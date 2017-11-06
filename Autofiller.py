###########################################
#Imports

import time
#Counts how fast the program takes
starttime=time.time()

import requests
import urllib.request
import urllib.parse
import re
import webbrowser
import logging
import tkinter as tk
import random
import os


cwd=os.getcwd()


###########################################
#Definitions

def waitfunc(delay):
    _waitwindow=tk.Toplevel()
    _waitwindow.withdraw()
    _starttime=time.time()
    _stoptime=_starttime
    while (int(_stoptime)-int(_starttime))<delay:
        _waitwindow.update()
        _stoptime=time.time()
    _waitwindow.destroy()

def quitcommand():
    try:
        os._exit(0)
    except:
        quit()

def resultcommand():
    global senturl
    new=2
    webbrowser.open(senturl,new=new)

def done(failed):
    global stoptime,starttime
    top=tk.Tk()

    #Icon
    top.iconbitmap('gifs/zergyicon.ico')

    #Title
    top.title('LOADING')
    #Misc
    font=('Georgia',12)
    background='gold'

    stoptime=time.time()
    
    _add='\nIf any questions were unanswered or wrong,\n train Zergy so he can do better next time! :)'
    _timetext='\nIt took ' + str(float(stoptime-starttime)) + ' seconds'

    #Fail check
    if failed==0:
        text='Sucess!'+_add+_timetext
    elif failed==1:
        text='Failed! Opening website...'+'\n'+_add+_timetext
    elif failed==2:
        text='Critical failure! Opening website...'+'\n'+_add+_timetext


    #Labels and buttons
    donelabel=tk.Label(top,text=text,font=font,bg=background)
    quitbutton= tk.Button(top, text="Quit", command=quitcommand,bg='red')
    resultbutton= tk.Button(top, text="Results", command=resultcommand,bg='orange')

    donelabel.pack()
    quitbutton.pack()
    resultbutton.pack()

    top.mainloop()
    

###########################################
#Reads data

#Gets URL
f=open('data/urlfixed.txt','r')
_lines=f.readlines()
url=_lines[0].replace('\n','')
f.close()

#Gets details
Details=[]
try:
    f=open('data/Details.txt','r')
    _lines=f.readlines()
    for i in _lines:
        Details.append(i.replace('\n',''))
    f.close()
except:
    #If no details detected, quickopen
    webbrowser.open(url)
    stoptime=time.time()
    done(1)
    
try:
    #Gets training
    Trainingquestions=[]
    Traininganswers=[]

    f=open('data/Training.txt','r')
    _lines=f.readlines()
    for i in _lines:
        _tempstring=i.replace('\n','')
        TQ=_tempstring[:_tempstring.index(';')]
        TA=_tempstring[_tempstring.index(';')+1:]
        Trainingquestions.append(TQ.lower()) #Makes it lowercase
        Traininganswers.append(TA)
    f.close()
except:
    Trainingquestions=['']
    Traininganswers=['']

	
#Gets Settings
Settings=[]
try:
    f=open('data/Settings.txt','r')
    _lines=f.readlines()
    for i in _lines:
        Settings.append(i.replace('\n',''))
    f.close()
except:
    Settings=['Manual: Fill',5,0,'No','No']


###########################################
#Quick open if Manual: open

for i in Settings:
    if 'Open' in str(i):
        webbrowser.open(url)
        stoptime=time.time()
        done(0)

###########################################
#Questions

r = requests.get(url)
_pattern=r'-describedby="i.desc.\d*">(.+?)</div><div'
questionsfetched=re.findall(_pattern,r.text)

#Location for later use
_location=re.finditer(_pattern, r.text)
questionlocations=[i.start(0) for i in _location]

#Gets saves form (Debug + Development)
f=open('data/form.txt','w')
f.write(r.text)
f.close()

#Cuts away bad parts and saves
questions=[]
questionstrue=[] #With case
for x in questionsfetched:
    try:
        cutlocation=x.index('<span')
        x=x[:cutlocation]
    except:
        pass
    questions.append(x.lower()) #Makes it lowercase
    questionstrue.append(x) #With all cases

###########################################
#Entry ids
_pattern=r'"entry.\d*"'
entriesfetched=re.findall(_pattern,r.text)

#Location for later use
_location=re.finditer(_pattern, r.text)
entrylocations=[i.start(0) for i in _location]

#Create entry list
entries=[]
for x in entriesfetched:
    x=x.replace('"','')
    entries.append(x)

###########################################
#Subquestions

#Radio (only one answer)
_pattern=r'RadioLabel">(.+?)</span></div>'
radiosubquestionsfetch=re.findall(_pattern,r.text)

#Location for later use
_location=re.finditer(_pattern, r.text)
radiolocations=[i.start(0) for i in _location]

#IDK if I need to cut
radiosubquestions=[]
for x in radiosubquestionsfetch:
    try:
        cutlocation=x.index('<span')
        x=x[:cutlocation]
    except:
        pass
    radiosubquestions.append(x)


#Checkbox (multiple answers)
_pattern=r'CheckboxLabel">(.+?)</span></div>'
checkboxsubquestionsfetch=re.findall(_pattern,r.text)

#Location for later use
_location=re.finditer(_pattern, r.text)
checkboxlocations=[i.start(0) for i in _location]

checkboxsubquestions=[]
#IDK if I need to cut
for x in checkboxsubquestionsfetch:
    try:
        cutlocation=x.index('<span')
        x=x[:cutlocation]
    except:
        pass
    checkboxsubquestions.append(x)


###########################################
#Organizing questions and subquestions

#Radiosort
radiomatch=[]

#Checkboxsort
checkboxmatch=[]

#Question/entry sort
questionentrymatch=[]

#Sorting everything, It's glorious :')
for i in range(0,len(questions)):
    try:
        Q1=questionlocations[i]
        Q2=questionlocations[i+1]
    except: #When out of range
        Q2=len(r.text)

    _templist=[]
    _templist.append(questions[i])
    for ii in range(0,len(radiolocations)):
        if Q1<radiolocations[ii] and Q2>radiolocations[ii]:
            _templist.append(radiosubquestions[ii])
    if len(_templist)>1:
        radiomatch.append(_templist)

    _templist=[]
    _templist.append(questions[i])
    for ii in range(0,len(checkboxlocations)):
        if Q1<checkboxlocations[ii] and Q2>checkboxlocations[ii]:
            _templist.append(checkboxsubquestions[ii])
    if len(_templist)>1:
        checkboxmatch.append(_templist)
            
    for ii in entrylocations:
        if Q1<ii and Q2>ii:
            questionentrymatch.append([questions[i],entries[entrylocations.index(ii)]])
	
    
###########################################
#Answers (The brain of the Autofill)

#Uses data for entry
data={}

#Details questions (handles "särskrivningar")
Detailsquestions=[['för','namn'],['efter', 'namn'],['post','nummer'],['adress'],['post','ort'],['ovve','namn'],['frakt']]

#Adds all entries and questions into dict (Main brain)
for i in questionentrymatch:
    #Question
    _tempquestion=i[0]

    #Checks for "särskrvningar"
    _checkwords=[[x in _tempquestion for x in y] for y in Detailsquestions] #True and false lists in list
    _boollist=[all(y) for y in _checkwords] #If all true, true i list

    #Long If statements

    #Easy answer, If question exist in Details
    if any(_boollist):
        _answerfix=''
        for ii in Detailsquestions:
            if all(x in _tempquestion for x in ii):
                if _answerfix!='': #Multiple answers
                    _answerfix=Details[Detailsquestions.index(ii)]+' '+_answerfix
                else:
                    _answerfix=Details[Detailsquestions.index(ii)]+_answerfix
        _answer=_answerfix
        
    #Medium answer, If not förnamn or efternamn exist --> anything containing namn that is not ovvenamn is full name.
    elif 'namn' in _tempquestion and not any(word in _tempquestion for word in ['ovvenamn','ovve namn']):
        _answer=Details[0]+' '+Details[1]

    #Hard answer, Question not found
    else:
    	#Looks for answer in Traning
        if any(x in _tempquestion for x in Trainingquestions):
            _answerfix=''
            
            for ii in Trainingquestions:
                if ii in _tempquestion:
                    _answerfix=Traininganswers[Trainingquestions.index(ii)]+_answerfix
                    _answer=_answerfix
                    continue

        else:
            #If force, the program will try to answer the question
            if 'Force' in Settings[0]:
                #Counter if question has been answered
                _isanswered=0
			
		#Check if Radio
                for ii in radiomatch:
                    if _tempquestion in ii[0]:
                        _answer=ii[random.randint(1,len(ii)-1)] #Takes a random answer
                        _isanswered=1

                #Check if Checkbox
                for ii in checkboxmatch:
                    if _tempquestion in ii[0]:
                        _answer=ii[random.randint(1,len(ii)-1)] #Takes a random answer
                        _isanswered=1


                #Check if Normal
                if _isanswered==0:
                    _answer='.' #Puts a dot in field
                    _isanswered=1
                    
            else:            
                #If not force, let the question be unanswered
                pass
    
    #Adds the answer to the list with the correct entry
    data[i[1]]=_answer
	
###########################################
#Writing answers

#Writes start (Debug, to see how it looks like before handling)
with open("data/start.html", "w") as f:
    f.write(r.text)

#Auto submit or not
if 'Auto' in Settings[0]:	
    #formResponse in url means that the program tries to submit the form.
    url=r.url.replace('viewform','formResponse')
elif 'Manual' in Settings [0]: #Opens up url if Manual
    url=r.url.replace('formResponse','viewform')
    new = 2
    webbrowser.open(url,new=new)

#Tricks google that this script is a real computer
user_agent = {'Referer':url,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

#Wait for submit according to the Settings
waitfunc(int(Settings[2]))

#Send request to the url
r = requests.get(url, params=data,headers=user_agent)

#Writes urlsent (Debug and development. Autolearning)
f=open('data/urlsent.txt','w')
f.write(r.url)
f.close()

#Writes final input (and also fixes url for viewing)
with open("data/results.html", "w") as f:
    #Auto fill or not
    if 'Auto' in Settings[0]:
        senturl=r.url.replace('formResponse','viewform')
        rsent = requests.get(senturl, params=data,headers=user_agent)
        f.write(rsent.text)

if not 'Ditt svar är registrerat' in r.text:
    if 'Manual' in Settings[0]:
        #Sucess
        done(0)
    elif 'Auto: Force' in Settings[0]:
        #Critical failure
        new = 2
        url=r.url.replace('formResponse','viewform')
        webbrowser.open(url,new=new)
        done(2)
    else:
        #Failure
        new = 2
        webbrowser.open(url,new=new)
        done(1)
		
elif 'Ditt svar är registrerat' in r.text:
    #Sucess
    new = 2
    done(0)




