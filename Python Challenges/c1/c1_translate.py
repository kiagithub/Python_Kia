# -*- coding: utf-8 -*-
"""
Created on Wed May 11 22:15:33 2016

@author: kiawo
"""

#Python Challenge 1
text = input('Inter your text: ')
text_split = list(text)

def conv(x):
    return {
       'k':'m',
       'o':'q',
       'e':'g'
    }[x]
    
for i in range(len(text_split)):
    if text_split[i] == ('k' or 'o' or 'e'):
        text_split[i] = conv(text_split[i])

''.join(text_split)

#----------------

text = input('Inter your text: ')
text_split = list(text)
    
for i in range(len(text_split)):
    text_split[i] = (chr(ord(text_split[i])+2))

''.join(text_split)

#----------------
from string import ascii_lowercase
text = input('Inter your text: ')
trans = str.maketrans(ascii_lowercase, ascii_lowercase[2:] + ascii_lowercase[:2])
text.translate(trans)


    
