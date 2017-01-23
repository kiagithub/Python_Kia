# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:55:47 2016

@author: kiawo

find the kth to last element of a singly linkedlist
"""

from LinkedList import LinkedList


def kth_to_last(ll, k):
    runner = current = ll.head
    #runner goes kth place forward
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next
    #while runner hasn't reached the end we continue and go through ll for two
    #pointers
    while runner:
        current = current.next
        runner = runner.next

    return current

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 4))