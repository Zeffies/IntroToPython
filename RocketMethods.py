from time import sleep
from math import sqrt
class Rocket():
    # simulates a rocket
    
    def __init__(self, name, x=0, y=0, crew_size=1, top_speed=10):
        self.x = x
        self.y = y
        self.name = name
        self.crew_size = crew_size
        self.top_speed = top_speed
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
        
    def launch(self):
        countdown = 3
        for x in range(0,countdown):
            print("%d..." % countdown)
            sleep(1)
            countdown -= 1
        print("Blastoff! %s has launched!" % self.name)
        
    def land_rocket(self):
        self.x = 0
        self.y = 0
        
    def safety_check(self, other_rocket):
        distance = self.get_distance(other_rocket)
        if distance == 0:
            print("The rocket %s and %s have crashed!" 
            % (self.name, other_rocket.name))
        elif distance <= 5:
            print("Watch out! The rockets %s and %s are awfully close!"
            % (self.name, other_rocket.name))
        elif distance > 5:
            print("The rockets %s and %s are at a safe distance from"
            % (self.name, other_rocket.name)
            + " each other.")
        
        
        
my_rocket = Rocket('Test', x=30, y=20)
#my_rocket.launch()
print("The rocket is currently located at %d, %d." % (my_rocket.x, my_rocket.y))
#input("Press enter to land rocket.")
#my_rocket.land_rocket()
#print("The rocket is currently located at %d, %d." % (my_rocket.x, my_rocket.y))
rocket_2 = Rocket('Test2', x=30, y=20)
my_rocket.safety_check(rocket_2)
