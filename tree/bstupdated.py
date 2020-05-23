class TreeNode:
    def __init__(self, data):
        self.item = data
        self.leftChild = None
        self.rightChild = None

    def find(self, data):
        if(self.item == data):
            return True
        elif self.item > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False


class BST:
    def __init__(self):
        self.__root = None
        self.__numOfItem = 0

    def size(self):
        return self.__numOfItem

    def insert(self, data):
        newNode = TreeNode(data)  # create new Node
        if self.__root is None:    # if BST is empty
            self.__root = newNode
        else:
            curr = self.__root
            par = None

            while curr is not None:    # traversal until leaf
                par = curr
                if data < curr.item:
                    curr = curr.leftChild
                elif data > curr.item:
                    curr = curr.rightChild
                else:
                    return False   # no allow duplicate item insert

            if data < par.item:
                par.leftChild = newNode  # insert as left child
            else:
                par.rightChild = newNode  # insert as right child
        self.__numOfItem += 1
        return True

    def lowestitemNode(self):
        if self.__root is None or TreeNode.leftChild is None:
            return self.__root
        return self.lowestitemNode(TreeNode.leftChild)

    def __remove(self, data):
        # empty tree
        if self.__root is None:
            return False

        # data is in root node
        elif self.__root.item == data:
            if self.__root.leftChild is None and self.__root.rightChild is None:
                self.__root = None
            elif self.__root.leftChild and self.__root.rightChild is None:
                self.__root = self.__root.leftChild
            elif self.__root.leftChild is None and self.__root.rightChild:
                self.__root = self.__root.rightChild
            elif self.__root.leftChild and self.__root.rightChild:
                delNodeParent = self.__root
                delNode = self.__root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                    self.__root.item = delNode.item
                    if delNode.rightChild:
                        if delNodeParent.item > delNode.item:
                            delNodeParent.leftChild = delNode.rightChild
                        elif delNodeParent.item < delNode.item:
                            delNodeParent.rightChild = delNode.rightChild
                        else:
                            if delNode.item < delNodeParent.item:
                                delNodeParent.leftChild = None
                            else:
                                delNodeParent.rightChild = None

            return True

        parent = None
        node = self.__root

        # find node to remove
        while node and node.item != data:
            parent = node
            if data < node.item:
                node = node.leftChild
            elif data > node.item:
                node = node.rightChild

        # case 1: data not found
        if node is None or node.item != data:
            return False

        # case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.item:
                parent.leftChild = None
            else:
                parent.rightChild = None
                return True

        # case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.item:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
                return True

        # case 4: remove-node has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.item:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
                return True

        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild

        node.item = delNode.item
        if delNode.rightChild:
            if delNodeParent.item > delNode.item:
                delNodeParent.leftChild = delNode.rightChild
            elif delNodeParent.item < delNode.item:
                delNodeParent.rightChild = delNode.rightChild
            else:
                if delNode.item < delNodeParent.item:
                    delNodeParent.leftChild = None
        else:
            delNodeParent.rightChild = None

    def find(self, data):
        if self.__root:
            return self.__root.find(data)
        else:
            return False

    def __inOrder(self, TreeNode):
        if TreeNode is None:
            return
        self.__inOrder(TreeNode.leftChild)
        print(TreeNode.item)
        self.__inOrder(TreeNode.rightChild)

    def displayAll(self):
        self.__inOrder(self.__root)

    def delete(self, data):
        self.__remove(data)


myBst = BST()
myBst.insert(40)
myBst.insert(10)
myBst.insert(15)
myBst.insert(50)
myBst.displayAll()
myBst.delete(15)
print("after delete 15")
myBst.displayAll()
print("search for 10")
print(myBst.find(10))
print("search for 100")
print(myBst.find(100))
