from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from math import sqrt


def loopTriangle(numOfSide):
    n = 0
    list = []
    while n < numOfSide:
        try:
            list.append(float(input("Enter the side length: ")))
            n += 1
        except:
            print("Please enter number only!")
    return list


def loopRectangle(numOfSide):
    n = 0
    list = []
    while n < numOfSide:
        try:
            list.append(float(input("Enter the side length: ")))
            n += 1
        except:
            print("Please enter number only!")
    return list


if __name__ == "__main__":
    side = int(input("Please enter the number of sides: "))
    if side == 3:
        print("This is a Triangle.\n")
        Tri1 = Triangle(loopTriangle(side))
        print("The area for triangle is {0:.2f}".format(Tri1.area()))
    elif side == 4:
        shape1 = loopRectangle(side/2)
        temp = shape1[0]
        if temp == shape1[1]:
            print("This is a Square.\n")
            Squ1 = Square(shape1)
            print("The area for square is {0:.2f}".format(Squ1.area()))

        elif temp != shape1[1]:
            print("This is a Rectangle.\n")
            Rec1 = Rectangle(shape1)
            print("The area for rectangle is {0:.2f}".format(Rec1.area()))

    else:
        print("error.")
