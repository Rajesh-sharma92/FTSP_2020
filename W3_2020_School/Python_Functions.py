# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:50:49 2020

@author: Rajesh
"""
'''
Python Functions :- 
-------------------
'''
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

'''
Creating a Function :- 
----------------------
In Python a function is defined using the def keyword.
'''
Ex :- 

def f1(): # Creating a Function
    print('This is f1() function')
    
'''    
Calling a Function :- 
---------------------
To call a function, use the function name followed by parenthesis:    
'''

def f1(): # Creating a Function
    print('This is f1() function')

f1() # Calling a Function
---------- Result ---------
This is f1() function

Ex :- Add 2 nos. by using function.

def add(x,y):
    return (x+y)

print('We have added 2 Nos.', add(10,20))
---------- Result ---------
We have added 2 Nos. 30

'''
Arguments :- 
----------------
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). When the function is called, 
we pass along a first name, which is used inside the function to print the full name.
'''
Ex :- 

def f1(fname):
    print(fname + ' Babudaya')
    
f1('Usha')
f1('Gududaya')
f1('Gochudaya')
---------- Result ---------
Usha Babudaya
Gududaya Babudaya
Gochudaya Babudaya

Ex :- 

def f1(x):
    print('The Square of', x , ':', x*x)

f1(5)
f1(8)
f1(2)
f1(4)
---------- Result ---------
The Square of 5 : 25
The Square of 8 : 64
The Square of 2 : 4
The Square of 4 : 16   

'''
Number of Arguments :- 
------------------------
By default, a function must be called with the correct number of arguments. Meaning that if 
your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
'''
Ex :- 

def f1(ename , edept):
    print('The Emp details are :' , ename + ' ' + edept)

f1('Rajesh' , 'Data Science')
---------- Result ---------
The Emp details are : Rajesh Data Science

Ex :- 

def f1(x,y):
    print('The Result :', x > y)
    
f1(100,99)
---------- Result ---------
The Result : True

'''
Arbitrary Arguments, *args :- 
-------------------------------
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
'''

Ex :- 
If the number of arguments is unknown, add a * before the parameter name:

def f1(*lover):
    print('My favoriate person :', lover[2])
    
f1('Rajesh','Usha','Babudaya-Gududaya')
---------- Result ---------
My favoriate person : Babudaya-Gududaya

'''    
Keyword Arguments :- 
--------------------
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
'''
Ex :- 

def f1(x,y,z):
    print('The value of Variable :', z)

f1(100,20,99)
---------- Result ---------
The value of Variable : 99    

Ex :- 

def f1(z,y,x):
    print('The value of Variable :', z)

f1(x=100,y=20,z=99)
---------- Result ---------
The value of Variable : 99

Ex :- 

def f1(z,y,x):
    print('The value of Variable :', z)

f1(100,20,99)
---------- Result ---------
The value of Variable : 100

'''
Arbitrary Keyword Arguments, **kwargs :- 
-----------------------------------------
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
If the number of keyword arguments is unknown, add a double ** before the parameter name:
'''
Ex :- 

def f1(**lover):
    print('My Favoriate Lover name :',lover['lname'])
    
f1(fname='Usha' , lname='Babudaya')    
---------- Result ---------
My Favoriate Lover name : Babudaya

'''
Default Parameter Value :- 
----------------------------
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:
'''
Ex :- 

def my_function(country = "Norway"):
  print("I am from :" , country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
---------- Result ---------
I am from : Sweden
I am from : India
I am from : Norway
I am from : Brazil

Ex :- 

def f1(x=10,y=20):
    print('The X & Y Values are :', x , y)
    
f1()
f1(x=100 , y = 200)
f1(x=2020)
f1(y=2025)    
---------- Result ---------
The X & Y Values are : 10 20
The X & Y Values are : 100 200
The X & Y Values are : 2020 20
The X & Y Values are : 10 2025

'''
Passing a List as an Argument :-
--------------------------------
You can send any data types of argument to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function.
E.g. if you send a List as an argument, it will still be a List when it reaches the function
'''
Ex :- 

def f1(details):
    for x in details:
        print(x , end=' ')

list1 = ['Rajesh','Usha',1001,201,'forsk']

f1(list1)
---------- Result ---------
Rajesh Usha 1001 201 forsk 

Ex :- 

def square(num):
    for x in num:
        print(x*x , end=' ')

list1 = [2,3,4,5]
square(list1)
---------- Result ---------
4 9 16 25 

'''
Return Values :- 
-------------------
To let a function return a value, use the return statement.
'''
Ex :- 

def f1(x):
    return 5*x

f1(3) # 15
f1(10) # 50
f1(15) # 75
f1(0) # 0

'''
The pass Statement :- 
-----------------------
function definitions cannot be empty, but if you for some reason have a function 
definition with no content, put in the pass statement to avoid getting an error.
'''
Ex :- 

def f1(x,y):
  pass

