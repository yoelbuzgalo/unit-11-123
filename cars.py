class Car:
    __slots__ = ['__vin', '__make', '__model', '__year', '__mileage', '__fuel']
    def __init__(self, vin, make, model, year, mileage=0, fuel=0):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__fuel = fuel
    
    def print_car(self):
        print("Car={VIN=", self.__vin, ", Make=", self.__make, ", Model=", self.__model, ", Year=", self.__year, ", Mileage=", self.__mileage, ", Fuel=", self.__fuel,"}" ,sep="")

    def filler_up(self, gallons):
        self.__fuel += gallons
        if self.__fuel > 15:
            self.__fuel = 15
