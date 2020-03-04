# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:46:32 2020

@author: Rajesh
"""

Question :- What is an exception ?
Answer :- Exceptions are also known as Runtime errors.
Runtime exceptions may be occured anytime in our day to day life like.
Runtime errors are those which occured while exceuting program / performing some task / 
doing some activities.

Runtime errors are like :- 
--> If we are watching some vedio / film through internet and suddenly Internet connection 
has been lost then Runtime error occured.
--> If we are trying to open some of the file but file does not exists into the system
then we will be getting any error like FileNotFoundError on console.
--> If we are going for shopping at market by bike and suddenly bike type punctured then 
we can not go to the market by using bike. so, such kind of TyrePuncturedError occured.
--> If we are attending any class and then we are getting sleep into the class then such 
kind of error SleepingError like runtime errors.
---> ValueError , ZeroDivisionError and etc.

"An unwanted and unexpected event then disturbs normal flow of program is called Exception."

Question :- Is it good or bad thing exceptions ?
Answer :- Exceptions are bad things coz our normal flow of program will be unexcepted 
terminated or throw some kind of errors so, handle these things we must use the 
Exception handling concepts.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Question :- What is the main objective of Exception Handling ?
Answer :-   It is highly recommanded to handle exceptions.
The main objective of exception handling Graceful Termination / Normal Termination
of the application.(i.e we should not block our resources and we should not miss anything.)
------------------------------------------------------------------------------------------------------------------------

Question :- What is the meaning of exception handling ?
Answer :- Exception handling does not mean repairing any exception. We have to define
alternative way to continue rest of the program exeuction normally.

This way of defining alternative is nothing but exception handling.
Ex :- Travling to native by bus and other services.

Ex :- 
try :
    Read the data from remote file which is locating at london.
except : 
    FileNotFoundError , Use the local file and continue rest of the program normally.
------------------------------------------------------------------------------------------------------------------------------------
NOTE :- Every exception in the python is Object. like ZeroDivisionError , ValueError and etc.
-------------------------------------------------------------------------------------------------------------
Default Exception handling in python :-
------------------------------------
print('!!! Hello Froends !!!')
print(10/0)
print('Forsk school') # We will not get this line result coz in the above line exception is there and It will not exexcuted further.

******** Result **************
!!! Hello Froends !!!

print(10/0)
ZeroDivisionError: division by zero

NOTE :- This is abnormal termination done by the PVM.
Question :- Who is the responsible to terminate the program abnormally ?
Answer :- Here PVM is the responsible to terminate coz there is runtime error in program.
----------------------------------------------------------------------------------------------------------
NOTE :- Every exception in the python is Object.For every exception type corresponding 
class is available.:
NOTE :- To pre-event this is abnormal termmination ,we should handle exception explicitly
Ofcourse by using try-except blocks.
--------------------------------------------------------------------------------------------------------------------------------
    


























    
    































