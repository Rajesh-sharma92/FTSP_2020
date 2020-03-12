# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:25:53 2020

@author: Rajesh
"""
Multithreading Introduction :- 
---------------------------

3) Creating a thread without extending Thread class :- 
---------------------------------------------------

from threading import *
class Test:
    def m1(self):
        for i in range(10):
            print('Child-Thread1')
obj = Test() # object creation for Test class.
t = Thread(target=obj.m1) # Object creation for Thread class.
t.start() # It will start the Child class Thread.
for i in range(10):
    print('Main Thread') 
    
-----------------------------------------------------------------------------------------------------------
Ex :- 

import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('Double Value :', 2*n)
        
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('Square Value :', n*n)
        
numbers = [1,2,3,4,5,6]
begintime = time.time()
doubles(numbers)
print('*'*30)
squares(numbers)
endtime = time.time()
print('--'*30)
print('The Total Time Taken :', endtime - begintime)

***************** Result ******************
Double Value : 2
Double Value : 4
Double Value : 6
Double Value : 8
Double Value : 10
Double Value : 12
******************************
Square Value : 1
Square Value : 4
Square Value : 9
Square Value : 16
Square Value : 25
Square Value : 36
------------------------------------------------------------
The Total Time Taken : 12.0116868019104 

NOTE :- In the above example we can see that there is only one Thread thats MainThread.
--------------------------------------------------------------------------------------------------------------------------------------------
How to use multi threading concept in that above programs :- 
---------------------------------------------------------

import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('Double Value :', 2*n)
        
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('Square Value :', n*n)
        
numbers = [1,2,3,4,5,6]
begintime = time.time()
t1 = Thread(target=doubles,args=(numbers,))
t2 = Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime = time.time()
print('--'*30)
print('The Total Time Taken :', endtime - begintime)

***************** Result ******************

Double Value :Square Value : 2
 1
Double Value :Square Value : 4
 4
Square Value :Double Value : 6
 9
Square Value :Double Value : 8
 16
Double Value :Square Value : 25
 10
Square Value :Double Value : 12
 36
------------------------------------------------------------
The Total Time Taken : 6.047346115112305

---------------------------------------------------------------------------------------------

How to getName & SetName of the Threads :-
---------------------------------------

from threading import *
print(current_thread().getName())
current_thread().setName('RAJESH SHARMA')
print(current_thread().getName())

************ Result **************
MainThread
RAJESH SHARMA
-----------------------------------------------------------------------------------------
from threading import *
print(current_thread().getName())
current_thread().name = 'FORSK SCHOOL'
print(current_thread().name)

************ Result **************        
RAJESH SHARMA
FORSK SCHOOL
------------------------------------------------------------------------------------------------------------------
To getName :-
----------
t.getName()
t.name

To setName :-
-----------
t.setName()
t.name
---------------------------------------------------------------------------------

Thread Identification Number :- Every Thread is having a unique ID number.
----------------------------
We can get the name of the Unique ID by using Implicit variable = "ident"
Ex :- 

from threading import *

def test():
    print('Child Thread')
t = Thread(target=test)
t.start()
print('The Main Thread Identification Number :', current_thread().ident)
print('The Child Thread Identification Number :', t.ident)    

************ Result **************        
The Main Thread Identification Number : 1740    
The Child Thread Identification Number : 8124
--------------------------------------------------------------------------------------------------------------------
How to count no. of Active threads :- 
----------------------------------
from threading import *
import time
def display():
    print(current_thread().name ,'.... started')
    time.sleep(3)
    print(current_thread().name ,'.....ended')
    
print('The No. of Active Threads :', active_count())
t1 = Thread(target=display,name='Child Thread-1')    
t2 = Thread(target=display,name='Child Thread-2')        
t3 = Thread(target=display,name='Child Thread-3')
t1.start()
t2.start()
t3.start()

print('The No. of Active Threads :', active_count())
time.sleep(10)
print('The No. of Active Threads :', active_count())
 
************ Result **************        
   
The No. of Active Threads : 1 
Child Thread-1 .... started
Child Thread-2 .... started
Child Thread-3 .... started
The No. of Active Threads : 4
Child Thread-1 .... ended
Child Thread-2 .... ended
Child Thread-3 .... ended
The No. of Active Threads : 1
---------------------------------------------------------------------------------------

How to use Enumerate() function in threads :- 
------------------------------------------
from threading import *
import time
def display():
    print(current_thread().name ,'.... started')
    time.sleep(3)
    print(current_thread().name ,'.....ended')
    
print('The No. of Active Threads :', active_count())
t1 = Thread(target=display,name='Child Thread-1')    
t2 = Thread(target=display,name='Child Thread-2')        
t3 = Thread(target=display,name='Child Thread-3')
t1.start()
t2.start()
t3.start()

print('The No. of Active Threads :', active_count())
time.sleep(10)
print('The No. of Active Threads :', active_count())
l = enumerate()
for t in l:
    print('Thread Name :', t.name)
    print('Thread Identification Number :', t.ident)
    print()
time.sleep(10)
l = enumerate()
for t in l:
    print('Thread Name :', t.name)
    print('Thread Identification Number :', t.ident)
    print()    

*********** Result *************

The No. of Active Threads : 5
Child Thread-1Child Thread-2 .... started
Child Thread-3The No. of Active Threads : 8
 .... started
 .... started
Child Thread-1 .....ended
Child Thread-3 .....ended
Child Thread-2 .....ended
The No. of Active Threads : 5
Thread Name : MainThread
Thread Identification Number : 7824

Thread Name : Thread-4
Thread Identification Number : 7200

Thread Name : Thread-5
Thread Identification Number : 7584

Thread Name : IPythonHistorySavingThread
Thread Identification Number : 13196

Thread Name : Thread-3
Thread Identification Number : 9400

Thread Name : MainThread
Thread Identification Number : 7824

Thread Name : Thread-4
Thread Identification Number : 7200

Thread Name : Thread-5
Thread Identification Number : 7584

Thread Name : IPythonHistorySavingThread
Thread Identification Number : 13196

Thread Name : Thread-3
Thread Identification Number : 9400    
-----------------------------------------------------------------------------

How to check Whether thread Alive or dead :-
-----------------------------------------
from threading import *
import time
def display():
    print(current_thread().name ,'.... started')
    time.sleep(3)
    print(current_thread().name ,'.....ended')
    
print('The No. of Active Threads :', active_count())
t1 = Thread(target=display,name='Child Thread-1')    
t2 = Thread(target=display,name='Child Thread-2')        
t1.start()
t2.start()
print(t1.name,'is Alive :',t1.is_alive())
print(t2.name,'is Alive :',t2.is_alive())
time.sleep(10)
print(t1.name,'is Alive :',t1.is_alive())
print(t2.name,'is Alive :',t2.is_alive())

*************** Result *************
Child Thread-1 .... started
Child Thread-2 .... started
Child Thread-1 is Alive : True
Child Thread-2 is Alive : True
Child Thread-1 .....ended
Child Thread-2 .....ended
Child Thread-1 is Alive : False
Child Thread-2 is Alive : False
-----------------------------------------------------------------------------------------

How to use join() method in Threads :-
-----------------------------------
If a thread wants to wait until some threads completing some other threads task.
Ex :- 
Venue Fixing.(t1)
Wedding Cards Printing.(t2)
Wedding Cards Distribution.(t3)

Ex :- 

from threading import *
import time
def test():
    for i in range(5):
        print('Sita Thread')
        time.sleep(3)
        
t = Thread(target=test)
t.start()

**************** Result ****************
Sita Thread
Sita Thread
Sita Thread
Sita Thread
Sita Thread
-----------------------------------------------------------------------------------------------------

from threading import *
import time
def display():
    for i in range(10):
        print('Sita Thread')
        time.sleep(3)
        
t = Thread(target=test)
t.start()

t.join()
for i in range(10):
    print('Rama Thread')
    
**************** Result ****************

Sita Thread
Sita Thread
Sita Thread
Sita Thread
Sita Thread
Sita Thread
Sita Thread
Sita Thread
Sita Thread
Sita Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread
Rama Thread

---------------------------------------------------------------------------------------------

from threading import *
import time
def display():
    for i in range(10):
        print('Sita Thread')
        time.sleep(3)
        
t = Thread(target=test)
t.start()

t.join()
for i in range(10):
    print('Rama Thread')
    
**************** Result ****************
The No. of Active Threads : 5
Child Thread-1Child Thread-2 .... started
Child Thread-3The No. of Active Threads : 8
 .... started
 .... started
Child Thread-1 .....ended
Child Thread-3 .....ended
Child Thread-2 .....ended
The No. of Active Threads : 5
Thread Name : MainThread
Thread Identification Number : 7824

Thread Name : Thread-4
Thread Identification Number : 7200

Thread Name : Thread-5
Thread Identification Number : 7584

Thread Name : IPythonHistorySavingThread
Thread Identification Number : 13196

Thread Name : Thread-3
Thread Identification Number : 9400

    



































        
        
        
                
        
            
    
            
        
    



 
