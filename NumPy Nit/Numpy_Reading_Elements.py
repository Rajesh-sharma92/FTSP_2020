# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:25:25 2020

@author: Rajesh
"""

Numpy Reading Elements Into Matrix  :- 
----------------------------------
import numpy as np

m = int(input('Enter the no. of rows :'))
n = int(input('Enter the no. of columns :'))

matrix = np.ndarray(shape=(m,n) , dtype = int)
print('Enter the %d elemenenst of %d X %d matrix :' %(m*n , m,n))

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input())
        
print('%d X %d matrix is :' %(m,n))
print(matrix)
        
 ************* Result **************
 
 3 X 3 matrix is :
     
[[10 20 30]
 [40 50 60]
 [70 80 90]]


************* Result **************

4 X 3 matrix is :
    
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]