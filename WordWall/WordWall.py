### Libraries ###
import os
from time import sleep
import sys
import pickle
import random


### Functions ###
def display_title_bar():
    global num_words_known, user_score, user_missed, game_running
    os.system('cls')

    print("\t************************************")
    print("\t***  Word Wall, made in Python!  ***")
    print("\t************************************")
    print("\t****Input q at any time to exit.****")
    print("\t************************************")
    print("\t***This program knows %d word(s)!****" % num_words_known)
    print("\t***This program has %d categories****" % num_categories_known)
    print("\t************************************\n")
    if game_running:
        print("You've gotten %d words right and %d words wrong!"
              % (user_score, user_missed))


def display_main_menu():
    print("1.) See all words known by this program.")
    print("2.) Add a new word.")
    print("3.) Modify or delete an existing word.")
    print("4.) Delete a category.")
    print("5.) Test your knowledge with a quiz!")
    print("q.) Save and quit.")


def display_modify_menu():
    print("You are modifying the entry for %s" % user_word)
    print("1.) Change spelling of %s" % user_word)
    print("2.) Change definition.")
    print("3.) Change category.")
    print("4.) Delete word.")
    print("5.) Cancel modifying.")


def display_categories():
    category_count = 0
    for category in categories:
        print(categories[categories.index(category)].title(), end=' ')
        category_count += 1
        if category_count == 4:
            print('\n')
            category_count = 0
    if category_count != 0:
        print('\n')


def delete_category():
    # need a check to make sure there are categories in the program
    global num_words_known, num_categories_known
    display_title_bar()
    print("Here are all of the categories this program knows: ")
    display_categories()
    delete_check = 'not_chosen'
    print("\nInput c to go back to the main menu")
    user_category = 'not_chosen'
    to_delete = []
    while user_category not in categories:
        if user_category == 'not_chosen':
            user_category = input("\nInput the category you want to "
                                  + "delete: ")
        else:
            # another place you can flood with messages
            user_category = input("\nSorry, that isn't a category,"
                                  + " try again!: ")
        if user_category != 'c':
            if user_category.lower() in categories:
                while delete_check != 'y' and delete_check != 'n':
                    display_title_bar()
                    print("Are you sure you want to delete the category '%s'?"
                          % user_category.title()
                          + "\nIf you do, all words in the category will be deleted"
                          + " as well. \nMake sure to change the category of any"
                          + " words you want to keep.")
                    if delete_check == 'not_chosen':
                        delete_check = input("\nInput y/n: ")
                    else:
                        delete_check = input("\nThat is not a valid choice."
                                             + " Input y or n for yes or no: ")
                if delete_check == 'y':
                    for word, data in dictionary.items():
                        for definition, category in data.items():
                            if category.lower() == user_category.lower():
                                to_delete.append(word)

                    for delword in to_delete:
                        del dictionary[delword]
                        num_words_known -= 1
                        num_categories_known -= 1
                    categories.remove(user_category.lower())
                    break
        else:
            break


# noinspection PyUnreachableCode
def show_all_entries():
    global dictionary, from_main_menu, redo, user_word
    display_title_bar()
    current_line = 0
    last_category = 'none'
    print("Here are all of the words this program knows:")
    for key, data in sorted(dictionary.items()):
        for category in sorted(data.values()):
            if category == last_category:
                break
            if category != 'cat1':
                print('\n')
            print("Category: " + category.title())
            current_category = category
            print('---------------')
            for key2, data2 in dictionary.items():
                for category2 in data2.values():
                    if category2 == current_category:
                        # need to make it so last entry doesn't have comma
                        print(key2.title(), end=', ')
                        current_line += 1
                if current_line == 4:
                    print('\n')
                    current_line = 0
            current_line = 0
            last_category = category
        if current_line != 0:
            print('\n')
    if from_main_menu == True:
        print("\n\nInput c to go back to the main menu")
        user_word = 'not_chosen'
        while user_word not in dictionary:
            if user_word == 'not_chosen':
                user_word = input("\nInput a word you want to see the"
                                  + " definition of: ")
            else:
                # this can flood the screen because it doesn't get cleared.
                # might need to outsource some of this into a second function
                # to make clearing the screen more viable.
                user_word = input("\nSorry, that word isn't in the dictionary,"
                                  + " try again!: ")
            if user_word != 'c':
                if user_word in dictionary:
                    for word, data in dictionary.items():
                        for definition, category in data.items():
                            if word.lower() == user_word.lower():
                                display_title_bar()
                                print("\nThe definition of %s is: "
                                      % user_word)
                                print(definition)
                                input("\n\nPress enter to continue...")
                                show_all_entries()
            if user_word == 'c':
                break
                input("Press enter to continue...")


