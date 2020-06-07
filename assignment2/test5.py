from Modules.Vehicle import *
from Modules.Person import *
from Modules.HashRV import *
from Modules.HashO import *
from Modules.Menu import *
from os import system, name


class Vehicle:
    def __init__(self, maker, model, colour, engineCapacity):
        self.maker = maker
        self.model = model
        self.colour = colour
        self.engineCapacity = engineCapacity


class registeredVehicle(Vehicle):
    CAR, MOTORCYCLE, TRUCK, BUS = range(4)

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
            print("Insert successfully.\n")
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
                    notFound = False
                    return 0
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
                    notFound = False
                    return 0
            elif counter > 3:
                for i in range(1, len(self.table[index2])):
                    if self.table[index2]:   # check if the list is empty
                        try:
                            print("Search executed at {} index. Try {}"
                                  .format(index2, counter+i-1))
                            position = self.table[index2][i][0].index(key)
                            notFound = False
                            print("Value found")
                            return self.table[index2][i][1]
                        except ValueError:
                            if (i+1) != len(self.table[index2]):
                                continue
                            else:
                                print("{} is not found in the system."
                                      .format(key))
                                notFound = False
                                return 0
                    else:
                        print("{} is not found in the system." .format(key))
                        return 0
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
                    notFound = False
                    return 0
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
                    notFound = False
                    return 0
            elif counter > 3:
                for i in range(1, len(self.table[index2])):
                    if self.table[index2]:   # check if the list is empty
                        try:
                            print("Search executed at {} index. Try {}"
                                  .format(index2, counter+i-1))
                            position = self.table[index2][i][0].index(key)
                            notFound = False
                            print("Value found")
                            return self.table[index2][i][1]
                        except ValueError:
                            if (i+1) != len(self.table[index2]):
                                continue
                            else:
                                print("{} is not found in the system."
                                      .format(key))
                                notFound = False
                                return 0
                    else:
                        print("{} is not found in the system." .format(key))
                        return 0
                    break


def showMenu():
    print("Welcome to JPJ Vehicle Ownership Registration System.")
    this_is_a_line()
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
    if not (len(value) <= 5 or len(value) > 14):
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
    if not len(value) < 1:
        for i in range(len(value)):
            if (ord(value[i]) >= 48 and ord(value[i]) <= 57) or \
               (ord(value[i]) >= 65 and ord(value[i]) <= 90) or \
               ord(value[i]) == 32:
                pass
            else:
                counter += 1
    else:
        print("Model name too short to recognize.\nPlease try again.")
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
            if ord(value[i]) == 46 or \
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


def newRegistration(hashO, hashRV):
    condition = True
    while condition:
        this_is_a_line()
        print("Is this a new owner vehicle registration or"
              " existing owner vehicle registration?")
        print("For new owner, insert '1'.")
        print("For existing owner, insert '2'.")
        print("To leave insert, '3'.")
        choice = int(input("Choice: "))
        this_is_a_line()
        if choice == 1:
            while condition:
                condition = True
                print("Please fill in owner info below.")
                while condition:  # pitstop for looping, so user don't
                                  # have to retype
                    ic = input("IC(eg. yymmdd-ss-nnnn)/Passport: ")
                    if isinstance(hashO.searchKey(ic), Person):
                        print("This IC/Passport belongs to existing"
                              " vehicle owner.")
                        print("Please go to existing vehicle owner"
                              " section.")
                        break
                    else:
                        if ECforIC(ic):
                            break
                        else:
                            continue
                while condition:  # pitstop for looping, so user don't
                                  # have to retype
                    name = input("Name: ")
                    if ECforName(name):
                        break
                    else:
                        continue
                while condition:  # pitstop for looping, so user don't
                                  # have to retype
                    address = input("Address(without symbol): ")
                    if ECforAddress(address):
                        break
                    else:
                        continue
                owner = vehicleOwner(name, ic, address)
                hashO.hybridHashChaining(owner.getIC(), owner)
                this_is_a_line()
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
                    if isinstance(hashRV.searchKey(regNum),
                                  registeredVehicle):
                        print("This vehicle register number has been"
                              " registered before.")
                        print("Please insert a new vehicle register"
                              " number to check for availability.")
                        continue
                    else:
                        if ECforAddress(regNum):
                            break
                        else:
                            continue
                while condition:  # implement vehicle info
                    maker = input("Vehicle Maker: ")
                    if ECforModel(maker):
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
                if vType == "1":
                    vehicle = registeredVehicle(registeredVehicle.CAR,
                                                regNum, maker,
                                                model, colour, engine)
                elif vType == "2":
                    vehicle = registeredVehicle(registeredVehicle.MOTORCYCLE,
                                                regNum, maker, model,
                                                colour, engine)
                elif vType == "3":
                    vehicle = registeredVehicle(registeredVehicle.TRUCK,
                                                regNum, maker, model,
                                                colour, engine)
                elif vType == "4":
                    vehicle = registeredVehicle(registeredVehicle.BUS,
                                                regNum, maker, model,
                                                colour, engine)
                owner.addVehicle(vehicle)
                if len(owner.ownedVehicle) < 1:
                    hashRV.hybridHashChaining(owner.ownedVehicle[0].getRegNum(), owner)
                else:
                    hashRV.hybridHashChaining(owner.ownedVehicle[-1].getRegNum(),
                                              owner)
                break
        elif choice == 2:
            condition = True
            while condition:
                ic = input("Please insert existing owner IC/Passport:")
                if isinstance(hashO.searchKey(ic), Person):
                    owner = hashO.searchKey(ic)
                    this_is_a_line()
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
                        if isinstance(hashRV.searchKey(regNum),
                                      registeredVehicle):
                            print("This vehicle register number has been"
                                  " registered before.")
                            print("Please insert a new vehicle register"
                                  " number to check for availability.")
                            continue
                        else:
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
                    if vType == "1":
                        vehicle = registeredVehicle(registeredVehicle.CAR,
                                                    regNum, maker,
                                                    model, colour, engine)
                    elif vType == "2":
                        vehicle = registeredVehicle(registeredVehicle.MOTORCYCLE,
                                                    regNum, maker, model,
                                                    colour, engine)
                    elif vType == "3":
                        vehicle = registeredVehicle(registeredVehicle.TRUCK,
                                                    regNum, maker, model,
                                                    colour, engine)
                    elif vType == "4":
                        vehicle = registeredVehicle(registeredVehicle.BUS,
                                                    regNum, maker, model,
                                                    colour, engine)
                    owner.addVehicle(vehicle)
                    if len(owner.ownedVehicle) < 1:
                        hashRV.hybridHashChaining(owner.ownedVehicle[0].getRegNum(), owner)
                    else:
                        hashRV.hybridHashChaining(owner.ownedVehicle[-1].getRegNum(),
                                                  owner)
                    break
                break
        elif choice == 3:
            return True
        else:
            print("Invalid input. Please try again.\n")
            continue


