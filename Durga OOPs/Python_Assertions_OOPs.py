# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:12:06 2020

@author: Rajesh
"""
Python Assertions in Simple Way :- 
-------------------------------
Assertions :- 
----------
Assertions are used / perform in Debuging purposes.

What is the Meaning of Debugging ?
Debugging means removing buggs from the programs.

Debugging :- 
---------
The process of identifying the bugs and fixing of those bugs in the program and 
getting the expected result/output is called as debugging.

NOTE :- The most usages of debugging is using the print statements.

NOTE :- Once we have got the expected Result then we need to remove all those print 
statements from the program. If we are not removing all those print statements from 
the program then the performance will be down and unwanted print msgs will be on
server console and server logs will be disturbed. No use for it.

NOTE :- To remove such kind of above server logs & Performance Issue we will go 
for a Concept is called Assertions.
-------------------------------------------------------------------------------------------
There are 3 Enviroments :
-------------------------
1) Development Enviroment
2) Test Enviroment
3) Production / Live Enviroment
    
NOTE :- Usually we can perform debugging only in Development or Test Enviroment.
We can not perform debugging on Production / Live Enviroment.

NOTE :- To remove such kind of above server logs & Performance Issue we will go 
for a Concept is called Assertions. The Main purposes of Assertations are to performing
debugging.

NOTE :- What is the biggest Advantage of print statements and Assertations ?
Here after fixing the bugs we are not required to delete the asserations statements.
because those Assertations statements will not be executed.

NOTE :- Based on our requirements  we can enable or disable the Asserations statements.
NOTE :- Asseratations we can perform only in Development or Test Enviroment.
We can not perform Asseratations on Production / Live Enviroment.

Question :- Is there any difference between bug and runtime error ?
Answer :-  

Defect , Bug , Error

NOTE :- Any mismatched identified by testing team between expected result and Original
result is called as Defect.

NOTE :- If testing team got the defect and after they send a defect build to developer
and once the developer as accepted then that defect will become as Bug.

NOTE :- Once the developer has fixed the bug then moved to production enviroment
and while executing the program in production if we are getting any identified 
mismatched then that will be called
--------------------------------------------------------------------------------------------

Types of assert Statements :- 
--------------------------
1) Simple Version 
2) Augmented Version
-------------------------------------------------------------------------------------
1) Simple Version :-
-----------------
syntax :- 
assert conditional_experssion
    AssertionError
------------------------------------------------------------------------------
Ex :- 
x = 10

# some lines codes


assert x==10

# some lines codes

print(x)

************* Result ********
10
-----------------------------------------------------------------------------------------------------------
Ex :- 

x = 10

# some lines codes


assert x > 10 # AE

# some lines codes

print(x)
  
************* Result ********
AssertionError  
---------------------------------------------------------------------------------------------------------
Ex :- 

x = 20

# some lines codes


assert x > 10 # AE

# some lines codes

print(x)
  
************* Result ********
20
------------------------------------------------------------------------------------------------------------------------------------
2) Augmented Version :- 
--------------------
syntax :- 
assert conditional_experssion,msg
    AssertionError

Ex :- 

x = 10

# some lines codes


assert x > 10,'Here X value should be greater than 10 but it is not'

# some lines codes

print(x)

************* Result ********
AssertionError: Here X value should be greater than 10 but it is not
----------------------------------------------------------------------------------------------------------------------
Ex :- 

def squareIt(x):
    return x*x

assert squareIt(2) == 4 , 'The square of 2 should be 4'
assert squareIt(3) == 9 , 'The square of 3 should be 9'
assert squareIt(4) == 16 , 'The square of 4 should be 16'

print(squareIt(2))
print(squareIt(3))
print(squareIt(4))

************* Result ********
4
9
16

-------------------------------------------------------------------------------------------------------------------------
NOTE :- How to use Asstertations concept into python and spyder Anaconda?













    





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    