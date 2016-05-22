# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:44:06 2016

@author: kiawo
"""

import urllib.request
import re

p = re.compile(b'.*?([0-9]+)$')
i = 1
my_text = []
my_int = [12345]
while i<4:
    f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(my_int[i-1]))    
    my_text.append(f.readline())  
    my_int.append(re.findall(p, my_text[i-1]))
    i = i+1

#=======================================     

from urllib.parse import urlparse
from urllib.request import urlopen
 
nothing = '8022'
 
while nothing.isdigit():
    # get modified url
    obj = urlparse('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing) 
    # get the web page source
    src = urlopen(obj.geturl()).read()
    # extract the part of digits, and convert it from bytes to str
    nothing = src.split( )[-1].decode()
    print(src)