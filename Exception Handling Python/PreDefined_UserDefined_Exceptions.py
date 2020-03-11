# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:59:02 2020

@author: Rajesh
"""
Types of Exceptions :- There are 2 types of exceptions.
-------------------
1) Pre-defined exceptions :- Which is handled by PVM or In-built python or pre-defined exceptions.
Ex :- 
print(10/0) # ZeroDivisionError: division by zero

x = int('10')
print(x) # 10

x = int('ten')
print(x) # ValueError: invalid literal for int() with base 10: 'ten'

NOTE :- Pre-defined exceptions are also known PVM exceptions or Python In-built exceptions.
NOTE :- These will raised automatically by PVM whenever a particular event occurs.
---------------------------------------------------------------------------------------------------------------

2) User defined exceptions :- 

Ex :- Bank Application.

def withdraw(amount):
    if amount >= balance:
        raise InsufficientFundsExceptions()
    else:
        process request

Ex :- Mobile recharge 
old an days we were recharge coupouns and No. like 123ABVg3409

def recharge(pin):
    if pin is not valid:
        raise InvalidPINExceptions()
        
Ex :- Any Matrimonaly site.
Age limit = 18-60

Age = 99 person wants to registred for a marriage. then we will raise an exception.

TooYoungException()
pls wait for some more time definately you will get the best matched.

Age = 12 person wants to marriage.

TooOldException()
Your age already crossed the marriage age, There is No chance of getting marry.
----------------------------------------------------------------------------------
NOTE :- User defined exceptions are also known as Customized exceptions or Programatic exceptions.

NOTE :- Sometimes we have to define and raised an own exceptions explicitly to 
indicate that something went wrong , such types of exceptions also called as
User defined exceptions or Customized exceptions or Programatic exceptions. 

NOTE :- Programmer / developer is the responsible to define these kind of exceptions
and PVM is not having any idea about these kind of exceptions. Hence we have to 
raised explicitly based on our requirements by using "raise" keyword.
-----------------------------------------------------------------------------------------------------------------------------

How to define and raised Customized Exceptions :- 
----------------------------------------------
NOTE :- Every exception in python is a class and it should be child class of 
BaseException.(or Exception also)

Define an Exception :-
-------------------
syntax :- 

class NameOfException(PredefinedException):
    def __init__(self,msg):
        self.msg = msg
        
Ex  :-
class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg = msg

NOTE :- TooYoungException is our own exception classname and It is the child
class of Exception.   
        
Raise an Exception :- To raise an exception we can use "raise" keyword.
------------------
syntax :- 

raise NameOfException(msg)

Ex :-

raise TooYoungException('msg')
here raise = keyword.
-------------------------------------------------------------------------------------

Ex :- This is simple example of Customized Exception.

class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg = msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg = msg
        
age = int(input('Enter your Age :'))
if age > 60:
    raise TooYoungException('!!! Plz wait for some more time, Definitely you will get the Best matched !!!')
 
elif age < 18:
    raise TooOldException('!!! Your age already crossed marriage Age , No chances of getting Marriage !!!')

else:
    print('!!!! You will get matched details as soon by E-mail !!!!')
   

************** Result ***************
Enter your Age :99
TooYoungException: !!! Plz wait for some more time, Definitely you will get the Best matched !!!
---------------------------------------------------------------------------------------------------------
Enter your Age :12
TooOldException: !!! Your age already crossed marriage Age , No chances of getting Marriage !!!
----------------------------------------------------------------------------------------------------------------------
Enter your Age :25
!!!! You will get matched details as soon by E-mail !!!!
-----------------------------------------------------------------------------------------------------------------------



        
        
        
        
        
        
        
        
        

    
       
        
        
        
        
        
        
        
        
    
        


        

        
        
        
        
        
        
        
        
        
        
        
    
       
        
        








        
        
        
    
        
     













