import random
import os
from time import sleep

"""
This program is to practice reading two sets of numbers at once
"""

score = 0
attempts = 0
current_streak = 0
best_streak = 0
single_digit_nums = []
double_digit_nums = []

for i in range(10, 100):
    single_digit_nums.append('0' + str(i))
for i in range(10, 100):
    double_digit_nums.append('0' + str(i))


def print_score():
    print('Score: %d / %d attempts' % (score, attempts))


def print_streak():
    print('Current streak: %d / Best streak: %d'
          % (current_streak, best_streak))


while True:
    os.system('cls')
    print_score()
    print_streak()
    print()
    print()
    random_number = str(random.randint(10, 1000))
    random_number_2 = str(random.randint(10, 1000))
    if ('0' + random_number) in single_digit_nums:
        random_number = '0' + random_number
    if ('0' + random_number_2) in double_digit_nums:
        random_number_2 = '0' + random_number_2
    print('\t\t\t......ready?.......')
    input('press enter when ready...')
    os.system('cls')
    print_score()
    print_streak()
    print()
    print()
    print('\t\t\t......%s......' % random_number)
    print('\t\t\t......%s......' % random_number_2)
    sleep(.1)
    os.system('cls')
    print_score()
    print_streak()
    print()
    print()
    your_guess = input('What was the top number?: ')
    your_guess_2 = input('What was the bottom number?: ')
    if your_guess == random_number and your_guess_2 == random_number_2:
        print('Grats, you got it right!')
        score += 1
        attempts += 1
        current_streak += 1
        if current_streak > best_streak:
            best_streak = current_streak
        sleep(.5)
    else:
        print('You guessed %s and %s, but it was %s and %s. Try again.'
              % (your_guess, your_guess_2, random_number, random_number_2))
        attempts += 1
        current_streak = 0
        input('press enter to continue...')
    # TODO: Add a current streak / highest streak; calculate percent gotten,
    # and save both the highest streak and attempt/correct numbers and keep
    # those for every time you log in
