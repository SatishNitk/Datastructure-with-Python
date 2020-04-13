class node:

    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data


class BST:
    
    root = None

    def insert(self, root,  data):
        if root == None:
            root = node(data)
            return root
        else:
            if root.data > data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root

    def inorder(self, root, ele):

        if root:
            self.inorder(root.left, ele)
            ele.append(root.data)
            self.inorder(root.right, ele)

    def preorder(self, root, ele):
        if root:
            ele.append(root.data)
            self.preorder(root.left, ele)
            self.preorder(root.right, ele)

    def postorder(self, root, ele):
        if root:
            self.postorder(root.left, ele)
            self.postorder(root.right, ele)
            ele.append(root.data)

    def height(self, root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)

        return left+1 if left > right else right +1

    def max(self, root):
        if root.right == None:
            return root.data
        return self.max(root.right)
            
    def min(self, root):
        if root.left == None:
            return root.data
        return self.min(root.left)

    def sum_of_tree(self, root):
        if root == None:
            return 0
        else:
            return (root.data + self.sum_of_tree(root.left) + self.sum_of_tree(root.right))


    def max_sum_root_leaf(self, root):
        if root == None:    return 0

        max_sum_left = 0 if root is None else self.max_sum_root_leaf(root.left)
        max_sum_right = 0 if root is None else self.max_sum_root_leaf(root.right)
        
        return (root.data + max_sum_left) if max_sum_left > max_sum_right else  (root.data + max_sum_right)
    
    def path_of_given_sum(self, root, sum1_val, ele):
        
        if sum1_val == 0:
            return True
        if root is None:
            return False
        sum1_val -= root.data
        left = self.path_of_given_sum(root.left, sum1_val, ele)
        right = self.path_of_given_sum(root.right, sum1_val, ele)
        if left or right:
            ele.append(root.data)
        return left or right

    def check_for_mirror_image(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        return (root1.data == root2.data and (self.check_for_mirror_image(root1.left, root2.right)) and (self.check_for_mirror_image(root1.right, root2.left))    )
    
    def print_all_path(self, root, ele, index):
        if root is None:
            return
        ele.insert(index,root.data)
        index += 1
        if root.left is None and root.right is None:
            print(ele[0:index])
            index -= 1
            return  

        self.print_all_path(root.left, ele, index)
        self.print_all_path(root.right, ele, index)







bst = BST()
BST.root = bst.insert(BST.root, 10)
BST.root  = bst.insert(BST.root, 3)
BST.root  = bst.insert(BST.root, 1)
BST.root  = bst.insert(BST.root, 2)
BST.root  = bst.insert(BST.root, 18)

ele = []
bst.print_all_path(BST.root, ele, 0)
ele.clear()

bst.inorder(BST.root, ele)
print("inorder", ele)

ele.clear()
bst.preorder(BST.root, ele)
print("preorder", ele)

ele.clear()
bst.postorder(BST.root, ele)
print("postorder", ele)

print("height : -", bst.height(BST.root))

print("MAX : -", bst.max(BST.root))
print("MIN : -", bst.min(BST.root))

print("sum_of_tree : -", bst.sum_of_tree(BST.root))

print(bst.max_sum_root_leaf(BST.root))
ele.clear()
bst.path_of_given_sum(BST.root, 16, ele)
print("path of given sum is :- ", ele)


#------- for mirror image

root1 = node(1) 
root2 = node(1) 
  
root1.left = node(2) 
root1.right = node(3) 
root1.left.left = node(4) 
root1.left.right = node(5) 
root1.left.right.left = node(15) 

  
root2.left = node(3) 
root2.right = node(2) 
root2.right.left = node(5) 
root2.right.right = node(4)
root2.right.left.right = node(15)


print(bst.check_for_mirror_image(root1, root2))

#------------ end mirror image