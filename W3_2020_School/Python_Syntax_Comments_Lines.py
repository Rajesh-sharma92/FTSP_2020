# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:35:37 2020

@author: Rajesh
"""
'''
Python Indentation :- 
------------------

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, 
the indentation in Python is very important.

Python uses indentation to indicate a block of code.
'''
Ex :- 

a = 20 
b = 10

if a > b:
    print('Yes, This is the Right Condition !!') # Indentation takes place here.

print('The A & B are :', a , b)    

---------------  Result -----------------------    
Yes, This is the Right Condition !!
The A & B are : 20 10




NOTE :- Python will give you an error if you skip the indentation.

a = 20 
b = 10

if a > b:
print('Yes, This is the Right Condition !!') # There is No Indentation.

print('The A & B are :', a , b)    
 
---------------  Result -----------------------    
   
IndentationError: expected an indented block    

NOTE :- The number of spaces is up to you as a programmer, but it has to be at least one.

x = 100
y = 25

if x > y:
            print('Yes, This is the Right Condition !!') # Here we have given 2 tab spaces.
            
---------------  Result -----------------------    
Yes, This is the Right Condition !!


--------------------------------------------------------------------------------------------------            
'''
Python Comments :- 
----------------
'''
Comments can be used to explain Python code.
Comments can be used to make the code more readable.
Comments can be used to prevent execution when testing code.

Comments starts with a #, and Python will ignore them.

Most of the times we will be using the comments in the last of the any line codes.

a = 10
b = 20
print('The Addition of A & B are :', a+b) # The Addition of a & b values. # This is single line comment.

---------------  Result -----------------------    
The Addition of A & B are : 30


x = 100
y = 200

if x < y:
    print(True)
else:
    print(False)
    
---------------  Result -----------------------    
True

NOTE :- Comments can be placed at the end of a line, and Python will ignore the rest of the line.


NOTE :- Comments does not have to be text to explain the code, it can also be used to prevent 
        Python from executing code:
    

# print('Please check these below information') # It won't executed at all coz we have put the #.
            
print('This is Rajesh sharma here from Sikar,Rajasthan.')    

print('I have completed my Machine Learning Course at Forsk Coding School,Jaipur,Rajasthan.')

---------------  Result -----------------------    
This is Rajesh sharma here from Sikar,Rajasthan.
I have completed my Machine Learning Course at Forsk Coding School,Jaipur,Rajasthan.            
    

'''
Multi Line Comments :- 
--------------------
Python does not really have a syntax for multi line comments.

To add a multiline comment you could insert a # for each line.
'''

a = 10
b = 20
print('The Values are :', a*b) # The Values are : 200

NOTE :- If we want to ignore the above full code then we have 2 options either we can put 
"#" before starting every line or else put it into triple quotes (''' ''').

Ex :- 

# a = 10
# b = 20
# print('The Values are :', a*b) 
---------------  Result -----------------------    
Here we will not getting any kind of result coz all the lines are commentted by "#" symbol.


Ex :- 

'''
a = 10
b = 20
print('The Values are :', a*b) 

'''
---------------  Result -----------------------    
Here we will not getting any kind of result coz all the lines are commentted by "#" symbol.

