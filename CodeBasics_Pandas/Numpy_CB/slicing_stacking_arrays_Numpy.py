# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:23:26 2020

@author: Rajesh
"""

slicing/stacking arrays, indexing with boolean arrays : -
-------------------------------------------------------
import numpy as np

n = [6,7,8,9]

n[1] # 7

n[-1] # 9

n[1:3] # [7,8]

a = np.array([6,7,8,9])

a[0] # 6

a[-2] # 8

a[1:3] # [7,8]

NOTE :- Here we can see that Python basic list and Numpy arrays are almost same.

# If we have values into multidimensional then how to slicing the values.
a = np.array([[6,7,8],[1,2,3],[9,3,2]])
a
---
array([[6, 7, 8],
       [1, 2, 3],
       [9, 3, 2]])

a[1,2] # 3 , # Here 1,2 Means Row , column like first row & 2nd column.

te 
a[0:2,2] # [8,3]

a[1: , 0] # [1,9]

a[-1] # [9, 3, 2]

a[0: , -1] # [8, 3, 2]

a[-1,0:2] # [9, 3]

a[:,1:3]
----
([7, 8],
[2, 3],
[3, 2]])


a[:,1:]
------
([[7, 8],
[2, 3],
[3, 2]])

# If we want to get values through any loop then we should use the for loop.

a = np.array([[6,7,8],[1,2,3],[9,3,2]])

# We will just iterate the row-wise values.
for row in a:
    print(row)
-----
[6 7 8]
[1 2 3]
[9 3 2]

# Now we use the flatting here.
# Numpy has one method is called as flat.
for cell in a.flat:
    print(cell)
-----    
6
7
8
1
2
3
9
3
2

-----------------------------------------------------------------------------------------

Stacking two arrays Together :- 
----------------------------
import numpy as np

a = np.arange(6).reshape(3,2)
----
array([[0, 1],
       [2, 3],
       [4, 5]])
    
b = np.arange(6,12).reshape(3,2)    
---
array([[ 6,  7],
       [ 8,  9],
       [10, 11]])
    
# If we want to stack them together.
# We have one method is called as np.vstack((a,b))
np.vstack((a,b))
-----
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11]])

np.hstack((a,b))    
-----
array([[ 0,  1,  6,  7],
       [ 2,  3,  8,  9],
       [ 4,  5, 10, 11]])
    


a = np.arange(30).reshape(2,15)    
------
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])

np.hsplit(a,3)    
---------
[array([[ 0,  1,  2,  3,  4],
        [15, 16, 17, 18, 19]]), array([[ 5,  6,  7,  8,  9],
        [20, 21, 22, 23, 24]]), array([[10, 11, 12, 13, 14],
        [25, 26, 27, 28, 29]])]
    
# Here we are not able to visualise properly so we will store this Array into a variable.
result = np.hsplit(a,3)
result[0]    
-----
array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]])
    
result[1]    
-------
array([[ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24]]
    
result[2]
-----
array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])


result = np.vsplit(a,2)    
-------
[array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]]),
 array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])]

result[0]
------
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]])

result[1]
------
array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])


'''
indexing with boolean arrays :- 
------------------------------
'''    
a = np.arange(12).reshape(3,4)   
----
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

b = a > 4
b 
----
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]])

a[b]
-----
[ 5,  6,  7,  8,  9, 10, 11]

# If we want to replace greater than 4 elements with -1.
a[b] = -1
-----
array([[ 0,  1,  2,  3],
       [ 4, -1, -1, -1],
       [-1, -1, -1, -1]])

a[b] = 100
-----
array([[  0,   1,   2,   3],
       [  4, 100, 100, 100],
       [100, 100, 100, 100]])

