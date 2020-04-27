# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:16:44 2020

@author: Rajesh
"""
'''
NumPy Array Iterating :- 
----------------------
'''
Iterating Arrays :- 
--------------------
Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through each element one by one.

Ex :- 

import numpy as np

arr = np.array([1,2,3,4,5,6])

#print(arr) # [1 2 3 4 5 6]

for x in arr:
    print(x)
-------
1
2
3
4
5
6

Ex :- 

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

print(arr) # [1 2 3 4 5 6]

for x in arr:
    print(x)
---------
[1 2 3]
[4 5 6]


Ex :- Iterate on each scalar element of the 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
------------
1
2
3
4
5
6

--------------------------------------------------------------------------------------------------------
'''
NumPy Joining Array :- 
----------------------
'''
Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, 
along with the axis. If axis is not explicitly passed, it is taken as 0.

Ex :- Join two arrays

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr) # [1 2 3 4 5 6]

print(arr.shape) # (6,)

print(arr.ndim) # 1

Ex :- 

Join two 2-D arrays along rows (axis=1):

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
---------
[[1 2 5 6]
 [3 4 7 8]]

print(arr.shape) # (2,4)

print(arr.ndim) # 2


Ex :- 

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
-------
[[1 4]
 [2 5]
 [3 6]]

print(arr.shape) # (3,2)

print(arr.ndim) # 2

'''
Stacking Along Rows :-
----------------------
NumPy provides a helper function: hstack() to stack along rows.
'''

Ex :- 

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr) # [1 2 3 4 5 6]

print(arr.shape) # (6,)

print(arr.ndim) # 1

Ex :- 

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
-------
[[1 2 3]
 [4 5 6]]

print(arr.shape) # (2,3)

print(arr.ndim) # 2

'''
Stacking Along Height (depth) :- 
-----------------------------------
NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
'''

Ex :- 

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)
---------
[[[1 4]
  [2 5]
  [3 6]]]

print(arr.shape) # (1,3,2)

print(arr.ndim) # 3



