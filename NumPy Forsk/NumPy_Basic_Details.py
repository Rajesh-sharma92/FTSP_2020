# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:39:36 2020

@author: Rajesh
"""
# Numerical Python 
'''Introduction to NumPy'''

my_list = [0,1,2,3,4,5,6,7,8]
print (type(my_list))
print (my_list)  

# Convert your list data to NumPy arrays.
import numpy as np

arr = np.array(my_list)
print(type(arr)) # <class 'numpy.ndarray'>
print('Array :\n', arr) # [0 1 2 3 4 5 6 7 8] --> It always prints the values WITHOUT comma seperated , thats ndarray
------------------------------------------------------------------------------------------------
my_tuple = 10,20,30,40,50
print(type(my_tuple))
print(my_tuple)

# Convert your tuple  data to NumPy arrays.
import numpy as np

arr = np.array(my_tuple)
print(type(arr))
print('Array :\n', arr) # [10 20 30 40 50]. Array gives the result always into list but elements will separated by space.

---------------------------------------------------------------------------------------------
my_dict = {10:1 , 20:2 , 30:4 , 40:5,'Name':'Rajesh','Class':'Forsk'}
print(type(my_dict)) # <class 'dict'>
print(my_dict)

import numpy as np

arr = np.array(my_dict)
print(type(arr))
print('Array :\n', arr)

************* Result **************
Array :
 {10: 1, 20: 2, 30: 4, 40: 5, 'Name': 'Rajesh', 'Class': 'Forsk'}
---------------------------------------------------------------------------------------------
""" Ex :- Take a list and perfrom some of the operations. """

import numpy as np

my_list = [10,20,30,40,50,60,70,80,90,100]

arr = np.array(my_list)

print('Array :', arr) # [ 10  20  30  40  50  60  70  80  90 100]
print('size :', arr.size) # 10
print('DataType :',arr.dtype) # int32
print('Dimensions :', arr.ndim) # 1
print('Shape :', arr.shape) # (10,)
print('ItemSize :', arr.itemsize) # 4 . It always gives the 4 Bytes for each element.
print('No. of Bytes :', arr.nbytes) # 40
print('Strides :', arr.strides) # (4,) --> It always show that how the element will be going into next line.

# Array Indexing will always return the data type object.

print (arr[0]) # 10
print (arr[2]) # 30
print (arr[-1]) # 100

----------------------------------------------------------------------------------------------
import numpy as np

my_list = [10.5,20.5,30.1,80.2,75.0]
print(my_list)

arr = np.array(my_list)
print('Array :', arr) # [10.5 20.5 30.1 80.2 75. ]
print('size :', arr.size) # 5
print('DataType :', arr.dtype) # float64
print('Dimnesions :', arr.ndim) # 1
print('shape :', arr.shape) # (5,)
print('Itemsize :', arr.itemsize) # 8
print('No. of Byte: ', arr.nbytes) # 40
print('strides :', arr.strides) # (8,)

# Array Indexing will always return the data type object.

print(arr[3]) # 80.2
print(arr[-1]) # 75.0
print(arr[1]) # 20.5
-----------------------------------------------------------------------------------------------------

import numpy as np

my_list = ['Rajesh',10,20,30,'Sharma','Yogi',20.50,-30.5]
print(my_list)

arr = np.array(my_list)
print('Array :', arr) # ['Rajesh' '10' '20' '30' 'Sharma' 'Yogi' '20.5' '-30.5']
print('size :', arr.size) # 8
print('DataType :', arr.dtype) # <U6
print('Dimnesions :', arr.ndim) # 1
print('shape :', arr.shape) # (8,)
print('Itemsize :', arr.itemsize) # 24
print('No. of Byte: ', arr.nbytes) # 192
print('strides :', arr.strides) # (24,)

# Array Indexing will always return the data type object.

print(arr[3]) # 30
print(arr[-1]) # -30.5
print(arr[1]) # 10

-------------------------------------------------------------------------------------------------------
"""
Reshaping is changing the arrangement of items so that shape of the array changes
Flattening, however, will convert a multi-dimensional array to a flat 1d array. And not any other shape.
"""
NOTE :- There are 2 types of arranging the data into different Arrays.
Reshaping :- Convert from small to big data types.
Flattening :- Convert from big to  small data types.

# Reshaping to 2 Dimensional Array - 3 Rows and 3 Columns.

Ex :- For 2D Arrays :- for integer  number.

import numpy as np

my_list = [10,20,30,40,50,60,70,80]
arr = np.array(my_list)

print('Array :', arr) # [ 10  20  30  40  50  60  70  80 ]
print('size :', arr.size) # 8
print('DataType :', arr.dtype) # int32
print('Dimnesions :', arr.ndim) # 1
print('shape :', arr.shape) # (8,)
print('Itemsize :', arr.itemsize) # 4
print('No. of Byte: ', arr.nbytes) # 32
print('strides :', arr.strides) # (4,)

Case - 1 :- 
--------
res = arr.reshape(4,2)
print('The New Array :\n', res)
print('size :', res.size) # 8
print('DataType :', res.dtype) # int32
print('Dimnesions :', res.ndim) # 2
print('shape :', res.shape) # (4,2)
print('Itemsize :', res.itemsize) # 4
print('No. of Byte: ', res.nbytes) # 32
print('strides :', res.strides) # (8,4) --> It represent the one line how many bytes total bytes required for next line and then int/float. 

********* Result **********
The New Array : 
 [[10 20]
 [30 40]
 [50 60]
 [70 80]]
size : 8
DataType : int32
Dimnesions : 2
shape : (4, 2)
Itemsize : 4
No. of Byte:  32
strides : (8, 4)
-------------------------------------------------------------------------------------------------------
Case - 2 :-
--------
res = arr.reshape(2,4)
print('The New Array :\n', res)
print('size :', res.size) # 8
print('DataType :', res.dtype) # int32
print('Dimnesions :', res.ndim) # 2
print('shape :', res.shape) # (2,4)
print('Itemsize :', res.itemsize) # 4
print('No. of Byte: ', res.nbytes) # 32
print('strides :', res.strides) # (16,4) --> It represent the one line how many bytes total bytes required for next line and then int/float. 

********* Result **********
The New Array :
 [[10 20 30 40]
 [50 60 70 80]]
size : 8
DataType : int32
Dimnesions : 2
shape : (2, 4)
Itemsize : 4
No. of Byte:  32
strides : (16, 4)
--------------------------------------------------------------------------------------------------
Ex :- For 2D Arrays :- for Float number.
      -------------    
import numpy as np

my_list = [10.5,20.5,30.1,80.2,75.0,80.50] # 1-D Array.
print(my_list)

arr = np.array(my_list)
print('Array :', arr) # [10.5 20.5 30.1 80.2 75. 80.50]
print('size :', arr.size) # 6
print('DataType :', arr.dtype) # float64
print('Dimnesions :', arr.ndim) # 1
print('shape :', arr.shape) # (6,)
print('Itemsize :', arr.itemsize) # 8
print('No. of Byte: ', arr.nbytes) # 48
print('strides :', arr.strides) # (8,)

Case - 1 :- 
--------
res = arr.reshape(3,2)
print('The New Array :\n', res)
print('size :', res.size) # 6
print('DataType :', res.dtype) # float64
print('Dimnesions :', res.ndim) # 2
print('shape :', res.shape) # (3,2)
print('Itemsize :', res.itemsize) # 8
print('No. of Byte: ', res.nbytes) # 48
print('strides :', res.strides) # (16,8) --> It represent the one line how many bytes total bytes required for next line and then int/float. 

************ Result **********
The New Array :
 [[10.5 20.5]
 [30.1 80.2]
 [75.  80.5]]
size : 6
DataType : float64
Dimnesions : 2
shape : (3, 2)
Itemsize : 8
No. of Byte:  48
strides : (16, 8)
----------------------------------------------------------------------------------------------------
Case - 2 :- 
--------
res = arr.reshape(2,3)
print('The New Array :\n', res)
print('size :', res.size) # 6
print('DataType :', res.dtype) # float64
print('Dimnesions :', res.ndim) # 2
print('shape :', res.shape) # (2,3)
print('Itemsize :', res.itemsize) # 8
print('No. of Byte: ', res.nbytes) # 48
print('strides :', res.strides) # (24,8) --> It represent the one line how many bytes total bytes required for next line and then int/float. 

************ Result **********
The New Array :
 [[10.5 20.5 30.1]
 [80.2 75.  80.5]]
size : 6
DataType : float64
Dimnesions : 2
shape : (2, 3)
Itemsize : 8
No. of Byte:  48
strides : (24, 8)

----------------------------------------------------------------------------------------------------
"""
For 1D array, shape return a  tuple with only 1 component (i.e. (n,))
For 2D array, shape return a  tuple with only 2 components (i.e. (n,m))
For 3D array, shape return a  tuple with only 3 components (i.e. (n,m,k) )
"""


























































 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 



















