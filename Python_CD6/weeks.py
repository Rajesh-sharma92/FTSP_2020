# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:01:28 2020

@author: Rajesh
"""

"""
Name: 
    weeks       
Filename:
    weeks.py 
Problem Statement:
    Write a program that adds missing days to existing tuple of days 
Sample Input:
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
Sample Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
""" 

t = ('Monday', 'Wednesday', 'Thursday', 'Saturday')

l1=list(t) # Now Tuple will be converted into list and then we will be appending some of the values into it.

print('The tuple becomes into List : ', l1)            
            
l1.append('Tuesday')
l1.append('Friday')
l1.append('Sunday')

print('The List after Adding some missing Items are :', l1)

t1 = tuple(l1)

sorted(t1)

print('The final output will be in Tuple only :', t1)


 ########### OR ##############
 
tuple = (10,20,30,40,50)

type(t)

list1 = list(tuple) # Now Tuple will be converted into list and then we will be appending some of the values into it.

print(list1)

list1.append(100)
list1.append(250)
list1.append(350)

print(list1)

for i in list1:
    list2 = list1.count(i)
    i+=1
print(list1)

list1.index(100)
list1.index(30)

list1.insert(5,0)
list1.insert(0,7)
list1.insert(2,450)
list1.remove(6) # We need to pass the particular element in list not index number. [ NOT Valid ]

list1.remove(0)

list1.pop()
print(list1)

list1.append(7)

list1.index(20)
list1.pop(3)

print(list1)

list2 = []  # Empty list.

print(list2) # It will be printing empty list.

list2.clear() # It is used to clear all the data from the list2.

print(list2) 

list2.extend(list1) # It will be combining both lists each other.

list2.append(list1) # It will be combining list2 then whole list1 full without removing [] bracket like single character.

list1.sort()

list1.reverse()






print(type(t))

print(t)

print(t[0])

print(t[3])

print(t[-1])

print(t[:2])

t=() # Data type is empty tuple

t=(10,) # Single value tuple value always ends with comma ( ,).

