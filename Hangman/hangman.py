### Libraries ###
import os
import random
import pickle
import sys
from time import sleep
from PyDictionary import PyDictionary
import textwrap

### Functions ###
def display_title_bar():
    os.system('cls')
    
    print("\t***********************************")
    print("\t***  Hang-man, made in Python!  ***")
    print("\t***********************************")
    print("\t**Input quit at any time to exit.**")
    print("\t***********************************")
    
    if game_running == True:
        global games_played
        if games_played >= 1:
            display_score()
        display_gallows()
        print("\nWrong letters you have guessed:" + str(wrong_letters) + '\n')
    print('\n')

def display_score():
    global num_players
    if num_players == 1:
        print("\tYou have won %d time(s)! You've lost %d time(s)." % 
        (single_player_wins, single_player_deaths))
    if num_players == 2:
        print("\t%s: %d wins  |  %s: %d wins" % (player_1, player_1_wins,
        player_2, player_2_wins))

def display_gallows():
    global wrong_guesses
    print('\t\t _______')
    print('\t\t |     |')
    print('\t\t |     |')
    if wrong_guesses > 0:
        print('\t\t O     |')
    else:
        print('\t\t       |')
    if wrong_guesses == 2:
        print('\t\t |     |')
    elif wrong_guesses == 3:
        print('\t\t/|     |')
    elif wrong_guesses >= 4:
        print('\t\t/|\\    |')
    else:
        print('\t\t       |')
    if wrong_guesses == 5:
        print('\t\t/      |      ' + gameboard_string)
    elif wrong_guesses >= 6:
        print('\t\t/ \\   |      ' + gameboard_string)
    else:
        print('\t\t       |      ' + gameboard_string)
    print('\t\t       |')
    print('\t\t       |')
    print('\t\t_______|')

def get_num_of_players():
    valid_choices = str(list(range(1,3)))
    num_players = input("\nHow many players are there? (Input 1 or 2): ")
    if num_players.lower() == 'quit':
        sys.exit()
    if num_players not in valid_choices or num_players == '':
        while num_players not in valid_choices or num_players == '':
            display_title_bar()
            num_players = input("\nSorry, that's not a valid number of players."
            + " (Please input either 1 or 2): ")
            if num_players.lower() == 'quit':
                sys.exit()
    num_players = int(num_players)
    return num_players
    
def get_player_names():
    display_title_bar()
    global player_1, player_2
    player_1 = input("Please input player 1's name: ")
    if player_1.lower() == 'quit':
        sys.exit()
    player_2 = input("Please input player 2's name: ")
    if player_2.lower() == 'quit':
        sys.exit()
    
def player_order_choices():
    print("Please choose who is choosing the word:")
    print("1.) %s" % player_1)
    print("2.) %s" % player_2)
    print("r.) Random.")

def show_orderstyle_choices():
	os.system('cls')
	print("How do you want to decide the order you play in?\n")
	print("1.) Players alternate who chooses the word.")
	print("2.) The person who is leading in overall score picks the word.")
	print("3.) The person who is losing in overall score picks the word.")
	print("4.) The computer randomly picks who chooses the next word.")
	print("5.) You pick who chooses the word each round.")
    
def show_turnorder5_choices():
    os.system('cls')
    print('Who do you want to choose the next word?')
    print('1.) %s' % player_1)
    print('2.) %s' % player_2)

def get_player_order():
# If it's the first game, ask who goes first: player 1, 2, or random
    global word_chooser, not_word_chooser, games_played, turn_order
    global valid_choices
    if games_played == 0:
        player_order = 'not_chosen'
        valid_choices = ['1', '2', 'r', 'quit']
        while player_order.lower() not in valid_choices:
            if player_order == 'not_chosen':
                display_title_bar()
                player_order_choices()
                player_order = input("What is your choice?: ")
            elif player_order.lower() != 1 or 2 or 'r' or 'quit':
                display_title_bar()
                player_order_choices()
                player_order = input("Sorry, I didn't understand that choice."
                + " Please try again: ")
        if player_order.lower() == 'quit':
            sys.exit()
        elif player_order == '1':
            word_chooser = player_1
            not_word_chooser = player_2
        elif player_order == '2':
            word_chooser = player_2
            not_word_chooser = player_1
        elif player_order.lower() == 'r':
            players = [player_1, player_2]
            word_chooser = random.choice(players)
            if word_chooser == player_1:
                not_word_chooser = player_2
            else:
                not_word_chooser = player_1
        else:
            print("Error somewhere getting player order.")
                
