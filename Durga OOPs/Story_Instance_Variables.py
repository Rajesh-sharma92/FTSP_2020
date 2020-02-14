# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:15:01 2020

@author: Rajesh
"""
Instance Variables :
------------------
1) If the value of variables are  varied from one object to object such types of variables 
 are called as Instance variables. for every object a seprate copy will be created.:
Ex :-
class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
            
s1 = student('Durga',101)
s2 = student('Rajesh',102)
s3 = student('Sunny',103)

################################################################################
2) Where we have to declared instance variables :- 
----------------------------------------------
i) Inside constructor by using self variable and we can declared by self.variable name.
Ex :-
class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
NOTE :- self.name & self.rollno are Instance variables in inside the class.
NOTE :-   name & rollno are just local variables. We can use any name for local variables.

ii) Inside instance method by using self variable.
Ex :- class student:
        def __init__(self,name,rollno):
            self.name=name
            self.rollno=rollno
            
        def info(self):
            self.marks=60 # Instance variable
            x = 10 # local variable coz it's not statring with self variable.
            
s1 = student('Durga',1001)
# s2 = student('RAJESH',501)
s1.info()
print(s1.__dict__)
# print(s2.__dict__)  

iii) From outside of the class by using object reference.
Ex :- class student:
        def __init__(self,name,rollno):
            self.name=name
            self.rollno=rollno
            
        def info(self):
            self.marks=60 # Instance variable
            x = 10 # local variable coz it's not statring with self variable.
            
s1 = student('Durga',1001)
# s2 = student('RAJESH',501)
s1.info()
s1.age = 25  # Declaring instance variables outside of the class by using object reference.
s1.gender = 'Male'
print(s1.__dict__)
# print(s2.__dict__)  
    
s2 = student('Rajesh',100)
s2.wife = 'Renu'
print(s2.__dict__)   
###########################################################################

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        
    def m1(self):
        self.d = 40
        
    def m2(self):
        self.e = 50
   
t1 = Test() # Object for class
t1.m1()
print(t1.__dict__)

t2 = Test() # Object for class
t2.m2()
t2.s=300
t2.y=500
print(t2.__dict__) # the output will be in the dictionary form.

************* Result *****************
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30, 'e': 50, 's': 300, 'y': 500}

-----------------------------------------------------------------------------
== >> How to access instance variables :- 
-----------------------------------------
1) within the class by using by self variable.
Ex :-  class student:
          def __init__(self,name,rollno):
              self.name = name
              self.rollno = rollno
              
          def display(self):
              print('Hello My name is :',self.name)
              print('My RollNo is :',self.rollno)
              
s = student('Durga',1001)
s.display()

******* Result ************
Hello My name is : Durga
My RollNo is : 1001
-----------------------------------------------------------------------------
2) Outside the class by using reference variable.
Ex :-  class student:
          def __init__(self,name,rollno):
              self.name = name
              self.rollno = rollno
              
          def display(self):
              print('Hello My name is :',self.name)
              print('My RollNo is :',self.rollno)
              
s = student('Durga',1001)
s.display()

print('Hello My name is :', s.name) # Object reference variable.
print('My RollNo is :', s.rollno)    

******* Result ************
Hello My name is : Durga
My RollNo is : 1001

##############################################################################

--->>> How to delete the instances variables :- 
--------------------------------------------
1) within the class delete the instance variables.
   syntax :-  del self.variablename
   
   Ex :- class Test:
        def __init__(self):
            self.a = 10
            self.b = 20
            self.c = 30
            
        def delete(self):
            del self.b 
            del self.c
            # del self.b , self.c

t1 = Test() 
t1.delete()    
print(t1.__dict__)   
-----------------------------------------------------------------------------
2) Outside of the class delete the instance variables.
  syntax :-  del objectReference.variablename

 Ex :- class Test:
        def __init__(self):
            self.a = 10
            self.b = 20
            self.c = 30
            
        def delete(self):
            del self.b 
            del self.c
            

t1 = Test() 
del t1.b
del t1.c
print(t1.__dict__)   
----------------------------------------------------------------------------
NOTE :- If we try to delete the self variable self variable will be deleted and there 
constructor will be executed once object created.

Ex :- class Test:
        def __init__(self):
            print('This is forsk coding school')
            self.a = 10
            self.b = 20
            self.c = 30
            
        def delete(self):
            del self  # It will be deleting only self variable.
            
t1 = Test() 
t1.delete() # It will be deleting only self variable.
print(t1.__dict__)   

*********** Result*********************
{'a': 10, 'b': 20, 'c': 30}
-----------------------------------------------------------------------------
Ex :-  class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        
t1 = Test()
t2 = Test()
del t1.b # b will be deleted and a & c will be in result.
del t2.a # a will be deleted and b & c will be in result.
print(t1.__dict__)
print(t2.__dict__)
-----------------------------------------------------------------------------
Ex :- class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        
t1 = Test()
t2 = Test()
t1.a = 888
t1.b = 999
print(t1.__dict__) # {'a': 888, 'b': 999}
print(t2.__dict__) # {'a': 10, 'b': 20}
--------------------------------------------------------------------------
Ex :- class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        
t1 = Test()
t2 = Test()
t1.a = 888
t2.b = 999
print(t1.__dict__) # {'a': 888, 'b': 20}
print(t2.__dict__) # {'a': 10, 'b': 999}

















        
        
        
        
        


        
        
        
        
        
        

 


      
              
              
              
              
            

    





           
            
            
            
            
            
            
            
            
            
            
            
            
    
    

    
    
    


   
    
    
    