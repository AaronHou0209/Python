"""
Demo of how to create different kinds of loops


Author: ChengYu Hou

Date: Oct 1 2024
"""
import random
from itertools import count
from shutil import which


def for_loops():
    #1. Create a loop that displays all values
    # inclusive between  1 and 5
    for i in range(1, 6):
        print(i, end=" ")

    # 2. Create a loop that displays all values
    # inclusive between 10 and 6
    print()

    for i in range(10, 5, -1):
        print(i, end=" ")

    # 3. Displays even numbers inclusive
    #    between 4 and 10
    print()

    for i in range(3, 11):
        if i % 2 == 0:
            print(i , end=" ")
    # 4. Displays the sum if all numbers inclusive
    #    between 1 and 10. The answer is 55.
    print()

    sum = 0
    for i in range (1, 11):
        sum = sum + i

    print(sum)

    # 5. Create a loop that displays all leap years
    #    inclusive between 1990 and 2010, The output
    #    should be 1992, 1996, 2000, 2004, 2008
    print()
    start_years = int(input("Entry start years:"))
    end_years = int(input("Entry end years:"))

    for i in range(start_years, end_years):
        if i % 4 == 0 :
            print(i, end=" ")

    # 6. Create a loop that runs 5 times, each time
    #    displays a random value between 1 and 10.
    print()

    for i in range(1, 6):
        print(random.randint(1,10),end=" ")

def while_loops():
    # 1. Displays all values inclusive between 1 and 10
    counter = 1

    while counter <= 10:
        print(counter)
        counter += 1

    #2. Create a counting loop
    print()
    keep_going = True
    counter = 0
    while keep_going is True:
       user_response = input("Do you want to count(y/n)?")
       if user_response == "y" :
            counter += 1
            print(counter)
       elif user_response == "n" :
            keep_going = False

def do_while_loops():
    # 1. Displays all values inclusive between 1 and 10
    counter = 1

    while True :
        print(counter, end=" ")
        counter += 1

        if counter > 10:
            break
    # 2. Create a menu system
    while True:
        print("\n\nMain Menu")
        print("1. Display value 1-5")
        print("2. say Hello")
        print("3. Exit")
        user_choice = input("Select an option:")
        if user_choice == "1":
            for i in range(1, 6):
                print(i, end=" ")
        elif user_choice == "2":
            print("Hello")
        elif user_choice == "3":
            print("Bye for now ")
            break
        else :
            print("Invalid Choice, Select 1-3. ")
 





# Mian Code
for_loops()
#while_loops()
#do_while_loops()















