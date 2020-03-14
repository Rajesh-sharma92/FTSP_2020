# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:53:14 2020

@author: Rajesh
"""

Nested Methods :- 
--------------
syntax :- 

def m1():
    def m2():
        xxxxxxx
        xxxxxxx # 1000 lines of codes.
        xxxxxxx
        
     m2()
     m2()
     m2()
------------------------------------------------------------------------------    
Ex :-
 
class Test:
    def m1(self):
        def sum(a,b):
            print('First Argument :', a)
            print('Second Argument :', b)
            print('The Sum :', a+b)
            print('The Product :', a*b)
            print('*'*30)
            
        sum(10,20)
        sum(100,200)
        sum(1000,2000)

t = Test()
t.m1()

******* Result *******
First Argument : 10
Second Argument : 20
The Sum : 30
The Product : 200
******************************
First Argument : 100
Second Argument : 200
The Sum : 300
The Product : 20000
******************************
First Argument : 1000
Second Argument : 2000
The Sum : 3000
The Product : 2000000
******************************
-----------------------------------------------------------------------------------------------
Nested Methods :- 
--------------
Q(1) : What is nested method ?
Q(2) : How to use nested method ?
Q(3) : How to declare nested method ?

--------------------------------------------------------------------------------------------
class Test:
    def m1(self):
        def square(n):
            print('The Square :', n*n)
            print('*'*30)
            
        square(2)   
        square(4)   
        square(10)
        square(50)
         
t = Test()
t.m1()

********* Result ********
The Square : 4
******************************
The Square : 16
******************************
The Square : 100
******************************
The Square : 2500
******************************
-----------------------------------------------------------------------------------------------

class Calci:
    def m1(self):
        def Math_Calculation(x,y):
            print('The Sum :', x+y)
            print('The Product :', x*y)
            print('The Sub :', x-y)
            print('The Division :', x/y)
            print('*'*30)
            
        Math_Calculation(20,5)
        Math_Calculation(15,3)
        
c = Calci()
c.m1()

********* Result ********
The Sum : 25
The Product : 100
The Sub : 15
The Division : 4.0
******************************
The Sum : 18
The Product : 45
The Sub : 12
The Division : 5.0
******************************





        
            
            
    








        
            
            
            
