class Stack:
    def __init__(self):
        self.size = 20
        self.top = -1
        self.item = [0] * self.size

    def isEmpty(self):
        return self.top == -1

    def push(self, new):
        if self.top == self.size-1:
            return False
        self.top += 1
        self.item[self.top] = new
        return True

    def pop(self):
        if self.isEmpty():
            return False
        data = self.item[self.top]
        self.item.pop(data)
        self.top -= 1
        return data, True

    def peek(self):
        if self.isEmpty():
            return False
        data = self.item[self.top]
        return data, True

    def displayAll(self):
        self.item.reverse()
        for i in self.item:
            if i == 0:
                continue
            print("| {} |".format(i))
        print("======")


def sorting(originalStack, tempStack):
    while not originalStack.isEmpty():
        temp1 = originalStack.pop()
        temp2 = tempStack.peek()
        while not tempStack.isEmpty():
            temp2 = tempStack.pop()
            originalStack.push(temp2[0])
        tempStack.push(temp1[0])
    tempStack.displayAll()


if __name__ == "__main__":
    originalStack = Stack()
    tempStack = Stack()
    originalStack.push(5)
    originalStack.push(10)
    originalStack.push(20)
    originalStack.push(50)
    originalStack.push(30)

    sorting(originalStack, tempStack)
