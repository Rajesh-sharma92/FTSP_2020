# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:57:51 2020

@author: Rajesh
"""

"""
Name: 
    Unlucky 13         
Filename:
    unlucky.py
Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user
Sample Input:
    13, 1, 2, 13, 2, 1, 13 
Sample Output:
    3 
"""   

# list1 = [13,1,2,13,2,1,13]

list1 = [13,1,20,13,2,30,13]

i = 0

sum_list = 0

while(i<len(list1)):
    
    if list1[i] == 13:
        
        i = i + 2
        
    else:
        
        sum_list = sum_list + list1[i]
        
        i = i + 1
        
        
print(sum_list)
        
        
        