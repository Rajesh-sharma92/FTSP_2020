# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:05:29 2020

@author: Rajesh
"""
Local Variables :- 
--------------
Local variables are method level variables.

We should not use self , cls , classname.

class Test:
    def m1(self):
        a = 100 # Local variable
        print(a)
        
    def m2(self):
        b = 200 # Local variable
        print(b)
        
      #  print(a)  --->> NameError: name 'a' is not defined. Coz a can be used for only m1().
        
t = Test()
t.m1() # 100
t.m2() # 200
-----------------------------------------------------------------------------
class Test:
    def m1(self):
        a = 100 # Local variable
        print(a)
        
    def m2(self):
        a = 900 # Local variable
        b = 200 # Local variable
        print(a)
        print(b)
        
t = Test()
t.m1() # 100 
t.m2() # 900 , 200
-----------------------------------------------------------------------------
class Test:
    def average(self,list):
        result = sum(list)/len(list) # result is the local variable to store the temp o/p.
        print('The Average value :', int(result))
        
t = Test()
t.average([10,20,30,40])
------------------------------------------------------------------------------
class Test:
    def average(self,tuple):
        result = sum(tuple)/len(tuple) # result is the local variable to store the temp o/p.
        print('The Average value :', int(result))
        
t = Test()
t.average((10,20,30,60))
------------------------------------------------------------------------------
NOTE :- Sometimes, we need to store the output of the some of functions in the 
program in some variable is called Local variables like A,B,result and etc.
----------------------------------------------------------------------------
--->> We can access any global variables into any method in the class.
---------------------------------------------------------------------
x = 100 # global variable
class Test:
    def m1(self):
        y = 20 # Local variable
        print('Local variable :', y)
        print('Global variable :', x) 
        
        
t = Test()
t.m1()        
------------------------------------------------------------------------------
NOTE :- Global variables can be access for N no. of methods and it will be 
available for every method.
-------------------------------
x = 100 # global variable
class Test:
    def m1(self):
        y = 20 # Local variable
        print('Local variable :', y)
        print('Global variable for m1() :', x) 
        
    def m2(self):
        print('Global variable for m2() :', x) 
            
t = Test()
t.m1()     
t.m2()
-----------------------------------------------------------------------------
NOTE :- Static variables can be accessed by using the self or classname.
x = 100  # global variable
class Test:
    x = 777 # static variable
    def m1(self):
        print(x) # 100
        print(self.x) # 777
        print(Test.x) # 777
        
    def m2(self):
        print(x) # 100
        print(self.x) # 777
        print(Test.x) # 777
        
t = Test()
t.m1()
t.m2()
-----------------------------------------------------------------------------
NOTE :- If global & local variables are available in program and then PVM will
be giving first preference to local variables other than global & static variables.
NOTE :- First local variables --> Static variables --> Global variables scope.

x = 100  # global variable
class Test:
    x = 777 # static variable
    def m1(self):
        x = 888  # Local variable
        print(x) # 888
        print(self.x) # 777
        
    def m2(self):
        x = 555  # Local variable
        print(x) # 555
        print(Test.x) # 777
        
t = Test()
t.m1() # 888 , # 777
t.m2() # 555 , # 777
-----------------------------------------------------------------------------
NOTE :- We can access  local variable for one method but into another method we can't access.
To Access into another we must use the global keyword into first method.
class Test:
    def m1(self):
        x = 999
        print(x)
        
    def m2(self):
        print(x)
        
t = Test()
t.m1() # 999  

t.m2() # NameError: name 'x' is not defined.
------------------------------------------------------------------------------
NOTE :- We can use global keyword into first method for accessing the local variables
and make them as global and accessing into another method also.
NOTE :- If we have declared variable as global then we can access anywhere in the class
and outside the variable there is No issue at all.

class Test:
    def m1(self):
        global x # global keyword.
        x = 999
        print(x) # 999  
        
    def m2(self):
        print(x) # 999  
        
t = Test()
t.m1() # 999  
t.m2() # 999
print(x) # Outside of the class and x = 999
-----------------------------------------------------------------------------
NOTE :- From the class we can access global variables directly.

x = 100 # Global variable and accessing anywhere in the class and outside of the class also.
class Test:
    def m1(self):
        print(x) # 100
        
    def m2(self):
        print(x) # 100
        
t = Test()
t.m1() # 100
t.m2() # 100
print(x) # 100 --> Outside of the class.
-----------------------------------------------------------------------------
NOTE :- Within the method of a class we can declare global variables by using
global keyword.

class Test:
    def m1(self):
        global x # Global keyword
        x = 1001 
        print(x) # 1001
        
    def m2(self):
        print(x) # 1001
 
t = Test()       
t.m1() # 1001
t.m2() # 1001
print(x)  # 1001 --> outside of the class.
------------------------------------------------------------------------------
NOTE :- Global keyword can declare within the class anywhere and we can anywhere in
the class as well as outside the class.

class Test:
    
    global x # Global keyword
    x = 777
    
    def m1(self):
        print(x) # 777
        
    def m2(self):
        print(x) # 777
        
t = Test()        
t.m1() # 777
t.m2() # 777
print(x) # 777 --> outside of the class.
------------------------------------------------------------------------------






























































































    









































