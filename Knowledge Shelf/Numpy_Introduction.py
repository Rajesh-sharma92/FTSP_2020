# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:15:37 2020

@author: Rajesh
"""

Numpy in Python :- It stands for Numerical Python.
---------------

import numpy as np

my_list = [1,2,3,4,5]

arr = np.array(my_list)

type(arr) # numpy.ndarray

print(arr) # [1 2 3 4 5]

--------------------------------------------------------------------------------------------------------

How to use arange() function :-
-----------------------------
np.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

np.arange(10,16) # array([10, 11, 12, 13, 14, 15])

NOTE :- In the example we can see that in the "arange()" function default the
range will be statring from 0 only. If we want we can change the staring position.

NOTE :- If we want we can define steps also.

np.arange(0,10,2) # array([0, 2, 4, 6, 8])

np.arange(10,20,3) # array([10, 13, 16, 19])
------------------------------------------------------------------------------

How to define zeros matrix in numpy :- 
-----------------------------------
np.zeros(4)

O/P :- [0., 0., 0., 0.]

np.zeros(10)

O/P :-[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
---------------------------------------------------------------------------------
np.zeros((3,5))

array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])

---------------------------------------------------------------------------
np.ones((3,5))

array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])

--------------------------------------------------
How to generate Random number inside python.

np.random.randint(0,10) # 9,1,3,9,6.

np.random.randint(0,100,(3,3))
array([[97,  1, 65],
       [11, 61, 73],
       [56, 69, 70]])

array([[96, 95, 96],
       [45, 54, 70],
       [59, 73, 23]])


--------------------------------------------------------------------------------------------
How to fix the Random numbers in the numpy.
np.random.seed(101) # Here we can pass any value for as a seed value. 
np.random.randint(0,100,10)

array([95, 11, 81, 70, 63, 87, 75,  9, 77, 40]) --> 1st time run

array([95, 11, 81, 70, 63, 87, 75,  9, 77, 40]) --> 2nd time run 

array = np.random.randint(0,100,10)
print(array) # [45 40 92 91 36 60 42 58 41 20]
array.max() # 92
array.min() # 20
array.mean() # 52.5
array.argmax() # 2
array.argmin() # 9

array.reshape(2,5)
([[45, 40, 92, 91, 36],
 [60, 42, 58, 41, 20]])

array.reshape(5,5) # ValueError: cannot reshape array of size 10 into shape (5,5).
--------------------------------------------------------------------------------
math = np.arange(0,100).reshape(10,10)
print(math)
 
math[0,0] # 0 --> Slicing inside matrix 

math[4,8] # 48 --> Slicing inside matrix 

math[0,:] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

math[:,5] # [ 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]

math[0:3,0:3]
#
[ 0,  1,  2],
[10, 11, 12],
[20, 21, 22]]






































