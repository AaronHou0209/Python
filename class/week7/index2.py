"""
1. Make the reel variables global
2. Create display_reels function
3. Create determine_results function
4. Add coins and bet_amount, (0-3), variables globally
5. Include new variables in determine_results, (win gives x2 bet)
6. Repeat program until 0 entered for bet_amount.
7. Display coins info before each bet
8. Check to see if user has more than 0 coins and end game if not
9. Check to ensure bet is <= the coins left
10. Ensure bet amount is in correct range, (0-3)
11. Include Exception handling
"""
import random

# global variables
reel1 = None
reel2 = None
reel3 = None
coins = 30
bet_amount = None
#Create display_reels function

def display_reels():
    global reel1,reel2,reel3,coins,bet_amount
    # generate random numbers for each reel
    reel1 = random.randint(1, 3)
    reel2 = random.randint(1, 3)
    reel3 = random.randint(1, 3)

    # for testing purposes
    # print(reel1, reel2, reel3)

    match reel1:
        case 1:
            print("   @", end="  ")
        case 2:
            print("   #", end="  ")
        case 3:
            print("   %", end="  ")

    match reel2:
        case 1:
            print("   @", end="  ")
        case 2:
            print("   #", end="  ")
        case 3:
            print("   %", end="  ")

    match reel3:
        case 1:
            print("   @")
        case 2:
            print("   #")
        case 3:
            print("   %")




#Create determine_results function
def determine_results():
    global reel1, reel2, reel3, coins, bet_amount
    # determine the outcome
    if reel1 == reel2 and reel1 == reel3:
        print("YOU WIN!!!!!")
        coins += bet_amount * 2

    elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
        print("So close. Try again.")

    else:
        print("You Lose :(")

#Main code
print("Welcome to Conestoga Casino")
try:
    while bet_amount != 0 and coins != 0 :
        print(f"You have {coins} coins left!")
        bet_amount = int(input("Enter bet amount? "))
    # check the result
        if 1 <= bet_amount <= 3 and bet_amount <= coins :
            coins -= bet_amount
            display_reels()
            determine_results()
            print(f"You have {coins} coins left!")
        elif bet_amount > coins :
            print(f"You can't bat over than you have")
        elif bet_amount > 3  :
            print(f"You onlt bet  1-3 coins left!")
        else:
            print("Come back soon!")
# Except the problems
except ValueError:
    print("Input must be an integer ")
except Exception as e:
    print(e)
