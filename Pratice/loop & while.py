"""
Demo practice loop & while

Author Aaron
Date Oct 3
"""


# 1.  Write a for loop to display every 3rd number
# starting at 10 and ending at 30.
def loop_number():
    for i in range(10, 30):
       final = i -10
       if final % 3 == 0:
           print(i, end=" ")

#2. Write a for loop that iterates through each number between 1 and 6,
# and uses a modulus operator along with an if statement
# to state whether each value is even or odd.

def loop_number1():
    for i in range(1,7):
        if i % 2 == 0 :
            print(f"{i} is even")
        elif i % 2 == 1 :
            print(f"{i} is odd")

#3. Print the pattern below using a for loop.
# Hint: Start off with a string that has 1 "*" in it
# then in the loop you will add another "*" using +=

def loop_number2():
    for i in range(1, 6):
        if i == 1:
            print('*')
        elif i == 2 :
            print("**")
        elif i == 3 :
            print("***")
        elif i == 4 :
            print("****")
        elif i == 5 :
            print("*****")
# 1. Write a program that will take in a start number and end number from a user.
# Then, using while loop show all the values from the start to the end number, (inclusive).
def while_function():
    number1 = int(input("Entry a number:"))
    number2 = int(input("Entry a number:"))

    if number1 > number2:
        for i in range(number1, number2):
            print(i)
    elif number2 > number1 :
        for i in range(number2, number1):
            print(i)
#Main code
while_function()