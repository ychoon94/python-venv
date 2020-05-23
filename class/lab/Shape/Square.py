from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, nLength):
        super().__init__(nLength)

    def area(self):
        A = (self.sideLengths[0] * self.sideLengths[1])

        return A
