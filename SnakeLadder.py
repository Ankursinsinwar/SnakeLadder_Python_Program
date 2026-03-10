import random

pos = 0
print("Welcome to Snake And Ladder program")
print("Single player at start position ", pos)

def rollDice():
    dice = random.randint(1,6)
    return dice