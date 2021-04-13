#Store five names in a list.
names = ['Danny', 'Uma', 'David', 'Winona', 'Arnold'] 
#Make a second list that adds the phrase "is awesome!" to each name, using a list comprehension.
awesome_names = [name + ' is awesome!' for name in names]
#Print out the awesome version of the names.
for awesome_name in awesome_names:
	print(awesome_name)
