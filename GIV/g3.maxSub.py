# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:15:11 2016

@author: kiawo

Given an array of integers, find two non-overlapping contiguous 
sub-arrays such that the absolute difference between the sum of 
two sub-arrays is maximum.

For example,

Input: [-2, -3, 4, -1, -2, 1, 5, -3]
Output: 12
Two subarrays are [-2, -3] and [4, -1, -2, 1, 5]

Input: [2, -1, -2, 1, -4, 2, 8]
Output: 16
Two subarrays are [-1, -2, 1, -4] and [2, 8] 
Expected time complexity is O(n).

more info:
http://www.geeksforgeeks.org/
maximum-absolute-difference-between-sum-of-two-contiguous-sub-arrays/
http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""
def abs_diff(data):
    return max_sub(data)-min_sub(data)
    
def max_sub(data):
    max_so_far = 0
    max_here = 0
    for i in range(len(data)):
        max_here = max(0, max_here+data[i])
        max_so_far = max(max_here, max_so_far)    
    return max_so_far
    
def min_sub(data):
    revdata =[x*(-1) for x in data]
    return (-(max_sub(revdata)))
    
data = [-2, -3, 4, -1, -2, 1, 5, -3]
data1 = [2, -1, -2, 1, -4, 2, 8]
