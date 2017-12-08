import sys
import xlrd
from xlrd import open_workbook
class schedule:
    def user_input(self,istrue):
        istrue = True
        self.yourstarttime = int(raw_input("Enter your start time:"))
        if self.yourstarttime <= 24:
            self.yourdesttime = int(raw_input("Enter your dest time:"))
            if self.yourdesttime <= 24:
                self.yourstartplace = str(raw_input("Enter your start place:"))
                self.yourdestplace = str(raw_input("Enter your dest place:"))
            else:
                print "enter the time less than 24"
                schedule.user_input()
                
        else:
            
            print "enter the time less than 24"
            istrue =False
            schedule.user_input()
        return istrue 
            
            
             
    def train_details(self,istrue):
        istrue = True
        col_value = []
        values = []
        l=""
        wb = open_workbook('Expenses01.xlsx')
        for s in wb.sheets():
            for row in range(s.nrows):
                for col in range(s.ncols):
                    value = (s.cell(row,col).value)
                    try : value = int(value)
                    except : pass
                    col_value.append(value)
                    
        values = [str(i) for i in col_value]
        changed_list = [int(f) if f.isdigit() else f for f in values]
        self.mylist = changed_list
        splitlist = [self.mylist[x:x+4] for x in range(0, len(self.mylist),4)]
        return istrue,splitlist
    
        
                   
    def best_board(self,splitlist,istrue):
        istrue = True
        self.list1 = []
        timelist = []
        highval = ""
        index = 0
        index1 = 1
        index2 = 2
        index3 = 3
        for l in range(1,len(splitlist)):
                if splitlist[l][index1]== self.yourstartplace:
                    if (splitlist[l][index2])<= self.yourdesttime:
                        if splitlist[l][index3]== self.yourdestplace:
                            self.list1.append(splitlist[l])
                             
        for m in range(0,len(self.list1)):
            timelist.append(self.list1[m][index2])
        self.highval = min(timelist)
        return istrue,highval
    
    def finalchoice(self,highval,istrue):
            istrue = True
            finallist = []
            ind2 = 2
            for f in range(0,len(self.list1)):
                if (self.list1[f][ind2]) == highval: 
                    finallist.append(self.list1[f])
                    print "final choice to board is:%s" %finallist
                        
                elif len(finallist)== 0:
                    if (self.list1[f][ind2]) < highval:
                        finallist.append(self.list1[f])
                        print "final choice to board is:%s" %finallist
                    
                else:
                    elval = len(finallist)== 0 
                    if elval:
                        print "no train avilable"
            return istrue
                    

            
                
if __name__== '__main__':
    s = schedule()
    s.user_input(True)
    arg,arg1 = s.train_details(True)
    val,val1 = s.best_board(arg1,arg)
    s.finalchoice(val1,val)
