import sys
class schedule:
    def user_input(self):
        self.yourstarttime = int(raw_input("Enter your start time:"))
        self.yourstartplace = str(raw_input("Enter your start place:"))
        self.yourdestplace = str(raw_input("Enter your dest place:"))
        self.yourdesttime = int(raw_input("Enter your dest time:"))

    def train_details(self):
        l1 =[]
        times= int(input("no.of train avilable"))
        for i in range(times):
            depttime = int(raw_input("Enter  train dept time:"))
            l1.append(depttime)
            startplace = str(raw_input("Enter train start place:"))
            l1.append(startplace)
            arvtime = int(raw_input("Enter your train arival time:"))
            l1.append(arvtime)
            destplace = str(raw_input("Enter train dest place:"))
            l1.append(destplace)

       
        mylist = l1
        self.splitlist = [mylist[x:x+4] for x in range(0, len(mylist),4)]
        print self.splitlist
        
   
    def check_arivplace(self):
        index=3
        self.bestchoice = []

        for l in range(0,len(self.splitlist)):
            if self.splitlist[l][index] == self.yourdestplace:
               self.bestchoice.append(self.splitlist[l])
               
            elif self.splitlist[l][index] ==1:
                print "no match"

      
        print self.bestchoice   

       
    def check_arivtime(self):
        index1=2
        timelist = []
        index2 = 2 
        bestarivtime = []
        for k in range(0,len(self.bestchoice)):
            if self.bestchoice[k][index1] <= self.yourdesttime:
                bestarivtime.append(self.bestchoice[k])
                
            elif self.bestchoice[k][index1] == " ":
                print "no match"
        for m in range(0,len(bestarivtime)):
            timelist.append(bestarivtime[m][index2])
        highval = max(timelist)
        
        if highval == self.yourdesttime:
            for r in range(0,len(bestarivtime)):
                if bestarivtime[r] == highval:
                    print bestarivtime[r]
                else :
                    print bestarivtime[r-1]
            
                
                
            print bestarivtime
            
                 
        print "the best train to board is %r:" %bestarivtime         



                


if __name__== '__main__':
    s = schedule()
    s.user_input()
    s.train_details()
    s.check_arivplace()
    s.check_arivtime()
    


















        
               
          
    

        

          

        
