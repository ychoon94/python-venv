class Vehicle:

    def __init__(self, regNum, color, engine, maker, model, vehicleType):
        self.__regNum = regNum
        self.color = color
        self.engine = engine
        self.maker = maker
        self.model = model
        self.vehicleType = vehicleType

    def getRegNum(self):
        return self.__regNum

    def setRegNum(self, newRegNum):
        self.__regNum = newRegNum
