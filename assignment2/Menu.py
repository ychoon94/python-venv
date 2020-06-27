# The controller modules for every function and object creations
# happens in the main program.

from Vehicle import *
from Person import *
from Hash import *
from Menu import *
from os import system, name
import time


# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def pause():
    try:
        input("Press Enter to continue...")
    except SyntaxError:
        pass


def title():
    clear()
    print("__________________________________________________________")
    print("|  Welcome to JPJ Vehicle Ownership Registration System. |")
    this_is_a_dashing_line()


def showMenu():
    title()
    print("Main Menu")
    this_is_a_dashing_line()
    print("Please choose a task to perform: ")
    print("1. Register new vehicle ownership")
    print("2. Transfer vehicle ownership")
    print("3. Search vehicle ownership")
    print("4. Exit System")


# error checking function for name
def ECforName(value):
    value = value.upper()
    counter = 0
    if not len(value) <= 4:
        for i in range(len(value)):
            if (ord(value[i]) >= 65 and ord(value[i]) <= 90) \
               or ord(value[i]) == 32:
                pass
            else:
                counter += 1
    else:
        print("\nInput too short.\nPlease try again.\n")
        return False

    if counter > 0:
        print("\nInput contain non-alphabet.\nPlease try again.\n")
        return False
    else:
        return True


# error checking function for IC
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
        print("\nStructure is wrong.\nPlease try again.\n")
        return False

    if counter > 0:
        print("\nInput contains symbols.\nPlease try again.\n")
        return False
    else:
        return True


# error checking function for address
def ECforAddress(value):
    value = value.upper()
    counter = 0
    if not len(value) <= 4:
        for i in range(len(value)):
            if (ord(value[i]) >= 65 and ord(value[i]) <= 90) \
               or (ord(value[i]) >= 48 and ord(value[i]) <= 57) \
               or ord(value[i]) == 32:
                pass
            else:
                counter += 1
    else:
        print("\nInput too short.\nPlease try again.\n")
        return False

    if counter > 0:
        print("\nInput contain non-alphanumberic.\nPlease try again.\n")
        return False
    else:
        return True


# error checking function for vehicle type
def ECforVType(value):
    counter = 0
    if len(value) == 1:
        for i in range(len(value)):
            if (ord(value[i]) >= 49 and ord(value[i]) <= 52):
                pass
            else:
                counter += 1
    else:
        print("\nPlease enter choice from 1 to 4.\nPlease try again.\n")
        return False

    if counter > 0:
        print("\nPlease enter choice from 1 to 4.\nPlease try again.\n")
        return False
    else:
        return True


# error checking function for vehicle model
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
        print("\nModel name too short to recognize.\nPlease try again.\n")
        return False

    if counter > 0:
        print("\nInput contains symbols.\nPlease try again.\n")
        return False
    else:
        return True


# error checking function for vehicle colour
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
        print("\nInput too short.\nPlease try again.\n")
        return False

    if counter > 0:
        print("\nInput contain non-alphabet.\nPlease try again.\n")
        return False
    else:
        return True


# error checking functions for engine value
def ECforEngine(value):
    counter = 0
    if len(value) <= 4 and len(value) > 0:
        for i in range(len(value)):
            if ord(value[i]) == 46 or \
             (ord(value[i]) >= 48 and ord(value[i]) <= 57):
                pass
            else:
                counter += 1
    else:
        print("\nInput too short.\nPlease try again.\n")
        return False

    if counter > 0:
        print("\nInput contains symbols or alphabet.\nPlease try again.\n")
        return False
    else:
        return True


def newRegistration(hashO, hashRV):
    condition = True
    while True:
        this_is_a_line()
        title()
        print("Register new vehicle ownership")
        this_is_a_dashing_line()
        print("Please choose an owner type before proceed: ")
        print("1. New Owner")
        print("2. Existing Owner")
        print("3. Return to previous menu")
        choice = input("Choice: ")
        this_is_a_line()
        if choice == "1":
            clear()
            condition = True
            while condition:
                title()
                print("Register New Vehicle")
                print("New owner option is selected.")
                this_is_a_line()
                print("Please fill in owner info below.\n")
                while condition:  # pitstop for looping, so user don't
                                  # have to retype
                    ic = input("IC(eg. yymmdd-ss-nnnn)/Passport: ")
                    if isinstance(hashO.searchKey(ic), Person):
                        print("This IC/Passport belongs to existing"
                              " vehicle owner.")
                        print("Please go to existing vehicle owner"
                              " section.")
                        condition = False
                        break
                    else:
                        if ECforIC(ic):
                            break
                        else:
                            continue
                if condition is False:
                    pause()
                    break
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
                print("Please fill in the vehicle info below.\n")
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
                                  vehicleOwner):
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
                pause()
                clear()
                break
        elif choice == "2":
            clear()
            condition = True
            while condition:
                title()
                print("Register New Vehicle")
                print("Existing owner option is selected.")
                this_is_a_dashing_line()
                ic = input("Please insert existing owner IC/Passport:")
                if ECforIC(ic):
                    pass
                else:
                    time.sleep(2.5)
                    continue
                if isinstance(hashO.searchKey(ic), Person):
                    owner = hashO.searchKey(ic)
                    this_is_a_line()
                    condition = True
                    print("Add new vehicle")
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
                                      vehicleOwner):
                            print("This vehicle register number has been"
                                  " registered before.")
                            print("Please insert a new vehicle register"
                                  " number to check for availability.")
                            pause()
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
                    pause()
                    break
                else:
                    pause()
                    break
        elif choice == "3":
            return True
        else:
            print("\nInvalid input. Please try again.\n")
            time.sleep(3)
            continue


