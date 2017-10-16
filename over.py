class rect():
    def __init__(self,length, breadth):
        self.len = length
        self.breadth = breadth
    def getarea(self):
            print self.len * self.breadth, "is a area of rect"

class squre(rect):

    def __init__(self, side):
        self.side = side
        rect.__init__(self, side, side)
    def getarea(self):
            print self.side * self.side,"is area of squre"
s = squre(4)
r = rect(2,4)
s.getarea()
r.getarea()
