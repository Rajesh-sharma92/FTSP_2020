# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:41:11 2020

@author: Rajesh
"""
'''
Python Data Types :- Python has some of the Build-in data types.
------------------
'''
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
    
1) Text Type:	str
2) Numeric Types:	int, float, complex
3) Sequence Types:	list, tuple, range
4) Mapping Type:	dict
5) Set Types:	set, frozenset
6) Boolean Type:	bool
7) Binary Types:	bytes, bytearray, memoryview    

NOTE :- We can check the data type of any object by using the type() function.

Ex :- 

x = 100
print('The Value of x :', x)
print(type(x))
y = 'Forsk Coding School'
print('The Value of y :', y)
print(type(y))
--------------- Result ------------------
The Value of x : 100
<class 'int'>
The Value of y : Forsk Coding School
<class 'str'>

Examples :- 

1) Text Type:	str 
    
x = "Hello World"
print(x)
print(type(x)) 
--------------- Result ------------------
Hello World
<class 'str'>


2) Numeric Types:	int, float, complex

x = 20
print(x)
print(type(x)) 
--------------- Result ------------------
20
<class 'int'>

x = 50.5
print(x)
print(type(x)) 
--------------- Result ------------------
50.5
<class 'float'>

x = 10+20j
print(x)
print(type(x)) 
--------------- Result ------------------
(10+20j)
<class 'complex'>


3) Sequence Types:	list, tuple, range

list1 = ['Rajesh',10,20.5,-15]    
print(list1)
print(type(list1))
--------------- Result ------------------
['Rajesh', 10, 20.5, -15]
<class 'list'> 
    
t1 = ('Rajesh',10,20.5,-15)    
print(t1)
print(type(t1))
--------------- Result ------------------
('Rajesh', 10, 20.5, -15)
<class 'tuple'>

x = range(10)
print(x)
print(type(x))
--------------- Result ------------------
range(0, 10)
<class 'range'>

4) Mapping Type:	dict

dict1 = {'Name':'Rajesh','Age':26}
print(dict1)
print(type(dict1)) 
--------------- Result ------------------
{'Name': 'Rajesh', 'Age': 26}
<class 'dict'>    


5) Set Types:	set, frozenset

set1 = {10,20,'Rajesh','x',20.5,20,10}
print(set1)
print(type(set1))
--------------- Result ------------------
{'Rajesh', 'x', 10, 20, 20.5}
<class 'set'>


x = frozenset({10,20,'Rajesh','x',20.5,20,10})
print(x)
print(type(x)) 
--------------- Result ------------------
frozenset({'Rajesh', 'x', 20, 20.5, 10})
<class 'frozenset'>


6) Boolean Type:	bool

x = True
y = False
print(x)
print(type(x))
print(y)
print(type(y))
--------------- Result ------------------
True
<class 'bool'>
False
<class 'bool'>

7) Binary Types:	bytes, bytearray, memoryview    
    
x = B'Hello World' # x = b'Hello World' # bytes.
print(x)
print(type(x))
--------------- Result ------------------
b'Hello World'
<class 'bytes'>

x = bytearray(5)
print(x)
print(type(x))
--------------- Result ------------------
bytearray(b'\x00\x00\x00\x00\x00')
<class 'bytearray'>

x = memoryview(bytes(5))   
print(x)
print(type(x))
--------------- Result ------------------
<memory at 0x000000000A878288>
<class 'memoryview'>

