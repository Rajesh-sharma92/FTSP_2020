# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:04:56 2020

@author: Rajesh
"""

Control flow in nested try-except-finally :- 
----------------------------------------
Ex :-

try:
    stmt1
    stmt2
    stmt3
    try:
        stmt4
        stmt5
        stmt6
    except XXX:
        stmt7
    finally:
        stmt8
    stmt9    
except YYY:
    stmt10
finally:
    stmt11
stmt12
------------------------------------------------------------------------------------------

Case - 1 :- If there is NO exception.
Answer :- 1,2,3,4,5,6,8,9,11,12 and NT / GT.
-------------------------------------------------------------------------------------
Case - 2 :- If there is exception raised at stmt2 and corresponding except block matched.
Answer :- 1,10,11,12 and NT / GT.
-----------------------------------------------------------------------------------------------------
Case - 3 :- If there is exception raised at stmt2 and corresponding except block not matched.
Answer :- 1,11 and AT.
------------------------------------------------------------------------------------------------------------
Case - 4 :- If an exception raised at stmt5 and Inner except block matched.
Answer :- 1,2,3,4,7,8,9,11,12 and NT / GT.
-------------------------------------------------------------------------------------------------------------
Case - 5 :- If an exception raised at stmt5 and Inner except block not matched but Outer except block. matched
Answer :- 1,2,3,4,8,10,11,12 and NT / GT.
-------------------------------------------------------------------------------------------------------------
Case - 6 :- If an exception raised at stmt5 and Inner except & Outer except block both not matched.
Answer :- 1,2,3,4,8,11 and AT.
----------------------------------------------------------------------------------------------------------------------
Case - 7 :- If an exception raised at stmt7 and corresponding except block matched.
Answer :- 1,2,3,. , . , . , 8,10,11,12 and NT / GT. NOTE :- . means may or may not be executed.
-----------------------------------------------------------------------------------------------------------------
Case - 8 :- If an exception raised at stmt7 and corresponding except block not matched.
Answer :- 1,2,3,. ,., . , 8,11 and AT.
----------------------------------------------------------------------------------------------------------------------
Case - 9 :- If an exception raised at stmt8 and corresponding except block matched.
Answer :- 1,2,3, . , . , . , . , 10,11,12 and NT / GT.
-----------------------------------------------------------------------------------------------
Case - 10 :- If an exception raised at stmt8 and corresponding except block not matched.
Answer :- 1,2,3,. , . , . , . , 11 and AT.
---------------------------------------------------------------------------------------------------
Case - 11 :- If an exception raised at stmt9 and corresponding except block matched.
Answer :- 1,2,3,. , . , . , . , 8,10,11,12 and NT / GT.
---------------------------------------------------------------------------------------------------------
Case - 12 :- If an exception raised at stmt9 and corresponding except block not matched.
Answer :- 1,2,3, . , . , . , . , 8 , 11 and AT.
---------------------------------------------------------------------------------------------------------------------
Case - 13 :- If an exception raised at stmt10.
Answer :- If an exception raised at stmt10 then It is always AT, but before AT 
only finally block will be executed. like stmt11.
-------------------------------------------------------------------------------------------------------------------
Case - 14 :- If an exception raised at stmt11 & stmt12.
Answer :- If an exception raised at stmt11 & stmt12 then always AT coz these stmt11 & stmt12 are not part of any try 
blocks and there is No except blocks also.
-----------------------------------------------------------------------------------------------------------------------












 

















































































    
    
    





        