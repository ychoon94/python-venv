from Vehicle import *
from Person import *
from HashRV import *
from HashO import *


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


class HashRV:

    def __init__(self, size):
        self.key = None
        self.tableSize = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def hashFunction(self, key):
        sumOfChar = 0
        for i in range(len(key)):
            sumOfChar += ord(key[i])
            return sumOfChar % self.tableSize

    def hash2(self, key):
        sumOfChar = 0
        for i in range(len(key)):
            sumOfChar += ord(key[i])
            return 7 - (sumOfChar % 7)

    def hybridHashChaining(self, key, value):
        index = self.hashFunction(key)
        if not self.table[index]:
            self.table[index].append([key, value])
            print("Insert successfully.")
        else:
            hash2 = self.hash2(key)
            notFound = True
            counter = 1
            while notFound:
                index2 = (index + counter * hash2) % self.tableSize
                if not self.table[index2]:
                    self.table[index2].append([key, value])
                    print("Double Hashing execute attempt {}: h({}) + {}: {}- "
                          "pass(insert successfully)"
                          .format(counter, key, counter, index2))
                    notFound = False
                else:
                    print("Double Hashing execute attempt {}: h({}) + {}: {}-"
                          "fail"
                          .format(counter, key, counter, index2))
                    counter += 1
                    if counter > 3:
                        break
            if notFound:
                counter = 1
                print("Chaining execute attempt {}: h({}) + {}: {}- "
                      "pass(insert successfully)"
                      .format(counter, key, counter, index2))
                self.table[index2].append([key, value])

    def displayHash(self):
        for i in range(self.tableSize):
            if self.table[i] is None:
                continue
            else:
                print(i, end=' ')
                print(" --> {}" .format(self.table[i]))
        print('\n')

    def searchKey(self, key):  # need implementation
        notFound = True
        counter = 0
        index = self.hashFunction(key)
        while notFound:
            # if not empty and 1st loop then perform search
            if counter is 0:
                if self.table[index]:  # check if the list is empty
                    try:
                        print("Search executed at {} index. Try {}"
                              .format(index, counter))
                        position = self.table[index][0].index(key)
                        notFound = False
                        return self.table[index][0][1]
                    except ValueError:
                        notFound = True
                        counter += 1
                else:
                    print("{} is not found in the system." .format(key))
                    break
            # if not found in 1st loop, perform doubleHashing and search
            elif counter > 0 and counter <= 3:
                hash2 = self.hash2(key)
                index2 = (index + counter * hash2) % self.tableSize
                if self.table[index2]:   # check if the list is empty
                    try:
                        print("Search executed at {} index. Try {}"
                              .format(index2, counter))
                        position = self.table[index2][0][0].index(key)
                        notFound = False
                        return self.table[index2][0][1]
                    except ValueError:
                        notFound = True
                        counter += 1
                else:
                    print("{} is not found in the system." .format(key))
                    break
            elif counter > 3:
                for i in range(len(self.table[index2])):
                    if self.table[index2]:   # check if the list is empty
                        try:
                            print("Search executed at {} index. Try {}"
                                  .format(index2, counter))
                            position = self.table[index2][i][0].index(key)
                            notFound = False
                            return self.table[index2][i][1]
                        except ValueError:
                            if i is not len(self.table[index2]):
                                continue
                            else:
                                print("{} is not found in the system."
                                      .format(key))
                                break
                    else:
                        print("{} is not found in the system." .format(key))
                        break
                    break


