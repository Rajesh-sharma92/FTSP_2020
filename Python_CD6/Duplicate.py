# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:32:23 2020

@author: Rajesh
"""
"""
Name: 
    Duplicate       
Filename:
    Duplicate.py 
Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values with original 
    order reserved.
"""

list1= [12,24,35,24,88,120,155,88,120,155]

l1=set(list1)

print(l1)


 ###### OR ############
 
list1 = [12,24,35,24,88,120,155,88,120,155]
 
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)
        
     
 ######### OR ###########

l1 = input('Enter some of the numbers :')

l2 = l1.split()

for i in l2:
    
    b=l2.count(i)
    
    for j in range(1,b):
        
        l2.remove(i)
 
print(l2)

a=sorted(l2)      

print(a)









 