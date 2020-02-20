# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:51:36 2020

@author: Rajesh
"""

Creating Two Dimensional Array in NumPy :-
---------------------------------------
import numpy 

m = int(input('Enter row size :'))
n = int(input('Enter columan size :'))

matrix = numpy.ndarray(shape=(m,n) , dtype = int)
print('Matrix size :', matrix.size)
print('Matrix shape :', matrix.shape)
print('Matrix dimension :', matrix.ndim)



NOTE :- size :- It gives the count of total elements will be present into matrix.

NOTE :- shape :- Here we have matrix = (M X N). that no. of rows and no. of columns.

NOTE :- Dimension :- Like 1D , 2D and etc.......

 ************* Result *************

Enter row size :4
Enter columan size :4

Matrix size : 16
Matrix shape : (4, 4)
Matrix dimension : 2
---------------------------------------------------------------------------

Enter row size :2

Enter columan size :6

Matrix size : 12
Matrix shape : (2, 6)
Matrix dimension : 2

















