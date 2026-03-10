import random

pos = 0
print("Welcome to Snake And Ladder program")
print("Single player at start position ", pos)

def rollDice():
    dice = random.randint(1,6)
    return dice

def option(pos, dice):
    option=random.randint(0,2)
    if(option==0):
        print("No move")
    elif(option==1):
        print("Ladder")
        pos+=dice
    else:
        print("Snake")
        pos-=dice
    return pos