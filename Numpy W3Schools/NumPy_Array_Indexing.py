# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:09:57 2020

@author: Rajesh
"""
'''
NumPy Array Indexing :- 
-----------------------
'''
Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, 
and the second has index 1 etc.

Ex :- 

import numpy as np 

arr = np.array([10,20,30,40,50])

print(arr) # [10 20 30 40 50]

print(arr[0]) # 10

print(arr[-1]) # 50

NOTE :- Get the 2nd & 3rd element and add them.

print(arr[2] + arr[3]) # 70

'''
Access 2-D Arrays :- 
-----------------------
To access elements from 2-D arrays we can use comma separated integers representing 
the dimension and the index of the element.
'''
Ex :-

import numpy as np

arr = np.array([[10,20,30,40,50] , [60,70,80,90,100]])

print(arr[0,1]) # 20
print(arr[1,3]) # 90
print(arr[0,-1]) # 50
print(arr[1,-3]) # 80

'''
Access 3-D Arrays :- 
---------------------
To access elements from 3-D arrays we can use comma separated integers representing
the dimensions and the index of the element.
'''
Ex :- 

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

print(arr[1,1,1]) # 11

'''
Negative Indexing :-
---------------------
Use negative indexing to access an array from the end.
'''

Ex :- Print the last element from the 2nd dim.

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1]) # Last element from 2nd dim:  10

print('Last element from 2nd dim: ', arr[0, -3]) # Last element from 2nd dim:  3

'''
NumPy Array Slicing :- 
----------------------
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1
'''
Ex :- Slice elements from index 1 to index 5 from the following array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) # [2 3 4 5]


NOTE :- The result includes the start index, but excludes the end index.


Ex :- Slice elements from index 4 to the end of the array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:]) # [5 6 7]


Ex :- Slice elements from the beginning to index 4 (not included).

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4]) # [1 2 3 4]

'''
Negative Slicing :- 
-------------------
Use the minus operator to refer to an index from the end:
'''
Ex :- Slice from the index 3 from the end to index 1 from the end.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])  # [5 6]

print(arr[-3:]) # [5 6 7]

'''
STEP :- 
-----------
Use the step value to determine the step of the slicing.
'''

Ex :- Return every other element from index 1 to index 5.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) # [2 4]


Ex :- Return every other element from the entire array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2]) # [1 3 5 7]

'''
Slicing 2-D Arrays :- 
------------------------
From the second element, slice elements from index 1 to index 4 (not included):
'''
EX :- 

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4]) # [7 8 9]


NOTE :- Remember that second element has index 1.


Ex :- From both elements, return index 2:

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2]) # [3 8]


Ex :- From both elements, slice index 1 to index 4 (not included), this will return
a 2-D array.

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
-------
[[2 3 4]
 [7 8 9]]


