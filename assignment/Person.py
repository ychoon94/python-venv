from Vehicle import Vehicle


class Person:

    def __init__(self, name, ic, address):
        self.__name = name
        self.__ic = ic
        self.__address = address.split(",")

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


class vehicleOwner(Person, Vehicle):  # function is a subclas for 2 parent
    def __init__(self, name, ic, address, regNum, color, engine, maker, model,
                 vehicleType):
        Person.__init__(self, name, ic, address)
        Vehicle.__init__(self, regNum, color, engine, maker, model,
                         vehicleType)

    def transferOwner(self, other):
        self.setName(other.getName())
        self.setIC(other.getIC())
        self.setAddress(other.getAddress())
# self, regNum, color, engine, maker, model, vehicleType
