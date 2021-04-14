pet_dictionary = {'ziggy':'canary', 'ozzy':'dog', 'oreo':'cat'}
def print_dictionary():
    for pet_name, animal in pet_dictionary.items():
        print('%s is a %s' % (pet_name, animal))
    print('\n')

print("This is the dictionary without modification:")
print_dictionary()

pet_dictionary['ziggy'] = 'robin'
print("This is the dictionary after modifying ziggy's animal tag")
print_dictionary()

pet_dictionary['olaf'] = 'snowman'
print("This is the dictionary after adding olaf to it")
print_dictionary()

del pet_dictionary['ziggy']
print("This is the dictionary after destroying ziggy from reality")
print_dictionary()
