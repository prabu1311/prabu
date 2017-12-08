#class Fish:
fishList=[]
    
FishFile=open("fishFile.txt","r")
    #FishFileOne=FishFile.read()
def types_of_fish():
    fish=raw_input("Enter fish:")
    fishList.append(fish)
    filewrite(fishList)
    

def  filewrite(item):
    if fishList==item:
        txt=open("fishFile.txt","a")
        for t in item:
            txt.write(t+"\n")
        txt.close()

types_of_fish()        



    
