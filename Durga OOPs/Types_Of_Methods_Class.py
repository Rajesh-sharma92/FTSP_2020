# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:40:02 2020

@author: Rajesh
"""
Types of Methods :- 
----------------
1) Instance method
2) Class method
3) Static method

1) Instance method :- If we are using atleast one instance variable is called as Instance method.

2) Class method :- If we are using only static variables but not the instance variables 
are called as Class method.

3) Static method :- If we are not going to use any static or Instance methods then it is
called as Static method. Static methods are also called as General Utility Methods.

How to declaare the Instance method :- 
-----------------------------------
def m1(self): # It always starts with self variable.
    self.x  # To access the Instances members of this function. 'x' is instance member.
    
How to declaare the Class method :- 
----------------------------------- 
@classmethod
def m1(cls):
    cls.x
    Test.x # By using classname also we can Access.

How to declaare the Static method :- 
-----------------------------------   
@staticmethod
def add(x+y):
    print(x+y)

##############################################################################
Instance Method :-
---------------
def m1(self):
    we are using Instance variables.
    NOTE :- Always first argument in instance method will be self only.
    
To Access :-
---------    within the class by using self.
outside of the class by using object reference.
------------------------------------------------------------------------------
Ex :- By using for Loop this program written.

class student:
    def __init__(self,name,marks):
        self.name = name # Instance variable
        self.marks = marks # Instance variable
        
    def display(self): # Instance method coz we are using Instance variable inside in this.
        print('Hi', self.name)
        print('Your marks are :', self.marks)
        
    def grade(self):
        if self.marks > 60:
            print('First grade')
        elif self.marks >=50:
            print('Second grade')
        elif self.marks >=35:
            print('You got Third grade')
        else:
            print('you are failed')
            
n = int(input('Enter No. of students :'))
for i in range(n):
   name = input('Enter student name :')
   marks = int(input('Enter student marks :'))
   s = student(name,marks)
   s.display() # Accessing the method outside of the class by using Object reference.
   s.grade() # Accessing the method outside of the class by using Object reference.
   print('*'*20)
   
------------------------------------------------------------------------------
Ex :- By using while Loop this program written.

class student:
    def __init__(self,name,marks):
        self.name = name # Instance variable
        self.marks = marks # Instance variable
        
    def display(self): # Instance method coz we are using Instance variable inside in this.
        print('Hi', self.name)
        print('Your marks are :', self.marks)
        
    def grade(self):
        if self.marks > 60:
            print('First grade')
        elif self.marks >=50:
            print('Second grade')
        elif self.marks >=35:
            print('You got Third grade')
        else:
            print('you are failed')
            
n = int(input('Enter No. of students :'))
count = 1
while(count<=n):
   
   name = input('Enter student name :')
   marks = int(input('Enter student marks :'))
   s = student(name,marks)
   s.display() # Accessing the method outside of the class by using Object reference.
   s.grade() # Accessing the method outside of the class by using Object reference.
   print('*'*20)
   count = count + 1
------------------------------------------------------------------------------
























   
   
                        
                    
                    
                    
                    
                    
                    
                    
            
            
            
            
            
            
            
            
            
            
 

























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    