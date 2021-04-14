class Rocket():
    # Simulates a rocket going up
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def move_up(self):
        self.y += 1


my_rocket = Rocket()
print(my_rocket)
print(my_rocket.y)
my_rocket.move_up()
print(my_rocket.y)
print('--------------')
rockets = [Rocket() for x in range(0,5)]

for rocket in rockets:
    print(rocket)
