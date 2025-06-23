"""
Demo of creating function that return values

Author : ChengYu Hou
Dare: Sep 24 2024
"""


def add_number(x,y):
    sum_of_value = x + y
    return sum_of_value
# 2. Create a function that accepts a radius, finds the
# area of a circle, and returns the answer.
def fin_circle_area(radius):
    area = 3.14 * radius ** 2  # same as area = 3.14 * radius * radius
    return area



# Main Code Here
answer = add_number(324,24)
answer = add_number(answer,42)
print(f"The sum is {answer}")
circle_area = fin_circle_area(99 )
print(f"The area of the circle is {circle_area}")