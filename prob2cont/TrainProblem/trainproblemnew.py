import sys
import xlrd
from xlrd import open_workbook
class Schedule:
    def user_input(self,inputdata):
        inputdata = True
        self.yourstarttime = int(raw_input("Enter your start time:"))
        if self.yourstarttime <= 24:
            yourdesttime = int(raw_input("Enter your dest time:"))
            if yourdesttime <= 24:
                yourstartplace = str(raw_input("Enter your start place:"))
                yourdestplace = str(raw_input("Enter your dest place:"))
            else:
                print "enter the time less than 24"
                schedule.user_input()   
        else:
            print "enter the time less than 24"
            inputdata =False
            schedule.user_input()
        return inputdata,yourdesttime,yourstartplace,yourdestplace,
             
    def train_details(self,details):
        details = True
        col_value = []
        values = []
        l=""
        fname = str(raw_input("enter the filename that has to read:"))
        fname.endswith(('.xlsx', '.xlsm', '.xltx','.xls'))
        wb = open_workbook(fname)
        for sheet in wb.sheets():
            for row in range(sheet.nrows):
                for col in range(sheet.ncols):
                    value = (sheet.cell(row,col).value)
                    try : value = int(value)
                    except : pass
                    col_value.append(value)
                    
        values = [str(i) for i in col_value]
        changed_list = [int(f) if f.isdigit() else f for f in values]
        self.mylist = changed_list
        splitlist = [self.mylist[x:x+4] for x in range(0, len(self.mylist),4)]
        return details,splitlist
        
    def best_board(self,splitlist,yourdesttime,yourstartplace,yourdestplace):
        boarding = True
        list1 = []
        self.timelist = []
        highval = ""
        index = 0
        index1 = 1
        index2 = 2
        index3 = 3
        try:
            for l in range(1,len(splitlist)):
                if splitlist[l][index1] == yourstartplace:
                    if (splitlist[l][index2])<= yourdesttime:
                        if splitlist[l][index3]== yourdestplace:
                            list1.append(splitlist[l])            
                            
                else:
                    pass

        except :
            boarding = False
            pass
            
               
        if len(list1) == 0:
            print "no train avilable"
            
        else:
            for num in range(0,len(list1)):
                self.timelist.append(list1[num][index2])
                minval = min(self.timelist)        
        return boarding,minval,list1
    
    
    
    def finalchoice(self,minval,list1):
            userchoice = True
            finallist = []
            ind2 = 2
           
            for f in range(0,len(list1)):
                if list1[f][ind2] >= minval:
                    finallist.append(list1[f])
                    print "final choice to board is:%s" %finallist
                    break
                elif len(finallist)== 0:
                    if (list1[f][ind2]) < minval:        
                        finallist.append(list1[f])
                        print "final choice to board is:%s" %finallist
                        
                else:
                    userchoice = False
                    elval = len(finallist)== 0 
                    if elval:
                        print "no train avilable"
                   
            return userchoice
            
                
if __name__== '__main__':
    s = Schedule()
    boolean,wholelist = s.train_details(True)
    boolvalue,destime,boardplace,desplace=s.user_input(True)
    returnchoice,minimum,returnlist = s.best_board( wholelist,destime,boardplace,desplace)
    s.finalchoice(minimum,returnlist)
