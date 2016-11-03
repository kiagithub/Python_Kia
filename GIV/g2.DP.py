# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:30:12 2016

@author: kiawo

Pots of gold game: Two players A & B. There are pots of gold 
arranged in a line, each containing some gold coins (the players 
can see how many coins are there in each gold pot - perfect information). 
They get alternating turns in which the player can pick a pot from one of 
the ends of the line. The winner is the player which has 
a higher number of coins at the end. 
The objective is to "maximize" the number of coins collected by A, 
assuming B also plays optimally. A starts the game. 

The idea is to find an optimal strategy that makes A win 
knowing that B is playing optimally as well. How would you do that? 

"""
def max_coin(start, end):
    if start > end:
        return
    a = coins[start] + max_coin(start+1, end)
    b = coins[end] + max_coin(start, end-1)
    
    return max(a, b)
    
coins = [1,2,3,4,5,6,7,8,9,10]

#==============================

pots = [1,2,3,4,5,6,7,8,9,10]
 
cache = {}
def optimal(left, right, player):
    if left > right:
        return 0
    if (left, right, player) in cache:
        return cache[(left, right, player)]
    if player == 'A':
        result = max(optimal(left + 1, right, 'B') + pots[left],
                     optimal(left, right - 1, 'B') + pots[right])
    else:
        result = min(optimal(left + 1, right, 'A'),
                     optimal(left, right - 1, 'A'))
    cache[(left, right, player)] = result
    return result
 
answer = optimal(0, len(pots)-1, 'A')