
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

    def insertItem(self, key):
        index = self.hashFunction(key)
        self.table[index].append(key)

    def deleteItem(self, key):
        index = self.hashFunction(key)

        try:
            if(self.table[index].remove(key)):
                print("Number {} has been successfully removed."
                      .format(key))
        except ValueError:
            print("There is no {} in the table."
                  .format(key))

    def displayHash(self):
        for i in range(len(self.table)):
            if not self.table[i]:
                print(i)
            else:
                print(i, end=' ')
                print(" --> {}" .format( self.table[i]))
        print('\n')


if __name__ == "__main__":
    a = ["pkb234", "pkv1234", "phb2323", "akb234", "ghe342"]
#"pkb234", "pkv1234", "phb2323",
#"0000", "kv1234c", "pob2523",
    h = Hash(7)

    for i in range(len(a)):
        h.insertItem(a[i])

    h.displayHash()

    h.deleteItem("0000")

    h.displayHash()
