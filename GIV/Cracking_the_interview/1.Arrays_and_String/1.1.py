# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 09:46:33 2016

@author: kiawo

Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures?


"""

# O(N)
import unittest

#def unique(string):
#    # Assuming character set is ASCII (128 characters)
#    if len(string) > 128:
#        return False
#
#    char_set = [False for _ in range(128)]
#    # a list of 128 False!!1
#    for char in string:
#        val = ord(char)
#        # ord returns ASCII number associated to char
#        if char_set[val]:
#            # Char already found in string
#            return False
#        char_set[val] = True
#
#    return True

#======================================================

#without data structure and with sort
#def unique(string):
#    text = sorted(string)
#    for i in range((len(text)-1)):       
#        if text[i] == text[i+1]:
#           return False
#    return True



# Using Set(), kia idea 1/8/17

def unique(string):
    string_unique = set(string)
    return len(string_unique)== len(string)


#======================================================

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()