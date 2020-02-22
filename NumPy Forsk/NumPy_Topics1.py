# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:09:36 2020

@author: Rajesh
"""
# NaN can be defined using the following constant.

import numpy as np


print (np.nan)
print(type(np.nan))
# Infinite value can be expressed using the following contant 
print (np.inf)
print(type(np.inf))


x = np.array( [1,2,3], dtype=np.float ) 
print (x)
print(x.dtype)


x[0] = np.nan
x[2] = np.inf
print (x)

print (np.isnan(x[0]))
print(np.isnan(x))

print (np.isinf(x[2]))
print(np.isinf(x))

-----------------------------------------------------------------------------------------------------------
"""
Arrays Operations - Basic operations apply element-wise. 
The result is a new array with the resultant elements.
Operations like *= and += will modify the existing array.
"""
import numpy as np
arr = np.arange(5) 
print('Array :', arr) # [0 1 2 3 4]

arr1 = np.arange(5) 
print('Array :', arr1) # [0 1 2 3 4]

array = np.array(list(zip(arr,arr1)))

print('Array :', array) 
print('Dimensions :', array.ndim) # 2
print('Shape :', array.shape) # (5,2)
print('DataType :', array.dtype) # int32
print('size :', array.size) # 10
print('Itemsize :', array.itemsize) # 4
print('Strides :', array.strides) # (8,4)


array = arr + arr1
print ('Array Addition :', array) # [0 2 4 6 8]

array = arr - arr1
print ('Array subtraction :', array) # [0 0 0 0 0]

array = arr * arr1
print ('Array Multiply :', array) # [ 0  1  4  9 16]

array = arr / arr1
print ('Array Division :', array) # [nan  1.  1.  1.  1.]

array = arr**3
print('Array :', array) # [ 0  1  8 27 64]
 
array = arr > 3
print('Array :', array) # [False False False False  True]
 
array = 10*np.sin(arr)
print('Array :', array) # [ 0.          8.41470985  9.09297427  1.41120008 -7.56802495]

--------------------------------------------------------------------------------------------------------



















































