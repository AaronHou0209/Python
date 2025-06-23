"""
Demo of how to manipulate string

Author: ChengYu
Date Nov 2024
"""
import re



def strings_demo():
    test_strings = "Tony Theo"
    print(test_strings)

#   1. Display the 3rd character in the string and
#      also display the string one character at a time
    print(test_strings[2])

    for char in test_strings:
        print(char, end=" ")
#   2. Display each character and what index it's at
    print()
    for i,char in enumerate(test_strings):
        print(f"position:{i} and letter: {char}")
#   3. Display only a specific letter in a string
#      in the position it was found, (blanks for
#       no match)
    letters = input("Entry letter to display: ")

    for i,char in enumerate(test_strings):
        if letters == char:
            print(f"{i},{char}")
        else:
            print(f"{i}, ")

#   4a.  Changes strings cases (e.g. uppercase to lowercase)
    print(test_strings.upper())
    print(test_strings)

    test_strings = test_strings.upper()
    print(test_strings)

    test_strings = test_strings.lower()
    print(test_strings)
#   4b. Change case of single character in string
    print(test_strings[6].upper())
#   5.  Determine what "type" a character is.
    if test_strings[0].isdigit():
        print(f"Element 0 in {test_strings} is a digit")
    if test_strings[0].isalpha():
        print(f"Element 0 in {test_strings} is a letter")
    if test_strings[0].isalnum():
        print(f"Element 0 in {test_strings} is a letter or digit")
    if test_strings[0].islower():
        print(f"Element 0 in {test_strings} is a lowercase")
    if test_strings[0].isupper():
        print(f"Element 0 in {test_strings} is a uppercase")
    if test_strings[4].isspace():
        print(f"Element 4 in {test_strings} is a space")

def searching_strings():
    test_strings = input("Enter a string: ")
# 1. Search for a string within another string in
#    any location, at the beginning, or at the end
    if "PROG" in test_strings:
        print("Programming Course")
    else:
        print("Not a Programming Course ")
    if test_strings.startswith("PROG"):
        print("PROG is at the beginning")
    else:
        print("PROG is not at the beginning")
    if test_strings.endswith("PROG"):
        print("PROG is at the end")
    else:
        print("PROG is not at the end")
#2.       Find where "P" is in the string
#--NOTE-- Show what index its in if found:
#       - P at beginning of string
#       - There  multiple P values
#       - P is lowercase
#       - There is no P
    # searching form the beginning
    index = test_strings.find("P")
    print("P found at index: ", index)
#3.       Find a character starting at the end of a string
    # searching form the end
    index = test_strings.rfind("P")
    print("P found at index: ", index)
#4.       Find a string within another string
    test_strings ="xx oo xx oo xx"

    index = test_strings.find("oo",4)
    print("oo found at index: ", index)

    index = test_strings.find("oo", 4,7)
    print("oo found at index: ", index)

    index = test_strings.rfind("oo",4,11)
    print("oo found at index: ", index)

def substrings():
    city = " New City "
#1. strip the excess blank space
    print(f">{city}<")
    print(f">{city.strip()}<")
    print(f">{city.lstrip()}<")
    print(f">{city.rstrip()}<")
    print(f">{city}<")

    city = city.strip()
    print(f">{city}<")
#2. Insert a string into a string
    city = city[0:4] + "York" + city[3:12]
    print(city)

#3. Remove a substring from a string
    donut = "Jelly filled donut"
    print(donut)

    donut = donut.replace("filled","")
    print(donut)

    number = "1, 2, 3, 4, 5, 6"
    print(number)
    number = number.replace(",",":")
    print(number)

def deliminators_tokens():
#1. Create a string of names separated by commas
#   and the split the names into a list of names
    names = "tony,steph,ari"
    print(names)

    tokens = names.split(",")
    print(tokens)

    for name in tokens:
        print(name)

    team = "Toronto Maple Leafs"
    tokens = team.split(" ")
    print(tokens)

    for name in tokens:
        print(name)

#2. Create a new string with many different delimiters
    players = "sid,mary bob:john"

    pattern = "[, :]"
    tokens = re.split(pattern, players)
    print(tokens)

    for name in tokens:
        print(name)

#3. Capitalize the first letter of each player name
    for i in range(len(tokens)):
        tokens[i]= tokens[i][0].upper() + tokens[i][1:]

    print(tokens)




#Main Code
#strings_demo()
#searching_strings()
#substrings()
deliminators_tokens()