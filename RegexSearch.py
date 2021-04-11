import re
from pathlib import Path
import pyinputplus as pyip
import os

print('Enter a word to seach for in text files')
response = pyip.inputStr()
srchwrdrgx = re.compile(response, re.I)
p = Path.cwd()
#p = Path.cwd()/'Read_WriteFiles/RegexSearch'

filelist = os.listdir(p)
nomatch = True
for i in filelist:
    if ".txt" in i:
        pass
        # open file with readlines
        theFile = open(p/i, "r")
        for j in theFile:
            mo = srchwrdrgx.search(j)
            if mo != None:
                print("Book: "+i, "Verse: "+j)
                nomatch=False
if nomatch == True:
    print('no matches found')
