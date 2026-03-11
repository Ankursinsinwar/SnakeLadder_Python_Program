import random

pos1 = 0
pos2 = 0
print("Welcome to Snake And Ladder program")
print("Single players at start position 0")

dice_count1 = 0
dice_count2 = 0

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

while(pos1<100 and pos2<100):

    dice=rollDice()
    pos1=option(pos1,dice)
    print("position of player 1: ",pos1)
    dice_count1 += 1
    if(pos1>=100):
        print("Player 1 win!")
        print("Total Dice count: ", dice_count1)
        break

    dice=rollDice()
    pos2=option(pos2,dice)
    print("position of player 2: ",pos2)
    dice_count2 += 1
    if(pos2>=100):
        print("Player 2 win!")
        print("Total Dice count: ", dice_count2)
        break