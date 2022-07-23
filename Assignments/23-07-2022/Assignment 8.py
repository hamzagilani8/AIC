# Get 2 lists with some similar numbers and find the common elements
import random

# Making lists
first = []
second = []
for i in range(6):
    first_list_element = random.randint(1,5)
    first.append(first_list_element)
    second_list_element = random.randint(1,5)
    second.append(second_list_element)

# Getting commons
commons = []
for i in first:
    for j in second:
        if first[i] == second[j]:
            commons.append(first[i])


# printing
print(f'First list is: {first} \nSecond list is {second}')
print(f'\nCommons are: {commons}')