# -*- coding: utf-8 -*-
"""
Created on Sun May 29 20:48:57 2016

@author: kia
"""

""" Challenge 1 """
    
def answer(x):
    level = x+1
    sum =0
    for i in range(level):
        sum = 7**i+ sum    
    #sum = sum +1
    
    return(sum)
    
""" Challenge 2 """

interval = [[10,14],[4,18],[19,20],[19,20],[13,20]]    


def answer(interval):
    start=[]
    end=[]
    for element in range(len(interval)):
        start.append(interval[element][0])
        end.append(interval[element][1])
    stmin = min(start)
    stmax = max(end)
    
    return(stmax-stmin)
    
""" Challenge 3 """
import string

names = ['annie', 'bonnie', 'liz']
names1 = ['kia', 'ali', 'zizo']
names2 = ['al', 'cj']
names3 = ['al','cj', 'bi']

def answer(names):   
    name_num = []
    name_dict = {}
    final_list = []
    chrnum = [ord(x.lower())-96 for x in string.ascii_lowercase]
    """chrnum = [ord(x.lower())-96 for x in string.lowercase] #in Python 2.7 """
    chrl = [x for x in string.ascii_lowercase]
    ref = dict(zip(chrl, map(int, chrnum)))
    for name in names:
        total = 0
        for letter in name:
            total = total + ref[letter]  
            
        if total in name_num:
            name_dict[total].append(name)
        
        else:
            name_num.append(total)
            name_dict[total]= [name]
    
    k = sorted(name_dict, reverse = True)
    for key in k:
        final_list.append(name_dict.get(key)) 
    for item in final_list:
        item.sort(reverse = True)
    final_list = [item for sublist in final_list for item in sublist]   # making a nestted list flat 
    return(final_list)