# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:44:34 2020

@author: Rajesh
"""
'''
Python Lists :-
--------------
'''
NOTE :- In python list order of elements are preserved :- 
--------------------------------------------------------
Ex :- 

list1 = [10,20,30,40,50]

list1[0] # 10

list1[3] # 40

list1[-1] # 50

list1[1:3] # [20, 30]

list1[2:] # [30, 40, 50]

list1[:] # [10, 20, 30, 40, 50]

list1[ : : 2] # [10, 30, 50]

Syntax :- [ start : end : step ]
-------

for item in list1:
    print(list1)

----------------
[10, 20, 30, 40, 50]


NOTE :- A list contains the Hetrogenius data like int , float and strings types etc :- 
------------------------------------------------------------------------------------------
Ex :- 

list1 = [100,'Rajesh','Forsk',-110,20.5]

list1[1] # 'Rajesh'

list1[3] # -110

NOTE :- A list may contains duplicate values means duplicates are allowed into list :- 
--------------------------------------------------------------------------------------
Ex :- 
list1 = [10,20,30,10,50,70,20]

list1[1] # 20

list1[-1]  # 20


NOTE :- In Python lists are Mutable or Changable Means we can modify on the existing lists :-
---------------------------------------------------------------------------------------------
Ex :-

list1 = [10,20,90,80,30,50,100]

print(len(list1)) # 7

list1.append(550) # append() method added a new value to list at end always.

print(list1) # [10, 20, 30, 10, 50, 70, 20, 550]

print(len(list1)) # 8

list1.remove(50)

print(list1) # [10, 20, 30, 10, 70, 20, 550]

print(len(list1)) # 7


NOTE :- We can Changes any items to list like this also :- 
-------------------------------------------------------
Ex :- 
list1 = [10,20,'forsk',40,50]

list1[2] = 'Rajesh' # [10, 20, 'Rajesh', 40, 50]

list1[-1] = 2020 # [10, 20, 'Rajesh', 40, 2020]


NOTE :- Loop Through a List :- 
------------------------------
Ex :- 
list1 = [10,20,'forsk',40,50]

for item in list1:
    print(item)
-------------
10
20
forsk
40
50

NOTE :- Check if Item Exists :-  We should use the 'in' keyword to find it.
-----------------------------
Ex :- 
list1 = [10,20,'forsk',40,50]

for item in list1:
    if item == 'forsk':
        print('Yes!! Its available :',item)
--------- Result ---------------
Yes!! Its available : forsk


NOTE :- Join Two Lists :- 
-------------------------
Ex :- 
list1 = [10,20,30,40]

list2 = [90,'Rajesh',100]

list3 = list1 + list2 

print(list3) # [10, 20, 30, 40, 90, 'Rajesh', 100]

NOTE :- Another way to join two lists are by appending all the items from list2 into list1, one by one.

Ex :- 
list1 = [10,'sharma',30,40]

list2 = [90,'Rajesh','forsk']

for item in list2:
    list1.append(item)
    
print(list1)
--------- Result ---------------
[10, 'sharma', 30, 40, 90, 'Rajesh', 'forsk']
    

NOTE :- We can use the extend() method, which purpose is to add elements from one list to 
another list.

If we append one to another list we will be getting the output like this to avoid we
will be using the extend() method to join two lists.

Ex :- 

list1 = [10,200,30,'Usha']

list2 = [90,'Rajesh',1001]

list1.append(list2)
print(list1)
---- Result -----
[10, 200, 30, 'Usha', [90, 'Rajesh', 1001]] # We don't need output like this.

list1.extend(list2)
print(list1)
---- Result -----
[10, 200, 30, 'Usha', 90, 'Rajesh', 1001]


NOTE :- We have list() constructor to convert into list data types.
Ex :- 

t1 = ('Rajesh',10,20,50,'forsk')
print(type(t1))
list1 = list(t1)
print(type(list1))
print(list1)
--------- Result ----------------
<class 'tuple'>
<class 'list'>
['Rajesh', 10, 20, 50, 'forsk']


NOTE :- Copy a List :- 
-----------------------
Ex :- 

list1 = [10,200,30,'Usha']

list2 = list1

print(list1) # [10, 200, 30, 'Usha']

print(list2) # [10, 200, 30, 'Usha']

list1.append('Rajesh')

print(list1) # [10, 200, 30, 'Usha','Rajesh']

print(list2) # [10, 200, 30, 'Usha','Rajesh']

list2.append('Parents')

print(list1) # [10, 200, 30, 'Usha','Rajesh','Parents']

print(list2) # [10, 200, 30, 'Usha','Rajesh','Parents']

# Copy making
list3 = list1.copy()
print(list3) # [10, 200, 30, 'Usha', 'Rajesh', 'Parents']

list3.append('sharma')

print(list1) # [10, 200, 30, 'Usha', 'Rajesh', 'Parents'] # No changes made into Actual list.

print(list3) # [10, 200, 30, 'Usha', 'Rajesh', 'Parents', 'sharma']

list3.insert(1,'Babudaya')

print(list1) # [10, 200, 30, 'Usha', 'Rajesh', 'Parents'] # No changes made into Actual list.

print(list3) # [10, 'Babudaya', 200, 30, 'Usha', 'Rajesh', 'Parents', 'sharma']


---------------------------------------------------------------------------------------------------------
'''
List Methods :- 
--------------
Python has a set of built-in methods that you can use on lists.
'''
Method	Description
1) append()	----> Adds an element at the end of the list
2) clear()	----> Removes all the elements from the list
3) copy()	----> Returns a copy of the list
4) count()	----> Returns the number of elements with the specified value
5) extend()	----> Add the elements of a list (or any iterable), to the end of the current list
6) index()	----> Returns the index of the first element with the specified value
7) insert()	----> Adds an element at the specified position
8) pop()	----> Removes the element at the specified position
9) remove()	----> Removes the item with the specified value
10) reverse()	----> Reverses the order of the list
11) sort()	----> Sorts the list

Examples :- 
---------
1) append() :- 
-------------
Ex :-     
list1 = [10,20,30,'Rajesh']
list1.append('sharma')
print(list1)
----- Result -----
[10, 20, 30, 'Rajesh', 'sharma']


list1.append(2020)
print(list1)
----- Result -----
[10, 20, 30, 'Rajesh', 'sharma', 2020]

-------------------------------------------------------------------------------------------
2) clear() :- 
--------------
Ex :- 
list1 = [10,20,30,'Rajesh']
list1.clear()
print('This is Empty list :', list1)
list1.append('Rajesh-sharma')
print('Now we have 1 value to empty list :', list1)
----- Result ---------------------
This is Empty list : []
Now we have 1 value to empty list : ['Rajesh-sharma']

-------------------------------------------------------------------------------------------------
3) copy() :- 
-------------
Ex :-
list1 = [10,20,'Forsk','School']
list2 = list1
print(list1) # [10, 20, 'Forsk', 'School']
print(list2) # [10, 20, 'Forsk', 'School']

NOTE :- If we make any changes into any of the list then automatically it will be refelect
list also pls check the below example.

list2.append(100)
print(list1) # [10, 20, 'Forsk', 'School', 100]
print(list2) # [10, 20, 'Forsk', 'School', 100]

list1.insert(1,'Rajesh')
print(list1) # [10, 'Rajesh', 20, 'Forsk', 'School', 100]
print(list2) # [10, 'Rajesh', 20, 'Forsk', 'School', 100]

NOTE :- If we do any copy of the original list and perform some operations like above.
Ex :- 

list1 = [10,20,'Forsk','School']
list3 = list1.copy()
print(list1) # [10, 20, 'Forsk', 'School']
print(list3) # [10, 20, 'Forsk', 'School']

list3.append(2020)
print(list3) # [10, 20, 'Forsk', 'School', 2020]
print(list1) # [10, 20, 'Forsk', 'School']

list1.insert(0,'Usha')
print(list1) # ['Usha', 10, 20, 'Forsk', 'School']
print(list3) # [10, 20, 'Forsk', 'School', 2020]

---------------------------------------------------------------------------------------------------------
4) count() :- 
-------------
Ex :- 
list1 = [10,20,'Forsk','School','Forsk']
print(list1.count('Forsk')) # 2

Ex :- 
list1 = [10,20,30,40,20,45,60,20,100]
print(list1.count(20)) # 3
list1.append(20)
print(list1.count(20))  # 4

---------------------------------------------------------------------------------------------------------
5) extend() :-
-------------    
Ex :- 
list1 = [1,2,3,4,'Forsk-guys']
list2 = [10,20,'Rajesh','Sandeep']
list1.extend(list2)
print(list1)
------------ Result -----------
[1, 2, 3, 4, 'Forsk-guys', 10, 20, 'Rajesh', 'Sandeep']

----------------------------------------------------------------------------------------------------
6) index() :-
-------------    
Ex :- 
list1 = [10,20,'Rajesh','sharma',101]
list1.index('sharma') # 3
list1.index(20) # 1

---------------------------------------------------------------------------------------------------------
7) insert() :- 
--------------
Ex :- 
    
list1 = [10,20,'Rajesh','sharma',101]
list1.insert(-1,'Forsk-school')
print(list1) # [10, 20, 'Rajesh', 'sharma', 'Forsk-school', 101]

list1.insert(0,2020)
print(list1) # [2020, 10, 20, 'Rajesh', 'sharma', 'Forsk-school', 101]

--------------------------------------------------------------------------------------------
8) pop() :- 
-----------
Ex :- 
list1 = ['Rajesh',100,101,401,'Forsk']
list1.pop()
print(list1) # ['Rajesh', 100, 101, 401]

list1.pop(0)
print(list1) # [100, 101, 401]
--------------------------------------------------------------------------------------------
9) remove() :- 
-----------------
Ex :- 
list1 = ['Forsk-people',101,102,202,2020]
list1.remove('Forsk-people')
print(list1) # [101, 102, 202, 2020]

list1.remove(202)
print(list1) # [101, 102, 2020]

list1 = ['Forsk-people',101,102,202,2020]
for i in list1:
    if i == 202:
        list1.remove(i)
print(list1)    
---------- Result ---------
['Forsk-people', 101, 102, 2020]

----------------------------------------------------------------------------------------------
10) reverse() :- 
---------------
Ex :- 

list1 = [10,20,'Usha',200,'Rajesh']
list1.reverse()
print(list1)   # ['Rajesh', 200, 'Usha', 20, 10]

list1.append(2020) # ['Rajesh', 200, 'Usha', 20, 10, 2020]
list1.reverse()
print(list1) # [2020, 10, 20, 'Usha', 200, 'Rajesh']

----------------------------------------------------------------------------------------------------
11) sort() :- 
-----------
Ex :- 

list1 = [101,501,10,51,21,5]
list1.sort()
print(list1) # [5, 10, 21, 51, 101, 501]

list1 = ['Rajesh','Sharma','Forsk','Jaipur']
list1.sort()
print(list1) # ['Forsk', 'Jaipur', 'Rajesh', 'Sharma']


list1 = ['Zombie-guys','Rajesh',101,501,-90,0]

list1.sort() # It will not supported b/w int & str.
print(list1)

list1 = ['Zombie-guys','Rajesh','Apple','Cunt']
list1.sort()
print(list1) # ['Apple', 'Cunt', 'Rajesh', 'Zombie-guys']

