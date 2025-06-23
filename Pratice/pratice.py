"""
Demo for the week10 pratice

Author: ChengYu Hou
Date : 2024 Nov
"""


import random




def user_age():
    try:
        age = int(input("What is your age ? "))
        if age < 16:
            print("You can not drive or vote.")
        elif age == 16 or age == 17:
            print("You can drive but not vote.")
        elif age > 18 or age == 18 :
            print(" You can drive and vote.")


    except Exception as e:
        print(e)
    finally:
        print("Good bye")

def test():
    try:
        y = 0
        x = 5 / y

        print("A")

    except ZeroDivisionError:
        print("B")
    finally:
        print("C")

def calculate(x, y):
    try:
        return x / y
    except:
        return 0

        print("Exception Handled")

def list_1():
    list1 = []
    list1.append(random.randint(0, 9))
    list1.append(random.randint(0, 9))
    list1.append(random.randint(0, 9))
    list1.append(random.randint(0, 9))
    list1.append(random.randint(0, 9))
    list1.append(random.randint(0, 9))
    list1.append(random.randint(0, 9))
    list1.append(random.randint(0, 9))
    list1.append(random.randint(0, 9))
    list1.append(random.randint(0, 9))


    list2 = []
    list2.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))


    print(f"list1:{list1}")
    print(f"list2:{list2}")
    list1.reverse()

    print(f"list1:{list1}")
    sum = 0
    for i in range(0,len(list1)):
        if list1[i] % 2 == 0 :
            sum = list1[i] + sum
    print("sum:", sum)
    numbers_of_3s = 0
    for number in range(0,len(list1)):
        if list1[number] == 3:
            numbers_of_3s +=1
    print("numbers of three:", numbers_of_3s)

    if 0 in list1:
        index = list1.index(0)
        print(f"The first occurrence of 0 is at index: {index}")
    else:
        print("no 0 exists")
    matching_number = 0
    for y in range(0,9):
        if list1[y] == list2[y]:
            matching_number += 1
    print("matching numbers in same position:", matching_number)

    sweep = list1
    list1 = list2
    list2 = sweep
    print(f"list1:{list1}")
    print(f"list2:{list2}")

def list2d():
    list2 = []
    max = 0
    even_total = 0
# 1. Create a 2d list for row = 3, column = 5
    for i in range(3):
        row = []
        for i in range(5):
            i = random.randint(0,20)
            row.append(i)
        list2.append(row)
    print(list2)

# 2. Determine and display the largest value in the 2d list.
    for i,row in enumerate(list2):
        for col in row:
            x = col
            if max < x:
                max = x
    print("max value is: ",max)
#3. Determine and display the sum of all even numbers in the 2d list.
    for i,row in enumerate(list2):
        for col in row:
            x = col
            if col % 2 == 0:
                even_total += x
    print("the sum of all even numbers is:", even_total)
#4. Create a multiplication table that represents a 4 x 4 multiplication table.
#   All values in the table, (with the exception of the row and column headings),
#   should be calculated, not entered manually.
    l1 = []
    l2 = []
    number = 1
    for i in range(4):
        row = []
        for i in range(4):
            row.append( (i + 1) * number )
        number +=1
        l1.append(row)
        print(row)


#class
class Character:

    def __init__(self,name,strength,health,level):
        self.name = name
        self.strength = strength
        self.health = health
        self.__level = int(level)
    def level_up(self,x):
        self.health = 1 * x
        self.strength = 1 * x
        self.__level = 1 + x

#function
heroes = []

def add_hero():
    print("------Add heroes------")
    while True:
        name = input("Enter name:")
        if len(name.strip()) == 0 :
            print("No blank names please")
            name = input("Enter name:")
        else:
            name = name.strip()
            break

    # first way - Complex
    """try:
        strength = int(input("Enter strength, (1-10):"))
    except ValueError:
        print("Number only")
    while strength > 10 or strength < 0:
        try:
            strength = int(input("Enter strength, (1-10):"))
            print("Must between 1 - 10 ")
            if 1 < strength < 10 :
                break
        except ValueError:
            print("Number only")
    """
    # Second way
    while True:
        try:
            strength = int(input("Enter health, (1-10):"))
            if strength > 10 or strength < 0:
                print("Must between 1 - 10 ")
            elif 1 < strength < 10 :
                break
        except ValueError:
            print("Number only")
    while True:
        try:
            health = int(input("Enter health, (1-10):"))
            if health > 10 or health < 0:
                print("Must between 1 - 10 ")
            elif 1 < health < 10 :
                break
        except ValueError:
            print("Number only")

    level = 1

    new_hero = Character(name,strength,health,level)
    heroes.append(new_hero)

def display_heroes():
    print("------Display heroes")
    for i in heroes:
        print(i.name)
        print(f"health :{i.health}")
        print(f"strength :{i.strength}")
        print()

def level_up_hero():
    print("-------levering-------")
    hero_name = input("Which hero you are going level up?")

    index = -1

    for i in heroes:
       if hero_name == i.name:
           number = int(input("How many level you leveling up?"))
           print(i.name)
           index = i

    if index >= 0 :
        heroes[index].level_up(number)
        heroes[index].level_up(number)
        print(f"health :{i.health}")
        print(f"strength :{i.strength}")







#Main Code
#user_age()
#test()

#print(return_value)

#list_1()
#list2d()


while True:
    print("\nMain Menu------------------")
    print("1. Create a Hero")
    print("2. Display all Heroes")
    print("3. level up")
    print("4. Get hero level")
    print("5. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        add_hero()
    elif choice == "2":
        display_heroes()
    elif choice == "3":
        level_up_hero()
    #elif choice == "4":
       # show_info()
    #elif choice == "5":
        #print("Bye for now")
        #break
    else:
        print("Invalid entry")
        print("Select 1-5")