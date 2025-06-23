"""
Author : CHengYu Hou
Date : Oct 10
"""
import random

menu = True
while menu is True:
    print("\n\nMenu")
    print("1. Display 10 Manipulate Values")
    print("2. Play Addition Game")
    print("3. Exit")

    user_answer = input("Select an option:")
    if user_answer == "1":
        value_start = int(input("Entry a start value:"))
        value_begin = int(value_start + 1)
        value_end = int(value_begin + 10 )
        for i in range(value_begin,value_end):
            if i % 2 == 0 :
                final_number = i * 3
                print(final_number, end=" ")
            elif i % 2 == 1:
                final_number = i * 4
                print(final_number, end=" ")
    elif user_answer == "2":
        total = True
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        while total is True:
            answer = str (num1 + num2)
            user_calculator = str(input(f"{num1}+{num2}="))
            if user_calculator == answer:
                print("You got it")
                user_idea = input("Play again?(Y/N)")
                if user_idea == "Y":
                    num1 = random.randint(1, 100)
                    num2 = random.randint(1, 100)
                elif user_idea == "N":
                    break
            else :
                print("try again")

    elif user_answer == "3":
        print("Bye for now")
        break

