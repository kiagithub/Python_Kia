"""
Tree
myTree = ['a',   #root
      ['b',  #left subtree
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #right subtree
       ['f', [], []],
       [] ]
     ]
"""

myTree = ['a',['b',['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', myTree[2])

#====================

def binary_tree(tree_root):
    """definition of a BINARY tree, those two brackets are children"""
    return [tree_root, [], []]

def insert_left(tree, new_branch):
    """inserts a new branch on the left side of the tree"""
    prev_left = tree.pop(1)
    if len(prev_left) > 1:
        tree.insert(1, [new_branch, prev_left, []])
    else:
        tree.insert(1, [new_branch, [], []])
    return tree

def insert_right(tree, new_branch):
    """inserts a new branch on the right side of the tree"""

    prev_right = tree.pop(2)
    if len(prev_right) > 1:
        tree.insert(2, [new_branch, [], prev_right])
    else:
        tree.insert(2, [new_branch, [], []])
    return tree

def getRootVal(tree):
    return tree[0]

def setRootVal(tree,newVal):
    tree[0] = newVal

def getLeftChild(tree):
    return tree[1]

def getRightChild(tree):
    return tree[2]

r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
l = getLeftChild(r)
print(l)

setRootVal(l, 9)
print(r)
insert_left(l, 11)
print(r)
print(getRightChild(getRightChild(r)))

