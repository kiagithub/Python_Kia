# -*- coding: utf-8 -*-
"""
Created on Sat May 28 11:26:14 2016

@author: kia
"""


"""Kia: from the writing idiomic python, look at list1 that I generated,
imported math function and also how, list() works as an empty list, and then
we append elements to it

"""

list1 = list(range(1, 1000))

import math

def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append(element)

    return result_list

# not germane to the example, but here's a possible implementation of
# is_prime...

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False
    
    
 #==================================================   

"""
Project Euler #10 : 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Here we want to use Yield! as a generator
"""
def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1
        
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return
