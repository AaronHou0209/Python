"""
Demo on the use of try, except, and finally

Author: chengYu hou
Date: 2024 Oct 29
"""

def try_examples():
    try:
        num1= int(input('Entry number (1-100) : '))
        if num1 < 0 or num1 > 100:
            raise ValueError
        num2 = int(input("Entry number (1-100): "))
        if num2 < 0 or num2 > 100:
            raise ValueError
        answer = num1 / num2
        print(f"{num1}/{num2} = {answer}")
    except ValueError:
        print("Input must be an integer (1-100)")
    except ZeroDivisionError:
        print("Can't be divide by 0")
    except Exception as e:
        print(e)
    finally:
        print("program terminated")
# Main code here

try_examples()

















