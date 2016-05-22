# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:46:50 2016

@author: kiawo
"""


import re

p = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')

# data = ''.join([line.rstrip() for line in open('c3_input.txt')])    
data = open('c3_input.txt').read()

m = re.findall(p, data)

print(''.join(m))
