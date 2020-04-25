# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:20:02 2020

@author: Rajesh
"""

NOTE :- NumPy is a python library used for working with arrays.
NOTE :- It also has functions for working in domain of linear algebra, fourier transform, 
and matrices.
NOTE :- NumPy stands for Numerical Python.

'''
Why Use NumPy ?  :- 
--------------
'''

1) In Python we have lists that serve the purpose of arrays, but they are slow to process.

2) NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.

3) The array object in NumPy is called ndarray, it provides a lot of supporting functions that
   make working with ndarray very easy.

4) Arrays are very frequently used in data science, where speed and resources are very important.

'''
Why is NumPy Faster Than Lists? :- 
------------------------------------
'''

NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

'''
How to install the Numpy into Spyder :- 
-----------------------------------------
'''
pip install numpy 

It is used to install it the numpy and use it.

NOTE :- We want to remove it from your system then what we should it.

pip uninstall numpy 

NOTE :- We have the one thing and we can check that particular package is installed or not.

pip list 

NOTE :- If we want to check the version of the Numpy ?

import numpy as np 
print('The Current Version of Numpy :', np.__version__)
# The Current Version of Numpy : 1.16.5

Ex :- 

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr) # [10 20 30 40 50]

arr # array([10, 20, 30, 40, 50])


'''
Create a NumPy ndarray Object :-
----------------------------------
'''
NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.

Ex :- 

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr) # [1 2 3 4 5]

print(type(arr)) # <class 'numpy.ndarray'>

print(arr.ndim) # 1

print(arr.size) # 5

print(arr.shape) # (5,)

NOTE :- To create an ndarray, we can pass a list, tuple or any array-like object into the 
array() method, and it will be converted into an ndarray.

Ex :- Use a tuple to create a NumPy array.

import numpy as np

arr = np.array((10,'Rajesh','sharma',20))

print(arr) # ['10' 'Rajesh' 'sharma' '20']

arr # array(['10', 'Rajesh', 'sharma', '20'], dtype='<U11')

print(type(arr))  # <class 'numpy.ndarray'>


'''
Dimensions in Arrays :- 
---------------------------
'''
0-D Arrays :- 
--------------
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

Ex :- Create a 0-D array with value 42.

import numpy as np

arr = np.array(42)
# arr = np.array('Rajesh')

print(arr)

print(arr.ndim) # 0

1-D Arrays :- 
-------------
Ex :- 

import numpy as np

arr = np.array([10,20,30,90,99])

print(arr) # [10 20 30 90 99]

print(arr.ndim) # 1



2-D Arrays :- 
-------------
Ex :- 

import numpy as np

arr = np.array([[10,20,30],[90,99,201]])

print(arr) 
#
 [[ 10  20  30]
 [ 90  99 201]]

print(arr.ndim) # 2



3-D Arrays :- 
-------------
Ex :- 

import numpy as np

arr = np.array([[[10,20,30],[90,99,201]]])

print(arr) 
#
 [[[ 10  20  30]
 [ 90  99 201]]]

print(arr.ndim) # 3


'''
Higher Dimensional Arrays :-
-------------------------------
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the 
ndmin argument.
'''
Ex :- Create an array with 5 dimensions and verify that it has 5 dimensions.


import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
# 
[[[[[1 2 3 4]]]]]

print('number of dimensions :', arr.ndim)
# number of dimensions : 5



