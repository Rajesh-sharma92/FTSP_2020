# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:26:16 2020

@author: Rajesh
"""
How to access members of one class inside another class :- 
-------------------------------------------------------
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        
    def display(self):
        print('The Employee No :', self.eno)
        print('The Employee Name :', self.ename)
        print('The Employee Salary :', self.esal)
       
class Test:
    def modify(emp): # static method coz we are not accessing this method by using any object reference.
        emp.esal = emp.esal+10000
        emp.display()
        
e = Employee(1234,'Rajesh',70000)
Test.modify(e)    

*********************** Result  ****************
The Employee No : 1234
The Employee Name : Rajesh
The Employee Salary : 80000    
------------------------------------------------------------------------------        
Inner Classes :- 
-------------
1) The class is declared inside another class is calles as Inner Class.
2) Without existing one type of object if there is NO chance of existing another
type of object then we should go for inner classes.
Ex :- Car   Engine
      class Car: ----->> Outer class
          ......
          ......
          class Engine: ---->> Inner class
             .........
             .........
Ex :-
        class University: ----->> Outer class
        
            class Department: ---->> Inner class
            
NOTE :- Without university class there will not Department class and both will combine always.

Ex :- 
        class Human: ----->> Outer class
            
            class Head: ---->> Inner class
NOTE :- Without human body is there head is possible ?
Answer : NO , both will be together.

NOTE :- Without existing outer class object there is No chance of existing inner class
object. Inner class object is always associated with outer class objects.
Ex :- 
class Outer:
    def __init__(self):
        print('The outer class object creation .....')
        
    class Inner:
        def __init__(self):
            print('The Inner class object creation .....')
        
        def m1(self):
            print('Inner class method')
        
o = Outer() # The outer class object creation 
i = o.Inner()  # The Inner class object creation
i.m1()   #   Inner class method

Question :- How to access inner class method ?
Answer :- To access inner class method, first we will be creating object for outer class  
then we will create object for inner class by using outer class and later we will be accessing
inner class methods by using the objects of inner class.
------------------------------------------------------------------------------------------
Ex :- 
class Outer:
    def __init__(self):
        print('The outer class object creation .....')
        
    class Inner:
        def __init__(self):
            print('The Inner class object creation .....')
        
        def m1(self):
            print('Inner class method')

i= Outer().Inner() # Object creation for both classes
i.m1() # Accessing inner class method by reference 
-------------------------------------------------------------------------------------
Ex :- 
class Outer:
    def __init__(self):
        print('The outer class object creation .....')
        
    class Inner:
        def __init__(self):
            print('The Inner class object creation .....')
        
        def m1(self):
            print('Inner class method')

Outer().Inner().m1() # Object creation for both classes and accessing the inner class method.
--------------------------------------------------------------------------------------------
Ex :- 
class Outer:
    def __init__(self):
        print('The outer class object creation .....') 
        
    def m2(self):
        print('Outer class method')
        
    class Inner:
        def __init__(self):
            print('The Inner class object creation .....')
        
        def m1(self):
            print('Inner class method')
            
o = Outer() # The outer class object creation
i = o.Inner() # The Inner class object creation
i.m1() # Inner class method
i.m2() # error coz we can not access the outerclass method by using reference if inner class.
o.m2() # Outer class method; here we accessing outer class method by using outer class reference.
-----------------------------------------------------------------------------------------------------
Ex :- WAP to display the DOB of a person by using Inner class.

class Person:
    def __init__(self):
        self.name = 'Rajesh'
        self.dob = self.DOB()
        
    def display(self):
        print('Name :',self.name)
        self.dob.display()
        
    class DOB:
        def __init__(self):
            self.dd=15
            self.mm=8
            self.yyyy=1947
        def display(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
                
p = Person()
p.display()
-------------------------------------------------------------------------------------------


            
                
                
            
            
            
            
            
            
            
            
            
            
            
            
        


            





















        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






            
            
            
            
            
            
                
                
                
                
           
                
             
    































