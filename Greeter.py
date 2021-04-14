# Write a function that takes in a person's name, and prints out a greeting.
def greeting(name):
    print('Hello and welcome, %s!\n' % name
        + 'This is a test program, %s.\n' % name
        + 'Why does this need to be three lines, %s?\n' % name
        )
# The greeting must be at least three lines, and the person's name must be in each line.
# Use your function to greet at least three different people.
names_ = ['Todd', 'Walter', 'Cheryl']
# Bonus: Store your three people in a list, and call your function from a for loop.
for name in names_:
    greeting(name)
