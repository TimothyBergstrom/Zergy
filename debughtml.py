#fix html

import os
import requests

url=r'https://www.facebook.com/events/727995224075725/permalink/734143970127517/'
os.chdir(r'C:\My stuff\Programming\Python\Zergy')

r=requests.get(url)
f=open('data/htmlfullreadtest.html','wb')
f.write(r.text.encode('utf-8'))
f.close()