def ownershipTransfer(hashO, hashRV):
    condition = True
    while condition:
        title()
        print("Transfer vehicle ownership")
        this_is_a_dashing_line()
        print("Please choose an owner type before proceed: ")
        print("1. New Owner")
        print("2. Existing Owner")
        print("3. Return to previous menu")
        choice2 = input("Choice: ")
        if choice2 == "1":
            clear()
            while condition:
                title()
                print("Transfer vehicle ownership")
                print("New owner option is selected.")
                this_is_a_line()
                print("Please fill in owner info below.\n")
                while condition:  # pitstop for looping, so user don't
                                  # have to retype
                    ic = input("IC(eg. yymmdd-ss-nnnn)/Passport: ")
                    if isinstance(hashO.searchKey(ic), Person):
                        print("This IC/Passport belongs to existing"
                              " vehicle owner.")
                        print("Please go to existing vehicle owner"
                              " section.")
                        condition = False
                        break
                    else:
                        if ECforIC(ic):
                            break
                        else:
                            continue
                if condition is False:
                    pause()
                    break
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
                break
            while condition:
                this_is_a_line()
                print("Please enter the registration number of the"
                      " vehicle.")
                regNum = input("Registration Number: ")
                existingOwner = hashRV.searchKey(regNum)
                if existingOwner != 0:
                    if len(existingOwner.ownedVehicle) is 1:
                        existingOwner.transferVehicle(existingOwner.ownedVehicle[0],
                                                      owner)
                        hashRV.searchReplace(regNum, owner)
                        print("\nTransfer Ownership successful.\n")
                        pause()
                        return 0
                    elif len(existingOwner.ownedVehicle) is not 0:
                        for i in range(len(existingOwner.ownedVehicle)):
                            if existingOwner.ownedVehicle[i].getRegNum() == regNum:
                                existingOwner.transferVehicle(existingOwner.ownedVehicle[i],
                                                              owner)
                                hashRV.searchReplace(regNum, owner)
                                print("\nTransfer Ownership successful.\n")
                                pause()
                                return 0

                    else:
                        print("No vehicle detected.\n")
                        pause()
                        return 0

        elif choice2 == "2":
            clear()
            condition = True
            while condition:
                title()
                print("Transfer vehicle ownership")
                print("Existing owner option is selected.")
                this_is_a_dashing_line()
                ic = input("Please insert existing owner IC/Passport:")
                if isinstance(hashO.searchKey(ic), Person):
                    if ECforIC(ic):
                        break
                    else:
                        continue
                else:
                    print("This IC/Passport did not belongs to existing"
                          " vehicle owner.")
                    print("Please go to new vehicle owner"
                          " section.")
                    condition = False
            if condition is False:
                time.sleep(2.5)
                break

            while condition:
                this_is_a_line()
                print("Please enter the registration number of the"
                      " vehicle.")
                regNum = input("Registration Number: ")
                owner = hashO.searchKey(ic)
                existingOwner = hashRV.searchKey(regNum)
                if existingOwner != 0:
                    if len(existingOwner.ownedVehicle) is 1:
                        existingOwner.transferVehicle(existingOwner.ownedVehicle[0],
                                                      owner)
                        hashRV.searchReplace(regNum, owner)
                        print("\nTransfer Ownership successful.\n")
                        pause()
                        return 0
                    elif len(existingOwner.ownedVehicle) is not 0:
                        for i in range(len(existingOwner.ownedVehicle)):
                            if existingOwner.ownedVehicle[i].getRegNum() == regNum:
                                existingOwner.transferVehicle(existingOwner.ownedVehicle[i],
                                                              owner)
                                hashRV.searchReplace(regNum, owner)
                                print("\nTransfer Ownership successful.\n")
                                pause()
                                return 0

                    else:
                        print("No vehicle detected.\n")
                        time.sleep(2.5)
                        return 0

        elif choice2 == "3":
            condition = False
            break
        else:
            print("Invalid input. Please try again.\n")
            time.sleep(2.5)
            continue


def searchOwnerInfo(hashO, hashRV):
    title()
    print("Search vehicle ownership")
    this_is_a_dashing_line()
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
        print("\nVehicle Registration Number not found.\n")
    pause()


def this_is_a_dashing_line():
    print("----------------------------------------------------------")
    print("\n")


def this_is_a_line():
    print("__________________________________________________________")
    print("\n")


def main(hashO, hashRV):
    while True:
        clear()
        showMenu()
        choice = input("Choice: ")

        if choice == "1":
            clear()
            newRegistration(hashO, hashRV)
        elif choice == "2":
            clear()
            ownershipTransfer(hashO, hashRV)
        elif choice == "3":
            clear()
            searchOwnerInfo(hashO, hashRV)
        elif choice == "4":
            title()
            print("Thank you for using JPJ Vehicle Ownership Registration"
                  " System.\n")
            return False
        else:
            print("\nChoose option 1-4 only.\n")
            pause()
