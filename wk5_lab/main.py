from Hash import Hash


def menu():
    print("Main Menu (Hash Table) ")
    print("______________________ ")
    print("1. Linear Probing ")
    print("2. Double Hashing ")
    print("3. Hybrid (Combination of option 2 and 3)")
    print("\n")
    choice = int(input("Choose an option: "))
    return choice


def userInput():
    userInput = input("Insert the number between 1-100: ")
    return userInput


if __name__ == "__main__":
    h = Hash(10)
    counter = 0
    choice = menu()
    if (choice == 1):
        while counter < 7:
            num = int(userInput())
            h.linearProbing(num, num, 1)
            h.displayHash()
            counter += 1
    elif (choice == 2):
        while counter < 7:
            h.doubleHashing(int(userInput()))
            h.displayHash()
            counter += 1
    elif (choice == 3):
        while counter < 7:
            h.hybridHashLinear(int(userInput()))
            h.displayHash()
            counter += 1
