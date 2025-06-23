"""
Demo of how to create functions with parameters
Author: CHNEGYU HOU
Date : Sep 24 2024
"""



# 1. Create an add function that accept 2
# integer parameters

def add_number(x,y):
    sum = x + y
    print(f"{x}+{y}={sum}")


# 2. Create a function that covert from inch to cm
def inch_to_cm(inches):
    cm = inches * 2.54
    print(f"{inches} is {cm} cm ")


# 3. Create a function that accepts 2 parameters, name and pin
# if the pin is "1234" the program welcomes the user with
# their name. Else an error message is displayed
def check_name_pin(name,pin):
    if pin == 1234:
        print(f"Welcomes the {name}")
    else:
        print("Error, Entry right pin ")



# Main Code Here
add_number(4,7)
add_number(46,74)
inch_to_cm(23)
inch_to_cm(44)
check_name_pin("rextcvb",1234)
