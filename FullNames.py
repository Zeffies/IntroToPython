4# Write a function that takes in a first name and a last name, 
# and prints out a nicely formatted full name, in a sentence. 
def get_full_name(first_name, last_name):
    full_name = (first_name + ' ' + last_name)
    print('Hello, %s!' % full_name)
# Your sentence could be as simple as, "Hello, full_name."
# Call your function three times, with a different name each time.
get_full_name('Joe', 'Peralta')
get_full_name('Mike', 'Santiago')
get_full_name('Roberta', 'Holt')
