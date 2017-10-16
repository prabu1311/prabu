z=2

def afun():
    global z
    z = 9

def afun2(x,y):
    global z
    return x+y+z

afun()
total = afun2(4,5)
print(total)

