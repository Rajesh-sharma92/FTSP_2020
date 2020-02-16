# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:43:24 2020

@author: Rajesh
"""
Setter And Getter Methods :-
--------------------------
NOTE :- It is also used to assign & getting the details like constructor and it
is alternative way of constructor.

def __init__(self,name,marks):
    self.name = name
    self.marks = marks
    
s = student('Rajesh',100) # Object creation and passing the data.
-----------------------------------------------------------------------------
s = student() # empty Object creation and we are not passing any kind of data.
s.setName('Rajesh')
s.setMarks(100)
print('student Name :', getName())
print('student Marks :', getmarks())
-----------------------------------------------------------------------------
NOTE :- Setter & getter methods are not build-in methods. we just need to use for making 
program as easy.
NOTE :- setter methods are used for set the data for objects.
NOTE :- Getter methods are used to get the data  from object.
NOTE :- These above methods are used for security purpose in the projects.
syntax :- 
------
def setVariableName(self,VariableName):
    self.VariableName = VariableName
    
 Ex :- 
 def setMarks(self,marks):
     self.marks = marks
     
syntax :-
------
def getMarks(self):
    return self.marks
------------------------------------------------------------------------------
NOTE :- Can we define like this below way for setter & getter methos.
Ex :-
    def setMarks(self,name,marks): # yes, you can but there is No security.
    
 Ex :- 
 def setMarks(self,marks):
     # validation stuff
     self.marks = marks
Ex :- 
print(s.name) # direct Access No Validation.
print(s.getName()) # security will be there.

NOTE :- data Hiding will be behind the methods ==> Encapsulation.
NOTE :- setter & getter methods are used in the Industry and it is good for data security.
and It's highly recommanded use the data in industry by using setter & getter methods.
Ex:- 
if age is the instance variable then used like this....

def setAge(self,age): # we need to use Instance variable name with settter and getter methods.
    self.age = age
    
NOTE :- The biggest advantage with Encapsulation is security.
The biggest dis-advantage with Encapsulation is length of the will be Increased 
and readability of the code will be down and performance issue will down.

NOTE :- Can we perfrom validations stuff inside Constructor ?
Yes , We can do it but Constructor will be using to initaliaze the values for 
instance variables & it is not good practice as programmer.
-----------------------------------------------------------------------------
Ex:- 
class student:
    
    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setMarks(self,marks):
        self.marks = marks
        
    def getMarks(self):
        return self.marks
    
n = int(input('Enter No. of students :'))
for i in range(n):
    
    name = input('set the name :')
    marks = int(input('get the marks are :'))
    
    s = student()
    s.setName(name)
    s.setMarks(marks)
    print('Hi',s.getName())
    print('Your marks are :', s.getMarks())
    print('*'*20)
    
-----------------------------------------------------------------------------    
NOTE :- Setter & getter methods are instance Methods  for student Object.   
NOTE :- No. of setter & getter methods are based on No. of Instance variables.
------------------------------------------------------------------------------

 
    
    
    
    
    
    



    
    
    









































































    
 

