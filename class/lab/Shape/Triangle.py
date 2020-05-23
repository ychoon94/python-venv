from math import sqrt

from Shape import Shape


class Triangle(Shape):
    def __init__(self, nLength):
        super().__init__(3, nLength)

    def area(self):
        s = (self.sideLengths[0] +
             self.sideLengths[1] + self.sideLengths[2]) / 2
        A = sqrt(s * (s - self.sideLengths[0]) * (s - self.sideLengths[1]) * (s - self.sideLengths[2]))

        return A
