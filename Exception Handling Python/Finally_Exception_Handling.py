# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:36:10 2020

@author: Rajesh
"""
finally Keyword :-
---------------

NOTE :- Pls see that example.

try:
    open db connection
    read data from db ---> If we get any exception in this statement then control will goes to except block.
    close db connection ---> Resource de-allocation code / Cleanup code
except:
    handling code
    
NOTE :- If we get any exception in this statement then control will goes to except block.
and close db connection will not executed and one db connection will be wasted.

Question :- Is it recommanded to use cleanup code inside try block ?
Answer :- It is not recommanded to use cleanup code inside the try block coz if we get
any kind of exception before cleanup code defined then close db connection statement 
will not executed at all. It is not a good practice to use cleanup code inside the
try block as a programmer.
------------------------------------------------------------------------------------

try:
    open db connection
    read data from db ---> If there is NO exception inside try block.
except:
    close db connection ---> Resource de-allocation code / Cleanup code
    
NOTE :- If there is NO exception inside try block. Then except block will be never executed at all.
It is very worst condition to use cleanup code inside the except block.

NOTE :- It is not recommanded to use cleanup code inside the except block.
----------------------------------------------------------------------------------------------------
try:
    Risky code
except:
    Handling code
finally:
    CleanUp code
    
NOTE :- In the above example we can see that all 3 blocks purposes.
try block to mention the Risky code.
except block to mention the handling code.
finally block is to used for CleanUp code mention.

NOTE :- finally block always will be executed irrespectively of wheather exception 
raised or not and exception handled or not does not matter at all.    

NOTE :- finally block is recommanded to use for CleanUp code and it is very 
responsible for cleanUp code execution and it will be executed always.

Question :- What is the purpose of finally block in Python ?.
Answer :- The purpose of finally block to maintain the CleanUp code and it will 
be executed always irrespectively of wheather exception raised or not and 
exception handled or not does not matter at all. 
-------------------------------------------------------------------------------------------------

There are some Important case we will be discussing  :-
---------------------------------------------------
case - 1 :- If No exception.

try:
    print('try block')
except ZeroDivisionError:
    print('except block')
finally:
    print('finally block')

************* Result ************    
try block
finally block

NOTE :- If there is No exception inside try block then except block never executed.
finally block always executed irrespectively of wheather exception raised or not and 
exception handled or not does not matter at all.
------------------------------------------------------------------------------------------------------------------------
Case - 2 :- If an exception raised and handled also.

try:
    print('try block')
    print(10/0)
except ZeroDivisionError:
    print('except block')
finally:
    print('finally block')    

************* Result ************    

try block
except block
finally block
NOTE :- Here is the normal / Graceful termination.
-----------------------------------------------------------------------------------------------------
Case - 3 :- If an exception raised but not handled.

try:
    print('try block')
    print(10/0)
except ValueError:
    print('except block')
finally:
    print('finally block')    

************* Result ************   
try block
finally block

ZeroDivisionError: division by zero

NOTE :- Here we can see that ZeroDivisionError came but handled for except block 
available for ValueError exception only, So it will not be able to handle the exception
and Program execution will be terminated as Abnormally.
NOTE :- finally block always executed irrespectively of wheather exception raised or not and 
exception handled or not does not matter at all.
NOTE :- The specility of finally block is that first finally block will be 
executed then Abnormal termination of the program.
-------------------------------------------------------------------------------------------------------------------
Question :- Could you please tell me when will be the finally block will not be executed ?.
Answer :- finally block always executed irrespectively of wheather exception raised or not and 
exception handled or not does not matter at all.
If we use os._exit(0) then finally block will not executed and PVM will be down.

Ex :- 

import os

try:
    print('try block')
    # os._exit(0)
except ValueError:
    print('Except block')
finally:
    print('finally block')

************* Result*********
try block


NOTE :- If we are using os._exit(0) program will terminate there only and it will not executed further.
NOTE :- here 0 means status code and here we can use any number like +ve & -ve and it will be terminated the 
program but If we are using 0 means Normal/Graceful termination and non-zero means Abnormal termination internally.
------------------------------------------------------------------------------------------------------------------

os._exit(0) Vs. finally block :-
-----------------------------
NOTE :- There is only one situtaion where finally block will not be executed if we are
using os._exit(0).
NOTE :- Whenever we are using os._exit(0) then python virtual machine itself 
will be shutdown. In this particular case finally block will not executed.

 




    
    
    














































    


























