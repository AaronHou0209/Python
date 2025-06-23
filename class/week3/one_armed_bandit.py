"""
A basic slot machine

Author : Aaron Hou
Date : Sept 2024
"""
# need to create random values
import random

print ("Welcome to Conestoga Casino")
input("press any key to play the slots")

# generate random numbers for each reel
reel1 = random.randint(1,3)
reel2 = random.randint(1,3)
reel3 = random.randint(1,3)

#for testing purpose
#print(reel1,reel2,reel3)

match reel1:
    case 1 :
        print("  @", end="  ")
    case 2 :
        print("  #", end="  ")
    case 3 :
        print("  %", end="  ")
match reel2:
    case 1:
        print("  @", end="  ")
    case 2:
        print("  #", end="  ")
    case 3:
        print("  %", end="  ")
match reel3:
    case 1 :
        print("  @")
    case 2 :
        print("  #")
    case 3 :
        print("  %")

# Determine the outcome

if reel1 == reel2 == reel3 :
    print("You WIN!")
elif    reel1 == reel2  or reel2 == reel3 or reel1 == reel3 :
    print("So closeee!")
else:
    print('You lose :(')

