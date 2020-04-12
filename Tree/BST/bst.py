class node:

    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data > data:
            if self.left:
                return self.left.insert(data)
            else:
                new_node = node(data)
                self.left = new_node
                return True
        elif(self.data < data):
            if self.right:
                return self.right.insert(data)
            else:
                new_node = node(data)
                self.right = new_node
                return True

    def inorder(self, ele):
        if self:
            if self.left:
                self.left.inorder(ele)
            ele.append(self.data)
            if self.right:
                self.right.inorder(ele)

    def preorder(self, ele):
        if self:
            ele.append(self.data)
            if self.left:
                self.left.preorder(ele)
            if self.right:
                self.right.preorder(ele)

    def postorder(self, ele):
        if self:
            if self.left:
                self.left.postorder(ele)
            if self.right:
                self.right.postorder(ele)
            ele.append(self.data)

    def find(self, data):
        """Check for element is available in a tree or not """
        if self:
            if self.data == data:
                return True
            elif int(self.data) < data:
                if self.right:
                    return self.right.find(data)
                else:
                    return False
            else:
                if self.left:
                    return self.left.find(data)
                else:
                    return False

    def height(self, root):
        """ calculate height of tree"""
        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        if left > right:
            return left + 1
        else:
            return right + 1



class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = node(data)
            return True
    
    def inorder(self):
        ele = []
        self.root.inorder(ele)
        print(ele)

    def preorder(self):
        ele = []
        self.root.preorder(ele)
        print(ele)

    def postorder(self):
        ele = []
        self.root.postorder(ele)
        print(ele)

    def find(self, data):
        print(self.root.find(data))

    def height(self):
        print(self.root.height(self.root))


bst  = BST()
bst.insert(6)
bst.insert(31)
bst.insert(1)
bst.insert(12)
bst.insert(112)


bst.inorder()
bst.preorder()
bst.postorder()

bst.find(1212)

bst.height()

