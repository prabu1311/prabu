import re
import sys

class prob():
    def check(self,fname):
        ischoice = True
        
        if '.html' in fname or'.txt' in fname:
            #print "you have entered the correct file"
            ischoice = True
        else:
            print "you have entered the wrong file"
            ischoice == False 
        fopen=open(fname, "r")
        rf=fopen.read()    
        return rf,ischoice

    def operation(self,rf):
        ischoice = True
        try:
            self.TagList=[]
            self.AttrList=[]
            self.ValList=[]
            lis=[]
    
            text = re.sub(r'<!.+-->', r' ', rf)

            for i in re.findall(r'<([^/][^>]*)>', text):
                if ' ' in i:
                    for ht in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)', i):
                        self.TagList.append(ht[0])
                        self.AttrList.append(ht[1])
                        self.ValList.append(ht[2])
                else:
                    self.TagList.append(i)

            lis=self.TagList+self.AttrList+self.ValList
            self.TagList = filter(None,self.TagList)

        except:
            ischoice == False      
        return lis,ischoice

    def display(self):
        ischoice = True
        try:
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
                    self.display()

        except:
            ischoice == False 

        return ischoice
                   
if __name__== '__main__':
    if len(sys.argv)>1:
        h = prob()
        arg,arg2=h.check(sys.argv[1])
        if arg2:
            val1,val2=h.operation(arg)
        if val2:
            h.display()



    
