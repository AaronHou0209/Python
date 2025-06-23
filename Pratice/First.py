# Section1

radius = 15
pi = 3.14
area = pi * radius * radius
print(f'{radius}*{pi}*{radius}={area}')

# Section2
l = 8.5
w = 6
a = l * w
s= a*20
print(f'{l} m*{w}m={a}m^2, the price : {s} ($/m^2) ')

# Section3

slices = float(input('Entry what you want size:'))
price = 3.25
subtotal = price * slices
tax_rate= 0.13
tax= subtotal * tax_rate
total = subtotal + tax


print(f'How many slices would you like: {slices}')
print(f'subtotal:   ${subtotal}')
print(f"tax         ${tax}")
print(f"total       ${total} ")


