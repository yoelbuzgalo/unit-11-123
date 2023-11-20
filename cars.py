class Car:
    TANK_SIZE = 15
    MPG = 30

    __slots__ = ['__vin', '__make', '__model', '__year', '__mileage', '__fuel']
    def __init__(self, vin, make, model, year, mileage=0, fuel=0):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__fuel = fuel

    def __repr__(self):
        return "Car:" \
            + "\n VIN=" + str(self.__vin) \
            + "\n Make=" + self.__make \
            + "\n Model=" + self.__model \
            + "\n Year=" + str(self.__year) \
            + "\n Mileage=" + str(self.__mileage) \
            + "\n Fuel=" + str(self.__fuel) \
            
    def __str__(self):
        return "Car={VIN=" + self.__vin + ", Make=" + self.__make + ", Model="+ self.__model \
            + ", Year=" + self.__year + ", Mileage=" + self.__mileage + ", Fuel=", self.__fuel,"}" \
            
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__vin == other.__vin
    
    def __lt__(self, other):
        return self.__vin < other.__vin
    
    def __hash__(self):
        return hash(self.__vin)

    def print_car(self):
        print("Car={VIN=", self.__vin, ", Make=", self.__make, ", Model=", self.__model, ", Year=", self.__year, ", Mileage=", self.__mileage, ", Fuel=", self.__fuel,"}" ,sep="")

    def filler_up(self, gallons):
        self.__fuel += gallons
        if self.__fuel > Car.TANK_SIZE:
            self.__fuel = Car.TANK_SIZE

    def drive(self, distance):
        fuel_taken = distance/Car.MPG
        mileage = distance
        if fuel_taken > self.__fuel:
            fuel_taken = self.__fuel
            mileage = fuel_taken*Car.MPG
        self.__mileage += mileage
        self.__fuel -= fuel_taken

