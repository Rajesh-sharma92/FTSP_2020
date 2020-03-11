# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:04:21 2020

@author: Rajesh
"""
else block with try-except-finally :- 
----------------------------------
In Python we can use else, with if conditions , with loops and as well as with 
try-except-finally blocks also.

if-else :- 
-------

x = 10
if x > 10:
    print('x > 10')
else:
    print('x is not > 10')
    
********* Result ************
x is not > 10

Question :- When will be else part executed in the above program ?
Answer :- The else part always executed when, if condition false then only the 
above else condition executed successfully.
-----------------------------------------------------------------------------------
loops with else :-
---------------
for x in range(10):
    print('The Current item :', x)
else:
    print('!!! Congratulations All items processed Successfully !!!')
********* Result ************
The Current item : 0
The Current item : 1
The Current item : 2
The Current item : 3
The Current item : 4
The Current item : 5
The Current item : 6
The Current item : 7
The Current item : 8
The Current item : 9
!!! Congratulations All items processed Successfully !!!    
----------------------------------------------------------------------------------
for x in range(10):
    if x > 5:
        break
    print('The Current item :', x)
else:
    print('!!! Congratulations All items processed Successfully !!!')    
********* Result ************    
The Current item : 0
The Current item : 1
The Current item : 2
The Current item : 3
The Current item : 4
The Current item : 5
------------------------------------------------------------------------------------------
Question :- When will be else part executed inside loops ?
Answer :- We can see the above 2 examples and there if loops did not encountered 
by break statement then always else part will be executed without any error.
But, If the loops encountered by break statment then else part of the loops 
will not be executed and that will be coming out of this things.
---------------------------------------------------------------------------------
x=1
while x < 10:
    print('The Current item :', x)
    x = x + 1 
else:
    print('!!! Congratulations All items processed Successfully !!!')

********* Result ************    
The Current item : 1
The Current item : 2
The Current item : 3
The Current item : 4
The Current item : 5
The Current item : 6
The Current item : 7
The Current item : 8
The Current item : 9
!!! Congratulations All items processed Successfully !!!
---------------------------------------------------------------------------------
x=0
while x < 10:
    if x > 5:
        break
    print('The Current item :', x)
    x = x + 1 
else:
    print('!!! Congratulations All items processed Successfully !!!')

********* Result ************    
The Current item : 1
The Current item : 2
The Current item : 3
The Current item : 4
The Current item : 5
-----------------------------------------------------------------------------------------------------
if-else ===> If condition false then only else part will be executed.

for-else ===> If loop executed without break statement then only the else part
will be executed.

while-else ===> If loop executed without break statement then only the else part
will be executed.
-------------------------------------------------------------------------------------------------------------
NOTE :- We can use else block with try-except-finally blokcs.
NOTE :- If there is No exception in try block then only the else block 
will be executed without any issue.
---------------------------------------------------------------------------------------------------------
Syntax :-
try:
    Risky codes
except:
    Handling codes
    It will be exceuted if there is any exception inside try block.
else:
    It will be exceuted if there is No exception inside try block.
finally:
    cleanUp codes
    It will be executed always wheather exception raised or not raised and 
    Handled or not handled.
-------------------------------------------------------------------------------------------------------------
Ex :- If There is No exception inside try block.

try:
    print('try-block')
except ZeroDivisionError:
    print('except-block')
else:
    print('else-block')
finally:
    print('finally-block')

*********** Result ***********
try-block
else-block
finally-block
-------------------------------------------------------------------------------------------
Ex :- If There is an exception inside try block.

try:
    print('try-block')
    print(10/0)
except ZeroDivisionError:
    print('except-block')
else:
    print('else-block')
finally:
    print('finally-block')

*********** Result ***********
try-block
except-block
finally-block

Question :- When will be except-block & else-block will be executed at simultansouly ?
Answer :- Here in the above 2 examples we can see that except & else blocks are never
executs simultensouly coz both will executed on condition based.

NOTE :- If except block executed then else block will not be executed and If else
block executed then except block will be executed.
------------------------------------------------------------------------------------------------------------------
try:
    print('try-block')
else:
    print('else-block')
finally:
    print('finally-block')
    
********** Result ************
SyntaxError: invalid syntax

NOTE :- We can not use else block without except block. If we are using else block
then we must use the except block or else there will be the syntax error.
--------------------------------------------------------------------------------------------------
f = None
try:
    f = open('E:/Durga OOPs/Files Handling/feedback.txt','r')
except:
    print('There is some problems while locating or openning file')
else:
    print('The file opened Successfully')
    print('The Contents of the file')
    print('*'*30)
    print(f.read())
finally:
    if f is not None:
        f.close()
********** Result ************        
The file opened Successfully
The Contents of the file
******************************
sitapura jaipur sikar 

------------------------------------------------------------------------------------------------------------------
f = None
try:
    f = open('E:/Durga OOPs/Files Handling/feedback1.txt','r')
except:
    print('There is some problems while locating or openning file')
else:
    print('The file opened Successfully')
    print('The Contents of the file')
    print('*'*30)
    print(f.read())
finally:
    if f is not None: # It means f is pointing to some existing file.
        f.close()

********** Result ************    
There is some problems while locating or openning file
-------------------------------------------------------------------------------------------------------------

Which of the following is TRUE about else-block :-
-----------------------------------------------
1) We can use else block with try-except-finally blocks only.
    
2) We can say that else block will be executed if there is No exception 
inside try-block.

3) There is No chances of both except-else block will be executed similtansouly.

4) We can say that else block can not be used without using except-block and If
we are using then syntax error.

NOTE :- Here we can see that above all 4 statements are TRUE.   

 
    
















        
        
    
    
    




















    
    
    
    
    
    
    



























































































