import fish1
class fishers:
    
    def fname(self):
        name = str(raw_input("name of the fisher"))
        minimum =10
        maxnum =10
        #self.size1 =fish1.size_of_fish()
        result = fish1.size_of_fish()
        print "Res:",result
        if result < minimum and cach < maxnum:
            print "i will not  take it and throw it bach to pond"
        else:
            print  "i will take it"

f = fishers()
f.fname()
            
