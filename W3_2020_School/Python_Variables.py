# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:24:59 2020

@author: Rajesh
"""
'''
Python Variables :- 
----------------
'''
Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

x = 5

y = 'FORSK CODING SCHOOL'

print(x) # 5

print(y) # FORSK CODING SCHOOL

'''
Variable Names :- 
-----------------

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

a = 10
print(type(a)) # <class 'int'>
print(a) # 10 

NOTE :- Strings we can declare within single/double/triple quotes also. No issue at all.
a = 'Forsk'
print(type(a)) # <class 'str'>
print(a) # Forsk

a = "Forsk"
print(type(a)) # <class 'str'>
print(a) # Forsk

a = '''Forsk'''
print(type(a)) # <class 'str'>
print(a) # Forsk


Legal variable names :- We can declare the Variables Names like also.
----------------------
x = 10 
print(x) # 10 , It is valid.

age = 25
print(age) # 25 , It is valid.

Rajesh_Age = 26 
print(Rajesh_Age) # 26 , It is valid.

_xvalue = 100
print(_xvalue) # 100 , It is valid.
 
_x_value = 150
print(_x_value) # 150 , It is valid.

xVal = '10'
print(xVal) # 10 , It is valid.

CarName = 'Swift&Oddy'
print(CarName) # Swift&Oddy , It is valid.

MYNAME = 'Rajesh sharma'
print(MYNAME) # Rajesh sharma , It is valid.

xydetails_ = 100
print(xydetails_) # 100 , It is valid.

ydetails2550 = 'EmailID'
print(ydetails2550) # EmailID, It is valid.


Illegal variable names :- We can not declare the Variables Names like.
------------------------

2x = 10  # It is not Valid.

x- = 200 # It is not Valid.

age-rajesh = 25 # It is not Valid.

student name = 'Rajesh sharma'


NOTE :- Remember that variable names are case-sensitive.

Z = 100

print(z) # name 'z' is not defined.

print(Z) # 100



'''
Assign Value to Multiple Variables :- 
-------------------------------------
'''
Ex :- 

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

------------------------- Result ----------------

Orange
Banana
Cherry

Ex :- 

a , b , c = 10,20,30

print(a,b,c) # 10 20 30


NOTE :- And you can assign the same value to multiple variables in one line.

Ex :- 
x = y = z = "Orange"

print(x)
print(y)
print(z)

------------------------- Result ----------------
Orange
Orange
Orange

Ex :- 

a = b = c = d = e = 1001
print(a,b,c,d,e) # 1001 1001 1001 1001 1001


'''
Output Variables :- 
-----------------
'''
The Python print() function is often used to output variables.

To combine both text and a variable, Python uses the + character:

Ex :- 
x = "awesome"
print("Python is " + x) # Python is awesome

Ex :- 
x = "awesome"
print("Python is ", x) # Python is  awesome # Means one space will be there.

Ex :- 
x = "Python is "
y = "awesome"
z =  x + y
print(z) # Python is awesome

Ex :- 
x = 5
y = 10
print(x + y) # 15

Ex :- 

x = 10 
y = 'Rajesh'
print(x+y) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

NOTE :- To avoid such kind of error we need to type the int into string.

print(str(10)+y) # 10Rajesh


'''
Global Variables :- 
-------------------
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
'''

Ex :- 

x = 10

def f1(): # Function defining or creation of function.
    print('The value of x :', x)
    
f1() # Function call    

print('The value of x :', x)
     
--------------- Result -------------
The value of x : 10


NOTE :- 
If you create a variable with the same name inside a function, this variable will be local,
and can only be used inside the function. The global variable with the same name will 
remain as it was, global and with the original value.
Ex :- 

x = "awesome"

def f1():
  x = "fantastic"
  print("Python is " + x) # Python is fantastic

f1()

print("Python is " + x) # Python is awesome


Ex :- 

x = 100 # Global variable declared.

def f1():
    y = 'Rajesh' # Local variable declared.
    
    print('The Value of x :', x)
    print('The value of y :', y)
    
f1() # Function Call

print('The Value of x :', x)
---------------- Result ------------
The Value of x : 100
The value of y : Rajesh
The Value of x : 100



'''
global Keyword :- 
----------------
'''
NOTE :- 

Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.

Ex :- 

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)


myfunc()

print("Python is " + x)

---------------- Result ------------
Python is fantastic
Python is fantastic


Ex :- 

x = "awesome"

def myfunc():
  global y
  y = "fantastic"
  print("Python is " + y)

myfunc()

print("Python is " + x)
print("Python is " + y)

---------------- Result ------------
Python is fantastic
Python is awesome
Python is fantastic

