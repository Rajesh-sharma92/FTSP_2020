# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:48:05 2020

@author: Rajesh
"""
'''
Python Lambda Function :- 
-------------------------
'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax :- 

lambda arguments : expression

The expression is executed and the result is returned:

Ex :- A lambda function that adds 10 to the number passed in as an argument, and print the result.

x = lambda x : x + 10 

x(5) # 15

Ex :- 
x = lambda x : x - 100

x(150) # 50


NOTE :- Lambda functions can take any number of arguments.

Ex :- 

z = lambda x,y : x*y

z(5,6) # 30

Ex :- 

x = lambda a , b ,c : a + b + c

x(10,20,30) # 60

Ex :- 

x = lambda a : a*a

x(5) # 25
x(2) # 4

'''
Why Use Lambda Functions? :-
-----------------------------
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
'''
Ex :- 

def f1(n):
    return lambda x : x*n

doubler = f1(2)

doubler(100) # 200

doubler(15) # 30

Ex :- 

def f1(n):
  return lambda a : a * n

tripler = f1(3)

tripler(11) # 33

Ex :- 

def f1(number):
    return lambda x : x/number

number = f1(20)

number(5) # 0.25

Ex :- 

def f1(n):
    return lambda x : x - n

sub = f1(50)

sub(5) # -45


Ex :- 

def f1(n):
    return lambda x : x + n

sub = f1(550)

sub(50) # 600

