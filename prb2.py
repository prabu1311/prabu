

import re
from sys import argv
tagList=[]
mainDict={}
script, file_name = argv
if '.html' in file_name or'.txt' in file_name:
        print "you have entered the correct file"
else:
    print "you have entered the wrong file"
f=open(file_name ,'r')
data = f.read()
text = re.sub(r'<!.+-->',r' ',data)
for i in re.findall(r'<([^/][^>]*)>', text):
    if ' ' in i:
        for ht in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',i):
            tagList.append(ht[0])
            dict= {ht[1]:ht[2]}
            mainDict.update(dict) 
 else:
        tagList.append(i)
print mainDict        
print tagList

