# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:35:56 2020

@author: Rajesh
"""

# Reshaping to 3 Dimensional Arry -  3 layers of 3 Rows and 3 Columns 
import numpy as np

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27] 
arr = np.array(my_list)

print('Array :', arr) # [1 to 27]
print('size :', arr.size) # 27
print('DataType :',arr.dtype) # int32
print('Dimensions :', arr.ndim) # 1
print('Shape :', arr.shape) # (27,)
print('ItemSize :', arr.itemsize) # 4 . It always gives the 4 Bytes for each element.
print('No. of Bytes :', arr.nbytes) #  108
print('Strides :', arr.strides) # (4,)       

NOTE :- How we can convert into from 1D to 3D Array.

Case -1 :- From from 1D to 3D Array :- 
-----------------------------------
import numpy as np

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27] 
arr = np.array(my_list)

res = arr.reshape(3,3,3)
print('The New Array :\n', res)
print('size :', res.size) # 27
print('DataType :',res.dtype) # int32
print('Dimensions :', res.ndim) # 3
print('Shape :', res.shape) # (3,3,3)
print('ItemSize :', res.itemsize) # 4 . It always gives the 4 Bytes for each element.
print('No. of Bytes :', res.nbytes) #  108
print('Strides :', res.strides) # (36,12,4)

************ Result *************
The New Array :
 [[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]
  [25 26 27]]]
size : 27
DataType : int32
Dimensions : 3
Shape : (3, 3, 3)
ItemSize : 4
No. of Bytes : 108
Strides : (36, 12, 4)

------------------------------------------------------------------------------------------------
import numpy as np

my_list = [10,20,30,40,50,60,70,80]

arr = np.array(my_list)
print('Array :', arr) # [10 20 30 40 50 60 70 80]
print('size :', arr.size) # 8
print('DataType :',arr.dtype) # int32
print('Dimensions :', arr.ndim) # 1
print('Shape :', arr.shape) # (8,)
print('ItemSize :', arr.itemsize) # 4 . It always gives the 4 Bytes for each element.
print('No. of Bytes :', arr.nbytes) #  32
print('Strides :', arr.strides) # (4,)       

NOTE :- How we can convert into from 1D to 3D Array.

Case -1 :- From from 1D to 3D Array :- 
-----------------------------------

import numpy as np

my_list = [10,20,30,40,50,60,70,80]

arr = np.array(my_list)

res = arr.reshape(2,2,2)
print('The New 3-D Array :\n', res)
print('size :', res.size) # 8
print('DataType :',res.dtype) # int32
print('Dimensions :', res.ndim) # 3
print('Shape :', res.shape) # (2,2,2)
print('ItemSize :', res.itemsize) # 4 . It always gives the 4 Bytes for each element.
print('No. of Bytes :', res.nbytes) # 32
print('Strides :', res.strides) # (16,8,4)

************ Result *************
The New 3-D Array :
 [[[10 20]
  [30 40]]

 [[50 60]
  [70 80]]]
size : 8
DataType : int32
Dimensions : 3
Shape : (2, 2, 2)
ItemSize : 4
No. of Bytes : 32
Strides : (16, 8, 4)
-------------------------------------------------------------------------------------------------------











































































