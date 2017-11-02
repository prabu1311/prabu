import fish
class fishers:
    
    def fname(self):
        name = str(raw_input("name of the fisher"))
        minimum =10
        maxnum =10
        
        #self.size1 =fish1.size_of_fish()
        self.result=fish.types_of_fish()
        print "Res:",self.result
        self.catch=fish.cach(self)
        if self.result < minimum and self.catch < maxnum:
            print "i will not  take it and throw it bach to pond"
        else:
            print  "i will take it"
            

                     
f = fishers()
f.fname()
                   
            

