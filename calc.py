def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("select choice:")
print("1. add")
print("2. sub")
print("3.mul")
print("4.div")

choice = int(raw_input("enter type of operation:1/2/3/4:"))
            
num1 = int(raw_input("number 1 is :"))
num2 = int(raw_input("number 2 is :"))

if(choice == 1):
    print (num1,"+",num2,"=", add(num1, num2))

elif(choice == 2):
    print (num1,"-",num2,"=", sub(num1, num2))

elif(choice == 3):
    print (num1,"*",num2,"=", mul(num1, num2))

elif(choice == 4):
    print (num1,"/",num2,"=", div(num1, num2))

else:
    print("invalid input")
