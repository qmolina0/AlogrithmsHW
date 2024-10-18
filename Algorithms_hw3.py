#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:22:56 2024

@author: quentin
"""
def stairs_top_down(n: int, memo={}) -> int:
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return 1
    
    if n not in memo:
        memo[n] = stairs_top_down(n - 1, memo) + stairs_top_down(n - 2, memo)
    return memo[n]

print(stairs_top_down(15))
    
#%%

def stairs_bottom_up (n: int) -> int:
    
    if n == 0:
        return 0 
    if n == 1:
        return 1
    if n == 2: 
        return 2
    
    stairs = [0] * (n + 1)
    stairs[1] = 1
    stairs[2] = 2
    
    for i in range(3 , n + 1):
        stairs[i] = stairs[i - 1] + stairs[i - 2]
        
    return stairs[n]


print(stairs_bottom_up(15))


#%%

def fibonacci(n): 
    if n == 0:
        return 0 
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(15))

