# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:05:02 2016

@author: kiawo

Info: https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""
from collections import deque

def array_left_rotation(a, n, k):
    item = deque(a)
    for i in range (k):
        item.append(item.popleft())
    return item

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(answer, sep=' ')
