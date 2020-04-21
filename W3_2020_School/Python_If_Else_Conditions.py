# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:29:31 2020

@author: Rajesh
"""
'''
Python If ... Else Conditions :- 
-----------------------------------
'''
Python Conditions and If statements :- 
-------------------------------------
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

Examples :- 
----------
Ex :- 

a = 200
b = 50

if a == b :
    print('This is True Statement')
else:
    print('This is not True statement')
-------- Result ----------
This is not True statement

Ex :- 

a = 200
b = 50

if a != b :
    print('This is True Statement')
else:
    print('This is not True statement')
-------- Result ----------
This is True Statement

Ex :- 

a = 200
b = 50

if a < b :
    print('This is True Statement')
else:
    print('This is not True statement')
-------- Result ----------
This is not True statement


Ex :- 

a = 200
b = 50

if a <= b :
    print('This is True Statement')
else:
    print('This is not True statement')
-------- Result ----------
This is not True statement


Ex :- 

a = 200
b = 50

if a > b :
    print('This is True Statement')
else:
    print('This is not True statement')
-------- Result ----------
This is True Statement


Ex :- 

a = 200
b = 50

if a >= b :
    print('This is True Statement')
else:
    print('This is not True statement')
-------- Result ----------
This is True Statement

'''
Elif Condition :- 
---------------
The elif keyword is pythons way of saying "if the previous conditions were not true, 
then try this condition".
'''
Ex :- 

x = 100
y = 200

if x == y :
    print('X is equal to the y :', x , y)
elif x < y :
    print('X is lesser than y :', x , y)
-------- Result ----------
    
X is lesser than y : 100 200  

'''
Else Condition :- 
-----------------
The else keyword catches anything which isn't caught by the preceding conditions.
'''
x = 200
y = 50

x = int(input('Enter x value :'))
y = int(input('Enter y value :'))

if x < y :
    print('x is less than y')
elif x == y:
    print('x and y both are equal')
else:
    print('x is greather than y')
    
'''
Short Hand If :- 
--------------
If you have only one statement to execute, you can put it on the same line as the if statement.    
'''
Ex :- 

x = 100
y = 45

if x > y : print('x is greater than y')
# x is greater than y   
    
'''
Short Hand If ... Else Condition :- 
-------------------------------------
If you have only one statement to execute, one for if, and one for else, you can put it 
all on the same line.
'''
Ex :- 

x = 100
y = 90

print('X') if x > y else print('Y') # X

Ex :- 

a = 1000
b = 200

a if a == b else b # 200

Ex :- 

x = 100
y = 200

print('x is less than y') if x < y else print('x is not less than y')
# x is less than y

NOTE :- You can also have multiple else statements on the same line.
Ex :- 

a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B") # =


'''
And condition :- 
----------------
The and keyword is a logical operator, and is used to combine conditional statements.
'''
Ex :- 

x = 200
y = 100
z = 300

if x > y and y < z :
    print('Both the statements are TRUE')
---------- Result --------
Both the statements are TRUE

'''
Or condition :- 
---------------
The or keyword is a logical operator, and is used to combine conditional statements.
'''
Ex :- 

x = 200
y = 100
z = 300

if x > y or y > z :
    print('Atleast one condition should be TRUE')
---------- Result --------
Atleast one condition should be TRUE


'''
Nested If Condition :- 
-------------------------
You can have if statements inside if statements, this is called nested if statements.
'''
Ex :- 

x = 50

if x > 20:
    print('Above 20 !!')
    if x > 49:
        print('Above 49 !!')
    else:
        print('Not above 50 !!')
---------- Result --------
Above 20 !!
Above 49 !!

'''
The pass Statement :- 
-----------------------
if statements cannot be empty, but if you for some reason have an if statement with no
 content, put in the pass statement to avoid getting an error.
'''
Ex :- 
        
x = 100
y = 200

if x == y :
    pass
elif x < y :
    print('x is less than y')
---------- Result --------
x is less than y

