# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 20:09:45 2024

twoSum but if theres multiple soln in array return the first one

@author: Kashyap
"""

def twoSum(arr, target):

    arrDict = {}    
    
    for ind, ele in enumerate(arr):
        diff = target-ele

        if diff in arrDict:
            return [arrDict[diff], ind]
        
        if arrDict.get(ele) != None:
            continue
        
        arrDict[ele] = ind

    return []

print(twoSum([2, 7, 11, 15], 9) == [0, 1])
print(twoSum([3, 2, 4], 6) == [1, 2])
print(twoSum([3, 3], 6) == [0, 1])
print(twoSum([3, 3, 6], 9) == [0,2])
print(twoSum([1, 2, 3, 4, 5], 9) == [3, 4])
print(twoSum([0, 4, 3, 0], 0) == [0, 3] )
print(twoSum([-3, 4, 3, 90], 0) == [0, 2])
print(twoSum([10, 10, 20, 10, 20], 30) == [0, 2])