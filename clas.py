class user:
    
    def __init__(self, name):
        self.name = name

    def sayhello(self):
        print "hello my name is" + self.name

james = user("ram")
ram = user("-ram")
raj = user("_ram")

james.sayhello()
ram.sayhello()
