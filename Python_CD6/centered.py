# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:32:17 2020

@author: Rajesh
"""

"""
Name: 
    Centered Average         
Filename:
    centered.py
Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is the 
    mean average of the values, except ignoring the largest and smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. Use int division to produce the final average. 
    You may assume that the array is length 3 or more.
    Take input from user
Sample Input:
    1, 2, 3, 4, 100 
Sample Output:
    3 
"""   

list2 = [] # Empty list.

n = input('Enter n value : ').split()

for i in n:
    
    i = int(i) # Type Casting from str to int.
    
    list2.append(i)

list2 = sorted(list2)

list2.remove(min(list2))

list2.remove(max(list2))

sum1= sum(list2)

length = len(list2)

Avg= (sum1/length)

print('Average :', Avg)




