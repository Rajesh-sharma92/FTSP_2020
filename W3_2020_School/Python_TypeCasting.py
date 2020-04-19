# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:32:14 2020

@author: Rajesh
"""
'''
Python TypeCasting :-
-------------------
'''
In the Python programmin Languages we have different kind of type casting concept like whenever
we have some issue with some of the functions type conversion for getting the desired results.

We have type casting for some of the data types like .

1) Integer Data Types 
2) Float Data Types
3) String Data Types


1) Integer Data Types :- 
----------------------
NOTE :- This is can be used to convert from int to into float data as well as string data types also.
Ex :- 

Integer to Float Data Type Conversion :- 
-----------------------------------------
x = 2020 # Integer Value

print('Before Type casting')
print('The Value of x :', x)
print(type(x))

print('After Type casting')
x = float(x) # Type Casting from int to float data types.
print('The Value of x :', x)
print(type(x))
------------ Result -------------
Before Type casting
The Value of x : 2020
<class 'int'>

After Type casting
The Value of x : 2020.0
<class 'float'>


Integer to String Data Type Conversion :- 
-----------------------------------------
x = 2020 # Integer Value

print('Before Type casting')
print('The Value of x :', x)
print(type(x))

print('After Type casting')
x = str(x) # Type Casting from int to string data types.
print('The Value of x :', x)
print(type(x))
------------ Result -------------
Before Type casting
The Value of x : 2020
<class 'int'>

After Type casting
The Value of x : 2020
<class 'str'>
x = '2020'

-------------------------------------------------------------------------------------------------------
2) Float Data Types :- 
NOTE :- This is can be used to convert from float to into int data as well as string data types also.
Ex :-

Float to Integer Data Type Conversion :- 
-----------------------------------------
x = 1992.2020  # Integer Value

print('Before Type casting')
print('The Value of x :', x)
print(type(x))

print('After Type casting')
x = int(x) # Type Casting from float to int data types.
print('The Value of x :', x)
print(type(x))
------------ Result -------------
Before Type casting
The Value of x : 1992.202
<class 'float'>
After Type casting
The Value of x : 1992
<class 'int'>



Float to String Data Type Conversion :- 
-----------------------------------------
x = 1992.2020  # Integer Value

print('Before Type casting')
print('The Value of x :', x)
print(type(x))

print('After Type casting')
x = str(x) # Type Casting from float to int data types.
print('The Value of x :', x)
print(type(x))
------------ Result -------------
Before Type casting
The Value of x : 1992.202
<class 'float'>
After Type casting
The Value of x : 1992.202
<class 'str'>
x = '1992.202'

-----------------------------------------------------------------------------------------------------
3) String Data Types :- 

NOTE :- This is can be used to convert from string to into int data as well as float data types also.
Ex :-

String to Integer Data Type Conversion :- 
-----------------------------------------
x = '2008'  # Integer Value

print('Before Type casting')
print('The Value of x :', x)
print(type(x))

print('After Type casting')
x = int(x) # Type Casting from float to int data types.
print('The Value of x :', x)
print(type(x))
------------ Result -------------
Before Type casting
The Value of x : 2008
<class 'str'>
After Type casting
The Value of x : 2008
<class 'int'>


String to Float Data Type Conversion :- 
-----------------------------------------
x = '2008'  # Integer Value

print('Before Type casting')
print('The Value of x :', x)
print(type(x))

print('After Type casting')
x = float(x) # Type Casting from float to int data types.
print('The Value of x :', x)
print(type(x))
------------ Result -------------
Before Type casting
The Value of x : 2008
<class 'str'>
After Type casting
The Value of x : 2008.0
<class 'float'>
 

-----------------------------------------------------------------------------------------------------
Ex :- 

Rajesh_Age = 25
Rajesh_Empid = 2020
print('Before Type casting')
print('Rajesh Age :', Rajesh_Age)
print('Rajesh EmpID :', Rajesh_Empid)

print('*** After Type casting into Float Data Types ***')
Rajesh_Age = float(Rajesh_Age)
Rajesh_Empid = float(Rajesh_Empid)
print('Rajesh Age :', Rajesh_Age)
print('Rajesh EmpID :', Rajesh_Empid)

print('*** After Type casting into String Data Types ***')
Rajesh_Age = str(Rajesh_Age)
Rajesh_Empid = str(Rajesh_Empid)
print('Rajesh Age :', Rajesh_Age)
print('Rajesh EmpID :', Rajesh_Empid)

------------------ Result ------------------
Before Type casting
Rajesh Age : 25
Rajesh EmpID : 2020

*** After Type casting into Float Data Types ***
Rajesh Age : 25.0
Rajesh EmpID : 2020.0

*** After Type casting into String Data Types ***
Rajesh Age : 25.0
Rajesh EmpID : 2020.0

Rajesh Age : '25.0' # Internally its converted into string only.
Rajesh EmpID : '2020.0' # Internally its converted into string only.