# If this is run after the first game, ask what type of order you want
    elif games_played == 1:
        for x in range(1,6):
            valid_choices.append(str(x))
        valid_choices.append('quit')
        while turn_order not in valid_choices:
            if turn_order == 'not_chosen':
                show_orderstyle_choices()
                turn_order = input("What is your choice?: ")
            elif turn_order not in valid_choices:
                show_orderstyle_choices()
                turn_order = input("I'm sorry, that is not one of the options."
                + " Please try again: ")
        if turn_order.lower() == 'quit': 
            sys.exit()       
    if games_played >= 1:
        if turn_order == '1':
            if word_chooser == player_1:
                word_chooser = player_2
                not_word_chooser = player_1
            else:
                word_chooser = player_1
                not_word_chooser = player_2
        elif turn_order == '2':
            if player_1_wins > player_2_wins:
                word_chooser = player_1
                not_word_chooser = player_2
            else:
                word_chooser = player_2
                not_word_chooser = player_1
        elif turn_order == '3':
            if player_1_wins < player_2_wins:
                word_chooser = player_1
                not_word_chooser = player_2
            else:
                word_chooser = player_2
                not_word_chooser = player_1
        elif turn_order == '4':
            word_chooser = random.choice(players)
            if word_chooser == player_1:
                not_word_chooser = player_2
            else:
                not_word_chooser = player_1
        elif turn_order == '5':
            valid_choices = str(list(range(1,3)))
            turn_order_5_input = 'not_chosen'
            while turn_order_5_input not in valid_choices:
                if turn_order_5_input == 'not_chosen':
                    show_turnorder5_choices()
                    turn_order_5_input = input("What is your choice?: ")
                    if turn_order_5_input == 'quit':
                        sys.exit()
                elif turn_order_5_input not in valid_choices:
                    show_turnorder5_choices()
                    turn_order_5_input = input("I'm sorry, that is not "
                    + "one of the options. Please try again: ")
                    if turn_order_5_input == 'quit':
                        sys.exit()
            if turn_order_5_input == '1':
                word_chooser = player_1
                not_word_chooser = player_2
            else:
                word_chooser = player_2
                not_word_chooser = player_1
                
    # From then on, this will instantly return who plays next if they
    # Choose to play another game
    
def get_word():
    global word, letters, gameboard_list, gameboard_string
    word = 'Not_chosen'
    letters = []
    gameboard_list = []
    gameboard_string = ''
    display_title_bar()
    if num_players == 1:
        try:
            english_dictionary = open('words_alpha.txt', 'r')
            lines = english_dictionary.readlines()
            while str(dictionary.meaning(word))[0:4] == 'None':
                display_title_bar()
                randomline = random.choice(range(1,370103))
                word = lines[randomline-1]
        except:
            english_dictionary = []
            print('oops')
        finally:
            english_dictionary.close()
        # Open the dictionary and get a random word
    else:
        global word_chooser
        print("%s, please look away from the screen while %s chooses a word!"
        % (not_word_chooser, word_chooser))
        word = input("%s, please input a word or phrase: " % word_chooser)
        if word == 'quit':
            sys.exit()
    letters = list(word)
    if letters[-1] == '\n':
        letters.pop()
        word = ''.join(letters)
    for letter in letters:
        if letter != ' ':
            gameboard_list.append('_')
        else:
            gameboard_list.append(' ')
    gameboard_string = list_to_string(gameboard_list)

def get_letter():
    global current_letter, wrong_letters
    current_letter = 'not_chosen'
    if len(user_letters) == 0:
        while current_letter not in valid_letters:
            display_title_bar()
            if current_letter == 'not_chosen':
                current_letter = input("Please input a letter: ")
                if current_letter == 'quit':
                    sys.exit()
            else:
                current_letter = input("Sorry, that is not a valid letter!"
                + " Try again: ")
                if current_letter == 'quit':
                    sys.exit()
        user_letters.append(current_letter)
    else:
        while current_letter not in valid_letters:
            display_title_bar()
            if current_letter == 'not_chosen':
                current_letter = input("Please input another letter: ")
                if current_letter == 'quit':
                    sys.exit()
            else:
                current_letter = input("Sorry, that is not a valid letter!"
                + " Try again: ")
                if current_letter == 'quit':
                    sys.exit()
        user_letters.append(current_letter)
        
