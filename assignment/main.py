from Person import *
from Vehicle import Vehicle


def showMenu():
    print("Welcome to JPJ Vehicle Ownership Registration System.")
    print("_____________________________________________________")
    print("Please choose a task to perform: ")
    print("1. Register new vehicle ownership")
    print("2. Transfer vehicle ownership")
    print("3. Search vehicle ownership")
    print("4. Exit System")


if __name__ == "__main__":
    p1 = vehicleOwner("yc", "123456-03-2323",
                      "8654, Medan bukit Marut 4, Testing 404, 10234,"
                      " BaTe Lopir, P3uyre", "P1234", "red", "1.4",
                      "toyota", "camry", "car")

    p2 = vehicleOwner("yc", "123456-03-2323",
                      "8654, Medan bukit Marut 4, Testing 404, 10234,"
                      " BaTe Lopir, P3uyre", "P1234", "red", "1.4",
                      "toyota", "camry", "car")

    p3 = vehicleOwner("yc", "123456-03-2323",
                      "8654, Medan bukit Marut 4, Testing 404, 10234,"
                      " BaTe Lopir, P3uyre", "P1234", "red", "1.4",
                      "toyota", "camry", "car")

    p4 = vehicleOwner("yc", "123456-03-2323",
                      "8654, Medan bukit Marut 4, Testing 404, 10234,"
                      " BaTe Lopir, P3uyre", "P1234", "red", "1.4",
                      "toyota", "camry", "car")

    mylist = [p1, p2, p3, p4]

    print(p1.getName())
    print(p1.getRegNum())
    print(p1.model)
    # print(type(p4.getAddress()))
    p5 = Person("cermanine", "967583-45-2323", "123, 1413 kjhhjhvj, hhhgj, ma")
    p4.transferOwner(p5)

    print(p4.getName())
    print(p4.getIC())
    print(p4.getAddress())
# name, ic, address, regNum, color, engine, maker, model, vehicleType):
# "yc", "123456-03-2323",
#                         "8654, Medan bukit Marut 4, Testing 404, 10234, BaTe Lopir, P3uyre", "P1234", "red", "1.4",
#                         "toyota", "camry", "car"
