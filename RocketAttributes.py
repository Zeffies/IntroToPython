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
        
        

my_rocket = Rocket('Test')
print("My rocket's position is %d, %d. Its name is %s, and it has a crew-size"
% (my_rocket.x, my_rocket.y, my_rocket.name)
+ " of %d. Its top speed is %d." % (my_rocket.crew_size, my_rocket.top_speed))

rockets = []
rockets.append(Rocket('Firstie', x=10, y=12, crew_size=13, top_speed=11))
rockets.append(Rocket('Secondie', x=15, y=3, crew_size=5, top_speed=6))
rockets.append(Rocket('Thirdie', x=30, y=-12, top_speed=15))

for index, rocket in enumerate(rockets):
    print("Rocket %d's position is %d, %d. Its name is %s, and it has a "
    % (index+1, rocket.x, rocket.y, rocket.name)
    + "crew-size of %d. Its top speed is %d." 
    % (rocket.crew_size, rocket.top_speed))
