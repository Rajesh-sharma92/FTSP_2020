# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:37:38 2020

@author: Rajesh
"""

Nested Classes  :- 
--------------
class Person:
    def __init__(self):
        self.name = 'Forsk Coding School'
        self.dob = self.DOB()
    def display(self):
        print('Name :', self.name)
        self.dob.display()
        
    class DOB:
            def __init__(self):
                self.dd = 27
                self.mm = 4
                self.yyyy = 2018
            def display(self):
                print('Date of Birth :{}/{}/{}'.format(self.dd,self.mm,self.yyyy))
                
p = Person()
p.display()
      
*********** Result ************
Name : Forsk Coding School
Date of Birth :27/4/2018

---------------------------------------------------------------------------------------------------------
class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name = name
        self.dob = self.DOB(dd,mm,yyyy)
    def display(self):
        print('Name :', self.name)
        self.dob.display()
        
    class DOB:
            def __init__(self,dd,mm,yyyy):
                self.dd = dd
                self.mm = mm
                self.yyyy = yyyy
            def display(self):
                print('Date of Birth :{}/{}/{}'.format(self.dd,self.mm,self.yyyy))
                
p1 = Person('Rajesh sharma',6,1,2020)
p2 = Person('Sandeep Jain',16,6,2019)
p3 = Person('Mohit Sharma',8,11,2015)
p1.display()
p2.display()
p3.display()
          
*********** Result ************
Name : Rajesh sharma
Date of Birth :6/1/2020
Name : Sandeep Jain
Date of Birth :16/6/2019
Name : Mohit Sharma
Date of Birth :8/11/2015
------------------------------------------------------------------------------------------------------------------

class Human:
    def __init__(self):
        self.name = 'Forsk coding school'
        self.head = self.Head()
    def display(self):
        print('Name :',self.name)
        self.head.talk()
        self.head.brain.think()
        
        
    class Head:
        def __init__(self):
            self.brain = self.Brain()
        def talk(self):
            print('Talking ........')
            
        class Brain:
            def think(self):
                print('Thinking .........')
    
h = Human()
h.display()

*********** Result ************
Name : Forsk coding school
Talking ........
Thinking .........
-----------------------------------------------------------------------------------






























               
                
                
                
                