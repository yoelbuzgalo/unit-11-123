class Pet:
    CALORIES_PER_POUND = 3000
    CALORIES_PER_MILE = 100
    __slots__ = ['__species', '__name', '__weight', '__fur_color', '__age']
    def __init__(self,species, name, weight, fur_color, age=0):
        self.__species = species
        self.__name = name
        self.__weight = weight
        self.__fur_color = fur_color
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_weight(self):
        return self.__weight

    def feed(self, calories):
        pounds = calories / Pet.CALORIES_PER_POUND
        self.__weight += pounds

    def walk(self, miles):
        pounds = miles * Pet.CALORIES_PER_MILE/Pet.CALORIES_PER_POUND
        self.__weight -= pounds
