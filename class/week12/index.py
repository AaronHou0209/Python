"""
Demo of a Circle class which can create
circle objects and calculate their area

Author:ChengYu Hou
Date: Nov 2024
"""

import math

class Circle:
#Conestructor method
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi


#Main Code

#1. Create a circle with radius 10 and
#   another with a radius of 20
c1 = Circle(10)
c2 = Circle(20)

#2. Display the radius of both circles
print("Circle 1:")
print(f"radius: {c1.radius}")

print("Circle 2:")
print(f"radius: {c2.radius}")

print()

#3.  Get and display the area of both circle
print("Circle 1:")
print(f"area: {c1.area()}")

print("Circle 2:")
print(f"radius: {c2.area()}")

print()

#4.  Modify the radius of firsy circle and
#    display full results

c1.radius = 1
c2.radius = 2

print("Circle 1:")
print(f"radius: {c1.radius}")
print("Circle 1:")
print(f"area: {c1.area()}")

print()

print("Circle 2:")
print(f"radius: {c2.radius}")
print("Circle 2:")
print(f"radius: {c2.area()}")

print()
#5. Create a new circle, make it equal to
#   first circle, and show full results
c3 = c1
print("Circle 3: ")
print(f"radius: {c3.radius}")
print(f"area: {c3.area()}")

print()
#6.  Modify first circle then display full
#    results for both first and third circle
c1.radius = 2


print("Circle 1: ")
print(f"radius: {c1.radius}")
print(f"area: {c1.area()}")

print("Circle 3: ")
print(f"radius: {c3.radius}")
print(f"area: {c3.area()}")

print()
#7.   Create a new circle with the same radius as c1.
#     Display the new circle. Modify c1, the show
#     both circles
c4 = Circle(c1.radius)


c1.radius = 1


print("Circle 1: ")
print(f"radius: {c1.radius}")
print(f"area: {c1.area()}")

print("Circle 4: ")
print(f"radius: {c4.radius}")
print(f"area: {c4.area()}")















