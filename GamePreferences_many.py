# Make a list that includes 3 or 4 games that you like to play.
games = ['Minecraft', 'Castlevania', 'Mega Man', 'Spelunky']
# Print a statement that tells the user what games you like.
new_game = ''
first_game = 1
print('This is a list of games that I like: ')
for game in games:
    print('- ' + game)
# Ask the user to tell you a game they like, 
# and store the game in a variable such as new_game.
while new_game != 'quit':
    if first_game == 1:
        new_game = input('\nWhat game do you like? (Enter quit if you do not'
        + ' want to add a game) ')
        if new_game != 'quit':
            games.append(new_game)
        first_game = 2
    else:
        new_game = input('\nWhat is another game you like? (Enter quit when you'
                       + ' have added all of the games you want to) ')
        if new_game != 'quit':
            games.append(new_game)
# Add the user's game to your list.

# Print a new statement that lists all of the games that we like to play
# (we means you and your user).
print('\nThis is a list of games we like to play: ')
for game in games:
    print('- ' + game)
