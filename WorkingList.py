# Make a list that includes four careers, such as 'programmer' and 'truck driver'.
careers = ['programmer', 'truck driver', 'construction worker', 'teacher']
# Use the list.index() function to find the index of one career in your list.
index = careers.index('truck driver')
print(index)
# Use the in function to show that this career is in your list.
print('construction worker' in careers)
# Use the append() function to add a new career to your list.
careers.append('clerk')
# Use the insert() function to add a new career at the beginning of the list.
careers.insert(0, 'dog walker')
# Use a loop to show all the careers in your list.
for career in careers:
	print(career.title())
print(len(careers))
