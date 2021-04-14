class Person():
    def __init__(self, name, age=None, place_of_birth=None,
     favourite_colour=None):
        self.name = name
        self.age = age
        self.place_of_birth = place_of_birth
        self.favourite_colour = favourite_colour
        
    def introduce_yourself(self):
        print("Hi, I'm %s!" % self.name)
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
            print("%s has aged a year. I'm not sure how old that makes them,"
            % self.name + "\nbut Happy Birthday nonetheless!")
            

def text_seperator():
    print('\n-------------')
test_person = Person('Test', age=23, place_of_birth='Indianapolis',
favourite_colour='Red')
test_person_2 = Person('Test2', favourite_colour='Black')
test_person.introduce_yourself()
text_seperator()
test_person_2.introduce_yourself()
text_seperator()
test_person.age_person()
text_seperator()
test_person_2.age_person()
