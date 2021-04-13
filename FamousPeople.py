# Make a list that includes the names of four famous people.
famous_people = ['David Harbour', 'Winona Ryder', 'Uma Thurman', 'Danny Devito']
# Remove each person from the list, one at a time, using each of the four methods we have just seen:
# Pop the last item from the list, and pop any item except the last item.
famous_people.pop()
print(famous_people)
famous_people.pop(1)
print(famous_people)
# Remove one item by its position, and one item by its value.
del famous_people[0]
print(famous_people)
famous_people.remove('Uma Thurman')
# Print out a message that there are no famous people left in your list, and print your list to prove that it is empty.
print('There are no famous people left in the list: ', famous_people)

