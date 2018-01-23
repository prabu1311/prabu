import random

class Fish:
    
    def __init__(self,name,size):
        self.name = name
        self.size = size

Pike = Fish('Pike', 10)
Sushi = Fish('Sushi', 12)
Bubbles = Fish('Bubbles', 8)
Casper = Fish('Casper', 6)
Shadow = Fish('Shadow',11 )
Comet = Fish('Comet', 6)
Charlie = Fish('Charlie', 11)
Goldie = Fish('Goldie',1 )
Nemo = Fish('Nemo',5 )
Pumpkin = Fish('Pumpkin', 15)
traut = Fish('traut', 15)
tuna = Fish('tuna', 15)
searobin = Fish('searobin', 15)
whale = Fish('whale', 15)
tough = Fish('tough', 15)
spadefish = Fish('spadefish', 15)


class pond:

    pondsname = "naile"
    
    def __init__(self, pondsname=None, capacity=0):
        self.fishlist=[]
        self.name = pondsname
        self.capacity = capacity
        
    def __addfish__(self,fish):
        self.fishlist.append((fish.name, fish.size))
        return self.fishlist
        
    def getemptyspace(self):
        strength = len(self.fishlist)
        emptyspace = self.capacity - strength
        print "you have %r emptyspace in this pond" %emptyspace
        return self.fishlist
    
    def fishreduce(self, randomfish):
        self.fishlist.remove(randomfish)
        print self.fishlist
        return self.fishlist
        
    
naile = pond("naile",10)
naile.__addfish__(Pike)
naile.__addfish__(Sushi)
naile.__addfish__(Bubbles)
naile.__addfish__(tuna)
naile.__addfish__(traut)
naile.__addfish__(searobin)

lotus = pond("lotus",10)
lotus.__addfish__(Casper)
lotus.__addfish__(Shadow)
lotus.__addfish__(Comet)
lotus.__addfish__(tuna)
lotus.__addfish__(tough)
lotus.__addfish__(whale)

brook = pond("brook",10)
brook.__addfish__(Charlie)
brook.__addfish__(Goldie)
brook.__addfish__(Nemo)
brook.__addfish__(Pumpkin)
brook.__addfish__(tuna)
brook.__addfish__(spadefish)
brook.__addfish__(Pike)


class Fisher():

    def __init__(self):
        self.selectedfish = []
        
    def fisher_details(self):
        fishername = "ram"
    
    def catchfish(self, userselectedpond):
        randomfish = random.choice(userselectedpond.fishlist)
        if randomfish[1] > 5:
            self.selectedfish.append(randomfish)
            print self.selectedfish
            return  self.selectedfish[0]
        else:
            info = "there is no fishes of your expected size"
            return info
        
     
if __name__== '__main__':

    user = pond()
    fisher = Fisher()
    fisher.fisher_details()
    if user.pondsname == "naile":
        naile.getemptyspace()
        random = fisher.catchfish(naile)
        naile.fishreduce(random)
    elif user.pondsname == "lotus":
        naile.getemptyspace()
        randomfish = fisher.catchfish(lotus)
        lotus.fishreduce(randomfish)
    elif user.pondsname == "brook":
        brook.getemptyspace()
        gotfish = fisher.catchfish(brook)
        brook.fishreduce(gotfish)
    else:
        print "you have entered wrong pond"
    
    
    
    
