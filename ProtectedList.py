#Your goal in this exercise is to prove that copying a list protects the original list.
#Make a list with three people's names in it.
people = ['Danny Devito', 'Uma Thurman', 'David Harbour']
#Use a slice to make a copy of the entire list.
people_copy = people[:]
#Add at least two new names to the new copy of the list.
people_copy.append('Winona Ryder')
people_copy.append('Ryan Reynolds')
#Make a loop that prints out all of the names in the original list, along with a message that this is the original list.
print('This is the original list: ')
for person in people:
	print('- ' + person)
#Make a loop that prints out all of the names in the copied list, along with a message that this is the copied list.
print('\nThis is the copied list with two names appended: ')
for person in people_copy:
	print('- ' + person)


