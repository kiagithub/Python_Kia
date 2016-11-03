# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 20:46:26 2016

@author: kiawo
"""

import math
import sys


def answer(document, search_terms):
    """Index the position of all search_terms then find the min "score" for a search."""
    index = {k: [] for k in search_terms}
    tokens = document.split()
    for i, token in enumerate(tokens, start=1):
        if token in search_terms:
            index[token].append(i)
    min_score = sys.maxsize
    winning_slice = None
    for term in index.keys():  # ignore duplicate terms
        for position in index[term]:
            positions = [position]
            for other_term in index.keys():
                distances = [int(math.fabs(position - x)) for x in index[other_term]]
                positions.append(index[other_term][distances.index(min(distances))])
            score = max(positions) - min(positions) + 1
            if score < min_score:
                winning_slice = (min(positions) - 1, max(positions),)
                min_score = score
    return " ".join(tokens[slice(*winning_slice)])

if __name__ == '__main__':
    print(answer("many google employees can program can google employees because google is a technology company that writes programs", ["google", "program", "can"]))
    print(answer("a b d a c a c c d a",["a", "c", "d"]))