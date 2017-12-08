
class fish:
    def types_of_fish(self):
        name = str(raw_input("name of fish:"))
        list1 =[]
        list1.append(name)
        l = name
        thefile.write(l)
def size_of_fish(thefile):
    size = int(raw_input("size of fish is"))
    list2 =[]
    list2.append(size)
    j = size
    thefile.write(str(j))
    #return size

thefile = open('tes.py','w')   
bass = fish()
bass.types_of_fish()
size_of_fish(thefile)
##
##
sunfish = fish()
sunfish.types_of_fish()
size_of_fish(thefile)
##
##
pike = fish()
pike.types_of_fish()
size_of_fish(thefile)

