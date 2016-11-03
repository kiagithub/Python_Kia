# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:59:09 2016

@author: kiawo

There is an island which is represented by square matrix NxN. 
A person on the island is standing at any given co-ordinates (x,y). 
He can move in any direction one step right, left, up, down on the island. 
If he steps outside the island, he dies. 

Let island is represented as (0,0) to (N-1,N-1) (i.e NxN matrix) & 
person is standing at given co-ordinates (x,y). He is allowed to 
move n steps on the island (along the matrix). 
What is the probability that he is alive after he walks n steps on the island? 

Write a psuedocode & then full code for function 
" float probabilityofalive(int x,int y, int n) ".

more info: https://careercup.com/question?id=15556758


"""
def pOfLiveStraight(x, y, step, N):
    if x < 0 or x > N or y < 0 or y > N: return ("out of grid!")
    return ((1/4)*((step<(N-x+1)) + (step<x+1) + (step<(N-y+1)) + (step<y+1)))
    
def pOfLive(x, y, step, N):
    cache = {}
    if x < 0 or x > N or y < 0 or y > N: 
        return ("out of grid!")
    if step ==0: 
        return 1
    if (x, y, step, N) in cache:
        return cache[(x, y, step, N)]
    p = 0
    
    if x>0:
        p += 0.25 * pOfLive(x-1, y, step-1, N)
    if x<N-1:
        p += 0.25 * pOfLive(x+1, y, step-1, N)
    if y>0:
        p += 0.25 * pOfLive(x, y-1, step-1, N)
    if y<N-1:
        p += 0.25 * pOfLive(x, y+1, step-1, N)
        
    cache[(x, y , step, N)] = p
    
    return p
    
answer = pOfLive(0,0,6,10)
    
        
        
        
