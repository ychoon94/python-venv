from Account import Account

class Saving(Account):
    def __init__(self, acctNo, deposit, interestRate):
        super().__init__(acctNo, deposit) #calling superclass constructor
        self.__interestRate = interestRate

    def __getInterestRate(self):
        return self.__interestRate

    def addInterest(self):
        self._balance = self._balance + self._balance * self.__interestRate


#program
if __name__ == '__main__':
    s1 = Saving("1234", 50000, 0.03)
    s1.deposit(1000)
    print("Balance: ", s1.checkBalance())
