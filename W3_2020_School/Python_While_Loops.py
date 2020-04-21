# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:57:03 2020

@author: Rajesh
"""
'''
Python While Loops :- 
--------------------
'''
Python Loops :- 
--------------
Python has two primitive loop commands.

1) while loops

2) for loops

The while Loop :- 
---------------
With the while loop we can execute a set of statements as long as a condition is true.

Ex :- 

i = 1
while i < 5 :
    print(i)
    i = i +1
    # i+= 1
----- Result ----------
1
2
3
4

NOTE :- Remember to increment i, or else the loop will continue forever.    
    
Ex :- 

i = 10
while i <= 20:
    print(i , end = ' ')
    i = i + 1
----- Result ----------
10 11 12 13 14 15 16 17 18 19 20 

'''
The break Statement :- 
-----------------------
With the break statement we can stop the loop even if the while condition is true.
'''
i = 1
while i < 10:
    print(i , end=' ')
    if i == 6:
        break
    i = i + 1
----- Result ----------
1 2 3 4 5 6 


'''
The continue Statement :- 
-----------------------
With the continue statement we can stop the current iteration, and continue with the next.  
'''
i = 10
while i < 20:
    i = i + 1
    if i == 15:
        continue
    print(i , end=' ')
----- Result ----------    
11 12 13 14 16 17 18 19 20  # 15 is not there .

'''
The else Statement :-
---------------------
With the else statement we can run a block of code once when the condition no longer is true.    
'''

Ex :- 

NOTE :- Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

----- Result ----------    
1
2
3
4
5
i is no longer less than 6


Examples :- 
------------
Ex :- 

x = 120

while x < 130:
    print(x , end=' ')
    if x == 126:
        break
    x = x + 1
----- Result ----------    
120 121 122 123 124 125 126 


Ex :- 

x = 25

while x < 30:
    x = x + 1
    if x == 28:
        continue 
    print(x , end=' ')

----- Result ----------    
26 27 29 30     

