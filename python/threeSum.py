# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:50:36 2024

Q. Given an array of integers, find all unique triplets (a, b, c) in the array such that their sum equals zero (a + b + c = 0).

Examples:
• Given an array: [1, 2, 0] returns: []
• Given an array: [-1, 0, 1, 0, 1] returns: [[-1, 0, 1]]
• Given an array: [-5, -1, 0, 1, 4, -1] returns: [[-5,1,4], [-1,0,1]]


@author: Kashyap
"""

def three_sum(arr, tar = 0):
    
    """
    if -(a+b) is not in a set, fails
    
    hash set of all digits
    
    
    
    """
    
    uniqueTriplets = [] #sorted solutions list
    
    for ind, a in enumerate(arr):
        
        for ind_b, b in enumerate(arr[(ind+1):]): #only look at things after a
        
            soln = tar-(a+b)
            sortedArr = sorted([a, b, soln]) #sort to avoid duplicates
            
            if (soln in arr[(ind+ind_b+2):]) and (sortedArr not in uniqueTriplets): 
                #only check elements in the array after location of b
                uniqueTriplets.append(sortedArr)
                
    return uniqueTriplets


#test cases

print(three_sum([-1, 0, 1, 0, 1]))
print(three_sum([-5, -1, 0, 1, 4, -1]))
print(three_sum([3, 3], 9))
print(three_sum([3, 3, 6, 1], 10))
print(three_sum([1, 2, 3, 4, 5], 12))
print(three_sum([0, 4, 3, 0, 0, -4, -7], 0)) 
print(three_sum([0, 4, 3, 0, 0], 3)) 
print(three_sum([-3, 4, 3, 0, 90], 0)) 