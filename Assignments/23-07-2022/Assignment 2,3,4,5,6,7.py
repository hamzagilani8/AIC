import random

# Disclaimer
print('**************Hello and welcome to this Program****************')
print('This program would take 2 limits and create a list of random numbers with length of your choice')
print('It then takes out list of numbers grater than "40" and gives you its mean and median')
print(' ')

# Taking Inputs
upr_lim = int(input('Enter Upper limit: '))
low_lim = int(input('Enter lower limit: '))
length = int(input('Length of list: '))

rand_numbers_list = []
greater_than_40 = []
sum = 0

# Getting random numbers
# storing them in a list
# Filtering numbers greater than 40 and sum them
for i in range((length+1)):
    rand_number = random.randint(low_lim,upr_lim)
    if rand_number >= 40:
        greater_than_40.append(rand_number)
        print('Greater than 40')
        sum = sum + rand_number
    rand_numbers_list.append(rand_number)
    print(rand_number)

# Checking the maximum and minimum numbers
max_num = 0
min_num = int(rand_numbers_list[0])
for x in range(100):
    if max_num < rand_numbers_list[x]:
        max_num = rand_numbers_list[x]
    if min_num > rand_numbers_list[x]:
        min_num = rand_numbers_list[x]

# Calculating Median
if_odd = len(greater_than_40) % 2
if if_odd == 0:
    a = int((len(greater_than_40)/2))
    med = greater_than_40[a]
else:
     a = int((len(greater_than_40)/2)-1)
     b = a+1
     med1 = greater_than_40[a]
     med2 = greater_than_40[b]
     med = (med1+med2)/2

# Printing results
print('***********')
print(f'Random numbers are: {rand_numbers_list}')
print('***********')
print(f'Random list have the maximum value of: {max_num}')
print(f'Random list have the minimum value of: {min_num}')
print('***********')
print(f'Numbers greater than 40 are: {greater_than_40}')
print('***********')
print(f'{len(greater_than_40)} numbers in the list are greater than 40 and have a sum of = {sum}')
print(f'Mean of these 40 numbers is: {sum/len(greater_than_40)}')
print(f'Median of these 40 numbers is: {med}')
