# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:48:52 2020

@author: Rajesh
"""
finally block Vs. Destructor :-
----------------------------
finally block meant for maintaining cleanup codes.

Destructor meant for maintaining cleanup codes.

seems to be the same..............

where is the difference ???????????
-----------------------------------------------------------------------------
NOTE :- finally block meant for cleanup activities ralated to try block. i.e.
whatever the resources we have opened as the part of try block will be closed
inside finally block.

NOTE :- Destructor meant for cleanup activities related to object. Whatever resources
associated with the object should be de-allocated inside destructor, which will be
executing before destroying object.
------------------------------------------------------------------------------------------------

Control Flow in try-except-finally :-
----------------------------------
try:
    stmt1
    stmt2
    stmt3
except xyz:
    stmt4
finally:
    stmt5

stmt6 # it is the outside of the finally block.It is Indepandent statement.
    
--------------------------------------------------------------------------------------
Case - 1 :- If there is No exception.
Answer :- 1,2,3,5,6 and NT/GT.
------------------------------------------------------------------------------
Case - 2 :- If an exception raised at stmt2 and corresponding except block matched.
Answer :- 1,4,5,6 and NT/GT.
------------------------------------------------------------------------------------------
Case - 3 :- If an exception raised at stmt2 and corresponding except block did not matched.
Answer :- 1,5 and AT.
----------------------------------------------------------------------------------------
Case - 4 :- If an exception raised at stmt4.
Answer :- If an exception raised at stmt4 (like in except block) then always Abnormal
termination will be happening in the program and always finally block will exceuted if it is there.
only 5 and AT.

NOTE :- If except block stmts are not part of any try block then Always will AT.
------------------------------------------------------------------------------------------
Case - 5 :- If an exception at stmt5 & stmt6.
Answer :- Here we can see that stmt5 in finally block but if it not part of the try block
and always will be abnormal termination.
For stmt6 is the outside of the finally block and not part of try block the 
always willl be AT.
------------------------------------------------------------------------------------------------------
Ex :- 1

try:
    print('This is Forsk Coding School')
    print('Rajesh sharma from sikar,Rajasthan')
    print('Forsk is at Sitapura RIICO Area')
except ZeroDivisionError:
    print('Except block')
finally:
    print('finally block always executed if it is not forecefully terminated by os._exit(0)')
print('This is outside of the finally block')

******************** Result ************
This is Forsk Coding School
Rajesh sharma from sikar,Rajasthan
Forsk is at Sitapura RIICO Area
finally block always executed if it is not forecefully terminated by os._exit(0)
This is outside of the finally block
----------------------------------------------------------------------------------
Ex :- 2

try:
    print('stmt1')
    print(10/0)
    print('stmt3')
except ZeroDivisionError:
    print('stmt4')
finally:
    print('stmt5')
print('stmt6')

******************** Result ************
stmt1
stmt4
stmt5
stmt6
And Normal Termination / Graceful Termination.
---------------------------------------------------------------------------------------
Ex :- 3

try:
    print('stmt1')
    print(10/0)
    print('stmt3')
except ValueError:
    print('stmt4')
finally:
    print('stmt5')
print('stmt6')

******************** Result ************
stmt1
stmt5
And Abnormal termination will be happens.
---------------------------------------------------------------------------------------------
Ex :- 4

try:
    print('stmt1')
    print('stmt2')
    print('stmt3')
except ZeroDivisionError:
    print(10/0)
finally:
    print('stmt5')
print('stmt6')

******************** Result ************
stmt1
stmt2
stmt3
stmt5
stmt6
------------------------------------------------------------------------------------
Ex :- 5

try:
    print('stmt1')
    print('stmt2')
    print('stmt3')
except ZeroDivisionError:
    print('stmt4')
finally:
    print(10/0)
print(200/0)

******************** Result ************
stmt1
stmt2
stmt3
ZeroDivisionError: division by zero And AT.
----------------------------------------------------------------------------------













    
    
    

























 

    
    
    



















