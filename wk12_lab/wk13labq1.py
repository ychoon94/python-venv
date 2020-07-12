class Stack:
    def __init__(self):
        self.MAXSTACK = 20
        self.top = -1
        self.item = [0] * self.MAXSTACK

    def isEmpty(self):
        return self.top == -1

    def push(self, newItem):
        if (self.top == self.MAXSTACK - 1):
            return False
        self.top += 1
        self.item[self.top] = newItem
        return True

    def pop(self):
        if (self.isEmpty()):
            return False

        data = self.item[self.top]
        self.top -= 1
        return (data, True)

    def peek(self):
        if (self.isEmpty()):
            return False

        data = self.item[self.top]
        return (data, True)

    def displayAll(self):
        counter = self.MAXSTACK - 1
        while counter != -1:
            if self.item[counter] == 0:
                counter -= 1
                pass
            else:
                print(self.item[counter])
                counter -= 1


if __name__ == "__main__":
    stack = Stack()
    stack.push(40)
    stack.push(30)
    stack.push(20)
    stack.push(10)

    stack.displayAll()
