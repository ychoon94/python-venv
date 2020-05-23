class TreeNode:
    self.item = data
    self.leftChild = None

    def __init__(self, data):
        self.rightChild = None


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
                    return False   # no allow duplicate value insert

            if data < par.item:
                par.leftChild = newNode  # insert as left child
            else:
                par.rightChild = newNode  # insert as right child
        self.__numOfItem += 1
        return True

    def __remove(self, data):
        # implementation required

    def __inOrder(self, TreeNode):
        if TreeNode is None:
            return
        self.__inOrder(TreeNode.leftChild)
        print(TreeNode.item)
        self.__inOrder(TreeNode.rightChild)

    def displayAll(self):
        self.__inOrder(self.__root)


myBst = BST()
myBst.insert(40)
myBst.insert(10)
myBst.insert(15)
myBst.insert(50)
myBst.displayAll()
