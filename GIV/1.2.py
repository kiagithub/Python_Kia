# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:39:45 2016

@author: kiawo
"""

# O(NlogN)
import unittest

'''
def check_permutation(string):
    # function checks if a string is permutation of another
    str1, str2 = string[0], string[1]
    #When we have input in the form of 'abcd', 'bacd': string[0] gets the first
    #word not the first character
    if len(str1) == len(str2):
        arr1, arr2 = [], []
        for char in str1:
            arr1.append(char)
        for char in str2:
            arr2.append(char)
        arr1.sort()
        arr2.sort()
        for index in range(len(arr1)):
            if arr1[index] != arr2[index]:
                return False
        return True
    else:
        return False
'''
#=============================================================
"""Kia's code"""

def check_permutation(string):
    str1, str2 = string[0], string[1]
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            return False
        else:
            return True

#=============================================================
class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]

    def test_cp(self):
        # true check
        for test_string in self.dataT:
            actual = check_permutation(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = check_permutation(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()