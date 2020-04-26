# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:32:08 2020

@author: Rajesh
"""
'''
NumPy Data Types :-
--------------------
'''
Data Types in Python :- 
------------------------
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. eg. "ABCD"
integer - used to represent integer numbers. eg. -1, -2, -3
float - used to represent real numbers. eg. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent a number in complex plain. eg. 1.0 + 2.0j, 1.5 + 2.5j

 
Data Types in NumPy :- 
-------------------------
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )


Checking the Data Type of an Array :- 
----------------------------------------
The NumPy array object has a property called dtype that returns the data type of the array:

Ex :- 

Get the data type of an array object:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr) # [1 2 3 4]

print(arr.dtype) # int32

Ex :- 

import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr) # ['apple' 'banana' 'cherry']

print(arr.dtype) # <U6

'''
Creating Arrays With a Defined Data Type :-
----------------------------------------------
We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:
'''

Ex :- 

Create an array with data type string:

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr) # [b'1' b'2' b'3' b'4']

print(arr.dtype) # |S1

Ex :- 

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype) # int32

arr = arr.astype(float)

print(arr.dtype) # float64

arr = arr.astype(int)

print(arr.dtype) # int32

Ex :- 

import numpy as np

arr = np.array([10,20,'Rajesh','forsk',101])

print(arr)

print(arr.dtype)

arr = arr.astype(str)

print(arr.dtype)


Ex :- 

import numpy as np

arr = np.arange(10)

print(arr) # [0 1 2 3 4 5 6 7 8 9]

print(arr.dtype) # int32

arr = arr.astype('f')

print(arr.dtype) # float32


Ex :- 

import numpy as np

arr = np.array([0,10,20,0,40,50,0] , dtype=bool)

print(arr) # [False  True  True False  True  True False]

print(arr.dtype) # bool


Ex :- 

import numpy as np

arr = np.array([1,2,3,4,5] , dtype='f')

print(arr) # [1. 2. 3. 4. 5.]

print(arr.dtype) # float32

-------------------------------------------------------------------------------------
COPY :- 
---------

Ex :- Make a copy, change the original array, and display both arrays.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()

arr[0] = 42

print(arr) # [42  2  3  4  5]

print(x) # [1 2 3 4 5]

Ex :- 

x[2] = 101

print(arr) # [1 2 3 4 5]

print(x) # [  1   2 101   4   5]


NOTE :- The copy SHOULD NOT be affected by the changes made to the original array.


VIEW :- 
-----------
Ex :- Make a view, change the original array, and display both arrays.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.view()

arr[0] = 42

print(arr) # [42  2  3  4  5]

print(x) # [42  2  3  4  5]

Ex :- 

x[3] = -2020

print(arr) # [   42     2     3 -2020     5]

print(x) # [   42     2     3 -2020     5]


NOTE :- The view SHOULD be affected by the changes made to the original array.


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()

y = arr.view()

print(x.base) # None

print(y.base) # [1 2 3 4 5]

NOTE :- The copy returns None.
The view returns the original array.


