# 1.Declare a variable and put your name in it
name='Aaron'
print(name)

# 2.Declare a variable and put your age in it
age=22
print(age)

# 3.Declare a variable and put decimal value in it
pi=3.14
print(pi)

# 4.Combine text with a variable to display 'Hello'
#   followed by your name and age.

print('Hello',name+'. You are',age,'years old.')
print(f'Hello,{name}. You are {age} years old')
# 5.Adding ,subtract,multiply,and divide number.

x=6
y=4
answer =x+y
print(f'{x}+{y}={answer}')
answer = x-y
print(f'{x}-{y}={answer}')
answer = x*y
print(f'{x}*{y}={answer}')
answer = x/y
print(f"{x}/{y}={answer}")
answer = x%y
print(f"{x}%{y}={answer}")

num1 = 8.2
num2 = 2.15
num3 = num1 / num2
print(f'{num1}/{num2} = {num3}')

# 6.Place the result of num3 into an int variable

num_cast=int(num3)
print(num_cast)

# 7.Perform math operation and place result back in one step

age=age+1
print(age)

age += 1
print(age)

age -=1
print(age)

age *=2
print(age)

name +=name
print(name)