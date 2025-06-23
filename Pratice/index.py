
value = int(input('Please Entry a value to convert:'))

inches = pounds = pints= value


def inches_to_centimetres():

    centimetres = inches * 2.54
    return centimetres

def pounds_to_kilograms():
    kilograms = pounds * 0.453
    return kilograms

def pints_to_litres():
    litres = pints * 0.473
    return litres

# Main Code Here
a1 = inches_to_centimetres()
a2 = pounds_to_kilograms()
a3 = pints_to_litres()
print(f"{value} inches is {a1} cm^2")
print(f"{value}  lbs is {a2} kgs")
print(f"{value}  pints is  {a3} litres")



def sum_number(*args):
    n1 = int(input("Please enter number 1:"))
    n2 =  int(input("Please enter number 2:"))
    n3 = int(input("Please enter number 3:"))
    n4 = int(input("Please enter number 4:"))
    return [n1,n2,n3,n4]


answer = sum_number()
g1 = answer[0] + answer[1]
g2 = g1 + answer[2]
g3 = g2 + answer[3]
print(f"The sum of the first two numbers is: {g1}")
print(f"The sum of the first three numbers is: {g2}")
print(f'The sum of all the numbers is: {g3}')