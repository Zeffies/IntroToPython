#Store a sentence in a variable.
sentence = 'This is a somewhat longer sentence for this problem.' 
#Using slices, 
#print out the first five characters, 
first_characters = sentence[:6]
print('This is the first five characters: ' + first_characters)
#any five consecutive characters from the middle of the sentence,
middle_characters = sentence[6:11]
print('These are five characters from the middle of the sentence: ' + middle_characters) 
#and the last five characters of the sentence.
last_characters = sentence[-5:]
print('These are the last five characters in the sentence: ' + last_characters)
