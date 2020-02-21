# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:51:36 2020

@author: Rajesh
"""

Numpy Multi Dimensional Arrays Defining :- 
---------------------------------------
import numpy as np

arr = np.ndarray(shape=(3,3,3,) , dtype = int)

print('Elements are :')
print('size :', arr.size) # size : 27
print('DataType :', arr.dtype) # DataType : int32
print('Shape :', arr.shape) # Shape : (3, 3, 3)
print('Dimnesional :', arr.ndim) # Dimnesional : 3
 
********** Result *************
Elements are :
    
size : 27
DataType : int32
Shape : (3, 3, 3)
Dimnesional : 3
--------------------------------------------------------------------------------------------
import numpy as np

arr = np.ndarray(shape=(3,3,3) , dtype = int)
# print('Enter %d elements :' %(arr.size)) # Enter 27 elements :
val = 1
x = arr.shape[0]
y = arr.shape[1]
z = arr.shape[2]

for i in range(x):
    for j in range(y):
        for k in range(z):
            arr[i][j][k] = val
            val = val + 1
            
print('The Elements are :\n', arr)            

*********** Result *********
Enter 27 elements :
The Elements are :
 [[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]
  [25 26 27]]]
----------------------------------------------------------------------------------------------
import numpy as np

arr = np.ndarray(shape=(4,3,3) , dtype = int)
# print('Enter %d elements :' %(arr.size)) # Enter 36 elements :
val = 1
x = arr.shape[0]
y = arr.shape[1]
z = arr.shape[2]

for i in range(x):
    for j in range(y):
        for k in range(z):
            arr[i][j][k] = val
            val = val + 1
            
print('The Elements are :\n', arr)            

*********** Result ****************

The Elements are :
    
 [[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]
  [25 26 27]]

 [[28 29 30]
  [31 32 33]
  [34 35 36]]] 
 
------------------------------------------------------------------------------------------
import numpy as np

arr = np.ndarray(shape=(2,2,2) , dtype = int)
print('Enter %d elements :' %(arr.size)) # Enter 8 elements :

x = arr.shape[0]
y = arr.shape[1]
z = arr.shape[2]

for i in range(x):
    for j in range(y):
        for k in range(z):
            arr[i][j][k] = int(input())
            
            
print('The Elements are :\n', arr)    

****** Result ***********
The Elements are :
    
 [[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]

------------------------------------------------------------------------------
import numpy as np

arr = np.ndarray(shape=(3,3,3) , dtype = int)
print('Enter %d elements :' %(arr.size)) # Enter 27 elements :

x = arr.shape[0]
y = arr.shape[1]
z = arr.shape[2]

for i in range(x):
    for j in range(y):
        for k in range(z):
            arr[i][j][k] = int(input())
            
            
print('The Elements are :\n', arr)    

****** Result ***********

The Elements are :
    
 [[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]
  [25 26 27]]]



 



























