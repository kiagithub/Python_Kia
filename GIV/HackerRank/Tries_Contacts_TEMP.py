# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:27:22 2016

@author: kiawo
"""

from collections import defaultdict


def get_nested(my_dict, keys=[]):
    key = keys.pop(0)
    if len(keys) == 0:
        return my_dict[key]
    return get_nested(my_dict[key], keys)

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

        
        
    # modified Startwith

    def find(self, prefix):
        current = self.root
        search_list = []
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
            search_list.append(letter)
        return len(get_nested(dict(self.root), keys = search_list))


test = Trie()    
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        test.insert(contact)
    elif op == 'find':
        print(test.find(contact))