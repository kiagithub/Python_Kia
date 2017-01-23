# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:52:57 2016

@author: kiawo

Write a method to replace all spaces in a string with '%20'

"""

# O(N)
import unittest

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    space = 0    
    for j in range(length):
        if string [j]==' ':
            space += 1
    new_index = length + (2*space)
    #we already have one space and we need to have 3 space overall for %20, so (2*space)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
            #new index is an integer and in the end it becomes zero
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

#kia's version 1/14/17
#def urlify(string, length):
#    true_string = "".join(string[0:length])
#    return list(true_string.replace(" ", "%20"))


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [(list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()