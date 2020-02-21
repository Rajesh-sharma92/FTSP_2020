# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:45:30 2020

@author: Rajesh
"""

NumPy reshape :-
-------------
import numpy as np

my_list = [10,20,30,40,50,60]

arr = np.array(my_list)
print('The Array :', arr) # [10 20 30 40 50 60]
print('The size :', arr.size) # 6
print('The Dimensional :', arr.ndim) # 1
print('The dataType :', arr.dtype) # int32

print('******* After Reshaping the Array will ************')

res = arr.reshape(2,3)
print('The new Array :', res)
print('The Array :', res) 
print('The size :', res.size) # 6
print('The Dimensional :', res.ndim) # 2
print('The dataType :', res.dtype) # int32


print('******* After Reshaping the Array will ************')

res = arr.reshape(3,2)
print('The new Array :', res)
print('The Array :', res) 
print('The size :', res.size) # 6
print('The Dimensional :', res.ndim) # 2
print('The dataType :', res.dtype) # int32

-----------------------------------  RESULT  ---------------------------------------------------------

The Array : [10 20 30 40 50 60]
The size : 6
The Dimensional : 1
The dataType : int32
******* After Reshaping the Array will ************
The new Array : [[10 20 30]
 [40 50 60]]
The Array : [[10 20 30]
 [40 50 60]]
The size : 6
The Dimensional : 2
The dataType : int32
******* After Reshaping the Array will ************
The new Array : [[10 20]
 [30 40]
 [50 60]]
The Array : [[10 20]
 [30 40]
 [50 60]]
The size : 6
The Dimensional : 2
The dataType : int32
---------------------------------------------------------------------------------------------
import numpy as np

my_list = [10,20,30,40,50,60,70,80]

arr = np.array(my_list)
print('The Array :', arr) # [10 20 30 40 50 60]
print('The size :', arr.size) # 6
print('The Dimensional :', arr.ndim) # 1
print('The dataType :', arr.dtype) # int32

print('******* After Reshaping the Array will ************')

res = arr.reshape(2,2,2)
print('The new Array :', res)
print('The Array :', res) 
print('The size :', res.size) # 6
print('The Dimensional :', res.ndim) # 2
print('The dataType :', res.dtype) # int32


































