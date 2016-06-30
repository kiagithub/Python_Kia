# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:29:51 2016

@author: kia
"""

# chapter 3 Ipython

from numpy.random import randn
data = {i : randn() for i in range(7)}
data

#data?

a = np.random.randn(100, 100)
# %timeit np.dot(a, a)
# %prun np.dot(a, a)


# a very large list of strings
strings = ['foo', 'foobar', 'baz', 'qux', 'python', 'Guido Van Rossum'] * 100000

#%time method1 = [x for x in strings if x.startswith('foo')]
#%time method2 = [x for x in strings if x[:3] == 'foo']

#%timeit method1 = [x for x in strings if x.startswith('foo')]
#%timeit method2 = [x for x in strings if x[:3] == 'foo']

#==========

import numpy as np
from numpy.linalg import eigvals
def run_experiment(niter=100):
    K = 100
    results = []
    for _ in range(niter):
        mat = np.random.randn(K, K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results
some_results = run_experiment()
print ('Largest one we saw: %s' % np.max(some_results))

import cProfile
cProfile.run(np.max(some_results))



