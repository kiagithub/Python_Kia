# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:52:57 2016

@author: kiawo
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

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
            #new index is an integer it can become negetaive
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string, new_index


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()