# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:13:29 2020

@author: Rajesh
"""
Question :- can we declare both cls & self in one method only ?
Answer :- Yes, We can but it is not good approach and it will be working as Instance method
only coz we will not using @classmethod decorators.
NOTE :- In the below example cls works as first like self variable and self will be working as
local variable.

class Test:
    
    def m1(cls,self): # Internally,this method will be works as Instance method.
        cls.x = 10
        print('Instance method :', cls.x,self)
        
t = Test()
t.m1('Forsk coding school')        
-----------------------------------------------------------------------------
class Test:
    
    def m1(cls,self): # Internally,this method will be works as Instance method.
        cls.self = self
        print('Instance method :', cls.self)
        
t = Test()
t.m1('Forsk coding school')        
------------------------------------------------------------------------------
# This is the proper way of using the Instance Method.
class Test:
    
    def m1(self,name):
        self.x = 10
        print('Instance Method :', self.x,name)
     
t = Test()
t.m1('Forsk')
-----------------------------------------------------------------------------
static method :- 
------------
Just general utility method / helper methods.
Ex :- 
class Test:
    
    @staticmethod
    def sum(x,y):
        print('The sum of two variables are :', x+y)
    
t = Test() # object creation but It is not compulsory to create object & then access. We can by using classname itself.

t.sum(10,20) # It is not recommmaned but we can access.

Test.sum(100,25) # This is right approach to Access the static method.

Test.sum(30,70)
------------------------------------------------------------------------------
class Test:
    
    @staticmethod
    def square(a):
        print('The square of no :', a*a)
       
Test.square(2) # Accessing by using the classname.This is right approach to Access the static method.
------------------------------------------------------------------------------        
class ForskMath:
    
    @staticmethod
    def add(x,y):
        print('The sum :',x+y)
    @staticmethod   
    def sub(x,y):
        print('The subtract :',x-y)
    @staticmethod    
    def mul(x,y):
        print('The Multiple :',x*y)
    @staticmethod  
    def div(x,y):
        print('The Division :',x/y)
    @staticmethod  
    def average(x,y):
        print('The Average :', (x+y)/2)
 
ForskMath.add(20,10)
ForskMath.sub(100,20)
ForskMath.mul(20,10)
ForskMath.div(100,5)    
ForskMath.average(20,10)
-----------------------------------------------------------------------------

Instance method vs. Classmethod vs. Static method :-
-------------------------------------------------
1) If we are using any instance variables inside method body then we should go for 
   Instance method. We should call & access by using object reference.

2) If we are using only static variable then we should go for Classmethod and 
we must use the @classmethod decorators. To call we shuould use by classname or
object reference and recommanded by classname only.

3) If we are not using any Instance variable & static variable inside method body
then, to define such type of general utility methods, we should go for static method.
To call we shuould use by classname or object reference and recommanded by classname only.

If we are not using any decorator :-
---------------------------------
for class method---> @classmethod decorator is mandatory.

for static method ---> @staticmethod decorator is optional.:
    
NOTE :- without any decorator the method can be instance method  or static method.
--> If we are calling by using object reference then we should declare that 
method as Instance method.

----> If we are calling by using classname then we should declare that method
as static method.
------------------------------------------------------------------------------
EXamples :- 
--------
class Test:
    
    def m1(): # Instance method
        print('some method')
t = Test()
t.m1() # TypeError: m1() takes 0 positional arguments but 1 was given.
# NOTE :- In the above,example PVM will be considering this method as Instance method but
not declaring the self variable in this method.
-----------------------------------------------------------------------------
class Test:
    
    def m1(): # static method and it takes zero no. of arguments like we can give or leave empty also.
        print('some method')
        
Test.m1() # some method
# NOTE :- It is valid and PVM will be considering this method as static method and 
takes zero or more arguments.
------------------------------------------------------------------------------   
class Test:
    @staticmethod
    def m1(): # static method and it takes zero no. of arguments like we can give or leave empty also.
        print('some method')
        
Test.m1() # some method
------------------------------------------------------------------------------
class Test:
    
    def m1(x):
        print('some method', x)
 
t = Test()
t.m1(10) # TypeError: m1() takes 1 positional argument but 2 were given.
-------------------------------------------------------------------------------




    
      
        










 













        
        











    

    
    
 








































  
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








































        
        
        
        








