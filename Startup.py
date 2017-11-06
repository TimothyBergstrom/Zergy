import subprocess
import os

try:
    Settings=[]
    f=open('data/Settings.txt','r')
    _lines=f.readlines()
    Settings.append([i.replace('\n','') for i in _lines])
    Settings=Settings[0] #Because list in list
    f.close()
except:
    Settings=['Manual: Fill',5,0,'No','No']


try:
    subprocess.Popen(['GUI.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)
except:
    os.system('GUI.py')
