# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:50:40 2020

@author: Rajesh
"""

basic array operations Numpy Model in Python :- 
---------------------------------------------
# One Dimensional Array :- 

import numpy as np 

a = np.array([1,2,3,4,5])

a # array([1, 2, 3, 4, 5])

print(a) # [1 2 3 4 5]

a.ndim # 1

a.itemsize # 4
 
a.size # 5

a.shape # (5,)

a[1] # 2

a[4] # 5

--------------------
# Two Dimensional Array :- 
---------------------------
a = np.array([[1,2],[3,4],[5,6]])

a

array([[1, 2],
       [3, 4],
       [5, 6]])

print(a)

[[1 2]
 [3 4]
 [5 6]]

a.itemsize # 4

a.size # 6

a.shape # (3, 2)

a.ndim # 2

a[0] # [1, 2]
a[0][0] # 1
a[0][1] # 2


a = np.array([[1,2],[3,4],[5,6]]).astype('float64')
# a = np.array([[1,2],[3,4],[5,6]] , dtype='float')
#  a = np.array([[1,2],[3,4],[5,6]] , dtype=float)
# a = np.array([[1,2],[3,4],[5,6]] , dtype=np.float)
a
array([[1., 2.],
       [3., 4.],
       [5., 6.]])


a = np.array([[1,2],[3,4],[5,6]] , dtype=complex)
a
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j],
       [5.+0.j, 6.+0.j]])


# If we want to get the Zeros Metrix or Zeros Numpy Array 
import numpy as np
np.zeros((2,2))
---
[[0., 0.],
[0., 0.]])

np.zeros((2,5))
-----
[0., 0., 0., 0., 0.],
[0., 0., 0., 0., 0.]])

# If we want to get the Ones Metrix & Ones Numpy Array.
np.ones((2,2))
----
[[1., 1.],
[1., 1.]])

# If we want to create the some list like this below.
l1 = range(10)

l1 # range(0, 10)

list(l1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l2 = range(20,30)

l2 # range(20, 30)

list(l2) # [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

l2[5] # 25

l2[0] # 20


# In the Numpy we have " arange() function like range() function in python "
l1 = np.arange(10)

l1 # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

l2 = np.arange(25,35)

l2 # array([25, 26, 27, 28, 29, 30, 31, 32, 33, 34])

# We want to give the steps also we can give it.

l1 = np.arange(10,20,2)

l1 # array([10, 12, 14, 16, 18])

# Linear Squence of Numbers.
# If we want to get the Linspace Number between some of the range.

x = np.linspace(10,20,5)
# Syntax :- start = 10, end=20 , no. of times = 5

x # [10. , 12.5, 15. , 17.5, 20. ]


# If we want to Reshape the Numpy Array or metrix.
a = np.array([[1,2],[3,4],[5,6]])
a.shape # (3, 2)
a 
---
array([[1, 2],
       [3, 4],
       [5, 6]])

a.reshape(2,3)
----
array([[1, 2, 3],
       [4, 5, 6]])

a.reshape(6,1)

a.reshape(1,6)

# To make the One Dimensional Array we just need to use the " raval()".
x = np.array([[1,2],[3,4],[5,6]])
x.shape # (3, 2)
x.ndim # 2

x = x.ravel() # array([1, 2, 3, 4, 5, 6])
x.shape # (6,)
x.ndim # 1

# Now we perform the mathematical Functions like.
x = np.array([[1,2],[3,4],[5,6]])

x.min() # 1

x.max() # 6

x.sum() # 21

x.mean()# 3.5

# Here we have Axis Concept like " axis = 0 Means Columns & axis = 1 Means Rows"

x.sum(axis=0) # array([ 9, 12])

x.sum(axis=1) # array([ 3,  7, 11])

# from math import sqrt 

np.sqrt(x)

np.sqrt(25) # 5.0

np.std(x) # 1.707825127659933

np.std(100) # 0.0

x = np.array([[1,2],[3,4]])

y = np.array([[5,6],[7,8]])

x+y
----
array([[ 6,  8],
       [10, 12]])


x-y
----
[[-4, -4],
[-4, -4]])



x*y
---
[[ 5, 12],
[21, 32]])


x/y
---
array([[0.2       , 0.33333333],
       [0.42857143, 0.5       ]])


x.dot(y)
---
array([[19, 22],
       [43, 50]])



