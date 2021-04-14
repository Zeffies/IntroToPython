mountains_list = {'Mount Everest':8848, 
                  'K2':8611, 
                  'Lhotse':8516, 
                  'Makalu':8485,
                  'Cho Oyu':8201
                  }


print('Here are all the mountains I know: ')
for mountain in mountains_list.keys():
    print(mountain)
print('\nHere are their heights:')    
for height in mountains_list.values():
    print(height)
print('\nHere are sentences saying that info with them in alphabetical order:')
    
for mountain, height in sorted(mountains_list.items()):
    print("%s is %d meters tall." % (mountain, height))
    
