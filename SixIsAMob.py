#Bonus: Store your if test in a function called something like crowd_test.
def crowd_test():
    #Write an if test that prints a message about the room being crowded, 
      #if there are more than three people in your list.
    if len(crowd) > 5:
        print("There's a mob in this room!")
    elif len(crowd) >= 3:
        print("Wow, this room is crowded!")
    elif len(crowd) >= 1:
        print("This room isn't that crowded.")
    else:
        print("This room is empty.")
#Make a list of names that includes at least four people.
crowd = ['Danny', 'Uma', 'Arnold', 'Winona']
#Modify your list so that there are only two people in it. 
  #Use one of the methods for removing people from the list, 
  #don't just redefine the list.
crowd_test()
for x in range(1,3):
    crowd.pop()
crowd_test()
crowd.extend(['Joe', 'Mike', 'Roberta', 'Bill', 'Pat'])
crowd_test()
#Run your if test again. There should be no output this time, 
  #because there are less than three people in the list.


