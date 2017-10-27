import os

file_name =open("raj.txt","r")
data=file_name.read()
name = str(raw_input("Enter the word you search in file.."))
for name in data:
    if name in data:
        print "true"
    else:
        print "false"
               
