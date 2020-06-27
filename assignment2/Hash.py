# hashing class to store Registered Vehicle
# here it convert user vehicle register number to hash key
# then stores both vehicle register number and vehicle owner object in a list
# the hashing structure use here are double hashing and chaining

class Hash:

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
            print("/n-------Inserted successfully--------/n")
        else:
            hash2 = self.hash2(key)
            notFound = True
            counter = 1
            while notFound:
                index2 = (index + counter * hash2) % self.tableSize
                if not self.table[index2]:
                    self.table[index2].append([key, value])
                    print("/n-------Inserted successfully--------/n")
                    notFound = False
                else:
                    counter += 1
                    if counter > 3:
                        break
            if notFound:
                counter = 1
                self.table[index2].append([key, value])
                print("/n-------Inserted successfully--------/n")

    def displayHash(self):
        for i in range(self.tableSize):
            if self.table[i] is None:
                continue
            else:
                print(i, end=' ')
                print(" --> {}" .format(self.table[i]))
        print('\n')

    def searchKey(self, key):
        notFound = True
        counter = 0
        index = self.hashFunction(key)
        while notFound:
            # if not empty and 1st loop then perform search
            if counter is 0:
                if self.table[index]:  # check if the list is empty
                    try:
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
                            position = self.table[index2][i][0].index(key)
                            notFound = False
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

    def searchReplace(self, key, newOwner):
        notFound = True
        counter = 0
        index = self.hashFunction(key)
        while notFound:
            # if not empty and 1st loop then perform search
            if counter is 0:
                if self.table[index]:  # check if the list is empty
                    try:
                        position = self.table[index][0].index(key)
                        notFound = False
                        self.table[index][0][1] = newOwner
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
                        position = self.table[index2][0][0].index(key)
                        notFound = False
                        self.table[index2][0][1] = newOwner
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
                            position = self.table[index2][i][0].index(key)
                            notFound = False
                            print("Value found.\n")
                            self.table[index2][i][1] = newOwner
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
