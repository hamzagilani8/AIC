# **********Lottery game************

import random

print('******Welcome to the PIAIC Game show *******')
print('Game rules are \n 1- A random number would be selected \n 2- Number would be between 1 and 10 \n 3- You would be given 3 chances')
print(' ')
consent = input('Are you ready? \nPress 1 for YES and 0 for NO: ')
print(' ')

if consent == '1':
    rand_num = random.randint(1,10)
    answers = []
    guess_num = int(input('Guess the number: '))
    answers.append(guess_num)

    if guess_num == rand_num:
        print('**** You won *****')
    else:
        for i in range(2):
            print('!!! Wrong Answer !!!')
            guess_num = int(input('Guess the number again: '))
            answers.append(guess_num)
        print('\n******* You Lost ********')
        print(f'The number was: {rand_num}')
        print(f'Your answers were: {answers}')
        print('***************')
else:
    print('Game Terminated')