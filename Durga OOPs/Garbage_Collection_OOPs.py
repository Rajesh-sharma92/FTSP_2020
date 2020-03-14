# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:37:35 2020

@author: Rajesh
"""

Garbage Collection :- 
-------------------
Based on our requirement we can enable and disable GC.

NOTE :- To destroyed the useless objects python has provide the Assistent is 
called Garbage Collector.

NOTE :- Garbage Collector will always running background at PVM.

NOTE :- We have module in Python for Garbage collection operations.

Module Name is gc module

gc.isenabled()
gc.enable()
gc.disable()
---------------------------------------------------------------------------------------------
Ex :- 

import gc
print(gc.isenabled()) # True
gc.disable()
print(gc.isenabled()) # False
gc.enable()

************* Result **********
True
False
------------------------------------------
import gc
print(gc.isenabled()) # True
gc.disable()
print(gc.isenabled()) # False
gc.enable()
print(gc.isenabled()) # True

************* Result **********
True
False
True
-----------------------------------------------------------------------
NOTE :- By default Garbage Collector will be enabled only in any Python program.

NOTE :- We have Constructor & Destructor in Python.

def __init__(self): # Constructor
    pass

def __del__(self): # Destructor
    pass
close db connection
close Network connection
----------------------------------------------------------------------------------
Question :- Who is calling destructor ?
Answer :- Garbage Collector automatically calls the destructor. GC always calls
the Destructor just destroying the objects.
Garbage collector just calls the destructor to perform the CleanUp activities.
CleanUp activities means any kind of resources De-allocated, to released those 
resources GC always calls the Destructors.
---------------------------------------------------------------------------------------------------------------
Question :- Is it GC are Daemon Threads ?
Answer :- Yes, GC is the Daemon thread because GC always works in background and 
Daemon threads means who works on background only.
-----------------------------------------------------------------------------------
Question :- If we don't write any destructor then what will happens ?
Answer :- Nothing will be happens and object class destructor will be executing 
automatically.
-----------------------------------------------------------------------------------------
NOTE :- destructor always calls by GC and GC invoked by PVM in Python program.
----------------------------------------------------------------------------------------------
Ex :- Here t1 is pointing to Test Object and it is useful.

import time
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
        
    def __del__(self): # Destructor
        print('Fulfilling last wish and performing cleanUp Activities....')
        
t1 = Test() # Object creation for Test Class.
time.sleep(10)
print('End of Application')

************ Result ***************
Object Initalization.....
End of Application

-----------------------------------------------------------------------------------------
Ex :- Here t1 is not pointing to any Object(None) and it is Useless. Here GC 
calls the destructor and will destroyed the useless object.

import time
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
        
    def __del__(self): # Destructor
        print('Fulfilling last wish and performing cleanUp Activities....')
        
t1 = Test() # Object creation for Test Class.
t1 = None # Here t1 is not pointing any Object means we need to delete it.
time.sleep(10)
print('End of Application')

************ Result ***************
Object Initalization.....
Fulfilling last wish and performing cleanUp Activities....
End of Application

--------------------------------------------------------------------------------------------------------------
Ex :- 

import time
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
        
    def __del__(self): # Destructor
        print('Fulfilling last wish and performing cleanUp Activities....')
        
t1 = Test() # Object creation for Test Class.
time.sleep(5)
print('End of Application')

NOTE :- In the above example we can see that while executing the program GC 
will not call the destructor to destroyed the object which is created but once 
the line no.131 will be executing before that GC will be knowing that now the 
program will be terminats. So, Automatically GC will be calling the destructor 
and destroyed the used object in the program.

NOTE :- In the program all created objects will be destroyed once the program 
will be terminated.

********* Result ************
Object Initalization.....
End of Application
Fulfilling last wish and performing cleanUp Activities....

----------------------------------------------------------------------------------------------
NOTE :- Here we can see that If we are calling GC or not does  not matter because 
at the time of list line execution in the program all created objects will be deleted
by GC calls the destructor and it will be deleting all those created objects.
--------------------------------------------------------------------------------------------------------
Ex :- 
import time
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
    
    def __del__(self): # Destructor
        print('Fulfilling last wish and performing cleanUp Activities....')


t1 = Test() # Object creation for Test Class.
time.sleep(10)
t1 = None # Here t1 is not pointing any Object means we need to delete it.
print(t1) # None coz t1 is not pointing any objetc.

************** Result **************
Object Initalization.....
Fulfilling last wish and performing cleanUp Activities....
None
-------------------------------------------------------------------------------------------
Ex :- 
import time
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
    
    def __del__(self): # Destructor
        print('Fulfilling last wish and performing cleanUp Activities....')


t1 = Test() # Object creation for Test Class.
time.sleep(10)
del t1 # Here t1 deleted means No scope of t1.
print(t1) # NameError: name 't1' is not defined.

************** Result **************
Object Initalization.....
Fulfilling last wish and performing cleanUp Activities....
NameError: name 't1' is not defined
----------------------------------------------------------------------------------------------
Ex :- To making GC disabled but then also destructor will be exeuting means 
Destroying object.

import gc # Importing Garbage collector
import time
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
        
    def __del__(self): # Destructor
        print('Fulfilling last wish and performing cleanUp Activities....')
        
gc.disable() # To making GC disabled but then also destructor will be exeuting means Destroying object.
print(gc.isenabled()) # GC enabled then also it is destroying an object.
t1 = Test() # Object creation for Test Class.
t1 = None # Here t1 is not pointing any Object means we need to delete it.
time.sleep(10)
print('End of Application')

************ Result ***************
False
Object Initalization.....
Fulfilling last wish and performing cleanUp Activities....
End of Application
-------------------------------------------------------------------------------------------
Ex :- 

import gc # Importing Garbage collector
import time
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
        
    def __del__(self): # Destructor
        print('Fulfilling last wish and performing cleanUp Activities....')
        
gc.disable() # To making GC disabled but then also destructor will be exeuting means Destroying object.
print(gc.isenabled()) # GC enabled then also it is destroying an object.
t1 = Test() # Object creation for Test Class.
time.sleep(10)
print('End of Application')

************ Result ***************
False
Object Initalization.....
End of Application
Fulfilling last wish and performing cleanUp Activities....
----------------------------------------------------------------------------------------
NOTE :- for Destructors Important points.
1) The purpose of destructor is to destroyed the useless objects.
2) The purpose of destructor is to perform Cleanup activities before destroying an objects.
-----------------------------------------------------------------------------------------------------------
Question :- If there are multiple reference variables are pointing to same object
then when will be that object will be applicable for GC ?
Answer :- If we are such situtation then first we need to make all reference variables 
to None and all those reference variables are should not be pointing to any object
then that object will be applicable for GC.

Ex :- 

import time
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
        
    def __del__(self): # Destructor
        print('Fulfilling last wish and performing cleanUp Activities....')
        
t1 = Test()
t2 = t1
t3 = t2
t4 = t3
del t1
time.sleep(10)
print('After deleted t1 object has not destroyed')
del t2
del t3
time.sleep(10)
print('still Object not eligible for GC')
time.sleep(10)
del t4
time.sleep(10)
print('End of Application')

************ Result ***********
Object Initalization.....
After deleted t1 object has not destroyed
still Object not eligible for GC
Fulfilling last wish and performing cleanUp Activities....
End of Application
-----------------------------------------------------------------------------------------
Question :- If we have list of multiple objects then how many times the destructor 
will be executed in the program ?
Answer :- Here first all objects will be executed by constructor and later all 
object will be deleted by destructor and we can see that for every object destructor 
will be exceuted sepearately.

Ex :- 

import time
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
        
    def __del__(self): # Destructor
        print('Fulfilling last wish and performing cleanUp Activities....')
        
list1 = [Test() , Test() , Test()] # For every object constructor will executed seperately.
time.sleep(10)        
list1 = None # It will be eligible for GC but one by one Object.
time.sleep(10)
print('End of Application')

*********** Result ***************
Object Initalization.....
Object Initalization.....
Object Initalization.....
Fulfilling last wish and performing cleanUp Activities....
Fulfilling last wish and performing cleanUp Activities....
Fulfilling last wish and performing cleanUp Activities....
End of Application
-------------------------------------------------------------------------------------------------
Question :- How to check like how many reference variables are there for same object ?
Answer :- first we need to import the sys module and later we need to go for
sys.getrefcount(t1).

Ex :- 

import time
import sys
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
        
t1 = Test()
t2 = t1
t3 = t2
t4 = t3
print('Total Reference Variables :', sys.getrefcount(t1))        

********** Result *******
Object Initalization.....
Total Reference Variables : 5

NOTE :- In above example we can see that there are 5 Reference Variables and 
4 are like t1,t2,t3,t4 and last one is the self which is internally pointing to object.
----------------------------------------------------------------------------------------------------
Ex :- 

import time
import sys
class Test:
    def __init__(self): # Constructor
        print('Object Initalization.....')
        
t1 = Test()
# t2 = t1
print('Total Reference Variables :', sys.getrefcount(t1))  
 
********** Result *******
 Object Initalization.....
Total Reference Variables : 3
    
Object Initalization.....
Total Reference Variables : 2
--------------------------------------------------------------------------------------------------

        
        
    
    































