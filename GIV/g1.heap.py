# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:59:15 2016

@author: kiawo

more info on heap : https://pymotw.com/2/heapq/
                    https://docs.python.org/3/library/heapq.html

"""

import heapq
import math
from io import StringIO

def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    print()
    return
 
data = [19, 9, 4, 10, 11, 8, 2]
   
heap = []
print ('random :', data)
print

for n in data:
    print ('add %3d:' % n)
    heapq.heappush(heap, n)
    show_tree(heap)   
    
"""
You have k lists of sorted integers. Find the smallest range that 
includes at least one number from each of the k lists. 

For example, 
List 1: [4, 10, 15, 24, 26] 
List 2: [0, 9, 12, 20] 
List 3: [5, 18, 22, 30] 

The smallest range here would be [20, 24] as it contains 24 from list 1, 
20 from list 2, and 22 from list 3.
"""
def smallest_range(data, n):
    heap =[] 
    for i in range(n): #taking first element of each array
        heapq.heappush(heap,(data[i][0], i))
        del data[i][0]
    rmin = max(heap)[0]-min(heap)[0]
    l=0        
    while True :
        r = max(heap)[0]-min(heap)[0]
        if r <= rmin:
            rmin = r
            print(heap)
        (num, l) = heapq.heappop(heap)
        if data[l]!=[]:
            heapq.heappush(heap, (data[l][0], l))
            del data[l][0]
        else:
            break
    return heap       

mydata = [4,10,15,24,26],[0,9,12,20],[5,18,22,30]        
