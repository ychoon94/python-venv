from Vehicle import *
from Person import *
from HashRV import *
from HashO import *
from Menu import *
from os import system, name


def showMenu():
    system('clear')
    print("__________________________________________________________")
    print("|  Welcome to JPJ Vehicle Ownership Registration System. |")
    this_is_a_dashing_line()
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
        choice = input("Choice: ")
        this_is_a_line()
        system('clear')
        if choice == "1":
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
                system("clear")
                break
        elif choice == "2":
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
        elif choice == "3":
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
        system("clear")
        if choice2 == "1":
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
        elif choice2 == "2":
            ic = input("Please insert existing owner IC/Passport:")
            if isinstance(hashO.searchKey(ic), Person):
                owner = hash0.searchKey(ic)
                inputVehicleDetail(owner, vehicle, hashRV)
            break
        elif choice2 == "3":
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
        this_is_a_dashing_line()
        if len(owner.ownedVehicle) == 1:
            print("Maker: {}" .format(owner.ownedVehicle[0].maker))
            print("Model: {}" .format(owner.ownedVehicle[0].model))
            print("Colour: {}" .format(owner.ownedVehicle[0].colour))
            print("Engine Capacity: {}" .format(owner.ownedVehicle[0].engineCapacity))
            print("Vehicle Registration Number: {}" .format(owner.ownedVehicle[0].getRegNum()))
            if owner.ownedVehicle[0].vehicleType == 0:
                print("Vehicle Type: {}" .format("CAR"))
            elif owner.ownedVehicle[0].vehicleType == 1:
                print("Vehicle Type: {}" .format("MOTORCYCLE"))
            elif owner.ownedVehicle[0].vehicleType == 2:
                print("Vehicle Type: {}" .format("TRUCK"))
            elif owner.ownedVehicle[0].vehicleType == 3:
                print("Vehicle Type: {}" .format("BUS"))
        elif len(owner.ownedVehicle) > 1:
            for i in range(len(owner.ownedVehicle)):
                print("Maker: {}" .format(owner.ownedVehicle[i].maker))
                print("Model: {}" .format(owner.ownedVehicle[i].model))
                print("Colour: {}" .format(owner.ownedVehicle[i].colour))
                print("Engine Capacity: {}" .format(owner.ownedVehicle[i].engineCapacity))
                print("Vehicle Registration Number: {}" .format(owner.ownedVehicle[i].getRegNum()))
                if owner.ownedVehicle[i].vehicleType == 0:
                    print("Vehicle Type: {}" .format("CAR"))
                elif owner.ownedVehicle[i].vehicleType == 1:
                    print("Vehicle Type: {}" .format("MOTORCYCLE"))
                elif owner.ownedVehicle[i].vehicleType == 2:
                    print("Vehicle Type: {}" .format("TRUCK"))
                elif owner.ownedVehicle[i].vehicleType == 3:
                    print("Vehicle Type: {}" .format("BUS"))

                this_is_a_line()
    else:
        print("Vehicle Registration Number not found.\n")
    try:
        input("Press Enter to continue...")
    except SyntaxError:
        pass

def this_is_a_dashing_line():
    print("----------------------------------------------------------")
    print("\n")


def this_is_a_line():
    print("__________________________________________________________")
    print("\n")


def main(hashO, hashRV):
    while True:
        system("clear")
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
