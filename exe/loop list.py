the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
changes = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for i in the_count:
    print "This is count %d" % i
for i in fruits:
    print "A fruit of type: %s" % i
for change in changes:
    print "I got %r" % change
elements = []
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)
for i in elements:
    print "Element was: %d" % i
