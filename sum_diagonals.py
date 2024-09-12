# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:38:18 2024
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Example(s)
Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Element mat[1][1] = 5 is counted only once.
@author: Kashyap
"""

def diagonalSum(mat):
    
    sum_d = 0
    for ind, row in enumerate(mat): # add up all the diagonal elements, going row by row
        sum_d = sum_d + row[ind] + row[-ind] 
        
    if (len(mat) % 2 == 1): #subtract the center number if its added twice
        center_index = int(len(mat)/2)
        sum_d = sum_d - mat[center_index][center_index]
        
    return sum_d



mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(diagonalSum(mat) == 25)

mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]
print(diagonalSum(mat) == 8)

mat = [[5]]
print(diagonalSum(mat) == 5)

mat = []
print(diagonalSum(mat) == 0)
    