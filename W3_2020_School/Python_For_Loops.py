# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:32:39 2020

@author: Rajesh
"""
'''
Python For Loops :- 
--------------------
'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
Ex :-                                                   

list1 = [10,20,'Rajesh',-100,'Forsk',350]
for x in list1:
    print(x , end=' ')
----------- Result ----------
10 20 Rajesh -100 Forsk 350 

'''
Looping Through a String :-
---------------------------
Even strings are iterable objects, they contain a sequence of characters:                                                  
'''
Ex :- 

str1 = 'forsk coding school'

for x in str1:
    print(x , end=' ')
----------- Result ----------
f o r s k   c o d i n g   s c h o o l 


'''
The break Statement :- 
--------------------------
With the break statement we can stop the loop before it has looped through all the items.
'''
Ex :- We need to break when item is equal to the 'forsk'.

list1 = ['Rajesh','sharma','sikar','forsk','school']

for x in list1:
    if x == 'forsk':
        break 
    print(x , end = ' ')

----------- Result ----------
Rajesh sharma sikar 

Ex :- 

list1 = (10,'forsk',0,401,-119,10)

for x in list1:
    if x == -119:
        break 
    print(x , end = ' ')
----------- Result ----------
10 forsk 0 401 


'''
The continue Statement :- 
---------------------------
With the continue statement we can stop the current iteration of the loop, and continue with the next.
'''
Ex :- 

list1 = ['Raj',101,205,'Usha','Babudaya',2020]

for x in list1:
    if x == 205:
        continue
    print(x , end=' ')
----------- Result ----------
Raj 101 Usha Babudaya 2020 

Ex :- 

t1 = (10,20,30,'forsk',101,2010,2020)

for x in t1:
    if x == 'forsk':
        continue
    print(x , end =' ')
----------- Result ----------
10 20 30 101 2010 2020 

'''
The range() Function :- 
------------------------
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and 
increments by 1 (by default), and ends at a specified number.    
'''
Ex :- 

for x in range(10):
    print(x , end=' ')
----------- Result ----------
    
Ex :- 

for x in range(25,30):
    print(x , end=' ')
----------- Result ----------
25 26 27 28 29 


NOTE :- The range() function defaults to increment the sequence by 1, however it is 
possible to specify the increment value by adding a third parameter: range(2, 20, 3).

Ex :- 

for x in range(2,20,3):
    print(x , end=' ')
----------- Result ----------
2 5 8 11 14 17 


'''
Else in For Loop :- 
------------------
The else keyword in a for loop specifies a block of code to be executed when the 
loop is finished.
'''
Ex :- Print all numbers from 15 to 20, and print a message when the loop has ended.

for x in range(15,20):
    print(x)
else:
    print('!! We have printed all the required Nos. on Console !!')
----------- Result ----------
15
16
17
18
19
!! We have printed all the required Nos. on Console !!

Ex :- 

str1 = 'Rajesh'
for x in str1:
    print(x)
else:
    print('!!! Message has been printed on screen successfully !!!')
----------- Result ----------
    
R
a
j
e
s
h
!!! Message has been printed on screen successfully !!!    

'''  
Nested Loops :- 
----------------
A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop".
'''
Ex :- 

list1 = range(3)
list2 = range(3)

for x in list1:
    for y in list2:
        print(x , y)
----------- Result ----------
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2  

Ex :- 

list1 = ['Rajesh','Usha']
list2 = ['Babudaya','Gududaya']

for x in list1:
    for y in list2:
        print(x , y)
    else:
        print('!! Both are made for each other !!')
        
----------- Result ----------
Rajesh Babudaya
Rajesh Gududaya
!! Both are made for each other !!
Usha Babudaya
Usha Gududaya
!! Both are made for each other !!

'''
The pass Statement :- 
-----------------------
for loops cannot be empty, but if you for some reason have a for loop with no content, 
put in the pass statement to avoid getting an error.
'''
Ex :- 

for x in [0,1,3]:
    pass
else:
    print('We have used the "PASS" statement')
----------- Result ----------   
We have used the "PASS" statement

Ex :- 

for x in range(0,5):
    pass
-------- Result -------
# No Error

Ex :-

for x in range(5,10):
    pass
else:
    print('There is No error at all Coz we have used the "PASS" statement')
----------- Result ----------   
There is No error at all Coz we have used the "PASS" statement.


NOTE :- WAP to print the even and Odd numbers from 0 to 20.

Even Numbers :- 
------------
for x in range(20):
    if x%2==0:
        print(x , end=' ')
        
----------- Result ----------   
0 2 4 6 8 10 12 14 16 18 

        
Odd Numbers :- 
------------
for x in range(20):
    if x%2!=0:
        print(x , end=' ')
        
----------- Result ----------   
1 3 5 7 9 11 13 15 17 19 

    