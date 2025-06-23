"""
Demo the use of lists and ad lists

Author: ChengYu Hou
Date: Nov 2024
"""



def list_demo():
#1a. Create a list to hold values 1-5
    numbers = []
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(5)
#1b. Display all the value in the list
    print(numbers)
    print(f"Length" , len(numbers))

    for i in range(0,len(numbers), 1):
        print(numbers[i], end=" ")

#2. Add 1 to each vvalue in the list and display results
    print()

    for i in range(0,len(numbers)):
        numbers[i] = numbers[i] +1
        print(numbers[i],end=" ")


# 3a. Sum all values in the list and display result.
    print()
    sum_values = 0
    for i in range(0,len(numbers)):
        sum_values += numbers[i] # sum_values = sum_values + numbers[i]
    print(sum_values)
#3b. Do the same operation by iterating through objects
#    instead of a range

    for number in numbers:
        sum_values = sum_values + number
    print(sum_values)
#4. Perform the following on the list. Display update list.
    print()

    numbers[1] = numbers[1] + 5
    numbers[2] =numbers[2] * numbers[4]
    numbers[0] = numbers[0] - numbers[1]
    swapper = numbers[3]
    numbers[3] = numbers[4]
    numbers[4] = swapper


    for i in range(0, len(numbers), 1):
        print(numbers[i], end=" ")
#5. Reset all the values in the list based on input
    print()

    for i in range(0, len(numbers)):
        numbers[i] = int(input("Enter a number:"))

    print(numbers)


def list_function():

# 1. Create and initialize a list of integer values
    numbers2 = [12, 22, 7 ,32]
    print(numbers2)
# 2. Add a value at index 2
    numbers2.insert(2, 44)
    print(numbers2)
# 3. Show the value in the list backwards
#    (do not change the order of values in the list)
    numbers2.reverse()
    print(numbers2)
    for i in range(len(numbers2) - 1,-1, -1):
        print(numbers2[i], end=" ")
# 4. Create a list th hold player names.
#    - Get form the user how many names to add
#    - Get each name and add to the list
#    - Display the names in sorted order
    print()

    names = []
    num_names = int(input("How many names would you like to add ? "))
    for i in range(num_names):
        names.append(input("Entry name: ") )
    print(names)
    names.sort()
    print(names)
# 5. -Have the user enter a name to remove form the list.
#    - Remove if they exist, or display an error message.
#    -Show update list
    name_to_remove = input("Vote a player off the island: ")

    if name_to_remove in names :
        names.remove((name_to_remove))
        names.pop(name_to_remove)
    else:
        print("Player does not exist")
    print(names)

def list_reference():
    list1 = [1,2,3]
    list2 = list1

    list1[0] = -1
    list2[0] = -2

    print("list1", list1)
    print("list2", list2)

    modify_list(list1)
    print("list1", list1)
    print("list2", list2)

    list3 = [7,4,9,1,3]
    list4 = list(list3)

    print("list3", list3)
    print("list4", list4)


    list3[0]=3
    list4[0]=4
    print("list3", list3)
    print("list4", list4)
def modify_list(function_list):
    function_list[0] = 7

 #Main Code
list_demo()
#list_function()
#list_reference()








