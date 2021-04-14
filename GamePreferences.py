# Make a list that includes 3 or 4 games that you like to play.
games = ['Minecraft', 'Castlevania', 'Mega Man', 'Spelunky']
# Print a statement that tells the user what games you like.
print('This is a list of games that I like: ')
for game in games:
    print('- ' + game)
# Ask the user to tell you a game they like, 
# and store the game in a variable such as new_game.
new_game = input('\nWhat game do you like? ')
# Add the user's game to your list.
games.append(new_game)
# Print a new statement that lists all of the games that we like to play
# (we means you and your user).
print('\nThis is a list of games we like to play: ')
for game in games:
    print('- ' + game)