def check_letter():
    global letter_index, current_letter, letters, gameboard_list, wrong_guesses
    global gameboard_string, right_guesses
    if current_letter in letters:
        while current_letter in letters:
            letter_index = letters.index(current_letter)
            gameboard_list[letter_index] = current_letter
            gameboard_string = list_to_string(gameboard_list)
            letters[letter_index] = '_'
            right_guesses = right_guesses + 1
    else:
        wrong_letters.append(current_letter)
        wrong_guesses = wrong_guesses + 1
    valid_letters.remove(current_letter)
        
def list_to_string(s):
    str1 = ""    
    for ele in s:
        str1 += ele
    return str1


def reset_game():
    global solved, failed, wrong_letters, wrong_guesses, right_guesses
    global valid_letters
    solved = False
    failed = False
    wrong_letters = []
    right_guesses = 0
    wrong_guesses = 0
    valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

### Define all those variables ###
game_running = False
games_played = 0
player_1 = player_2 = ''
player_1_wins = player_2_wins = 0
player_order = turn_order = turn_order_5_input = 'not_chosen'
word_chooser = not_word_chooser = ''
wrong_guesses = right_guesses = 0
valid_choices = []
num_players = 0
valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = []
gameboard_list = []
gameboard_string = ''
user_letters = []
wrong_letters = []
current_letter = ''
letter_index = 0
solved = failed = False
single_player_wins = single_player_deaths = 0
dictionary = PyDictionary()


### Main Program ###
display_title_bar()
num_players = get_num_of_players()
if num_players == 2:
    get_player_names()
    get_player_order()
get_word()
while current_letter != 'quit':
    game_running = True
    get_letter()
    check_letter()
    if right_guesses == len(letters):
        solved = True
    if wrong_guesses == 6:
        failed = True
    if solved == True:
        game_running = False
        games_played = games_played + 1
        if num_players == 1:
            single_player_wins = single_player_wins + 1
            display_title_bar()
            print("The word was %s." % word)
            try:
                print("Definition: ", 
                textwrap.fill(str(dictionary.meaning(word)), 64, 
                subsequent_indent=(' '*len("Definition:  "))))
            except:
                print("Definition not found.")
            print("\nSynonyms: ", 
            textwrap.fill(str(dictionary.synonym(word)), 64,
            initial_indent=('  '), 
            subsequent_indent=(' '*len("Synonyms:    "))))
            print("-"*64)
            print("Congrats, you've beaten the game!")
            input("\nPress Enter to continue...")
        if num_players == 2:
            if word_chooser == player_1:
                player_2_wins += 1
            else:
                player_1_wins += 1
            display_title_bar()
            print("The word was %s." % word)
            print("Congrats, %s! You've guessed %s's word and gained a point!"
            % (not_word_chooser, word_chooser))
            input("\nPress Enter to continue...")
            get_player_order()
        reset_game()
        get_word()

    if failed == True:
        game_running = False
        games_played += 1
        if num_players == 1:
            single_player_deaths += 1
            display_title_bar()
            print("The word was %s." % word)
            print("-"*64)
            try:
                print("Definition: ", 
                textwrap.fill(str(dictionary.meaning(word)), 64, 
                subsequent_indent=(' '*len("Definition:  "))))
            except:
                print("Definition not found.")
            print("\nSynonyms: ", 
            textwrap.fill(str(dictionary.synonym(word)), 64,
            initial_indent=('  '), 
            subsequent_indent=(' '*len("Synonyms:    "))))
            print("-"*64)
            print("\nYou've lost! Don't feel too bad, with 370102 words to"
            + " choose from, I had the advantage for sure!")
            input("\nPress Enter to continue...")
        if num_players == 2:
            if word_chooser == player_1:
                player_1_wins += 1
            else:
                player_2_wins += 1
            display_title_bar()
            print("The word was %s." % word)
            print("Congrats, %s! You've picked a word/phrase that %s couldn't" % (word_chooser, not_word_chooser)
            + " guess. Better luck next time, %s!" % not_word_chooser)
            input("\nPress Enter to continue...")
            get_player_order()
        reset_game()
        get_word()
        
    
