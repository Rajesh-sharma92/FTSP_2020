# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:56:27 2020

@author: Rajesh
"""
Abstraction in Python :- 
----------------------
Question :- What is an abstract class in python ?
Answer :- A class which contain atleast one abstract method is called as an Abstract class.

Question :- What is an abstract methods in python ?
Answer :- A method which is declared in parent class but does not contain any 
kind of implementation.

Question :- Can we create an object(Instance) of an abstract class in python ?
Answer :- We can not create any object(Instance) of an abstract class in python.
and we just have provide the implementation of abstarct methods inside subclass.

NOTE :- In the abstract class we can not create aobject and we are not able access the 
abstract methods also. Here we will create the object of the subclass of the abstract class
later we will implemnet all abstract methods and accessed also by using the object creation.

NOTE :- Abstract methods which contains only method defination but it does not 
contains any kind of implementation.

Question :- When we will be going for abstract classes ?
Answer :- When we are not sure about our proper requirement then we will be going 
for an abtract class concept and we will be defining some abstract methods inside:
the class and later we can create an object of any subclass and we can access those 
methods by extending that abstract class.

Ex :- 

NOTE :- ABC is the predefined abstract class in python.

from abc import ABC , abstractmethod # Abstract claas importing.

class A(ABC): # Abstract class which contains abtsract methods.
    @abstractmethod
    def display(self):
        None # pass # It does not contain any Implemenatation.
        
class B(A): # Child class / sub class and extends from Parent class like Abstract class.
    
    def read(self): # Child class method
        print('This is Read Method()')
    
    def display(self): # Abstarct method of parent class and Implementation also available.
        print('This is display Method()')
    
b = B() # Object creation of Child class coz we can not create object for Abstract class.
b.read() # Accessing child class method by using reference variable.
b.display() # Accessing parent class abstract method by using reference variable.

************* Result *************

This is Read Method()
This is display Method()

------------------------------------------------------------------------------------------------------------------------------
Ex :- 

from abc import ABC,abstractmethod

class Animal(ABC): # Abstarct class which contains abstract method like eat.
    @abstractmethod
    def eat(self):
        pass # It does not contains any implementation.
    
class Tiger(Animal): # Child class
    def eat(self):
        print('Tiger eats always Non-Veg')
        
class Cow(Animal): # Child class
    def eat(self):
        print('Cow eats always Veg Only')
        
t = Tiger() # Object creation of Tiger class.
t.eat()

c = Cow() # Object creation of Cow class.
c.eat()        
        
************* Result *************
Tiger eats always Non-Veg
Cow eats always Veg Only
-------------------------------------------------------------------------------------------------------------------
NOTE :- Here in the abstract class we can create the Constructor.
----------------------------------------------------------------------------
Question :- If we have multiple abstract methods in the parent class and we will just \
implement only one method in the subclass. So, can we create object for that subclass ?
Answer :- No, We can not If we try to create an object for subclass then it will
give some error like TypeError: Can't instantiate abstract.

Ex :- 

from abc import ABC , abstractmethod

class X(ABC): # Abstract class
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    
class Y(X): # sub class 
    def m1(self):
        print('This is m1() method')

y = Y() # Object creation of subClass Y but we can not coz we have not implemented m2() method.
y.m1() # This is m1() method

************ Result ********
# Object creation of subClass Y but we can not coz we have not implemented m2() method.

TypeError: Can't instantiate abstract class Y with abstract methods m2
----------------------------------------------------------------------------------------------------------------------

Ex :- 

from abc import ABC , abstractmethod

class X(ABC): # Abstract class
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    
class Y(X): # sub class 
    def m1(self):
        print('This is m1() method')
        
class Z(Y): # sub class 
    def m2(self):
        print('This is m2() method')
        

z = Z() # Object creation of subClass Z.
z.m1()  # This is m1() method
z.m2() # This is m2() method

*************** Result *********
This is m1() method
This is m2() method
----------------------------------------------------------------------------------------------------

How to use Constructor in Abstract class :- 
----------------------------------------
NOTE :- Yes, we can use Constructor in the abstract class.

Ex :- 

from abc import ABC , abstractmethod

class Calci(ABC):
    
    def __init__(self,value): # Constructor 
        self.value = value
        
    @abstractmethod   
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    
class B(Calci): # Child Class
    
    def add(self):
        print('Add :', self.value + 100)
    
    def sub(self):
        print('Sub :', self.value - 10)
        
b = B(100)
b.add() # 200
b.sub() # 90

*********** Result ********
Add : 200
Sub : 90

---------------------------------------------------------------------------------------------------------
Ex :- 

from abc import ABC , abstractmethod

class Calci(ABC): # Abstract class
    
    def __init__(self,a,b): # Constructor 
        self.a = a
        self.b = b
        
    @abstractmethod   
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    
class B(Calci): # Child Class
    
    def add(self):
        print('Add :', self.a + self.b)
    
    def sub(self):
        print('Sub :', self.a - self.b)
        
b = B(500,100)
b.add() # 600
b.sub() # 400

************* Result *******
Add : 600
Sub : 400








        
    
    
    
    
    
        







        
    

        
    
        
        







 



    

