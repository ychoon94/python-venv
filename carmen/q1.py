class hashTable:
    def __init__(self):
        self.size = 30
        self.arr = [None] * self.size
        self.keyCount = 0
        self.comparisons = 0

    def get_Hash(self,registrationNumber):
        h = 0
        for x in range(len(registrationNumber)):
            h += ord(registrationNumber[x])
        return h % self.size

    def is_hashTableFull(self):
        if self.keyCount == self.size:
            return True
        else:
            return False

    def quadraticProbing(self, registrationNumber, value, index):
        indexFound = False
        limit = 60
        y = 1
        while y <= limit:
            newIndex = index + (y**2)
            newIndex = newIndex % self.size
            if self.arr[newIndex] == 0:
                indexFound = True
                break
            else:
                y += 1
        return indexFound, newIndex


    def insert(self,registrationNumber,value):
        index = self.get_Hash(registrationNumber)
        if self.is_hashTableFull():
             print("Hash Table is Full")
             return False

        isStored = False
        if self.arr[index] is None:
            self.arr[index] = [registrationNumber, value]
            print("Key " + str(registrationNumber) + ','  "Value " + str(value) + ',' "at index " + str(index) + '.')
            isStored = True
            self.keyCount += 1

        else:
            print("Collision has been occured for key " + str(registrationNumber) + " at index " + str(index) + " is finding new index.")
            isStored, index = self.quadraticProbing(registrationNumber, value, index)
            if isStored:
                self.arr[index] = [registrationNumber, value]
                self.keyCount += 1

        return isStored

    def get(self, registrationNumber):
        index = self.get_Hash(registrationNumber)
        if self.arr[index] is None:
            raise KeyError()
        else:
            for kvp in self.arr[index]:
                if kvp[0] == registrationNumber:
                    kvp[1] = value
            raise KeyError

    def delete(self,registrationNumber):
        index = self.get_Hash(registrationNumber)
        self.arr[index] = None
        print('Key ' + str(registrationNumber) + ' has been deleted.')

    def search(self, registrationNumber):
        indexFound = False
        value = self.arr[self.get_Hash(registrationNumber)]
        self.comparisons += 1
        try:
            if(value[0] == registrationNumber):
                return value[1]

            else:
                limit = 60
                y = 1
                index = self.get_Hash(registrationNumber)
                newIndex = index
                while y <= limit:
                    newIndex = index + (y**2)
                    newIndex = newIndex % self.size
                    value = self.arr[newIndex]
                    if value[0] == registrationNumber:
                        indexfound = True
                        break

                    else:
                        y += 1

                if indexFound:
                    return value[1]
                else:
                    print("Key is not Found in the Hash Table.")
                    return indexFound
        except TypeError:
            print("Key is not Found in the Hash Table.")
            return indexFound

    def displayHash(self):
        for i in range(self.size):
            print(i,end = ' ')
            print('->', end = " ")
            print(self.arr[i], end = ' ')
            print()

    def h_setitem(self,registrationNumber,val):
        h = self.get_Hash(registrationNumber)
        self.arr[h] = val

    def h_getitem(self,registrationNumber):
        h = self.get_Hash(registrationNumber)
        return self.arr[h]

class Owner:
    def __init__(self,name,icpassportNum,address):
        self.name = name
        self.icpassportNum = icpassportNum
        self.address = address

class Vehicle(Owner):
    def __init__(self,name,icpassportNum, address, model,color,engineCapacity,registrationNumber):
        Owner. __init__(self,name,icpassportNum,address)
        self.model = model
        self.color = color
        self.engineCcty = engineCapacity
        self.registrationNo = registrationNumber


def Menu(choice, h):
    while choice != 'Q' or choice != 'q':
        print(20* '*', 'MAIN MENU', 20* '*')
        print('\n[A] Enter A to register new vehicle ownership')
        print('[B] Enter B to transfer vehicle ownership')
        print('[C] Enter C to search vehicle ownership')
        print('[Q] Enter Q to exit System')
        print('\t')
        choice = input("***(Please enter your option [A-Q]): ")
        print('')
        if choice == 'A' or choice == 'a':
            print('Register New Vehicle Ownership')
            print('\t')
            name = input('1.Please enter your full name: ')
            ic = int(input('2.Please enter your IC or Passport number: '))
            address = input('3.Please enter your address: ')
            model = input("4.Please enter your vehicle's model: ")
            color = input("5.Please enter your vehicle's color: ")
            engineC = int(input("6.Please enter your vehicle's engine capacity: "))
            RNo = input("7.Please enter your vehicle's registration number: ")
            vehicle1 = Vehicle(name, ic, address, model, color, engineC, RNo)
            list1 = [vehicle1]
            print(list1)
            h.insert(RNo, vehicle1)
            print("____________________________________")
            print(h.search(RNo))
            print("____________________________________")
            foundObj = h.search(RNo)
            print(foundObj.name)
            h.displayHash()

        elif choice == 'B' or choice == 'b':
            print('Transfer Vehicle Ownership')

        elif choice == 'C' or choice == 'c':
            print('Search Vehicle Ownership')
            print(end = ' ')
            RNo = input("Please enter the vehicle registration number: ")
            foundObj = h.search(RNo)
            print(foundObj.name)
            print(foundObj.icpassportNum)
            print(foundObj.address)
            print(foundObj.model)
            print(foundObj.color)
            print(foundObj.engineCcty)
            print(foundObj.registrationNo)

        elif choice == 'Q' or choice == 'q':
            choice == 'Q'
            return choice
        else:
            print('You must only enter either -> (A,B,C,or Q).')
            print('Please reenter again')





if __name__ == '__main__':
    h = hashTable()
    print("\nWelcome to the Vehicle Ownership Registration System.")
    print('')
    choice = ' '
    Menu(choice, h)
