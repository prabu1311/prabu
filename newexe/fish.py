#class Fish:
fishList=[]
list2=[]
    
FishFile=open("fishFile.txt","r")
Sizefile=open("sizefile.txt","r")
    #FishFileOne=FishFile.read()
def types_of_fish():
    fish=raw_input("Enter fish:")
    fishList.append(fish)
    filewrite(fishList)
    
    size = raw_input("size of fish is")
    list2.append(size)
    filewrite(list2)
    return size
def cach(self):
    cac = (random.randint(0 , 10)
    return cac
    
def  filewrite(item):
    if fishList==item:
        txt=open("fishFile.txt","a")
        for t in item:
            txt.write(t)
        txt.close()    

    elif list2 == item:
        txt=open("sizefile.txt","a")
        for t in item:
            txt.write(t)
        txt.close()
    else:
        exit()

        

#types_of_fish()




    
