# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:34:05 2016

@author: kia
"""

def answer(food, grid):
    def remain(n, i, j):
        n -= grid[i][j]
        if i < 0 or j < 0 or n < 0:
            return food + 1
        elif i == j == 0:
            return n
        else:
            return min(remain(n, i - 1, j), remain(n, i, j - 1))

    remainder = remain(food, len(grid) - 1, len(grid) - 1)
    return remainder if remainder <= food else -1
    
#============Modified by me
    
"""
Created on Thu Jun  2 13:34:05 2016

@author: kia
"""
from functools import wraps

def memo(f):
    """Decorator that caches a function's return value each time it is
    called. If called later with the same arguments, the cached value
    is returned, and not re-evaluated.

    """
    cache = {}
    @wraps(f)
    def wrapped(*args):
        try:
            result = cache[args]
        except KeyError:
            result = cache[args] = f(*args)
        return result
    return wrapped
    
def answer(food, grid):

    @memo
    def r(t, i, j):
        # Smallest remainder from t after subtracting the numbers on a path
        # from top left to (i, j) in grid, or total + 1 if there is no
        # path whose sum is less than or equal to t.
        t -= grid[i][j]
        if i < 0 or j < 0 or t < 0:
            return food + 1
        elif i == j == 0:
            return t
        else:
            return min(r(t, i - 1, j), r(t, i, j - 1))

    remainder = r(food, len(grid) - 1, len(grid) - 1)
    return remainder if remainder <= food else -1
    