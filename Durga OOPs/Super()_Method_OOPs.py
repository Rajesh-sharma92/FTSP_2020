# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:14:09 2020

@author: Rajesh
"""

Super() Method :- It is nothing but parent class methods are called super methods because Parent means super only.
-------------
Question :- Why do we need of super() method ?
Answer :- It is very useful in the python OOPs concepts in Inheritance.
It is used in child class like form child class to call parent call members.
Code Re-useability.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # 100 properties.
        
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        self.name = name
        self.age = age
        # 100 properties.
        self.rollno = rollno
        self.marks = marks
        
    
class Teacher(Person):
    def __init__(self,name,age,salary,subject):
        self.name = name
        self.age = age
        # 100 properties.
        self.salary = salary
        self.subject = subject
        
s = Student('Rajesh',25,1001,75)
t = Teacher('Durga',45,10000,'Python')

************ Result ************
Here we will not be getting any kind of output coz all the codes are correct but duplicates things are so many.
So, we need to use the super() method.
------------------------------------------------------------------------------------------------------------------
class Person:
    def __init__(self,name,age): # Parent Constructor
        self.name = name
        self.age = age
        # 100 properties.
        
class Student(Person):
    def __init__(self,name,age,rollno,marks): # child constructor
        
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks
    def display(self):
        print('Name :', self.name)
        print('Age :', self.age)
        print('Roll No.', self.rollno)
        print('Marks :', self.marks)
    
class Teacher(Person):
    def __init__(self,name,age,salary,subject): # child constructor
        
        super().__init__(name,age)
        self.salary = salary
        self.subject = subject
    def display(self):
        print('Name :', self.name)
        print('Age :', self.age)
        print('Salary :', self.salary)
        print('Subject :', self.subject)    
        
s = Student('Rajesh',25,1001,75)
t = Teacher('Durga',45,10000,'Python')

s.display()
print('*'*20)
t.display()

NOTE :- Only one time we have written in the parent constructor and we can call any time in the 
child constructors. Here we can see that code re-useability is there.
Code efficieny will be increased automatically.

Question :- The above parent constructor will be executed for child purpose or not ?
Answer :- Yes, offcourse parent constructor will be executed for child class object like
Student & Teacher and i have not created any object for parent class.

NOTE :- Here we are just creating objects for child classes like Student & Teacher and automatically
parent Constrctor will be executed for both the classes. but Parent class object will not be created 
Automatically after creating object for child classes.

NOTE :- In this above scenario we can say that the super() method is used for Code Re-usability 
& calling the parent constructor by using the help of child class object creation.

NOTE :- Internally, Super() method will be works on MRO Algorithm only.

------------------------------------------------------------------------------------------------------------------
NOTE :- We can see that in the above example Code Re-usability is there for name and age 
but there is NO code Re-usability for display() method. We can do some modification in the above codes.

class Person:
    def __init__(self,name,age): # Parent Constructor
        self.name = name
        self.age = age
        # 100 properties.
    def display(self):
        print('Name :', self.name)
        print('Age :', self.age)
        
class Student(Person):
    def __init__(self,name,age,rollno,marks): # child constructor
        
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks
    def display(self):    
        super().display()
        print('Roll No.', self.rollno)
        print('Marks :', self.marks)
    
class Teacher(Person):
    def __init__(self,name,age,salary,subject): # child constructor
        
        super().__init__(name,age)
        self.salary = salary
        self.subject = subject
    def display(self):
        super().display()
        print('Salary :', self.salary)
        print('Subject :', self.subject)    
        
s = Student('Rajesh',25,1001,75)
t = Teacher('Durga',45,10000,'Python')

s.display()
print('*'*20)
t.display()

NOTE :- The biggest use of super() method is to call the parent class constructor and parent class display()
method for every child classes. We just need to define common methods and constructor in parent class always 
and easy to access for every child classes and It helps in code Re-usability.
----------------------------------------------------------------------------------------------------------------
Ex :- 

                                A 
                                |
                                B
                                |
                                C
                                |
                                D
                                |
                                E  ---> super().m1()
                                
NOTE :- If E class contains super() method and we just want to call the m1() method in the E class
then the Immediate parent class for E is the class D is parent class. it goes to D class and check it 
and If not then D class then it will be going to another classes like C and etc.
----------------------------------------------------------------------------------------------------------------
                                A --> m1()
                                |
                                B --> m1()
                                |
                                C --> m1()
                                |
                                D --> m1()
                                |
                                E  ---> super().m1()
                                
NOTE :- If every class contains the m1() method but it always works MRO Algorithm only.                                
NOTE :- If E class contains super() method and we just want to call the m1() method in the E class
then the Immediate parent class for E is the class D is parent class. it goes to D class and check it 
and If not then D class then it will be going to another classes like C and etc.

Ex :- 

class A:
    def m1(self):
        print('A class m1() method')
class B(A):
    def m1(self):
        print('B class m1() method')
class C(B):
    def m1(self):
        print('C class m1() method')
class D(C):
    def m1(self):
        print('D class m1() method')
class E(D):
    def m1(self):
        print('E class m1() method')

e = E() # Obcject Creation for E class.
e.m1() # calling the m1() of E class. # E class m1() method.

*********** Result **********
E class m1() method
---------------------------------------------------------------------------------------------------------
Ex :- 
class A:
    def m1(self):
        print('A class m1() method')
class B(A):
    def m1(self):
        print('B class m1() method')
class C(B):
    def m1(self):
        print('C class m1() method')
class D(C):
    def m1(self):
        print('D class m1() method')
class E(D):
    def m1(self):
        super().m1()

e = E() # Obcject Creation for E class.
e.m1() # D class m1() method

*********** Result **********
D class m1() method
-----------------------------------------------------------------------------------------------
Ex :- 
class A:
    def m1(self):
        print('A class m1() method')
class B(A):
    def m1(self):
        print('B class m1() method')
class C(B):
    def m1(self):
        print('C class m1() method')
class D(C):pass
    
class E(D):
    def m1(self):
        super().m1()

e = E() # Obcject Creation for E class.
e.m1() # C class m1() method

*********** Result **********
C class m1() method
-----------------------------------------------------------------------------------------------------
How to call a particular parent class method by using super() method :-
--------------------------------------------------------------------
Ex :- Here we want to call in E class and m1() method of B class. 
NOTE :- They are 2 ways to call the from parent class to in like child class B and etc.

1) parentclassname.methodname(self)
    ex :- B.m1(self)
    
    For Constructor also it will work
    Ex :- parentclassname.Constructor(self,parameters names)
          B.__init__(self,name,age)
          
          
2) super(D,self).m1()
          
          
class A:
    def m1(self):
        print('A class m1() method')
class B(A):
    def m1(self):
        print('B class m1() method')
class C(B):
    def m1(self):
        print('C class m1() method')
class D(C):
    def m1(self):
        print('D class m1() method')
class E(D):
    def m1(self):
        B.m1(self)
        A.m1(self)
    
e = E() # Obcject Creation for E class.
e.m1() 

*********** Result **********

B class m1() method
A class m1() method
-------------------------------------------------------------------------------------------
2) super(D,self).m1()
          
          
class A:
    def m1(self):
        print('A class m1() method')
class B(A):
    def m1(self):
        print('B class m1() method')
class C(B):
    def m1(self):
        print('C class m1() method')
class D(C):
    def m1(self):
        print('D class m1() method')
class E(D):
    def m1(self):
        super(D,self).m1() # super of D class is the class C and It gives m1() method class C.
        # super(C,self).m1()
        # super(A,self).m1() # AttributeError: 'super' object has no attribute 'm1'
        
e = E() # Obcject Creation for E class.
e.m1() # C class m1() method

***************** Result ***********
C class m1() method
NOTE :- super(D,self).m1() here only most of the people gets confused and they will be telling the 
wrong answer like D class m1() method will be executed but here super of D class m1() method will 
be executed and super of D class means C class and then finally the result will be the # C class m1() method
will be executed only.

NOTE :- If we will taking super(C,self).m1() then which class m1() method will be executed 
super class C means Class B and then B class m1() method will be executed successfully.

NOTE :- If we will be calling super(A,self).m1() then we will be getting any error coz there is NO 
super class of A class. Then will throw an error like " AttributeError: 'super' object has no attribute 'm1' ".

---------------------------------------------------------------------------------------------------------------------------------
class P:
    a = 10 # static variable
    def __init__(self):
        self.b = 20 # Instance variable
        
class C(P):
    def m1(self):
        print(super().a) # It will be working 
        # print(super().b) # error coz we can not use super in the child class and called the parent class Instance variasles.
        
c = C()
c.m1() # 10     

MOTE :- print(super().b) # error coz we can not use super method in the child class and called the parent class Instance variasles.        
NOTE :- We can not use super() method in the child class C and can not called the Instance variables of Parent class.
--------------------------------------------------------------------------------------------------------------
Important Points are :-
--------------------
1) From child class by using super() method we can not call parent class Instance variables.
And we should use self keyword only.

2) From child class by using super() method we can parent ia static variables.

class P:
    a = 10 # static variable
    def __init__(self):
        self.b = 20 # Instance variable
        
class C(P):
    def m1(self):
        print(super().a) # It will be working 
        print(self.b) # It will be working also
        
c = C()
c.m1() # 10  

**************** Result ****************
10
20
---------------------------------------------------------------------------------------------------------------
class P:
    def __init__(self):
        print('Parent class Constructor')
        
    def m1(self):
        print('Parent class Instance m1() method')
    @classmethod
    def m2(cls):
        print('Parent class class m2() method')
    @staticmethod
    def m3():
        print('Parent class static m3() method')
        
class C(P):
    def __init__(self): # child class Constructor
        print('Child class Constructor')
        
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
      
c = C() # Object creation for child class C.

************* Result *************

Child class Constructor
Parent class Constructor
Parent class Instance m1() method
Parent class class m2() method
Parent class static m3() method

NOTE :- Here when we create the object for child class C then automatically the child constructor 
and its correspodance methods will be executed itself.
-----------------------------------------------------------------------------------------------------------
class P:
    def __init__(self):
        print('Parent class Constructor')
        
    def m1(self):
        print('Parent class Instance m1() method')
    @classmethod
    def m2(cls):
        print('Parent class class m2() method')
    @staticmethod
    def m3():
        print('Parent class static m3() method')
        
class C(P):
    def method1(self): # child class Instance method.
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
  
c = C() # Object creation for child class C.
c.method1()
-------------------------------------------------------------------------------------------------
class P:
    def __init__(self):
        print('Parent class Constructor')
        
    def m1(self):
        print('Parent class Instance m1() method')
    @classmethod
    def m2(cls):
        print('Parent class class m2() method')
    @staticmethod
    def m3():
        print('Parent class static m3() method')
        
class C(P):
    @classmethod
    def method1(cls): # child class Instance method.
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
  
c = C() # Object creation for child class C.
c.method1()
-------------------------------------------------------------------------------------------------------
class P:
    def __init__(self):
        print('Parent class Constructor')
        
    def m1(self):
        print('Parent class Instance m1() method')
    @classmethod
    def m2(cls):
        print('Parent class class m2() method')
    @staticmethod
    def m3():
        print('Parent class static m3() method')
        
class C(P):
    @staticmethod
    def method1(): # child class Instance method.
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
  
#c = C() # Object creation for child class C.
#c.method1()
C.method1()

------------------------------------------------------------------------------------------------------------





















      
        
        
        
        























    





















        
























































































                                
                                
                                






























        
        
        
        
        
        
        
        
        
        
        
        


        