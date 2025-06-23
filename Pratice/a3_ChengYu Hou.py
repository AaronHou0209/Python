"""
Assignment 3

Author: ChengYu Hou

Date : Nov 2024
"""

def two_di_list():
    #try:
        list1 = []
        location = 0
        # get how many row and col that costumer wants
        row_number = int(input("Entry number of row: "))
        col_number = int(input("Entry number of seats: "))
        # create a row
        for i in range(0,row_number):
            row = []
            location = i + 1
        # create a seat
            for i in range(1,col_number + 1):
                row.append(i)
            list1.append(row)
            print(f"Row {location} : {row}")
        keep_going = True
        # start the Menu the let the costumer choices
        while keep_going == True:
            print("Main Menu")
            print("---------------------------------------")
            print("1.Add New Reservation")
            print("2.Edit Existing Reservation")
            print("3.Cancel Reservation")
            print("4.Display Seating Chart ")
            print("5.Exit ")
            print("---------------------------------------")
            option = int(input("Select an option: "))
        # option 1
            if option == 1:
                for i,char in enumerate(list1):
                    print(f"Row{i + 1 }: {char}")
            # grab where is the costumer choice seat
                while keep_going:
                    row_seat = input("Entry desired row: ")
                    if row_seat.isalpha() or row_seat.isalnum:
                        print("Number only")
                    elif row_seat.isdigit():
                        break
                while keep_going:
                    col_seat = input("Entry desired seat: ")
                    if col_seat.isdigit():
                        break
                    elif col_seat.isalpha() or col_seat.isalnum:
                        print("Number only")
                    costumer_name1 = input("Entry your name: ")

            # make a reservation
                if list1[(row_seat - 1)][(col_seat -1)] == col_seat:
                    list1[(row_seat - 1)][(col_seat -1)] = costumer_name1
                    for i,char in enumerate(list1):
                        print(f"Row{i +1 }: {char}")
                elif list1[(row_seat - 1)][(col_seat -1)].isalpha():
                    print("Already Reserved")

        # option2
            if option == 2:
                for i,char in enumerate(list1) :
                    print(f"Row{i +1 }: {char}")
            # grab where is the costumer edits seat
                row_seat = int(input("Entry desired row: "))
                col_seat = int(input("Entry desired seat: "))
                costumer_name = input("Entry your name: ")
                if list1[(row_seat - 1)][(col_seat - 1)] == col_seat :
                    print("Not already reserved")
                elif list1[(row_seat - 1)][(col_seat - 1)].isalpha():
                    list1[(row_seat - 1)][(col_seat - 1)] = costumer_name

                for i, char in enumerate(list1):
                    print(f"Row{i + 1}: {char}")
        # option3
            if option == 3:
                for i,char in enumerate(list1) :
                    print(f"Row{i +1 }: {char}")
            # grab where is the costumer wants cancel
                row_seat = int(input("Entry desired row: "))
                col_seat = int(input("Entry desired seat: "))
            # No reservation
                if list1[(row_seat - 1)][(col_seat - 1)] == col_seat :
                    print("No reservation found")
            # had reservation
                elif list1[(row_seat - 1)][(col_seat - 1)].isalpha():
                    print("Seat reserved for: ",list1[(row_seat - 1)][(col_seat - 1)])
                    cancel = input("Do you want to cancel?(y/n)")
                    if cancel == "y":
                        list1[(row_seat - 1)][(col_seat - 1)] = col_seat
                    elif cancel == "n":
                        print()
                    for i, char in enumerate(list1):
                        print(f"Row{i + 1}: {char}")


        # option4 Display all seating chart
            if option == 4:
                for i,char in enumerate(list1) :
                    print(f"Row{i +1 }: {char}")
        # option5 Exit
            if option == 5:
                break

    #detect the incorrect value
    #except ValueError:
        #print("Input must be an number ")
    #except Exception as e:
        #print(e)


# Main Code
two_di_list()