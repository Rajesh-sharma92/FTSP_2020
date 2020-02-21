# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:15:31 2020

@author: Rajesh
"""
How to create the numpy.ndarray :- 
-------------------------------
We can create the 1-dimnesional array :- 
-------------------------------------
import numpy as np

arr = np.ndarray(shape=(5), dtype = int)

print('size :', arr.size)
print('dimension :', arr.ndim)
print('shape :', arr.shape)
print('Data Type :', arr.dtype)

-------------------------------------------------------------------------------
import numpy as np

n = int(input('Enter the value of n :'))
arr = np.ndarray(shape=(n), dtype = int)

print('size :', arr.size)
print('dimension :', arr.ndim)
print('shape :', arr.shape)
print('Data Type :', arr.dtype)

---------------------------------------------------------------------------------------

import numpy as np

arr = np.ndarray(shape=(5) , dtype = int)

n = arr.size
print('Enter %d elements :' %n) # NOTE :- here n value is 5 and it will be taking place of %d = 5
for i in range(n): # 0,1,2,3,4. coz n = 5 then size = (n-1) = 4. 
    arr[i] = int(input())
print('The Elements are :', arr)    

print('Size :', arr.size)
print('Dimension :', arr.ndim)
print('Data Type :', arr.dtype)
print('shape :', arr.shape)
    
**************** Result **************

The Elements are : [10 20 30 40 50]
Size : 5
Dimension : 1
Data Type : int32
shape : (5,)


----------------------------------------------------------------------------------------------
import numpy as np

arr = np.ndarray(shape=(5) , dtype = float)

n = arr.size
print('Enter %d elements :' %n) # NOTE :- here n value is 5 and it will be taking place of %d = 5
for i in range(n): # 0,1,2,3,4. coz n = 5 then size = (n-1) = 4. 
    arr[i] = float(input())
print('The Elements are :', arr)    

print('Size :', arr.size)
print('Dimension :', arr.ndim)
print('Data Type :', arr.dtype)
print('shape :', arr.shape)


**************** Result **************

The Elements are : [ 10.   20.   30.   40.5 100.2]
Size : 5
Dimension : 1
Data Type : float64
shape : (5,)




















