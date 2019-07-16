class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.pronounce = 'meow'
        self.weight = 0

    def speak(self):
        print(self.pronounce)
    
    def eat(self, calories):
        self.weight += calories / 1000
        print('Weight becomes', self.weight)

cat = Pet('Cat', '寶寶')
print(cat)	
print(type(cat))
print(cat.name)

cat.speak()	    # Output: meow
cat.eat(2473)	    # Output: Weight becomes 2.473

