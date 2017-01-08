# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:30:08 2016

@author: kiawo

info: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen
"""

# Python program to check if a binary tree is bst or not
 
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
# Returns true if the given tree is a binary search tree 
def check_binary_search_tree_(root):
    return is_binary_tree(root, -float('inf'), float('inf'))

# Return true if the given tree is a BST and its values
# >= min and <= max
def is_binary_tree(node, mini, maxi):
    if node is None:
        return True
    
    if node.data < mini or node.data > maxi:
        return False
    
    return (is_binary_tree(node.left, mini, node.data-1)) and (is_binary_tree(node.right, node.data+1, maxi))
    
# Driver program to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

check_binary_search_tree_(root)