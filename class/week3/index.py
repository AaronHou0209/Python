"""
Demonstration of if, elif, and match

Author:Aaron
Date : 17 Sep 2024
"""
import nis
from nis import match
from unicodedata import category

# 1. Determine if a person is old enough to vote
age = int(input(' How old are you? '))
if age >= 18 :
  print('You can vote')
else:
    print("You can't vote")
# 2, Find the max value between 2 numbers

num1= int(input("Entry a number:"))
num2= int(input("Entry a second number:"))

if num1 >num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

# 3. Check if two numbers are equal
if num1 == num2 :
    print("Both numbers are equal")
else:
    print("The numbers are different")

# 4. Check if two numbers are NOT equal
if num1 != num2 :
    print("The two numbers are not the same")
else:
    print("The two numbers are the same")

# 5. Determine overtime hours
hours = float(input("Entry hours worked:"))
overtime = hours - 40

if hours > 40 :
    print(f"YOu woked {overtime} overtime hours")
else:
    print(f"You worked {hours} hours")

# 6. Determine the colour of a card suit

suit = "diamonds"
if suit == "hearts" :
    print("The colour is red")
elif suit == "diamonds":
    print("THe colour is black")
elif suit == "space":
    print("THe colour is yellow")

# 7. Same as above with an QR statement

if suit == "hearts" or suit == "space" :
    print("The colour is red")
elif suit == "diamonds" or suit == "track":
    print("THe colour is black")
else:
    print("That is not a suit ")

# 8. Use And to see if two conditions are true
sock_on = True
hat_on = False
if sock_on is True and hat_on is True:
    print("you are warm")
elif sock_on is True and hat_on is False:
    print("your head are cold")
elif sock_on is False and hat_on is True:
    print("your toes are cold")
elif sock_on is False and hat_on is False:
    print("you are warm")

# 9. Determine hurricane wind speeds

category = 3

match category :

    case 1 :
             print("119-153 km/hr")
    case 2 :
            print("154-177 km/hr")
    case 3 :
            print("178-209km/hr")
    case 4 :
            print("210-249km/hr")
    case 5 :
            print("greater than 249 km/hr")
    case _ :
            print("That is not a category")

"""
speed = 144


match speed:

    case (119,153) :
             print("category 1")
    case (154,177) :
            print("category 2")
 """

# 10. Show if it is a weekday or a weekend
day= "Monday"

match day :
    case "Monday" | "Tuesday" |"Wednesday"| "Friday" | "Thursday" :
        print("This is a weekday")
    case "Sunday" | "Saturday":
        print("This is a weekday")
    case _:
        print("This is not a day")





