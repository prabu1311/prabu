import re
from sys import argv

script,file_name = argv

class prob:

    def check(self,fname):
	self.fname = file_name
        if '.html' in file_name or'.txt' in file_name:
            print "you have entered the correct file"
        else:
            print "you have entered the wrong file"
        return fname

    def operation(self):
        self.TagList=[]
        self.AttrList=[]
        self.ValList=[]
        

        f=open(file_name ,'r')
        data = f.read()
        text = re.sub(r'<!.+-->',r' ',data)

        for i in re.findall(r'<([^/][^>]*)>', text):
            if ' ' in i:
                for ht in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',i):
                    self.TagList.append(ht[0])
                    self.AttrList.append(ht[1])
                    self.ValList.append(ht[2])
                       
                     
            else:
                self.TagList.append(i)

        
        self.TagList = filter(None,self.TagList)        
        print self.TagList
        print self.AttrList
        print self.ValList

    def display(self):
	ischoice = True
        choice=int(raw_input("Enter your choice 1,2,3,4"))
    
        if choice==1:
            for tag in self.TagList:
                print tag
            self.display()   

        elif choice==2:
            for att in self.AttrList:
                print att
            self.display()   
        elif choice==3:
            if len(self.AttrList)==len(self.ValList):
                for ind in range(0,len(self.AttrList)):
                    print self.AttrList[ind],"=",self.ValList[ind]
            self.display()
        elif choice==4:
            ans=raw_input("Enter any key:")
            if ans in self.AttrList:
                val=self.AttrList.index(ans)
                print self.AttrList[val],"=",self.ValList[val]
            else:
                print "Enter the correct key"
		return ischoice
                self.display()
        
        
        


h = prob()
h.check(file_name)
h.operation()
h.display()
