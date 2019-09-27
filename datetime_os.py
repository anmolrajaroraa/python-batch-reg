Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import *
>>> print(date.today())
2019-09-27
>>> today = date.today()
>>> today
datetime.date(2019, 9, 27)
>>> print(today.day)
27
>>> print(f"{today.day}/{today.month}/{today.year})")
27/9/2019)
>>> print(f"{today.day}/{today.month}/{today.year}")
27/9/2019
>>> now = datetime.now()
>>> print(now)
2019-09-27 10:21:53.855122
>>> now.strftime("%y %Y")
'19 2019'
>>> now.strftime("%a")
'Fri'
>>> now.strftime("%A")
'Friday'
>>> now.strftime("%d")
'27'
>>> now.strftime("%D")
'09/27/19'
>>> now.strftime("%b")
'Sep'
>>> now.strftime("%B")
'September'
>>> now.strftime("%X")
'10:21:53'
>>> now.strftime("%c")
'Fri Sep 27 10:21:53 2019'
>>> now.strftime("%a %d %b %H:%M:%S %p")
'Fri 27 Sep 10:21:53 AM'
>>> now.strftime("%a %d %b %H:%M:%S %z")
'Fri 27 Sep 10:21:53 '
>>> now.strftime("%a %d %b %H:%M:%S %Z")
'Fri 27 Sep 10:21:53 '
>>> now.strftime("%a %d %b %H:%M:%S %p")
'Fri 27 Sep 10:21:53 AM'
>>> 
>>> 
>>> 
>>> import os
>>> os.getcwd()
'/Users/anmolrajarora/Documents'
>>> #get current working directory
>>> #os.chdir('C:\\Users\\Siddharth\\Music')
>>> os.chdir('/Users/anmolrajarora/Documents/aws')
>>> os.getcwd()
'/Users/anmolrajarora/Documents/aws'
>>> os.listdir()
['05-IAM_roles.mov', '.DS_Store', '01-CloudComputingIntro.mov', 'aws-cdn.mov', '05-IAM.mov']
>>> songs = os.listdir()
>>> songs
['05-IAM_roles.mov', '.DS_Store', '01-CloudComputingIntro.mov', 'aws-cdn.mov', '05-IAM.mov']
>>> songs.pop(1)
'.DS_Store'
>>> songs
['05-IAM_roles.mov', '01-CloudComputingIntro.mov', 'aws-cdn.mov', '05-IAM.mov']
>>> import random
>>> song = random.choice(songs)
>>> song
'01-CloudComputingIntro.mov'
>>> os.start(song)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    os.start(song)
AttributeError: module 'os' has no attribute 'start'
>>> os.startfile(song)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    os.startfile(song)
AttributeError: module 'os' has no attribute 'startfile'
>>> import subprocess
>>> subprocess.call(['open', song])
0
>>> subprocess.call(['open', 'Applications/TextEdit'])
1
>>> subprocess.call(['open', '/Applications/TextEdit'])
1
>>> subprocess.call(['open', '/Applications/TextEdit'])
1
>>> subprocess.call(['open', '/Applications/TextEdit.app'])
0
>>> 
