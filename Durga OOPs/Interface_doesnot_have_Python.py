# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 21:43:17 2020

@author: Rajesh
"""

Interface in Python :- 
-------------------
NOTE :- In Python, The interface concept explicitly not available like other
languages such as C++ , Java.

NOTE :- In Python, an interface is an abstract class which contains only abstract methods
method not a single concrete method.

How to Achieve Interface in Python :- 
----------------------------------
First we need to import Abstract method from abc module. like below

from abc import ABC , abstractmethod

where abc = module name 
and ABC = Abstract class name

How to define Interface in Python :- 
---------------------------------
class Father(ABC): # Abstract class extends from ABC which works as Interface.
    
    @abstractmethod
    def display(self): # Abstract method does not contains any implementation.
        pass
    @abstractmethod
    def show(self): # Abstract method does not contains any implementation.
        pass
    
  
NOTE :- In the above example we can see that class it contains only abstract methods    
and means that we can called as Interface.
NOTE :- Interface always contains the abstract methods only.

NOTE :- If a class which contains abstract methods & concreate methods together
then it will called as Abstract class.

Ex :- 

claas Mother(ABC): # Abstract class  extends from ABC.
    
    @abstractmethod
    def display(self): # Abstract method does not contains any implementation.
        pass
     
    def read(self): # Concerate method
        print('concerate method()')
------------------------------------------------------------------------------------------------------
NOTE :- If you want you can use abstract method as well as concerate method in the same class
which will not give any error if are trying to make it as Interface in python.

NOTE :- All methods of an interface as is an abstract.
MOTE :- We can not create an object of interface.
NOTE :- If a class is implementing an interface it has to define all the methods given in that interface.
means we need to provide implementation of all abstract methods inside the subclass
or child class.
NOTE :- If a class does not implement all the methods declared in the interface
then that class has to declare as Abstract class only.

---------------------------------------------------------------------------------------------------------------------

When we use Interface :- 
---------------------
We use interface when all the features need to be implemented differently for
different objects.

from abc import ABC , abstractmethod

class Defence_Force(ABC): # Abstarct class but works also as Interface.
    
    def Gun(self): # Abstract method 
        pass
   
    def Area(self): # Abstract method
        pass
    
class Army(Defence_Force): # Child class
    def Gun(self):
        print('The Army Gun : AK - 41')
    def Area(self):
        print('The Area of Army : Land')
        
class AirForce(Defence_Force):# Child class
    def Gun(self):
        print('The AirForce Gun : AK - 42')
    def Area(self):
        print('The Area of AirForce : Sky')

class Navy(Defence_Force): # Child class
    def Gun(self):
        print('The Navy Gun : AK - 43')
    def Area(self):
        print('The Area of Navy : Sea')
        
ar = Army()        
ar.Gun()
ar.Area()
        
af = AirForce()        
af.Gun()
af.Area()

nv = Navy()        
nv.Gun()
nv.Area()

*********** Result ************
The Army Gun : AK - 41
The Area of Army : Land
The AirForce Gun : AK - 42
The Area of AirForce : Sky
The Navy Gun : AK - 43
The Area of Navy : Sea
-----------------------------------------------------------------------------------------
Ex :- 

from abc import ABC , abstractmethod

class Father(ABC): # Abstract class works as Interface also sometimes.
    
    @abstractmethod
    def display(self): # Abstract Method
        pass
    
class Child(Father): # child class
    def display(self):
        print('Defining the display abstarct method Implemetation in child class')

c = Child() # Object creation of Child class 

c.display() # Accessing abstract method as display by using reference variable.

*************** Result ********
Defining the display abstarct method Implemetation in child class

---------------------------------------------------------------------------------------------------------------
NOTE :- If we have multiple abstarct methods in parent class then we need
to defined all methods implementation in child class then only we can create 
an object & Access easily.

Ex :- 

from abc import ABC , abstractmethod

class Father(ABC): # Abstract class which works as Interface.
    
    @abstractmethod
    def display1(self): # Abstract method
        pass
    @abstractmethod
    def display2(self): # Abstract method
        pass

class Child(Father): # Child class
    def display1(self):
        print('This is Child & display1() method')

class Grand_Child(Child): # GrandChild class
    def display2(self):
        print('This is GrandChild & display2() method')
        

gc = Grand_Child() # Object creation    

gc.display1()
gc.display2()
        
************* Result ***********
This is Child & display1() method
This is GrandChild & display2() method

--------------------------------------------------------------------------------------------------




    

     
    


























