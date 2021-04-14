#Write out the following code without using a list comprehension:

#plus_thirteen = [number + 13 for number in range(1,11)]

plus_thirteen = []
for number in range(1,11):
	plus_thirteen.append(number+13)
for number in plus_thirteen:
	print(number)
