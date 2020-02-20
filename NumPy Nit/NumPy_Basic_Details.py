# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:42:15 2020

@author: Rajesh
"""
NumPy :- Numerical Python and It is module or Library.

Pyhton is providing set of modules.
Python is a general purpose programming language.

Libraries :- Numpy , scipy , Pandas .... etc.

import numpy

my_list = [10,20,30,40,50]
print(type(my_list)) # <class 'list'>
print(my_list) # [10, 20, 30, 40, 50] NOTE :- Elements are seperated by comma in list.

Ar = numpy.array(my_list)
print(type(Ar)) # <class 'numpy.ndarray'>
print(Ar) # [10 20 30 40 50] NOTE :- Elements are seperated by space in list.

NOTE :- array is the function and which is available in numpy module.
It is used to convert the list into Array form.
NOTE :- Array doesn't support python coz Arrays are static and python is dynamic programming language.
Question :- How we can achieve array concept in python coz python doesn't support ? 
Answer :- In python we can use array concept by numpy module. 
------------------------------------------------------------------------------------------------
Find the properties of An Array :- 
-------------------------------
import numpy

my_list = [10,20,30,40,50]
arr = numpy.array(my_list) 
# To check the size of any array and size is not a method. It is just calling the dynamic variable on object.
print('The Array :', arr)
print('size :', arr.size) # 5 # It shows the full data present in list or any other data types.
print('DataType :', arr.dtype) # int32 --> It shows the data types.
print('Dimension :', arr.ndim) # 1 --> It shows the dimension of the data.
print('Shape :', arr.shape) # (5,) --> It shows the details of no.of rows & no. of cols. like (m X n).

NOTE :- Shape (5,) coz it is 1 dimensional array so it always shows the data in form of (n,).
NOTE :- The shape of any data types always will be reprsenting in tuple data type.
---------------------------------------------------------------------------------------------
import numpy

my_list = [[10,20,30],[40,50,60],[70,80,90],[100,101,102]]
print(my_list)
matrix = numpy.array(my_list)
print('The Matrix :', matrix)
print('size :', matrix.size) # 12 --> It shows the full element present in list or any other data types.
print('DataType :', matrix.dtype) # int32 --> It shows the data types.
print('Dimension :', matrix.ndim) # 2 --> It shows the dimension of the data.
print('Shape :', matrix.shape) # (4,3) --> It shows the details of no.of rows & no. of cols. like (m X n).
NOTE :- Shape (4,3) coz it is 2 dimensional array so it always shows the data in form of (n,n).
NOTE :- The shape of any data types always will be reprsenting in tuple data type.
NOTE :- All size,dtype,ndim and shape are object level variables and which are pre-defined variables in python.
----------------------------------------------------------------------------------------------------------------
import numpy as np

my_list = [10,20,30,40,50]
arr = np.array(my_list)
print('Elements are :')
for ele in arr:
    print(ele)
 *********** Output *************
Elements are :
10
20
30
40
50   
-------------------------------------------------------------------------------------------    
import numpy as np

my_list = [[10,20,30],[40,50,60],[70,80,90]]
print(my_list)

matrix = np.array(my_list)
print(matrix) 
print('Elements are :')
for row in matrix:
    print(row)
    
    for row in matrix:
        for ele in row:
            print(ele)
    
    for row in matrix:
        for ele in row:
            print(ele , end=" ")
        print()    
    
-----------------------------------------------------------------------------------------------------
    


















   















































 
