# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:14:46 2020

@author: Rajesh
"""

Method Overriding :-
-----------------
Inheritance :-
-----------

class P:
    10 methods are there

class C extends P: # In Java child class created.
    5 more methods are there

class C(P): # In Python child class created.
    5 more methods are there
    
class C(P1,P2,P3 .....Pn): # In Python child class created by any no. of parents classes.
    5 more methods are there
    
NOTE :- Parent class is having only 10 methods.
NOTE :- Child class is having 15 methods coz 10 methods from parent class & 5 from itself and Total = 15 methods.
NOTE :- We can see that Inheritance is very powerful concept in the python.
1) Code Re-usability.
2) Existing functionality we can extend.
--------------------------------------------------------------------------------------------------------------
class P: # parent class
    
    def property(self): # parent class Method
        print('cash+land+gold+power')
        
    def marry(self): # parent class Method
        print('Marry with Deepka sharma')
        
class C(P):pass
# pass
c = C() # Object creation for child class.

c.property() # cash+land+gold+power
c.marry() # Marry with Deepka sharma

************ Result **********
cash+land+gold+power
Marry with Deepka sharma

NOTE :- We can see that the child is capable to use parent things without any issue.
------------------------------------------------------------------------------------------------------
class P:
    def property(self): # parent class Method
        print('cash+land+gold+power')
        
    def marry(self): # parent class Method
        print('Marry with Deepka sharma')  
        
class C(P):
    
    def marry(self): # Child class Method
        print('Marry with Sunny Leoney from Forsk') 

c = C()  # Object creation for child class.

c.property() # cash+land+gold+power
c.marry() # Marry with Sunny Leoney from Forsk

************ Result **********
cash+land+gold+power
Marry with Sunny Leoney from Forsk
----------------------------------------------------------------------------------------------------
class P:
    def property(self): # parent class Method
        print('cash+land+gold+power')
        
    def marry(self): # parent class Method
        print('Marry with Deepka sharma')  
        
class C(P):
    
    def marry(self): # Child class Method
        super().marry()    
        print('Marry with Sunny Leoney from Forsk') 
    

c = C()  # Object creation for child class.

c.property() # cash+land+gold+power
c.marry() # Marry with Sunny Leoney from Forsk

************ Result **********

cash+land+gold+power
Marry with Deepka sharma
Marry with Sunny Leoney from Forsk
--------------------------------------------------------------------------------------------------


        
    

        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

























    