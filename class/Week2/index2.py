# global values
TAX_RATE = 0.25

# get inputs

name = input('Entry your name:')
hours = float(input('Enry your work hours:'))
pay_rate = float(input('Entry your pay rate:'))

# process calculations

pre_tax= hours * pay_rate
tax = pre_tax * TAX_RATE
earned = pre_tax - tax

# show results
print(f'Pay sub for {name}')
print('------------------------')
print(f'pre_tax     ${pre_tax:.2f}')
print(f'tax         ${tax:.2f}')
print(f'earned      ${earned:.2f}')
