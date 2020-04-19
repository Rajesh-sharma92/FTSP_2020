# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:50:09 2020

@author: Rajesh
"""
'''
Python Booleans :- 
------------------
'''
NOTE :- Booleans represent one of two values: True or False.
Ex :- 

print(10 > 9) # True

print(10 == 9) # False

print(10 < 9) # False

print(2020==2020) # True


Ex :- Print a message based on whether the condition is True or False.

x = 100
y = 99

if x > y:
    print('X is greater than Y')
else:
    print('X is not greater than Y')

------------ Result -----------
X is greater than Y

'''
Evaluate Values and Variables :- 
-------------------------------
'''

NOTE :- The bool() function allows you to evaluate any value, and give you True or False 
in return.

Ex :-  

Evaluate a string and a number:

print(bool("Hello")) # True

print(bool(15)) # True

print(bool(10+20j)) # True


'''
Evaluate two variables :- 
-----------------------
'''

x = 100
y = 2020.2020
z = 'Forsk coding school'
c = 25+35j

l1 = [10,20,30,40]
t1 = (100,200,300)
d1 = {'Name':'Rajesh','RollNo':1001}

print(bool(x))
print(bool(y))
print(bool(z))
print(bool(c))
print(bool(l1))
print(bool(t1))
print(bool(d1))
---------- Result ------------
True
True
True
True
True
True
True

''''
Most Values are True :- 
----------------------
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

Any None Values are None Means It will be evaluated to False only.
Any Value is assign to False will be be evaluated to False only.
'''
Ex :- 

x = 0
y = ''
l1 = []
t1 = ()
d1 = {}
a = None
b = False

print(bool(x))
print(bool(y))
print(bool(l1))
print(bool(t1))
print(bool(d1))
print(bool(a))
print(bool(b))
------------ Result -------------
False
False
False
False
False
False
False


'''
Functions can Return a Boolean : - 
--------------------------------
'''
Ex :- 

def f1(): # Function defining
    return True

f1() # Function calling

Ex :- 

Print "YES!" if the function returns True, otherwise print "NO!".

def f1():
    return True

if f1():
    print('YES!!')
else:
    print('NO!!')
-------- Result ------
YES!!


NOTE :- Python also has many built-in functions that returns a boolean value, like the 
isinstance() function, which can be used to determine if an object is of a certain data type.

Ex :- 

x = 2020
print(isinstance(x , int)) # True

x = 2020.2020
print(isinstance(x , int)) # False

x = 'FORSK CODING SCHOOL'
print(isinstance(x , str)) # True

x = 25.20
print(isinstance(x , float)) # True

x = 10+55j
print(isinstance(x , complex)) # True


Ex :- 

sum1 = 200

x = int(input('enter the x value :'))
y = int(input('enter the y value :'))
print('The sum of x & y are :', (x+y))

if ((x+y) > sum1):
    print(True)
else:
    print(False)

------------- Result -------------
enter the x value :200

enter the y value :400
The sum of x & y are : 600
True


enter the x value :100

enter the y value :99
The sum of x & y are : 199
False

    
