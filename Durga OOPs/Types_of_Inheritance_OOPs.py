# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:17:46 2020

@author: Rajesh
"""

Types of Inheritance :- 
--------------------
IS-A vs. Has-A Relationship :-
---------------------------
Composition vs. Aggregation :-
---------------------------
Boy friend vs. Girl friend :- 
--------------------------
Boy friend :-  
----------
without you i can not be ==> strong association --->> Composition
without you also i can be ==> Weak association  --->> Aggregation

Ex :- 
University  vs. Department ==> Strongly Associated 
University(Container) , Departments(Contained) -->> Both are strongly associated.

University  vs. Department ==> Strongly Associated 
University Has-A Department  but ==> Strongly Associated 

Department vs Professer --- >> Weakly associated -->  Aggregation Concept.
Department Has-A Professer

Department(Container) Object , Professer (Contained) object
------------------------------------------------------------------------------------------------------
Ex :- 

class Student:
    
    collegeName = 'Forsk coding school'
    
    def __init__(self,name):
        self.name = name
        
s = Student('Rajesh')
print(s.name) # Rajesh

print(Student.collegeName) # static variable & Student class we can access without any restrictions.
print(s.collegeName) # static variable & Student class object reference 
   
NOTE :- Student & name are strongly associatied and this is called Composition.
Coz student is there means name will be coming or else it does not exist itself.

NOTE :- CollegeName & student are weak associated and this is called Aggregation.
Coz newly opened college and there is NO student so we can say if there is No student but
collegeName will be there and finally we can say that weakly associated and it is Aggregation.

NOTE :- Inner class is also related to the Composition means like If there is No outer class then
there will not Inner class possibility.
-------------------------------------------------------------------------------------------------------
Types of Inheritance :- 
--------------------

1) Single Inheritance
2) Multi level Inheritance
3) Hierarchical Inheritance
4) Multiple Inheritance
5) Hybrid Inheritance
6) Cyclic Inheritance
 
NOTE :- Python provides support for all these above Inheritance except Cyclic Inheritance and 
in the real it does not required (Cyclic Inheritance) at all in python.
--------------------------------------------------------------------------------------------------------------------------------
1) Single Inheritance :- It contains only single parent & single child is called as Single Inheritance.
   -----------------
       P --> Parent class
       |
       |
       C --> Child class
       
       # Fig :- Single Inheritance

class P: # Parent class
    def m1(self):
        print('Parent method')
    
class C(P): # Child class
    def m2(self):
        print('Child method')
        
c = C() # Object creation for child class.

c.m1() # Parent method
c.m2() # Child method

************* Result **************
Parent method
Child method      

NOTE :- By seeing, that above example of Single Inheritance and we can say that child will be having the Access
Parent class method as well as extra methods of itself also. It is very simple & easy to use.

NOTE :- Code Re-useability is there and Code extensions are there too.
---------------------------------------------------------------------------------------------------------
2) Multi level Inheritance :- It contains multiple parents & multiple childs are there.
   ----------------------- 
                    A ---> Parent class
                    |
                    B ----> Child class ---> Parent class for child c class 
                    |
                    C -----> child class ---> Parent class for child D class 
                    |
                    D -----> Child class ----> 
                    
                    # Fig :- Multi level Inheritance

class A:
    
    def m1(self):
        print('Parent class of method() --> A')
    
class B(A):
    
    def m2(self):
        print('Child class of metohod() --> B')
        
class C(B):
    
    def m3(self):
        print('Child class of metohod() --> C')
        
class D(C):
    def m4(self):
        print('Child class of metohod() --> D')
        
b = B() # Object creation for Child class B.
b.m1()
b.m2()

c = C() # Object creation for Child class C.
c.m1()
c.m2()
c.m3()

d = D() # Object creation for Child class D.
d.m1()
d.m2()
d.m3()
d.m4()

a = A()  # Object creation for Parent class A.
a.m1()

***************** Result *************
Parent class of method() --> A
Child class of metohod() --> B
Parent class of method() --> A
Child class of metohod() --> B
Child class of metohod() --> C
Parent class of method() --> A
Child class of metohod() --> B
Child class of metohod() --> C
Child class of metohod() --> D
Parent class of method() --> A

Ex :- 

class Parent:
    def m1(self):
        print('Parent class method m1()')
        
class Child(Parent):
    def m2(self):
        print('Child class method m2()')
        
class Sub_Child(Child):
    def m3(self):
        print('Sub-Child class method m3()')
        
sc = Sub_Child() # Object creation for Sub_Child class.
sc.m1()
sc.m2()
sc.m3()

c = Child() # Object creation for child class.
c.m1()
c.m2()

p = Parent() # Object creation for parent class.
p.m1()

************** Result ************
Parent class method m1()
Child class method m2()
Sub-Child class method m3()
Parent class method m1()
Child class method m2()
Parent class method m1()

-----------------------------------------------------------------------------------------------------------
3) Hierarchical Inheritance :- One parent but multiple childs at same level.
   ------------------------ 
                    Parent  # One Parent class 
                  |     |   |  
                  |     |   |
                  |     |   |
               Child Child Child # Many child classes at same level.
               
               # Fig :- Hierarchical Inheritance
               
Ex :- 
class P:
    def m1(self):
        print('Parent class method m1()')
        
class C1(P):
    def m2(self):
        print('Child1 class method m2()')
        
class C2(P):
    def m3(self):
        print('Child2 class method m3()')
        
c1 = C1()    # Object creation for Child1 class.
c1.m1()
c1.m2()

c2 = C2()   # Object creation for Child2 class.
c2.m1()
c2.m3()

p = P()     # Object creation for Parent class.
p.m1()

****************** Result ****************
Parent class method m1()
Child1 class method m2()
Parent class method m1()
Child2 class method m3()
Parent class method m1()
--------------------------------------------------------------------------------------------------------
4) Multiple Inheritance :- Multiple Parents & only Single child is called as Multiple Inheritance.
   -------------------- 
           P1  P2  P3  P4  --->> Multiple Parents
           |    |   |   |
           |    |   |   |
           ---------------
                 || 
                Child   --->> Single child 
                
           # Fig :- Multiple Inheritance     
Ex :- 

class P1: # Parent class
    def m1(self):
        print('Parent p1 class method m1()')
        
class P2: # Parent class
    def m1(self):
        print('Parent p2 class method m1()')
        
class C(P1,P2): # Child class
    pass

c = C() # Object creation for Child class C.
c.m1() # Parent p1 class method m1()

************ Result *********
Parent p1 class method m1()
---------------------------------------------------
NOTE :- We can say that there are 2 parents classes & both the parents classes contains have same m1() method 
only one child class is there and If we create the Object for child class then which m1()
will be called first. Always Parent p1 class method m1() will be executed first coz order is very 
Important there and after that Parent P2 class m1() will be executed.

NOTE :- As we said, that order is very important in the Multiple Inheritance and If Parent P1 class 
does not contain any kind of methods then the next parent (p2) class methods will be executed first.
---------------------------------------------------------------------------------------------------
Ex :-
class P1: # Parent P1 class & doesn't contain any method.
    pass

class P2: # Parent P2 class & it contain m1() method.
    def m1(self):
        print('Parent P2 class method m1()')
        
class C(P1,P2): # Child class cretaed with help of multiple parent classes.
    pass

c = C() # Object creation for Child class.
c.m1() # Parent P2 class method m1() # Coz Order is very Important but Parent p1 class doesn't contain any method so, P2 class m1() will be executed first.

********** Result ********
Parent P2 class method m1()

NOTE :- Coz Order is very Important but Parent p1 class doesn't contain any method 
so, P2 class m1() will be executed first.

NOTE :- In the hospital if there is any emergency case came first of all hospital people  will be 
asking the point of contact nos. like first no. , second no.  and alternative no. also.
First they will be calling to first no. and if NO response from first no then go for second and If no 
response from second no also then finally they will be going for altrenative no and it will be connected at last.

NOTE :- Same like Insurence also.

class P1: # Parent P1 class and It contain m1() method.
    def m1(self):
        print('Parent P1 class method m1()')

class P2: # Parent P2 class & it contain m1() method.
    def m1(self):
        print('Parent P2 class method m1()')
        
class C(P2,P1): # Child class cretaed with help of multiple parent classes.
    pass

c = C() # Object creation for Child class.
c.m1() # Parent P2 class method m1()

******** Result *********
Parent P2 class method m1()
NOTE :- Order is very important in multiple Inheritance in Python.

NOET :- If child class is having any mehtod then first child class all methods will be executed
first not any parent methods.
Ex :- 

class P1: # Parent P1 class
    def m1(self):
        print('Parent P1 class m1() method ')
        
class P2: # Parent P2 class
    def m1(self):
        print('Parent P2 class m1() method')
        
class C(P1,P2): # Child class cretaed with help of multiple parent classes.
    def m1(self):
        print('Child class m1() method')
        
c = C() # Object creation for Child class.
c.m1() # Child class m1() method

************* Result **********
Child class m1() method
------------------------------------------------------------------------------------------

class P1: # Parent P1 class
    def m1(self):
        print('Parent P1 class m1() method ')
        
class P2: # Parent P2 class
    def m1(self):
        print('Parent P2 class m1() method')
        
class C(P1,P2): # Child class cretaed with help of multiple parent classes.
    def m1(self):
        print('Child class m1() method')
        
    def m2(self):
        print('Child class m2() method')
        
c = C() # Object creation for Child class.
c.m1() # Child class m1() method
c.m2() # Child class m2() method

************* Result **********

Child class m1() method
Child class m2() method
-----------------------------------------------------------------------------------------------------
class P1: # Parent P1 class
    def m1(self):
        print('Parent P1 class m1() method ')
        
    def m2(self):
        print('Parent P1 class m2() method')
        
class P2: # Parent P2 class
    def m1(self):
        print('Parent P2 class m1() method')
        
class C(P1,P2): # Child class cretaed with help of multiple parent classes.
    def m1(self):
        print('Child class m1() method')
        
        
c = C() # Object creation for Child class.
c.m1() # Child class m1() method
c.m2() # Parent P1 class m2() method

********* Result *************
Child class m1() method
Parent P1 class m2() method
--------------------------------------------------------------------------------------------------
class P1: # Parent P1 class
    def m1(self):
        print('Parent P1 class m1() method ')
        
    def m2(self):
        print('Parent P1 class m2() method')
        
class P2: # Parent P2 class
    def m1(self):
        print('Parent P2 class m1() method')
        
    def m2(self):
        print('Parent P2 class m2() method')    
        
class C(P2,P1): # Child class cretaed with help of multiple parent classes.
    def m1(self):
        print('Child class m1() method')
        
        
c = C() # Object creation for Child class.
c.m1() # Child class m1() method
c.m2() # Parent P2 class m2() method

********* Result *************
Child class m1() method
Parent P2 class m2() method
---------------------------------------------------------------------------------------------
Ex :- 
class P1: # Parent p1 class & It doesn't contain any m1() method.
    pass
class P2: # Parent p2 class & It doesn't contain any m1() method.
    pass
class C(P1,P2): # Child class & It doesn't contain any m1() method.
    pass

c = C() # Object creation for Child class.
c.m1() # AttributeError: 'C' object has no attribute 'm1'.

NOTE :- As we can say that there should be atleast one m1() method. So easily we can call it.
-----------------------------------------------------------------------------------------------
5) Hybrid Inheritance :- The combination is one or more is called as Hybrid Inheritance.
   ------------------ 

6) Cyclic Inheritance :- It occurs when if class A required itself property then is called as Cyclic Inheritance.
   ------------------- 
   
   class A(A) : --- > parent class is A & it is accessing it's property itself but NO issue for it.
   We should not use the Cyclic Inheritance in python.
   
   class A(B):
       
   class B(A):
      
NOTE :- In python we can use the Cyclic Inheritance but it is not required at all.

class A:
    def m1(self):
        print('Parent A class method')
        
class A(A):
    def m2(self):
        print('Child A class method')
        
a = A()
a.m1()
a.m2()

********* Result *************
Parent A class method
Child A class method
-------------------------------------------------------------------------------------------------

class A(A):
    def m1(self):
        print('Cyclic Inheritance in Python')
        
a = A()
a.m1()        
        
        
    
         
        




























        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















































        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




















    



        
    









    
    















    
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
               
               
               
               


        
        
        
        
        
        
        
        
        


        
        
        










        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           





























 





























































