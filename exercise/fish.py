class fish:
    def types_of_fish(self, name):
        self.name = name
        print "name of fish" + self.name

    def size_of_fish(self,size):
        self.size = size
        print "size of fish is" + self.size + "cm"
        
bass = fish()
sunfish = fish()
pike = fish()

bass.types_of_fish("bass")
sunfish.types_of_fish("sunfish")
pike.types_of_fish("pike")


bass.size_of_fish("23")
sunfish.size_of_fish("34")
pike.size_of_fish("34")
