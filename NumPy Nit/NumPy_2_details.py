# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:40:52 2020

@author: Rajesh
"""
Numpy subMatrix From Matrix Using Slicing :-
-----------------------------------------
import numpy

my_list = [[10,20,30],[40,50,60],[70,80,90]]
matrix = numpy.array(my_list)
print(matrix)

# NOTE :- syntax for the slicing in matrix.
# syntax :- [row_lwr : row_upp , col_lwr : col_upp]

# res = matrix[ 0: , :]
res = matrix[ : , : ]
print(res)

res = matrix[0:3 , 0:3]
print(res)

res = matrix[0:1 , 0:3]
print(res)

res = matrix[0:2 , 0:3]
print(res)

res = matrix[0:3 , 0:2]
print(res)

res = matrix[1:3 , 1:3]
print(res)

-------------------------------------------------------------------------------------------
Creating One Dimensional Array in NumPy :- 
---------------------------------------
import numpy

n = int(input('Enter size :'))
arr = numpy.ndarray(shape=(n) ,dtype = int)

print('Enter %d elements :', %n)
for i in range(n):
    arr[i] = int(input()) # converting into int type.
print('The Array elements are :', arr)
    
*********** Result ***********
The Array elements are : [1 2 3 4 5 6]
--------------------------------------------------------------------------------------
import numpy

n = int(input('Enter size :'))
arr = numpy.ndarray(shape=(n) ,dtype = int)

print('Enter %d elements :' %n)
for i in range(n):
    arr[i] = input() # By default it is taking float values.
print('The Array elements are :', arr)
    
*********** Result ***********
The Array elements are : [1. 2. 3. 4.]
------------------------------------------------------------------------------------














































