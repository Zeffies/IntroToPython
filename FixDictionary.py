from PyDictionary import PyDictionary
import pickle
currentline = 0
valid_words = []
dictionary = PyDictionary()
try:
    english_dictionary = open('words_alpha.txt', 'r')
    lines = english_dictionary.readlines()
    while currentline <= 10:
        currentline += 1
        word = lines[currentline-1]
        if str(dictionary.meaning(word))[0:4] == 'None':
            print("%d.) Word added to be removed!" % currentline)
        else:
            valid_words.append(word)
            print("%d.) Word is valid!" % currentline)
except:
    english_dictionary = []
    print('oops')
finally:
    english_dictionary.close()
    
try:
    file_object = open('words_alpha_fixed.txt', 'wb')
    pickle.dump(valid_words, file_object)
    file_object.close()
except Exception as e:
    print(e)
    print("\nCouldn't save the words.")