def enter_new_entry():
    global user_word, user_definition, num_words_known, user_category
    global from_new_entry, del_word
    word_ok = 'not_chosen'
    display_title_bar()
    print("Input c to go back to the main menu.")
    user_word = input("Please input the new word you'd like to add: ")
    user_word.strip()
    if user_word in dictionary:
        entry_already_exists()
    elif user_word == 'c':
        return
    else:
        define()
        if user_definition == 'c':
            return
        categorize()
        if user_category == 'c':
            return
        while word_ok.lower() != 'y':
            display_title_bar()
            print("Word: %s" % user_word)
            print("Definition: %s" % user_definition)
            print("Category: %s" % user_category)
            if word_ok == 'not_chosen':
                word_ok = input("\nIs this okay? (y/n): ")
            else:
                word_ok = input("\nThat was not a valid choice. Use y or n: ")
            if word_ok.lower() == 'n':
                from_new_entry = True
                modify_word()
                if del_word:
                    from_new_entry = False
                    return
                word_ok = 'not_chosen'
            if word_ok.lower() == 'y':
                dictionary[user_word.lower()] = {user_definition:
                                                     user_category.lower()}
                display_title_bar()
                print("\nThank you for teaching me the word '%s!'" % user_word)
                num_words_known += 1
                input("\nPress enter to continue...")


def define():
    global user_definition, user_word
    display_title_bar()
    print("Input c to go back to the main menu.")
    user_definition = input("Please input the definition for %s: " % user_word)
    if user_definition == 'q':
        save_and_quit()


def delete_word():
    global user_word, num_words_known
    delete_choice = 'not_chosen'
    while delete_choice != 'y' and delete_choice != 'n':
        display_title_bar()
        print("Are you sure you want to delete %s?" % user_word)
        if delete_choice == 'not_chosen':
            delete_choice = input("Input y/n: ")
        else:
            delete_choice = input("Sorry, that wasn't a valid choice. "
                                  + "Input y or n for yes or no.")
    if delete_choice == 'y':
        print("The word %s has been deleted!" % user_word)
        del dictionary[user_word]
        num_words_known -= 1
        input("\nInput enter to continue...")


def categorize():
    global user_word, user_category, from_main_menu, num_categories_known
    category_count = 0
    user_category = ''
    add_category_check = 'not_chosen'
    display_title_bar()
    print("Input c to go back to the main menu.")
    print("\nPlease choose a category for %s" % user_word)
    display_categories()
    if category_count != 0:
        print('\n')
    print("\nIf no category fits, type a new one and it will be added to the "
          + "list for future words as well.\n")
    if user_category.lower() != 'any':
        user_category = input("Input category here: ")
    else:
        user_category = input("Sorry, 'any' is a reserved word! Use a"
                              " different word: ")
    if user_category == 'c':
        return
    if user_category not in categories and user_category.lower() != 'any':
        while add_category_check.lower() != 'y' and add_category_check != 'n':
            display_title_bar()
            if add_category_check == 'not_chosen':
                print("Add %s as a new category?" % user_category)
                add_category_check = input("Input y/n: ")
            else:
                print("Sorry, that was not a valid answer! Do you want to add"
                      + " %s as a category?" % user_category)
                add_category_check = input("Input y or n for yes or no: ")
        if add_category_check == 'y':
            num_categories_known += 1
            categories.append(user_category.lower())
        elif add_category_check == 'n' and from_main_menu == True:
            return
        else:
            add_category_check = 'not_chosen'
            categorize()


def change_spelling():
    display_title_bar()
    global user_word
    sp_change = 'not_chosen'
    print("Changing the spelling of %s. Input 'c' to cancel." % user_word)
    while sp_change == 'not_chosen':
        sp_change = input("What would you like to change the spelling to?: ")
        if sp_change == 'c':
            return
        else:
            if dictionary[user_word]:
                dictionary[sp_change] = dictionary[user_word]
                del dictionary[user_word]
            print("Spelling of %s has been changed to %s!" % (user_word,
                                                              sp_change))
            user_word = sp_change


