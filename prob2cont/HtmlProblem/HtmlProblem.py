import re
import sys
import time

class Htmlproblem():
    def check_input(self,fname):
        begin = time.time()
        userinput = True
        if fname.endswith('.html') or fname.endswith('.txt'):
            print "you have entered the correct file"
            
        else:
            userinput = False
            print "you have entered the wrong file"        
        fileopen=open(fname, "r")
        readfile=fileopen.read()
        return fname,userinput,readfile
    
    def operation(self,readfile):
        filedatas= True
        try:
            self.TagList=[]
            self.AttributeList=[]
            self.ValueList=[]
            totallist=[]
            text = re.sub(r'<!.+-->', r' ', readfile)
            for lines in re.findall(r'<([^/][^>]*)>', text):
                if ' ' in lines:
                    for word in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)', lines):
                        self.TagList.append(word[0])
                        self.AttributeList.append(word[1])
                        self.ValueList.append(word[2])
                else:
                    self.TagList.append(lines)
            
            totallist=self.TagList+self.AttributeList+self.ValueList
            self.TagList = filter(None,self.TagList)

        except:
            filedatas == False    
        return totallist,filedatas

    def display(self):
        displaychoice = True
        try:
            choice=int(raw_input("""
1: tags,
2: attributes,
3: attribute values,
4:for search attribute value,
5:exit
        Enter your choice:"""))
        
            if choice==1:
                for tag in self.TagList:
                    print tag
                self.display()   

            elif choice==2:
                for attribute in self.AttributeList:
                    print attribute
                self.display()   
            elif choice==3:
                if len(self.AttributeList)==len(self.ValueList):
                    for index in range(0,len(self.AttributeList)):
                        print self.AttributeList[index],"=",self.ValueList[index]
                self.display()
            elif choice==4:
                answer=raw_input("Enter any key:")
                if answer in self.AttributeList:
                    value=self.AttributeList.index(answer)
                    print self.AttributeList[value],"=",self.ValueList[value]
                else:
                    print "Enter the correct key"
                    self.display()
        except:
            displaychoice == False
        return displaychoice
       
if __name__== '__main__':
    if len(sys.argv)>1:
        html = Htmlproblem()
        result,result2,result3=html.check_input(sys.argv[1])
        if result2:
            value1,value2=html.operation(result3)
            if value2:
                html.display()


    
