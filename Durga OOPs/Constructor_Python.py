# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:41:35 2020

@author: Rajesh
"""
" Pg (1) :- Constructor will be executed when object is created for the class."

class Test: # Class Name
    def __init__(self): # Constructor
        print('constructor will be executed')
        print('THIS IS FORSK SCHOOL')
        
        t = Test() # Object creation and 't' is reference variable.
        t1 = Test()
        t = Test()
        t = Test()
        
 # NOTE :- We are creating 4 objects then constructor will be executing 4 times
and once for every objects.

class Test:
    def __init__(self):
        print('no-arg constructor')
        
    def __init__(self,x):
        print('1-arg constructor')
    
    def __init__(self,x,y):
        print('2-arg constructor')
        
#t = Test()

#t1 = Test(10)

t2 = Test(20,30)

t3 = Test(20,30)

# NOTE :- In python method overloading , Constructor overloading is not allowed.
# If will be trying to use this concepts then PVM will give an error.
# We can use Multiple constructors in a class.

------------------------------------------------------------------------------

class student:
    def __init__(self,name,rollno):
        print('constructor will be executed')
        self.name = name
        self.rollno = rollno
        
    def display(self):
        print('Method will be Executed')
        print('Hello My Name is :', self.name)
        print('My rollno :', self.rollno)
        
s = student('Durga',100) # Always first constructor will be executed.

s.display() # Then method will be executed.












































