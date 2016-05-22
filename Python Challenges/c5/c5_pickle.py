# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:40:14 2016

@author: kiawo
"""

from urllib.request import urlopen
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
text = urlopen(url).read()
text[:20]

import pickle
data = pickle.loads(text)
len(data)

from pprint import  pprint

pprint(data[:5])

for pair in data[1]:
    print (pair[0]*pair[1])



for row in data:
    print(''.join(pair[0] * pair[1] for pair in row))