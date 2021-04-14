exercize_dictionary = {'Squat Thrusts':5, 'Sit-ups':20, 'Push-ups':10}
def print_dictionary():
    for exercizes, amount in exercize_dictionary.items():
        print("Tim did %d %s." % (amount, exercizes.lower()))
    print('\n')
print_dictionary()

exercize_dictionary['Deadlifts'] = exercize_dictionary['Squat Thrusts']
del exercize_dictionary['Squat Thrusts']
print_dictionary()

exercize_dictionary['Deadlifts'] = 10
print_dictionary()

exercize_dictionary['Jumping Jacks'] = 20
print_dictionary()

del exercize_dictionary['Sit-ups']
print_dictionary()
