# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:28:43 2020

@author: Rajesh
"""
Inside Python class 3 types of variables :- 
----------------------------------------
1) Instance variables / Object level variables.

Ex :- 
class student:
    def __init__(self,name,rollno):
        print('Constructor will be executed')
        self.name = name
        self.rollno = rollno # Object level variables
        
    def display(self):
        print('Method will be executed')
        print('Hello My Name is :', self.name)
        print('My rollno is :', self.rollno)
        
s1 = student('Rajesh',1001)
s2 = student('Kamesh',1002)
s3 = student('Mohit',1003)

s1.display()
s2.display()
s3.display()        
------------------------------------------------------------------------------    
2) static variables / class level variables :- 
 
Ex :- 
class student:
    cname = 'DURGASOFT' # class level variable and declared with in class only.
    
    def __init__(self,name,rollno):
        print('Constructor will be executed')
        self.name = name
        self.rollno = rollno
        
    def display(self):
        print('Method will be executed')
        print('Hello My Name is :', self.name)
        print('My rollno is :', self.rollno)
        
s1 = student('Rajesh',1001)
s2 = student('Kamesh',1002)
s3 = student('Mohit',1003)

print(s3.cname)
print(s2.cname)
print(s1.cname)

s1.display()
s2.display()
s3.display()           
    
print(id(s1))    
print(id(s2))
print(id(s3))

print(id('cname'))    
------------------------------------------------------------------------------
3) Local variables :- 
Ex :- 
class student:
    def __init__(self,name,rollno):
        print('Constructor will be executed')
        count=0 # Local variables.
        self.name = name
        self.rollno = rollno 
        
    def display(self):
        x = 10 # Local variables.
        print('Method will be executed')
        print('Hello My Name is :', self.name)
        print('My rollno is :', self.rollno)
        
s1 = student('Rajesh',1001)
s2 = student('Kamesh',1002)
s3 = student('Mohit',1003)

NOTE :- Local variables are declared inside the constructor or method and 
accessed within the constructor and method itself and we can't accessed outside of it.

---------------------------------------------------------------------------
Inside Python class 3 types of Methods :- 
----------------------------------------
1) Instance method / object related methods :- 
    
To Access the instance variables inside the method, we need the self variable
and then we can called as this kind of method as instance method.
where we are using the instance variables such kind of method is called instance
or object related methods.
Ex :- 
class student:
    cname = 'DURGASOFT' # Class level variable
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        
    def display(self):
        print('Hello My Name is :', self.name)
        print('My rollno is :', self.rollno)
        
    @classmethod
    def getCollegeName(cls):
        print('The College Name :', cls.cname)
        
    @staticmethod
    def findAverage(x,y):
        print('The Average :', (x+y)/2)
    
            
s1 = student('Rahul',501)
s2 = student('Yogi',502)
s3 = student('Mohit',503)
s1.display()
s2.display()
s3.display()
student.getCollegeName() # DURGASOFT
s1.getCollegeName() # DURGASOFT
                
    
s1 = student('Rahul',501)
s1.findAverage(10,20)
student.findAverage(30,40)
-----------------------------------------------------------------------------
2) Class method :- 
   Ex :-  
    class student:
    cname = 'DURGASOFT' # Class level variable
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        
    def display(self):
        print('Hello My Name is :', self.name)
        print('My rollno is :', self.rollno)
        
    @classmethod
    def getCollegeName(cls):
        print('The College Name :', cls.cname)
        
        s1 = student('Rahul',501)
s2 = student('Yogi',502)
s3 = student('Mohit',503)
s1.display()
s2.display()
s3.display()
student.getCollegeName() # DURGASOFT
s1.getCollegeName() # DURGASOF
-----------------------------------------------------------------------------        
3) static method :- 
    Ex :- 
class student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        
    def display(self):
        print('Hello My Name is :', self.name)
        print('My rollno is :', self.rollno)
        
    @staticmethod
    def findAverage(x,y):
        print('The Average :', (x+y)/2)
    
            
s1 = student('Rahul',501)
s2 = student('Yogi',502)
s3 = student('Mohit',503)
s1.display()
s2.display()
s3.display()
                
s1.findAverage(10,20)
student.findAverage(30,40)

NOTE :- If we are calling without using static method in any function then we should use 
class name for the accessing the methods.:
    
    












