# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:13:31 2020

@author: Rajesh
"""
Exception Handling In Python :-
----------------------------
There are 2 types of Exception error occurs most of times.
1) Syntax Error
2) Runtime Error
------------------------------------------------------------------------------------------------
1) Syntax Error :- This kind of errors occured when you are not following the 
proper / valid syntax as per some standard rules.

x = 10
if x == 10
    print('X values is 10')

********* Result ***********
if x == 10
              ^
SyntaxError: invalid syntax

NOTE :- Here we can see that in the above example there is " : " missing after the 10.
If we put the colon (:) then we will be getting the valid result.

x = 10
if x == 10:
    print('X values is 10')

********* Result ***********
X values is 10

--------------------------------------------------------------------------------------------------
print " Hello World"

********* Result ***********

print 'Hello World'
                       ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(" Hello World")?

NOTE :- Here we need to use the parentheses to call the print function.

print('Hello World')

********* Result ***********
Hello World
-------------------------------------------------------------------------------------------------------
Question :- Who is the responsible to correct this syntax mistakes / errors ?
Answer :- As a programmer we need to rectify all these kind of syntax errors and 
we need to resolve it and care of it as per writing the codes.

NOTE :- One more important thing is that all syntax errors are correct then only
our program will be start executing and PVM will be start executing the codes.
--------------------------------------------------------------------------------------------------
2) Runtime Error :- This kind of errors occured while executing the programs we may 
get some runtime exceptions like end user has not entered the Input correctly, Memory Issue
and some logic mistakes and etc.

Ex :-

x = int(input('Enter first number :')) # 20
y = int(input('Enter second number :')) # 5
print('The Result :', x/y) # Here All 3 lines look very correct and NO syntax errors at all.

********* Result ***********  
The Result : 4.0
-----------------------------------------------------------------------------------
NOTE :- Here we can see that some times end user may entered the invalid Inputs and 
there may be chances of getting any runtime error like.

x = int(input('Enter first number :')) # 10 # ten
y = int(input('Enter second number :')) # 0
print('The Result :', x/y) # ZeroDivisionError: division by zero

********* Result ***********  
ZeroDivisionError: division by zero

ValueError: invalid literal for int() with base 10: 'ten'
-------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/feedback1.txt')
print(f.read())

********* Result ***********  
FileNotFoundError: [Errno 2] No such file or directory: 'E:/Durga OOPs/Files Handling/Output1.txt'
-------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/feedback.txt')
print(f.read())

********* Result ***********  
sitapura jaipur sikar 
----------------------------------------------------------------------------------------------------------
NOTE :- Runtime errors are also known as Exceptions.
NOTE :- Exception Handling concepts are related to runtime errors only not 
related to syntax errors.
---------------------------------------------------------------------------------------
Ex :- If we are driving car / bike after drinking alcohal and some kind of accident 
happended that which error occured ? There will be syntax error coz we should not 
driving after drinking alcohal and then obvisouly accident happens.

If we are driving car/bike and everything is running properly but suddenly some
full drunk person came and hit to us then accident happended then there will 
be Runtime errors occured.
---------------------------------------------------------------------------------------------



















































































