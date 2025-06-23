"""
Demo of how to create overloaded function in python

Author: CHENGYU HOU
DATE: SEP 24 2024
"""


# 1. Create a function that accepts a length and a
# width and finds the area of a rectangle
def find_area1(length,width):
    area = length * width
    return area

#2 Re-write the above function to accept a tuple
# parameters . If the tuple has one value in it
# find area of circle. If the tuple has 2 values
# find the area of a rectangle

def find_area(*args):
    if len(args) == 1:
        area = 3.14 * args[0] ** 2
    elif len(args) == 2:
        area = args[0] * args[1]
    else:
        area = 0

    return area


# Main Code Here
answer = find_area1(234,52)
print(f" The rectangle is {answer}")
answer = find_area(24,24,24)
print(f"The area is {answer}")

test_tuple = (2,6,7)
print(len(test_tuple))
print(test_tuple)
print(test_tuple[1]) # first value is 0
