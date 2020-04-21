# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:11:21 2020

@author: Rajesh
"""

'''
Python Sets Datastructure :- 
-----------------------------
'''
NOTE :- A set is a collection which is unordered and unindexed. 
        In Python sets are written with curly brackets.

Ex :- 
set1 = {10,20,30,40,20,10}

print(set1) # {40, 10, 20, 30}

Ex :- 
set1 = {'Rajesh',100,201,'forsk',1001,'Rajesh'}

print(set1) # {'Rajesh', 100, 201, 'forsk', 1001}


NOTE :-  Sets are unordered, so you cannot be sure in which order the items will appear.
NOTE :- We can not perform slicing into sets data types.

'''
Access Items :- 
--------------
You cannot access items in a set by referring to an index, since sets are unordered the 
items has no index.

But you can loop through the set items using a for loop, or ask if a specified value is
present in a set, by using the in keyword.

'''

Ex :- 
set1 = {'Rajesh',100,201,'forsk',1001,'Rajesh'}

for item in set1:
    print(item)

----- Result ------
Rajesh
100
201
forsk
1001

Ex :- 

Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset) # True

'''
Change Items :- 
----------------
Once a set is created, you cannot change its items, but you can add new items.
'''
'''
Add Items :- 
-------------
To add one item to a set use the add() method.
To add more than one item to a set use the update() method.
'''
Ex :- 

set1 = {'Rajesh',100,201,'forsk',1001,'Rajesh'}
set1.add(2020)
print(set1) # {'Rajesh', 100, 2020, 201, 'forsk', 1001}

set1.add('sharma')
print(set1) # {'Rajesh', 100, 2020, 201, 'forsk', 1001, 'sharma'}

Ex :- 

set1 = {10,20,30,'Rajesh'}
set1.update(['sharma',40,50])
print(set1) # {'Rajesh', 40, 10, 50, 20, 'sharma', 30}

'''
Get the Length of a Set :- 
--------------------------
To determine how many items a set has, use the len() method.
'''
Ex :- 
set1 = {10,20,30,'Rajesh'}
print(len(set1)) # 4

'''
Remove Item :- 
---------------
To remove an item in a set, use the remove(), or the discard() method.
'''
Ex :- 
set1 = {10,20,30,'Rajesh'}
set1.remove('Rajesh')
print(set1) # {10, 20, 30}

Ex :- 

set1 = {10,20,30,'Rajesh'}
set1.discard(20)
print(set1) # {'Rajesh', 10, 30}

NOTE :- If the item to remove does not exist, remove() will raise an error.
NOTE :- If the item to remove does not exist, discard() will NOT raise an error.

Ex :- 
set1 = {10,20,30,'Rajesh'}
set1.remove('sharma') # KeyError: 'sharma'

Ex :- 
set1 = {10,20,30,'Rajesh'}
set1.discard('sharma') # No Error
set1.discard(100) # No Error

'''
You can also use the pop(), method to remove an item, but this method will remove the last item. 
Remember that sets are unordered, so you will not know what item that gets removed.
The return value of the pop() method is the removed item.
'''
Ex :- 

Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) # apple
print(thisset) # {'cherry', 'banana'}


The clear() method empties the set :-
-----------------------------------
Ex :- 
set1 = {10,20,30,'Rajesh'}
set1.clear()
print(set1) # set()


The del keyword will delete the set completely :- 
--------------------------------------------------

thisset = {"apple",100,201,450}

del thisset

print(thisset) # NameError: name 'thisset' is not defined


'''
Join Two Sets :- 
----------------
There are several ways to join two or more sets in Python.
You can use the union() method that returns a new set containing all items from both sets,
or the update() method that inserts all the items from one set into another.
'''
Ex :- 

set1 = {10,20,30,10,40,50}
set2 = {-100,20,70,101}

set3 = set1.union(set2)
print(set3) # {101, 70, 40, 10, 50, 20, -100, 30}

Ex :- 
set1 = {'Rajesh',101,201,'Forsk','sharama',301}
set2 = {301,401,501,'Rajesh'}

set3 = set1.union(set2)
print(set3) # {'Rajesh', 101, 201, 'Forsk', 301, 401, 501, 'sharama'}

Ex :- 

set1 = {10,20,30,10,40,50}
set2 = {-100,20,70,101}

set1.update(set2)
print(set1) # {101, 70, 40, 10, 50, 20, -100, 30}

NOTE :- Both union() and update() will exclude any duplicate items.

'''
The set() Constructor :- 
--------------------------
'''
list1 = [10,20,30,10,'Rajesh',40,'Forsk','Rajesh',10]
print(type(list1))

set1 = set(list1)
print(type(set1))
print(set1) # {'Rajesh', 40, 10, 'Forsk', 20, 30}


'''
copy() method in sets :- 
------------------------
'''
Ex :- 
set1 = {10,20,30,40,50}
set2 = set1.copy()
print(set2) # {10, 20, 30, 40, 50}

set2.add(101)
print(set2) # {50, 20, 101, 40, 10, 30}

print(set1) # {40, 10, 50, 20, 30}

set1.remove(20)
print(set1) # {40, 10, 50, 30}

print(set2) # {50, 20, 101, 40, 10, 30}


'''
Intersection() method in sets : -
---------------------------------
'''
Ex :- 
set1 = {10,20,30,40,50}
set2 = {101,20,90,50,60,201}

set3 = set1.intersection(set2)
print(set3) # {50, 20}

