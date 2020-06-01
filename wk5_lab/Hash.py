
class Hash:

    def __init__(self, size):
        self.key = None
        self.tableSize = size
        self.table = [None] * size

    def hashFunction(self, key):
        return key % self.tableSize

    def deleteItem(self, key):
        index = self.hashFunction(key)

        try:
            if(self.table.remove(key)):
                print("Number {} has been successfully removed."
                      .format(key))
        except ValueError:
            print("There is no {} in the table."
                  .format(key))

    def displayHash(self):
        for i in range(self.tableSize):
            if self.table[i] is None:
                continue
            else:
                print(i, end=' ')
                print(" --> {}" .format(self.table[i]))
        print('\n')

    def linearProbing(self, key, key2, counter):
        index = self.hashFunction(key2)
        count = 0

        while(count < self.tableSize):
            if self.table[index + count] is None:
                self.table[index + count] = key
                if count is 0:
                    print("Insert successfully.")
                    break
                else:
                    print("Linear probing execute attempt {}: h({}) + {}: {}- "
                          "pass(insert successfully)"
                          .format(count, key, count, (count+index)))
                    break
            elif counter is not 0:
                if count is 0:
                    print("Collision detect at h{} : {}".format(key, index))
                    count += 1
                    continue
                else:
                    print("Linear probing execute attempt {}: h({}) + {}: {}-"
                          "fail"
                          .format(count, key, count, (count+index)))
                    count += 1
                    continue

    def doubleHashing(self, key):
        notFound = True
        index = self.hashFunction(key)
        if self.table[index] is None:
            self.table[index] = key
            print("Insert successfully.")
        else:
            hash2 = 7 - (key % 7)
            counter = 1
            while notFound:
                index2 = index
                index2 = self.hashFunction((index2 + counter * hash2))
                if self.table[index2] is None:
                    self.table[index2] = key
                    print("Double Hashing execute attempt {}: h({}) + {}: {}- "
                          "pass(insert successfully)"
                          .format(counter, key, counter, index2))
                    notFound = False
                else:
                    print("Double Hashing execute attempt {}: h({}) + {}: {}-"
                          "fail"
                          .format(counter, key, counter, index2))
                    counter += 1
                    if counter > self.tableSize:
                        print("Reached max table size. Unable to input {}"
                              .format(key))
                        break

    def hybridHashLinear(self, key):
        notFound = True
        index = self.hashFunction(key)
        if self.table[index] is None:
            self.table[index] = key
            print("Insert successfully.")
        else:
            hash2 = 7 - (key % 7)
            counter = 1
            while notFound:
                index2 = index
                index2 = self.hashFunction((index2 + counter * hash2))
                if self.table[index2] is None:
                    self.table[index2] = key
                    print("Linear probing execute attempt {}: h({}) + {}: {}- "
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
                self.linearProbing(key, index2, counter)
