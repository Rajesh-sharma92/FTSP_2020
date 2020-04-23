# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:39:32 2020

@author: Rajesh
"""
'''
Python Scope :- 
----------------
'''
NOTE :- A variable is only available from inside the region it is created. 
This is called scope.

Local Scope :- 
---------------
A variable created inside a function belongs to the local scope of that function, 
and can only be used inside that function.

Ex :- 

def f1(): # Function definitation / function creation.
    x = 1001 # Local variable.
    print('The Value of X :' ,x)
    
f1() # Function calling     
------------ Result --------
The Value of X : 1001

Ex :- 

def f1():
    x = 2020
    y = 'Rajesh'
    print('The value of X :', x)
    print('The value of Y :', y)

f1()    
------------ Result --------
The value of X : 2020
The value of Y : Rajesh

'''
Function Inside Function :- 
---------------------------
As explained in the example above, the variable x is not available outside the function, 
but it is available for any function inside the function.
'''
Ex :- 

def f1():
    x = 2020
    def f2():
         print('The value of X :', x)
    f2()

f1()
------------ Result --------
The value of X : 2020

'''
Global Scope :- 
-----------------
A variable created in the main body of the Python code is a global variable and 
belongs to the global scope.
Global variables are available from within any scope, global and local.
'''

Ex :- 
NOTE :- A variable created outside of a function is global and can be used by anyone.

x = 2020 # Global Variable.

def f1():
    y = 'Forsk Coding School , Jaipur.'
    print('The value of Global X and accessing Inside the fucntion:', x)
    print('The value of Local Y and accessing Inside the fucntion:', y)

f1() # Function Calling.
print('The value of Global X and accessing Outside the fucntion :', x)
------------ Result --------
The value of Global X and accessing Inside the fucntion: 2020
The value of Local Y and accessing Inside the fucntion: Forsk Coding School , Jaipur.
The value of Global X and accessing Outside the fucntion : 2020

'''
Naming Variables :- 
-------------------
If you operate with the same variable name inside and outside of a function, Python will 
treat them as two separate variables, one available in the global scope (outside the function)
and one available in the local scope (inside the function).
'''
Ex :- 

x = 'Forsk coding school' # Global Variable.

def f1():
    x = 2001 # # Local Variable.
    print('The value of Local X and accessing Inside the fucntion:', x)
    
f1()

print('The value of Global X and accessing Outside the fucntion:', x)
------------ Result --------
The value of Local X and accessing Inside the fucntion: 2001
The value of Global X and accessing Outside the fucntion: Forsk coding school


'''
Global Keyword :- 
---------------------
If you need to create a global variable, but are stuck in the local scope, you can 
use the global keyword.
The global keyword makes the variable global.
'''
Ex :- 

def f1():
    global x
    x = 'FORSK CODING SCHHOL JAIPUR,INDIA.'
    
    y = 2020
    print('The Value of X :', x)
    print('The Value of Y :', y)
    
f1() # Function Calling.

print('The Value of X :', x)
------------ Result --------
The Value of X : FORSK CODING SCHHOL JAIPUR,INDIA.
The Value of Y : 2020
The Value of X : FORSK CODING SCHHOL JAIPUR,INDIA.

Ex :- 

def f1():
    global x 
    x = 2020
    
    y = 'My Sweet Babu Usha'
    
    print('The Value of X :', x)
    print('The Value of Y :', y)
    
f1() # Function Calling.

print('The Value of X :', x)    
------------ Result --------    
The Value of X : 2020
The Value of Y : My Sweet Babu Usha
The Value of X : 2020

'''
NOTE :- Also, use the global keyword if you want to make a change to a global 
variable inside a function.
'''
Ex :- 

x = 2020

def f1():
    global x 
    x = 2030
    
    y = 'Babudaya Girl'
    
    print('The Value of X :', x)
    print('The Value of Y :', y)
    
f1() # Function Calling.

print('The Value of X :', x)    
------------ Result --------    
The Value of X : 2030
The Value of Y : Babudaya Girl
The Value of X : 2030

Ex :- 

x = 'Sweetheart_Babudaya_Gududaya'

def f1():
    global x
    x = 'Usha_Babudaya_Gududaya'
    
    y = 'Rajesh sharma Loves Babudaya'
    
    print('The Value of X :', x)
    print('The Value of Y :', y)
    
f1() # Function Calling.

print('The Value of X :', x)    
------------ Result --------        
The Value of X : Usha_Babudaya_Gududaya
The Value of Y : Rajesh sharma Loves Babudaya
The Value of X : Usha_Babudaya_Gududaya

