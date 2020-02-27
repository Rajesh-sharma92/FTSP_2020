# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:17:57 2020

@author: Rajesh
"""
Operator Overloading :- 
--------------------
class Book:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        return self.pages + other.pages
        
b1 = Book(100)  
b2 = Book(200)   
b3 = Book(700)  
  
print(b1+b2) # 300
print(b1+b3) # 800
print(b2+b3) # 900

NOTE :- The return type of the __add__() magic method will be integer type.
---------------------------------------------------------------------------------------------------------------
Ex :- 
class Book:
    def __init__(self,pages):
        self.pages = pages
    
    def __str__(self):
        return 'Forsk'
        
b1 = Book(100) 
print(b1) # Forsk
b2 = Book(200)
print(b2) # Forsk

NOTE :- Actually, we need to print the no. of pages in a book not a printing simply any return string name.

class Book:
    def __init__(self,pages):
        self.pages = pages
    
    def __str__(self): # magic method for single object like b1 printing.
        return 'The No. of Pages :' + str(self.pages)

b1 = Book(100) 
print(b1) # The No. of Pages :100

NOTE :- We are using __str__() method to print a single values like print(b1). then we should this method
and return the string values and always we need to type cast of these values.

-----------------------------------------------------------------------------------------------------------------
class Book:
    def __init__(self,pages):
        self.pages = pages
    
    def __str__(self): # magic method for single object like b1 printing.
        return 'The No. of Pages :' + str(self.pages)
    
    def __add__(self,other):
        return self.pages + other.pages

b1 = Book(100) 
b2 = Book(200)
b3 = Book(300)
print(b1) # The No. of Pages :100
print(b1+b2) # 300
print(b1+b2+b3) # unsupported operand type(s) for +: 'int' and 'Book'.
--------------------------------------------------------------------------------------------------
Question :- How to print the values of like print(b1+b2+b3) by using operator overloading in python.

class Book:
    def __init__(self,pages):
        self.pages = pages
    
    def __str__(self): # magic method for single object like b1 printing.
        return 'The No. of Pages :' + str(self.pages)
    
    def __add__(self,other):
        total = self.pages + other.pages # total no. of pages of b1+b2
        b = Book(total) # creating one more object like b
        return b 
        
b1 = Book(100) 
b2 = Book(200)
b3 = Book(300)
b4 = Book(700)
b5 = Book(1000)

print(b1) # The No. of Pages :100
print(b1+b2) # The No. of Pages :300
print(b1+b2+b3) # The No. of Pages :600
print(b1+b2+b3+b4) # The No. of Pages :1300
print(b1+b2+b3+b4+b5) # The No. of Pages :2300
--------------------------------------------------------------------------------------------------------------
NOTE :- Whenever we are calling + operator then __add__() method will be called.
+ operator return type will become __add__() method return type.
NOTE :- Whenever we are printing book object reference / object then __str__() method will be called.
If we are not providing this method then default implemention will be executed.


class Book:
    def __init__(self,pages):
        self.pages = pages
    
    def __str__(self): # magic method for single object like b1 printing.
        return 'The No. of Pages :' + str(self.pages)
    
    def __add__(self,other):
        total = self.pages + other.pages # total no. of pages of b1+b2
        b = Book(total) # creating one more object like b
        return b 
    
    def __mul__(self,other):
        total = self.pages * other.pages # total no. of pages of b2*b3
        b = Book(total) # creating one more object like b
        return b 
        
b1 = Book(100) 
b2 = Book(200)
b3 = Book(300)
b4 = Book(700)
b5 = Book(1000)

print(b1) # The No. of Pages :100
print(b1+b2) # The No. of Pages :300
print(b1+b2+b3) # The No. of Pages :600
print(b1+b2*b3+b4) # The No. of Pages :60800

-------------------------------------------------------------------------------------------------------
class student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
s1 = student('Rajesh',100)
s2 = student('sharma',200)

print(s1<s2) # TypeError: '<' not supported between instances of 'student' and 'student'.
-----------------------------------------------------------------------------------------------------
Question :- How to check the 2 students marks are greater or less then between them by using operator loading ?
Answer :- Yes, We can do it by using the __lt__() magic method and can check the condition is True or False.

class student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def __lt__(self,other):
        return self.marks < other.marks
        
s1 = student('Rajesh',100)
s2 = student('sharma',200)

print(s1<s2) # True
print(s1>s2) # False
----------------------------------------------------------------------------------------------------
Question :- How to display the employee salary as per operator overloading ?
Answer :- Yes, We can display it by using __mul__() magic method.

class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def __mul__(self,other):
        return self.salary * other.days
        
class TimeSheet:
      
    def __init__(self,name,days):
        self.name = name
        self.days = days
        
       
e = Employee('Rajesh',500)
t = TimeSheet('Rajesh',25)

print('This Month Salary :', e*t) # This Month Salary : 12500
print('This Month Salary :', t*e) # TypeError: unsupported operand type(s) for *: 'TimeSheet' and 'Employee'
--------------------------------------------------------------------------------------------------
class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def __mul__(self,other):
        return self.salary * other.days
        
class TimeSheet:
      
    def __init__(self,name,days):
        self.name = name
        self.days = days
        
    def __mul__(self,other):
        return self.days * other.salary
        
       
e = Employee('Rajesh',500)
t = TimeSheet('Rajesh',25)

print('This Month Salary :', e*t) # This Month Salary : 12500   
print('This Month Salary :', t*e) # This Month Salary : 12500 

 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        









































































































