class HashO:

    def __init__(self, size):
        self.key = None
        self.tableSize = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def hashFunction(self, key):
        sumOfChar = 0
        for i in range(len(key)):
            sumOfChar += ord(key[i])
            return sumOfChar % self.tableSize

    def hash2(self, key):
        sumOfChar = 0
        for i in range(len(key)):
            sumOfChar += ord(key[i])
            return 7 - (sumOfChar % 7)

    def hybridHashChaining(self, key, value):
        index = self.hashFunction(key)
        if not self.table[index]:
            self.table[index].append([key, value])
            print("Insert successfully.")
        else:
            hash2 = self.hash2(key)
            notFound = True
            counter = 1
            while notFound:
                index2 = (index + counter * hash2) % self.tableSize
                if not self.table[index2]:
                    self.table[index2].append([key, value])
                    print("Double Hashing execute attempt {}: h({}) + {}: {}- "
                          "pass(insert successfully)"
                          .format(counter, key, counter, index2))
                    notFound = False
                else:
                    print("Double Hashing execute attempt {}: h({}) + {}: {}-"
                          "fail"
                          .format(counter, key, counter, index2))
                    counter += 1
                    if counter > 3:
                        break
            if notFound:
                counter = 1
                print("Chaining execute attempt {}: h({}) + {}: {}- "
                      "pass(insert successfully)"
                      .format(counter, key, counter, index2))
                self.table[index2].append([key, value])

    def displayHash(self):
        for i in range(self.tableSize):
            if self.table[i] is None:
                continue
            else:
                print(i, end=' ')
                print(" --> {}" .format(self.table[i]))
        print('\n')

    def searchKey(self, key):  # need implementation
        notFound = True
        counter = 0
        index = self.hashFunction(key)
        while notFound:
            # if not empty and 1st loop then perform search
            if counter is 0:
                if self.table[index]:  # check if the list is empty
                    try:
                        print("Search executed at {} index. Try {}"
                              .format(index, counter))
                        position = self.table[index][0].index(key)
                        notFound = False
                        return self.table[index][0][1]
                    except ValueError:
                        notFound = True
                        counter += 1
                else:
                    print("{} is not found in the system." .format(key))
                    break
            # if not found in 1st loop, perform doubleHashing and search
            elif counter > 0 and counter <= 3:
                hash2 = self.hash2(key)
                index2 = (index + counter * hash2) % self.tableSize
                if self.table[index2]:   # check if the list is empty
                    try:
                        print("Search executed at {} index. Try {}"
                              .format(index2, counter))
                        position = self.table[index2][0][0].index(key)
                        notFound = False
                        return self.table[index2][0][1]
                    except ValueError:
                        notFound = True
                        counter += 1
                else:
                    print("{} is not found in the system." .format(key))
                    break
            elif counter > 3:
                for i in range(len(self.table[index2])):
                    if self.table[index2]:   # check if the list is empty
                        try:
                            print("Search executed at {} index. Try {}"
                                  .format(index2, counter))
                            position = self.table[index2][i][0].index(key)
                            notFound = False
                            return self.table[index2][i][1]
                        except ValueError:
                            if i is not len(self.table[index2]):
                                continue
                            else:
                                print("{} is not found in the system."
                                      .format(key))
                                break
                    else:
                        print("{} is not found in the system." .format(key))
                        break
                    break


def showMenu():
    print("Welcome to JPJ Vehicle Ownership Registration System.")
    print("_____________________________________________________")
    print("Please choose a task to perform: ")
    print("1. Register new vehicle ownership")
    print("2. Transfer vehicle ownership")
    print("3. Search vehicle ownership")
    print("4. Exit System")


def ECforName(value):
    value = value.upper()
    counter = 0
    if not len(value) <= 5:
        for i in range(len(value)):
            if (ord(value[i]) >= 65 and ord(value[i]) <= 90) \
               or ord(value[i]) == 32:
                pass
            else:
                counter += 1
    else:
        print("Input too short.\nPlease try again.")
        return False

    if counter > 0:
        print("Input contain non-alphabet.\nPlease try again.")
        return False
    else:
        return True


def ECforIC(value):
    value = value.upper()
    counter = 0
    if not len(value) <= 5:
        for i in range(len(value)):
            if (ord(value[i]) >= 65 and ord(value[i]) <= 90) or \
               (ord(value[i]) >= 48 and ord(value[i]) <= 57) or \
               ord(value[i]) == 45:
                pass
            else:
                counter += 1
    else:
        print("Input too short.\nPlease try again.")
        return False

    if counter > 0:
        print("Input contains symbols.\nPlease try again.")
        return False
    else:
        return True


def ECforAddress(value):
    value = value.upper()
    counter = 0
    if not len(value) <= 5:
        for i in range(len(value)):
            if (ord(value[i]) >= 65 and ord(value[i]) <= 90) \
               or (ord(value[i]) >= 48 and ord(value[i]) <= 57) \
               or ord(value[i]) == 32:
                pass
            else:
                counter += 1
    else:
        print("Input too short.\nPlease try again.")
        return False

    if counter > 0:
        print("Input contain non-alphabet.\nPlease try again.")
        return False
    else:
        return True


