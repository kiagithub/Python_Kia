"""
we are going to examine parse trees in more detail.
In particular we will look at:

How to build a parse tree from a fully parenthesized mathematical expression.
How to evaluate the expression stored in a parse tree.
How to recover the original mathematical expression from a parse tree.
RULES:
If the current token is a '(', add a new node as the left child of the current
 node, and descend to the left child.
If the current token is in the list ['+','-','/','*'], set the root value of
the current node to the operator represented by the current token.
Add a new node as the right child of the current node and descend to
the right child.
If the current token is a number, set the root value of the current node
to the number and return to the parent.
If the current token is a ')', go to the parent of the current node.
"""
from stack import Stack
from tree1 import BinaryTree


def build_Parse_Tree(fpexp):
    """
    a function that builds a parsed tree
    """
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    current_tree = eTree
    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            pStack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_value(int(i))
            parent = pStack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            pStack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = pStack.pop()
        else:
            raise ValueError
    return eTree
pt = build_Parse_Tree("( ( 10 + 5 ) * 3 )")

#pt.preorder()  #defined and explained in the next section
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