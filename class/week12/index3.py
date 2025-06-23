"""
Demonstrate the creation and use of a static class

Author: ChengYu
Date: Nov 2024
"""



class Calculator:
    g = 9.81

    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def valocity(seconds):
        return Calculator.g * seconds


#Main Code
answer = Calculator.add(2, 3)
print(answer)

answer = Calculator.add(5, 11)
print(answer)

time = float(input("Enter your time: "))
speed = Calculator.valocity(time)
print(f"{speed:.2f} m/s")

Calculator.g = Calculator.g / 6
speed = Calculator.valocity(time)
print(f"{speed:.2f} m/s")