def ECforVType(value):
    counter = 0
    if len(value) == 1:
        for i in range(len(value)):
            if (ord(value[i]) >= 49 and ord(value[i]) <= 52):
                pass
            else:
                counter += 1
    else:
        print("Please enter choice from 1 to 4.\nPlease try again.")
        return False

    if counter > 0:
        print("Please enter choice from 1 to 4.\nPlease try again.")
        return False
    else:
        return True


def ECforModel(value):
    value = value.upper()
    counter = 0
    if len(value) < 1:
        for i in range(len(value)):
            if (ord(value[i]) >= 48 and ord(value[i]) <= 57) or \
               (ord(value[i]) >= 65 and ord(value[i]) <= 90) or \
               ord(value[i]) == 32:
                pass
            else:
                counter += 1
    else:
        print("Input contain non-alphabet.\nPlease try again.")
        return False

    if counter > 0:
        print("Input contains symbols.\nPlease try again.")
        return False
    else:
        return True


def ECforColour(value):
    value = value.upper()
    counter = 0
    if not len(value) < 3:
        for i in range(len(value)):
            if (ord(value[i]) >= 65 and ord(value[i]) <= 90) \
               or ord(value[i]) == 32:
                pass
            else:
                counter += 1
    else:
        print("Input too short.\nPlease try again.")
        return False

    if counter > 0:
        print("Input contain non-alphabet.\nPlease try again.")
        return False
    else:
        return True


def ECforEngine(value):
    counter = 0
    if len(value) <= 4:
        for i in range(len(value)):
            if ord(value) == 46 or \
             (ord(value[i]) >= 48 and ord(value[i]) <= 57):
                pass
            else:
                counter += 1
    else:
        print("Input too long.\nPlease try again.")
        return False

    if counter > 0:
        print("Input contains symbols or alphabet.\nPlease try again.")
        return False
    else:
        return True


def option(choice, owner, vehicle, hashRV, hashO):
    condition = True
    if choice == 1:  # register new vehicle ownership
        print("Please fill in owner info below.")
        while condition:  # pitstop for looping, so user don't have to retype
            name = input("Name: ")
            if ECforName(name):
                break
            else:
                continue
        while condition:  # pitstop for looping, so user don't have to retype
            ic = input("IC(eg. yymmdd-ss-nnnn)/Passport: ")
            if ECforIC(ic):
                break
            else:
                continue
        while condition:  # pitstop for looping, so user don't have to retype
            address = input("Address(without symbol): ")
            if ECforAddress(address):
                break
            else:
                continue
        owner = VehicleOwner(name, ic, address)
        print("______________________________________________________________")
        condition = True
        print("Please fill in the vehicle info below.")
        while condition:
            print("Choose your vehicle type:")
            print("CAR--1 \nMOTORCYCLE--2 \nTRUCK--3 \nVAN--4")
            vType = input("Vehicle Type(Number only): ")
            if ECforVType(vType):
                break
            else:
                continue
        while condition:
            regNum = input("Vehicle Register Number: ")
            if ECforAddress(regNum):
                break
            else:
                continue
        while condition:  # implement vehicle info
            maker = input("Vehicle Maker: ")
            if ECforName(maker):
                break
            else:
                continue
        while condition:
            model = input("Vehicle Model: ")
            if ECforModel(model):
                break
            else:
                continue
        while condition:
            colour = input("Vehicle Colour: ")
            if ECforColour(colour):
                break
            else:
                continue
        while condition:
            engine = input("Engine Capacity: ")
            if ECforEngine(engine):
                break
            else:
                continue
        if vType == 1:
            vehicle = registeredVehicle(registeredVehicle.CAR, regNum, maker,
                                        model, colour, engine)
        elif vType == 2:
            vehicle = registeredVehicle(registeredVehicle.MOTORCYCLE, regNum,
                                        maker, model, colour, engine)
        elif vType == 3:
            vehicle = registeredVehicle(registeredVehicle.TRUCK, regNum,
                                        maker, model, colour, engine)
        elif vType == 4:
            vehicle = registeredVehicle(registeredVehicle.VAN, regNum,
                                        maker, model, colour, engine)
        owner.addVehicle(vehicle)
        if len(owner.ownedVehicle) < 1:
            hashRV.hybridHashChaining(owner.ownedVehicle[0].getRegNum(), owner)
        else:
            hashRV.hybridHashChaining(owner.ownedVehicle[-1].getRegNum(),
                                      owner)

    elif choice == 2:  # Transfer vehicle ownership
        pass
    elif choice == 3:  # Search vehicle ownership, return owner detail
        pass
    elif choice == 4:  # exit system
        pass
    else:  # choice not in range
        pass


