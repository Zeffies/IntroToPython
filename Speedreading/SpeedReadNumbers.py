import random
import os
from time import sleep

score = 0
attempts = 0
current_streak = 0
best_streak = 0


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
    random_number = str(random.randint(100000, 999999))
    print('\t\t\t......ready?.......')
    input('press enter when ready...')
    os.system('cls')
    print_score()
    print_streak()
    print()
    print()
    print('\t\t\t......%s......' % random_number)
    sleep(.1)
    os.system('cls')
    print_score()
    print_streak()
    print()
    print()
    your_guess = input('What number did you see?: ')
    if your_guess == random_number:
        print('Grats, you got it right!')
        score += 1
        attempts += 1
        current_streak += 1
        if current_streak > best_streak:
            best_streak = current_streak
        sleep(.5)
    else:
        print('You guessed %s, but it was %s. Try again.'
              % (your_guess, random_number))
        attempts += 1
        current_streak = 0
        input('press enter to continue...')
    # TODO: Add a current streak / highest streak; calculate percent gotten,
    # and save both the highest streak and attempt/correct numbers and keep
    # those for every time you log in
