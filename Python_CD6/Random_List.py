# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 07:34:22 2020

@author: Rajesh
"""
"""
Name: 
    2 Dimensional Random List         
Filename:
    random_list.py
Problem Statement:
    Create a 2-Dimensional list of list of integers 10 by 10.
    Fill the 2-Dimensional list with random numbers in the range 0 to 255
    Display the array on the screen showing the numbers.
    
"""

import random

list1=[]

list2=[]

for i in range(10):
    
    for j in range(10):
        
        list1.append(random.randint(0,255))
        
        
        list2.append(list1)
       
       # list2.append(list1.copy())
        
        list1.clear()
        
        print(list2)
        
        
        
        
        
        
        