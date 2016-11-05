"""
we are going to examine parse trees in more detail. 
In particular we will look at:

How to build a parse tree from a fully parenthesized mathematical expression.
How to evaluate the expression stored in a parse tree.
How to recover the original mathematical expression from a parse tree.
RULES:
If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.
If the current token is a number, set the root value of the current node to the number and return to the parent.
If the current token is a ')', go to the parent of the current node.
"""
from stack import Stack
from tree1 import BinaryTree
