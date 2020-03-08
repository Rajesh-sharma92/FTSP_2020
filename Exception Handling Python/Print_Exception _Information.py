# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:38:17 2020

@author: Rajesh
"""
How to print exception Information :-
----------------------------------
try:
    print(10/0)
except ZeroDivisionError as msg: # msg is the reference variable and 'as' is the keyword in python.
    print('The Type of an Exception :', type(msg)) # he Type of an Exception : <class 'ZeroDivisionError'>
    
    print('The class of an Exception :', msg.__class__) # The Type of an Exception : <class 'ZeroDivisionError'>
    
    print('The Name of an Exception class :', msg.__class__.__name__) # The Name of an Exception class : ZeroDivisionError
    
    print('The Description of an Exception :' , msg) # The Description of an Exception : division by zero
    
*********** Result *************    
The Type of an Exception : <class 'ZeroDivisionError'>
The Type of an Exception : <class 'ZeroDivisionError'>
The Name of an Exception class : ZeroDivisionError
The Description of an Exception : division by zero

NOTE :- Here in the place of msg any kind of name we can use like x , y , exception and e and etc. 
but on the place of "as" it is python keyword it is constant and we can not changed it to any names.
---------------------------------------------------------------------------------------------------------------------------------
try:
    print(10/0)
except ZeroDivisionError as e:
    print('The Type of an Exception :', type(e))
    print('The class of an Exception :', e.__class__)
    print('The Name of an Exception class :', e.__class__.__name__)
    print('The Description of an Exception :' , e)

*********** Result *************    
The Type of an Exception : <class 'ZeroDivisionError'>
The Type of an Exception : <class 'ZeroDivisionError'>
The Name of an Exception class : ZeroDivisionError
The Description of an Exception : division by zero
----------------------------------------------------------------------------------------------------------------------
try:
    x = int(input('Enter first number :'))
    y = int(input('Enter first number :'))
    print('The Result :', x/y)
except BaseException as msg:
    print('Type of Exception :', type(msg))
    print('Class of Exception :',msg.__class__)
    print('Class Name of Exception :', msg.__class__.__name__)
    print('Description of an Exception :',msg)

*********** Result *************        
Enter first number :20

Enter first number :0
Type of Exception : <class 'ZeroDivisionError'>
Class of Exception : <class 'ZeroDivisionError'>
Class Name of Exception : ZeroDivisionError
Description of an Exception : division by zero
--------------------------------------------------------------
Enter first number :20

Enter first number :rajesh
Type of Exception : <class 'ValueError'>
Class of Exception : <class 'ValueError'>
Class Name of Exception : ValueError
Description of an Exception : invalid literal for int() with base 10: 'rajesh'
----------------------------------------------
Enter first number :50

Enter first number :5
The Result : 10.0
------------------------------------------------------------------------------------------------------

NOTE :- It is very very Important topic.

try block with multiple except blocks :-
-------------------------------------
NOTE :- The way of handling an exception is varied from exception to exception.

NOTE :- Hence for every possible exception type , we have to take a seperate 
except block. try with multiple except blocks are possible and recommanded to use also.
Ex :- syntax
try:
    .....
    .....
    .....
except ZeroDivisionError:
    perform alternative Arithematic error
except FileNotFoundError:
    use local file instead of remote file
    
If try with multiple except blocks are available, then based on raised exception
the corresponding except block will be executed.
Ex :- 

try:
    x = int(input('Enter first number :'))
    y = int(input('Enter second number :'))
    print('The Result :', x/y)
except ZeroDivisionError:
    print('can not divide by zero')
except ValueError:
    print('Please provide Integer value only')

************ Result ***********    
Enter first number :10

Enter second number :5
The Result : 2.0
------------------------------------------------------------------    
Enter first number :10

Enter second number :0
can not divide by zero    
----------------------------------------------------------    
Enter first number :10

Enter second number :forsk
Please provide Integer value only
--------------------------------------------------------------------------------    
NOTE :- If try block with multiple except blocks available then the order of these 
except blocks are very Important. PVM will always consider from top to bottom until 
matched except block identified.

Ex :- 

try:
    print(10/0)
except ZeroDivisionError:
    print('Zero Division Error')
except ArithmeticError:
    print('Arithmetic Error')
 
************ Result ***********    
Zero Division Error
---------------------------------------------------------------------------------
try:
    print(10/0)
except ArithmeticError:
    print('Arithmetic Error')
except ZeroDivisionError:
    print('Zero Division Error')
 
************ Result ***********   
Arithmetic Error
-----------------------------------------------------------------------------------------------

NOTE :- Plaese look into this one solution also.

Single except block that can handle multiple different exceptions :-
-----------------------------------------------------------------
NOTE :- If handling code is same for multiple exceptions, then instead of taking 
different except blocks, We can take single except block to handle all those exceptions.
like :-
except(excp1 , excp2 ,....., excpn):
    
except(excp1 , excp2 ,....., excpn) as msg:
    
NOTE :- Paranthesis are mandatory and this group of exceptions internally considerd as tuple.    

Ex :-

try:
    x = int(input('Enter first number :'))
    y = int(input('Enter second number :'))
    print('The Result :', x/y)
except(ZeroDivisionError,ValueError) as msg:
    print('Exception Name :', msg.__class__.__name__)
    print('Description of Exception :', msg)
    print('Please provide valid Input only')
    
************ Result ***********       
Enter first number :10

Enter second number :2
The Result : 5.0
---------------------------------------------------------------------------------
Enter first number :10

Enter second number :0
Exception Name : ZeroDivisionError
Description of Exception : division by zero
Please provide valid Input only
---------------------------------------------------------------------------------
 Enter first number :10

Enter second number :forsk
Exception Name : ValueError
Description of Exception : invalid literal for int() with base 10: 'forsk'
Please provide valid Input only
--------------------------------------------------------------------------------------------------------



   
    
    
    
    
    
    
    

























  
    
    

    
    


    



    
















