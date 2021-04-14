from math import sqrt
class Rocket():
    # simulates a rocket
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
        
def display_my_rocket_pos():
    print("My rocket is at %d, %d" % (my_rocket.x, my_rocket.y))
        
my_rocket = Rocket()
display_my_rocket_pos()

my_rocket.move_rocket(0,3)
display_my_rocket_pos()
my_rocket.move_rocket(2,3)
display_my_rocket_pos()
my_rocket.move_rocket()
display_my_rocket_pos()

rockets = [Rocket() for x in range(0,5)]
rockets[0].move_rocket(0,2)
rockets[1].move_rocket(4,12)
rockets[2].move_rocket(10,5)

for index, rocket in enumerate(rockets):
    print("Rocket %d is at %d, %d!" % (index+1, rocket.x, rocket.y))

distance = rockets[2].get_distance(rockets[3])
print("The distance between rocket 3 and 4 is: %d" % distance)
