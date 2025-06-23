"""
Demo how to use 2d list

Author: ChengYu Hou
Date: Nov 2024
"""



def two_dim_example():
# 1. Create a 2d list of numbers and display it
    numbers = [
        [1,2,3],
        [4,5,6]
    ]


    print(numbers)

# 2. Show each row in 2d list on separate line
    for row in numbers:
        for element in row :
            print(element, end=" ")
        print()

# 3. Display number if rows, columns and elements
    print("rows", len(numbers))
    total_element = 0
    for i in range(len(numbers)):
        print(f"row {i}: {len(numbers[i])}")
        total_element += len(numbers[i])
    print(f"elements: {total_element}")
# 4. Add another row, with a different number of
#    elements and then display rows, columns,
#    and elements totals again
    numbers.append([7,8,9,10,11])

    print()

    for row in numbers:
        for element in row:
            print(element, end=" ")
        print()

    print("rows", len(numbers))

    total_element = 0

    for i in range(len(numbers)):
        print(f"row {i}: {len(numbers[i])}")
        total_element += len(numbers[i])
    print(f"elements: {total_element}")

def two_dim_example2():
# 1. Create a 2d list to represent sales data for
#    3 people .Each row is a separate salesperson.
#    Each column is a month, Jan - April
    sales = [
        [1000,1500,1200,2100], # row0
        [800,2200,2500,500],   # row1
        [1200,1000,700,700]    # row2
    ]

# 2, Show all values for each person, including total
    for i, row in enumerate(sales):
        print(f"Salesperson:{i+1} ", end=" ")
        for elements in row:
            print(elements, end=' ')
        print()
        print("Total:", sum(row))
        print()


def two_dim_example3():
#1. Create a 2d list to track lap times of 3 drivers
    lap_times = [
        ["Ari",45.7,46.2,45.5,45.2],
        ["Noah",47.6,48.1,47.9,47.3],
        ["Jack",45.9,45.2,49.2,48.8]
    ]
#2. Show each driver's laps, total time, and
#   average times
    for i,row in enumerate(lap_times):
        total_time = 0
        print(row[0], end=" ")
        for elements in row[1:]:
            print(elements, end=" ")
            total_time += elements
        print()
        print(f"Total times: {total_time:.1f}")
        average = total_time / (len(row) - 1)
        print(f"Average time: {average:.1f} ")
        print()




#Main Code
two_dim_example3()













