class Person():
    def __init__(self, name, age=None, place_of_birth=None,
    favourite_colour=None):
        self.name = name
        self.age = age
        self.place_of_birth = place_of_birth
        self.favourite_colour = favourite_colour
        
    def introduce_yourself(self):
        print("Hi, I'm %s!" % self.name.title())
        if self.age:
            print("I'm %d years old!" % self.age)
        if self.place_of_birth:
            print("I was born in %s." % self.place_of_birth)
        if self.favourite_colour:
            print("My favourite colour is %s." % self.favourite_colour)
            
    def age_person(self):
        if self.age:
            self.age += 1
            print("%s has aged a year. They're now %d years old."
            % (self.name, self.age) + " Happy Birthday!")
        else:
            print("""%s has aged a year. I'm not sure how old that makes them,
            but Happy Birthday nonetheless!""".replace('    ','') % self.name)
            
class Student(Person):
    def __init__(self, name, school, grad_year=None, gpa=None, age=None):
        super().__init__(name, age)
        self.school=school
        self.grad_year=grad_year
        self.gpa=gpa
    
    def introduce_yourself(self):
        super().introduce_yourself()
        if not self.grad_year:
            print("I'm going to %s." % self.school)
            if self.gpa:
                print("My gpa is %d" % (self.gpa))
        else:
            print("I went to %s and graduated in %d." 
            % (self.school, self.grad_year))
            if self.gpa:
                print("My gpa was %g" % (self.gpa))
