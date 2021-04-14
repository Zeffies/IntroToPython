mountains_list = {'Mount Everest':8848, 
                  'K2':8611, 
                  'Lhotse':8516, 
                  'Makalu':8485,
                  'Cho Oyu':8201
                  }
mountains_both_units = {}

print('Here are all the mountains I know: ')
for mountain in mountains_list.keys():
    print(mountain)
print('\nHere are their heights:')    
for height in mountains_list.values():
    print(height)

print('\nHere are sentences saying that info with them in alphabetical order:')    
for mountain, height in sorted(mountains_list.items()):
    print("%s is %d meters tall." % (mountain, height))

print('\nHere are the mountains alone, this time in a dictionary with both '
    +'meters and feet.')
# Create a new dictionary with the original height in meters, and convert that
# to feet.
mountains_both_units = {}
for mountain, height in mountains_list.items():
    mountains_both_units[mountain] = {height:(int((height * 3.28084)))}
for mountain in mountains_both_units:
    print(mountain)

print('\nHere are the elevations in meters, this time in the dictionary with'
    + ' both units.')
for mountain, units in mountains_both_units.items():
    for meters in units:
        print(meters)

print("\nHere are the mountain's elevations in feet: ")
for mountain, units in mountains_both_units.items():
    for meters, feet in units.items():
        print(feet)

print("\nHere's a bunch of sentences because why not: ")
for mountain, units in mountains_both_units.items():
    for meters, feet in units.items():
        print("%s is %d meters tall, or %d feet." % (mountain, meters, feet))
        
mountains_with_range = {'mount everest':{'elevation':8848,'range':'himalaya'},
                        'k2':{'elevation':8611,'range':'karakoram'},
                        'lhotse':{'elevation':8516,'range':'himalayas'},
                        'makalu':{'elevation':8485,'range':'himalayas'},
                        'cho oyu':{'elevation':8201,'range':'himalayas'}
                        }
print('\nHere are the mountains in the mountain_with_range dictionary: ')
for mountain in sorted(mountains_with_range.keys()):
    print(mountain.title())
    
# Print out just the mountains' elevations.
print('\nHere are the elevations in the mountain_with_range dictionary: ')
for mountain, data in sorted(mountains_with_range.items()):
    for key in data:
        if key == 'elevation':
            print(data[key])
# Print out just the range for each mountain.
print('\nHere are the ranges in the mountain_with_range dictionary: ')
for mountain, data in sorted(mountains_with_range.items()):
    for key in data:
        if key == 'range':
            print(data[key])
# Print out a series of statements that say everything you know 
# about each mountain: "Everest is an 8848-meter tall mountain 
# in the Himalaya range."
print("\nAnd here's some more sentences:")
for mountain, data in sorted(mountains_with_range.items()):
        print("%s is an %d-meter tall mountain in the %s range." 
        % (
        mountain.title(),
        data['elevation'], 
        data['range'].title())
        )
