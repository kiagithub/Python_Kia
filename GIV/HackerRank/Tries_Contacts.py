# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:54:27 2016

@author: kiawo

Info: https://www.hackerrank.com/challenges/ctci-contacts?h_r=next-challenge&h_v=zen
Info: https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python/11015381#11015381

"""
"""
how to write a trie with dictionary

"""
#_end = '_end_'
# 
#def make_trie(*words):
#    root = dict()
#    for word in words:
#        current_dict = root
#        for letter in word:
#            current_dict = current_dict.setdefault(letter, {})
#        current_dict[_end] = _end
#    return root
#
##a function to test whether the word is in the trie (complete word not a partial)
#def in_trie(trie, word):
#    current_dict = trie
#    for letter in word:
#        if letter in current_dict:
#            current_dict = current_dict[letter]
#        else:
#            return False
#    if _end in current_dict:
#        return True
#    else:
#        return False
#        
#in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'baz')
#in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barz')
#in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barzz')
#in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'ba')

"""
HackerRank problem

"""

from collections import defaultdict

class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.
    """
    def __init__(self):
        self.root = defaultdict()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")
        return self.root
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True

# Now test the class

test = Trie()
test.insert('helloworld')
test.insert('ilikeapple')
test.insert('helloz')

print (test.search('hello'))
print (test.startsWith('hello'))
print (test.search('ilikeapple'))
    
    
    
    
    
    
    
    