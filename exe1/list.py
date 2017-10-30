ten_things = "apple orange sugar telephone tv mobile"
print "there is no ten things"
stuff = ten_things.split(' ')

more_stuff = ['song','boy', 'girl', 'pot', 'bat','fruit','dog']

while len(stuff) != 10:
    get = more_stuff.pop
    print "adding", more_stuff
    stuff.append(get)
    a=len(stuff)
    print "now it has %d items" %a
    print "now list is",stuff
    
print "lets do something with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#' .join(stuff[3:5])
