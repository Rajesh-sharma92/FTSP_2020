# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:17:50 2020

@author: Rajesh
"""
Default except Block :-
--------------------
NOTE :- We can use default except block to handle any kind of exceptions.
Default except block, Generally we can print exception information to the console.

syntax :-

except: # except keyword and just write only colon.
    statements
    
Ex :-

try:
    x = int(input('Enter first number :'))
    y = int(input('Enter second number :'))
    print('The Result :', x/y)
except ZeroDivisionError:
    print('Zero Division Error : can not divide by zero')
except: # Default Except Block
    print('Default Except Block : please provide only Integer values')

************* Result *************
Enter first number :10

Enter second number :2
The Result : 5.0
------------------------------------------------------------------------------    
Enter first number :10

Enter second number :0
Zero Division Error : can not divide by zero
-------------------------------------------------------------------------------
Enter first number :10

Enter second number :rajesh
Default Except Block : please provide only Integer values
---------------------------------------------------------------------------------------------------------------

Ex :- If there is No zeroDivisionError block also default except will be handle such exceptions.

try:
    x = int(input('Enter first number :'))
    y = int(input('Enter second number :'))
    print('The Result :', x/y)
except: # Default Except Block
    print('Default Except Block : please provide only Integer values')

************* Result *************

Enter first number :10

Enter second number :0
Default Except Block : please provide only Integer values
-----------------------------------------------------------------------------
Enter first number :20

Enter second number :forsk
Default Except Block : please provide only Integer values
    
NOTE :- Default except block can handle any kind of execptions and executed it.
It is just using for general purpose and just displaying message on console.
---------------------------------------------------------------------------------
NOTE :- Can i define default except like this pls see in the below example ?
Ex :-

try:
    x = int(input('Enter first number :'))
    y = int(input('Enter second number :'))
    print('The Result :', x/y)
except: # Default Except Block
    print('Default Except Block : please provide only Integer values')
except ZeroDivisionError:
    print('Zero Division Error : can not divide by zero')

************* Result *************
SyntaxError: default 'except:' must be last

NOTE :- PVM always give the chance to search for specific except block for an exception occured 
from top to bottom.
But here default except block can any kind of exceptions and it will not give the chance
to any other except blocks to handle those particular exceptions.
NOTE :- Always default except block, We must need to defined as last in the program.
----------------------------------------------------------------------------------------------------------------
NOTE :- If there are multiple except blocks but default except block must be at last only.

try:
    x = int(input('Enter first number :'))
    y = int(input('Enter second number :'))
    print('The Result :', x/y)
except ValueError:
    print('Value Error : Integer values only ')
except ZeroDivisionError:
    print('Zero Division Error : can not divide by zero')
except: # Default Except Block
    print('Default Except Block : please provide only Integer values')

************* Result *************
Enter first number :10

Enter second number :0
Zero Division Error : can not divide by zero
--------------------------------------------------------------------------------
Enter first number :10

Enter second number :forsk
Value Error : Integer values only 

-------------------------------------------------------------------------------------------------------------------

Various possible Combinations of except blocks :-
----------------------------------------------

except ZeroDivisionError: ---> Valid 

except (ZeroDivisionError): ---> Valid 
    
except ZeroDivisionError as msg: ---> Valid 

except (ZeroDivisionError) as msg: ---> Valid 
    
except (ZeroDivisionError,ValueError): ---> Valid 

except (ZeroDivisionError,ValueError) as msg:  ---> Valid 
    
except: # Default except block. ---> Valid 
    
NOTE :- We can say that all these above combinations are valid for except blocks.

------------------------------------------------------------------------------------------------------------------

NOTE :- Now we need to define some of these except block combinations are valid or not ?
-----------------------------------------------------------------------------------------
except (ZeroDivisionError as msg): ---> Invalid 
# coz as msg always comes outside of the paranthesis.

except ZeroDivisionError,ValueError: ---> Invalid 
# coz whenever we are using multiple exception then we must use the paranthesis as tuple forms.

except (ZeroDivisionError,ValueError as msg): ---> Invalid 
# coz as msg always comes outside of the paranthesis.

NOTE :- If except block is defined only for only one exception then paranthesis
is optional. If multiple exceptions are there then we must use the paranthesis and 
paranthesis are mandatory.

NOTE :- If we use the paranthesis then "as" keyword we must use outside of 
paranthesis only or else it will throw an execption.

----------------------------------------------------------------------------------------------------------------
    























    












































    