def ownershipTransfer(hashO, hashRV):
    condition = True
    while condition:
        print("Is the new owner of the vehicle a non-registered owner or"
              " a registered owner?")
        print("For new owner, insert '1'.")
        print("For existing owner, insert '2'.")
        print("To leave insert, '3'.")
        choice2 = input("Choice: ")
        if choice2 == 1:
            while condition:
                inputOwnerDetail(owner, hashO)
                break
            while condition:
                this_is_a_line()
                print("Please enter the registration number of the"
                      " vehicle.")
                regNum = input("Registration Number: ")
                existingOwner = hashRV.searchKey(regNum)
                if len(existingOwner.ownedVehicle) is 1:
                    existingOwner.transferVehicle(existingOwner.
                                                  ownedVehicle[0],
                                                  owner)
                elif len(existingOwner.ownedVehicle) is not 0:
                    for i in range(len(existingOwner.ownedVehicle)):
                        if existingOwner.ownedVehicle[i].getRegNum()\
                                == regNum:
                            existingOwner.transferVehicle(existingOwner.
                                                          ownedVehicle[i],
                                                          owner)
                        else:
                            continue
                else:
                    break
        elif choice2 == 2:
            ic = input("Please insert existing owner IC/Passport:")
            if isinstance(hashO.searchKey(ic), Person):
                owner = hash0.searchKey(ic)
                inputVehicleDetail(owner, vehicle, hashRV)
            break
        elif choice2 == 3:
            condition = False
            break
        else:
            print("Invalid input. Please try again.\n")
            continue


def searchOwnerInfo(hashO, hashRV):
    print("Please enter the following to search.")
    regNum = input("Vehicle Registration Number: ")
    owner = hashRV.searchKey(regNum)
    if owner != 0:
        print("Name: {}" .format(owner.getName()))
        print("IC/Passport: {}" .format(owner.getIC()))
        print("Address: {}" .format(owner.getAddress()))
        this_is_a_line()
        print("Vehicle Detail for {} vehicle below." .format(len(owner.ownedVehicle)))
        if len(owner.ownedVehicle) == 1:
            print("Maker: {}" .format(owner.ownedVehicle[0].maker))
            print("Model: {}" .format(owner.ownedVehicle[0].model))
            print("Colour: {}" .format(owner.ownedVehicle[0].colour))
            print("Engine Capacity: {}" .format(owner.ownedVehicle[0].engineCapacity))
            print("Vehicle Registration Number: {}" .format(owner.ownedVehicle[0].getRegNum()))
            print("Vehicle Type: {}" .format(owner.ownedVehicle[0].vehicleType))
        elif len(owner.ownedVehicle) > 1:
            for i in range(len(owner.ownedVehicle)):
                print("Maker: {}" .format(owner.ownedVehicle[i].maker))
                print("Model: {}" .format(owner.ownedVehicle[i].model))
                print("Colour: {}" .format(owner.ownedVehicle[i].colour))
                print("Engine Capacity: {}" .format(owner.ownedVehicle[i].engineCapacity))
                print("Vehicle Registration Number: {}" .format(owner.ownedVehicle[i].getRegNum()))
                print("Vehicle Type: {}" .format(owner.ownedVehicle[i].vehicleType))
    else:
        print("Vehicle Registration Number not found.\n")


def this_is_a_line():
    print("\n")
    print("__________________________________________________________________")
    print("\n")


def main(hashO, hashRV):
    while True:

        showMenu()
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Enter number only.\n")

        if choice == 1:
            system('clear')
            newRegistration(hashO, hashRV)
        elif choice == 2:
            system('clear')
            ownershipTransfer(hashO, hashRV)
        elif choice == 3:
            system('clear')
            searchOwnerInfo(hashO, hashRV)
        elif choice == 4:
            system('clear')
            print("Thank you for using JPJ Vehicle Ownership Registration"
                  " System.\n")
            return False
        else:
            print("Choose option 1-4 only.\n")


if __name__ == "__main__":
    hashO = HashO(30)
    hashRV = HashRV(30)
    main(hashO, hashRV)
