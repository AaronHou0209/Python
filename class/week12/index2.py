"""
Demo

Author:ChengYu
Date: Nov 2024
"""



class Car:
#Constructor method
    def __init__(self, year, make, mileage, price):
        self.year = year
        self.make = make
        self.mileage = mileage
        self.__price = float(price)
        self.__admin = float(500)
        self.__total_price = self.__price + self.__admin
    # __ 會隱藏value

    def drive(self, km):
        self.mileage = self.mileage + km

    def display_sticker(self):
        print("-----------")
        print(f"{self.make} - {self.year}\n")
        print(f"Base price       ${self.__price:.2f}")
        print(f"Admin Fee        ${self.__admin:.2f}")
        print(f"Total Price      ${self.__total_price:.2f}")
#Main code:
cars = []
def add_car():
    print("\nAdd Car ------")
    year = input("Enter year:")
    make = input("Enter maker:")
    mileage = int(input("Enter mileage:"))
    price = float(input("Enter Price:"))

    new_car = Car(year, make, mileage,price)
    cars.append(new_car)


def display_cars():
    print("\nDisplay Car---")

    for car in cars:
        print(car.year, car.make, car.mileage)

def drive_car():
    print("\nDrive Car-----")
    index = -1
    car_to_drive = input("Enter a car to drive: ")
    for i,car in enumerate(cars):
        if car.make == car_to_drive:
            index = i
            break
    if index >= 0:
        distance = int(input("How far do you drive? "))
        cars[index].drive(distance)

    else:
        print("Car not found")
def show_info():
    print("\nShow Info-----")

    index = -1

    car_to_find = input("Enter a car to drive: ")
    for i, car in enumerate(cars):
        if car.make == car_to_find:
            index = i
            break
    if index >= 0:
        cars[index].display_sticker()

    else:
        print("Car not found")

def find_car():
    print("\nFind Car------")


# MAIN CODE STARTS HERE
while True:
    print("\nMain Menu------------------")
    print("1. Add a Car")
    print("2. Display all Cars")
    print("3. Drive Car")
    print("4. Display Sticker Price")
    print("5. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        add_car()
    elif choice == "2":
        display_cars()
    elif choice == "3":
        drive_car()
    elif choice == "4":
        show_info()
    elif choice == "5":
        print("Bye for now")
        break
    else:
        print("Invalid entry")
        print("Select 1-5")
