# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:57:41 2020

@author: Rajesh
"""

Method Overloading :- 
------------------
class Test:
    
    def m1(self):
        print('No-arg method')
        
    def m1(self,x):
        print('One-arg method')
        
t = Test()

t.m1() # TypeError: m1() missing 1 required positional argument: 'x'
t.m1(10) # One-arg method      
-------------------------------------------------------------------------------------------
class Test:
    
    def m1(self):
        print('No-arg method')
        
    def m1(self,x):
        print('One-arg method')
        
    def m1(self,x,y):
        print('Two-arg method')
        
t = Test()

t.m1() # TypeError: m1() missing 2 required positional arguments: 'x' and 'y'

t.m1(10) # m1() missing 1 required positional argument: 'y'

t.m1(20,30) # Two-arg method
----------------------------------------------------------------------------------------------------------------
NOTE :- In python, Method Overloading concept is not available and whenever we need to perform method overloading 
then always the last one method will be executed. Python does not support method overloading.

Method Overloading definition :- 
-----------------------------
Whenever the method name is same but different arguments type , number of arguments then it is called 
as Method Overloading.

NOTE :- Python does not provide support for Method Overloading & Constructor Overloading.

NOTE :- In Python we can not provide the explicitly arguments type and then how will be using the
method overloading concept. Implicitly data types will be there.
-----------------------------------------------------------------------------------------------------
class Test:
    
    def m1(self,i):
        print(i)
        
t = Test()

t.m1(10)        # 10
t.m1('Forsk')   # Forsk     
t.m1(20.5)      # 20.5
t.m1(10+20j)    # (10+20j)

NOTE :- By seeing this above example we can say that method Overloading concept is not required in python
coz by using single method we can all these different operations.
-----------------------------------------------------------------------------------------------------------
 NOTE :- In Python , these two concepts are very powerful as listed below.
1) Default Arguments
2) Variable length Arguments
-------------------------------
Default Arguments :-
-----------------

class Test:
    
    def sum(self,a=None,b=None,c=None):
    
        if a != None and b != None and c != None:
            print('The sum of 3 numbers are :', a+b+c)
        elif a != None and b != None:
            print('The sum of 2 numbers are :', a+b)
        else:
            print('Plz enter 2 or 3 numbers')
             
t = Test()

t.sum(10,20,30) # The sum of 3 numbers are : 60
t.sum(10,20) #   The sum of 2 numbers are : 30
t.sum(10) # Plz enter 2 or 3 numbers
-----------------------------------------------------------------------------------------------
Variable length Arguments :-
-------------------------
class Test:
    
    def sum(self,*a):
        total = 0
        for x in a:
            total = total+x
        print('The sum :', total)

t = Test()

t.sum(10,20) # 30
t.sum(10,20,30,40) # 100
t.sum(10,20,30,40,50,60) # 210
t.sum() # 0
t.sum(10) # 10
----------------------------------------------------------------------------------------------------
class Test: 
    
    def m1(self,*a):
        total = ' '
        for x in a:
            total = total + x
        print('The Result :', total)
        
t = Test()

t.m1('Forsk') # Forsk
t.m1('Forsk','Coding') # ForskCoding
t.m1('Forsk','Coding','school') # ForskCodingschool
t.m1() # Empty string
--------------------------------------------------------------------------------------------------------
Constructor Overloading :-
-----------------------
class Test:
    
    def __init__(self):
        print('No-arg Constructor')

    def __init__(self,a):
        print('One-arg Constructor')
        
    def __init__(self,a,b):
        print('Two-arg Constructor')
        
t = Test() # TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'.
t = Test(10) # TypeError: __init__() missing 1 required positional argument: 'b'
t = Test(10,20) # Two-arg Constructor.

NOTE :- Python does not support Constructor overloading concept and it will be always 
executing the last one Constructor method. We can see that in the above example first & second
constructor methods will be ignored and last one will be executed successfully.

---------------------------------------------------------------------------------------------------------------

class Test:
    
    def __init__(self, a = None , b = None , c = None):
        print('Constructor with 0|1|2|3')
        
t = Test() # Constructor with 0|1|2|3
t = Test(10) # Constructor with 0|1|2|3 
t = Test(10,20) # Constructor with 0|1|2|3
t = Test(10,20,30) # Constructor with 0|1|2|3   

*************** Result ************
Constructor with 0|1|2|3
Constructor with 0|1|2|3
Constructor with 0|1|2|3
Constructor with 0|1|2|3
----------------------------------------------------------------------------------------------------------
class Test:
    
    def __init__(self,*a):
        print('Any no. of args-Constructors')
        
t = Test(10)
t = Test(10,20)
t = Test(10,20,30)
t = Test(10,20,30,40)
t = Test(10,20,30,40,50)
t = Test()  
      
*************** Result ************
Any no. of args-Constructors
Any no. of args-Constructors
Any no. of args-Constructors
Any no. of args-Constructors
Any no. of args-Constructors
Any no. of args-Constructors

---------------------------------------------------------------------------------------------------------
NOTE :- Python does not support Operator overloading , Method overloading and Constructor overloading.
NOTE :- We have internally in-built concept that supports to all these  things like Operator overloading , 
Method overloading and Constructor overloading.
NOTE :- That's why python does not support all these things as explicitly.
--------------------------------------------------------------------------------------------------------------































        










































        











            
            
            
            
















































          
 
            


































        


























