# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:11:38 2020

@author: Rajesh
"""
'''
Python Operators :- 
--------------------
'''
NOTE :- Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

1) Arithmetic operators
2) Assignment operators
3) Comparison operators
4) Logical operators
5) Identity operators
6) Membership operators
7) Bitwise operators

'''    
1) Arithmetic operators :- 
-------------------------    
'''

NOTE :- Arithmetic operators are used with numeric values to perform common mathematical operations.
Ex :- 

x = 20
y = 10
print('The Addition :', (x+y))
print('The subtraction :', (x-y))
print('The Multiplication :', (x*y))
print('The Division :', (x/y))
print('The Modulus :', (x%y))
print('The Exponentiation (power) :', (x**y))
print('The Floor division :', (x//y))
-------- Result --------------
The Addition : 30
The subtraction : 10
The Multiplication : 200
The Division : 2.0
The Modulus : 0
The Exponentiation (power) : 10240000000000
The Floor division : 2

------------------------------------------------------------------------------------------------
'''
2) Assignment operators :- 
---------------------------    
'''
NOTE :- Assignment operators are used to assign values to variables.

x = 100
print('The X value :', x) # The X value : 100

x = 5
x+= 3
print('The X value :',x) # The X value : 8

x = 5
x-= 3
print('The X value :',x) # The X value : 2

x = 5
x*= 3
print('The X value :',x) # The X value : 15

x = 5
x/= 3
print('The X value :',x) # The X value : 1.66

x = 5
x%= 3
print('The X value :',x) # The X value : 2


x = 5
x**= 3
print('The X value :',x) # The X value : 125


x = 5
x//= 3
print('The X value :',x) # The X value : 1


x = 5
x|= 3
print('The X value :',x) # The X value : 7


x = 5
x^= 3
print('The X value :',x) # The X value : 6


x = 5
x>>= 3
print('The X value :',x) # The X value : 0


x = 5
x<<= 3
print('The X value :',x) # The X value : 40

---------------------------------------------------------------------------------------------------
'''
3) Comparison operators :- 
---------------------------
'''

NOTE :- Comparison operators are used to compare two values.

Ex :- 

x = 10
y = 20

print('The Equal :', (x == y))
print('The Not  Equal:',(x != y))
print('The Greater than  :', (x > y))
print('The Less than :', (x < y))
print('The Greater than or Equal to :', (x >= y))
print('The Less than or Equal to  :', (x <= y))
-------------------- Result ------------
The Equal : False
The Not  Equal: True
The Greater than  : False
The Less than : True
The Greater than or Equal to : False
The Less than or Equal to  : True

-------------------------------------------------------------------------------------------------
'''
4) Logical operators :- 
----------------------
'''
NOTE :- Logical operators are used to combine conditional statements. 

Ex :- and operator 

x = 100
print(x > 50 and x < 101) # True

Ex :- 

x = 250
if x == 250 and x < 251:
    print('This is Right Condition') # This is Right Condition
    
    
Ex :- or operator 

x = 200
print(x > 250 or x < 251) # True

 
x = 250
if x == 250 or x < 251:
    print('This is Right Condition') # This is Right Condition


Ex :- not operator  

x = 50
print(not(x < 51 and x == 50)) # False

Ex :- 
x = 200
print(not(x > 250 or x < 251))  # False

------------------------------------------------------------------------------------------------------
'''
5) Identity operators :- 
-------------------------
'''

Ex :- 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # True

# returns True because z is the same object as x

print(x is y) # False

# returns False because x is not the same object as y, even if they have the same content

print(x == y) # True

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(id(x)) # 169254792
print(id(y)) # 170140168
print(id(z)) # 169254792


Ex :- 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) # False

# returns False because z is the same object as x

print(x is not y) # True

# returns True because x is not the same object as y, even if they have the same content

print(x != y) # False

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

-----------------------------------------------------------------------------------------------------
'''
6) Membership operators :- 
--------------------------    
'''
Ex :-  in operator 

x = [10,20,30,40,50]

if 30 in x:
    print(True)
else:
    print(False)
--------- Result -----------
True

Ex :- 

list1 = [10,-99,'Forsk','Rajesh']
print('Forsk' in list1) # True


Ex :- not in 

x = [10,20,30,40,50]

if 100 not in x:
    print(True)
else:
    print(False)
--------- Result -----------
True

Ex :- 

list1 = [10,-99,'Forsk','Rajesh']
print('Forsk' not in list1) # False

list1 = [10,-99,'Forsk','Rajesh']
print('sharma' not in list1) # True

----------------------------------------------------------------------------------------------------
'''
7) Bitwise operators :- 
-------------------------    
'''
Bitwise operators are used to compare (binary) numbers:

Operator	Name	              Description
& 	         AND	                Sets each bit to 1 if both bits are 1
|	         OR	                    Sets each bit to 1 if one of two bits is 1
 ^	         XOR	                Sets each bit to 1 if only one of two bits is 1
~ 	         NOT	                Inverts all the bits
<<	         Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	         Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
      
