count = 0
word =raw_input(str("enter the word"))

if word in filename:
    print "the word %s is present in file" % word
    for word in filename:
        count + 1
else:
    print "word is not present"


    