def createOwnerObj():
    ownerObjs = []
    for i in range(100):
        ownerObj = 'owner_{}' .format(i)
        ownerObjs.append(ownerObj)
    return ownerObjs


def createVehicleObj():
    vehicleObjs = []
    for i in range(100):
        vehicleObj = 'vehicle_{}' .format(i)
        vehicleObjs.append(vehicleObj)
    return vehicleObjs


if __name__ == "__main__":
    p1 = vehicleOwner("Jane", "987654-07-2345",
                      "8654, Medan bukit Marut 4, Testing 404, 10234,"
                      " BaTe Lopir, P3uyre")
    p2 = vehicleOwner("Mary", "927654-07-2345",
                      "8634, Medan bukit Mirut 4, Testing 104, 10234,"
                      " BaTe Lepir, P3uyre")
    p3 = vehicleOwner("Mary1", "927654-07-2345",
                      "8634, Medan bukit Mirut 4, Testing 104, 10234,"
                      " BaTe Lepir, P3uyre")
    p4 = vehicleOwner("Mary2", "927654-07-2345",
                      "8634, Medan bukit Mirut 4, Testing 104, 10234,"
                      " BaTe Lepir, P3uyre")
    p5 = vehicleOwner("Mary3", "927654-07-2345",
                      "8634, Medan bukit Mirut 4, Testing 104, 10234,"
                      " BaTe Lepir, P3uyre")
    p6 = vehicleOwner("Mary4", "927654-07-2345",
                      "8634, Medan bukit Mirut 4, Testing 104, 10234,"
                      " BaTe Lepir, P3uyre")
    car1 = registeredVehicle(registeredVehicle.CAR, "P1234", "toyota",
                             "camry", "red", "1.5L")

    car2 = registeredVehicle(registeredVehicle.CAR, "P1324", "toyota",
                             "camry", "bloodred", "2.5L")
    car3 = registeredVehicle(registeredVehicle.CAR, "P1423", "toyota",
                             "camry", "shinyred", "1.5L")
    car4 = registeredVehicle(registeredVehicle.CAR, "P4321", "toyota",
                             "camry", "superred", "1.5L")
    car5 = registeredVehicle(registeredVehicle.CAR, "P2134", "toyota",
                             "camry", "redredred", "1.5L")
    car6 = registeredVehicle(registeredVehicle.CAR, "P2143", "toyota",
                             "camry", "redredveryred", "1.5L")
    p1.addVehicle(car1)
#    p1.removeVehicle(car1)
    p2.addVehicle(car2)
    p3.addVehicle(car3)
    p4.addVehicle(car4)
    p5.addVehicle(car5)
    p6.addVehicle(car6)
#    p1.transferVehicle(car1, p2)

    # print(p1.ownedVehicle[0].getRegNum())
#    print(p1.ownerType)
    # print(car1.getRegNum())
    print("______________________________________________")
#    print(p2.ownedVehicle[0].getRegNum())
#    print(car2.getOwner()[0].getName())
    # if len(p1.ownedVehicle) is None:
    #     print("you did it")
    # else:
    #     print("you misunderstood None = 0")
    #     print(len(p1.ownedVehicle))
    h = HashRV(30)
    h.hybridHashChaining(p1.ownedVehicle[0].getRegNum(), p1)
    h.hybridHashChaining(p2.ownedVehicle[0].getRegNum(), p2)
    h.hybridHashChaining(p3.ownedVehicle[0].getRegNum(), p3)
    h.hybridHashChaining(p4.ownedVehicle[0].getRegNum(), p4)
    h.hybridHashChaining(p5.ownedVehicle[0].getRegNum(), p5)
    h.hybridHashChaining(p6.ownedVehicle[0].getRegNum(), p6)
    h.displayHash()
    # print(p6.ownedVehicle[0].getRegNum())
    # obj = h.searchKey(p6.ownedVehicle[0].getRegNum())
    obj = h.searchKey("123333333")
    print("Name: {}" .format(obj.getName()))
    print("IC/Passport: {}" .format(obj.getIC()))
    print("Colour: {}" .format(obj.ownedVehicle[0].colour))
