#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:12:33 2024

@author: quentin
"""

"Question 1"
arr = [-1, -5, -3, -9, -2]  

def find_max(arr):
    highest = arr[0]
    for i in arr:
        if i > highest:
            highest = i
    return highest
    
print(find_max(arr)) # Output should be 9

"Question 2"
# with help from https://www.geeksforgeeks.org/binary-search/

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = int(input("Enter target number: "))

def binarySearch(target, arr2):
    
    x = 0
    low = 0
    high = len(arr2) - 1

    while (low <= high):
        
        x = low + (high - low) // 2 
        
        if (arr2[x] == target):
            return arr2[x]
            
        if (arr2[x] > target):
            high = x - 1
            
        if (arr2[x] < target):
            low = x + 1 
        
    return -1

print(binarySearch(target, arr2)) # Output should be 3

