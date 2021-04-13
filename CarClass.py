class Car():
    
    def __init__(self, make, model, year, num_doors=None, owner=None):
        self.make = make
        self.model = model
        self.year = year
        self.num_doors = num_doors
        self.owner = owner
        
    def describe_car(self):
        print("Make: %s" % self.make)
        print("Model: %s" % self.model)
        print("Year: %d" % self.year)
        if self.num_doors:
            print("Number of Doors: %d" % self.num_doors)
        if self.owner:
            print("Owner: %s" % self.owner)
            
test_car = Car('Tesla', 'Model S', 2020, 4, 'Elon')
test_car.describe_car()
