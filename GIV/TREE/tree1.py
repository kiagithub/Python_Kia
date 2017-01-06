class BinaryTree:
    """a Binary Tree Class
    """
    def __init__(self, rootObj):
        self.key = rootObj
        self.left_child = None
        self.right_child = None
    def insert_left(self, new_node):
        """Inserts a new node on the left side of the Root"""
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.left_child = self.left_child
            self.left_child = temp
    def insert_right(self, new_node):
        """Inserts a new node on the right side of the Root"""
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def set_root_value(self, obj):
        self.key = obj
    def get_root_value(self):
        return self.key

#    def preorder(self):
#        print(self.key)
#        if self.left_child:
#            self.left_child.preorder()
#        if self.right_child:
#            self.right_child.preorder()
# Some tests
#TESTTREE = BinaryTree('a')
#print(TESTTREE.get_root_value())
#TESTTREE.insert_left('b')
#TESTTREE.insert_right('c')
#TESTTREE.insert_left('b1')
#TESTTREE.insert_right('c1')

def preorder(tree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_value())
def inorder(tree):
    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_value())
        inorder(tree.get_right_child())