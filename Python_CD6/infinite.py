# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:48:35 2020

@author: Rajesh
"""
"""
Name:
    Infinite input
Filename: 
    infinite.py    
Problem Statement:
    Write a program that asks the user, again and again, to enter a number.
    When the user enters an empty string, then stop asking for additional inputs.
    Along the way, as the user is entering numbers, 
    I want you to store those numbers in a list. 
    I also want you to keep track of the minimum and maximum values that you've seen so far.
    When the user has finished entering numbers, your program should print out:
         The sum of these numbers
         The average (mean) of these numbers
         The largest and smallest numbers you received from the user
"""

import statistics
list1=[]
while(True):
    
    num=input('Enter some of the numbers :')
    
    if not num:
        
        print('The Inserted elements into the list are :', sorted(list1))
        print('The Sum of Inputs :',sum(list1))
        print('The Max of Inputs :',max(list1))
        print('The Min of Inputs :',min(list1))
        print('The Mean of Inputs :',statistics.mean(list1))
        
        break
    num1=int(num)
    list1.append(num1)
    
print("List of entered input is: ",list1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
