# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:36:19 2024

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

[-1, 0], target = -1

@author: Kashyap
"""


def twoSum(arr, target):

    arrDict = {}    
    
    for ind, ele in enumerate(arr):
        diff = target-ele
        
        if diff in arrDict:
            return [arrDict[diff], ind]
        
        arrDict[ele] = ind

    return []

print(twoSum([2, 7, 11, 15], 9) == [0, 1])
print(twoSum([3, 2, 4], 6) == [1, 2])
print(twoSum([3, 3], 6) == [0, 1])
print(twoSum([1, 2, 3, 4, 5], 9) == [3, 4])
print(twoSum([0, 4, 3, 0], 0) == [0, 3] )
print(twoSum([-3, 4, 3, 90], 0) == [0, 2])