def entry_already_exists():
    global user_word
    modify_choice = 'not_chosen'
    display_title_bar()
    print("That word is already known by this program! Would you like to "
          + "modify the definition or category it's in?")
    for word, data in dictionary.items():
        for definition in data.keys():
            if user_word == word:
                print("The current definition is: %s" % definition)
    while modify_choice.lower() != 'y' or 'n':
        if modify_choice == 'not_chosen':
            modify_choice = input("\nInput y/n for yes or no: ")
        if modify_choice.lower() == 'y':
            modify_word()
            return
        if modify_choice.lower() == 'n':
            break
        elif modify_choice.lower() != 'n':
            print("Sorry, that was not a valid choice.")
            modify_choice = input("\nInput y/n for yes or no: ")


def modify_word():
    global from_new_entry, del_word
    modify_choice = 0
    stop_modifying = False
    while stop_modifying == False:
        display_title_bar()
        display_modify_menu()
        modify_choice = input("\nWhat would you like to do?: ")
        if modify_choice == '1':
            change_spelling()
        elif modify_choice == '2':
            define()
            for word, data in dictionary.items():
                for definition, category in data.items():
                    if word == user_word:
                        dictionary[word] = {user_definition: category}
        elif modify_choice == '3':
            categorize()
            for word, data in dictionary.items():
                for definition, category in data.items():
                    if word == user_word:
                        dictionary[word] = {definition: user_category}
        elif modify_choice == '4':
            if not from_new_entry:
                delete_word()
            else:
                del_word = True
                return
            if user_word not in dictionary:
                stop_modifying = True
        elif modify_choice == '5':
            stop_modifying = True


def quiz_get_category():
    global user_category
    while user_category.lower() not in categories and user_category.lower() != 'any':
        display_title_bar()
        print("Here's a list of categories:\n")
        display_categories()
        print("Which category would you like to be quizzed on?")
        if user_category == 'not_chosen':
            user_category = input("(Type any to be quizzed on any word): ")
        else:
            user_category = input("Sorry, that is not a valid category! Type"
                                  + " one of the known categories above, or 'any' to proceed: ")


def get_full_list():
    global full_list
    for word, data in dictionary.items():
        for definition, category in data.items():
            if user_category.lower() == 'any':
                full_list.append(word)
            else:
                if category == user_category.lower():
                    full_list.append(word)


def change_quiz_category():
    global change_category
    change_category = 'not_chosen'
    while change_category != 'y' and change_category != 'n':
        display_title_bar()
        print("Would you like to change the category you're being"
              + " quizzed on?")
        if change_category == 'not_chosen':
            change_category = input("Input y/n: ")
        else:
            change_category = input("Sorry, that is not a valid choice"
                                    + "! Please input y or n for yes or no.")


# noinspection PyUnboundLocalVariable
def quiz_game():
    global user_score, user_missed, question_number, user_category, full_list
    global game_running, change_category
    user_category = 'not_chosen'
    user_word = 'not_chosen'
    full_list = []
    quiz_list = []
    correct_word = 'not_assigned'
    games_played = 0
    valid_quiz_choices = ['1', '2', '3', '4', 'c', 'q', 'f']

    if not game_running:
        user_score = 0
        user_missed = 0
        game_running = True

    while game_running:
        # get full list to pull from
        if games_played == 0:
            quiz_get_category()
            get_full_list()
        # else:
        # # change this so that it doesn't ask every time, give the user
        # # a command to initiate changing category. it's annoying.
        # change_quiz_category()
        # if change_category == 'y':
        # user_category = 'not_chosen'
        # quiz_get_category()
        # get_full_list()

        # initialize quiz list
        correct_word = random.choice(full_list)
        quiz_list.append(correct_word)
        for x in range(0, 3):
            can_be_added = False
            while not can_be_added:
                word_to_append = random.choice(full_list)
                if word_to_append not in quiz_list:
                    can_be_added = True
            quiz_list.append(word_to_append)
        random.shuffle(quiz_list)

        # the actual game bit
        display_title_bar()
        print("\nThe definition of the word is:")
        for word, data in dictionary.items():
            for definition in data:
                if word == correct_word:
                    print(definition)
        for word in quiz_list:
            num_word = quiz_list.index(word) + 1
            print("%d.) %s" % (num_word, word))
        while user_word not in valid_quiz_choices:
            if user_word != 'not_chosen':
                print("Sorry, please pick a number between 1 and 4 to answer.")
            user_word = input("Type the number of the word that matches"
                              + " the given definition: ")
        if user_word.lower() == 'c':
            game_running = False
        if user_word.lower() == 'f':
            quiz_game()
        if user_word.lower() == 'q':
            game_running = False
            save_and_quit()
        if user_word.lower() != 'c':
            if user_word == str(quiz_list.index(correct_word) + 1):
                user_score += 1
                print("Correct!")
                input("Press enter to continue...")
            else:
                user_missed += 1
                print("Incorrect!")
                input("Press enter to continue...")
        quiz_list = []
        user_word = 'not_chosen'
        games_played += 1
        # choose a random entry from the category they chose,
        # and display the definition.
        # Display 3 random words and the actual correct
        # word. Need to have the correct word be on a random line, as well.
        # Get 3 words and put them in a list unrandom_words. Add the correct word
        # to the end of that list. for word in unrandom_words, randomly pull a
        # word out of unrandom_words and put it into random_words. make sure to
        # remove it from unrandom_words.


