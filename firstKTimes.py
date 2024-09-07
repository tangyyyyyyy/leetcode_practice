# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:31:29 2024

Q. Given an array of positive integers, find the first element that occurs k number of times. 
If no element occurs k times, return -1, and you may assume k is greater than 0. 

Examples:
• Given an array: [1, 2, 2, 3, 3], k: 2 // returns 2
• Given an array: [], k: 1 // returns -1

@author: Kashyap
"""


"""
APPROACH:
    1. Track counts of each digit in a dictionary
    2. Every iteration, add a count to the digit and check if count>k
    
TIME:
    1. For loop at most n (O(n))
    2. dictionary update (hash table look up O(1))
    3. early escape criteria: return immediately when digit is found

"""


def firstKTimes(arr, k):
    
    intCounter = {} #dictionary full of digits
     
    for digit in arr:

        intCounter[digit] = intCounter.get(digit, 0) + 1
        if intCounter[digit] == k:
            return digit
    
    return -1

print(firstKTimes([1, 2, 2, 3, 3], 2)) # 2
print(firstKTimes([1, 42, 42, 42, 3], 3)) # -1
print(firstKTimes([], 1)) # -1