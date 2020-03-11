# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:33:12 2020

@author: Rajesh
"""
Various possible combinations of try-except-finally blocks :- 
----------------------------------------------------------
1)
try:
    print('try')

**** Result********    
SyntaxError: unexpected EOF while parsing

NOTE :- We can not use single try-block and it will be invalid. Always we need 
to use atleast one of them like except or finally blocks.
NOTE :- try-block must be associated with any of them like except or finally blocks.

NOTE : It is In-valid.
--------------------------------------------------------------------------------------------------------------------------
2)
except:
    print('except')
**** Result********        
SyntaxError: invalid syntax    

NOTE :- If we are using except block then there should be the try block always.    
Except-block is used for handling the exception but if there is No exception in 
try-block then no need to use the except and It is meaningless codes.

NOTE : It is In-valid.
-------------------------------------------------------------------------------------------------------------------------
3) 
else:
    print('else')
**** Result********        
SyntaxError: invalid syntax    

NOTE :- If we are using else-block there should be the except-block and if 
except-block then compulsory try-block must be there. 

NOTE : It is In-valid.
------------------------------------------------------------------------------------------------------
4) 
finally:
    print('finally')
**** Result********        
SyntaxError: invalid syntax    

NOTE :- finally-block is meant for to cleanUp the codes / Resources  which is  
opened inside the try-block.

NOTE : It is In-valid.
-------------------------------------------------------------------------------------------
5) 
try:
    print('try')
except:
    print('except')

******* Result ***********    
try 
NOTE : It is Valid.    
-----------------------------------------------------------------------------------------------------------
6) 
try:
    print('try')
else:
    print('else')

******* Result ***********    
SyntaxError: invalid syntax

NOTE :- As we know that else block without except-block is Invalid.
NOTE : It is In-valid.
----------------------------------------------------------------------------------------
7) 
try:
    print('try')
finally:
    print('finally')
 
******* Result ***********    
try
finally
NOTE : It is Valid.  
--------------------------------------------------------------------------------------------------
8)
try:
    print('try')
else:
    print('else')
except:
    print('except')
    
******* Result ***********    
SyntaxError: invalid syntax

NOTE :- Here we have got an error coz we must follow the order always. except-block
should be first than to else. Except-block must be followed by else-block always.
NOTE :- Here we can see that order is very Important and we need to always this 
order only like try-->except-->else-->finally.

NOTE : It is In-valid.
--------------------------------------------------------------------------------------------------------------------------
9) 
try:
    print('try')
else:
    print('else')
finally:
    print('finally')

******* Result ***********    
SyntaxError: invalid syntax 

NOTE :- We can say that without except-block we can not use the else-block.
    
NOTE : It is In-valid.
-----------------------------------------------------------------------------------------------------    
10) 
try:
    print('try')
except:
    print('except')
else:
    print('else')
finally:
    print('finally')
    
******* Result ***********    
try
else
finally

NOTE :- In the above ex-10 , we can say that if there is an error in try block 
then akways except block will be executed.
NOTE :- If there is No exception inside try-block then always else-block will be executed.
NOTE : It is Valid.    
-------------------------------------------------------------------------------------------------------------------------
11) 
try:
    print('try')
except:
    print('except')
try:
    print('try')
finally:
    print('finally')
    
******* Result ***********        
try
try
finally  
NOTE :- Here in the above example we can see that try is followed by except 
and one more try-block followed by finally-block and we can use like this.
NOTE : It is Valid. 
--------------------------------------------------------------------------------------------------------------------------
12) 
try:
    print('try')
except:
    print('except')
try:
    print('try')
else:
    print('else')

******* Result ***********      
SyntaxError: invalid syntax

NOTE :- Here we can see that in the above example try is followed by except and it is valid but try is followed by
else block is not valid combination and coz we can see that the combination shuold be like 
try-except-else and it is valid combination.

NOTE : It is In-Valid. 
--------------------------------------------------------------------------------------------------------------------
13)
try:
    print('try')
except XXX:
    print('except-1')
except YYY:
    print('except-2')
    
******* Result ***********      
try

NOTE :- Single try-block can be associated with multiple except blocks.
NOTE : It is Valid. 
----------------------------------------------------------------------------------------------------
14) 
try:
    print('try')
except:
    print('except')
else:
    print('else-1')
else:
    print('else-2')
    
******* Result ***********     
SyntaxError: invalid syntax

NOTE :- Single except-block can not be associated with multiple else blocks.
NOTE : It is In-Valid. 
NOTE :- Here we can not take more than one else block.
----------------------------------------------------------------------------------------------------------------------
15)
try:
    print('try')
except:
    print('except')
finally:
    print('finally-1')
finally:
    print('finally-2')
    
******* Result ***********      
SyntaxError: invalid syntax

NOTE :- Single try-block can not be associated with multiple finally blocks.
NOTE : It is In-Valid. 
NOTE :- Here we can not take more than one finally block.
----------------------------------------------------------------------------------------------------------
16)
try:
    print('try')
except:
    print('except')
if 10 > 20:
    print('if')
else:
    print('else')
    
******* Result ***********        
try
else

NOTE :- Here we can see that in above example first try is associated with except block and it is valid.
and If statement is associated with normal else statement and this else is nowhere is related to try block 
and It is valid statements.
NOTE : It is Valid.
--------------------------------------------------------------------------------------------------------------------------
17)
try:
    print('try')
print('Hello')
except:
    print('except')

******* Result ***********        
SyntaxError: invalid syntax    

NOTE :- try-block and except-block is fine but outside of the try we are using
that print statement is not valid and it will be throwing an error.
NOTE :- Here between try-except we can not write any Indepandant statements all these are Invalid statements.
NOTE : It is In-Valid.
----------------------------------------------------------------------------------------
18)
try:
    print('try')
except XXX:
    print('except-1')    
print('Hello')
except YYY:
    print('except-2')    
******* Result ***********        
SyntaxError: invalid syntax    

NOTE :- We can not use any Indepandent statements between 2 except blocks coz 
both are invalid in the program.
NOTE : It is In-Valid.
------------------------------------------------------------------------------------------------------------
19)
try:
    print('try')
except:
    print('except')    
print('Hello')
else:
    print('else')    
******* Result ***********        
SyntaxError: invalid syntax       

NOTE :- We can say that we can not use any Indepandent statements between except-block
and else-block.
NOTE : It is In-Valid.
-----------------------------------------------------------------------------------------------------------------
20)
try:
    print('try')
except:
    print('except')    
print('Hello')
finally:
    print('finally')    
******* Result ***********        
SyntaxError: invalid syntax      
NOTE :- We can say that we can not use any Indepandent statements between except-block
and finally-block.
NOTE : It is In-Valid.
----------------------------------------------------------------------------------------------------------------------
21)
try:
    print('outer try')
    try:
        print('Inner try')
    except:
        print('Inner except')
    finally:
        print('Inner finally')
     
except:
    print('Outer except')

******* Result ***********        
outer try
Inner try
Inner finally
NOTE : It is Valid.
----------------------------------------------------------------------------------------------------------------
22) 
try:
    print('outer try')
except:
    try:
        print('Inner try')
    except:
        print('Inner except')    
        
******* Result ***********        
outer try        
NOTE : It is Valid.
----------------------------------------------------------------------------------------------------------
23) 
try:
    print('try')
except:
    print('except')
else:
    try:
        print('try')
    finally:
        print('finally')
    
******* Result ***********     
try
try
finally   
NOTE : It is Valid.
--------------------------------------------------------------------------------------------
24) 
try:
    print('try')
except:
    print('except')
finally:
    try:
        print('try')
    except:
        print('except')
    
******* Result ***********    
try
try
NOTE : It is Valid.
-------------------------------------------------------------------------------------------
25)
try:
    try:
        print('Inner try')
except:
    print('except')

******* Result *******
IndentationError: unexpected unindent    
NOTE : It is In-Valid.
-------------------------------------------------------------------------------------
26)     
try:
    try:
        print('Inner try')
    finally:
        print('Inner finally')
except:
    print('except')

******* Result *******    
Inner try
Inner finally
NOTE : It is Valid.
--------------------------------------------------------------------------------------

Important Conclusions try-except-finally blocks :-
-----------------------------------------------
1) Whenever we are writing try-block then compulsory we should write except or 
finally with it.
i.e., try-block without except or finally blocks are Invalid statements.

2) Whenever we are writing except-block then compulsory try-block must be there.
i.e., except-block is invalid without writing try-block.

3) Whenever we are writing finally-block then compulsory try-block must be there.
i.e., finally-block is invalid without writing try-block.
     
4) Whenever we are writing else-block then compulsory except-block should be there.
i.e., Without except-block it is Invalid statements.

5) We can write multiple except-blocks for the same try-block, but we can not 
write multiple else and finally blocks for that same try.

6) We must know that try-except-else-finally order is very Important.

7) We can write try-except-else-finally inside try-block,except-block,else-block
and finally-block. Hence we can say that nesting of try-except-else-finally
blocks are always possible.

-------------------------------------------------------------------------------------------------------------------------------

    









    
    
    
    







    
    
    

























    
    
    
    
    


  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















    
    
    















     


























































    
    





















