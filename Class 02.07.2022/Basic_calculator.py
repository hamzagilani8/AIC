operand1 = input('Enter number 1: ')
operator = input('Enter operation: ')
operand2 = input('Enter number 2: ')

if operator == '+':
    result = float(operand1) + float(operand2)
elif operator == '-':
    result = float(operand1) - float(operand2)
elif operator == '*':
    result = float(operand1) * float(operand2)
elif operator == '/':
    result = float(operand1) / float(operand2)
else:
    print('Invalid Operator')
    exit()
    
print(operand1 + operator + operand2 + '=', result)
exit()