def reset_var():
    global user_word, user_definition, user_category, program_running
    global game_running, from_main_menu, valid_choices, menu_choice
    user_word = ''
    user_definition = ''
    user_category = ''
    program_running = True
    game_running = False
    from_new_entry = False
    from_main_menu = False
    valid_choices = [1, 2, 3, 4, 'q']
    menu_choice = 'not_chosen'
    del_word = False
    user_score = 0
    question_number = 0


def save_and_quit():
    global file_object, dictionary, categories
    display_title_bar()
    try:
        file_object = open('wordwall_dictionary.pydata', 'wb')
        pickle.dump(dictionary, file_object)
        file_object.close()
    except Exception as e:
        print(e)
        print("\nCouldn't save the words.")
    try:
        file_object = open('wordwall_categories.pydata', 'wb')
        pickle.dump(categories, file_object)
        file_object.close()
    except Exception as e:
        print(e)
        print("\nCouldn't save the categories.")

    print("\nThanks for using this program. See you next time.")
    sys.exit()


### Load data ###
try:
    file_object = open('wordwall_dictionary.pydata', 'rb')
    dictionary = pickle.load(file_object)
    file_object.close()
    file_object = open('wordwall_categories.pydata', 'rb')
    categories = pickle.load(file_object)
    file_object.close()
    num_words_known = 0
    num_categories_known = 0
    for word in dictionary:
        num_words_known += 1
    for category in categories:
        num_categories_known += 1
except:
    print("couldn't load?")
    sleep(3)
    dictionary = {}
    categories = []
    num_words_known = 0
    num_categories_known = 0

### Define variables ###
user_word = ''
user_definition = ''
user_category = ''
program_running = True
game_running = False
from_main_menu = False
from_new_entry = False
del_word = False
valid_choices = ['1', '2', '3', '4', 'q']
menu_choice = 'not_chosen'
user_score = 0
user_missed = 0

### Main Program ###

while program_running == True:
    while menu_choice not in valid_choices:
        display_title_bar()
        display_main_menu()
        if menu_choice == 'not_chosen':
            menu_choice = input("Which would you like to do?: ")
        elif menu_choice not in valid_choices:
            menu_choice = input("Sorry, that is not a valid choice: ")
        if menu_choice == '1':
            from_main_menu = True
            if num_words_known > 0:
                show_all_entries()
                from_main_menu = False
            else:
                display_title_bar()
                print("No words known by this program! Add some to see"
                      + " them listed here.")
                input("\nPress enter to continue...")
            reset_var()
        if menu_choice == '2':
            enter_new_entry()
            reset_var()
        if menu_choice == '3':
            user_word = 'not_chosen'
            if num_words_known > 0:
                while user_word not in dictionary:
                    show_all_entries()
                    if user_word == 'not_chosen':
                        print("\n\n(Enter c to cancel choosing to modify a "
                              + "word)")
                        user_word = input("\nWhich word would you like to "
                                          + "modify?: ")
                    else:
                        user_word = input("\n\nSorry, the word %s isn't found!"
                                          % user_word + " Input another: ")
                    if user_word == 'c':
                        break
                if user_word != 'c':
                    modify_word()
            else:
                display_title_bar()
                print("No words known by this program! Add something "
                      + "before choosing to modify a word.")
                input("\nPress enter to continue...")
            reset_var()
        if menu_choice == '4':
            delete_category()
            reset_var()
        if menu_choice == '5':
            quiz_game()
            reset_var()
        if menu_choice == 'q':
            save_and_quit()
