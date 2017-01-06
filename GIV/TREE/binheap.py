# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:16:19 2016

@author: kiawo
"""

class BinHeap(object):
    """
    Since the entire binary heap can be represented by a single list,
    all the constructor will do is initialize the list and an attribute
    currentSize to keep track of the current size of the heap.
    an empty binary heap has a single zero as the first element of heapList
    and that this zero is not used, but is there so that simple integer division 
    can be used in later methods.
    start index of the tree from 1 in your mind if you want index division to work
    """
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        """
        percUp method, which percolates a new item as far up in the tree
        as it needs to go to maintain the heap property.
        Here is where our wasted element in heapList is important.
        Notice that we can compute the parent of any node by using
        simple integer division. 
        The parent of the current node can be computed by dividing the index of
        the current node by 2.
        """
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
    
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        """
        First, we will restore the root item by taking the last item in
        the list and moving it to the root position. Moving the last item
        maintains our heap structure property.
        However, we have probably destroyed the heap order property of
        our binary heap. Second, we will restore the heap order property
        by pushing the new root node down the tree to its proper position. 
        """
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    def minChild(self,i):
        """
        In order to maintain the heap order property, all we need to do is 
        swap the root with its smallest child less than the root.
        After the initial swap, we may repeat the swapping process with
        a node and its children until the node is swapped into a position
        on the tree where it is already less than both children
        """
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
                
    def delMin(self):
        """
        Since the heap property requires that the root of the tree be 
        the smallest item in the tree, finding the minimum item is easy.
        The hard part of delMin is restoring full compliance with 
        the heap structure and heap order properties after the root 
        has been removed.
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
        
    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())        
