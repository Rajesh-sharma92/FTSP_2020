# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:56:01 2020

@author: Rajesh
"""
'''
Python Modules :- 
------------------
'''
What is a Module ? :- 
------------------------
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

Create a Module :- 
------------------
To create a module just save the code you want in a file with the file extension ".py".

NOTE :- Save this code in a file named mymodule.py


Use a Module :- 
-----------------
Now we can use the module we just created, by using the import statement:

NOTE :- Import the module named mymodule, and call the greeting function:

Ex :- 

import mymodule

mymodule.greeting('FORSK CODING SCHOOL')
# Hello and Welcome to the , FORSK CODING SCHOOL

mymodule.greeting('Usha Babudaya')
# Hello and Welcome to the , Usha Babudaya

mymodule.greeting('My Sweetheart Gududaya')
# Hello and Welcome to the , My Sweetheart Gududaya

mymodule.add(10,20) # The Addition x & y are : 30

mymodule.sub(100,20) # The Sub x & y are : 80

mymodule.mul(10,2) # The Mul x & y are : 20

mymodule.div(100,5) # The Div x & y are : 20.0

'''
Variables in Module :- 
-----------------------
The module can contain functions, as already described, but also variables of all types 
(arrays, dictionaries, objects etc).
'''
Ex :- 

import mymodule

x = mymodule.person['name']
y = mymodule.person['age']
z = mymodule.person['country']

print('The Name of the Person :', x)

print('The Age of the Person :', y)

print('The Country of the Person :', z)

------------- Result -----------
The Name of the Person : RAJESH USHA BABU
The Age of the Person : 26
The Country of the Person : Sikar,Rajastha,India

Ex :- 

mymodule.list1[0] # 2020

mymodule.list1[1] # 'Rajesh-Usha-Babudaya'

mymodule.list1[-1] # 50


'''
Re-naming a Module :- 
---------------------
You can create an alias when you import a module, by using the " as " keyword.
'''
Ex :- 

import mymodule as mm 

mm.greeting('Gochudaya-Babudaya')

mm.add(20,2000)
-------- Result ------
Hello and Welcome to the , Gochudaya-Babudaya
The Addition x & y are : 2020


'''
Built-in Modules :-
----------------------
There are several built-in modules in Python, which you can import whenever you like.
'''
NOTE :- Import and use the platform module.
Ex :- 

import platform

x = platform.system()

y = platform.version()

print('Which platform we are using :', x)

print('Which Vesrion we are using :', y)

-------- Result --------------
Which platform we are using : Windows

Which Vesrion we are using : 6.1.7601

'''
Using the dir() Function :- 
-----------------------------
There is a built-in function to list all the function names (or variable names) 
in a module. The dir() function.
'''
Ex :- 

import platform 

x = dir(platform)

print(x) # There are 75 Functions.


NOTE :- The dir() function can be used on all modules, also the ones you create yourself.

Ex :- 

import mymodule

x = dir(mymodule)

print(x) # There are 14 Functions and we have created it.


'''
Import From Module :-
-----------------------
You can choose to import only parts from a module, by using the from keyword.
'''
NOTE :- The module named mymodule has one function and one dictionary.

NOTE :- Import only the person dictionary from the module.

Ex :- 

from mymodule import person

x = person['name']

print(x) # RAJESH USHA BABU

Ex :- 

from mymodule import add

add(20,2000) # The Addition x & y are : 2020

Ex :- 

from mymodule import greeting

greeting('!!! FORSK JAIPUR GUYS !!!')

# Hello and Welcome to the , !!! FORSK JAIPUR GUYS !!!


