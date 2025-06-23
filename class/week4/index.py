"""
Demo of how to create and use function

Author: ChengYu Hou
Date : Sep 24 2024
"""

# 1. Create a function that gets a name and
# combines it with a random number to make
# a username

"""
    A function always put on the top 
"""
import random

def create_username():
    name = input ("Enter your name: ")
    random_value = random.randint(10,99)
    username = name + str(random_value)
    print(f"Hello {username}")

# 2.Create a function to calculate the area
# of a rectangle

def find_area():
    length = int(input("Enter your length:"))
    width = int(input ("Enter your width:"))
    area = length * width
    print (f" The area of a {length} x {width} rectangle is : ")
    print(f"{area} units^2")

# 3. Create a function to determine the max
# of three values

def find_max():
    num1 = int (input("Enter number 1:"))
    num2 = int (input("Enter number 2:"))
    num3 = int (input("Enter number 3:"))
    max = num1
    if num2 > num1 :
        max = num2
    elif num3 > num2 :
        max = num3
    print(f"{max} is the biggest number" )
# Main Code Here
print("Welcome to Week4")
create_username();
find_area();
find_max();