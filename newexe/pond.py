import random
import fish1
class pond:

    def capacity(self):
        cap=int(raw_input( "enter the capacity of pond"))
        num =int(raw_input("ur value is"))

        if num >= cap:
            print "pond is full"
            print "u cant add some more"
        
        else:
            print "u can add %d fishes more "%(cap - num)
            val =int(raw_input("howmuch u are going to add"))
            print (num+val)
            tot =(num+val)
            print (random.randint(1,tot))
            list = ['bass','sunfish','pike']
            print "type of the random fish is:",(random.choice(list))
            
            
capa = pond()
capa.capacity()



   
    

