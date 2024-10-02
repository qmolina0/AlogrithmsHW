#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:37:45 2024

@author: quentin
"""
def merge_sorted_arrays(arr1 , arr2):
    sort = []
    count1 = 0
    count2 = 0
    
    while count1 != len(arr1) and count2 != len(arr2): 
        
        if arr1[count1] < arr2[count2]:
            sort.append(arr1[count1])
            count1 += 1
            
        elif arr1[count1] > arr2[count2]:
            sort.append(arr2[count2])
            count2 += 1
            
        elif arr1[count1] == arr2[count2]:
            sort.append(arr1[count1])
            sort.append(arr2[count2])
            count1 += 1
            count2 += 1
            
        if count1 >= len(arr1):
            for i in range(count2, len(arr2)):
                sort.append(arr2[i])
        if count2 >= len(arr2):
            for i in range(count1, len(arr1)):
                sort.append(arr1[i])
            
    return sort


# merge_sort() function from https://www.codecademy.com/learn/sorting-algorithms-python/modules/merge-sort-python/cheatsheet
def merge_sort(lst):
  if len(lst) <= 1:
    return lst
  middle = len(lst) // 2
  left = lst[:middle]
  right = lst[middle:]
  sleft = merge_sort(left)
  sright = merge_sort(right)
  return merge_sorted_arrays(sleft, sright)


#print statements

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

print(merge_sorted_arrays(arr1, arr2))


arr = [38, 27, 43, 3, 9, 82, 10]
arr2 = [54, 34, 97, 45, 234, 0]

print(merge_sort(arr))
print(merge_sort(arr2))



