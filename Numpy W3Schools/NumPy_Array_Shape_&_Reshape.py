# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:00:13 2020

@author: Rajesh
"""
'''
NumPy Array Shape & Reshape :- 
------------------------------
'''
Shape of an Array
The shape of an array is the number of elements in each dimension.

Get the Shape of an Array :- 
---------------------------
NumPy arrays have an attribute called shape that returns a tuple with each index having 
the number of corresponding elements.

Ex :- 

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr.ndim) # 1

print(arr.shape) # (5,)

Ex :- 

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
---------
[[1 2 3 4]
 [5 6 7 8]]

print(arr.shape) # (2, 4)

arr = np.array([['Rajesh','forsk'] , ['school','sharma']])

print(arr)
--------
[['Rajesh' 'forsk']
 ['school' 'sharma']]

print(arr.shape) # (2, 2)

print(arr.ndim) # 2

Ex :- Create the array with the 3-D.

import numpy as np

arr = np.array([1, 2, 3, 4 ,5], ndmin=3)

print(arr) # [[[1 2 3 4 5]]]

print('shape of array :', arr.shape)
-------------
shape of array : (1, 1, 5)

print(arr.ndim) # 3


Ex :- Create the array with the 5-D.

import numpy as np

arr = np.array([1, 2, 3, 4 ,5], ndmin=5)

print(arr) # [[[[[1 2 3 4 5]]]]]

print('shape of array :', arr.shape)
-------------
shape of array : (1, 1, 1, 1, 5)

print(arr.ndim) # 5

---------------------------------------------------------------------------------------------

Reshaping arrays :- 
-------------------
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.

Ex :- 

Reshape From 1-D to 2-D :- 
---------------------------
Ex :- 

Convert the following 1-D array with 12 elements into a 2-D array.

The outermost dimension will have 4 arrays, each with 3 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
---------------------
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

Ex :- 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(3,4)

print(newarr)
---------------------
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Ex :- 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(6,2)

print(newarr)
---------------------
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]
 [11 12]]

Ex :- 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2,6)

print(newarr)
---------------------
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]

'''
Reshape From 1-D to 3-D :- 
---------------------------
'''

Ex :- 

Convert the following 1-D array with 12 elements into a 3-D array.

The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
-----------
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
    
print(newarr.ndim) # 3

'''
Can We Reshape Into any Shape? :- 
--------------------------------
Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):
'''
Ex :- 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3) # There will be an error.

print(newarr)

'''
Returns Copy or View ? :- 
-------------------------
'''

Ex :- 

Check if the returned array is a copy or a view:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4))
-----------------
[[1 2 3 4]
 [5 6 7 8]]

print(arr.reshape(2,4).base) # [1 2 3 4 5 6 7 8]

NOTE :- The example above returns the original array, so it is a view.

Ex :- Convert 1D array with 8 elements to 3D array with 2x2 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)
--------------
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]

print(newarr.ndim) # 3


NOTE :- We can not pass -1 to more than one dimension.

'''
Flattening the arrays :- 
------------------------
Flattening array means converting a multidimensional array into a 1D array.
'''

We can use reshape(-1) to do this.

Ex :- 

Convert the array into a 1D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
---------
[[1 2 3]
 [4 5 6]]

print(arr.ndim) # 2

newarr = arr.reshape(-1)

print(newarr) # [1 2 3 4 5 6]

print(newarr.ndim) # 1



