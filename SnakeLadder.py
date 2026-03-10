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
        pass
    elif(option==1):
        if(pos+dice<=100):
            pos+=dice
    else:
        pos-=dice
        if pos<0 :
            pos=0
    return pos

while(pos<100):
    dice=rollDice()
    pos=option(pos,dice)

if(pos>=100):
    print("Player win!")