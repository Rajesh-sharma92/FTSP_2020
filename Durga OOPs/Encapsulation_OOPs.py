# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:33:17 2020

@author: Rajesh
"""
Encapsulation in Python :- 
-----------------------
1) In OOPs python program, you can restrict access to Methods & Variables.
2) This can be prevent the data from being modified by accidently and is known as encapsulation.
3) Encapsulation can be achived using private variables & private methods.

-------------------------------------------------------------------------------------------------------------------------------

Scope of private variables & private methods :- 
--------------------------------------------
There are some important points are listed below.

1) public methods :- Access from anywhere in the class.

2) private methods :- Access only in their own class. It starts with two underscores
like __display()

3) public variables :- Access from anywhere in the class.

4) private variables :- Access only in their own class or by a method defined.
It starts with two underscores like __x1 = 10

------------------------------------------------------------------------------------------------------------------------
private variables :- private variables can be access only within the method.
-----------------

Ex :- 

class myClass:
    __a = 10 # private variable and starts with two underscores.
    
    def display(self):
        print(self.__a) # private variables can be access only within the method.
        
mc = myClass() # Object creation of myClass
mc.display() # Accessing the private variables by using object refrence variables like mc.

print(myClass.__a) # AttributeError: type object 'myClass' has no attribute '__a'. We can not access outside of the class.

NOTE :- In the above example we can see that private variables(__a) can be 
accessed with in method of the same class inside the class only.

NOTE :- private variables(__a) can not be accessed outside of the class and If we 
try access them then we will getting an error like AttributeError.
---------------------------------------------------------------------------------------------------------------------
private methods :- Private method can be access only within the methods.
---------------

Ex :- 

class myClass: # className
    def __display1(self): # private method and It starts with two underscores.
        print('This is display1 method()')
        
    def display2(self): # public method and access from anywhere in the class.
        print('This is display2 method()')
        self.__display1() # private method accessing within method or class only.
        
mc = myClass() # object creation of myClass.
mc.display2() # We are accessing display2() method outside of the class and easily we can do coz it is public method.

#mc.__display1() # AttributeError: 'myClass' object has no attribute '__display1'. We can  not access private method outside of the class.

myClass.__display1() # AttributeError: type object 'myClass' has no attribute '__display1'

********** Result *****************
This is display2 method()
This is display1 method()

NOTE :- private method accessing within method or class only and we can easily 
accessed with any issue but If we are trying to access private method (__display1())
then we will getting an error like AttributeError.

NOTE :- We can access public method anywhere inside or outside of the class.

NOTE :- We can not access private method outside of the class by using ClassName(myClass).
and we try to accessed then we will be getting an error like AttributeError.

--------------------------------------------------------------------------------------------------------------------------------

private variables :- We can access private variables outside of the class indirectly by using method.
-----------------
Ex :- 

class myClass: # ClassName
    __empid = 1001 # private variable.
    
    def get_empid(self,eid):# private variables can be access only within the method.
        self.__empid = eid
        
    def disp_empid(self): # It works as Indirectly method.
        print(self.__empid) # It prints the Private variable indirectly on console.
        
mc = myClass() # object creation of myClass.

mc.disp_empid() # 1001 --> Here we are accessing private variables indirectly outside of the class.

************* Result ************
1001
--------------------------------------------------------------------------------------

Ex :- Here we can re-assign the value to private variable.

class myClass: # ClassName
    __empid = 1001 # private variable.
    
    def get_empid(self,eid):# private variables can be access only within the method.
        self.__empid = eid
        
    def disp_empid(self): # It works as Indirectly method.
        print(self.__empid) # It prints the Private variable indirectly on console.
        
mc = myClass() # object creation of myClass.

mc.get_empid(2001) # Value re-assigning.

mc.disp_empid() # 2001 --> Here we are accessing private variables indirectly outside of the class.

************* Result ************
2001

---------------------------------------------------------------------------------------------------------------------------------
class Hello:
    def __display(self):
        print('Private Method ()')
        
    def disp(self):
        print('public method like display ()')
        print(self.__display())
        
h = Hello()
h.disp()

********** Result ************

public method like display ()
Private Method ()

--------------------------------------------------------------------------------------

        
        

        
        
        
        



















        



