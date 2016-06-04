# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:28:36 2016

@author: kia
"""
chunk1 = "lololololo"
word1 = "lol"

def answer(chunk, word):
    final_result = []
    # indices of word occurance
    instance = [i for i in range(len(chunk)) if chunk.startswith(word, i)]
    # Loop through those instance
    for i in instance:
        # word remover
        text = chunk[0:i] + chunk[i+len(word):len(chunk)]
        # Only the first one
        while word in text:
            text = text.replace(word, '', 1)
        final_result.append(text)
    final_result.sort() # Sort lexicographically earliest string
    return final_result[0]
    
#======== my attempt 
    
def answer(chunk, word):
    import re
    word_rev = word[::-1] #reverse of the Word
    if word in chunk:
        while ((word in chunk) or (word_rev in chunk[::-1])):
            org = re.sub(word , '', chunk)
            rev = re.sub(word_rev , '', chunk[::-1])[::-1]
            chunk = org
        final_result = min(org, rev) 
    else:
        final_result = chunk
    return(final_result)