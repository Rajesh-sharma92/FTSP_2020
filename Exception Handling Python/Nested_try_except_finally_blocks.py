# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:33:18 2020

@author: Rajesh
"""

Nested try-except-finally blocks :- 
--------------------------------
We can take nesting of try-except-finally blocks pls see the below example.

try: # Outer try-block
    # General Risky codes.
    ......
    try: # Inner try-block
        ...
        # Too Much Risky codes.
        
    except: # Inner except-block
        ...
    finally:
        ....
        
except: # outer except-block
    
    try:
        ...
    except:
        ...
    finally:
        ....  
        
finally:
    try:
        ...
    except:
        ...
    finally:
        ....        
        
NOTE :- We can take try-except-finally inside try or except or finally blocks.
Hence nesting of try-except-finally blocks are possible.

NOTE :- General Risky codes we need to take inside the Outer try-block and Too much
Risky codes we should take inside the inside the Inner try-block.

NOTE :- Inside Inner try-block If an exception raised then Inner except-block
is the responsible to handle it. If it is unable to handle it then Outer except-block
is responsible to handle it.
--------------------------------------------------------------------------------------------------------------------
Ex :- If there is NO exception.

try:
    print('Outer try block')
    try:
        print('Inner try block')
    except ZeroDivisionError:
        print('Inner except block')
    finally:
        print('Inner finally block')
except:
    print('Outer except block')
finally:
    print('Outer finally block')
    
************** Result ************
Outer try block
Inner try block
Inner finally block
Outer finally block
-------------------------------------------------------------------------------------------------------

Ex :- If there is exception in Inner try block and matched in except block and handled.

try:
    print('Outer try block')
    try:
        print('Inner try block')
        print(10/0)
    except ZeroDivisionError:
        print('Inner except block')
    finally:
        print('Inner finally block')
except:
    print('Outer except block')
finally:
    print('Outer finally block')
    
************** Result ************
Outer try block
Inner try block
Inner except block
Inner finally block
Outer finally block
-------------------------------------------------------------------------------------
Ex :- If there is exception in Inner try block and but not matched by Inner except block.

try:
    print('Outer try block')
    try:
        print('Inner try block')
        print(10/0)
    except ValueError:
        print('Inner except block')
    finally:
        print('Inner finally block')
except:
    print('Outer except block')
finally:
    print('Outer finally block')

*********** Result ************
Outer try block
Inner try block
Inner finally block
Outer except block
Outer finally block
----------------------------------------------------------------------------------
Ex :- If there is exception in inside Outer try block.
    
try:
    print('Outer try block')
    print(10/0)
    try:
        print('Inner try block')
    except ValueError:
        print('Inner except block')
    finally:
        print('Inner finally block')
except:
    print('Outer except block')
finally:
    print('Outer finally block')

*********** Result ************    
Outer try block
Outer except block
Outer finally block

NOTE :- If the control not entered in the try block then finally block will not be
executed.

NOTE :- If the control entered in the try block then finally block compulsory 
will be executed.

-----------------------------------------------------------------------------------------


        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




















        