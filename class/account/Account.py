class Account:

    def __init__(self, acctNo, deposit):
        self.__acctNo = acctNo  # double underscore __private
        self._balance = deposit  # single underscore _protected

    def checkBalance(self):
        return self._balance

    def withdraw(self, amt):
        if amt <= self._balance:
            self._balance = self._balance + amt
            return True

        return False

    def deposit(self, amt):
        if amt > 0:
            self._balance = self._balance + amt
            return True
        return False


# main program
if __name__ == '__main__':
    a1 = Account("A1221", 6800)
    print("Initial Depost: ", a1.checkBalance())
    a1.deposit(3000)
    print("after deposit: ", a1.checkBalance())
