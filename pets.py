class Pet:
    __slots__ = ['species', 'name', 'weight', 'fur_color', 'age']
    def __init__(self,species, name, weight, fur_color, age=0):
        self.species = species
        self.name = name
        self.weight = weight
        self.fur_color = fur_color
        self.age = age