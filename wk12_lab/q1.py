class Stack:
    def __init__(self):
        self.MAXSTACK = 20
        self.top = -1
        self.item = [0] * self.MAXSTACK

    def isEmpty(self):
        return self.top == -1

    def push(self, newItem):
        if (self.top == self.MAXSTACK-1):
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
        for i in self.item[self.top::-1]:
            if i == 0:
                continue
            print("|{}|".format(i))
        print("====")


if __name__ == "__main__":
    newStack = Stack()

    newStack.push(40)
    newStack.push(30)
    newStack.push(20)
    newStack.push(10)
    newStack.push(50)

    newStack.displayAll()
    newStack.pop()
    newStack.displayAll()
    print("\n")
    print(newStack.item)
