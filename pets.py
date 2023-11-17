class Pet:
    CALORIES_PER_POUND = 3000
    __slots__ = ['species', 'name', 'weight', 'fur_color', 'age']
    def __init__(self,species, name, weight, fur_color, age=0):
        self.species = species
        self.name = name
        self.weight = weight
        self.fur_color = fur_color
        self.age = age

    def feed(self, calories):
        pounds = calories / Pet.CALORIES_PER_POUND
        self.weight += pounds
