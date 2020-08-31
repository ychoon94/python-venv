class Person:
    def __init__(self, name, ic, address):
        self.__name = name
        self.__ic = ic
        self.__address = address.split(",")
        self.__ownedVehicle = []

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getIC(self):
        return self.__ic

    def setIC(self, newIC):
        self.__ic = newIC

    def getAddress(self):
        return self.__address  # it is a list

    def setAddress(self, newAddress):
        if (type(newAddress) == list):
            self.__address = newAddress
        else:
            self.__address = newAddress.split(",")

    def addVehicle(self, Vehicle):
        self.__ownedVehicle.append(Vehicle)
        Vehicle.owner = self

    def removeVehicle(self, Vehicle):
        self.__ownedVehicle.remove(Vehicle)
        Vehicle.owner = 0


class Vehicle:
    def __init__(self, maker, model, colour, engineCapacity,regNum):
        self.maker = maker
        self.model = model
        self.colour = colour
        self.engineCapacity = engineCapacity
        self.regNum = regNum
        self.owner = 0
