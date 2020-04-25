# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:17:16 2020

@author: Rajesh
"""
'''
Python Try Except Finally :- 
-----------------------------
'''
NOTE :- There are we have mainly 3 blocks like listed below.
1) try block 
2) except block
3) finally block

1) try block :- 
----------------
It is used to test the errors which is available into written codes.

2) except block :- 
----------------
It is used to handle the errors.

3) finally block :- 
-------------------
It will be always executed irrespective of try and except blocks and whether the exception 
raised or not.

'''
Exception Handling :- 
-----------------------
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement.
'''
Ex :- The try block will generate an exception, because x is not defined.

try:
    print(x)
except:
    print('An Exception Occured')
----------- Result ---------
An Exception Occured

NOTE :- Since the try block raises an error, the except block will be executed.

NOTE :- Without the try block, the program will crash and raise an error.

Ex :- This statement will raise an error, because x is not defined.

print(x) # NameError: name 'x' is not defined

'''
Many Exceptions :- 
---------------------
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
'''

Ex :- Print one message if the try block raises a NameError and another for other errors.

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
----------- Result ---------
Variable x is not defined

Ex :- 

try:
    print(20/0)
except:
    print('There is some error into codes')
----------- Result ---------
There is some error into codes    
    
Ex :- 

try:
    print(10/0)
except NameError:
    print("Variable x is not defined")
except FileNotFoundError:
    print('File is not found error')
except ZeroDivisionError:
    print('division by zero')
----------- Result ---------
division by zero

'''
Else :-
-------------
You can use the else keyword to define a block of code to be executed if no errors 
were raised.
'''
Example
In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")    
----------- Result ---------
Hello
Nothing went wrong   
    
'''
Finally :- 
------------
The finally block, if specified, will be executed regardless if the try block raises 
an error or not.    
'''
Ex :- 

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
----------- Result ---------
Something went wrong
The 'try except' is finished



NOTE :- This can be useful to close objects and clean up resources.    

Ex :- Try to open and write to a file that is not writable:

try:
  f = open("E:\W3_2020_School\demofile.txt")
  f.write("FORSK CODING SCHOOL , JAIPURA. This is Rajesh sharma from Sikar,Rajasthan.")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

'''
Raise an exception :- 
-----------------------
As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.
'''
Ex :- Raise an error and stop the program if x is lower than 0.

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
------- Result --------
Exception: Sorry, no numbers below zero

x = 125

if x < 250:
  raise Exception('Is it X value is greather than given value.')
------- Result --------
Exception: Is it X value is greather than given value.



NOTE :- The raise keyword is used to raise an exception.

NOTE :- You can define what kind of error to raise, and the text to print to the user.    
    


Ex :- Raise a TypeError if x is not an integer.


x = "hello"

#x = 120

if not type(x) is int:
  raise TypeError("Only integers are allowed")
 
------- Result --------
TypeError: Only integers are allowed


