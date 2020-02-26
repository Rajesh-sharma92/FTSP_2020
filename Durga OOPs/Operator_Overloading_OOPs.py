# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:41:59 2020

@author: Rajesh
"""
Polymorphism :-  
------------
Polymorphism
Duck Typing phylosophy of Python.
Overloading :-
-----------
1) Operator Overloading 
2) Method Overloading 
3) Constructor Overloading 

Overriding :-
----------
1) Method Overriding
2) Constructor Overriding
----------------------------------------------------------------------------------------------------
Polymorphism :- 
------------
poly means Many
morphs means forms 

one name but many forms.

Examples :- HOME :- class , book , temple , college.
outside of home but with friends.
brand , cigar , cinema , park ...........
outside of his native palce.
different color .

Ex :- A person plays many roles in a day ?
Morning Time : Tea
Afternoon Time : Butter Milk
Night Time : Beer , Brandy

Ex :- A boy starts LOVE with the word friendship , but girl ends with LOVE with the same word friendship.
Word is same but purpose is the different.

overloading :- 
-----------
10+20 ==> 30
'durga'+'soft' ==> durgasoft

10*3 ==> 30
'durga'*3 ==> durgadurgadurga

deposit(cash)
deposit(cheque)
deposit(DD)

Operator Overloading :- 
--------------------
+ 
*
any operator in python
< , <= , > , >=

Example :-

class Book:
    def __init__(self,pages):
        self.pages = pages
        
b1= Book(100)
b2 = Book(200)
print(b1+b2) # unsupported operand type(s) for +: 'Book' and 'Book'.

NOTE :- Java does not support to Operator Overloading concept but Python supports to the Operator Overloading.
NOTE :- Supports means it must support to our own created objects also.
NOTE :- Java supports to Operator Overloading but some of the concepts.
-------------------------------------------------------------------------------------------------

NOTE :- Internally, Python magic method will be supporting to the Operator Overloading concept in python.
NOTE :- Operator Overloading methods are internally implemented into python by using the magic methods.
-------------------------------------------------------------------------------------------------------
Operator Overloading by using Magic Methods :-
-------------------------------------------

1) + ===> __add__()
    
    __add__(self,other)
    
    how many objects are there in book class.
    two objects are there means vaule will be supplying like this self = b1 & other = b2.
    
Ex :- 

class Book:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        return self.pages + other.pages
        
b1= Book(100)
b2 = Book(200)
b3 = Book(700)
print(b1+b2) # 300
print(b1+b3) # 800
print(b2+b3) # 900
print(b1+b2+b3) # unsupported operand type(s) for +: 'int' and 'Book'. It will  not support coz magic method is implemented for 2 variable

NOTE :- By seeing the above examples we can say that python provides support for Operator Overloading but by using Magic Methods.
NOTE :- print(b1+b2+b3+b4+n) ---> # unsupported operand type(s) for +: 'int' and 'Book'.

class Book:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        return self.pages + other.pages   
        
    def __sub__(self,other):
        return self.pages - other.pages
    
    def __mul__(self,other):
        return self.pages * other.pages
    
    def __div__(self,other):
        return self.pages/other.pages
        
b1= Book(100)
b2 = Book(200)
b3 = Book(700)
print(b1+b2) # 300
print(b1-b2) # -100
print(b1*b2) # 20000
print(b1/b2) # 300
---------------------------------------------------------------------------------------------------
Arithematic Operators :-
---------------------
1) + ==> __add__()
2) - ==> __sub__()
3) * ==> __mul__()
4) / ==> __div__()
5) % ==> __mod__()
6) // ==> __floordiv__()
7) ** ==> __pow__()
    
    
Assignments Opeartors :-
---------------------    
1) +=    ==> __iadd__()
2) -=    ==> __isub__()
3) *=    ==> __imul__()
4) /=    ==> __idiv__()
5) %=    ==> __imod__()
6) //=   ==> __ifloordiv__()
7) **=   ==> __ipow__()    
    
Relational Opearators :-
---------------------
1) >     ==> __gt__()
2) >=    ==> __ge__()
3) <     ==> __lt__()
4) <=    ==> __le__()
5) ==    ==> __eq__()
6) !=    ==> __ne__()

NOTE :- Where ever we will getting like this kind of function __xyz__() methods are called as Magic methods.
NOTE :- All magic methods are pre-defined in the python and all are having some special meaning.
NOTE :- We can not change anything into it.
NOTE :- All are very useful & easy to use.
---------------------------------------------------------------------------------------------------------
Question :- Can we use same magic methods in a class more than once ?
Answer :- Yes. We can use it more than one magic method but always last one will be executed.
Python will be consider that last one magic method in a class.

NOTE :- Method overloading concept is not available in Python.
NOTE :- Same method in a class we can define more than once with different bhavioral & finctions but
always last one will be executed coz python does not support to Method overloading.








    
    











    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























    
    
    





























-------------------------------------------------------------------------------------------------------












































