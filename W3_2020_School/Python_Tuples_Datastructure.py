# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:26:18 2020

@author: Rajesh
"""
'''
Python Tuples Datastructure :- 
---------------------------------
'''
NOTE :- A tuple is a collection which is ordered and unchangeable. 
In Python tuples are written with round brackets.

Ex :- 
tuple1 = (10,20,'Rajesh',201,'Forsk')

tuple1[2] # 'Rajesh'

tuple1[3] # 201

tuple1[-1] # 'Forsk'

tuple1[2:] # ('Rajesh', 201, 'Forsk')

tuple1[-4:-1] # (20, 'Rajesh', 201)

'''
Change Tuple Values :- 
----------------------

Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, 
and convert the list back into a tuple.
'''
Ex :- 
tuple1 = (10,20,'Rajesh',201,'Forsk')

tuple1[1] = 'sharma' # TypeError: 'tuple' object does not support item assignment

tuple1.append(20) # AttributeError: 'tuple' object has no attribute 'append'

NOTE :- Now we will converting the tuple1 from tuple to list data types and do some 
operations and convert back into the tuple data types.

Ex :- 
tuple1 = (10,20,'Rajesh',201,'Forsk')
print(type(tuple1)) # <class 'tuple'>
list1 = list(tuple1)
print(type((list1))) # <class 'list'>
print(list1) # [10, 20, 'Rajesh', 201, 'Forsk']

list1.append('school')
list1.insert(0,'Gududaya-Babu')
print(list1) # ['Gududaya-Babu', 10, 20, 'Rajesh', 201, 'Forsk', 'school']

t1 = tuple(list1)
print(t1) # ('Gududaya-Babu', 10, 20, 'Rajesh', 201, 'Forsk', 'school')


Loop Through a Tuple :- 
-----------------------
Ex :- 

t1 = (10,20,'Rajesh',201,'Forsk')
for i in t1:
    print(i , end=' ')
---------- Result ---------
10 20 Rajesh 201 Forsk 


Check if Item Exists :- 
---------------------------
Ex :- 

t1 = (10,20,'Rajesh',201,'Forsk')
for i in t1:
    if i == 'Rajesh':
        print('Yes!! Item is available into Tuple :', i)
------ Result ---------
Yes!! Item is available into Tuple : Rajesh

Ex :- 

t1 = (10,20,'Rajesh',201,'Forsk')
if 'Forsk' in t1:
    print('Yes!! Item is available into Tuple :', i)
    
'''    
Tuple Length :- 
--------------
To determine how many items a tuple has, use the len() method.
'''    
t1 = (10,20,'Rajesh',201,'Forsk',1001,2001,'School')
print(len(t1)) # 8

'''
Create Tuple With One Item :- 
------------------------------

To create a tuple with only one item, you have to add a comma after the item, 
otherwise Python will not recognize it as a tuple.

'''
Ex :- 

tuple1 = (10,20,30,40,50)
print(type(tuple1)) # <class 'tuple'>

t1 = (10)
print(type(t1)) # <class 'int'>

# How to define the single element tuple.
t1 = (10,)
print(type(t1)) # <class 'tuple'>

Ex :- 

t1 = ('Forsk')
print(type(t1)) # <class 'str'>

# How to define the single element tuple.
t1 = ('Forsk',)
print(type(t1)) # <class 'tuple'>

'''
Remove Items :- 
--------------
'''
NOTE :- We can not remove any items from tuple and tuples are Immutable like strings.

NOTE :- If we want to delete the tuple that we can do it.

Ex :- 

tuple1 = (10,20,30,40,50)

del tuple1 # tuple has been deleted.

print(tuple1) # NameError: name 'tuple1' is not defined

'''
Join Two Tuples :- 
------------------
To join two or more tuples you can use the + operator:
'''

Ex :-

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) # ('a', 'b', 'c', 1, 2, 3)


'''
Tuple Methods :-
---------------
Python has two built-in methods that you can use on tuples.
'''

Ex :- 

tuple1 = (10,20,'Rajesh',20,40,'sharma')
print(tuple1.count(20)) # 2

Ex :- 

tuple1 = (10,20,'Rajesh',20,40,'sharma')
print(tuple1.index('Rajesh')) # 2

print(tuple1.index(40)) # 4

