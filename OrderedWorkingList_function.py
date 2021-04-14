#Start with the list you created in Working List.
def career_list(message, careers):
    print('This is the careers in %s order:' % message)
    for career in careers:
        print('\t- ' + career)
careers = ['bee', 'cee', 'ayy', 'dee']
career_list('their original', careers)
career_list('alphabetical', sorted(careers))
career_list('their original', careers)
career_list('reverse alphabetical', sorted(careers, reverse=True))
career_list('their original', careers)
careers.reverse()
career_list('reverse from what they started', careers)
careers.reverse()
career_list('their original', careers)
careers.sort()
career_list('permanently alphabetical', careers)
careers.sort(reverse=True)
career_list('permanently reverse alphabetical', careers)
#You are going to print out the list in a number of different orders.
#Each time you print the list, use a for loop rather than printing the raw list.
#Print a message each time telling us what order we should see the list in.
	#Print the list in its original order.
#print('This is the careers in their original order:')
# for career in careers:
	# print(career)
# print('----------------\n')
	# #Print the list in alphabetical order.
# print('This is the careers in alphabetical order:')
# for career in sorted(careers):
	# print(career)
# print('----------------\n')
	# #Print the list in its original order.
# print('This is the careers in their original order again:')
# for career in careers:
	# print(career)
# print('----------------\n')
	# #Print the list in reverse alphabetical order.
# print('This is the careers in reverse alphabetical order:')
# for career in sorted(careers, reverse=True):
	# print(career)
# print('----------------\n')
	# #Print the list in its original order.
# print('This is the careers in their original order for the third time...:')
# for career in careers:
	# print(career)
# print('----------------\n')
	# #Print the list in the reverse order from what it started.
# careers.reverse()
# print('This is the careers in reverse order from what they started:')
# for career in careers:
	# print(career)
# print('----------------\n')
# careers.reverse()
	# #Print the list in its original order
# print('This is the careers in their original order for a FOURTH time:')
# for career in careers:
	# print(career)
# print('----------------\n')
	# #Permanently sort the list in alphabetical order, and then print it out.
# careers.sort()
# print('This is the careers sorted alphabetically permanently:')
# for career in careers:
	# print(career)
# print('----------------\n')
	# #Permanently sort the list in reverse alphabetical order, and then print it out.
# careers.sort(reverse=True)
# print('This is the careers sorted in reverse alphabetical order permanently:')
# for career in careers:
	# print(career)
# print('----------------\n')
