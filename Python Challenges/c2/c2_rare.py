# -*- coding: utf-8 -*-
"""
Created on Wed May 11 23:59:32 2016

@author: kiawo
"""

import string
text = input('Inter your text: ')
exclude = set(string.punctuation)
text = ''.join(ch for ch in text if ch not in exclude)
text = text.strip()
f = open ('c2.txt', 'r+')
f.write(str(text))
f.close()

#==========================
from collections import OrderedDict
data = ''.join([line.rstrip() for line in open('c2_input.txt')])    
OCCURRENCES = OrderedDict()
for c in data: 
    OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
    avgOC = len(data) // len(OCCURRENCES)
print (''.join([c for c in OCCURRENCES if OCCURRENCES[c] < avgOC])) 