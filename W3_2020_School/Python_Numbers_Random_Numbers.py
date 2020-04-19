# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:07:10 2020

@author: Rajesh
"""
'''
Python_Numbers_Random_Numbers :- 
---------------------------------
'''
Python Numbers :- 
----------------
There are three numeric types in Python:

1) int
2) float
3) complex

NOTE :- Variables of numeric types are created when you assign a value to them.
Ex :- 

x = 120
y = 20.50
z = 25+30j
print(type(x))
print(type(y))
print(type(z))
-------------- Result ---------------
<class 'int'>
<class 'float'>
<class 'complex'>

Type Conversion :- 
-----------------
NOTE :- we can convert from one type to another with the int(), float(), and complex() methods.
x = 100
print(x)
print(type(x))
y = float(x)
print(y)
print(type(y))
-------------- Result ---------------
100
<class 'int'>
100.0
<class 'float'>


x = 550.2025
print(x)
print(type(x))
y = int(x)
print(y)
print(type(y))
-------------- Result ---------------
550.2025
<class 'float'>
550
<class 'int'>

x = 20
y = complex(x)
print(y)
print(type(y))
-------------- Result ---------------
(20+0j)
<class 'complex'>

a = 10j
b = complex(a)
print(b)
print(type(b))
-------------- Result ---------------
10j
<class 'complex'>


NOTE :- You cannot convert complex numbers into another number type.

x = 10+20j
y = int(x) # TypeError: can't convert complex to int

-------------------------------------------------------------------------------------------------
'''
Random Number :- 
-------------
'''

Python does not have a random() function to make a random number, but Python has a built-in
module called random that can be used to make random numbers.
 
import random

print(random.randrange(0,10)) # 2,6,8,2,1,0,9

Ex :- 
Set the seed value to 10 and see what happens:

import random

random.seed(10)
print(random.random())

import random 
print(random.randint(5,10)) # 7,9,10,6,5,8

import random 
x = [10,20,30,40,50]
print(random.choice(x)) # 30,10,40,20,50

import random
print(random.random()) # It generates the always float values.
------------
0.3661456016604264
0.8981962445391883

import random
x = [10,20,'Rajesh','sharma',20.5]
random.shuffle(x)
print(x)
----------------
['Rajesh', 10, 20, 20.5, 'sharma']

[20.5, 'Rajesh', 10, 'sharma', 20]

