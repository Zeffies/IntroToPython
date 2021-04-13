### Libraries ###
import os

### Functions ###
def display_title_bar():
    os.system('cls')
    
    print("\t************************************")
    print("\t***  An Abacus, made in Python!  ***")
    print("\t************************************")
    print("\t***Input quit at any time to exit.**")
    print("\t************************************")
    

### Define those vars and such
user_number = 'not_chosen'
number_is_valid = False
abacus = ['', '', '', '']

### Main Program ###

# Get User's number
while number_is_valid is False:
    if user_number == 'not_chosen':
        display_title_bar()
        user_number = input("\nPlease enter a number from 1 to 9999: ")
    elif user_number.isnumeric() is False:
        display_title_bar()
        user_number = input("That is not a valid choice. Please try again: ")
    elif 0 <= int(user_number) >= 10000:
        display_title_bar()
        user_number = input("That is not a valid choice. Please try again: ")
    else:
        number_is_valid = True
num_as_list = list(user_number)

display_title_bar()
# Convert user's number into an integer
for index, number in enumerate(num_as_list):
    num_as_list[index] = int(num_as_list[index])
for cur_num in range(0,4):
    try:
        if num_as_list[cur_num]:
            for x in range(1,(10 - num_as_list[cur_num])):
                abacus[cur_num] = abacus[cur_num] + 'x'
            abacus[cur_num] = abacus[cur_num] + '------'
            for x in range(1,(num_as_list[cur_num]+1)):
                abacus[cur_num] = abacus[cur_num] + 'x'
    except:
        abacus[cur_num] = "xxxxxxxxx------"

for aba_print in range(0,4):
    print(abacus[(3 - aba_print)])

