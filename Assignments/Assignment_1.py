# ***********Get a number and identify either its Odd or Even**********

print('*****Even odd detector******')

# Get Input
num = int(input ('Enter a Numer: '))
# Main
result = num % 2
if result == 0:
    print('The number entered is EVEN')
else:
    print('The number enterd is ODD')
