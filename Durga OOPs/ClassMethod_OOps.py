# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:44:42 2020

@author: Rajesh
"""
NOTE :- Inside method body if we are accessing only class level(static variables) data.
what is the need of declaring as instance method.

s = student() # object creation for class student.
s.m1() # Accessing the method m1() by using the 's' object reference.
NOTE :- It is very costlty operation coz we need to create the object then access.
NOTE :- In Instance method we can't access without object creation coz we need
the object reference.
NOTE :- Inside class methos easily we can access. We just need to use the 
classname.method name. 
Ex :- student.m1()
      student.Average()
    
NOTE :- Internally, performance will be there.
NOTE :- If you are accessing only static variables in the class then better to 
use the @classmethod decorators. 

NOTE :- If we are using atleast one instance variable then compulsory we have
to declared that method as Instance method.

NOTE :- Until, If not necessary then pls do not go for Instance method coz we
need to accessing method by using object reference & it is very costly operation.
so, better to use @classmethod.
------------------------------------------------------------------------------
How to accessing by using Instance method :-
-----------------------------------------
def m1(self): # self is the reference variable to pointing to the current object.
    print(self.name)
    print(self.marks)
    print(self.rollno)
--------------------------------------------------------------------------
How to Declare & Accessing by using Class method :-
------------------------------------------------
NOTE :- Every class method compulsory should contains atleast one argument like 'cls'.
NOTE :- cls means current class object.

def m1(cls):
    print(cls.collegename)
    print(cls.bankname)
     
NOTE :- We are able to access class level variables means static variables.
NOTE :- Instance method does not use any decorators but class method compulsory
shoud use the @classmethod decorators.

@classmethod 
def m1(cls):
    print(cls.collegename)
    
  
NOTE :- By using self we can access only Instance variables & by using cls 
we can access only class level variables or static variables.

NOTE (Question) :- Anyway, we are passing cls variable which is used as class then why we
are again using @classmethod ???
Answer :- We are passing @classmethod coz there is one more concept like @staticmethod.
and it can treated as @staticmethod. So to differentiate in both of it.

NOTE :- Inside Instance method we can access the Instance variables as well as
static variables also.

NOTE :- Inside static method we can only access class level variables means static variables.

Instance methos vs. Class method :-
--------------------------------
1) Inside method body if we are using atleast one instance variable then compulsory 
   we should declare that method as Instance method.
1) Inside method body we are using only static variable then it is highly recommanded
   to declare that metod as Class method.
2) To declare any instance method we are not required to use any decorators.
2) To declare class method compulsory we must have to use @classmethod decorators.
3) The first argument to the instance method should be self; and which is refering
   to the current object by using self, we can access instance variables inside the method.
3) The argument to the classmethod should be the cls and which is refereing to the 
    current class object and by using that we can access static variables.
4) Inside instance method we can access both instance variables and static variables 
4) Inside classmethod we can access only the static variables and we can not 
   access instance variables.
5) We can call instance method by using object reference.
5) We can call classmethod either by using object referencce or by using classname.
   but recommanded to use classname.
Ex :- 
---
class Animal:
    legs = 4 # static variable.
    
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))
        
Animal.walk('dog') # We can access by using classname and NO need to create oject and which is called as level variables.
Animal.walk('cat')
------------------------------------------------------------------------------
## WAP to track no. of objects created for a class ??.

class Test:
    count = 0 # static variable
    def __init__(self):
        Test.count = Test.count+1

    @classmethod
    def getNoOfObjects(cls):
        print('The No. of objects are created :', cls.count)
        
t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()   

Test.getNoOfObjects() # Accessing the method by using the classname.






















   

   
   
    
    
    
    
    
     
    
    
   
   
 














































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









    
      







