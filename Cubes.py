#We saw how to make a list of the first ten squares. 
#Make a list of the first ten cubes (1, 8, 27... 1000) using a list comprehension, and print them out.
cubes = [number**3 for number in range(1,11)]
for cube in cubes:
	print(cube)
