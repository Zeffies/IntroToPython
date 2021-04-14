import pickle
import os
# Write a program that lets users enter a number of different games.

### Load data ###
try:
    file_object = open('picklinggames.pydata', 'rb')
    games = pickle.load(file_object)
    file_object.close()
except:
    games = []
    
### Functions ###
def display_title_bar():
    os.system('cls')
    
    print("\t**************************************")
    print("\t***  The Amazing Game Rememberer!  ***")
    print("\t**************************************")
    print("\tStats: This program knows %d games" % len(games))
    
def show_choices():
    print('\n\t1: See a list of games known by this program.')
    print('\t2: Add a new game to be remembered.')
    print('\tq: Save and exit.')
    
    return input('\nWhat would you like to do?: ')

def show_games():
    if games:
        print('\n\tHere are the games that I know:\n')
        for game in games:
            print('\t- ' + game.title())
    else:
        print("I don't know any games yet!")

def get_game():
    new_game = input('\nTell me the game name: ')
    print(new_game.lower() in games)
    print(games)
    if new_game.lower() in games:
        while new_game.lower() in games and new_game.lower() != 'q':
            display_title_bar()
            print('\n I already know that game. Try another!')
            new_game = input('\n (input q if you wish to stop adding a new game): ')
        if new_game.lower() != 'q':
            display_title_bar()
            games.append(new_game.lower())
            print('\n\tThanks for telling me about %s!' % new_game.title())
        else:
            display_title_bar()
    else:
        games.append(new_game.lower())
        display_title_bar()
        print('\n\tThanks for telling me about %s!' % new_game.title())
    
### Main Program ###
choice = ''
display_title_bar()
while choice.lower() != 'q':
    choice = show_choices()
    display_title_bar()
    if choice == '1':
        show_games()
    elif choice == '2':
        get_game()
    elif choice.lower()  == 'q':
        print('\n\tThanks for using this program!')
    else:
        display_title_bar()
        print('\n\tI did not understand that choice. Try again!\n')
        
### Save Data ###
try:
    file_object = open('picklinggames.pydata', 'wb')
    pickle.dump(games, file_object)
    file_object.close()

except Exception as e:
    print(e)
    print("I couldn't figure out how to store the games, sorry.")
# Save the games to disk, using pickle, before the program closes.
# Load the games from the saved file at the beginning of your program.
