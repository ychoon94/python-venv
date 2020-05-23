from Shape import Shape


class Rectangle(Shape):
    def __init__(self, nLength):
        super().__init__(4, nLength)

    def area(self):
        A = self.sideLengths[0] * self.sideLengths[1]

        return A
