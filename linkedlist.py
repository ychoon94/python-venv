class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("List has no element.")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, ' ')
                temp = temp.next

    def createnode(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insert_start(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_position(self, pos, value):
        if pos == 1:
            new_node = node(value)
            new_node.next = self.head
            self.head = new_node
        i = 1
        temp = start.head
        while i < pos - 1 and temp is not None:
            temp = pos.next
            i += 1
        if temp is None:
            print("Position is out of bound.")
        else:
            new_node = node(value)
            new_node.next = temp.next
            temp.next = new_node

    def insert_after_item(self, x, value):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                break
            temp = temp.next
        if temp is None:
            print("Item not in the list.")
        else:
            new_node = node(value)
            new_node.next = temp.next
            temp.next = new_node

    def insert_before_item(self, x, value):
        if self.head is None:
            print("List has no element.")
            return
        if x == self.head.data:
            new_node = node(data)
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.value == x:
                break
            temp = temp.next
        if temp.next is None:
            print("Item not in the list")
        else:
            new_node = node(value)
            new_node.next = temp.next
            temp.next = new_node

    def get_count(self):
        if self.head is None:
            return 0;
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def search_item(self, x):
        if self.head is None:
            print("List has no element.")
            return
        temp = self.head
        while temp is not None:
            if temp.data == x:
                print("Item found.")
                return True
            temp = temp.next
        print("Item not found.")
        return False

    def delete_first(self):
        if self.head is None:
            print("The list has no element to delete.")
            return
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("The list has no element to delete.")
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_value(self, x):
        if self.head is None:
            print("The list no element to delete.")
            return

        #deleting first node
        if self.head.data == x:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.value == x:
                break
            temp = temp.next

        if temp.next is None:
            print("Item not found in the list.")
        else:
            temp.next = temp.next.next


if __name__ == "__main__":
    obj = LinkedList()

    obj.createnode(100)
    obj.createnode(20)
    obj.createnode(10)
    obj.insert_after_item(20, 300)

    obj.delete_first()
    obj.delete_last()
    obj.display()
