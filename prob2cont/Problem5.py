import re
from sys import argv

script,file_name = argv

class prob:

    def check(self):
        if '.html' in file_name or'.txt' in file_name:
            print "you have entered the correct file"
        else:
            print "you have entered the wrong file"
    def operation(self):
        self.tagList=[]
        self.attrlist=[]
        self.vallist=[]
        

        f=open(file_name ,'r')
        data = f.read()
        text = re.sub(r'<!.+-->',r' ',data)

        for i in re.findall(r'<([^/][^>]*)>', text):
            if ' ' in i:
                for ht in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',i):
                    self.tagList.append(ht[0])
                    self.attrlist.append(ht[1])
                    self.vallist.append(ht[2])
                                 #dic = OrderedDict(zip(tagList, zip(attrlist, vallist)))  
                     
            else:
                self.tagList.append(i)

        
        self.tagList = filter(None,self.tagList)        
        print self.tagList
        print self.attrlist
        print self.vallist

    def display(self):
        choice=int(raw_input("Enter your choice 1,2,3,4"))
        if choice==1:
            for tag in self.tagList:
                print tag
            self.display()   

        elif choice==2:
            for att in self.attrlist:
                print att
            self.display()   
        elif choice==3:
            if len(self.attrlist)==len(self.vallist):
                for ind in range(0,len(self.attrlist)):
                    print self.attrlist[ind],"=",self.vallist[ind]
            self.display()
        elif choice==4:
            ans=raw_input("Enter any key:")
            if ans in self.attrlist:
                val=self.attrlist.index(ans)
                print self.attrlist[val],"=",self.vallist[val]
            else:
                print "Enter the correct key"
                self.display()
        


h = prob()
h.check()
h.operation()
h.display()
