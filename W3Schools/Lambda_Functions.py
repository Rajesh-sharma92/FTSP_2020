# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:17:14 2020

@author: Rajesh
"""
Lambda Functions :-
----------------
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax :- 
lambda arguments : expression

Question :- A lambda function that adds 10 to the number passed in as an argument, and print the result.

x = lambda a : a + 10
print(x(5)) #15 

x = lambda a : a - 50
print(x(10)) # -40

x = lambda a : a * 10
print(x(12)) # 120

x = lambda a : a / 10
print(x(5)) # 0.5

x = lambda a : a * a
print(x(5)) # 25

x = lambda a : a**2
print(x(8)) # 64

x = lambda a : a**3
print(x(2)) # 8

x = lambda a : a**2
print(x(100)) # 10000 
------------------------------------------------------------------------------------------------------------
Question :- A lambda function that multiplies argument a with argument b and print the result.

x = lambda a,b : a+b
print(x(6,4)) # 10

x = lambda a,b : a-b
print(x(1,100)) # -99

x = lambda a,b : a*b
print(x(5,6)) # 30

x = lambda a,b : a/b
print(x(10,20)) # 0.5
--------------------------------------------------------------------------------------------------------
Question :- A lambda function that sums argument a, b, and c and print the result.

x = lambda a,b,c : a+b+c
print(x(10,20,30)) # 60
--------------------------------------------------------------------------------------------------
Why Use Lambda Functions :-
------------------------

The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied 
with an unknown number.:

Question :- Use that function definition to make a function that always doubles the number you send in.    

def myfunc(n):
    return lambda a : a*n

my_double = myfunc(2)
my_triple = myfunc(3)

print(my_double(25)) # 50

print(my_triple(30)) # 90

NOTE :- Use lambda functions when an anonymous function is required for a short period of time.
--------------------------------------------------------------------------------------------------------------------


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





















