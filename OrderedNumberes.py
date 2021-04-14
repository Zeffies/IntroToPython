#Make a list of 5 numbers, in a random order.
numbers = [51, 73, 1, 40, 103]
#You are going to print out the list in a number of different orders.
#Each time you print the list, use a for loop rather than printing the raw list.
#Print a message each time telling us what order we should see the list in.
#Print the numbers in the original order.
print('This is the numbers in their original order:')
for number in numbers:
	print(number)
print('----------------\n')
#Print the numbers in increasing order.
print('This is the numbers in increasing order:')
for number in sorted(numbers):
	print(number)
print('----------------\n')
#Print the numbers in the original order.
print('This is the numbers in their original order:')
for number in numbers:
	print(number)
print('----------------\n')
#Print the numbers in decreasing order.
print('This is the numbers in decreasing order:') 
for number in sorted(numbers, reverse=True):
	print(number)
print('----------------\n')
#Print the numbers in their original order.
print('This is the numbers in their original order:')
for number in numbers:
	print(number)
print('----------------\n')
#Print the numbers in the reverse order from how they started.
numbers.reverse()
print('This is the numbers in reverse order from what they started:')
for number in numbers:
	print(number)
print('----------------\n')
numbers.reverse()
#Print the numbers in the original order.
print('This is the numbers in their original order:')
for number in numbers:
	print(number)
print('----------------\n')
#Permanently sort the numbers in increasing order, and then print them out.
print('This is the numbers sorted in increasing order permanently:')
numbers.sort()
for number in numbers:
	print(number)
print('----------------\n')
#Permanently sort the numbers in descreasing order, and then print them out.
print('This is the numbers sorted in decreasing order permanently:')
numbers.sort(reverse=True)
for number in numbers:
	print(number)
print('----------------\n')
