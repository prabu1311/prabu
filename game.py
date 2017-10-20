import random

guesstaken = 0

print ("hello whats your name")
myname = raw_input()
number = random.randint(1,20)
print("well", myname , "i am thinking of number 1 to 20")

while guesstaken <6:
    print("take a guess")
    guess=input()
    guess=int(guess)

    guesstaken =guesstaken+1

    if guess <number:
        print("gess is to low")

    elif guess <number:
        print("guess is high")

    elif guess == number:
        break

if guess == number:
    guesstaken = str(guesstaken)
    print('nice job,'+ 'my name,' + 'ur guess is right,' + 'u guessed  number in ' + guesstaken + 'gusses,')

elif guess!= number:
    number =str(number)
    print("the number is" + number)
