# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:23:10 2020

@author: Rajesh
"""

Numpy Module In Python :- 
-----------------------
--> It is very popular in the python and it is very useful the Machine Learning projects.
--> It is used for the scintific calculations in machine learning.

How to install into spyder Anaconda.
----------------------------------------
!pip install numpy

--> Numpy is the most useful feature is n dimensional array object (a.k.a) means also 
known as ndarray

How to create the numpy array in python :- 
-----------------------------------------
import numpy as np

arr = np.array([1,2,3,4,5])
arr.size # 5

arr.dtype # dtype('int32')

print(arr) # [1 2 3 4 5]

arr[0] # 1
arr[3] # 4

arr.itemsize # 4

arr = np.array([1,2,3,4,5]).astype('float64')
arr # [1., 2., 3., 4., 5.]

arr.dtype # dtype('float64')

arr.itemsize # 8

arr = np.array([1,2,3,4,5] , dtype='int')
arr # [1, 2, 3, 4, 5]

arr.dtype # dtype('int32')

arr.itemsize # 4


Question :- I have already list into python then why do i need the numpy array ?
Answer :- There are mainly 3 benefits from numpy array compare to python list.
1) Less Memory   2)   Fast  3) Convinient

import sys

import time

l = range(1000)
print(sys.getsizeof(5)*len(l)) # 28000

array = np.arange(1000)
print(array.size * array.itemsize) # 4000 

# We will check the Numpy is Faster than Python List.
SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python List
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print('Python List Took :', (time.time()-start)*1000)

start = time.time()
result = a1+a2
print('Numpy Array Took:', (time.time()-start)*1000)

Python List Took : 684.0391159057617
Numpy Array Took: 35.00175476074219

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

print(a1+a2) # [5 7 9]

print(a1-a2) # [-3 -3 -3]

print(a1*a2) # [ 4 10 18]

print(a1/a2) # [0.25 0.4  0.5 ]


a = np.arange(10)
print(a) # [0 1 2 3 4 5 6 7 8 9]

x = np.arange(10).reshape(2,5)
print(x)
----
[[0 1 2 3 4]
 [5 6 7 8 9]]

x[0] # [0, 1, 2, 3, 4]

x[1] # [5, 6, 7, 8, 9]

