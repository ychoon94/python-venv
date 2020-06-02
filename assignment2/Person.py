from Vehicle import *


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


class vehicleOwner(Person):
    OWNER, NON_OWNER = range(2)

    def __init__(self, *args, **kwargs):
        self.ownedVehicle = []
        super(vehicleOwner, self).__init__(*args, **kwargs)
        self.ownerType = None
        self._checkOwnerType()

    def _checkOwnerType(self):
        if len(self.ownedVehicle) is 0:
            self.ownerType = vehicleOwner.NON_OWNER
        else:
            self.ownerType = vehicleOwner.OWNER

    def addVehicle(self, registeredVehicle):
        self.ownedVehicle.append(registeredVehicle)
        registeredVehicle.addOwner(self)
        if len(self.ownedVehicle) > 0:
            self.ownerType = vehicleOwner.OWNER
        else:
            self.ownerType = vehicleOwner.NON_OWNER

    def removeVehicle(self, registeredVehicle):
        self.ownedVehicle.remove(registeredVehicle)
        registeredVehicle.removeOwner(self)
        if len(self.ownedVehicle) is 0:
            self.ownerType = vehicleOwner.NON_OWNER
        else:
            self.ownerType = vehicleOwner.OWNER

    def transferVehicle(self, registeredVehicle, new_owner):
        self.removeVehicle(registeredVehicle)
        new_owner.addVehicle(registeredVehicle)
