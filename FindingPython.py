#Store a sentence in a variable, making sure you use the word Python at least twice in the sentence.
sentence = "Python and BASIC are both programming languages, but the current one I'm learning is Python."
#Use the in keyword to prove that the word Python is actually in the sentence.
test_for_python = 'Python' in sentence
print(test_for_python)
#Use the find() function to show where the word Python first appears in the sentence.
first_python = sentence.find('Python')
print(first_python)
#Use the rfind() function to show the last place Python appears in the sentence.
last_python = sentence.rfind('Python')
print(last_python)
#Use the count() function to show how many times the word Python appears in your sentence.
number_of_pythons = sentence.count('Python')
print(number_of_pythons)
#Use the split() function to break your sentence into a list of words. Print the raw list, and use a loop to print each word on its own line.
split_sentence = sentence.split(' ')
print(split_sentence)
for word in split_sentence:
	print(word)
#Use the replace() function to change Python to Ruby in your sentence.
ruby_sentence = sentence.replace('Python', 'Ruby')
print(ruby_sentence)

