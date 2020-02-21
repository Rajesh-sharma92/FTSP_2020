# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:28:46 2020

@author: Rajesh
"""
"""
For 1D array, shape return a  tuple with only 1 component (i.e. (n,))
For 2D array, shape return a  tuple with only 2 components (i.e. (n,m))
For 3D array, shape return a  tuple with only 3 components (i.e. (n,m,k) )
"""
"""
There are a couple of mechanisms for creating arrays in NumPy:
 a. Conversion from other Python structures (e.g., lists, tuples).
 b. Built-in NumPy array creation (e.g., arange, ones, zeros, etc.).
 c. Reading arrays from disk, either from standard or custom formats 
     (e.g. reading from a CSV file).
"""
# Using the built in function arange 

NOTE :- Arange function will generate array from 0 to size-1 
NOTE :- arange is similar to range function but generates an array , 
NOTE :- where in range gives you a list of elements.

import numpy as np

arr = np.arange(20 , dtype = int) 
print ('Array :\n', arr) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print ('Dimensions :', arr.ndim) # 1
print ('Shape :', arr.shape) # (20,)
print ('DataType :', arr.dtype) # int32
print ('Item Size :', arr.itemsize) # 4
print('strides :', arr.strides) # (4,)

************ Result **************

Array :
 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
Dimensions : 1
Shape : (20,)
DataType : int32
Item Size : 4
strides : (4,)

-----------------------------------------------------------------------------------------------
import numpy as np

n = int(input('Enter n size :'))
arr = np.ndarray(shape=(n) , dtype = int)
for i in range(n):
    arr[i] = int(input())

print ('Array :\n', arr) # [ 1  2  3  4  5  6 ]
print ('Dimensions :', arr.ndim) # 1
print ('Shape :', arr.shape) # (6,)
print ('DataType :', arr.dtype) # int32
print ('Item Size :', arr.itemsize) # 4
print('strides :', arr.strides) # (4,)

************ Result **************
Array :
 [1 2 3 4 5 6]
Dimensions : 1
Shape : (6,)
DataType : int32
Item Size : 4
strides : (4,)

--------------------------------------------------------------------------------------------------------
# zeros(shape) -- creates an array filled with 0 values with the specified shape.
# The default dtype is float64.

import numpy as np

arr = np.zeros((3, ))
print ('Array :\n', arr) # [0.  0. 0.]
print ('Dimensions :', arr.ndim) # 1
print ('Shape :', arr.shape) # (3,)
print ('DataType :', arr.dtype) # float64
print ('Item Size :', arr.itemsize) # 8
print('strides :', arr.strides) # (8,)

******** Result *************
Array :
 [0. 0. 0.]
Dimensions : 1
Shape : (3,)
DataType : float64
Item Size : 8
strides : (8,)
-----------------------------------------------------------------------------------------
import numpy as np

arr = np.ones((5, ))
print ('Array :\n', arr) # [1. 1. 1. 1. 1.]
print ('Dimensions :', arr.ndim) # 1
print ('Shape :', arr.shape) # (5,)
print ('DataType :', arr.dtype) # float64
print ('Item Size :', arr.itemsize) # 8
print('strides :', arr.strides) # (8,)

******** Result *************
Array :
 [1. 1. 1. 1. 1.]
Dimensions : 1
Shape : (5,)
DataType : float64
Item Size : 8
strides : (8,)
----------------------------------------------------------------------------------------------------
arr = np.zeros((3, 3))
print ('Array :\n', arr) 
print ('Dimensions :', arr.ndim) # 2
print ('Shape :', arr.shape) # (3,3)
print ('DataType :', arr.dtype) # float64
print ('Item Size :', arr.itemsize) # 8
print('strides :', arr.strides) # (24,8)

******** Result *************
Array :
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
Dimensions : 2
Shape : (3, 3)
DataType : float64
Item Size : 8
strides : (24, 8)
---------------------------------------------------------------------------------------------------
arr = np.zeros((3, 3, 3))
print ('Array :\n', arr) 
print ('Dimensions :', arr.ndim) # 3
print ('Shape :', arr.shape) # (3,3,3)
print ('DataType :', arr.dtype) # float64
print ('Item Size :', arr.itemsize) # 8
print('strides :', arr.strides) # (72,24,8)

******** Result *************

Array :
 [[[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]

 [[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]

 [[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]]
Dimensions : 3
Shape : (3, 3, 3)
DataType : float64
Item Size : 8
strides : (72, 24, 8)
------------------------------------------------------------------------------------------------------
# ones(shape) -- creates an array filled with 1 values. 

import numpy as np 
x = np.ones((3, ), dtype=np.int8 )
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.itemsize)

x = np.ones((3, 3), dtype=np.int8 )
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)


x = np.ones((3, 3, 3), dtype=np.int8 )
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
-------------------------------------------------------------------------------------------------------
# linspace() -- creates arrays with a specified number of elements, 
# and spaced equally between the specified beginning and end values.

import numpy as np 
arr = np.linspace(1, 4, 10, dtype = np.float) # try with float16,float32,float64
print ('Array :\n', arr) 
print ('Dimensions :', arr.ndim) # 1
print ('Shape :', arr.shape) # (10,)
print ('DataType :', arr.dtype) # float64
print ('Item Size :', arr.itemsize) # 8
print('strides :', arr.strides) # (8,)

************* Result ******************

Array :
 [1.         1.33333333 1.66666667 2.         2.33333333 2.66666667
 3.         3.33333333 3.66666667 4.        ]
Dimensions : 1
Shape : (10,)
DataType : float64
Item Size : 8
strides : (8,)

----------------------------------------------------------------------------------------------------
import numpy as np 
#random.random(shape) – creates arrays with random floats over the interval [0,1].
arr = np.random.random((2,3))*100
print ('Array :\n', arr) 
print ('Dimensions :', arr.ndim) # 2
print ('Shape :', arr.shape) # (2,3)
print ('DataType :', arr.dtype) # float64
print ('Item Size :', arr.itemsize) # 8
print('strides :', arr.strides) # (24,8)

************* Result ******************
Array :
 [[38.17219358 40.1656143  39.86705903]
 [18.51840201 47.19243198 42.82629506]]
Dimensions : 2
Shape : (2, 3)
DataType : float64
Item Size : 8
strides : (24, 8)
---------------------------------------------------------------------------------------------------------
NOTE :- np.identity() to create a square 2d array with 1's across the diagonal.

import numpy as np

arr = np.identity(n = 5)   # Size of the array
print ('Array :\n', arr) 
print ('Dimensions :', arr.ndim) # 2
print ('Shape :', arr.shape) # (5,5)
print ('DataType :', arr.dtype) # float64
print ('Item Size :', arr.itemsize) # 8
print('strides :', arr.strides) # (40,8)

************* Result ******************
Array :
 [[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
Dimensions : 2
Shape : (5, 5)
DataType : float64
Item Size : 8
strides : (40, 8)
------------------------------------------------------------------------------------------------------
NOTE :- np.eye() to create a 2d array with 1's across a specified diagonal
import numpy as np

arr = np.eye(N = 3,  # Number of rows
       M = 5,  # Number of columns
       k = 1)  # Index of the diagonal (main diagonal (0) is default)
print ('Array :\n', arr) 
print ('Dimensions :', arr.ndim) # 2
print ('Shape :', arr.shape) # (3,5)
print ('DataType :', arr.dtype) # float64
print ('Item Size :', arr.itemsize) # 8
print('strides :', arr.strides) # (40,8)

************* Result ******************
Array :
 [[0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]]
Dimensions : 2
Shape : (3, 5)
DataType : float64
Item Size : 8
strides : (40, 8)
----------------------------------------------------------------------------------------------------






























































































































































