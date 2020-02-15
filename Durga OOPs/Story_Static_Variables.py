# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:21:14 2020

@author: Rajesh
"""
" Instance variables vs. Static variables ? "
-----------------------------------------
Instance :- For every object seperate copy will be maintaned.
Static :- For All objects a single copy of variable will be maintained at class level.

Ex :- In the any online class assume that there 100 students are having different - different system
headsets , pen, notebook and etc. but there is one faculty.
All required materials are comes under ---> Instance variables.
Faculty ---> Static variable.

Ex :- class Student:
    cname = 'FORSK CODING SCHOOL'
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        
s1 = Student('Rajesh',101)
s2 = Student('sharma',102)

print(s1.name , s1.rollno , Student.cname)
print(s2.name , s2.rollno , Student.cname)

# print(s1.name , s1.rollno , s1.cname) 
#  print(s2.name , s2.rollno , s2.cname)

# NOTE :- Actually we need to use the classname.static variables while accessing this
recommaned and we can use object reference also. 
syntax :- classname.staticvariable
-----------------------------------------------------------------------------
NOTE :- If there are 1000 students are there in the college and 100 students
are in one particular branch and other are in different branches.

Branches are :- Instance variables like [ CSE , ISE , Mech, Civil]
College name :- static variable.
---------------------------------------------------------------
what are various places are there to declare the static variables :- ?
-----------------------------------------------------------------------
1) Within the class directly but outside of any method.
2) Inside constructor by using classname.
3) Inside Instance method by using classname.
4) Inside classmethod or by using cls variable or classname.
5) Inside static method by using claasname.    
6) From outside of the class by using classname.
Ex :- 
    class Test:
        a = 10
    def __init__(self):
        Test.b = 20
    def m1(self): 
        Test.c = 30
    
    @classmethod
    def m2(cls):
        cls.d = 40
        Test.e = 50
        
    @staticmethod
    def m3():
        Test.f = 60

Test.g = 70    
print(Test.__dict__)  # {a:10 , g : 70} coz a & g are static variables.
NOTE :- We are not calling other function and not creating any object also.
------------------------------------------------------------------------------
Ex :- 
    
class Test:
    a = 10
    def __init__(self):
        Test.b = 20
    def m1(self): 
        Test.c = 30
    
    @classmethod
    def m2(cls):
        cls.d = 40
        Test.e = 50
        
    @staticmethod
    def m3():
        Test.f = 60
        
t = Test()
t.m1()  
t.m2()
t.m3()      
    
Test.g = 70   # Outside the class.
print(Test.__dict__) 
NOTE :- All are static variables.
##############################################################################
How to Access static variables :- 
------------------------------
Within the class we can access by using classname but Inside classmethod
we can also use cls variable.
NOTE :- Coz cls always pointing to class objects.

From outside of the class we can access only by using classname.

NOTE :- We can access static variables either by classname or object reference.

within the class :-
---------------
classname , cls , self

outside of the class :-
--------------------
classname , object reference
Ex :- 
class Test:
    a = 10
    def __init__(self):
        print('Inside Constructor')
        print(Test.a)
        print(self.a)
        
    def m1(self):
        print('Inside Instance Method')
        print(Test.a)
        print(self.a)
        
    @classmethod
    def m2(cls):
        print('Inside class Method')
        print(Test.a)
        print(cls.a)
       
        
    @staticmethod
    def m3():
        print('Inside static method')
        print(Test.a)
        
t = Test()
t.m1()
t.m2()
t.m3()

print('Outside the class')
print(Test.a) # static variable accessing by using classname.
print(t.a)  # static variable accessing by using object reference.

#############################################################################
How to modify the static variables:- 
----------------------------------
with in the class :- 
----------------
We should use classname or cls variable to modify the static variabales.

Outside the class :-
------------------
We can use only classname.
Ex:-
class Test:
    a = 10
    def __init__(self):
        Test.a = 20
        
    @classmethod   
    def m1(cls):
        cls.a = 30
        Test.a = 40
     
    @staticmethod
    def m2():
        Test.a = 50
    
        
t = Test()
t.m1()
t.m2()
# Test.m2()
Test.a = 60 # Outside of the class.
# t.a = 60 # Here static variable value won't be chabged.
print(Test.a) # 20
print(t.a) # 20 
------------------------------------------------------------------------------
How to delete the static variables :- 
----------------------------------
class Test:
    a = 10
    def __init__(self):
       del Test.a
       
print(Test.__dict__)
t = Test() # After creating the object a value will be deleted.
print(Test.__dict__)
----------------------------------------------------------------------------
class Test:
    a = 10 # static variable
     
t = Test() # object Creation.
del t.a # AttributeError: a ; Coz we can't delete the static variable by using the 
object reference variable outside the class.

NOTE :- To delete static variable outside the class, We must use the classname.static variable.
class Test:
    a = 20
t = Test()
del Test.a # classname.static variable we must use.
print(Test.a)
############################################################################
Examples are :- 
-----------------------------
class Test:
    a = 10
    def m1(self):
        self.a=888

t = Test()
t.m1()
print(Test.a) # 10
print(t.a) # 888

---------------------------------------------------------------------------
class Test:
    x = 10 # static variable
    def m1(self):
        self.y = 20 # Instance variable
        
t1 = Test()
t2 = Test()
t1.x = 888
t1.y = 999
print(t1.x , t1.y)
print(t2.x , t2.y)
print(t2.x)
print(t2.y) # AttributeError: 'Test' object has no attribute 'y'
----------------------------------------------------------------------------
class Test:
    x = 10
    def __init__(self):
        self.y = 20
        
t1 = Test()
t2 = Test()
t1.x = 888
t1.y = 999
print(t1.x , t1.y) # 888 999
print(t2.x , t2.y) # 10 20
------------------------------------------------------------------------------
class Test:
    x = 10
    def __init__(self):
        self.y = 20
        
t1 = Test()
t2 = Test()
Test.x = 888
t1.y = 999
print(t1.x , t1.y) # 888 999
print(t2.x , t2.y) # 888 20


















        








































       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       













































































































   
            
            
            
            
            
            
            
            
            
            
            
            
            
          
            














































 







 






























  
    










     

















































