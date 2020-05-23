import random
from datetime import datetime

class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createnode(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def Display_Distinction(self):
        if self.head is None:
            print("List has no element.")
            return
        else:
            temp = self.head
            while temp is not None:
                if temp.data >= 70:
                    print("{}  ".format(temp.data), end = " ")
                    temp = temp.next
                else:
                    temp = temp.next


if __name__ == "__main__":
    obj = LinkedList()
    for i in range(20):
        random.seed(datetime.now()) #seed random time
        obj.createnode(random.randint(50,100)) #create random obj from range 50-100
    print("\n-------------------------------------------------------\n")
    print("--------------Displaying Distinction only--------------")
    print("\n-------------------------------------------------------\n")
    obj.Display_Distinction()
    print("\n-------------------------------------------------------\n")
