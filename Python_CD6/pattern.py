# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 08:14:22 2020

@author: Rajesh
"""

"""
Code Challenge
Name: 
    Pattern Builder
Filename: 
    pattern.py
Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  

Sample Input: 
    5
Sample Output:
    Below is the output of execution of this program.
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 
    * 
"""


n = int(input('Enter n value :'))

for i in range(n):
    
    print('* ' *(i+1) , (' ' *(n-i-1)))
    
for i in range(n-1):
    
    print('* '*(n-i-1) , (' ' *(i+1)))
        

