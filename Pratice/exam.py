"""
exma 5
"""
import random
def create_account():
    keep_going_name = True
    keep_going_password = True
    username = []
    password = []
    number_of_name = 0
    while keep_going_name == True:
        name = input("What's your username:(At least 6 characters)")
        username.append(name)
        for i,char in enumerate(username):
            for x in char:
                if number_of_name < 6:
                    number_of_name += 1
                elif number_of_name == 6:
                    break
        if number_of_name < 6:
            print("Username must over or equal six.")
        if number_of_name == 6:
            break

    while keep_going_password == True:

        index = 0
        password_character = input("Enter your password:(including 8 characters and a special character)")
        password.append(password_character)
        number_of_password = 0
        for i, char in enumerate(username):
            for x in char:
                if x.isalnum() or not x.isalnum():
                    if number_of_password < 8:
                        number_of_password += 1
                    elif number_of_password == 8:
                        break
            if number_of_password < 8:
                print("Password must over or equal eight.")
            elif number_of_password == 8:
                for i,char in enumerate(password):
                    if not char.isalnum():
                        index = -1
                        keep_going_password = False
                if index == 0:
                    print("Password must have a special character")

    for i,char in enumerate(username):
        list_change = password
        for x in char:
            if x.isupper():
                x = x.lower()
            elif x.islower():
                x = x.upper()
            elif x.isdigit():
                x = int(x)
                x = x + 3
                x = str(x)


    end_number = str(random.randint(1,100))
    password = str(password)
    password = password.replace("[",' ')
    password = password.replace("]", end_number)

    username = str(username)
    username = username.replace('[',"")
    username = username.replace(']'," ")



    print(username)
    print(password)



create_account()
