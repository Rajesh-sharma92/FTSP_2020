# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:07:48 2020

@author: Rajesh
"""
NOTE :- Every exception in python is a class.

NOTE :- All exception classess are child classes of BaseException either directly
or Indirectlty and hence base exception acts as root for python exception Hierarachy.

NOTE :- Being, a programmer,most of the times, we have to concerate / handle exception 
and its child classes.


Customized exception handling by using try-except :-
-------------------------------------------------
without using try-except block :-
------------------------------
print('stmt1') ---> Open DB connection.
print(10/0) # Read the data from here.
print('stmt3') ---> Close DB connection.

************* Result **************
stmt1 
ZeroDivisionError 
Abnormal termmination 
Non-Graceful termination

ex :- In the above example we can say that first server will be opened means connected
and then there is NO one is there to close the connection we are having next line dis-continued.
---------------------------------------------------------------------------------------------------------
with using try-except block :-
---------------------------
NOTE :- The code which may rise the error is called as Risky error.
syntax :-
try:
    Risky Code
except:
    handling code / Alternative code
    
Question :- When the except block will be executed ?
answer :- If we try block does not executed in the program then we will be going 
for except block and we will be executed except successfully and program will be 
executed normally.
ex :-
print('stmt1')
try :
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print('stmt3')
 
*********** Result ***********
stmt1
5.0   
stmt3
NOTE :- In the above program we can see that normal / Graceful termination.
---------------------------------------------------------------------------------------------------
Customized exception handling by using try-except :-
-------------------------------------------------
It is highly recommanded to handle exceptions.
The code which may raise an exception is called Risky code and we have to that
Risky code inside try block.
The corresponding code we have to take inside except block.
-----------------------------------------------------------------------------------------------------------
try & except blocks control flows :-
---------------------------------
Condition-1 :-  If there is No exception. {Means except block never executed.}
try: # try block
    stmt1
    stmt2
    stmt3
except XXX: # except block 
    stmt4 # Inside except block 
stmt5 # Outside except block 

********** Result ********
stmt1
stmt2
stmt3
stmt5

NOTE :- If there is No exception in the above code then except block will not be 
executed at all and Normal termination/Graceful termination.
-----------------------------------------------------------------------------------------------
Condition-2 :- If an exception raised at the stmt2 and corresponding except block matched.

********** Result ********
stmt1 
stmt4
stmt5
NOTE :- Just Normal / Graceful termination are there in the above program.
NOTE :- One more important thing is that one you got the error at stmt2 in try block
and then corresponding except block is there then immediatly control will go to
except block and executed the except block codes and then rest of the codes:
will be executed successfully but control will never goes to back to stmt3 execution.
coz try is the main flow and except is the alternative flow.
NOTE :- Consider a example like if you are not getting bus then you will be trying 
for train ticket and after getting the train ticket will you go back to bus.
You will not go to back.
NOTE :- Inside the try block always we should take only the Risky codes coz once we 
get the error and even though we are handling the error also but rest of the try block
codes will not executed at all. We need to take the less codes inside the try block.
----------------------------------------------------------------------------------------------------------
Condition-3 :- If an exception raised at the stmt2 and corresponding except block not matched.

******** Result *************
stmt1 
There will be Abnormal termination coz we do not have corresponding except block to handle the error.
The rest of the codes will not be executed at all.
----------------------------------------------------------------------------------------------
Condition-4 :- If an exception raised at stmt4 & stmt5 then what will be flow of program ?.

********** Result ************
NOTE :- There will be always Abnormal termination coz stmt4 inside the except block and stmt5 outside 
of the except block and always Abnormal termination will be there.
NOTE :- If any kind of exception raised into try block then except block is the 
responsible for that error to resolve it but not apart from try block codes.

NOTE :- There are possibilites of raised an exception in any blocks like try block,
except block and finally block also.

NOTE :- If any statement which is not part of try block and raising an exception
and there will be always Abnormal Termination.
---------------------------------------------------------------------------------------------------------------
    
    
    


    
    


    
    
    





    
    
    


































                