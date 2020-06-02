from Person import *


class Vehicle:
    def __init__(self, maker, model, colour, engineCapacity):
        self.maker = maker
        self.model = model
        self.colour = colour
        self.engineCapacity = engineCapacity


class registeredVehicle(Vehicle):
    CAR, MOTORCYCLE, TRUCK, VAN = range(4)

    def __init__(self, vehicleType, regNum, *args, **kwargs):
        self.vehicleType = vehicleType
        self.__regNum = regNum
        self.__owner = []
        super(registeredVehicle, self).__init__(*args, **kwargs)

    def addOwner(self, owner):
        self.__owner.append(owner)

    def removeOwner(self, owner):
        self.__owner.remove(owner)

    def getRegNum(self):
        return self.__regNum

    def getOwner(self):
        return self.__owner
