
"""
assignment

Author : ChengYu , Chahat
Date : 23 Sept 2024
"""

# step1
id = input("What's ' your customer ID:")
name = input ("What's your name:")
unit = int(input("Units of electricity consumed:"))
sub = input("Are you eligible for a subsidy (yes or no ):")
year = int(input("How many years they have been a customer:"))
tax_rate = 0.13

# step2
if unit <= 199 :
    charge = 0.2
elif 200 <= unit <500:
    charge = 0.3
elif 500 <= unit < 800:
    charge = 0.5
elif 800<= unit:
    charge = 0.75

# step three
if sub == 'yes' :
    sub = 0.1285
else:
    sub = 0
# step four
if year <= 1:
    dis = 0
elif 2 <= year <= 3 :
    dis = 5
elif  4 <= year <= 6 :
    dis =10
elif year > 6 :
    dis = 15
x = charge * unit
y = sub * unit
total = x - dis - y

#step five

if total < 30 :
    total = 30

# step final
print(f"Customer name: {name}")
print(f"Customer ID : {id}")

print(f"Units Consumed: {unit:}  ")

if charge == 0.2:
    print(f"Unit Fee @.20/unit: ${x:.2f}")
elif charge == 0.3:
    print(f"Unit Fee @.30/unit: ${x:.2f}")
elif charge == 0.5:
    print(f"Unit Fee @.50/unit: ${x:.2f}")
elif charge == 0.75 :
    print(f"Unit Fee @.75/unit: ${x:.2f}")
print(f"Loyalty Discount:      -${dis}")


print(f"Subsidy Amount:         -${y:.2f}")

tax = total * tax_rate
z = total - tax


print(f"Subtotal:                ${total:.2f}")
print(f"Tax Amount:              ${tax:.2f}")
print(f"Total Amount Owed:       ${z:.2f}")







